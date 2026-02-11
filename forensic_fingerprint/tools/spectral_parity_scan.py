#!/usr/bin/env python3
"""
Sliding-window scan for spectral_parity_test with optional ell-filtering (primes/composites).

This script is designed to answer questions like:
- "Does a prime-only subset of multipoles show a different pattern than composites?"
- "Is there a resonance-like dip/peak in p-values around certain ell?"

It produces:
- CSV with observed metrics and Monte Carlo p-values per ell-window
- PNG plot (p-values vs window center), optionally overlaying prime/composite curves

It does NOT modify spectral_parity_test.py; it reuses its quantization logic
and implements a compatible symbol stream builder with ell-filtering.

Run from repo root (recommended inside your venv):
  python3 -m forensic_fingerprint.tools.spectral_parity_scan \
    --tt-map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \
    --scan-lmin 64 --scan-lmax 256 \
    --win 16 --step-ell 2 \
    --mc 500 \
    --ell-filter all \
    --also-prime-composite \
    --out-prefix scans/scan_64_256_w16

Notes:
- MC cost scales with number of windows × mc. Start with mc=200 for a quick look.
- For "codes" hypotheses, you should compare ALL vs PRIMES vs COMPOSITES,
  and later consider adding additional nulls (permute/block shuffle).
"""
from __future__ import annotations

import argparse
import math
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, List, Optional, Tuple

import numpy as np

try:
    import healpy as hp
except Exception as e:
    raise SystemExit(f"[scan] healpy is required. Import error: {e}")


# --- Helpers copied/compatible with spectral_parity_test.py --------------------

DEFAULT_LMIN = 2

def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    f = 3
    while f <= r:
        if n % f == 0:
            return False
        f += 2
    return True


def k_index(ell: int, m: int) -> int:
    # shell-by-shell ordering used in spectral_parity_test.py
    return ell * ell + ell + m


def quantize_phase_to_u8(z: complex) -> int:
    # phase to 8-bit symbol in [0..255]
    phi = math.atan2(z.imag, z.real)
    if phi < 0:
        phi += 2 * math.pi
    return int((phi / (2 * math.pi)) * 256) & 0xFF


def hamming_8_4_is_valid(byte: int) -> bool:
    # Standard Hamming(8,4) parity check (as in original script)
    b = [(byte >> i) & 1 for i in range(8)]
    # parity bits positions depend on convention; this is the same used in many quick checks:
    # p1 covers bits 0,2,4,6; p2 covers 1,2,5,6; p4 covers 3,4,5,6; overall parity bit 7
    p1 = b[0] ^ b[2] ^ b[4] ^ b[6]
    p2 = b[1] ^ b[2] ^ b[5] ^ b[6]
    p4 = b[3] ^ b[4] ^ b[5] ^ b[6]
    p0 = b[7] ^ b[0] ^ b[1] ^ b[2] ^ b[3] ^ b[4] ^ b[5] ^ b[6]
    return (p1 == 0) and (p2 == 0) and (p4 == 0) and (p0 == 0)


def hamming_valid_rate(symbols: np.ndarray) -> float:
    if symbols.size == 0:
        return float("nan")
    ok = 0
    for x in symbols.tolist():
        ok += 1 if hamming_8_4_is_valid(int(x)) else 0
    return ok / float(symbols.size)


# --- RS syndrome support -------------------------------------------------------
# We expect rs_syndrome.py to exist (you already added/fixed it in your tree).
try:
    from .rs_syndrome import RSParams, syndrome_zero_count  # type: ignore
except Exception as e:
    raise SystemExit(
        "[scan] Missing RS helpers. Ensure forensic_fingerprint/tools/rs_syndrome.py exists.\n"
        f"Import error: {e}"
    )


def make_rs_params(n: int = 255, k: int = 201, nsym: Optional[int] = None) -> RSParams:
    # Keep it simple: our RSParams in rs_syndrome.py supports nsym.
    nsym_eff = (n - k) if nsym is None else nsym
    return RSParams(n=n, k=k, nsym=nsym_eff)


def monte_carlo_pvalue(obs: float, null_values: List[float]) -> float:
    if not null_values:
        return float("nan")
    ge = sum(1 for v in null_values if v >= obs)
    return (1.0 + ge) / (1.0 + len(null_values))


