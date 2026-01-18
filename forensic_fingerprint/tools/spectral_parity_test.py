#!/usr/bin/env python3
"""Spectral parity / RS-consistency test on Planck CMB alms.

This tool implements:
- Symbolization of phases into GF(256) symbols
- RS(255,201) Hamming validity rate proxy
- Prime-gated purity test across ell shells
- Permutation p-values for delta mean(P - C)
- Optional Gaussian weighting around a prime cluster
- Optional phase-shear compensation and phase-shear scans

CLI entry:
  python3 -m forensic_fingerprint.tools.spectral_parity_test ...

Notes:
- This script intentionally avoids scipy; Fisher p-value combination uses an
  exact survival function for chi-square with even df.
"""

from __future__ import annotations

import argparse
import csv
import math
import os
import sys
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np

try:
    import healpy as hp
except Exception as e:  # pragma: no cover
    hp = None
    _HEALPY_IMPORT_ERROR = e
else:
    _HEALPY_IMPORT_ERROR = None

# Optional progress bar
try:
    from tqdm import tqdm
except Exception:  # pragma: no cover
    tqdm = None

# ---------------------------------------------------------------------
# Fisher meta-analysis utilities (no scipy)
# ---------------------------------------------------------------------


def _chi2_sf_even_df(x: float, df: int) -> float:
    """
    Survival function for Chi-square with even degrees of freedom.

    Fisher:
      X = -2 * sum(log p_i)  ~  chi2(df=2k).
    For df = 2k (k integer), chi-square is Gamma(k, theta=2) and:
      SF(x) = exp(-x/2) * sum_{j=0..k-1} (x/2)^j / j!
    """
    if df <= 0 or (df % 2) != 0:
        raise ValueError("df must be a positive even integer")
    if x <= 0:
        return 1.0
    k = df // 2
    t = x / 2.0
    # sum_{j=0}^{k-1} t^j/j!
    s = 0.0
    term = 1.0
    for j in range(k):
        if j == 0:
            term = 1.0
        else:
            term *= t / float(j)
        s += term
    return float(math.exp(-t) * s)


def combine_pvalues_fisher(pvals: Sequence[float]) -> float:
    """
    Combine independent p-values using Fisher's method.
    Returns combined p-value.

    X = -2 Σ log(p_i) ~ χ²(df=2k)
    """
    cleaned: List[float] = []
    for p in pvals:
        if p is None:
            continue
        p = float(p)
        if not (0.0 < p <= 1.0):
            continue
        cleaned.append(p)
    if not cleaned:
        return float("nan")
    x = -2.0 * float(np.sum(np.log(np.array(cleaned, dtype=float))))
    df = 2 * len(cleaned)
    return _chi2_sf_even_df(x, df)


# ---------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------


def _safe_mean(x: np.ndarray) -> float:
    """NaN-safe mean. Returns NaN if there are no finite values."""
    x = np.asarray(x, dtype=float)
    m = np.isfinite(x)
    if not np.any(m):
        return float("nan")
    return float(np.mean(x[m]))


def _safe_div(num: float, den: float) -> float:
    """Safe division with NaN/Inf/zero guards."""
    num = float(num)
    den = float(den)
    if not np.isfinite(num) or not np.isfinite(den) or den == 0.0:
        return float("nan")
    return float(num / den)


def debug_symbols(symbols: np.ndarray, *, label: str = "", max_show: int = 20) -> Dict[str, object]:
    """Print and return basic diagnostics for a uint8 symbol stream."""
    out: Dict[str, object] = {"label": label}
    if symbols is None:
        out.update({"ok": False, "reason": "symbols is None"})
        print(f"[DEBUG] {label} symbols=None", flush=True)
        return out

    s = np.asarray(symbols)
    out["dtype"] = str(s.dtype)
    out["size"] = int(s.size)
    if s.size == 0:
        out.update({"ok": False, "reason": "empty symbols"})
        print(f"[DEBUG] {label} empty symbols", flush=True)
        return out

    # Basic stats (cast to float for safety)
    sf = s.astype(np.float64, copy=False)
    out["min"] = float(np.nanmin(sf))
    out["max"] = float(np.nanmax(sf))
    out["mean"] = float(np.nanmean(sf))
    out["std"] = float(np.nanstd(sf))

    # Unique count on a sample (avoid huge unique() cost)
    sample = s if s.size <= 200_000 else s[:200_000]
    uniq = np.unique(sample)
    out["unique_count_sample"] = int(uniq.size)
    out["unique_head"] = uniq[: min(10, uniq.size)].tolist()

    preview = s[:max_show]
    print(
        f"[DEBUG] {label} symbols: dtype={out['dtype']} n={out['size']} "
        f"min={out['min']:.3g} max={out['max']:.3g} mean={out['mean']:.3g} std={out['std']:.3g} "
        f"unique(sample)={out['unique_count_sample']}",
        flush=True,
    )
    try:
        print(f"[DEBUG] {label} first[{max_show}]: {preview.tolist()}", flush=True)
    except Exception:
        print(f"[DEBUG] {label} first[{max_show}]: {preview}", flush=True)

    collapsed = (out["unique_count_sample"] <= 1) or (out["std"] == 0.0)
    out["collapsed"] = bool(collapsed)
    out["ok"] = not collapsed
    if collapsed:
        out["reason"] = "digital collapse: symbols nearly constant"
        print(f"[WARN] {label} DIGITAL COLLAPSE: symbols nearly constant", flush=True)
    return out


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if (n % 2) == 0:
        return False
    r = int(math.isqrt(n))
    f = 3
    while f <= r:
        if (n % f) == 0:
            return False
        f += 2
    return True


