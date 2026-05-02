# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
tests/test_sportka_probability_scaling.py — Verify correct probability scaling.

Acceptance criteria:
- RandomPredictor: sum(probs) == 7 exactly
- GlobalFreqPredictor: sum(probs) ≈ 7 (within 0.5)
- RollingFreqPredictor: sum(probs) ≈ 7 (within 0.5)
- ExpDecayFreqPredictor: sum(probs) ≈ 7 (within 0.5)
- None of the above normalise to 1 (which would be wrong for multi-label)
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from sportka.features import N_NUMBERS, DRAWN_PER_DRAW
from sportka.models import (
    RandomPredictor,
    GlobalFreqPredictor,
    RollingFreqPredictor,
    ExpDecayFreqPredictor,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_df(n: int = 200, seed: int = 42) -> pd.DataFrame:
    """Generate synthetic draw DataFrame."""
    rng = np.random.default_rng(seed)
    rows = []
    for i in range(n):
        nums = sorted(
            rng.choice(N_NUMBERS, size=int(DRAWN_PER_DRAW), replace=False) + 1
        )
        rows.append({"draw_index": i, "numbers": list(nums)})
    return pd.DataFrame(rows)


@pytest.fixture
def df():
    return _make_df(n=200)


# ---------------------------------------------------------------------------
# Probability sum tests
# ---------------------------------------------------------------------------

class TestRandomPredictor:
    def test_prob_sum_exactly_7(self, df):
        pred = RandomPredictor()
        probs = pred.predict(df)
        assert probs.shape == (N_NUMBERS,), "Output shape must be (49,)"
        assert abs(probs.sum() - 7.0) < 1e-6, (
            f"RandomPredictor prob sum should be exactly 7, got {probs.sum():.6f}"
        )

    def test_all_probs_equal(self, df):
        pred = RandomPredictor()
        probs = pred.predict(df)
        expected = DRAWN_PER_DRAW / N_NUMBERS
        assert np.allclose(probs, expected), (
            f"RandomPredictor should be uniform at {expected:.6f}"
        )

    def test_matrix_row_sum(self, df):
        pred = RandomPredictor()
        mat = pred.predict_proba_matrix(df)
        row_sums = mat.sum(axis=1)
        assert np.allclose(row_sums, 7.0), "Each row of proba matrix should sum to 7"

    def test_not_normalised_to_1(self, df):
        pred = RandomPredictor()
        probs = pred.predict(df)
        assert abs(probs.sum() - 1.0) > 1.0, (
            "RandomPredictor should NOT normalise to 1 (multi-label, not single-class)"
        )


class TestGlobalFreqPredictor:
    def test_prob_sum_close_to_7(self, df):
        pred = GlobalFreqPredictor()
        pred.fit(df)
        probs = pred.predict(df)
        assert probs.shape == (N_NUMBERS,)
        s = probs.sum()
        assert abs(s - 7.0) < 0.5, (
            f"GlobalFreqPredictor prob sum should be ≈7, got {s:.4f}"
        )

    def test_not_normalised_to_1(self, df):
        pred = GlobalFreqPredictor()
        pred.fit(df)
        probs = pred.predict(df)
        assert abs(probs.sum() - 1.0) > 1.0, (
            "GlobalFreqPredictor should NOT normalise to 1"
        )

    def test_uses_count_over_n_draws(self):
        """Manual check: freq / n_draws, not freq / total_hits."""
        # 3 draws, number 1 appears twice → p(1) = 2/3
        data = pd.DataFrame([
            {"draw_index": 0, "numbers": [1, 2, 3, 4, 5, 6, 7]},
            {"draw_index": 1, "numbers": [1, 8, 9, 10, 11, 12, 13]},
            {"draw_index": 2, "numbers": [14, 15, 16, 17, 18, 19, 20]},
        ])
        pred = GlobalFreqPredictor()
        pred.fit(data)
        probs = pred.predict(data)
        # p(1) = 2 / 3 ≈ 0.667, NOT 2/21 ≈ 0.095 (total_hits denominator)
        assert abs(probs[0] - 2 / 3) < 0.01, (
            f"p(number=1) should be 2/3, got {probs[0]:.4f}"
        )
        # Total sum should be 7 (3 draws × 7/draw = 21 hits / 3 draws = 7)
        assert abs(probs.sum() - 7.0) < 0.5

    def test_matrix_mean_sum_close_to_7(self, df):
        pred = GlobalFreqPredictor()
        pred.fit(df)
        mat = pred.predict_proba_matrix(df)
        mean_sum = mat.sum(axis=1).mean()
        assert abs(mean_sum - 7.0) < 0.5, (
            f"Mean probability sum should be ≈7, got {mean_sum:.4f}"
        )


class TestRollingFreqPredictor:
    def test_prob_sum_close_to_7(self, df):
        pred = RollingFreqPredictor(window=52)
        probs = pred.predict(df)
        s = probs.sum()
        assert abs(s - 7.0) < 0.5, (
            f"RollingFreqPredictor prob sum should be ≈7, got {s:.4f}"
        )

    def test_not_normalised_to_1(self, df):
        pred = RollingFreqPredictor(window=52)
        probs = pred.predict(df)
        assert abs(probs.sum() - 1.0) > 1.0

    def test_divides_by_window_draws_not_window_times_7(self):
        """
        Critical: should divide by n_draws_in_window, NOT by window * 7.
        """
        # 10 draws, window=10, each draw contains exactly 7 numbers
        # Each number 1–49 should appear ≈ 10*7/49 ≈ 1.43 times
        # p(k) = count_k / 10 → sum ≈ 7
        # WRONG: p(k) = count_k / (10 * 7) → sum ≈ 1
        n = 50
        data = _make_df(n=n)
        pred = RollingFreqPredictor(window=10)
        mat = pred.predict_proba_matrix(data)
        # For rows with at least 10 past draws, mean sum should be near 7
        mean_sum = mat[10:].sum(axis=1).mean()
        assert abs(mean_sum - 7.0) < 1.0, (
            f"Rolling freq mean prob sum should be ≈7, got {mean_sum:.4f}. "
            "If it's ≈1, dividing by window*7 instead of window."
        )

    def test_matrix_mean_sum_close_to_7(self, df):
        pred = RollingFreqPredictor(window=52)
        mat = pred.predict_proba_matrix(df)
        # Skip first few rows where window is small
        mean_sum = mat[52:].sum(axis=1).mean()
        assert abs(mean_sum - 7.0) < 1.0


class TestExpDecayFreqPredictor:
    def test_prob_sum_close_to_7(self, df):
        pred = ExpDecayFreqPredictor(decay=0.98)
        probs = pred.predict(df)
        s = probs.sum()
        assert abs(s - 7.0) < 0.5, (
            f"ExpDecayFreqPredictor prob sum should be ≈7, got {s:.4f}"
        )

    def test_not_normalised_to_1(self, df):
        pred = ExpDecayFreqPredictor(decay=0.98)
        probs = pred.predict(df)
        assert abs(probs.sum() - 1.0) > 1.0

    def test_divides_by_total_weight_not_total_weight_times_7(self):
        """
        Critical: should divide by total_weight, NOT total_weight * 7.
        """
        n = 50
        data = _make_df(n=n)
        pred = ExpDecayFreqPredictor(decay=0.98)
        mat = pred.predict_proba_matrix(data)
        mean_sum = mat[10:].sum(axis=1).mean()
        assert abs(mean_sum - 7.0) < 1.0, (
            f"ExpDecay mean prob sum should be ≈7, got {mean_sum:.4f}. "
            "If ≈1, dividing by total_weight*7 instead of total_weight."
        )

    def test_matrix_mean_sum_close_to_7(self, df):
        pred = ExpDecayFreqPredictor(decay=0.98)
        mat = pred.predict_proba_matrix(df)
        mean_sum = mat[10:].sum(axis=1).mean()
        assert abs(mean_sum - 7.0) < 1.0


# ---------------------------------------------------------------------------
# Cross-predictor consistency
# ---------------------------------------------------------------------------

class TestProbabilitySumConsistency:
    """All predictors must agree on the ≈7 sum convention."""

    @pytest.mark.parametrize("pred_cls", [
        RandomPredictor,
        GlobalFreqPredictor,
        RollingFreqPredictor,
        ExpDecayFreqPredictor,
    ])
    def test_all_predictors_sum_near_7(self, df, pred_cls):
        pred = pred_cls()
        if hasattr(pred, "fit"):
            pred.fit(df)
        probs = pred.predict(df)
        s = probs.sum()
        assert abs(s - 7.0) < 0.5, (
            f"{pred_cls.__name__} prob sum = {s:.4f}, expected ≈7"
        )
