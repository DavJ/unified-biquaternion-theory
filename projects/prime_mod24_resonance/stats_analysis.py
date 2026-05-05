#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
stats_analysis.py

Task 2: Basic statistical structure of the k = (p^2 - 1) / 24 sequence.

Computes:
  - Distribution and histogram of k
  - Histogram of k mod small bases (2, 3, 5, 7, 11, 13)
  - Autocorrelation of the k sequence
  - Pearson correlation: k vs log(p)  and  k vs prime index

Outputs:
  - reports/stats_summary.json
  - plots/k_distribution.png
  - plots/k_autocorrelation.png
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats as sp_stats


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def autocorrelation(x: np.ndarray, max_lag: int) -> np.ndarray:
    """Return normalised autocorrelation for lags 0..max_lag."""
    x = x - x.mean()
    var = np.dot(x, x)
    if var == 0:
        return np.zeros(max_lag + 1)
    acf = np.array([np.dot(x[: len(x) - lag], x[lag:]) / var for lag in range(max_lag + 1)])
    return acf


def chi2_uniformity(counts: np.ndarray) -> dict:
    """Chi-squared test of uniformity over residue classes."""
    expected = np.full_like(counts, counts.mean(), dtype=float)
    chi2, p = sp_stats.chisquare(counts, expected)
    return {"chi2": float(chi2), "p_value": float(p), "dof": int(len(counts) - 1)}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Statistical analysis of prime mod-24 sequence")
    ap.add_argument("--data", default="DATA/prime_mod24/primes_mod24.parquet",
                    help="Input Parquet (default: DATA/prime_mod24/primes_mod24.parquet)")
    ap.add_argument("--max-lag", type=int, default=200,
                    help="Maximum lag for autocorrelation (default: 200)")
    ap.add_argument("--out-json", default="reports/prime_mod24/stats_summary.json")
    ap.add_argument("--out-dist", default="reports/prime_mod24/k_distribution.png")
    ap.add_argument("--out-acf", default="reports/prime_mod24/k_autocorr.png")
    args = ap.parse_args()

    for p in [args.out_json, args.out_dist, args.out_acf]:
        Path(p).parent.mkdir(parents=True, exist_ok=True)

    print(f"Loading {args.data} …")
    df = pd.read_parquet(args.data)
    k = df["k"].to_numpy(dtype=np.float64)
    log_p = df["log_p"].to_numpy(dtype=np.float64)
    idx = np.arange(len(k), dtype=np.float64)

    # -----------------------------------------------------------------------
    # 1. Basic descriptive stats
    # -----------------------------------------------------------------------
    desc = {
        "n_primes": int(len(k)),
        "k_min": int(k.min()),
        "k_max": int(k.max()),
        "k_mean": float(k.mean()),
        "k_std": float(k.std()),
        "k_median": float(np.median(k)),
    }
    print("  Descriptive stats:", desc)

    # -----------------------------------------------------------------------
    # 2. k mod small bases
    # -----------------------------------------------------------------------
    small_bases = [2, 3, 5, 7, 11, 13]
    mod_stats: dict = {}
    for b in small_bases:
        residues = (k.astype(np.int64) % b)
        counts = np.bincount(residues, minlength=b).astype(float)
        chi2_result = chi2_uniformity(counts)
        mod_stats[f"mod_{b}"] = {
            "counts": counts.tolist(),
            "chi2_uniformity": chi2_result,
        }
    print("  Mod-base chi2 done.")

    # -----------------------------------------------------------------------
    # 3. Autocorrelation of k
    # -----------------------------------------------------------------------
    acf = autocorrelation(k, args.max_lag)

    # Ljung-Box-style statistic (simplified): sum of squared ACF values beyond lag 0
    lb_stat = float(len(k) * np.sum(acf[1:] ** 2 / (len(k) - np.arange(1, args.max_lag + 1))))
    acf_stats = {
        "max_lag": args.max_lag,
        "acf_lag1": float(acf[1]),
        "acf_lag2": float(acf[2]),
        "acf_lag5": float(acf[5]),
        "ljung_box_stat": lb_stat,
    }

    # -----------------------------------------------------------------------
    # 4. Correlations
    # -----------------------------------------------------------------------
    r_logp, p_logp = sp_stats.pearsonr(k, log_p)
    r_idx, p_idx = sp_stats.pearsonr(k, idx)
    correlation_stats = {
        "k_vs_logp": {"r": float(r_logp), "p_value": float(p_logp)},
        "k_vs_index": {"r": float(r_idx), "p_value": float(p_idx)},
    }
    print(f"  Correlation k vs log(p): r={r_logp:.4f}, p={p_logp:.2e}")
    print(f"  Correlation k vs index:  r={r_idx:.4f}, p={p_idx:.2e}")

    # -----------------------------------------------------------------------
    # Save JSON report
    # -----------------------------------------------------------------------
    summary = {
        "descriptive": desc,
        "mod_bases": mod_stats,
        "autocorrelation": acf_stats,
        "correlations": correlation_stats,
    }
    with open(args.out_json, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"  → {args.out_json}")

    # -----------------------------------------------------------------------
    # Plot 1: k distribution
    # -----------------------------------------------------------------------
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    fig.suptitle("k = (p² - 1) / 24  distribution and mod-base residues", fontsize=13)

    # Main histogram (log scale for y)
    ax = axes[0, 0]
    ax.hist(k, bins=100, color="steelblue", edgecolor="none", alpha=0.8)
    ax.set_yscale("log")
    ax.set_xlabel("k")
    ax.set_ylabel("count (log scale)")
    ax.set_title("k histogram")

    # Mod residues
    for i, b in enumerate(small_bases[1:]):   # skip mod 2 (trivial for p>3)
        r = i + 1
        ax = axes[r // 3, r % 3]
        residues = (k.astype(np.int64) % b)
        counts = np.bincount(residues, minlength=b)
        chi2_val = mod_stats[f"mod_{b}"]["chi2_uniformity"]["chi2"]
        pval = mod_stats[f"mod_{b}"]["chi2_uniformity"]["p_value"]
        ax.bar(np.arange(b), counts, color="coral")
        ax.set_xlabel(f"k mod {b}")
        ax.set_ylabel("count")
        ax.set_title(f"k mod {b}  (χ²={chi2_val:.1f}, p={pval:.3f})")

    plt.tight_layout()
    plt.savefig(args.out_dist, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  → {args.out_dist}")

    # -----------------------------------------------------------------------
    # Plot 2: autocorrelation
    # -----------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 4))
    lags = np.arange(len(acf))
    ax.bar(lags, acf, width=1.0, color="steelblue", alpha=0.7)
    conf = 1.96 / np.sqrt(len(k))
    ax.axhline(conf, color="red", linestyle="--", linewidth=1, label=f"±95% CI ({conf:.4f})")
    ax.axhline(-conf, color="red", linestyle="--", linewidth=1)
    ax.axhline(0, color="black", linewidth=0.5)
    ax.set_xlabel("Lag")
    ax.set_ylabel("ACF")
    ax.set_title("Autocorrelation of k = (p² − 1) / 24 sequence")
    ax.legend()
    plt.tight_layout()
    plt.savefig(args.out_acf, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  → {args.out_acf}")

    print("Done.")


if __name__ == "__main__":
    main()