def primes_in_range(lmin: int, lmax: int) -> List[int]:
    return [ell for ell in range(lmin, lmax + 1) if is_prime(ell)]


def _rng(seed: Optional[int]) -> np.random.Generator:
    return np.random.default_rng(seed)


def _ensure_healpy():
    if hp is None:
        raise RuntimeError(
            "healpy import failed. Install healpy or run with --tt-alm/--e-alm/--b-alm. "
            f"Original error: {_HEALPY_IMPORT_ERROR}"
        )


# ---------------------------------------------------------------------
# RS proxy via Hamming validity rate
# ---------------------------------------------------------------------

# RS(255,201) has 54 parity symbols; we are not decoding.
# We use a fast proxy: treat each 255-symbol block, compute a simple parity-like
# check using a fixed generator table approximation. This is a forensic signal,
# not a communication-grade decoder.

# NOTE: this proxy is deterministic; do not interpret as a true RS decoder.


def _hamming_valid_rate_uint8(block: np.ndarray) -> float:
    """
    Proxy "validity" score for a 255-length uint8 block.
    Returns fraction of positions that match a deterministic checksum-like rule.

    This is intentionally simple and fast; it creates a consistent integrity
    statistic to compare across shells and perturbations.
    """
    # Fixed pseudo-check: checksum of first 201 symbols compared to last 54
    # using rolling XOR and rotation; returns a pseudo "syndrome match rate".
    if block.dtype != np.uint8:
        block = block.astype(np.uint8, copy=False)
    if block.size != 255:
        raise ValueError("block must have length 255")
    data = block[:201]
    parity = block[201:]

    # rolling checksum
    acc = np.uint8(0)
    chk = np.empty(54, dtype=np.uint8)
    for i in range(201):
        # rotate left by 1 (in 8-bit space) and xor
        acc = np.uint8(((int(acc) << 1) & 0xFF) | ((int(acc) >> 7) & 0x01))
        acc ^= data[i]
        if i < 54:
            chk[i] = acc
        else:
            # spread influence
            chk[i % 54] ^= acc

    # compare checksum to parity; score is match fraction
    return float(np.mean(chk == parity))


def hamming_valid_rate_fast(symbols: np.ndarray) -> float:
    """
    Compute mean validity rate over all 255-length frames in the 1D symbol stream.
    """
    if symbols.dtype != np.uint8:
        symbols = symbols.astype(np.uint8, copy=False)
    n = symbols.size
    if n < 255:
        return float("nan")
    n_frames = n // 255
    if n_frames <= 0:
        return float("nan")
    s = 0.0
    for i in range(n_frames):
        blk = symbols[i * 255 : (i + 1) * 255]
        s += _hamming_valid_rate_uint8(blk)
    return float(s / n_frames)


def tail_rate_ge_k(x: np.ndarray, k: int = 8) -> float:
    """Tail probability proxy: fraction of values >= k."""
    return float(np.mean(np.asarray(x) >= k))


# ---------------------------------------------------------------------
# Symbol stream and slicing utilities
# ---------------------------------------------------------------------


def ell_shell_slice(ell: int) -> slice:
    """
    Return slice into the linearized (ell,m) stream for a given ell,
    using k = ell^2 + ell + m with m in [-ell, +ell].

    In the linear stream where we concatenate shells by increasing ell:
      shell length = 2*ell + 1
    We use offsets:
      start = ell^2
      end   = (ell+1)^2
    because sum_{j=0}^{ell-1} (2j+1) = ell^2.
    """
    start = ell * ell
    end = (ell + 1) * (ell + 1)
    return slice(start, end)


def phase_to_symbol(phi: np.ndarray) -> np.ndarray:
    """
    Map phase in [-pi,pi] to uint8 symbols [0,255] by linear mapping.
    """
    # map to [0,1)
    # Guard against NaN/Inf propagating into a collapsed or empty symbol stream.
    phi = np.asarray(phi, dtype=np.float64)
    if not np.all(np.isfinite(phi)):
        phi = np.nan_to_num(phi, nan=0.0, posinf=0.0, neginf=0.0)
    u = (phi + np.pi) / (2.0 * np.pi)
    u = np.mod(u, 1.0)
    sym = np.floor(u * 256.0).astype(np.int32)
    sym = np.clip(sym, 0, 255).astype(np.uint8)
    return sym


@dataclass
class Symbols:
    """
    Simple container that behaves like a 1D numpy array of uint8 symbols,
    but can carry metadata and be optionally transformed (phase shear).
    """

    arr: np.ndarray  # uint8 1D
    ells: np.ndarray  # int 1D, same length as arr

    def __post_init__(self):
        if self.arr.dtype != np.uint8:
            self.arr = self.arr.astype(np.uint8, copy=False)
        if self.arr.ndim != 1:
            self.arr = np.ravel(self.arr)
        if self.ells.ndim != 1:
            self.ells = np.ravel(self.ells)
        if self.arr.shape != self.ells.shape:
            raise ValueError("Symbols: arr and ells must have same shape")

    def __len__(self) -> int:
        return int(self.arr.size)

    def __getitem__(self, key):
        return self.arr[key]


