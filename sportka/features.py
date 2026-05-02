# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
sportka/features.py — Feature engineering for Sportka lottery prediction.

Sportka draws 7 numbers (6 main + 1 bonus) from 1–49.
All probability vectors must satisfy: sum(p) ≈ 7.

Key rules
---------
- GlobalFreqPredictor  : p(k) = count_k / n_draws
- RollingFreqPredictor : p(k) = count_k_in_window / n_draws_in_window
- ExpDecayFreqPredictor: p(k) = weighted_count_k / total_weight
- RandomPredictor      : p(k) = 7/49 for all k

Leakage prevention
------------------
All feature builders accept a ``train_max_index`` argument.  When
building features for rows beyond ``train_max_index`` the function must
only use information available up to (but not including) the row being
featurised.  Use :func:`build_walk_forward_features` for the full
train/val/test split.

Time normalisation
------------------
``complex_time_features`` normalises the draw index by the maximum index
seen in the *training* window, not the local split range.  The caller is
responsible for passing ``t_max_train``.
"""
from __future__ import annotations

import math
from typing import List, Optional, Sequence

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
N_NUMBERS = 49          # numbers in the lottery pool
DRAWN_PER_DRAW = 7      # 6 main + 1 bonus drawn each round
EXPECTED_PROB_SUM = float(DRAWN_PER_DRAW)   # ≈ 7.0


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _validate_df(df: pd.DataFrame) -> None:
    """Require columns 'draw_index' and 'numbers' (list of ints)."""
    if "draw_index" not in df.columns:
        raise ValueError("DataFrame must have a 'draw_index' column.")
    if "numbers" not in df.columns:
        raise ValueError("DataFrame must have a 'numbers' column (list of ints).")


def _build_count_matrix(df: pd.DataFrame) -> np.ndarray:
    """Return binary matrix (n_draws, N_NUMBERS); entry [i,k]=1 if number k+1 was drawn in draw i."""
    n = len(df)
    mat = np.zeros((n, N_NUMBERS), dtype=np.float32)
    for i, nums in enumerate(df["numbers"]):
        for num in nums:
            if 1 <= num <= N_NUMBERS:
                mat[i, num - 1] = 1.0
    return mat


# ---------------------------------------------------------------------------
# Global frequency features
# ---------------------------------------------------------------------------

def global_freq_features(df: pd.DataFrame, train_max_index: Optional[int] = None) -> np.ndarray:
    """
    Compute per-number global frequency probabilities.

    Parameters
    ----------
    df : DataFrame with columns ['draw_index', 'numbers'].
    train_max_index : If given, only draws with draw_index <= train_max_index
        are used to compute frequencies (prevents leakage into future splits).

    Returns
    -------
    prob_vec : shape (N_NUMBERS,) with sum ≈ DRAWN_PER_DRAW.
    """
    _validate_df(df)
    if train_max_index is not None:
        src = df[df["draw_index"] <= train_max_index]
    else:
        src = df

    n_draws = len(src)
    if n_draws == 0:
        return np.full(N_NUMBERS, DRAWN_PER_DRAW / N_NUMBERS, dtype=np.float32)

    counts = np.zeros(N_NUMBERS, dtype=np.float64)
    for nums in src["numbers"]:
        for num in nums:
            if 1 <= num <= N_NUMBERS:
                counts[num - 1] += 1.0

    # Correct rule: p(k) = count_k / n_draws  → sum ≈ 7
    return (counts / n_draws).astype(np.float32)


# ---------------------------------------------------------------------------
# Rolling frequency features
# ---------------------------------------------------------------------------

def rolling_freq_features(
    df: pd.DataFrame,
    window: int = 52,
    row_idx: Optional[int] = None,
) -> np.ndarray:
    """
    Compute rolling-window frequency probabilities for a single row.

    Parameters
    ----------
    df : Full DataFrame sorted by draw_index ascending.
    window : Number of past draws to include.
    row_idx : Integer position in df of the row we are featurising.
        If None, uses the last row.

    Returns
    -------
    prob_vec : shape (N_NUMBERS,) with sum ≈ DRAWN_PER_DRAW.
    """
    _validate_df(df)
    if row_idx is None:
        row_idx = len(df) - 1

    # Only look at past draws (exclude the row itself to avoid leakage)
    start = max(0, row_idx - window)
    past = df.iloc[start:row_idx]

    n_draws_in_window = len(past)
    if n_draws_in_window == 0:
        return np.full(N_NUMBERS, DRAWN_PER_DRAW / N_NUMBERS, dtype=np.float32)

    counts = np.zeros(N_NUMBERS, dtype=np.float64)
    for nums in past["numbers"]:
        for num in nums:
            if 1 <= num <= N_NUMBERS:
                counts[num - 1] += 1.0

    # Correct rule: divide by number of draws in window, not by window * DRAWN_PER_DRAW
    return (counts / n_draws_in_window).astype(np.float32)


def build_rolling_freq_matrix(
    df: pd.DataFrame,
    window: int = 52,
) -> np.ndarray:
    """
    Build rolling-frequency feature matrix for all rows.

    Returns
    -------
    mat : shape (len(df), N_NUMBERS)
    """
    n = len(df)
    mat = np.zeros((n, N_NUMBERS), dtype=np.float32)
    for i in range(n):
        mat[i] = rolling_freq_features(df, window=window, row_idx=i)
    return mat


# ---------------------------------------------------------------------------
# Exponential-decay frequency features
# ---------------------------------------------------------------------------

def exp_decay_freq_features(
    df: pd.DataFrame,
    decay: float = 0.98,
    row_idx: Optional[int] = None,
) -> np.ndarray:
    """
    Compute exponentially-decayed frequency probabilities for a single row.

    Parameters
    ----------
    df : Full DataFrame sorted by draw_index ascending.
    decay : Per-draw decay factor (e.g. 0.98 means 2% decay per draw).
    row_idx : Integer position in df of the row we are featurising.

    Returns
    -------
    prob_vec : shape (N_NUMBERS,) with sum ≈ DRAWN_PER_DRAW.
    """
    _validate_df(df)
    if row_idx is None:
        row_idx = len(df) - 1

    past = df.iloc[:row_idx]
    if len(past) == 0:
        return np.full(N_NUMBERS, DRAWN_PER_DRAW / N_NUMBERS, dtype=np.float32)

    counts = np.zeros(N_NUMBERS, dtype=np.float64)
    total_weight = 0.0
    for offset, row_nums in enumerate(reversed(past["numbers"].tolist())):
        w = decay ** offset
        total_weight += w
        for num in row_nums:
            if 1 <= num <= N_NUMBERS:
                counts[num - 1] += w

    if total_weight == 0:
        return np.full(N_NUMBERS, DRAWN_PER_DRAW / N_NUMBERS, dtype=np.float32)

    # Correct rule: divide by total_weight only (not total_weight * DRAWN_PER_DRAW)
    return (counts / total_weight).astype(np.float32)


def build_exp_decay_matrix(
    df: pd.DataFrame,
    decay: float = 0.98,
) -> np.ndarray:
    """Build exp-decay feature matrix for all rows. Shape (len(df), N_NUMBERS)."""
    n = len(df)
    mat = np.zeros((n, N_NUMBERS), dtype=np.float32)
    for i in range(n):
        mat[i] = exp_decay_freq_features(df, decay=decay, row_idx=i)
    return mat


# ---------------------------------------------------------------------------
# Complex time features
# ---------------------------------------------------------------------------

def complex_time_features(
    df: pd.DataFrame,
    t_max_train: Optional[float] = None,
    periods: Sequence[float] = (7, 52, 365),
) -> np.ndarray:
    """
    Compute complex-time (sin/cos) features for each draw.

    Parameters
    ----------
    df : DataFrame with 'draw_index' column.
    t_max_train : Maximum draw_index seen in the training window.  Used to
        normalise time consistently across train/val/test splits.  If None,
        uses max(df['draw_index']).  Pass the training max to prevent
        scale inconsistency.
    periods : Oscillation periods (in draws) for sin/cos encoding.

    Returns
    -------
    feat : shape (len(df), 1 + 2*len(periods))
        Columns: [t_norm, sin(2π t/T1), cos(2π t/T1), sin(2π t/T2), ...]
    """
    _validate_df(df)
    t = df["draw_index"].values.astype(np.float64)

    if t_max_train is None:
        t_max_train = float(t.max())

    if t_max_train == 0:
        t_norm = np.zeros_like(t)
    else:
        t_norm = t / t_max_train

    cols = [t_norm]
    for p in periods:
        cols.append(np.sin(2 * math.pi * t / p))
        cols.append(np.cos(2 * math.pi * t / p))

    return np.stack(cols, axis=1).astype(np.float32)


# ---------------------------------------------------------------------------
# Winding / torus history features
# ---------------------------------------------------------------------------

def winding_history_features(
    df: pd.DataFrame,
    train_max_index: Optional[int] = None,
    window: int = 10,
) -> np.ndarray:
    """
    Compute "winding" features: relative draw offset modulo small primes.

    Leakage note: global frequency is computed only up to train_max_index.

    Returns
    -------
    feat : shape (len(df), N_NUMBERS + 3*window)
    """
    _validate_df(df)

    global_freq = global_freq_features(df, train_max_index=train_max_index)
    roll = build_rolling_freq_matrix(df, window=window)

    n = len(df)
    t = df["draw_index"].values.astype(np.float64)

    # Small-prime modular features
    mods = [7, 11, 13]
    mod_feats = np.stack([t % m / m for m in mods], axis=1).astype(np.float32)

    global_tile = np.tile(global_freq, (n, 1))
    return np.concatenate([global_tile, roll, mod_feats], axis=1).astype(np.float32)


# ---------------------------------------------------------------------------
# Combined feature builder
# ---------------------------------------------------------------------------

FEATURE_GROUPS = {
    "base": global_freq_features,          # (N_NUMBERS,) per draw
    "time": complex_time_features,
    "rolling": build_rolling_freq_matrix,
    "expdecay": build_exp_decay_matrix,
    "winding": winding_history_features,
}


def _feature_group_width(group: str) -> int:
    widths = {
        "base": N_NUMBERS,
        "time": 1 + 2 * 3,   # 7 columns with default 3 periods
        "rolling": N_NUMBERS,
        "expdecay": N_NUMBERS,
        "winding": N_NUMBERS + N_NUMBERS + 3,  # global + rolling + 3 mod feats
    }
    return widths[group]


def get_feature_slice(groups: List[str], feature_name: str) -> slice:
    """
    Return the column slice for *feature_name* within the concatenated feature
    matrix built by :func:`build_features`.

    Parameters
    ----------
    groups : Ordered list of feature group names used to build the matrix.
    feature_name : One of the group names in *groups*.

    Returns
    -------
    slice object indexing the relevant columns.

    Example
    -------
    >>> sl = get_feature_slice(["base", "winding"], "winding")
    >>> X[:, sl]   # columns belonging to "winding"
    """
    start = 0
    for g in groups:
        w = _feature_group_width(g)
        if g == feature_name:
            return slice(start, start + w)
        start += w
    raise KeyError(f"Feature group '{feature_name}' not found in {groups}.")


def build_features(
    df: pd.DataFrame,
    groups: List[str],
    train_max_index: Optional[int] = None,
    t_max_train: Optional[float] = None,
    window: int = 52,
    decay: float = 0.98,
) -> np.ndarray:
    """
    Build feature matrix for all rows in *df*.

    Parameters
    ----------
    df : Sorted by draw_index ascending.
    groups : Ordered list of feature group names to include.
    train_max_index : Used to prevent leakage in global-freq and winding.
    t_max_train : Training max draw_index for time normalisation.
    window : Rolling window size.
    decay : Exponential decay rate.

    Returns
    -------
    X : shape (len(df), total_feature_width)
    """
    parts = []
    for g in groups:
        if g == "base":
            freq = global_freq_features(df, train_max_index=train_max_index)
            parts.append(np.tile(freq, (len(df), 1)))
        elif g == "time":
            parts.append(complex_time_features(df, t_max_train=t_max_train))
        elif g == "rolling":
            parts.append(build_rolling_freq_matrix(df, window=window))
        elif g == "expdecay":
            parts.append(build_exp_decay_matrix(df, decay=decay))
        elif g == "winding":
            parts.append(winding_history_features(df, train_max_index=train_max_index, window=window))
        else:
            raise ValueError(f"Unknown feature group: {g!r}")
    return np.concatenate(parts, axis=1).astype(np.float32)


# ---------------------------------------------------------------------------
# Walk-forward split builder (no leakage)
# ---------------------------------------------------------------------------

def build_walk_forward_features(
    df: pd.DataFrame,
    train_end: int,
    val_end: int,
    groups: List[str],
    window: int = 52,
    decay: float = 0.98,
) -> tuple:
    """
    Build features for train, validation, and test splits without leakage.

    The key insight: features for validation/test rows must be computed using
    only information available at that point in time.  Concretely:
    - Global frequencies for val/test rows use only draws up to the row
      being featurised (not the entire val/test window).
    - Time normalisation uses the training-window maximum.

    Parameters
    ----------
    df : Full dataset sorted by draw_index ascending.
    train_end : Last draw_index (inclusive) in training split.
    val_end : Last draw_index (inclusive) in validation split.
    groups : Feature groups to build.

    Returns
    -------
    (X_train, y_train), (X_val, y_val), (X_test, y_test)
    where each X has shape (n_rows, n_features)
    and each y has shape (n_rows, N_NUMBERS) as binary indicators.
    """
    _validate_df(df)
    df = df.sort_values("draw_index").reset_index(drop=True)

    t_max_train = float(df.loc[df["draw_index"] <= train_end, "draw_index"].max())

    train_mask = df["draw_index"] <= train_end
    val_mask = (df["draw_index"] > train_end) & (df["draw_index"] <= val_end)
    test_mask = df["draw_index"] > val_end

    def _build_split(mask: pd.Series, description: str) -> tuple:
        split_df = df[mask].reset_index(drop=True)
        if len(split_df) == 0:
            ncols = sum(_feature_group_width(g) for g in groups)
            return np.zeros((0, ncols), dtype=np.float32), np.zeros((0, N_NUMBERS), dtype=np.float32)

        # For each row in the split, compute features using history up to that row
        split_rows = []
        for pos, row in split_df.iterrows():
            row_draw_idx = row["draw_index"]
            # Use all df rows up to (but not including) current row
            hist_df = df[df["draw_index"] < row_draw_idx].copy()
            # Append a dummy row for the current position to allow rolling lookups
            # that need position info — we compute per-row features instead
            feat = _build_single_row_features(
                history_df=hist_df,
                current_draw_index=row_draw_idx,
                groups=groups,
                train_max_index=train_end,
                t_max_train=t_max_train,
                window=window,
                decay=decay,
            )
            split_rows.append(feat)

        X = np.array(split_rows, dtype=np.float32)
        y = _build_label_matrix(split_df)
        return X, y

    # Training: can use all training data (no per-row overhead needed for
    # "base" features, but rolling still uses walk-forward logic)
    X_train = build_features(
        df[train_mask].reset_index(drop=True),
        groups=groups,
        train_max_index=train_end,
        t_max_train=t_max_train,
        window=window,
        decay=decay,
    )
    y_train = _build_label_matrix(df[train_mask].reset_index(drop=True))

    X_val, y_val = _build_split(val_mask, "validation")
    X_test, y_test = _build_split(test_mask, "test")

    return (X_train, y_train), (X_val, y_val), (X_test, y_test)


def _build_single_row_features(
    history_df: pd.DataFrame,
    current_draw_index: float,
    groups: List[str],
    train_max_index: int,
    t_max_train: float,
    window: int,
    decay: float,
) -> np.ndarray:
    """Build a feature vector for a single draw using only its history."""
    # Create a 1-row df for time features
    single_row = pd.DataFrame({"draw_index": [current_draw_index], "numbers": [[]]})

    parts = []
    for g in groups:
        if g == "base":
            freq = global_freq_features(history_df, train_max_index=train_max_index)
            parts.append(freq)
        elif g == "time":
            feat = complex_time_features(single_row, t_max_train=t_max_train)
            parts.append(feat[0])
        elif g == "rolling":
            feat = rolling_freq_features(history_df, window=window, row_idx=len(history_df))
            parts.append(feat)
        elif g == "expdecay":
            feat = exp_decay_freq_features(history_df, decay=decay, row_idx=len(history_df))
            parts.append(feat)
        elif g == "winding":
            feat = winding_history_features(history_df, train_max_index=train_max_index, window=window)
            if len(feat) > 0:
                parts.append(feat[-1])
            else:
                parts.append(np.zeros(_feature_group_width("winding"), dtype=np.float32))
        else:
            raise ValueError(f"Unknown feature group: {g!r}")
    return np.concatenate(parts).astype(np.float32)


def _build_label_matrix(df: pd.DataFrame) -> np.ndarray:
    """Build binary label matrix. Shape (len(df), N_NUMBERS)."""
    return _build_count_matrix(df)
