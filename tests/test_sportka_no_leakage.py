# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
tests/test_sportka_no_leakage.py — Verify no data leakage in feature building.

Acceptance criteria:
- Walk-forward splits are strictly chronological
- Validation/test features use only training history + past val/test rows
- Global frequency is not computed from the full validation/test split
- Time normalisation uses training max, not local split max
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from sportka.features import (
    N_NUMBERS,
    DRAWN_PER_DRAW,
    global_freq_features,
    rolling_freq_features,
    complex_time_features,
    build_walk_forward_features,
    build_features,
    get_feature_slice,
    _build_label_matrix,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_df(n: int = 200, seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    for i in range(n):
        nums = sorted(
            rng.choice(N_NUMBERS, size=int(DRAWN_PER_DRAW), replace=False) + 1
        )
        rows.append({"draw_index": i, "numbers": list(nums)})
    return pd.DataFrame(rows)


@pytest.fixture
def df200():
    return _make_df(n=200)


# ---------------------------------------------------------------------------
# Test 1: global_freq_features respects train_max_index
# ---------------------------------------------------------------------------

class TestGlobalFreqLeakage:
    def test_train_max_index_limits_data(self, df200):
        """
        global_freq_features with train_max_index should produce different
        (smaller) frequencies than without, because it ignores future draws.
        """
        train_max = 99  # first half
        freq_train = global_freq_features(df200, train_max_index=train_max)
        freq_all = global_freq_features(df200, train_max_index=None)

        # They should differ (future draws change frequencies)
        # In rare cases with random data they might agree, but in expectation they differ
        assert not np.allclose(freq_train, freq_all), (
            "global_freq_features should produce different results when "
            "train_max_index is restricted to first half of data."
        )

    def test_train_split_uses_only_training_draws(self):
        """
        Manually verify: if we add a biased block of future draws,
        train_max_index should prevent those from affecting training frequencies.
        """
        # First 100 draws: number 1 appears rarely (just by chance with seed)
        base_draws = []
        for i in range(100):
            # Exclude number 1 entirely from training draws
            nums = list(range(2, 9))  # numbers 2–8
            base_draws.append({"draw_index": i, "numbers": nums})

        # Next 50 draws: number 1 appears in every draw
        for i in range(100, 150):
            nums = [1, 2, 3, 4, 5, 6, 7]
            base_draws.append({"draw_index": i, "numbers": nums})

        df = pd.DataFrame(base_draws)

        # With train_max_index=99: number 1 should have freq=0
        freq_train = global_freq_features(df, train_max_index=99)
        assert freq_train[0] == pytest.approx(0.0), (
            f"p(1) in training (excl future) should be 0, got {freq_train[0]}"
        )

        # Without restriction: number 1 has positive freq
        freq_all = global_freq_features(df, train_max_index=None)
        assert freq_all[0] > 0, "p(1) with all data should be > 0"


# ---------------------------------------------------------------------------
# Test 2: rolling_freq_features only uses past rows
# ---------------------------------------------------------------------------

class TestRollingLeakage:
    def test_row_does_not_use_itself(self):
        """
        For row_idx=i, rolling window should use rows i-window .. i-1,
        NOT row i itself.
        """
        # Create a draw where number 1 appears ONLY at index 5
        rows = []
        for i in range(10):
            if i == 5:
                nums = [1, 2, 3, 4, 5, 6, 7]
            else:
                nums = [8, 9, 10, 11, 12, 13, 14]
            rows.append({"draw_index": i, "numbers": nums})
        df = pd.DataFrame(rows)

        # Compute rolling freq for row 5 (should NOT include row 5 itself)
        freq_at_5 = rolling_freq_features(df, window=10, row_idx=5)
        assert freq_at_5[0] == pytest.approx(0.0), (
            f"p(1) at row_idx=5 should be 0 (row 5 is excluded), got {freq_at_5[0]}"
        )

        # Compute rolling freq for row 6 (should include row 5)
        freq_at_6 = rolling_freq_features(df, window=10, row_idx=6)
        assert freq_at_6[0] > 0, (
            "p(1) at row_idx=6 should be > 0 (row 5 is in window)"
        )

    def test_does_not_see_future_draws(self, df200):
        """
        Rolling freq at row i should be identical whether df has 200 rows
        or only i rows (future rows must not affect past features).
        """
        row_idx = 50
        df_short = df200.iloc[:row_idx].copy().reset_index(drop=True)
        df_full = df200.copy()

        freq_short = rolling_freq_features(df_short, window=20, row_idx=len(df_short))
        freq_full = rolling_freq_features(df_full, window=20, row_idx=row_idx)

        assert np.allclose(freq_short, freq_full), (
            "Rolling freq should be the same whether future rows are present or not."
        )


# ---------------------------------------------------------------------------
# Test 3: complex_time_features uses training max for normalisation
# ---------------------------------------------------------------------------

class TestTimeNormalisationLeakage:
    def test_normalisation_uses_training_max(self, df200):
        """
        Normalising draw_index by the split-local max creates inconsistent
        scales.  Provide t_max_train and verify consistent results.
        """
        train_df = df200[df200["draw_index"] <= 139].reset_index(drop=True)
        val_df = df200[df200["draw_index"] > 139].reset_index(drop=True)

        t_max_train = float(train_df["draw_index"].max())

        feat_val_correct = complex_time_features(val_df, t_max_train=t_max_train)
        feat_val_leaky = complex_time_features(val_df, t_max_train=None)

        # With t_max_train: val times should be > 1 (since val indices > training)
        # Without t_max_train: they'd be normalised within [0,1] incorrectly
        t_norm_correct = feat_val_correct[:, 0]  # first column is t_norm
        t_norm_leaky = feat_val_leaky[:, 0]

        assert (t_norm_correct > 1.0).any(), (
            "With correct normalisation, val t_norm should exceed 1.0 "
            "(val draws after training period)."
        )
        assert not (t_norm_leaky > 1.0).any(), (
            "Leaky normalisation re-scales within [0,1], hiding the time offset."
        )

    def test_consistent_scale_across_splits(self, df200):
        """
        Train and val features should use the same time normalisation constant.
        """
        train_df = df200[df200["draw_index"] <= 139].reset_index(drop=True)
        val_df = df200[df200["draw_index"] > 139].reset_index(drop=True)
        t_max = float(train_df["draw_index"].max())

        feat_train = complex_time_features(train_df, t_max_train=t_max)
        feat_val = complex_time_features(val_df, t_max_train=t_max)

        # Max t_norm in train should be 1.0 (last train draw / t_max = 1)
        assert abs(feat_train[:, 0].max() - 1.0) < 0.02

        # Min t_norm in val should be > 1 / n_draws (strictly after training)
        assert feat_val[:, 0].min() > feat_train[:, 0].max()


# ---------------------------------------------------------------------------
# Test 4: build_walk_forward_features produces chronological splits
# ---------------------------------------------------------------------------

class TestWalkForwardSplits:
    def test_splits_are_disjoint(self, df200):
        """Train, val, test must have no overlapping draw indices."""
        train_end = 139
        val_end = 169

        (X_tr, y_tr), (X_val, y_val), (X_te, y_te) = build_walk_forward_features(
            df200, train_end=train_end, val_end=val_end, groups=["base"]
        )

        train_df = df200[df200["draw_index"] <= train_end]
        val_df = df200[(df200["draw_index"] > train_end) & (df200["draw_index"] <= val_end)]
        test_df = df200[df200["draw_index"] > val_end]

        assert len(X_tr) == len(train_df), "Train size mismatch"
        assert len(X_val) == len(val_df), "Val size mismatch"
        assert len(X_te) == len(test_df), "Test size mismatch"
        assert len(X_tr) + len(X_val) + len(X_te) == len(df200), "Splits must cover all data"

    def test_train_comes_before_val_comes_before_test(self, df200):
        """Splits must be in chronological order."""
        train_end = 139
        val_end = 169

        train_indices = df200[df200["draw_index"] <= train_end]["draw_index"]
        val_indices = df200[(df200["draw_index"] > train_end) & (df200["draw_index"] <= val_end)]["draw_index"]
        test_indices = df200[df200["draw_index"] > val_end]["draw_index"]

        assert train_indices.max() < val_indices.min(), "All train indices must precede val"
        assert val_indices.max() < test_indices.min(), "All val indices must precede test"

    def test_val_features_do_not_use_future_val_rows(self):
        """
        Feature for val row i should not depend on val row j > i.
        We verify this by checking that global_freq for val rows matches
        the training-restricted frequency, not the future-val-restricted one.
        """
        # Construct data where the future val rows have a strong signal in number 1
        rows = []
        for i in range(100):
            nums = list(range(2, 9))  # no number 1 in training
            rows.append({"draw_index": i, "numbers": nums})
        for i in range(100, 120):
            nums = [1, 2, 3, 4, 5, 6, 7]  # number 1 in val/test
            rows.append({"draw_index": i, "numbers": nums})
        df = pd.DataFrame(rows)

        (X_tr, _), (X_val, _), (X_te, _) = build_walk_forward_features(
            df, train_end=99, val_end=109, groups=["base"]
        )

        # The "base" feature for the first val row should show p(1)=0
        # because number 1 was not drawn in training
        first_val_global_freq = X_val[0, :N_NUMBERS]  # base = global_freq
        assert first_val_global_freq[0] == pytest.approx(0.0, abs=1e-4), (
            f"Val row 0 global freq for number 1 should be 0 (not seen in training), "
            f"got {first_val_global_freq[0]:.4f}. This suggests future leakage."
        )


# ---------------------------------------------------------------------------
# Test 5: get_feature_slice correctness
# ---------------------------------------------------------------------------

class TestFeatureSlice:
    def test_base_winding_slice(self):
        """get_feature_slice should return correct slice for base+winding."""
        groups = ["base", "winding"]
        sl_base = get_feature_slice(groups, "base")
        sl_wind = get_feature_slice(groups, "winding")

        assert sl_base.start == 0
        assert sl_base.stop == N_NUMBERS
        assert sl_wind.start == N_NUMBERS

    def test_base_time_winding_slice(self):
        """Slice ordering: base, time, winding."""
        groups = ["base", "time", "winding"]
        sl_base = get_feature_slice(groups, "base")
        sl_time = get_feature_slice(groups, "time")
        sl_wind = get_feature_slice(groups, "winding")

        assert sl_base.start == 0
        assert sl_time.start == sl_base.stop
        assert sl_wind.start == sl_time.stop

    def test_unknown_group_raises(self):
        with pytest.raises(KeyError):
            get_feature_slice(["base"], "unknown_group")

    def test_slices_non_overlapping(self):
        groups = ["base", "rolling", "expdecay"]
        slices = [get_feature_slice(groups, g) for g in groups]
        ranges = [set(range(s.start, s.stop)) for s in slices]
        # No overlap
        for i in range(len(ranges)):
            for j in range(i + 1, len(ranges)):
                assert not (ranges[i] & ranges[j]), f"Overlap between {groups[i]} and {groups[j]}"