def symbols_from_alm_phase(
    alm: np.ndarray,
    lmax: int,
    *,
    differential: bool = False,
    dither_amp: float = 0.0,
    rng: Optional[np.random.Generator] = None,
) -> Symbols:
    """
    Build symbol stream from a_{ell m} complex alm array.
    """
    # healpy alm ordering: packed; use hp.Alm.getlm
    _ensure_healpy()
    ell, m = hp.Alm.getlm(lmax, np.arange(hp.Alm.getsize(lmax)))
    phi = np.arctan2(np.imag(alm), np.real(alm))

    # Optional: tiny phase dither (in radians) to prevent quantization lock-in.
    # Typical safe values are ~1e-4 .. 1e-3 rad; default is off.
    if dither_amp and float(dither_amp) > 0.0:
        if rng is None:
            rng = np.random.default_rng(0)
        phi = phi + (rng.random(size=phi.shape) - 0.5) * float(dither_amp)

    # Optional: differential phase (DPSK-style), robust to global phase drift.
    if bool(differential):
        # Use delta between consecutive alm samples in healpy packing.
        # This is not "adjacent m" guaranteed, but is still a useful robustness check.
        phi = np.mod(np.diff(phi, prepend=phi[0]), 2.0 * np.pi) - np.pi

    sym = phase_to_symbol(phi)
    # Build linearized stream by ell shells:
    # We want stream ordered by ell shells and m increasing.
    # healpy getlm already gives ell,m by index, but not contiguous by ell^2 scheme.
    # We'll place symbols into positions using start=ell^2 + (m+ell).
    n_stream = (lmax + 1) * (lmax + 1)
    arr = np.zeros(n_stream, dtype=np.uint8)
    ells = np.zeros(n_stream, dtype=np.int32)
    for i in range(sym.size):
        e = int(ell[i])
        mm = int(m[i])
        k = e * e + e + mm  # since mm in [-e,+e]
        arr[k] = sym[i]
        ells[k] = e
    return Symbols(arr=arr, ells=ells)


def apply_phase_shear(
    sym: Symbols,
    theta_deg: float,
    mode: str = "k",
) -> Symbols:
    """
    Apply a deterministic phase-shear compensation to the symbol stream.

    This is implemented as a phase offset that depends linearly on:
      mode='k'  : stream index k
      mode='ell': multipole ell

    We don't have original phases anymore (we have symbols).
    We approximate by rotating symbols in phase space:
      symbol -> symbol + round(256 * theta/(2pi) * f)
    where f is k-normalized or ell-normalized.

    The purpose is to "de-skew" a consistent linear drift.
    """
    if abs(theta_deg) < 1e-15:
        return sym
    theta = float(theta_deg) * np.pi / 180.0
    # convert radians to symbol offset per unit f:
    # 2pi corresponds to 256 symbols.
    scale = 256.0 / (2.0 * np.pi) * theta

    arr = sym.arr.astype(np.int16, copy=True)

    if mode == "k":
        # normalize k to [0,1] across stream
        k = np.arange(arr.size, dtype=np.float64)
        f = (k - k.min()) / (k.max() - k.min() + 1e-12)
    elif mode == "ell":
        e = sym.ells.astype(np.float64)
        f = (e - e.min()) / (e.max() - e.min() + 1e-12)
    else:
        raise ValueError("phase-shear mode must be 'k' or 'ell'")

    offset = np.rint(scale * f).astype(np.int16)
    arr = (arr + offset) & 0xFF
    out = Symbols(arr=arr.astype(np.uint8), ells=sym.ells.copy())
    return out


# ---------------------------------------------------------------------
# Prime-gated integrity curve and permutation stats
# ---------------------------------------------------------------------


def shell_hamming_integrity(symbol_stream: Symbols, ell: int) -> float:
    sl = ell_shell_slice(ell)
    return hamming_valid_rate_fast(symbol_stream[sl])


def prime_gated_integrity_curve(
    symbol_stream: Symbols,
    lmin: int,
    lmax: int,
) -> Tuple[np.ndarray, np.ndarray]:
    ells = np.arange(lmin, lmax + 1, dtype=np.int32)
    integrity = np.zeros_like(ells, dtype=np.float64)
    for i, ell in enumerate(ells):
        integrity[i] = shell_hamming_integrity(symbol_stream, int(ell))
    return ells.astype(np.int32), integrity.astype(np.float64)


def prime_gated_delta_mean(ells: np.ndarray, integrity: np.ndarray) -> float:
    p = integrity[[is_prime(int(e)) for e in ells]]
    c = integrity[[not is_prime(int(e)) for e in ells]]
    # Many ells may yield NaN integrity if the slice is shorter than 255.
    # Use finite-only means to prevent NaN cascades.
    p = p[np.isfinite(p)]
    c = c[np.isfinite(c)]
    if p.size == 0 or c.size == 0:
        return float("nan")
    return float(np.mean(p) - np.mean(c))


def prime_gated_delta_mean_weighted(
    ells: np.ndarray,
    integrity: np.ndarray,
    weights: np.ndarray,
) -> float:
    if ells.shape != integrity.shape or ells.shape != weights.shape:
        raise ValueError("ells, integrity, weights must have same shape")
    mask_p = np.array([is_prime(int(e)) for e in ells], dtype=bool)
    mask_c = ~mask_p
    if not np.any(mask_p) or not np.any(mask_c):
        return float("nan")
    wp = weights[mask_p]
    wc = weights[mask_c]
    ip = integrity[mask_p]
    ic = integrity[mask_c]
    # finite-only (keep weights aligned)
    fp = np.isfinite(ip)
    fc = np.isfinite(ic)
    ip = ip[fp]
    wp = wp[fp]
    ic = ic[fc]
    wc = wc[fc]
    mp = float(np.sum(wp * ip) / (np.sum(wp) + 1e-18))
    mc = float(np.sum(wc * ic) / (np.sum(wc) + 1e-18))
    return mp - mc


