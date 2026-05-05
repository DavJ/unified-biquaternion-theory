#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
quadratic_test.py

Task 5: Radial / Quadratic Structure Test

Tests whether k = (p^2 - 1) / 24 behaves like a quadratic phase signal.
Since k arises from squaring primes, we compare it against synthetic
sequences of the form  s(n) = (n^2) mod M  for several moduli M,
and also against linear chirp / chirp-z style quadratic signals.

Metrics:
  - Spectral overlap: fraction of shared power-spectrum mass in top-10 peaks
  - Phase coherence: magnitude of normalised cross-correlation at lag 0
  - Pearson r between power spectra (same-length sequences)

Outputs:
  - reports/quadratic_similarity.json
  - plots/quadratic_overlay.png
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
from scipy.stats import pearsonr
from scipy.signal import find_peaks


# ---------------------------------------------------------------------------
# Synthetic signals
# ---------------------------------------------------------------------------

def synth_n2_mod(n: int, modulus: int) -> np.ndarray:
    """Return sequence  (i^2) mod modulus  for i = 0 .. n-1."""
    i = np.arange(n, dtype=np.int64)
    return (i * i % modulus).astype(np.float64)


def synth_chirp(n: int, f0: float = 0.01, f1: float = 0.5) -> np.ndarray:
    """Linear frequency sweep (chirp) from f0 to f1 over n samples."""
    t = np.arange(n) / n
    phase = 2 * np.pi * (f0 * t + 0.5 * (f1 - f0) * t ** 2) * n
    return np.cos(phase)


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def power_spectrum(x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    x = (x - x.mean()) / (x.std() + 1e-12)
    window = np.hanning(len(x))
    fft = np.fft.rfft(x * window)
    freqs = np.fft.rfftfreq(len(x))
    power = np.abs(fft) ** 2 / len(x)
    return freqs, power


def spectral_overlap(power_a: np.ndarray, power_b: np.ndarray, top_k: int = 10) -> float:
    """Fraction of top-k peaks in a that also appear (within ±2 bins) in top-k peaks of b."""
    peak_idx_a = set(np.argsort(power_a)[-top_k:])
    peak_idx_b = set(np.argsort(power_b)[-top_k:])
    expanded_b = set()
    for idx in peak_idx_b:
        expanded_b.update([idx - 2, idx - 1, idx, idx + 1, idx + 2])
    hits = sum(1 for idx in peak_idx_a if idx in expanded_b)
    return hits / top_k


def phase_coherence(a: np.ndarray, b: np.ndarray) -> float:
    """Normalised cross-correlation magnitude at lag 0."""
    a = (a - a.mean()) / (a.std() + 1e-12)
    b = (b - b.mean()) / (b.std() + 1e-12)
    return float(np.dot(a, b) / len(a))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Quadratic structure test of k sequence")
    ap.add_argument("--data", default="data/primes_mod24.parquet")
    ap.add_argument("--n", type=int, default=5000,
                    help="Number of k elements to analyse (default: 5000)")
    ap.add_argument("--out-json", default="reports/quadratic_similarity.json")
    ap.add_argument("--out-plot", default="plots/quadratic_overlay.png")
    args = ap.parse_args()

    for p in [args.out_json, args.out_plot]:
        Path(p).parent.mkdir(parents=True, exist_ok=True)

    print(f"Loading {args.data} …")
    df = pd.read_parquet(args.data)
    k = df["k"].to_numpy(dtype=np.float64)[: args.n]
    n = len(k)
    print(f"  Using first {n} elements.")

    freqs_k, power_k = power_spectrum(k)

    # -----------------------------------------------------------------------
    # Synthetic signals
    # -----------------------------------------------------------------------
    moduli = [24, 60, 120, 240, 2310]   # highly composite numbers (products of small primes)
    synthetics: dict[str, np.ndarray] = {}
    for m in moduli:
        synthetics[f"n2_mod{m}"] = synth_n2_mod(n, m)
    synthetics["chirp"] = synth_chirp(n)
    # Pure quadratic index sequence (k_approx ≈ n^2 / 24)
    synthetics["n2_div24"] = (np.arange(n, dtype=np.float64) ** 2) / 24.0

    # -----------------------------------------------------------------------
    # Compute metrics for each synthetic
    # -----------------------------------------------------------------------
    results = []
    for name, sig in synthetics.items():
        _, power_s = power_spectrum(sig)
        r, p_val = pearsonr(power_k, power_s)
        overlap = spectral_overlap(power_k, power_s, top_k=10)
        coherence = phase_coherence(k, sig)
        results.append({
            "signal": name,
            "spectral_pearson_r": float(r),
            "spectral_pearson_p": float(p_val),
            "spectral_overlap_top10": float(overlap),
            "phase_coherence_lag0": float(coherence),
        })
        print(f"  {name:20s}: r={r:.3f}, overlap={overlap:.2f}, coherence={coherence:.4f}")

    # -----------------------------------------------------------------------
    # Save JSON
    # -----------------------------------------------------------------------
    output = {"n_elements": n, "metrics": results}
    with open(args.out_json, "w") as f:
        json.dump(output, f, indent=2)
    print(f"  → {args.out_json}")

    # -----------------------------------------------------------------------
    # Plot
    # -----------------------------------------------------------------------
    n_synthetics = len(synthetics)
    ncols = 3
    nrows = (n_synthetics + 1 + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(15, 4 * nrows))
    axes = axes.flatten()
    fig.suptitle("k power spectrum vs synthetic quadratic signals", fontsize=12)

    # First panel: k itself
    ax = axes[0]
    ax.semilogy(freqs_k[1:], power_k[1:], color="steelblue", linewidth=0.7, alpha=0.9)
    ax.set_title("k = (p² − 1) / 24")
    ax.set_xlabel("Freq")
    ax.set_ylabel("Power")

    for i, (name, sig) in enumerate(synthetics.items(), start=1):
        _, power_s = power_spectrum(sig)
        ax = axes[i]
        ax.semilogy(freqs_k[1:], power_k[1:], color="steelblue", linewidth=0.6, alpha=0.6, label="k")
        ax.semilogy(freqs_k[1:], power_s[1:], color="darkorange", linewidth=0.6, alpha=0.6, label=name)
        r_val = next(r["spectral_pearson_r"] for r in results if r["signal"] == name)
        ax.set_title(f"{name}\n(r={r_val:.3f})", fontsize=8)
        ax.set_xlabel("Freq")
        ax.legend(fontsize=6)

    # Hide unused axes
    for j in range(len(synthetics) + 1, len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()
    plt.savefig(args.out_plot, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  → {args.out_plot}")

    print("Done.")


if __name__ == "__main__":
    main()
