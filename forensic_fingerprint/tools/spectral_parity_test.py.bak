#!/usr/bin/env python3
"""Spectral parity / RS-consistency test for CMB alm coefficients.

Rotation-invariant "multiplex" test:
  1) Obtain a_{\ell m} coefficients (TT, and optionally EE/BB via Q/U).
  2) Define an ordering k(\ell,m) = \ell^2 + \ell + m (shell-by-shell).
  3) Quantize each coefficient to an 8-bit symbol (phase quantization).
  4) Scan frames of length 255 symbols and compute:
     - Hamming(8,4) validity rate (quick screening)
     - RS(255,201) syndrome score E = count_{j=1..54}[S_j==0]
  5) Compute p-values via Monte Carlo nulls that preserve C_\ell.

Inputs
------
You can pass either maps (HEALPix FITS) or alm (FITS) files.
For polarization, pass Q/U maps or precomputed almE/almB.

Null models
-----------
N1: Phase randomization per \ell (preserves |a_{\ell m}| hence C_\ell.

Notes
-----
- This is a forensic "consistency" test, not a proof of any model.
- A null result does not invalidate UBT Layer-1; it only constrains this
  specific Layer-2 encoding hypothesis.
"""

from __future__ import annotations

import argparse
import math
import os
import random
import sys
import time
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np

# Optional plotting (only used for the Prime-Gated view).
# Keeping this optional avoids forcing matplotlib for headless/CI runs.
try:  # pragma: no cover
    import matplotlib.pyplot as plt
except Exception:  # pragma: no cover
    plt = None

try:
    from tqdm import tqdm
except Exception:  # pragma: no cover
    tqdm = None

try:
    import healpy as hp
except Exception as e:  # pragma: no cover
    hp = None

from .rs_syndrome import RSParams, syndrome_zero_count


# -----------------------------------------------------------------------------
# Prime-gated helper utilities
# -----------------------------------------------------------------------------