def prime_gated_permutation_pvalue(
    ells: np.ndarray,
    integrity: np.ndarray,
    w_h: Optional[np.ndarray],
    n_perm: int,
    rng: np.random.Generator,
) -> float:
    """
    Two-sided permutation p-value by shuffling the prime/composite labels.
    If w_h is given, uses weighted delta.
    """
    if n_perm <= 0:
        return float("nan")

    mask_p = np.array([is_prime(int(e)) for e in ells], dtype=bool)
    if not np.any(mask_p) or np.all(mask_p):
        return float("nan")

    if w_h is None:
        obs = prime_gated_delta_mean(ells, integrity)
    else:
        obs = prime_gated_delta_mean_weighted(ells, integrity, w_h)

    # If obs is NaN (e.g., not enough 255-symbol frames in shells), bail out
    if not np.isfinite(obs):
        return float("nan")

    # Permute labels by shuffling mask
    cnt = 0
    for _ in range(n_perm):
        perm = rng.permutation(mask_p)
        if w_h is None:
            p = integrity[perm]
            c = integrity[~perm]
            # finite-only
            p = p[np.isfinite(p)]
            c = c[np.isfinite(c)]
            if p.size == 0 or c.size == 0:
                continue
            d = float(np.mean(p) - np.mean(c))
        else:
            wp = w_h[perm]
            wc = w_h[~perm]
            ip = integrity[perm]
            ic = integrity[~perm]
            # finite-only (keep weights aligned)
            fp = np.isfinite(ip)
            fc = np.isfinite(ic)
            ip = ip[fp]
            wp = wp[fp]
            ic = ic[fc]
            wc = wc[fc]
            if ip.size == 0 or ic.size == 0:
                continue
            mp = float(np.sum(wp * ip) / (np.sum(wp) + 1e-18))
            mc = float(np.sum(wc * ic) / (np.sum(wc) + 1e-18))
            d = mp - mc
        if abs(d) >= abs(obs):
            cnt += 1
    # add-one smoothing
    return float((cnt + 1) / (n_perm + 1))


def gaussian_weights_for_ell(
    ells: np.ndarray, center: float, sigma: float
) -> np.ndarray:
    if sigma <= 0:
        raise ValueError("sigma must be > 0 for gaussian weights")
    x = (ells.astype(np.float64) - float(center)) / float(sigma)
    w = np.exp(-0.5 * x * x)
    # normalize to mean ~1 (optional, keeps scale stable)
    w = w / (np.mean(w) + 1e-18)
    return w.astype(np.float64)


# ---------------------------------------------------------------------
# Phase randomization MC on alms
# ---------------------------------------------------------------------


def randomize_phases_per_ell(alm: np.ndarray, lmax: int, rng: np.random.Generator) -> np.ndarray:
    """
    Phase randomize a_{ell m} per ell shell, preserving amplitude.
    """
    _ensure_healpy()
    out = alm.copy()
    ell, m = hp.Alm.getlm(lmax, np.arange(hp.Alm.getsize(lmax)))
    for e in range(lmax + 1):
        idx = np.where(ell == e)[0]
        if idx.size == 0:
            continue
        amp = np.abs(out[idx])
        # random uniform phases
        ph = rng.uniform(-np.pi, np.pi, size=idx.size)
        out[idx] = amp * (np.cos(ph) + 1j * np.sin(ph))
    return out


# ---------------------------------------------------------------------
# IO: maps and alms
# ---------------------------------------------------------------------


def read_map_field(map_path: str, field: int):
    _ensure_healpy()
    # healpy API compatibility: verbose argument may be removed in future
    try:
        m = hp.read_map(map_path, field=field, verbose=False)
    except TypeError:
        m = hp.read_map(map_path, field=field)
    return m


def read_tt_map(map_path: str):
    # Planck IQU: field=0 is I
    return read_map_field(map_path, field=0)


def read_qu_maps(q_path: str, u_path: str):
    _ensure_healpy()
    try:
        q = hp.read_map(q_path, field=0, verbose=False)
    except TypeError:
        q = hp.read_map(q_path, field=0)
    try:
        u = hp.read_map(u_path, field=0, verbose=False)
    except TypeError:
        u = hp.read_map(u_path, field=0)
    return q, u


def map_to_alm_tt(tt_map: np.ndarray, lmax: int) -> np.ndarray:
    _ensure_healpy()
    return hp.map2alm(tt_map, lmax=lmax, iter=3)


def map_to_alm_eb_from_qu(q: np.ndarray, u: np.ndarray, lmax: int) -> Tuple[np.ndarray, np.ndarray]:
    _ensure_healpy()
    # healpy API compatibility: iter parameter may not exist in some versions
    try:
        almE, almB = hp.map2alm_spin([q, u], spin=2, lmax=lmax, iter=3)
    except TypeError:
        almE, almB = hp.map2alm_spin([q, u], spin=2, lmax=lmax)
    return almE, almB


def load_alm(path: str) -> np.ndarray:
    _ensure_healpy()
    return hp.read_alm(path)


# ---------------------------------------------------------------------
# Metrics: RS proxy summary on stream
# ---------------------------------------------------------------------


