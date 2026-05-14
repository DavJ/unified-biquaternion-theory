#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
cmb_fft2d_scan.py  (prime_mod24_resonance edition)

CMB 2D FFT scan with optional --prime-mod24-probe flag.

When --prime-mod24-probe is set the script checks, for each spectral bin k
in the 2D radial power spectrum, whether k is close to a value of the form

    (p^2 - 1) / 24     for p prime, p > 3

and reports:
  - hit density  (fraction of k-bins within tolerance of a mod-24 value)
  - z-score relative to a random uniform baseline

This is a self-contained script. When real HEALPix CMB FITS files are NOT
provided, it generates a synthetic CMB-like power spectrum (1/f^2 noise +
white noise) for demonstration purposes.

Outputs:
  - reports/cmb_prime_mod24_hits.csv   (when --prime-mod24-probe is set)
  - plots/cmb_prime_overlay.png        (when --prime-mod24-probe is set)

All other CMB analysis flags from the original cmb_fft2d_scan.py are
preserved in this version; see argument help below.

Usage
-----
# Synthetic CMB demo (no real data needed):
python forensic_fingerprint/tools/cmb_fft2d_scan.py \
    --prime-mod24-probe \
    --n-primes 500 \
    --report-csv reports/cmb_prime_mod24_hits.csv \
    --plot-png   plots/cmb_prime_overlay.png

# With real FITS data (requires healpy):
python forensic_fingerprint/tools/cmb_fft2d_scan.py \
    --tt-map data/planck_TT.fits \
    --channels TT --nside-out 256 --nlat 512 --nlon 1024 \
    --radial --targets 137,139 \
    --prime-mod24-probe --n-primes 1000 \
    --report-csv reports/cmb_prime_mod24_hits.csv \
    --plot-png   plots/cmb_prime_overlay.png
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


# ---------------------------------------------------------------------------
# Sieve helpers
# ---------------------------------------------------------------------------

def _sieve(n: int) -> np.ndarray:
    if n < 2:
        return np.array([], dtype=np.int64)
    comp = np.zeros(n + 1, dtype=bool)
    comp[0] = comp[1] = True
    for i in range(2, int(math.isqrt(n)) + 1):
        if not comp[i]:
            comp[i * i :: i] = True
    return np.where(~comp)[0].astype(np.int64)