def phase_randomize_per_ell(alm: np.ndarray, lmax: int, rng: np.random.Generator, lmin: int, lmax_win: int) -> np.ndarray:
    """Randomize phases for m>0 within each ell in [lmin, lmax_win], preserving amplitudes."""
    out = np.array(alm, copy=True)
    for ell in range(lmin, lmax_win + 1):
        for m in range(1, ell + 1):
            idx = hp.Alm.getidx(lmax, ell, m)
            r = abs(out[idx])
            phi = rng.uniform(0.0, 2 * math.pi)
            out[idx] = r * (math.cos(phi) + 1j * math.sin(phi))
    return out


@dataclass
class Symbols:
    name: str
    symbols: np.ndarray


def build_symbol_stream_filtered(
    alm: np.ndarray,
    lmax: int,
    name: str,
    lmin_win: int,
    lmax_win: int,
    ell_keep: Callable[[int], bool],
) -> Symbols:
    # Build list of (k, byte) then sort by k
    items: List[Tuple[int, int]] = []
    for ell in range(lmin_win, lmax_win + 1):
        if not ell_keep(ell):
            continue
        # m=0
        idx0 = hp.Alm.getidx(lmax, ell, 0)
        items.append((k_index(ell, 0), quantize_phase_to_u8(alm[idx0])))
        for m in range(1, ell + 1):
            idx = hp.Alm.getidx(lmax, ell, m)
            items.append((k_index(ell, m), quantize_phase_to_u8(alm[idx])))
    items.sort(key=lambda t: t[0])
    arr = np.fromiter((b for _, b in items), dtype=np.uint8, count=len(items))
    return Symbols(name=name, symbols=arr)


def compute_scores(
    symbols: np.ndarray,
    rs_params: RSParams,
    frame: int = 255,
    step: int = 255,
    tail_k: int = 8,
    max_frames: Optional[int] = None,
    rng: Optional[np.random.Generator] = None,
) -> Tuple[float, float]:
    counts: List[int] = []
    if symbols.size < frame:
        return float("nan"), float("nan")

    if max_frames is not None and max_frames > 0:
        if rng is None:
            rng = np.random.default_rng(12345)
        max_start = max(0, symbols.size - frame)
        if max_start <= 0:
            return float("nan"), float("nan")
        grid = np.arange(0, max_start + 1, step, dtype=np.int64)
        if grid.size == 0:
            return float("nan"), float("nan")
        choose = min(int(max_frames), int(grid.size))
        starts = rng.choice(grid, size=choose, replace=False)
        for s in starts.tolist():
            w = symbols[s : s + frame]
            counts.append(syndrome_zero_count(w.tolist(), rs_params))
    else:
        for start in range(0, symbols.size - frame + 1, step):
            w = symbols[start : start + frame]
            counts.append(syndrome_zero_count(w.tolist(), rs_params))

    if not counts:
        return float("nan"), float("nan")
    arr = np.array(counts, dtype=np.float64)
    mean = float(arr.mean())
    tail = float((arr >= tail_k).mean())
    return mean, tail


def run_one(
    alm: np.ndarray,
    lmax: int,
    lmin_win: int,
    lmax_win: int,
    ell_filter: str,
    frame: int,
    step_sym: int,
    max_frames: int,
    tail_k: int,
    mc: int,
    seed: int,
) -> Tuple[float, float, float, float, float]:
    """Returns observed: (ham, mean, tail) and p-values (p_mean, p_tail)."""
    if ell_filter == "all":
        keep = lambda ell: True
    elif ell_filter == "primes":
        keep = _is_prime
    elif ell_filter == "composites":
        keep = lambda ell: (ell >= 2) and (not _is_prime(ell))
    else:
        raise ValueError(f"Unknown ell-filter: {ell_filter}")

    rs_params = make_rs_params(255, 201, 54)
    rng = np.random.default_rng(seed)

    sym_obs = build_symbol_stream_filtered(alm, lmax, "TT", lmin_win, lmax_win, keep)
    ham_obs = hamming_valid_rate(sym_obs.symbols)
    mean_obs, tail_obs = compute_scores(
        sym_obs.symbols,
        rs_params,
        frame=frame,
        step=step_sym,
        tail_k=tail_k,
        max_frames=max_frames if max_frames > 0 else None,
        rng=rng,
    )

    null_means: List[float] = []
    null_tails: List[float] = []
    for _ in range(int(mc)):
        alm_null = phase_randomize_per_ell(alm, lmax, rng, lmin_win, lmax_win)
        sym_null = build_symbol_stream_filtered(alm_null, lmax, "TT", lmin_win, lmax_win, keep)
        m, t = compute_scores(
            sym_null.symbols,
            rs_params,
            frame=frame,
            step=step_sym,
            tail_k=tail_k,
            max_frames=max_frames if max_frames > 0 else None,
            rng=rng,
        )
        null_means.append(m)
        null_tails.append(t)

    p_mean = monte_carlo_pvalue(mean_obs, null_means)
    p_tail = monte_carlo_pvalue(tail_obs, null_tails)
    return ham_obs, mean_obs, tail_obs, p_mean, p_tail


