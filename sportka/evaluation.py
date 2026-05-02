# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
sportka/evaluation.py — Evaluation metrics and reporting for Sportka experiments.

Metrics
-------
- Brier score per number (mean squared error of probability vs label)
- Log-loss per number
- Top-k recall (fraction of drawn numbers among top-k predictions)
- Rank metrics: mean reciprocal rank, NDCG
- Probability sum check (should be ≈ 7)

Controls
--------
- Shuffled-label control: same model, labels permuted randomly
- Reversed-time control: train on future, test on past

Confidence intervals
--------------------
Bootstrap over draws with 1000 re-samples by default.
"""
from __future__ import annotations

import warnings
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

from sportka.features import N_NUMBERS, DRAWN_PER_DRAW

# ---------------------------------------------------------------------------
# Core metrics
# ---------------------------------------------------------------------------

def brier_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Mean Brier score over all numbers and draws.

    Parameters
    ----------
    y_true : shape (n_draws, N_NUMBERS), binary.
    y_pred : shape (n_draws, N_NUMBERS), probabilities (each row sums ≈ 7).

    Notes
    -----
    y_pred is scaled to [0, 1] by dividing by DRAWN_PER_DRAW before computing
    MSE.  This converts the multi-label probability (sum ≈ 7) to a per-number
    probability comparable to the binary label.

    Returns
    -------
    float — lower is better.
    """
    # Scale predictions to [0, 1] by dividing by DRAWN_PER_DRAW for Brier
    p = y_pred / DRAWN_PER_DRAW
    return float(np.mean((p - y_true) ** 2))


def log_loss_multilabel(y_true: np.ndarray, y_pred: np.ndarray, eps: float = 1e-7) -> float:
    """
    Mean binary cross-entropy across all (draw, number) pairs.

    Parameters
    ----------
    y_true : shape (n_draws, N_NUMBERS), binary.
    y_pred : shape (n_draws, N_NUMBERS), probabilities (each row sums ≈ 7).

    Returns
    -------
    float — lower is better.
    """
    p = np.clip(y_pred / DRAWN_PER_DRAW, eps, 1.0 - eps)
    return float(-np.mean(y_true * np.log(p) + (1 - y_true) * np.log(1 - p)))


def top_k_recall(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    k: int = 7,
) -> float:
    """
    Fraction of drawn numbers that appear in the top-k predicted numbers.

    For each draw, take the k numbers with highest predicted probability.
    Count how many of the truly drawn numbers appear in that top-k set.
    Average over draws.

    Parameters
    ----------
    y_true : shape (n_draws, N_NUMBERS).
    y_pred : shape (n_draws, N_NUMBERS).
    k : number of top predictions to consider.

    Returns
    -------
    float in [0, 1].
    """
    n = len(y_true)
    recalls = []
    for i in range(n):
        topk = set(np.argsort(y_pred[i])[-k:])
        drawn = set(np.where(y_true[i] > 0)[0])
        if len(drawn) == 0:
            continue
        recalls.append(len(topk & drawn) / len(drawn))
    return float(np.mean(recalls)) if recalls else 0.0


