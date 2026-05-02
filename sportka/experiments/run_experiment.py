#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
sportka/experiments/run_experiment.py — Baseline experiment runner.

Evaluates all standard predictors on a synthetic or provided Sportka dataset
and prints a summary table.

Usage
-----
    python -m sportka.experiments.run_experiment [--draws 1000] [--seed 42]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Ensure repo root is on path when run as a script
# ---------------------------------------------------------------------------
_repo_root = Path(__file__).resolve().parent.parent.parent
if str(_repo_root) not in sys.path:
    sys.path.insert(0, str(_repo_root))

from sportka.features import N_NUMBERS, DRAWN_PER_DRAW
from sportka.models import (
    RandomPredictor,
    GlobalFreqPredictor,
    RollingFreqPredictor,
    ExpDecayFreqPredictor,
    LogisticPredictor,
    MLPPredictor,
)
from sportka.evaluation import compare_predictors, beats_random_baseline


# ---------------------------------------------------------------------------
# Synthetic data generator
# ---------------------------------------------------------------------------

def generate_synthetic_draws(n: int = 1000, seed: int = 42) -> pd.DataFrame:
    """
    Generate synthetic Sportka draws (7 numbers from 1–49, uniform random).

    This is a null model: no predictable pattern exists.

    Parameters
    ----------
    n : Number of draws to generate.
    seed : Random seed.

    Returns
    -------
    DataFrame with columns ['draw_index', 'numbers'].
    """
    rng = np.random.default_rng(seed)
    draws = []
    for i in range(n):
        nums = sorted(rng.choice(N_NUMBERS, size=int(DRAWN_PER_DRAW), replace=False) + 1)
        draws.append({"draw_index": i, "numbers": list(nums)})
    return pd.DataFrame(draws)


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

def run(n_draws: int = 1000, seed: int = 42, n_bootstrap: int = 200) -> pd.DataFrame:
    """
    Run the baseline experiment.

    Returns
    -------
    DataFrame with evaluation results for each predictor.
    """
    df = generate_synthetic_draws(n=n_draws, seed=seed)

    train_end = int(n_draws * 0.7)
    val_end = int(n_draws * 0.85)

    # Convert draw_index to ints matching df
    train_end_idx = int(df["draw_index"].quantile(0.7))
    val_end_idx = int(df["draw_index"].quantile(0.85))

    predictors = [
        RandomPredictor(),
        GlobalFreqPredictor(),
        RollingFreqPredictor(window=52),
        ExpDecayFreqPredictor(decay=0.98),
        LogisticPredictor(groups=["base", "rolling"]),
        MLPPredictor(groups=["base", "rolling"]),
    ]

    results = compare_predictors(
        predictors,
        df,
        train_end=train_end_idx,
        val_end=val_end_idx,
        n_bootstrap=n_bootstrap,
    )
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Sportka baseline experiment")
    parser.add_argument("--draws", type=int, default=1000, help="Number of synthetic draws")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--bootstrap", type=int, default=200, help="Bootstrap samples")
    args = parser.parse_args()

    results = run(n_draws=args.draws, seed=args.seed, n_bootstrap=args.bootstrap)

    print("\n=== Sportka Experiment Results ===\n")
    cols_to_show = ["predictor", "n_test", "prob_sum_mean",
                    "brier_score", "brier_score_ci_lo", "brier_score_ci_hi",
                    "top7_recall", "top7_recall_ci_lo", "top7_recall_ci_hi"]
    available = [c for c in cols_to_show if c in results.columns]
    print(results[available].to_string(index=False, float_format="{:.4f}".format))

    print(f"\n>>> UBT beats random baseline: {beats_random_baseline(results)}")
    print("\nNote: with uniform random data, no predictor should significantly beat random.\n")


if __name__ == "__main__":
    main()