def _ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tt-map", required=True, help="Planck TT map (HEALPix FITS)")
    ap.add_argument("--scan-lmin", type=int, default=64)
    ap.add_argument("--scan-lmax", type=int, default=256)
    ap.add_argument("--win", type=int, default=16, help="ell-window width (inclusive range uses [lmin, lmin+win])")
    ap.add_argument("--step-ell", type=int, default=2, help="slide step in ell")
    ap.add_argument("--mc", type=int, default=200)
    ap.add_argument("--seed", type=int, default=12345)
    ap.add_argument("--ell-filter", choices=["all", "primes", "composites"], default="all")
    ap.add_argument("--also-prime-composite", action="store_true", help="also scan primes and composites (three curves)")
    ap.add_argument("--frame", type=int, default=255)
    ap.add_argument("--step", dest="step_sym", type=int, default=255)
    ap.add_argument("--max-frames", type=int, default=2048)
    ap.add_argument("--tail-k", type=int, default=8)
    ap.add_argument("--out-prefix", type=str, default="scan_out/scan")
    args = ap.parse_args()

    # Load alm once (TT only). Use map2alm for given lmax.
    # We set lmax to scan-lmax+win to support last window.
    lmax_needed = int(args.scan_lmax + args.win)
    m = hp.read_map(args.tt_map, field=0, verbose=False)
    alm = hp.map2alm(m, lmax=lmax_needed)

    # window start positions
    starts = list(range(int(args.scan_lmin), int(args.scan_lmax) + 1, int(args.step_ell)))

    out_prefix = Path(args.out_prefix)
    _ensure_parent(out_prefix.with_suffix(".csv"))
    csv_path = out_prefix.with_suffix(".csv")
    png_path = out_prefix.with_suffix(".png")

    filters = [args.ell_filter]
    if args.also_prime_composite:
        filters = ["all", "primes", "composites"]

    rows = []
    for f in filters:
        for lmin_win in starts:
            lmax_win = lmin_win + int(args.win)
            ham, mean, tail, p_mean, p_tail = run_one(
                alm=alm,
                lmax=lmax_needed,
                lmin_win=lmin_win,
                lmax_win=lmax_win,
                ell_filter=f,
                frame=int(args.frame),
                step_sym=int(args.step_sym),
                max_frames=int(args.max_frames),
                tail_k=int(args.tail_k),
                mc=int(args.mc),
                seed=int(args.seed) ^ (lmin_win * 1315423911) ^ (hash(f) & 0xFFFFFFFF),
            )
            rows.append((f, lmin_win, lmax_win, (lmin_win + lmax_win) / 2.0, ham, mean, tail, p_mean, p_tail))

    # Write CSV
    header = "filter,lmin,lmax,center,hamming_rate,rs_mean_zero,rs_tail_rate,p_mean,p_tail\n"
    with csv_path.open("w", encoding="utf-8") as w:
        w.write(header)
        for r in rows:
            w.write(",".join(str(x) for x in r) + "\n")

    # Plot
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.figure()
    for f in filters:
        xs = [r[3] for r in rows if r[0] == f]
        ys = [r[7] for r in rows if r[0] == f]  # p_mean
        plt.plot(xs, ys, marker="o", linewidth=1, markersize=3, label=f"p_mean {f}")
    plt.ylim(-0.02, 1.02)
    plt.xlabel("ell window center")
    plt.ylabel("p-value (rs_mean_zero)")
    plt.title(f"Sliding scan p_mean (mc={args.mc}, win={args.win}, step_ell={args.step_ell})")
    plt.legend()
    plt.tight_layout()
    plt.savefig(png_path, dpi=150)

    print(f"[scan] Wrote CSV: {csv_path}")
    print(f"[scan] Wrote plot: {png_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