def rs_mean_zero_proxy(symbols: np.ndarray) -> float:
    """
    Proxy statistic: mean number of "zero-ish" symbols per frame.
    Here defined as count(symbol == 0) in each 255 block, then mean.
    """
    if symbols.dtype != np.uint8:
        symbols = symbols.astype(np.uint8, copy=False)
    n = symbols.size // 255
    if n <= 0:
        return float("nan")
    x = []
    for i in range(n):
        blk = symbols[i * 255 : (i + 1) * 255]
        x.append(int(np.sum(blk == 0)))
    return float(np.mean(x))


def rs_tail_rate_proxy(symbols: np.ndarray, tail_k: int = 8) -> float:
    """
    Proxy tail rate: P(count(symbol==0) >= tail_k) over frames.
    """
    if symbols.dtype != np.uint8:
        symbols = symbols.astype(np.uint8, copy=False)
    n = symbols.size // 255
    if n <= 0:
        return float("nan")
    x = []
    for i in range(n):
        blk = symbols[i * 255 : (i + 1) * 255]
        x.append(int(np.sum(blk == 0)))
    return tail_rate_ge_k(np.array(x, dtype=int), k=tail_k)


def print_observed_scores(label: str, sym: Symbols, tail_k: int):
    hr = hamming_valid_rate_fast(sym.arr)
    rz = rs_mean_zero_proxy(sym.arr)
    rt = rs_tail_rate_proxy(sym.arr, tail_k=tail_k)
    print(f"{label}: hamming_rate={hr:.6f}  rs_mean_zero={rz:.3f}  rs_tail_rate(>={tail_k})={rt:.6f}", flush=True)


# ---------------------------------------------------------------------
# Plotting helpers (optional)
# ---------------------------------------------------------------------


def _maybe_import_matplotlib():
    try:
        import matplotlib.pyplot as plt
    except Exception:
        return None
    return plt


def save_prime_plot(prefix: str, chan: str, ells: np.ndarray, integ: np.ndarray, highlight: Optional[int] = None):
    plt = _maybe_import_matplotlib()
    if plt is None:
        return
    os.makedirs(os.path.dirname(prefix), exist_ok=True) if os.path.dirname(prefix) else None
    out = f"{prefix}_{chan}_prime_purity.png"
    plt.figure()
    plt.plot(ells, integ, marker="o", linestyle="-")
    if highlight is not None:
        try:
            idx = int(np.where(ells == int(highlight))[0][0])
        except Exception:
            idx = None
        if idx is not None:
            plt.scatter([ells[idx]], [integ[idx]], s=60)
    plt.xlabel("ell")
    plt.ylabel("Hamming validity rate (proxy)")
    plt.title(f"Prime-Gated integrity curve ({chan})")
    plt.tight_layout()
    plt.savefig(out, dpi=160)
    plt.close()


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------


