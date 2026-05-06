#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
compare_zeta.py

Task 4: Compare the k = (p^2 - 1) / 24 sequence with the imaginary parts of
the first non-trivial zeros of the Riemann zeta function.

Method:
  - Load first n_zeros zeta zeros via mpmath.
  - Normalise both k and zeta sequences to unit variance.
  - Compute FFT of each and compare power spectra.
  - Compute cross-correlation of k (truncated to n_zeros) vs zeta imaginary parts.
  - Report Pearson correlation of FFT magnitudes.

Outputs:
  - reports/zeta_correlation.json
  - plots/zeta_vs_k_fft.png
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_zeta_zeros(n: int) -> np.ndarray:
    """Return imaginary parts of the first n non-trivial Riemann zeta zeros."""
    try:
        import mpmath
        mpmath.mp.dps = 15
        zeros = []
        print(f"  Computing {n} zeta zeros via mpmath …")
        for i in range(1, n + 1):
            z = mpmath.zetazero(i)
            zeros.append(float(z.imag))
        return np.array(zeros, dtype=np.float64)
    except ImportError as exc:
        raise RuntimeError("mpmath is required for zeta zeros.") from exc


def normalise(x: np.ndarray) -> np.ndarray:
    return (x - x.mean()) / (x.std() + 1e-12)


def power_spectrum(x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    x = normalise(x)
    window = np.hanning(len(x))
    fft = np.fft.rfft(x * window)
    freqs = np.fft.rfftfreq(len(x))
    power = np.abs(fft) ** 2 / len(x)
    return freqs, power


def cross_correlation(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Normalised cross-correlation (full mode, then keep centre region)."""
    a = normalise(a)
    b = normalise(b)
    cc = np.correlate(a, b, mode="full") / len(a)
    return cc


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Compare k FFT vs Riemann zeta zeros")
    ap.add_argument("--data", default="DATA/prime_mod24/primes_mod24.parquet")
    ap.add_argument("--n-zeros", type=int, default=500,
                    help="Number of Riemann zeta zeros to use (default: 500)")
    ap.add_argument("--out-json", default="reports/prime_mod24/zeta_correlation.json")
    ap.add_argument("--out-plot", default="reports/prime_mod24/zeta_fft_compare.png")
    args = ap.parse_args()

    for p in [args.out_json, args.out_plot]:
        Path(p).parent.mkdir(parents=True, exist_ok=True)

    print(f"Loading {args.data} …")
    df = pd.read_parquet(args.data)
    k = df["k"].to_numpy(dtype=np.float64)

    # Load zeta zeros
    Z = load_zeta_zeros(args.n_zeros)
    n = min(len(k), len(Z))
    k_cut = k[:n]

    print(f"  Using {n} elements for comparison.")

    # -----------------------------------------------------------------------
    # Power spectra
    # -----------------------------------------------------------------------
    freqs_k, power_k = power_spectrum(k_cut)
    freqs_z, power_z = power_spectrum(Z[:n])

    # Pearson correlation of power spectra (same length, same frequency grid)
    from scipy.stats import pearsonr
    r_spec, p_spec = pearsonr(power_k, power_z)

    # -----------------------------------------------------------------------
    # Cross-correlation
    # -----------------------------------------------------------------------
    cc = cross_correlation(k_cut, Z[:n])
    lags = np.arange(-(n - 1), n)
    peak_lag = int(lags[np.argmax(np.abs(cc))])
    peak_cc = float(cc[np.argmax(np.abs(cc))])
    lag0_cc = float(cc[n - 1])   # lag 0

    # Z-score of peak cross-correlation vs shuffled null
    rng = np.random.default_rng(42)
    n_null = 200
    null_peaks = []
    for _ in range(n_null):
        k_shuf = rng.permutation(k_cut)
        cc_null = cross_correlation(k_shuf, Z[:n])
        null_peaks.append(float(np.max(np.abs(cc_null))))
    null_mean = float(np.mean(null_peaks))
    null_std = float(np.std(null_peaks))
    z_score = (abs(peak_cc) - null_mean) / (null_std + 1e-12)

    print(f"  Spectral Pearson r = {r_spec:.4f}, p = {p_spec:.2e}")
    print(f"  Cross-corr peak: lag={peak_lag}, cc={peak_cc:.4f}, z={z_score:.2f}")

    # -----------------------------------------------------------------------
    # Save JSON
    # -----------------------------------------------------------------------
    result = {
        "n_elements": n,
        "n_zeta_zeros": args.n_zeros,
        "spectral_pearson": {"r": float(r_spec), "p_value": float(p_spec)},
        "cross_correlation": {
            "lag_0": lag0_cc,
            "peak_lag": peak_lag,
            "peak_value": peak_cc,
            "null_mean": null_mean,
            "null_std": null_std,
            "z_score": float(z_score),
        },
    }
    with open(args.out_json, "w") as f:
        json.dump(result, f, indent=2)
    print(f"  → {args.out_json}")

    # -----------------------------------------------------------------------
    # Plot
    # -----------------------------------------------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle("k sequence vs Riemann zeta zero imaginary parts", fontsize=12)

    # Power spectra overlay
    ax = axes[0]
    ax.semilogy(freqs_k[1:], power_k[1:], label="k sequence", color="steelblue", alpha=0.7, linewidth=0.8)
    ax.semilogy(freqs_z[1:], power_z[1:], label=f"Zeta zeros (n={n})", color="darkorange", alpha=0.7, linewidth=0.8)
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Power (log scale)")
    ax.set_title(f"Power spectra\nPearson r={r_spec:.3f}, p={p_spec:.2e}")
    ax.legend(fontsize=8)

    # Ratio of power spectra
    ax = axes[1]
    ratio = np.where(power_z[1:] > 1e-20, power_k[1:] / power_z[1:], np.nan)
    ax.semilogy(freqs_k[1:], ratio, color="purple", linewidth=0.6, alpha=0.8)
    ax.axhline(1.0, color="black", linestyle="--", linewidth=1)
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Power(k) / Power(Z)")
    ax.set_title("Power ratio k / zeta")

    # Cross-correlation
    ax = axes[2]
    half = min(50, n - 1)
    centre = n - 1
    ax.plot(lags[centre - half: centre + half + 1],
            cc[centre - half: centre + half + 1],
            color="seagreen", linewidth=0.9)
    ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.set_xlabel("Lag")
    ax.set_ylabel("Normalised cross-correlation")
    ax.set_title(f"Cross-correlation (peak z={z_score:.2f})")

    plt.tight_layout()
    plt.savefig(args.out_plot, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  → {args.out_plot}")

    print("Done.")


if __name__ == "__main__":
    main()