def mean_reciprocal_rank(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Mean reciprocal rank of the first drawn number in the ranked prediction list.
    """
    mrr_values = []
    n = len(y_true)
    for i in range(n):
        ranking = np.argsort(y_pred[i])[::-1]  # descending
        drawn = set(np.where(y_true[i] > 0)[0])
        for rank, num_idx in enumerate(ranking, start=1):
            if num_idx in drawn:
                mrr_values.append(1.0 / rank)
                break
    return float(np.mean(mrr_values)) if mrr_values else 0.0


def prob_sum_mean(y_pred: np.ndarray) -> float:
    """Mean sum of probability vector across draws. Should be ≈ 7."""
    return float(y_pred.sum(axis=1).mean())


# ---------------------------------------------------------------------------
# Bootstrap confidence intervals
# ---------------------------------------------------------------------------

def bootstrap_metric(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    metric_fn,
    n_bootstrap: int = 1000,
    alpha: float = 0.05,
    seed: int = 42,
) -> Tuple[float, float, float]:
    """
    Compute point estimate and bootstrap confidence interval for a metric.

    Returns
    -------
    (point_estimate, ci_lower, ci_upper)
    """
    rng = np.random.default_rng(seed)
    n = len(y_true)
    point = metric_fn(y_true, y_pred)

    boot_values = []
    for _ in range(n_bootstrap):
        idx = rng.integers(0, n, size=n)
        boot_values.append(metric_fn(y_true[idx], y_pred[idx]))

    lo = float(np.percentile(boot_values, 100 * alpha / 2))
    hi = float(np.percentile(boot_values, 100 * (1 - alpha / 2)))
    return point, lo, hi


# ---------------------------------------------------------------------------
# Control experiments
# ---------------------------------------------------------------------------

def shuffled_label_control(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    metric_fn,
    n_shuffles: int = 100,
    seed: int = 0,
) -> Tuple[float, float]:
    """
    Compute metric with randomly shuffled labels.

    Returns
    -------
    (mean_shuffled, std_shuffled)
    """
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(n_shuffles):
        idx = rng.permutation(len(y_true))
        vals.append(metric_fn(y_true[idx], y_pred))
    return float(np.mean(vals)), float(np.std(vals))


def reversed_time_control(
    df: pd.DataFrame,
    predictor,
    metric_fn,
    train_frac: float = 0.7,
) -> float:
    """
    Train on future data, test on past data (time-reversed).

    This is a sanity control: a good predictor should NOT perform better
    when trained on the future.  If it does, there is data leakage.

    Returns
    -------
    metric value on the time-reversed test set.
    """
    from sportka.features import _build_label_matrix, build_features, N_NUMBERS

    df_rev = df.sort_values("draw_index", ascending=False).reset_index(drop=True)
    n = len(df_rev)
    split = int(n * train_frac)

    train_df = df_rev.iloc[:split].copy()
    test_df = df_rev.iloc[split:].copy()

    predictor.fit(train_df)
    groups = getattr(predictor, "groups", ["base"])
    X_test = build_features(
        test_df,
        groups=groups,
        train_max_index=int(train_df["draw_index"].max()),
        t_max_train=float(train_df["draw_index"].max()),
    )
    y_test = _build_label_matrix(test_df)
    y_pred = predictor.predict_proba_matrix(test_df)
    return metric_fn(y_test, y_pred)


# ---------------------------------------------------------------------------
# Full evaluation report
# ---------------------------------------------------------------------------

def evaluate_predictor(
    predictor,
    df: pd.DataFrame,
    train_end: int,
    val_end: int,
    n_bootstrap: int = 500,
) -> Dict:
    """
    Evaluate a predictor using walk-forward splits.

    Returns a dict with:
    - prob_sum_mean
    - brier_score (point, ci_lower, ci_upper)
    - log_loss (point, ci_lower, ci_upper)
    - top7_recall (point, ci_lower, ci_upper)
    - mrr (point, ci_lower, ci_upper)
    """
    from sportka.features import build_walk_forward_features, _build_label_matrix

    groups = getattr(predictor, "groups", ["base"])

    (X_train, y_train), (X_val, y_val), (X_test, y_test) = build_walk_forward_features(
        df,
        train_end=train_end,
        val_end=val_end,
        groups=groups,
    )

    train_df = df[df["draw_index"] <= train_end].sort_values("draw_index").reset_index(drop=True)
    predictor.fit(train_df)

    test_df = df[df["draw_index"] > val_end].sort_values("draw_index").reset_index(drop=True)
    if len(test_df) == 0:
        warnings.warn("Empty test split.")
        return {"error": "empty test split"}

    y_pred = predictor.predict_proba_matrix(test_df)

    metrics: Dict = {
        "predictor": predictor.name,
        "n_test": len(test_df),
        "prob_sum_mean": prob_sum_mean(y_pred),
    }

    for metric_name, metric_fn in [
        ("brier_score", brier_score),
        ("log_loss", log_loss_multilabel),
        ("top7_recall", lambda yt, yp: top_k_recall(yt, yp, k=7)),
        ("mrr", mean_reciprocal_rank),
    ]:
        pt, lo, hi = bootstrap_metric(y_test, y_pred, metric_fn, n_bootstrap=n_bootstrap)
        metrics[metric_name] = {"point": pt, "ci_lower": lo, "ci_upper": hi}

    return metrics


def compare_predictors(
    predictors: List,
    df: pd.DataFrame,
    train_end: int,
    val_end: int,
    n_bootstrap: int = 500,
) -> pd.DataFrame:
    """
    Evaluate multiple predictors and return a comparison DataFrame.

    Parameters
    ----------
    predictors : List of predictor instances.
    df : Full dataset sorted by draw_index.
    train_end, val_end : Split boundaries.

    Returns
    -------
    DataFrame with one row per predictor and columns for each metric.
    """
    rows = []
    for pred in predictors:
        result = evaluate_predictor(pred, df, train_end=train_end, val_end=val_end,
                                    n_bootstrap=n_bootstrap)
        row = {"predictor": result.get("predictor", str(pred))}
        row["n_test"] = result.get("n_test", 0)
        row["prob_sum_mean"] = result.get("prob_sum_mean", np.nan)
        for m in ["brier_score", "log_loss", "top7_recall", "mrr"]:
            d = result.get(m, {})
            row[m] = d.get("point", np.nan)
            row[f"{m}_ci_lo"] = d.get("ci_lower", np.nan)
            row[f"{m}_ci_hi"] = d.get("ci_upper", np.nan)
        rows.append(row)
    return pd.DataFrame(rows)


def beats_random_baseline(results_df: pd.DataFrame) -> bool:
    """
    Return True if any non-random predictor significantly beats
    the random baseline on Brier score.

    Significance: model CI upper < random CI lower.
    """
    if "random_uniform" not in results_df["predictor"].values:
        return False
    rand_row = results_df[results_df["predictor"] == "random_uniform"].iloc[0]
    rand_lo = rand_row.get("brier_score_ci_lo", np.nan)

    for _, row in results_df.iterrows():
        if row["predictor"] == "random_uniform":
            continue
        model_hi = row.get("brier_score_ci_hi", np.nan)
        if not np.isnan(model_hi) and not np.isnan(rand_lo) and model_hi < rand_lo:
            return True
    return False