def build_arg_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        description=(
            "Spectral parity / RS-consistency test on Planck CMB.\n\n"
            "Workflow:\n"
            "  1) Obtain a_{\\ell m} coefficients (TT, and optionally EE/BB via Q/U).\n"
            "  2) Convert phases to 8-bit symbols in GF(256).\n"
            "  3) Compute RS-proxy integrity (Hamming validity rate) per 255-block.\n"
            "  4) Prime-Gated analysis: compare ell shells at primes vs composites.\n"
            "  5) Optional permutation p-value and phase-randomization MC.\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    ap.add_argument("--lmin", type=int, default=2)
    ap.add_argument("--lmax", type=int, default=256)

    ap.add_argument("--tt-map", type=str, default=None, help="FITS map for TT (field=0 for IQU).")
    ap.add_argument("--tt-alm", type=str, default=None, help="Input TT alm file (healpy .fits alm).")

    ap.add_argument("--q-map", type=str, default=None, help="FITS map for Q (single-field fits).")
    ap.add_argument("--u-map", type=str, default=None, help="FITS map for U (single-field fits).")

    ap.add_argument("--e-alm", type=str, default=None, help="Input E-mode alm file.")
    ap.add_argument("--b-alm", type=str, default=None, help="Input B-mode alm file.")

    ap.add_argument("--mc", type=int, default=1000, help="Monte Carlo count (phase randomization per ell). 0 disables.")
    ap.add_argument("--frame", type=int, default=None, help="If set, restrict symbol stream to a single 255 frame index.")
    ap.add_argument("--step", type=int, default=255, help="Frame size (default 255).")
    ap.add_argument("--max-frames", type=int, default=2048, help="Max number of frames to use from the stream.")
    ap.add_argument("--tail-k", type=int, default=8, help="Tail threshold for rs_tail_rate proxy.")

    ap.add_argument("--seed", type=int, default=0)

    ap.add_argument(
        "--debug-symbols",
        action="store_true",
        help="Print symbol-stream diagnostics (unique counts, preview) per channel.",
    )
    ap.add_argument(
        "--phase-dither-amp",
        type=float,
        default=0.0,
        help=(
            "Add tiny phase dither (radians) before quantization to avoid bin lock-in. "
            "Typical values: 1e-4..1e-3. Default 0 disables."
        ),
    )
    ap.add_argument(
        "--differential-phase",
        action="store_true",
        help="Use differential phase (DPSK-style) before quantization. Default off.",
    )

    ap.add_argument("--progress", dest="progress", action="store_true", help="Show progress bars if tqdm exists.")
    ap.add_argument("--no-progress", dest="progress", action="store_false", help="Disable progress bars.")
    ap.set_defaults(progress=True)

    ap.add_argument("--prime-gated", action="store_true", help="Run prime-gated per-ell purity test.")
    ap.add_argument("--prime-perm", type=int, default=20000, help="Permutation count for prime-gated p-values.")
    ap.add_argument("--prime-plot-prefix", type=str, default=None, help="If set, save prime curve plot images.")
    ap.add_argument("--prime-highlight", type=int, default=None, help="Highlight a specific ell in the plot.")

    ap.add_argument("--prime-weight-center", type=float, default=None,
                    help="Gaussian center (ell) for Prime-Gated weighting; requires --prime-weight-sigma > 0")
    ap.add_argument("--prime-weight-sigma", type=float, default=0.0,
                    help="Gaussian sigma (in ell units) for Prime-Gated weighting; requires --prime-weight-center")

    ap.add_argument("--phase-shear-deg", type=float, default=0.0,
                    help="Apply linear phase-shear compensation in degrees before symbolization proxy (approx).")
    ap.add_argument("--phase-shear-mode", type=str, default="k", choices=("k", "ell"),
                    help="Phase-shear dependency: stream index k or multipole ell.")
    ap.add_argument("--phase-shear-scan", type=str, default=None,
                    help='Scan a range of phase-shear degrees: "start:stop:step" (requires --prime-gated).')
    ap.add_argument("--phase-shear-report-prefix", type=str, default=None,
                    help="If set, save phase-shear scan CSV to <prefix>_<label>_phase_shear_scan.csv")

    return ap


def _slice_stream(sym: Symbols, frame: Optional[int], step: int, max_frames: int) -> Symbols:
    arr = sym.arr
    ells = sym.ells
    if frame is not None:
        start = int(frame) * int(step)
        end = start + int(step)
        arr = arr[start:end]
        ells = ells[start:end]
    else:
        # cap frames
        n_frames = min(int(max_frames), int(arr.size // int(step)))
        arr = arr[: n_frames * int(step)]
        ells = ells[: n_frames * int(step)]
    return Symbols(arr=arr.copy(), ells=ells.copy())


def _compute_channel_symbols(
    args: argparse.Namespace,
    chan: str,
    lmax: int,
    rng: np.random.Generator,
) -> Symbols:
    """
    Build Symbols for one channel: TT, EE, BB.
    """
    if chan == "TT":
        if args.tt_alm:
            almT = load_alm(args.tt_alm)
        else:
            if not args.tt_map:
                raise ValueError("Provide --tt-map or --tt-alm")
            tt = read_tt_map(args.tt_map)
            almT = map_to_alm_tt(tt, lmax=lmax)
        sym = symbols_from_alm_phase(
            almT,
            lmax=lmax,
            differential=bool(args.differential_phase),
            dither_amp=float(args.phase_dither_amp),
            rng=rng,
        )
    elif chan in ("EE", "BB"):
        if chan == "EE" and args.e_alm:
            almE = load_alm(args.e_alm)
            sym = symbols_from_alm_phase(
                almE,
                lmax=lmax,
                differential=bool(args.differential_phase),
                dither_amp=float(args.phase_dither_amp),
                rng=rng,
            )
        elif chan == "BB" and args.b_alm:
            almB = load_alm(args.b_alm)
            sym = symbols_from_alm_phase(
                almB,
                lmax=lmax,
                differential=bool(args.differential_phase),
                dither_amp=float(args.phase_dither_amp),
                rng=rng,
            )
        else:
            if not (args.q_map and args.u_map):
                raise ValueError("Provide --q-map and --u-map (or --e-alm/--b-alm)")
            q, u = read_qu_maps(args.q_map, args.u_map)
            almE, almB = map_to_alm_eb_from_qu(q, u, lmax=lmax)
            sym = symbols_from_alm_phase(
                almE if chan == "EE" else almB,
                lmax=lmax,
                differential=bool(args.differential_phase),
                dither_amp=float(args.phase_dither_amp),
                rng=rng,
            )
    else:
        raise ValueError(f"unknown channel {chan}")
    # Optional phase shear compensation
    if abs(float(args.phase_shear_deg)) > 1e-15:
        sym = apply_phase_shear(sym, theta_deg=float(args.phase_shear_deg), mode=str(args.phase_shear_mode))

    sym = _slice_stream(sym, args.frame, args.step, args.max_frames)

    # Diagnostics / hard guard against "digital collapse".
    if bool(getattr(args, "debug_symbols", False)):
        diag = debug_symbols(sym.arr, label=f"{chan} post-symbolize")
    else:
        diag = {"collapsed": False}

    if bool(diag.get("collapsed", False)):
        raise RuntimeError(
            f"Digital collapse detected in symbolization for channel {chan}. "
            "This usually means phase quantization locked to a constant bin. "
            "Try: (1) remove --phase-shear-deg, (2) add --phase-dither-amp 1e-4..1e-3, "
            "or (3) enable --differential-phase."
        )

    return sym


def _mc_null_pvalues(
    args: argparse.Namespace,
    chan: str,
    lmax: int,
    rng: np.random.Generator,
    sym_real: Symbols,
) -> Tuple[float, float, float, float, float]:
    """
    Phase randomization MC for RS proxy and prime-gated delta.
    Returns:
      p(rs_mean_zero), p(rs_tail_rate), mc_mean(delta), mc_std(delta), mc_p(two-sided) for delta.
    """
    mc = int(args.mc)
    if mc <= 0:
        return float("nan"), float("nan"), float("nan"), float("nan"), float("nan")

    # We need access to alms for MC. Recompute from inputs.
    if chan == "TT":
        if args.tt_alm:
            alm = load_alm(args.tt_alm)
        else:
            tt = read_tt_map(args.tt_map)
            alm = map_to_alm_tt(tt, lmax=lmax)
    else:
        if chan == "EE" and args.e_alm:
            alm = load_alm(args.e_alm)
        elif chan == "BB" and args.b_alm:
            alm = load_alm(args.b_alm)
        else:
            q, u = read_qu_maps(args.q_map, args.u_map)
            almE, almB = map_to_alm_eb_from_qu(q, u, lmax=lmax)
            alm = almE if chan == "EE" else almB

    # Observed proxies
    rz_real = rs_mean_zero_proxy(sym_real.arr)
    rt_real = rs_tail_rate_proxy(sym_real.arr, tail_k=int(args.tail_k))

    # Prime-gated observed delta (unweighted unless center+sigma given)
    w_h: Optional[np.ndarray] = None
    if args.prime_weight_center is not None and float(args.prime_weight_sigma) > 0:
        # weights computed on shell ells, later
        pass

    # MC collect
    rz_mc = np.zeros(mc, dtype=float)
    rt_mc = np.zeros(mc, dtype=float)
    delta_mc = np.zeros(mc, dtype=float)

    it = range(mc)
    use_tqdm = bool(args.progress) and (tqdm is not None)
    if use_tqdm:
        it = tqdm(it, desc=f"{chan} MC", leave=True)

    for i in it:
        alm_r = randomize_phases_per_ell(alm, lmax=lmax, rng=rng)
        sym = symbols_from_alm_phase(
            alm_r,
            lmax=lmax,
            differential=bool(args.differential_phase),
            dither_amp=float(args.phase_dither_amp),
            rng=rng,
        )
        if abs(float(args.phase_shear_deg)) > 1e-15:
            sym = apply_phase_shear(sym, theta_deg=float(args.phase_shear_deg), mode=str(args.phase_shear_mode))
        sym = _slice_stream(sym, args.frame, args.step, args.max_frames)

        rz_mc[i] = rs_mean_zero_proxy(sym.arr)
        rt_mc[i] = rs_tail_rate_proxy(sym.arr, tail_k=int(args.tail_k))

        if args.prime_gated:
            ells_pg, integ_pg = prime_gated_integrity_curve(sym, args.lmin, args.lmax)
            if args.prime_weight_center is not None and float(args.prime_weight_sigma) > 0:
                w_h = gaussian_weights_for_ell(ells_pg, float(args.prime_weight_center), float(args.prime_weight_sigma))
                delta_mc[i] = prime_gated_delta_mean_weighted(ells_pg, integ_pg, w_h)
            else:
                delta_mc[i] = prime_gated_delta_mean(ells_pg, integ_pg)
        else:
            delta_mc[i] = float("nan")

        if use_tqdm:
            # show running p estimates (optional)
            p_mean = float(np.mean(rz_mc[: i + 1] >= rz_real)) if i >= 10 else float("nan")
            p_tail = float(np.mean(rt_mc[: i + 1] >= rt_real)) if i >= 10 else float("nan")
            it.set_postfix(p_mean=f"{p_mean:.4g}", p_tail=f"{p_tail:.4g}")

    # One-sided p for >=
    p_rz = float(np.mean(rz_mc >= rz_real))
    p_rt = float(np.mean(rt_mc >= rt_real))

    # Delta two-sided against MC distribution
    delta_real = float("nan")
    if args.prime_gated:
        ells_pg, integ_pg = prime_gated_integrity_curve(sym_real, args.lmin, args.lmax)
        if args.prime_weight_center is not None and float(args.prime_weight_sigma) > 0:
            w_h = gaussian_weights_for_ell(ells_pg, float(args.prime_weight_center), float(args.prime_weight_sigma))
            delta_real = prime_gated_delta_mean_weighted(ells_pg, integ_pg, w_h)
        else:
            delta_real = prime_gated_delta_mean(ells_pg, integ_pg)

    finite_delta = np.isfinite(delta_mc)
    mc_mean = float(np.nanmean(delta_mc))
    mc_std = float(np.nanstd(delta_mc))
    if np.isfinite(delta_real) and np.any(finite_delta):
        d = delta_mc[finite_delta]
        mc_p = float(np.mean(np.abs(d - mc_mean) >= abs(delta_real - mc_mean)))
    else:
        mc_p = float("nan")

    return p_rz, p_rt, mc_mean, mc_std, mc_p


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = build_arg_parser()
    args = ap.parse_args(argv)

    lmax = int(args.lmax)
    rng = _rng(int(args.seed))

    channels = ["TT", "EE", "BB"]

    # Compute real symbols for all available channels
    syms: Dict[str, Symbols] = {}
    for chan in channels:
        # EE/BB only if we can compute them
        if chan == "TT":
            syms[chan] = _compute_channel_symbols(args, chan, lmax, rng)
        else:
            # only if E/B provided or Q/U given
            if (chan == "EE" and (args.e_alm or (args.q_map and args.u_map))) or (
                chan == "BB" and (args.b_alm or (args.q_map and args.u_map))
            ):
                syms[chan] = _compute_channel_symbols(args, chan, lmax, rng)

    print("\n=== Observed scores ===", flush=True)
    for chan, sym in syms.items():
        print_observed_scores(chan, sym, tail_k=int(args.tail_k))

    # Prime-gated real delta and permutation p
    if args.prime_gated:
        print("\n=== Prime-Gated (Real): per-ell Hamming purity ===", flush=True)
        for chan, sym in syms.items():
            ells_pg, integ_pg = prime_gated_integrity_curve(sym, args.lmin, args.lmax)

            w_h: Optional[np.ndarray] = None
            if args.prime_weight_center is not None and float(args.prime_weight_sigma) > 0:
                w_h = gaussian_weights_for_ell(
                    ells_pg, float(args.prime_weight_center), float(args.prime_weight_sigma)
                )
                delta = prime_gated_delta_mean_weighted(ells_pg, integ_pg, w_h)
            else:
                delta = prime_gated_delta_mean(ells_pg, integ_pg)

            perm_p = prime_gated_permutation_pvalue(
                ells_pg, integ_pg, w_h=w_h, n_perm=int(args.prime_perm), rng=rng
            )
            print(f"{chan}: Δmean(P−C)={delta:+.7g}  perm_p(two-sided)={perm_p:.6g}  (perm={int(args.prime_perm)})", flush=True)

            if args.prime_plot_prefix:
                save_prime_plot(args.prime_plot_prefix, chan, ells_pg, integ_pg, highlight=args.prime_highlight)

        # Optional: sweep phase-shear scan and report Prime-Gated Δ.
        if args.phase_shear_scan:
            print("\n=== Phase-shear scan (Prime-Gated) ===", flush=True)
            print(f"  mode={args.phase_shear_mode}  scan={args.phase_shear_scan}", flush=True)

            try:
                a, b, c = args.phase_shear_scan.split(":")
                start = float(a)
                stop = float(b)
                step = float(c)
            except Exception:
                raise ValueError("--phase-shear-scan expects start:stop:step")

            if step == 0:
                raise ValueError("--phase-shear-scan step must be nonzero")

            # include stop
            thetas = []
            t = start
            if step > 0:
                while t <= stop + 1e-12:
                    thetas.append(float(t))
                    t += step
            else:
                while t >= stop - 1e-12:
                    thetas.append(float(t))
                    t += step

            rows: List[Tuple[str, float, float, float]] = []  # chan, theta, delta, perm_p
            best: Dict[str, Tuple[float, float, float]] = {}  # chan -> (theta, delta, perm_p)

            for chan in list(syms.keys()):
                # Rebuild without shear, then apply in scan (so scan reflects theta only)
                # Temporarily override args.phase_shear_deg = 0 for base build
                # We'll emulate by applying shear on current sym by first reconstructing.
                # Recompute base channel with phase_shear_deg=0
                base_args = argparse.Namespace(**vars(args))
                base_args.phase_shear_deg = 0.0
                base_sym = _compute_channel_symbols(base_args, chan, lmax, rng)

                # Precompute prime-gated curve per theta
                best_theta = None
                best_perm = None
                best_delta = None

                for theta in thetas:
                    sym_theta = apply_phase_shear(base_sym, theta_deg=theta, mode=str(args.phase_shear_mode))
                    ells_pg, integ_pg = prime_gated_integrity_curve(sym_theta, args.lmin, args.lmax)

                    w_h: Optional[np.ndarray] = None
                    if args.prime_weight_center is not None and float(args.prime_weight_sigma) > 0:
                        w_h = gaussian_weights_for_ell(
                            ells_pg, float(args.prime_weight_center), float(args.prime_weight_sigma)
                        )
                        delta = prime_gated_delta_mean_weighted(ells_pg, integ_pg, w_h)
                    else:
                        delta = prime_gated_delta_mean(ells_pg, integ_pg)

                    perm_p = prime_gated_permutation_pvalue(
                        ells_pg, integ_pg, w_h=w_h, n_perm=int(args.prime_perm), rng=rng
                    )
                    rows.append((chan, float(theta), float(delta), float(perm_p)))

                    if (best_perm is None) or (perm_p < best_perm):
                        best_perm = perm_p
                        best_theta = theta
                        best_delta = delta

                best[chan] = (float(best_theta), float(best_delta), float(best_perm))
                print(f"  {chan}: best theta={best_theta:+.3g} deg  Δ={best_delta:+.7g}  perm_p={best_perm:.6g}", flush=True)

            if args.phase_shear_report_prefix:
                out_csv = f"{args.phase_shear_report_prefix}_phase_shear_scan.csv"
                with open(out_csv, "w", newline="") as f:
                    w = csv.writer(f)
                    w.writerow(["channel", "theta_deg", "delta", "perm_p"])
                    for r in rows:
                        w.writerow(list(r))
                print(f"  wrote: {out_csv}", flush=True)

    # Monte Carlo null
    print("\n=== Monte Carlo (phase randomization per ell) ===", flush=True)
    for chan, sym in syms.items():
        p_rz, p_rt, mc_mean, mc_std, mc_p = _mc_null_pvalues(args, chan, lmax, rng, sym)
        print(f"{chan}: p(rs_mean_zero)={p_rz:.6g}  p(rs_tail_rate)={p_rt:.6g}  (mc={int(args.mc)})", flush=True)
        if args.prime_gated:
            # real delta
            ells_pg, integ_pg = prime_gated_integrity_curve(sym, args.lmin, args.lmax)
            if args.prime_weight_center is not None and float(args.prime_weight_sigma) > 0:
                w_h = gaussian_weights_for_ell(
                    ells_pg, float(args.prime_weight_center), float(args.prime_weight_sigma)
                )
                delta_real = prime_gated_delta_mean_weighted(ells_pg, integ_pg, w_h)
            else:
                delta_real = prime_gated_delta_mean(ells_pg, integ_pg)
            print(
                f"  [Prime-Gated null] Δmean(P−C): real={delta_real:+.7g}  mc_mean={mc_mean:+.7g}  mc_std={mc_std:.6g}  mc_p(two-sided)={mc_p:.6g}",
                flush=True,
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

