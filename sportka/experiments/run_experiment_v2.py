#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
sportka/experiments/run_experiment_v2.py — Full UBT-enhanced experiment runner.

Extends run_experiment.py with:
- UBT theta-transform augmented models
- Shuffled-label and reversed-time controls
- Walk-forward feature building (no leakage)
- Full metric table including confidence intervals

Usage
-----
    python -m sportka.experiments.run_experiment_v2 [--draws 1000] [--report PATH]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

_repo_root = Path(__file__).resolve().parent.parent.parent
if str(_repo_root) not in sys.path:
    sys.path.insert(0, str(_repo_root))

from sportka.features import N_NUMBERS, DRAWN_PER_DRAW, _build_label_matrix
from sportka.models import (
    RandomPredictor,
    GlobalFreqPredictor,
    RollingFreqPredictor,
    ExpDecayFreqPredictor,
    LogisticPredictor,
    MLPPredictor,
    UBTMLPPredictor,
)
from sportka.evaluation import (
    compare_predictors,
    beats_random_baseline,
    brier_score,
    shuffled_label_control,
    reversed_time_control,
    prob_sum_mean,
)
from sportka.experiments.run_experiment import generate_synthetic_draws


# ---------------------------------------------------------------------------
# Control summary
# ---------------------------------------------------------------------------

def run_controls(
    predictor,
    df: pd.DataFrame,
    train_end_idx: int,
    val_end_idx: int,
) -> dict:
    """
    Run shuffled-label and reversed-time controls.

    Returns dict with keys:
    - shuffled_mean, shuffled_std
    - reversed_brier
    """
    train_df = df[df["draw_index"] <= train_end_idx].reset_index(drop=True)
    test_df = df[df["draw_index"] > val_end_idx].reset_index(drop=True)

    if len(test_df) == 0:
        return {"shuffled_mean": np.nan, "shuffled_std": np.nan, "reversed_brier": np.nan}

    predictor.fit(train_df)
    y_pred = predictor.predict_proba_matrix(test_df)
    y_true = _build_label_matrix(test_df)

    sh_mean, sh_std = shuffled_label_control(y_true, y_pred, brier_score)
    rev_brier = reversed_time_control(df, predictor, brier_score)

    return {
        "shuffled_mean": sh_mean,
        "shuffled_std": sh_std,
        "reversed_brier": rev_brier,
    }


# ---------------------------------------------------------------------------
# Main experiment v2
# ---------------------------------------------------------------------------

def run_v2(
    n_draws: int = 1000,
    seed: int = 42,
    n_bootstrap: int = 200,
) -> tuple:
    """
    Run full experiment with UBT models and controls.

    Returns
    -------
    (results_df, controls_df)
    """
    df = generate_synthetic_draws(n=n_draws, seed=seed)

    train_end_idx = int(df["draw_index"].quantile(0.7))
    val_end_idx = int(df["draw_index"].quantile(0.85))

    predictors = [
        RandomPredictor(),
        GlobalFreqPredictor(),
        RollingFreqPredictor(window=52),
        ExpDecayFreqPredictor(decay=0.98),
        LogisticPredictor(groups=["base", "rolling"]),
        MLPPredictor(groups=["base", "rolling"], hidden_layer_sizes=(128, 64)),
        UBTMLPPredictor(groups=["base", "rolling"], hidden_layer_sizes=(256, 128)),
    ]

    results = compare_predictors(
        predictors,
        df,
        train_end=train_end_idx,
        val_end=val_end_idx,
        n_bootstrap=n_bootstrap,
    )

    # Run controls for a representative subset
    control_rows = []
    control_predictors = [RandomPredictor(), GlobalFreqPredictor(), MLPPredictor(groups=["base", "rolling"])]
    for pred in control_predictors:
        ctrl = run_controls(pred, df.copy(), train_end_idx, val_end_idx)
        ctrl["predictor"] = pred.name
        control_rows.append(ctrl)
    controls_df = pd.DataFrame(control_rows)

    return results, controls_df


def _format_report(results: pd.DataFrame, controls: pd.DataFrame, n_draws: int) -> str:
    """Format a Markdown experiment report."""
    lines = [
        "# Sportka UBT Experiment Report (v2)",
        "",
        f"**Dataset**: {n_draws} synthetic draws (uniform random, 7 from 49)",
        "",
        "## Main Results",
        "",
        results.to_markdown(index=False, floatfmt=".4f"),
        "",
        "## Probability Sum Check",
        "",
        "All predictors should have `prob_sum_mean ≈ 7.0`.",
        "",
    ]
    for _, row in results.iterrows():
        ps = row.get("prob_sum_mean", np.nan)
        ok = "✓" if abs(ps - 7.0) < 0.5 else "✗"
        lines.append(f"- {row['predictor']}: {ps:.4f} {ok}")

    lines += [
        "",
        "## Control Experiments",
        "",
        controls.to_markdown(index=False, floatfmt=".4f"),
        "",
        "## Signal Assessment",
        "",
    ]

    beats = beats_random_baseline(results)
    if beats:
        lines.append("**SIGNAL DETECTED**: At least one model significantly beats the random baseline.")
        lines.append("However, on purely random data this should NOT occur — check for leakage.")
    else:
        lines.append("**NO SIGNAL**: No model significantly outperforms the random baseline.")
        lines.append("This is the expected result on uniform random data.")

    lines += [
        "",
        "## Interpretation",
        "",
        "On synthetic uniform-random data, all models should perform at chance level.",
        "The random baseline Brier score provides the null hypothesis reference.",
        "UBT models are evaluated against corrected baselines (prob sum ≈ 7).",
        "",
        "To use real Sportka data, replace `generate_synthetic_draws` with a",
        "real data loader and re-run this script.",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Sportka UBT experiment v2")
    parser.add_argument("--draws", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--bootstrap", type=int, default=200)
    parser.add_argument("--report", type=str, default=None,
                        help="Path to save Markdown report")
    args = parser.parse_args()

    results, controls = run_v2(
        n_draws=args.draws, seed=args.seed, n_bootstrap=args.bootstrap
    )

    print("\n=== Sportka UBT Experiment v2 ===\n")
    cols_to_show = ["predictor", "prob_sum_mean",
                    "brier_score", "brier_score_ci_lo", "brier_score_ci_hi",
                    "top7_recall", "mrr"]
    available = [c for c in cols_to_show if c in results.columns]
    print(results[available].to_string(index=False, float_format="{:.4f}".format))

    print("\n=== Control Experiments ===\n")
    print(controls.to_string(index=False, float_format="{:.4f}".format))

    print(f"\n>>> UBT beats random: {beats_random_baseline(results)}")

    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_text = _format_report(results, controls, args.draws)
        report_path.write_text(report_text)
        print(f"\nReport saved to: {args.report}")


if __name__ == "__main__":
    main()
