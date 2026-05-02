# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
sportka/multiscale_features.py — Multi-scale feature engineering.

Combines features computed at multiple temporal scales (short, medium, long)
to capture both recent patterns and long-term frequency baselines.
"""
from __future__ import annotations

from typing import List, Optional

import numpy as np
import pandas as pd

from sportka.features import (
    N_NUMBERS,
    DRAWN_PER_DRAW,
    build_rolling_freq_matrix,
    build_exp_decay_matrix,
    global_freq_features,
)
from sportka.ubt_theta_transform import theta_heat_kernel_matrix

# Default window sizes (in draws) for multiscale rolling frequencies
DEFAULT_WINDOWS = [13, 52, 208]

# Default decay rates for multiscale exponential decay
DEFAULT_DECAYS = [0.95, 0.98, 0.995]


def build_multiscale_rolling(
    df: pd.DataFrame,
    windows: List[int] = None,
) -> np.ndarray:
    """
    Build rolling frequency features at multiple scales.

    Returns
    -------
    mat : shape (len(df), N_NUMBERS * len(windows))
    """
    if windows is None:
        windows = DEFAULT_WINDOWS
    parts = [build_rolling_freq_matrix(df, window=w) for w in windows]
    return np.concatenate(parts, axis=1).astype(np.float32)


def build_multiscale_expdecay(
    df: pd.DataFrame,
    decays: List[float] = None,
) -> np.ndarray:
    """
    Build exponential-decay features at multiple scales.

    Returns
    -------
    mat : shape (len(df), N_NUMBERS * len(decays))
    """
    if decays is None:
        decays = DEFAULT_DECAYS
    parts = [build_exp_decay_matrix(df, decay=d) for d in decays]
    return np.concatenate(parts, axis=1).astype(np.float32)


def build_multiscale_theta(
    df: pd.DataFrame,
    windows: List[int] = None,
    sigma: float = 3.0,
) -> np.ndarray:
    """
    Build theta-smoothed rolling frequency features at multiple scales.

    Applies the UBT heat-kernel theta transform after computing rolling
    frequencies at each scale.

    Returns
    -------
    mat : shape (len(df), N_NUMBERS * len(windows))
    """
    if windows is None:
        windows = DEFAULT_WINDOWS
    parts = []
    for w in windows:
        rolling = build_rolling_freq_matrix(df, window=w)
        smoothed = theta_heat_kernel_matrix(rolling, sigma=sigma)
        parts.append(smoothed)
    return np.concatenate(parts, axis=1).astype(np.float32)


def build_multiscale_features(
    df: pd.DataFrame,
    windows: List[int] = None,
    decays: List[float] = None,
    include_theta: bool = False,
    theta_sigma: float = 3.0,
    train_max_index: Optional[int] = None,
) -> np.ndarray:
    """
    Build a combined multi-scale feature matrix.

    Includes:
    - Global frequency (1 × N_NUMBERS)
    - Multi-scale rolling frequencies (len(windows) × N_NUMBERS)
    - Multi-scale exponential decay (len(decays) × N_NUMBERS)
    - Optionally: theta-smoothed rolling (len(windows) × N_NUMBERS)

    Parameters
    ----------
    df : Sorted by draw_index ascending.
    windows : Rolling window sizes.
    decays : Exponential decay rates.
    include_theta : Whether to include theta-smoothed features.
    theta_sigma : Gaussian sigma for theta transform.
    train_max_index : For leakage-safe global frequency.

    Returns
    -------
    mat : shape (len(df), total_features)
    """
    if windows is None:
        windows = DEFAULT_WINDOWS
    if decays is None:
        decays = DEFAULT_DECAYS

    n = len(df)
    global_freq = global_freq_features(df, train_max_index=train_max_index)
    global_tile = np.tile(global_freq, (n, 1))

    parts = [
        global_tile,
        build_multiscale_rolling(df, windows=windows),
        build_multiscale_expdecay(df, decays=decays),
    ]

    if include_theta:
        parts.append(build_multiscale_theta(df, windows=windows, sigma=theta_sigma))

    return np.concatenate(parts, axis=1).astype(np.float32)
