#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
null_models.py

Task 7: Null models — baselines for avoiding false positives.

Generates three null baselines:
  (a) random_primes   — random integers with same prime-count density, compute k_rand
  (b) shuffled_k      — same k values as real data but randomly permuted
  (c) random_quadratic — (n^2) / 24 for random integers n drawn from [5, p_max]

For each baseline:
  - Compute FFT power spectrum
  - Find top peaks
  - Compute cross-correlation with Riemann zeta zeros (optional, fast version)
  - Pearson correlation of power spectra vs real k

Outputs:
  - reports/null_comparison.json
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
# Helpers (same as spectrum_analysis / compare_zeta)
# ---------------------------------------------------------------------------

def power_spectrum(x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    x = (x - x.mean()) / (x.std() + 1e-12)
    window = np.hanning(len(x))
    fft = np.fft.rfft(x * window)
    freqs = np.fft.rfftfreq(len(x))
    power = np.abs(fft) ** 2 / len(x)
    return freqs, power


def top_n_peaks(power: np.ndarray, n: int = 5) -> list[int]:
    peak_idx, _ = find_peaks(power, height=power.mean() + power.std())
    if len(peak_idx) == 0:
        return []
    order = np.argsort(power[peak_idx])[::-1][:n]
    return [int(peak_idx[i]) for i in order]


def spectral_overlap(power_a: np.ndarray, power_b: np.ndarray, top_k: int = 10) -> float:
    peak_a = set(np.argsort(power_a)[-top_k:])
    peak_b_exp = set()
    for idx in np.argsort(power_b)[-top_k:]:
        peak_b_exp.update([idx - 2, idx - 1, idx, idx + 1, idx + 2])
    return sum(1 for idx in peak_a if idx in peak_b_exp) / top_k


def cross_corr_lag0(a: np.ndarray, b: np.ndarray) -> float:
    a = (a - a.mean()) / (a.std() + 1e-12)
    b = (b - b.mean()) / (b.std() + 1e-12)
    return float(np.dot(a, b) / len(a))


# ---------------------------------------------------------------------------
# Null sequence generators
# ---------------------------------------------------------------------------

def make_random_primes_k(n: int, p_max: int, rng: np.random.Generator) -> np.ndarray:
    """
    Approximate null: draw n odd integers > 3 coprime to 6 (p ≡ 1,5 mod 6),
    then compute k = (p^2 - 1) // 24.
    This mimics the form of real k but uses non-prime quadratics.
    """
    # Generate candidates of the form 6m+1 and 6m+5 (same residue classes as primes > 3)
    m = np.arange(1, p_max // 6 + 1, dtype=np.int64)
    cands = np.concatenate([6 * m + 1, 6 * m + 5])
    cands = cands[cands > 3]
    idx = rng.choice(len(cands), size=min(n, len(cands)), replace=False)
    p_rand = np.sort(cands[idx])[:n]
    k_rand = (p_rand ** 2 - 1) // 24
    return k_rand.astype(np.float64)


def make_shuffled_k(k: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    return rng.permutation(k)


def make_random_quadratic(n: int, p_max: int, rng: np.random.Generator) -> np.ndarray:
    """Random integers drawn uniformly from [5, p_max], then k = (p^2 - 1) / 24."""
    p_rand = rng.integers(5, p_max, size=n)
    return ((p_rand.astype(np.int64) ** 2 - 1) / 24.0)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Null models for prime mod-24 resonance")
    ap.add_argument("--data", default="DATA/prime_mod24/primes_mod24.parquet")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--n-reps", type=int, default=50,
                    help="Number of random realisations per null model (default: 50)")
    ap.add_argument("--out-json", default="reports/prime_mod24/null_comparison.json")
    ap.add_argument("--out-plot", default="reports/prime_mod24/null_comparison.png")
    args = ap.parse_args()

    for p in [args.out_json, args.out_plot]:
        Path(p).parent.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(args.seed)

    print(f"Loading {args.data} …")
    df = pd.read_parquet(args.data)
    k = df["k"].to_numpy(dtype=np.float64)
    n = len(k)
    p_max = int(df["p"].max())
    print(f"  n={n:,}, p_max={p_max:,}")

    freqs_k, power_k = power_spectrum(k)
    peaks_k = top_n_peaks(power_k, n=10)

    # -----------------------------------------------------------------------
    # Run null models
    # -----------------------------------------------------------------------
    null_results: dict = {}

    for label, gen_fn in [
        ("random_primes", lambda: make_random_primes_k(n, p_max, rng)),
        ("shuffled_k",    lambda: make_shuffled_k(k, rng)),
        ("random_quadratic", lambda: make_random_quadratic(n, p_max, rng)),
    ]:
        pearson_rs = []
        overlaps = []
        coherences = []

        for rep in range(args.n_reps):
            null_k = gen_fn()
            _, power_null = power_spectrum(null_k)
            r, _ = pearsonr(power_k, power_null)
            overlap = spectral_overlap(power_k, power_null, top_k=10)
            coh = cross_corr_lag0(k, null_k)
            pearson_rs.append(float(r))
            overlaps.append(float(overlap))
            coherences.append(float(coh))

        null_results[label] = {
            "n_reps": args.n_reps,
            "spectral_pearson_r": {
                "mean": float(np.mean(pearson_rs)),
                "std": float(np.std(pearson_rs)),
                "max": float(np.max(pearson_rs)),
            },
            "spectral_overlap_top10": {
                "mean": float(np.mean(overlaps)),
                "std": float(np.std(overlaps)),
            },
            "phase_coherence_lag0": {
                "mean": float(np.mean(coherences)),
                "std": float(np.std(coherences)),
            },
        }
        print(f"  {label}: r={np.mean(pearson_rs):.3f}±{np.std(pearson_rs):.3f}, "
              f"overlap={np.mean(overlaps):.2f}±{np.std(overlaps):.2f}")

    # -----------------------------------------------------------------------
    # Save JSON
    # -----------------------------------------------------------------------
    output = {
        "real_k_n": n,
        "null_models": null_results,
        "seed": args.seed,
        "note": (
            "These null models establish baselines for spectral and correlation metrics. "
            "Any signal in the real k sequence must exceed the null distributions to be "
            "considered non-random."
        ),
    }
    with open(args.out_json, "w") as f:
        json.dump(output, f, indent=2)
    print(f"  → {args.out_json}")

    # -----------------------------------------------------------------------
    # Plot: distribution of null Pearson r values
    # -----------------------------------------------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    fig.suptitle("Null model distributions (spectral Pearson r)", fontsize=12)

    plot_models = [
        ("random_primes",    lambda: make_random_primes_k(n, p_max, rng)),
        ("shuffled_k",       lambda: make_shuffled_k(k, rng)),
        ("random_quadratic", lambda: make_random_quadratic(n, p_max, rng)),
    ]
    for ax, (label_str, gen_fn) in zip(axes, plot_models):
        rs = []
        for _ in range(args.n_reps):
            null_k = gen_fn()
            _, pw = power_spectrum(null_k)
            r, _ = pearsonr(power_k, pw)
            rs.append(float(r))
        ax.hist(rs, bins=20, color="steelblue", edgecolor="white", alpha=0.8)
        ax.set_xlabel("Pearson r (vs real k spectrum)")
        ax.set_title(label_str)
        ax.axvline(np.mean(rs), color="red", linewidth=1.5, linestyle="--",
                   label=f"mean={np.mean(rs):.3f}")
        ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(args.out_plot, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  → {args.out_plot}")

    print("Done.")


if __name__ == "__main__":
    main()