def is_prime(n: int) -> bool:
    """Return True if n is a prime number.

    Notes
    -----
    - We only care about small-ish multipoles (ell), so a deterministic
      sqrt(n) test is more than enough.
    - ell=0,1 are treated as non-prime.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if (n % 2) == 0 or (n % 3) == 0:
        return False
    r = int(math.isqrt(n))
    f = 5
    while f <= r:
        if (n % f) == 0 or (n % (f + 2)) == 0:
            return False
        f += 6
    return True


def ell_shell_indices(ell: int) -> np.ndarray:
    """Return the k-indices for the full (ell,m) shell: m in [-ell, ..., +ell]."""
    # NOTE: With k(ell,m)=ell^2+ell+m, the shell is actually contiguous:
    #   m=-ell -> k=ell^2
    #   m=+ell -> k=ell^2+2ell
    # Keeping the explicit list is handy for clarity, but the prime-gated
    # computation uses the contiguous slice directly for performance.
    return np.array([k_index(ell, m) for m in range(-ell, ell + 1)], dtype=np.int64)


def ell_shell_slice(ell: int) -> slice:
    """Return a contiguous slice covering the (ell,m) shell in the k-stream."""
    start = int(ell * ell)
    stop = int(ell * ell + 2 * ell + 1)  # python stop is exclusive
    return slice(start, stop)


def shell_hamming_integrity(symbol_stream: np.ndarray, ell: int) -> float:
    """Digit-level "purity" for one multipole shell.

    We use the Hamming(8,4) validity rate as a fast, purely digital checksum.
    For a random byte stream, expected validity is 1/16 = 0.0625.

    This matches the user's intended "Hammingova čistota" view per multipole.
    """
    # Fast path: the shell is contiguous in k.
    sl = ell_shell_slice(int(ell))
    return hamming_valid_rate_fast(symbol_stream[sl])


def prime_gated_integrity_curve(
    symbol_stream: np.ndarray,
    lmin: int,
    lmax: int,
) -> Tuple[np.ndarray, np.ndarray]:
    """Compute per-ell integrity curve for plotting / inspection."""
    ells = np.arange(int(lmin), int(lmax) + 1, dtype=int)
    integrity = np.empty_like(ells, dtype=float)
    for i, ell in enumerate(ells.tolist()):
        integrity[i] = shell_hamming_integrity(symbol_stream, ell)
    return ells, integrity


def prime_gated_delta_from_symbol_stream(
    symbol_stream: np.ndarray,
    lmin: int,
    lmax: int,
) -> float:
    """Compute Δmean(P−C) for one symbol stream without storing the whole curve."""
    p_sum = 0.0
    c_sum = 0.0
    p_n = 0
    c_n = 0
    for ell in range(int(lmin), int(lmax) + 1):
        r = shell_hamming_integrity(symbol_stream, ell)
        if not np.isfinite(r):
            continue
        if is_prime(ell):
            p_sum += r
            p_n += 1
        elif ell >= 2:
            c_sum += r
            c_n += 1
    if p_n == 0 or c_n == 0:
        return float('nan')
    return float((p_sum / p_n) - (c_sum / c_n))


def prime_gated_delta_mean(ells: np.ndarray, integrity: np.ndarray) -> float:
    """Compute mean(integrity | ell is prime) - mean(integrity | ell is composite)."""
    prime_mask = np.array([is_prime(int(e)) for e in ells], dtype=bool)
    comp_mask = (ells >= 2) & (~prime_mask)
    p = integrity[prime_mask]
    c = integrity[comp_mask]
    if p.size == 0 or c.size == 0:
        return float('nan')
    return float(np.mean(p) - np.mean(c))


def prime_gated_delta_mean_weighted(
    ells: np.ndarray,
    integrity: np.ndarray,
    weights: np.ndarray,
) -> float:
    """Weighted version of prime_gated_delta_mean.

    weights are applied to *both* prime and composite groups, so the
    comparison stays local (e.g., emphasizing multipoles near a carrier).
    """
    ells = np.asarray(ells, dtype=int)
    integrity = np.asarray(integrity, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if ells.shape != integrity.shape or ells.shape != weights.shape:
        raise ValueError('ells, integrity, weights must have the same shape')

    prime_mask = np.array([is_prime(int(e)) for e in ells], dtype=bool)
    comp_mask = (ells >= 2) & (~prime_mask)
    if not np.any(prime_mask) or not np.any(comp_mask):
        return float('nan')

    wp = weights[prime_mask]
    wc = weights[comp_mask]
    if float(np.sum(wp)) <= 0.0 or float(np.sum(wc)) <= 0.0:
        return float('nan')

    mp = float(np.sum(wp * integrity[prime_mask]) / np.sum(wp))
    mc = float(np.sum(wc * integrity[comp_mask]) / np.sum(wc))
    return float(mp - mc)


def permutation_null_deltas(
    ells: np.ndarray,
    integrity: np.ndarray,
    n_perm: int,
    rng: np.random.Generator,
) -> np.ndarray:
    """Permutation null for Prime-Gated effect.

    Keeps the integrity values fixed, but randomly reassigns "prime" labels
    to the same number of multipoles. This tests whether P vs C difference
    can arise purely from the marginal integrity distribution.
    """
    ells = np.asarray(ells, dtype=int)
    integrity = np.asarray(integrity, dtype=float)

    prime_mask = np.array([is_prime(int(e)) for e in ells], dtype=bool)
    comp_mask = (ells >= 2) & (~prime_mask)
    valid_idx = np.where(ells >= 2)[0]

    p_count = int(np.sum(prime_mask))
    c_count = int(np.sum(comp_mask))
    if p_count == 0 or c_count == 0:
        return np.array([], dtype=float)

    out = np.empty(int(n_perm), dtype=float)
    for i in range(int(n_perm)):
        perm = rng.permutation(valid_idx)
        p_idx = perm[:p_count]
        c_idx = perm[p_count : p_count + c_count]
        out[i] = float(np.mean(integrity[p_idx]) - np.mean(integrity[c_idx]))
    return out


def permutation_null_deltas_weighted(
    ells: np.ndarray,
    integrity: np.ndarray,
    weights: np.ndarray,
    n_perm: int,
    rng: np.random.Generator,
) -> np.ndarray:
    """Permutation null with weights.

    Same as permutation_null_deltas, but the delta is computed using
    weighted means. The weights remain attached to each ell position and
    are *not* permuted; we only permute group labels.
    """
    ells = np.asarray(ells, dtype=int)
    integrity = np.asarray(integrity, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if ells.shape != integrity.shape or ells.shape != weights.shape:
        raise ValueError('ells, integrity, weights must have the same shape')

    prime_mask = np.array([is_prime(int(e)) for e in ells], dtype=bool)
    comp_mask = (ells >= 2) & (~prime_mask)
    valid_idx = np.where(ells >= 2)[0]

    p_count = int(np.sum(prime_mask))
    c_count = int(np.sum(comp_mask))
    if p_count == 0 or c_count == 0:
        return np.array([], dtype=float)

    out = np.empty(int(n_perm), dtype=float)
    for i in range(int(n_perm)):
        perm = rng.permutation(valid_idx)
        p_idx = perm[:p_count]
        c_idx = perm[p_count : p_count + c_count]
        wp = weights[p_idx]
        wc = weights[c_idx]
        mp = float(np.sum(wp * integrity[p_idx]) / np.sum(wp))
        mc = float(np.sum(wc * integrity[c_idx]) / np.sum(wc))
        out[i] = float(mp - mc)
    return out


# RSParams API compatibility: some versions accept nsym, others derive it.
# Our local rs_syndrome.RSParams accepts (n,k,nsym), but keep this robust.
def _make_rs_params(RSParams, n=255, k=201, nsym=54):
    try:
        import inspect
        sig = inspect.signature(RSParams)
        params = sig.parameters
        if 'nsym' in params:
            return RSParams(n=n, k=k, nsym=nsym)
        if 'parity' in params:
            return RSParams(n=n, k=k, parity=nsym)
        if 'npar' in params:
            return RSParams(n=n, k=k, npar=nsym)
        return RSParams(n=n, k=k)
    except Exception:
        try:
            return RSParams(n, k, nsym)
        except Exception:
            return RSParams(n, k)


class _Progress:
    """Single-line progress reporting with optional tqdm support.

    Uses tqdm if available; otherwise writes a single updating line to stderr.
    Designed to avoid spamming many lines in long Monte Carlo runs.
    """

    def __init__(self, enabled: bool, total: int, desc: str, unit: str = 'it'):
        self.enabled = bool(enabled)
        self.total = int(total)
        self.desc = str(desc)
        self.unit = str(unit)
        self._count = 0
        self._tqdm = None
        if self.enabled and tqdm is not None:
            self._tqdm = tqdm(total=self.total, desc=self.desc, unit=self.unit)

    def update(self, n: int = 1, **postfix):
        self._count += int(n)
        if self._tqdm is not None:
            if postfix:
                self._tqdm.set_postfix(postfix)
            self._tqdm.update(n)
            return
        if not self.enabled:
            return
        # Manual single-line update.
        msg = f'{self.desc}: {self._count}/{self.total}'
        if postfix:
            msg += '  ' + '  '.join([f'{k}={v}' for k, v in postfix.items()])
        sys.stderr.write('\r' + msg[:200])
        sys.stderr.flush()

    def close(self):
        if self._tqdm is not None:
            self._tqdm.close()
        elif self.enabled:
            sys.stderr.write('\n')
            sys.stderr.flush()


# -----------------------------------------------------------------------------
# Symbolization and transforms
# -----------------------------------------------------------------------------

def k_index(ell: int, m: int) -> int:
    """Rotation-invariant shell-by-shell index for (ell,m)."""
    return int(ell * ell + ell + m)


def _phase_to_u8(phase: np.ndarray) -> np.ndarray:
    """Map phases in [-pi, pi] to uint8 [0,255] with wrapping."""
    # Normalize to [0,1)
    x = (phase + np.pi) / (2.0 * np.pi)
    x = np.mod(x, 1.0)
    return np.floor(x * 256.0).astype(np.uint8)


def _apply_phase_shear(
    alm: np.ndarray,
    lmax: int,
    lmin: int,
    phase_shear_deg: float,
    mode: str,
) -> np.ndarray:
    """Apply a linear phase shear to alm.

    phase_shear_deg is interpreted as degrees per:
      - 'k'   : per k-index in the concatenated stream (ell^2+ell+m)
      - 'ell' : per multipole ell (same for all m in a shell)
    """
    if phase_shear_deg == 0.0:
        return alm
    theta = np.deg2rad(float(phase_shear_deg))
    out = np.array(alm, copy=True)
    if mode == 'ell':
        for ell in range(lmin, lmax + 1):
            sl = hp.Alm.getidx(lmax, ell, np.arange(0, ell + 1, dtype=int))
            out[sl] *= np.exp(-1j * theta * ell)
        return out
    # mode == 'k'
    # Construct phase ramp over the *symbol stream* ordering.
    # We approximate by applying per-(ell,m) ramp based on k-index; this is
    # consistent with the rotation-invariant stream definition.
    # Healpy alm indexing stores only m>=0. We'll apply ramp to those and
    # rely on the conjugate symmetry being handled when building the stream.
    for ell in range(lmin, lmax + 1):
        for m in range(0, ell + 1):
            idx = hp.Alm.getidx(lmax, ell, m)
            k = k_index(ell, m)
            out[idx] *= np.exp(-1j * theta * k)
    return out


@dataclass
class Symbols:
    """Lightweight wrapper for the 1D uint8 symbol stream.

    Some code paths pass the stream around as a numpy array, others as a
    named wrapper. To keep helper functions (that expect numpy slicing)
    working, Symbols emulates a 1D numpy array for indexing/slicing.

    The underlying array is stored in `.symbols` and aliased as `.arr`.
    """
    name: str
    symbols: np.ndarray  # uint8

    def __post_init__(self) -> None:
        self.symbols = np.asarray(self.symbols, dtype=np.uint8)
        if self.symbols.ndim != 1:
            self.symbols = self.symbols.reshape(-1)

    @property
    def arr(self) -> np.ndarray:
        return self.symbols

    def __len__(self) -> int:
        return int(self.symbols.shape[0])

    def __iter__(self):
        return iter(self.symbols)

    def __getitem__(self, key):
        return self.symbols[key]

    def __array__(self, dtype=None):
        return np.asarray(self.symbols, dtype=dtype)


def build_symbol_stream_from_alm(
    alm: np.ndarray,
    lmax: int,
    name: str,
    lmin: int,
    phase_shear_deg: float = 0.0,
    phase_shear_mode: str = 'k',
) -> Symbols:
    """Build the rotation-invariant k-stream symbolization from alm.

    - Uses k(ell,m)=ell^2+ell+m ordering over full m in [-ell..+ell]
    - Quantizes phase of alm to 8-bit symbols
    """
    if hp is None:
        raise RuntimeError("healpy is required to build symbol stream from alm")

    a = alm
    if phase_shear_deg != 0.0:
        a = _apply_phase_shear(a, lmax=lmax, lmin=lmin, phase_shear_deg=phase_shear_deg, mode=phase_shear_mode)

    # Full stream length is (lmax+1)^2
    stream_len = (lmax + 1) * (lmax + 1)
    out = np.zeros(stream_len, dtype=np.uint8)

    for ell in range(lmin, lmax + 1):
        for m in range(0, ell + 1):
            idx = hp.Alm.getidx(lmax, ell, m)
            z = a[idx]
            # m>=0 phase
            k = k_index(ell, m)
            out[k] = _phase_to_u8(np.array([np.angle(z)], dtype=float))[0]
            if m != 0:
                # infer negative m using conjugate symmetry:
                # a_{ell,-m} = (-1)^m * conj(a_{ell,m})
                zneg = ((-1) ** m) * np.conjugate(z)
                kneg = k_index(ell, -m)
                out[kneg] = _phase_to_u8(np.array([np.angle(zneg)], dtype=float))[0]

    return Symbols(name=name, symbols=out)


# -----------------------------------------------------------------------------
# Hamming(8,4) validity
# -----------------------------------------------------------------------------

# Valid Hamming(8,4) codewords (extended Hamming with overall parity).
# Precompute membership for fast validity checks.
def _build_hamming_valid_table() -> np.ndarray:
    valid = np.zeros(256, dtype=bool)
    # Enumerate all 16 possible 4-bit messages and encode them.
    for msg in range(16):
        d = [(msg >> i) & 1 for i in range(4)]  # d0..d3
        # Using a standard extended Hamming(8,4) construction:
        # positions: [p0 p1 d0 p2 d1 d2 d3 p3]  (one of many conventions)
        # We'll follow the encoding used by the original implementation.
        p1 = d[0] ^ d[1] ^ d[3]
        p2 = d[0] ^ d[2] ^ d[3]
        p3 = d[1] ^ d[2] ^ d[3]
        p0 = p1 ^ p2 ^ d[0] ^ p3 ^ d[1] ^ d[2] ^ d[3]  # overall parity
        code = (p0 << 7) | (p1 << 6) | (d[0] << 5) | (p2 << 4) | (d[1] << 3) | (d[2] << 2) | (d[3] << 1) | (p3 << 0)
        valid[code] = True
    return valid


_HAMMING_VALID = _build_hamming_valid_table()


def hamming_valid_rate_fast(symbols: np.ndarray) -> float:
    """Compute fraction of bytes that are valid extended Hamming(8,4) codewords."""
    if symbols.size == 0:
        return float('nan')
    return float(np.mean(_HAMMING_VALID[symbols]))


# -----------------------------------------------------------------------------
# RS(255,201) syndrome scoring
# -----------------------------------------------------------------------------

def rs_zero_syndrome_count(frames: np.ndarray, rs_params: RSParams) -> np.ndarray:
    """Count how many RS syndromes are zero per frame."""
    # frames shape: (n_frames, 255)
    out = np.empty(frames.shape[0], dtype=int)
    for i in range(frames.shape[0]):
        out[i] = int(syndrome_zero_count(frames[i].tolist(), rs_params))
    return out


def frame_view(symbols: np.ndarray, frame: int, step: int, max_frames: Optional[int]) -> np.ndarray:
    """Create a strided view of frames of length `frame`."""
    n = symbols.shape[0]
    if n < frame:
        return np.zeros((0, frame), dtype=np.uint8)
    starts = np.arange(0, n - frame + 1, step, dtype=int)
    if max_frames is not None and max_frames > 0:
        starts = starts[:max_frames]
    frames = np.vstack([symbols[s:s + frame] for s in starts])
    return frames.astype(np.uint8, copy=False)


@dataclass
class Scores:
    hamming_rate: float
    rs_mean_zero_syndromes: float
    rs_tail_rate: float


def compute_scores(
    symbols: np.ndarray,
    rs_params: RSParams,
    frame: int,
    step: int,
    tail_k: int,
    max_frames: Optional[int],
    rng: np.random.Generator,
) -> Tuple[float, float]:
    """Compute RS(255,201) based mean and tail metrics on a symbol stream."""
    frames = frame_view(symbols, frame=frame, step=step, max_frames=max_frames)
    if frames.shape[0] == 0:
        return float('nan'), float('nan')
    zeros = rs_zero_syndrome_count(frames, rs_params)
    mean_zero = float(np.mean(zeros))
    tail_rate = float(np.mean(zeros >= int(tail_k)))
    return mean_zero, tail_rate


# -----------------------------------------------------------------------------
# Loading TT / Q / U, and E/B transforms
# -----------------------------------------------------------------------------

def load_alm_from_map(map_path: str, lmax: int, field: int = 0) -> np.ndarray:
    if hp is None:
        raise RuntimeError("healpy is required to load maps")
    m = hp.read_map(map_path, field=field, verbose=False)
    alm = hp.map2alm(m, lmax=lmax, iter=3)
    return alm


def load_alm_from_alm_fits(alm_path: str) -> np.ndarray:
    if hp is None:
        raise RuntimeError("healpy is required to load alms")
    return hp.read_alm(alm_path)


def load_almE_B_from_qu_maps(q_path: str, u_path: str, lmax: int) -> Tuple[np.ndarray, np.ndarray]:
    if hp is None:
        raise RuntimeError("healpy is required to load Q/U maps")
    q = hp.read_map(q_path, field=0, verbose=False)
    u = hp.read_map(u_path, field=0, verbose=False)
    # healpy API compatibility: some versions accept iter=..., some do not
    try:
        almE, almB = hp.map2alm_spin([q, u], spin=2, lmax=lmax, iter=3)
    except TypeError:
        almE, almB = hp.map2alm_spin([q, u], spin=2, lmax=lmax)
    return almE, almB


# -----------------------------------------------------------------------------
# Null model
# -----------------------------------------------------------------------------

def phase_randomize_per_ell(alm: np.ndarray, lmax: int, rng: np.random.Generator, lmin: int) -> np.ndarray:
    """Randomize phases per ell shell, preserving |a_{ell m}|."""
    if hp is None:
        raise RuntimeError("healpy is required for phase randomization")
    out = np.array(alm, copy=True)
    for ell in range(lmin, lmax + 1):
        # Apply a single random phase to all m in the shell, or independent?
        # For the strictest null, do independent phases per m (keeping amp).
        for m in range(0, ell + 1):
            idx = hp.Alm.getidx(lmax, ell, m)
            amp = np.abs(out[idx])
            phi = rng.uniform(0.0, 2.0 * np.pi)
            out[idx] = amp * np.exp(1j * phi)
    return out


def monte_carlo_pvalue(observed: float, null_samples: Sequence[float]) -> float:
    """One-sided p-value P(null >= observed) with +1 smoothing."""
    x = np.asarray(null_samples, dtype=float)
    x = x[np.isfinite(x)]
    if x.size == 0 or not np.isfinite(observed):
        return float('nan')
    return float((np.sum(x >= observed) + 1) / (x.size + 1))


# -----------------------------------------------------------------------------
# Prime-gated plotting helpers
# -----------------------------------------------------------------------------

def _plot_prime_gated_integrity(
    ells: np.ndarray,
    integrity: np.ndarray,
    title: str,
    highlight_ells: Optional[Sequence[int]],
    outpath: str,
) -> None:
    if plt is None:
        return
    plt.figure(figsize=(10, 4))
    plt.plot(ells, integrity, lw=1.0)
    if highlight_ells:
        for e in highlight_ells:
            plt.axvline(int(e), ls='--', lw=0.8, alpha=0.7)
    plt.xlabel(r'$\ell$')
    plt.ylabel('Hamming(8,4) validity rate')
    plt.title(title)
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()


def _plot_prime_gated_null_hist(null_deltas: np.ndarray, real_delta: float, title: str, outpath: str) -> None:
    if plt is None:
        return
    null_deltas = np.asarray(null_deltas, dtype=float)
    null_deltas = null_deltas[np.isfinite(null_deltas)]
    if null_deltas.size == 0:
        return
    plt.figure(figsize=(7, 4))
    plt.hist(null_deltas, bins=60, alpha=0.8)
    plt.axvline(real_delta, lw=2)
    plt.axvline(-real_delta, lw=1, ls='--')
    plt.xlabel('Δmean(P−C)')
    plt.ylabel('count')
    plt.title(title)
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser()

    ap.add_argument('--lmin', type=int, default=2)
    ap.add_argument('--lmax', type=int, default=512)

    ap.add_argument('--tt-map', type=str, default=None)
    ap.add_argument('--tt-alm', type=str, default=None)

    ap.add_argument('--q-map', type=str, default=None)
    ap.add_argument('--u-map', type=str, default=None)
    ap.add_argument('--e-alm', type=str, default=None)
    ap.add_argument('--b-alm', type=str, default=None)

    ap.add_argument('--mc', type=int, default=1000)
    ap.add_argument('--frame', type=int, default=255)
    ap.add_argument('--step', type=int, default=255)
    ap.add_argument('--max-frames', type=int, default=2048)
    ap.add_argument('--tail-k', type=int, default=8)

    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--progress', action='store_true', default=True)
    ap.add_argument('--no-progress', action='store_false', dest='progress')

    # Prime-gated analysis
    ap.add_argument('--prime-gated', action='store_true', default=False)
    ap.add_argument('--prime-perm', type=int, default=20000)
    ap.add_argument('--prime-plot-prefix', type=str, default=None)
    ap.add_argument('--prime-highlight', type=str, default=None,
                    help='comma-separated list of ells to highlight in prime-gated plots')

    # Prime-gated weighting: gaussian weights centered at ell0 (e.g. 137)
    ap.add_argument('--prime-weight-center', type=float, default=None,
                    help='center ℓ for gaussian weighting in Prime-Gated Δ (e.g., 137)')
    ap.add_argument('--prime-weight-sigma', type=float, default=0.0,
                    help='gaussian sigma (in ℓ units) for Prime-Gated weighting; requires --prime-weight-center')

    # Phase shear compensation
    ap.add_argument('--phase-shear-deg', type=float, default=0.0,
                    help='apply linear phase shear compensation in degrees (default 0)')
    ap.add_argument('--phase-shear-mode', type=str, default='k', choices=('k', 'ell'),
                    help='phase shear ramp mode: "k" (per k-index) or "ell" (per multipole)')
    ap.add_argument('--phase-shear-scan', type=str, default=None,
                    help='scan a range of phase-shear degrees: "start:stop:step" (requires --prime-gated)')
    ap.add_argument('--phase-shear-report-prefix', type=str, default=None,
                    help='if set, save phase-shear scan CSV to <prefix>_<label>_phase_shear_scan.csv')

    args = ap.parse_args(argv)

    if args.tt_map is None and args.tt_alm is None:
        ap.error("Provide --tt-map or --tt-alm")

    if args.prime_weight_sigma and args.prime_weight_sigma > 0 and args.prime_weight_center is None:
        ap.error("--prime-weight-sigma requires --prime-weight-center")

    if args.prime_weight_center is not None:
        args.prime_weight_center = float(args.prime_weight_center)

    highlight_ells: Optional[List[int]] = None
    if args.prime_highlight:
        highlight_ells = [int(x.strip()) for x in str(args.prime_highlight).split(',') if x.strip() != '']

    rng = np.random.default_rng(int(args.seed))

    rs_params = _make_rs_params(RSParams, n=255, k=201, nsym=54)

    # Load TT
    if args.tt_alm:
        tt_alm = load_alm_from_alm_fits(args.tt_alm)
    else:
        tt_alm = load_alm_from_map(args.tt_map, lmax=args.lmax, field=0)

    # Load EE/BB if present
    e_alm = None
    b_alm = None
    if args.e_alm and args.b_alm:
        e_alm = load_alm_from_alm_fits(args.e_alm)
        b_alm = load_alm_from_alm_fits(args.b_alm)
    elif args.q_map and args.u_map:
        e_alm, b_alm = load_almE_B_from_qu_maps(args.q_map, args.u_map, lmax=args.lmax)

    # Build symbol streams
    symbols_all: List[Tuple[str, np.ndarray, Symbols]] = []
    tt_sym = build_symbol_stream_from_alm(
        tt_alm, args.lmax, "TT", lmin=args.lmin,
        phase_shear_deg=args.phase_shear_deg,
        phase_shear_mode=args.phase_shear_mode,
    )
    symbols_all.append(("TT", tt_alm, tt_sym))

    if e_alm is not None and b_alm is not None:
        ee_sym = build_symbol_stream_from_alm(
            e_alm, args.lmax, "EE", lmin=args.lmin,
            phase_shear_deg=args.phase_shear_deg,
            phase_shear_mode=args.phase_shear_mode,
        )
        bb_sym = build_symbol_stream_from_alm(
            b_alm, args.lmax, "BB", lmin=args.lmin,
            phase_shear_deg=args.phase_shear_deg,
            phase_shear_mode=args.phase_shear_mode,
        )
        symbols_all.append(("EE", e_alm, ee_sym))
        symbols_all.append(("BB", b_alm, bb_sym))

    # Observed scores
    print("\n=== Observed scores ===")
    observed: Dict[str, Scores] = {}
    for label, _alm, sym in symbols_all:
        mf = None if args.max_frames == 0 else args.max_frames
        mean, tail = compute_scores(
            sym.symbols, rs_params,
            frame=args.frame, step=args.step,
            tail_k=args.tail_k, max_frames=mf, rng=rng
        )
        hamming = hamming_valid_rate_fast(sym.symbols)
        observed[label] = Scores(hamming_rate=hamming, rs_mean_zero_syndromes=mean, rs_tail_rate=tail)
        print(f"{label}: hamming_rate={hamming:.6f}  rs_mean_zero={mean:.3f}  rs_tail_rate(>={args.tail_k})={tail:.6f}")

    # Prime-gated
    prime_real: Dict[str, Dict[str, object]] = {}
    if args.prime_gated:
        print("\n=== Prime-Gated (Real): per-ell Hamming purity ===")
        for label, _alm, sym in symbols_all:
            ells_pg, integ_pg = prime_gated_integrity_curve(sym, args.lmin, args.lmax)

            weights_pg: Optional[np.ndarray] = None
            if args.prime_weight_center is not None and args.prime_weight_sigma and args.prime_weight_sigma > 0:
                weights_pg = np.exp(-0.5 * ((ells_pg - args.prime_weight_center) / args.prime_weight_sigma) ** 2)

            if weights_pg is not None:
                delta_real = prime_gated_delta_mean_weighted(ells_pg, integ_pg, weights_pg)
                perm_deltas = permutation_null_deltas_weighted(ells_pg, integ_pg, weights_pg, n_perm=args.prime_perm, rng=rng)
            else:
                delta_real = prime_gated_delta_mean(ells_pg, integ_pg)
                perm_deltas = permutation_null_deltas(ells_pg, integ_pg, n_perm=args.prime_perm, rng=rng)

            perm_deltas = np.asarray(perm_deltas, dtype=float)
            perm_deltas = perm_deltas[np.isfinite(perm_deltas)]
            if perm_deltas.size:
                p_perm_two_sided = float((np.sum(np.abs(perm_deltas) >= abs(delta_real)) + 1) / (perm_deltas.size + 1))
            else:
                p_perm_two_sided = float('nan')

            print(f"{label}: Δmean(P−C)={delta_real:.6g}  perm_p(two-sided)={p_perm_two_sided:.4g}  (perm={args.prime_perm})")
            prime_real[label] = {'delta': float(delta_real), 'perm_p': float(p_perm_two_sided), 'ells': ells_pg, 'integrity': integ_pg, 'weights': weights_pg}

            # Optional plots
            if args.prime_plot_prefix:
                prefix = str(args.prime_plot_prefix)
                _plot_prime_gated_integrity(
                    ells=ells_pg,
                    integrity=integ_pg,
                    title=(
                        f'Prime-Gated integrity vs ℓ ({label}, Real)  '
                        f'Δmean={delta_real:.3g}, perm_p≈{p_perm_two_sided:.3g}'
                    ),
                    highlight_ells=highlight_ells,
                    outpath=f'{prefix}_{label}_prime_gated_integrity.png',
                )
                if perm_deltas.size:
                    _plot_prime_gated_null_hist(
                        null_deltas=perm_deltas,
                        real_delta=float(delta_real),
                        title=f'Prime-Gated Δmean(P−C) permutation null ({label})',
                        outpath=f'{prefix}_{label}_prime_gated_perm_null.png',
                    )

    # Optional: sweep phase-shear compensation and report Prime-Gated Δ.
    # This is useful for checking whether a small linear phase drift (e.g. from
    # a 255/256 clock mismatch) can further sharpen the Prime-Gated signature.
    if args.phase_shear_scan and args.prime_gated:
        def _parse_scan(s: str) -> np.ndarray:
            # Format: start:stop:step  (degrees)
            parts = [p.strip() for p in s.split(':') if p.strip() != '']
            if len(parts) != 3:
                raise ValueError("--phase-shear-scan expects start:stop:step")
            a, b, step = (float(parts[0]), float(parts[1]), float(parts[2]))
            if step == 0:
                raise ValueError("--phase-shear-scan step must be nonzero")
            # Include endpoint if it lands exactly on the grid.
            n = int(math.floor((b - a) / step)) + 1
            if n <= 0:
                # Fallback for reversed ranges.
                n = int(math.floor((a - b) / (-step))) + 1
                step = -step
            return a + step * np.arange(n, dtype=float)

        thetas = _parse_scan(args.phase_shear_scan)
        scan_rows: List[Dict[str, float]] = []

        print('\n=== Phase-shear scan (Prime-Gated) ===', flush=True)
        print(f'  mode={args.phase_shear_mode}  scan={args.phase_shear_scan}', flush=True)

        for theta_deg in thetas:
            for label, alm, _sym0 in symbols_all:
                sym = build_symbol_stream_from_alm(
                    alm,
                    args.lmax,
                    label,
                    lmin=args.lmin,
                    phase_shear_deg=float(theta_deg),
                    phase_shear_mode=args.phase_shear_mode,
                )
                ells_pg, integ_pg = prime_gated_integrity_curve(sym, args.lmin, args.lmax)
                weights_pg: Optional[np.ndarray] = None
                if args.prime_weight_center is not None and args.prime_weight_sigma and args.prime_weight_sigma > 0:
                    weights_pg = np.exp(-0.5 * ((ells_pg - args.prime_weight_center) / args.prime_weight_sigma) ** 2)
                if weights_pg is not None:
                    delta = prime_gated_delta_mean_weighted(ells_pg, integ_pg, weights_pg)
                    perm_deltas = permutation_null_deltas_weighted(ells_pg, integ_pg, weights_pg, n_perm=args.prime_perm, rng=rng)
                else:
                    delta = prime_gated_delta_mean(ells_pg, integ_pg)
                    perm_deltas = permutation_null_deltas(ells_pg, integ_pg, n_perm=args.prime_perm, rng=rng)
                p_perm = float((np.sum(np.abs(perm_deltas) >= abs(delta)) + 1) / (len(perm_deltas) + 1))
                scan_rows.append({'theta_deg': float(theta_deg), 'delta': float(delta), 'p_perm': p_perm, 'label': label})

        # Print best (min p) per label
        for label in sorted({r['label'] for r in scan_rows}):
            rows = [r for r in scan_rows if r['label'] == label]
            rows.sort(key=lambda r: r['p_perm'])
            best = rows[0]
            print(f"  {label}: best theta={best['theta_deg']:.6g} deg  Δ={best['delta']:.6g}  perm_p={best['p_perm']:.6g}")

        if args.phase_shear_report_prefix:
            out_csv = f"{args.phase_shear_report_prefix}_phase_shear_scan.csv"
            with open(out_csv, 'w', encoding='utf-8') as f:
                f.write('label,theta_deg,delta,perm_p\n')
                for r in scan_rows:
                    f.write(f"{r['label']},{r['theta_deg']:.9g},{r['delta']:.9g},{r['p_perm']:.9g}\n")
            print(f'  wrote: {out_csv}', flush=True)

            if plt is not None:
                for label in sorted({r['label'] for r in scan_rows}):
                    rows = [r for r in scan_rows if r['label'] == label]
                    rows.sort(key=lambda r: r['theta_deg'])
                    xs = np.array([r['theta_deg'] for r in rows], dtype=float)
                    ys = np.array([r['p_perm'] for r in rows], dtype=float)
                    plt.figure(figsize=(7, 4))
                    plt.plot(xs, ys, marker='o')
                    plt.yscale('log')
                    plt.xlabel('phase_shear_deg')
                    plt.ylabel('perm p (two-sided, log scale)')
                    plt.title(f'Phase-shear scan (Prime-Gated) — {label}')
                    out_png = f"{args.phase_shear_report_prefix}_{label}_phase_shear_scan.png"
                    plt.tight_layout()
                    plt.savefig(out_png, dpi=150)
                    plt.close()
                    print(f'  wrote: {out_png}', flush=True)

    # Monte Carlo null
    print('\n=== Monte Carlo (phase randomization per ell) ===', flush=True)
    for label, alm, sym in symbols_all:
        null_means: List[float] = []
        null_tails: List[float] = []
        # Optional: Prime-Gated deltas (Δmean(P−C)) under the MC null.
        null_prime_deltas: List[float] = []
        obs_mean = observed[label].rs_mean_zero_syndromes
        obs_tail = observed[label].rs_tail_rate

        ge_mean = 0
        ge_tail = 0
        mc_prog = _Progress(args.progress, total=args.mc, desc=f'{label} MC', unit='mc')
        for i_mc in range(args.mc):
            a_null = phase_randomize_per_ell(alm, args.lmax, rng, lmin=args.lmin)
            s_null = build_symbol_stream_from_alm(
                a_null,
                args.lmax,
                name=label,
                lmin=args.lmin,
                phase_shear_deg=args.phase_shear_deg,
                phase_shear_mode=args.phase_shear_mode,
            ).symbols
            mf = None if args.max_frames == 0 else args.max_frames
            mean, tail = compute_scores(
                s_null,
                rs_params,
                frame=args.frame,
                step=args.step,
                tail_k=args.tail_k,
                max_frames=mf,
                rng=rng,
            )
            null_means.append(mean)
            null_tails.append(tail)

            # Prime-Gated null: compute Δmean(P−C) for this MC realization.
            # This is the key "MC sees no difference" check when compared to real Δ.
            if args.prime_gated and label in prime_real:
                ells_mc, integ_mc = prime_gated_integrity_curve(s_null, args.lmin, args.lmax)
                w_mc = prime_real[label].get('weights', None)
                if w_mc is not None:
                    d_mc = prime_gated_delta_mean_weighted(ells_mc, integ_mc, w_mc)
                else:
                    d_mc = prime_gated_delta_mean(ells_mc, integ_mc)
                null_prime_deltas.append(float(d_mc))

            # Running p-value estimate (one-sided, >= observed)
            if mean >= obs_mean:
                ge_mean += 1
            if tail >= obs_tail:
                ge_tail += 1

            # Update progress occasionally to reduce overhead.
            postfix = None
            if (i_mc + 1) % 5 == 0 or (i_mc + 1) == args.mc:
                p_est_mean = (1.0 + ge_mean) / (1.0 + (i_mc + 1))
                p_est_tail = (1.0 + ge_tail) / (1.0 + (i_mc + 1))
                postfix = {
                    'p_mean': f'{p_est_mean:.4g}',
                    'p_tail': f'{p_est_tail:.4g}',
                }

            if postfix:
                mc_prog.update(1, **postfix)
            else:
                mc_prog.update(1)

        mc_prog.close()

        p_mean = monte_carlo_pvalue(observed[label].rs_mean_zero_syndromes, null_means)
        p_tail = monte_carlo_pvalue(observed[label].rs_tail_rate, null_tails)

        print(f'{label}: p(rs_mean_zero)={p_mean:.4g}  p(rs_tail_rate)={p_tail:.4g}  (mc={args.mc})')

        # Report Prime-Gated behavior under phase-randomization MC.
        if args.prime_gated and label in prime_real:
            real_delta = float(prime_real[label]['delta'])
            mc_arr = np.array(null_prime_deltas, dtype=float)
            mc_arr = mc_arr[np.isfinite(mc_arr)]

            if mc_arr.size and np.isfinite(real_delta):
                p_mc_two_sided = float((np.sum(np.abs(mc_arr) >= abs(real_delta)) + 1) / (mc_arr.size + 1))
                mc_mu = float(np.mean(mc_arr))
                mc_sd = float(np.std(mc_arr))
            else:
                p_mc_two_sided = float('nan')
                mc_mu = float('nan')
                mc_sd = float('nan')

            print(
                f'  [Prime-Gated null] Δmean(P−C): real={real_delta:.6g}  '
                f'mc_mean={mc_mu:.6g}  mc_std={mc_sd:.6g}  mc_p(two-sided)={p_mc_two_sided:.4g}'
            )

            # Optional plot saving.
            if args.prime_plot_prefix and mc_arr.size:
                prefix = str(args.prime_plot_prefix)
                _plot_prime_gated_null_hist(
                    null_deltas=mc_arr,
                    real_delta=real_delta,
                    title=f'Prime-Gated Δmean(P−C) phase-randomization MC null ({label})',
                    outpath=f'{prefix}_{label}_prime_gated_mc_null.png',
                )

    return 0


if __name__ == '__main__':
    raise SystemExit(main())

