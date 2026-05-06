#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
spectrum_analysis.py

Task 3: Spectral analysis (FFT) of the k = (p^2 - 1) / 24 sequence.

Pipeline:
  1. Load k sequence from Parquet
  2. Z-score normalise
  3. Apply Hann window
  4. Compute real FFT → power spectrum
  5. Detect dominant peaks
  6. Stability test: subsample at 50 % and 25 % of data, compare peak positions
  7. Window-size stability: repeat with half the window

Outputs:
  - plots/fft_spectrum.png
  - reports/fft_peaks.json
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
from scipy.signal import find_peaks


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def compute_power_spectrum(x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return (freqs, power) for a windowed, z-scored signal."""
    x = (x - x.mean()) / (x.std() + 1e-12)
    window = np.hanning(len(x))
    x_win = x * window
    fft = np.fft.rfft(x_win)
    freqs = np.fft.rfftfreq(len(x))
    power = (np.abs(fft) ** 2) / len(x)
    return freqs, power


def top_peaks(freqs: np.ndarray, power: np.ndarray, n: int = 10) -> list[dict]:
    """Find top-n peaks in the power spectrum."""
    peak_idx, props = find_peaks(power, height=power.mean() + power.std())
    if len(peak_idx) == 0:
        return []
    order = np.argsort(power[peak_idx])[::-1][:n]
    results = []
    for i in order:
        idx = peak_idx[i]
        results.append({
            "freq": float(freqs[idx]),
            "power": float(power[idx]),
            "power_norm": float(power[idx] / power.mean()),
            "bin_index": int(idx),
        })
    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="FFT spectral analysis of k sequence")
    ap.add_argument("--data", default="DATA/prime_mod24/primes_mod24.parquet")
    ap.add_argument("--out-plot", default="reports/prime_mod24/fft_spectrum.png")
    ap.add_argument("--out-json", default="reports/prime_mod24/fft_peaks.json")
    ap.add_argument("--n-peaks", type=int, default=10, help="Number of top peaks to report")
    args = ap.parse_args()

    for p in [args.out_plot, args.out_json]:
        Path(p).parent.mkdir(parents=True, exist_ok=True)

    print(f"Loading {args.data} …")
    df = pd.read_parquet(args.data)
    k = df["k"].to_numpy(dtype=np.float64)
    N = len(k)
    print(f"  Sequence length: {N:,}")

    # -----------------------------------------------------------------------
    # Full spectrum
    # -----------------------------------------------------------------------
    freqs, power = compute_power_spectrum(k)
    peaks_full = top_peaks(freqs, power, n=args.n_peaks)
    print(f"  Top peaks (full):")
    for pk in peaks_full[:5]:
        print(f"    freq={pk['freq']:.6f}  power_norm={pk['power_norm']:.2f}x mean")

    # -----------------------------------------------------------------------
    # Stability under subsampling
    # -----------------------------------------------------------------------
    rng = np.random.default_rng(42)
    sub50 = k[rng.choice(N, N // 2, replace=False)]
    sub25 = k[rng.choice(N, N // 4, replace=False)]

    _, power_50 = compute_power_spectrum(sub50)
    freqs_50 = np.fft.rfftfreq(len(sub50))
    peaks_50 = top_peaks(freqs_50, power_50, n=args.n_peaks)

    _, power_25 = compute_power_spectrum(sub25)
    freqs_25 = np.fft.rfftfreq(len(sub25))
    peaks_25 = top_peaks(freqs_25, power_25, n=args.n_peaks)

    # -----------------------------------------------------------------------
    # Window-size stability: use first half of sequence
    # -----------------------------------------------------------------------
    k_half = k[: N // 2]
    freqs_h, power_h = compute_power_spectrum(k_half)
    peaks_half = top_peaks(freqs_h, power_h, n=args.n_peaks)

    # -----------------------------------------------------------------------
    # Save JSON
    # -----------------------------------------------------------------------
    result = {
        "n_total": N,
        "full_spectrum": {
            "top_peaks": peaks_full,
            "mean_power": float(power.mean()),
            "std_power": float(power.std()),
        },
        "subsample_50pct": {"top_peaks": peaks_50},
        "subsample_25pct": {"top_peaks": peaks_25},
        "half_window": {"top_peaks": peaks_half},
    }
    with open(args.out_json, "w") as f:
        json.dump(result, f, indent=2)
    print(f"  → {args.out_json}")

    # -----------------------------------------------------------------------
    # Plot
    # -----------------------------------------------------------------------
    fig, axes = plt.subplots(2, 2, figsize=(14, 8))
    fig.suptitle("FFT Power Spectrum of k = (p² − 1) / 24", fontsize=13)

    def _plot_spectrum(ax, freqs, power, peaks, title, color="steelblue"):
        ax.semilogy(freqs[1:], power[1:], color=color, linewidth=0.6, alpha=0.8)
        for pk in peaks[:5]:
            ax.axvline(pk["freq"], color="red", linewidth=1, alpha=0.7,
                       label=f"f={pk['freq']:.4f} ({pk['power_norm']:.1f}×)")
        ax.set_xlabel("Frequency (cycles / sample)")
        ax.set_ylabel("Power (log scale)")
        ax.set_title(title)
        if peaks:
            ax.legend(fontsize=7)

    _plot_spectrum(axes[0, 0], freqs, power, peaks_full, "Full sequence (N)")
    _plot_spectrum(axes[0, 1], freqs_50, power_50, peaks_50, "Subsample 50%", color="seagreen")
    _plot_spectrum(axes[1, 0], freqs_25, power_25, peaks_25, "Subsample 25%", color="darkorange")
    _plot_spectrum(axes[1, 1], freqs_h, power_h, peaks_half, "First half (window stability)", color="purple")

    plt.tight_layout()
    plt.savefig(args.out_plot, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  → {args.out_plot}")

    print("Done.")


if __name__ == "__main__":
    main()