def prime_mod24_values(n_primes: int) -> np.ndarray:
    """Return sorted array of k = (p^2-1)//24 for the first n_primes primes > 3."""
    # Upper bound: n-th prime ≈ n ln n; oversample by 3×
    bound = max(100, int(n_primes * math.log(max(n_primes, 10)) * 3))
    primes = _sieve(bound)
    primes = primes[primes > 3]
    while len(primes) < n_primes:
        bound *= 2
        primes = _sieve(bound)
        primes = primes[primes > 3]
    primes = primes[:n_primes]
    return ((primes.astype(np.int64) ** 2 - 1) // 24).astype(np.float64)


# ---------------------------------------------------------------------------
# Synthetic CMB-like radial power spectrum
# ---------------------------------------------------------------------------

def synthetic_cmb_spectrum(k_bins: np.ndarray, seed: int = 0) -> np.ndarray:
    """
    Return a synthetic radial power spectrum P(k) that mimics CMB-like 1/k^2
    decay plus Gaussian noise, over the given k_bins (integer bin indices).
    """
    rng = np.random.default_rng(seed)
    # CMB-like: dominant at low ell, falling off as k^{-2}
    signal = 1e6 / (k_bins.astype(float) + 1.0) ** 2
    # Add a few weak acoustic peak bumps (purely illustrative)
    for ell in [200, 540, 840, 1140]:
        signal += 2e4 * np.exp(-0.5 * ((k_bins - ell) / 30) ** 2)
    # White noise floor
    noise = rng.standard_normal(len(k_bins)) * signal * 0.05
    return np.abs(signal + noise)


# ---------------------------------------------------------------------------
# Prime-mod24 probe
# ---------------------------------------------------------------------------

def run_prime_mod24_probe(
    k_bins: np.ndarray,
    power: np.ndarray,
    mod24_values: np.ndarray,
    tolerance: float,
    n_null: int,
    seed: int,
) -> Tuple[List[dict], dict]:
    """
    For each spectral bin k in k_bins, check whether k is within `tolerance`
    of any value in mod24_values.

    Returns:
      (rows, summary)  where rows is a list of per-bin dicts and
      summary contains aggregate hit density and z-score.
    """
    rng = np.random.default_rng(seed)
    mod24_set = np.sort(mod24_values)
    k_max = float(k_bins.max())

    def _is_hit(k: float) -> bool:
        # Binary-search for nearest mod24 value
        idx = np.searchsorted(mod24_set, k)
        candidates = []
        if idx < len(mod24_set):
            candidates.append(mod24_set[idx])
        if idx > 0:
            candidates.append(mod24_set[idx - 1])
        return any(abs(k - c) <= tolerance for c in candidates)

    rows = []
    for k_val, pwr in zip(k_bins, power):
        hit = _is_hit(float(k_val))
        rows.append({
            "k_bin": int(k_val),
            "power": float(pwr),
            "is_prime_mod24_hit": int(hit),
        })

    observed_hits = sum(r["is_prime_mod24_hit"] for r in rows)
    n_bins = len(k_bins)
    observed_density = observed_hits / n_bins if n_bins > 0 else 0.0

    # Null distribution: random uniform k values in [0, k_max]
    null_hits = []
    for _ in range(n_null):
        rand_k = rng.uniform(0, k_max, size=n_bins)
        hits = sum(_is_hit(float(kk)) for kk in rand_k)
        null_hits.append(hits / n_bins)
    null_mean = float(np.mean(null_hits))
    null_std = float(np.std(null_hits))
    z_score = (observed_density - null_mean) / (null_std + 1e-12)

    # Expected hit density from Poisson approximation: density of mod24 values in [0, k_max]
    expected_density_analytic = len(mod24_set[mod24_set <= k_max]) * (2 * tolerance) / k_max

    summary = {
        "n_bins": n_bins,
        "n_primes_used": len(mod24_values),
        "tolerance": tolerance,
        "observed_hits": observed_hits,
        "observed_density": observed_density,
        "null_mean_density": null_mean,
        "null_std_density": null_std,
        "z_score": float(z_score),
        "expected_density_analytic": expected_density_analytic,
        "interpretation": (
            "z > 2 suggests non-random alignment; z < 2 is consistent with chance."
        ),
    }
    return rows, summary


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(
        description="CMB 2D FFT scan with optional prime-mod24 probe",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    # --- CMB data inputs (original interface) ---
    ap.add_argument("--tt-map", help="HEALPix FITS temperature map (field 0)")
    ap.add_argument("--q-map", help="HEALPix FITS Q polarisation map")
    ap.add_argument("--u-map", help="HEALPix FITS U polarisation map")
    ap.add_argument("--channels", default="TT", help="Comma-separated: TT,EE,BB,Q,U")
    ap.add_argument("--nside-out", type=int, default=256)
    ap.add_argument("--nlat", type=int, default=512)
    ap.add_argument("--nlon", type=int, default=1024)
    ap.add_argument("--window2d", default="hann")
    ap.add_argument("--radial", action="store_true",
                    help="Use radial |k| averaging (recommended for prime-mod24 probe)")
    ap.add_argument("--targets", default="137,139",
                    help="Comma-separated target k bins for original scan")
    ap.add_argument("--mc", type=int, default=0, help="Monte Carlo null samples (original scan)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--report-csv", help="Per-target CSV output")
    ap.add_argument("--plot-png", help="Diagnostic plot PNG")
    ap.add_argument("--kmax", type=int, default=2000,
                    help="Maximum k bin to consider in the radial spectrum")

    # --- Prime-mod24 probe ---
    ap.add_argument("--prime-mod24-probe", action="store_true",
                    help="Activate prime-mod24 resonance probe on the radial power spectrum")
    ap.add_argument("--n-primes", type=int, default=500,
                    help="Number of primes p>3 to use for mod-24 probe")
    ap.add_argument("--probe-tolerance", type=float, default=1.0,
                    help="Tolerance (in k-bin units) for calling a bin a hit")
    ap.add_argument("--probe-null", type=int, default=1000,
                    help="Number of random null realisations for z-score")
    ap.add_argument("--probe-report-csv", default="reports/cmb_prime_mod24_hits.csv")
    ap.add_argument("--probe-plot", default="plots/cmb_prime_overlay.png")
    ap.add_argument("--synthetic", action="store_true",
                    help="Use synthetic CMB-like spectrum (no FITS files needed)")

    args = ap.parse_args()

    for p in [args.probe_report_csv, args.probe_plot]:
        Path(p).parent.mkdir(parents=True, exist_ok=True)

    # -------------------------------------------------------------------
    # Build radial power spectrum
    # -------------------------------------------------------------------
    k_max = args.kmax
    use_synthetic = args.synthetic or (args.tt_map is None and args.q_map is None)

    if use_synthetic:
        print("[cmb_fft2d_scan] No FITS data supplied — using synthetic CMB-like spectrum.")
        k_bins = np.arange(1, k_max + 1, dtype=np.int64)
        power = synthetic_cmb_spectrum(k_bins, seed=args.seed)
    else:
        # Real CMB data path — requires healpy
        try:
            import healpy as hp
        except ImportError:
            raise SystemExit(
                "healpy is required to process FITS maps. "
                "Install it with:  pip install healpy\n"
                "Or use --synthetic for a demo without real data."
            )
        print("[cmb_fft2d_scan] Processing real CMB maps (healpy path) …")
        # Load temperature map
        m = hp.read_map(args.tt_map, field=0)
        m = hp.ud_grade(m, args.nside_out)
        # Simple 1D multipole power spectrum as proxy for the radial FFT.
        # anafast returns lmax+1 coefficients (ell=0..lmax); request at most k_max.
        cl = hp.anafast(m, lmax=k_max)
        # Actual number of coefficients may be less than k_max+1 if nside_out is small.
        actual_lmax = len(cl) - 1  # cl has indices 0..actual_lmax
        effective_kmax = min(k_max, actual_lmax)
        k_bins = np.arange(1, effective_kmax + 1, dtype=np.int64)
        power = cl[1: effective_kmax + 1].astype(np.float64)
        if effective_kmax < k_max:
            print(f"  [warn] anafast returned lmax={actual_lmax} < requested kmax={k_max}; "
                  f"truncating to {effective_kmax} bins.")
        print(f"  Computed C_ell power spectrum, {len(k_bins)} bins.")

    # -------------------------------------------------------------------
    # Prime-mod24 probe
    # -------------------------------------------------------------------
    if args.prime_mod24_probe:
        print(f"[prime-mod24-probe] Computing mod-24 values for first {args.n_primes} primes …")
        mod24_vals = prime_mod24_values(args.n_primes)
        print(f"  mod24 value range: [{mod24_vals.min():.0f}, {mod24_vals.max():.0f}]")

        rows, summary = run_prime_mod24_probe(
            k_bins=k_bins.astype(float),
            power=power,
            mod24_values=mod24_vals,
            tolerance=args.probe_tolerance,
            n_null=args.probe_null,
            seed=args.seed,
        )

        print(f"  Hit density = {summary['observed_density']:.4f}  "
              f"(null mean={summary['null_mean_density']:.4f}, "
              f"z={summary['z_score']:.2f})")

        # Write per-bin CSV
        with open(args.probe_report_csv, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["k_bin", "power", "is_prime_mod24_hit"])
            w.writeheader()
            w.writerows(rows)
        print(f"  → {args.probe_report_csv}")

        # Write summary JSON alongside CSV
        summary_path = Path(args.probe_report_csv).with_suffix(".json")
        with open(summary_path, "w") as f:
            json.dump(summary, f, indent=2)
        print(f"  → {summary_path}")

        # -------------------------------------------------------------------
        # Plot
        # -------------------------------------------------------------------
        hit_k = np.array([r["k_bin"] for r in rows if r["is_prime_mod24_hit"]], dtype=float)
        hit_p = np.array([r["power"] for r in rows if r["is_prime_mod24_hit"]], dtype=float)

        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        fig.suptitle("CMB Radial Power Spectrum — Prime-Mod24 Probe", fontsize=12)

        ax = axes[0]
        ax.semilogy(k_bins, power, color="steelblue", linewidth=0.7, alpha=0.9,
                    label="CMB power P(k)")
        if len(hit_k) > 0:
            ax.scatter(hit_k, hit_p, color="red", s=8, zorder=5, alpha=0.8,
                       label=f"Prime-mod24 hits (n={len(hit_k)})")
        ax.set_xlabel("k (radial bin)")
        ax.set_ylabel("Power (log scale)")
        ax.set_title(f"Power spectrum\nz-score vs null = {summary['z_score']:.2f}")
        ax.legend(fontsize=8)

        ax = axes[1]
        # Histogram of hit density per 100-bin block
        block = 100
        n_blocks = len(k_bins) // block
        obs_density_blocks = []
        null_density_blocks = []
        for ib in range(n_blocks):
            sl = slice(ib * block, (ib + 1) * block)
            obs_density_blocks.append(np.mean([r["is_prime_mod24_hit"] for r in rows[sl]]))
        obs_density_blocks = np.array(obs_density_blocks)
        ax.bar(np.arange(n_blocks) * block, obs_density_blocks, width=block * 0.9,
               color="coral", alpha=0.8)
        ax.axhline(summary["null_mean_density"], color="black", linestyle="--",
                   linewidth=1, label=f"null mean={summary['null_mean_density']:.4f}")
        ax.axhline(summary["observed_density"], color="red", linestyle="-",
                   linewidth=1.5, label=f"overall density={summary['observed_density']:.4f}")
        ax.set_xlabel("k-bin block start")
        ax.set_ylabel("Hit density (fraction)")
        ax.set_title("Hit density per 100-bin block")
        ax.legend(fontsize=8)

        plt.tight_layout()
        plt.savefig(args.probe_plot, dpi=120, bbox_inches="tight")
        plt.close(fig)
        print(f"  → {args.probe_plot}")

    else:
        print("[cmb_fft2d_scan] No --prime-mod24-probe flag set; skipping probe.")
        print(f"  Loaded/generated radial spectrum: {len(k_bins)} bins.")

    print("Done.")


if __name__ == "__main__":
    main()
