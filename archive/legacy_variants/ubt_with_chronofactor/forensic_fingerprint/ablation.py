#!/usr/bin/env python3
"""
Multipole Range Ablation Testing for CMB Comb Analysis
=======================================================

This module provides pre-defined ℓ-range splits for ablation testing.
Ablation tests verify that a signal persists across multiple independent
multipole windows, ruling out narrow-range artifacts.

Pre-defined splits are FIXED (not data-driven) to avoid overfitting.

License: MIT
Author: UBT Research Team
"""

import numpy as np
from typing import List, Tuple, Dict


# Pre-defined ablation ranges (LOCKED, not data-driven)
# These splits are chosen to:
# 1. Cover complementary ℓ regions
# 2. Have sufficient data points in each split (typically 100+)
# 3. Test low/mid/high ℓ independently

ABLATION_RANGES_PLANCK = [
    ("low", 30, 250),       # Acoustic peaks + early damping tail
    ("mid", 251, 800),      # Damping tail
    ("high", 801, 1500),    # Deep damping tail
    ("full_low", 30, 800),  # Exclude high-ℓ
    ("full_high", 200, 1500),  # Exclude very low-ℓ
]

ABLATION_RANGES_WMAP = [
    ("low", 30, 200),       # First 2-3 acoustic peaks
    ("mid", 201, 500),      # Damping tail begins
    ("high", 501, 800),     # Deep damping tail (if available)
]


def get_ablation_ranges(dataset='planck', custom_ranges=None):
    """
    Get pre-defined ablation ranges for a dataset.
    
    Parameters
    ----------
    dataset : str
        Dataset name: 'planck' or 'wmap'
    custom_ranges : list of tuples, optional
        Custom (name, ell_min, ell_max) tuples. If provided, overrides defaults.
    
    Returns
    -------
    ranges : list of tuples
        List of (name, ell_min, ell_max) tuples
    
    Raises
    ------
    ValueError
        If dataset is not recognized
    """
    if custom_ranges is not None:
        return custom_ranges
    
    dataset = dataset.lower()
    
    if dataset == 'planck':
        return ABLATION_RANGES_PLANCK
    elif dataset == 'wmap':
        return ABLATION_RANGES_WMAP
    else:
        raise ValueError(f"Unknown dataset '{dataset}'. Use 'planck', 'wmap', or provide custom_ranges.")


def validate_ablation_range(ell_min, ell_max, ell_data, min_points=50):
    """
    Validate that an ablation range has sufficient data points.
    
    Parameters
    ----------
    ell_min : int
        Minimum multipole for ablation window
    ell_max : int
        Maximum multipole for ablation window
    ell_data : array-like
        Available multipole moments in the dataset
    min_points : int
        Minimum number of points required in window (default: 50)
    
    Returns
    -------
    is_valid : bool
        True if range has sufficient points
    n_points : int
        Actual number of points in range
    skip_reason : str or None
        If invalid, reason for skipping
    """
    ell_data = np.asarray(ell_data)
    
    # Count points in range
    mask = (ell_data >= ell_min) & (ell_data <= ell_max)
    n_points = np.sum(mask)
    
    if n_points < min_points:
        skip_reason = f"Insufficient data points: {n_points} < {min_points}"
        return False, n_points, skip_reason
    
    if n_points == 0:
        skip_reason = "No data points in range"
        return False, 0, skip_reason
    
    return True, n_points, None


def create_sliding_windows(ell_data, window_size=300, step=100, min_points=50):
    """
    Create sliding window ablation ranges (optional mode).
    
    WARNING: This is an optional exploratory mode. For pre-registered analysis,
    use fixed ablation ranges only.
    
    Parameters
    ----------
    ell_data : array-like
        Available multipole moments
    window_size : int
        Window size in ℓ (default: 300)
    step : int
        Step size between windows (default: 100)
    min_points : int
        Minimum points per window (default: 50)
    
    Returns
    -------
    windows : list of tuples
        List of (name, ell_min, ell_max) tuples
    """
    ell_data = np.asarray(ell_data)
    ell_min_data = int(ell_data[0])
    ell_max_data = int(ell_data[-1])
    
    windows = []
    window_id = 0
    
    for ell_start in range(ell_min_data, ell_max_data - window_size + 1, step):
        ell_end = ell_start + window_size
        
        # Validate window has sufficient points
        is_valid, n_points, _ = validate_ablation_range(
            ell_start, ell_end, ell_data, min_points=min_points
        )
        
        if is_valid:
            name = f"window_{window_id}_{ell_start}_{ell_end}"
            windows.append((name, ell_start, ell_end))
            window_id += 1
    
    return windows


def summarize_ablation_results(results):
    """
    Summarize ablation test results across multiple ranges.
    
    Parameters
    ----------
    results : dict
        Dictionary mapping range names to test results.
        Each result should have keys: 'best_period', 'p_value', 'phase', 'amplitude'
    
    Returns
    -------
    summary : dict
        Summary statistics including:
        - n_ranges: int (number of ranges tested)
        - n_skipped: int (number of ranges skipped)
        - periods: dict (count of each best period across ranges)
        - mean_p_value: float
        - median_p_value: float
        - consistency: dict (phase consistency statistics)
    """
    if not results:
        return {
            'n_ranges': 0,
            'n_skipped': 0,
            'periods': {},
            'mean_p_value': None,
            'median_p_value': None,
            'consistency': None
        }
    
    # Filter out skipped ranges
    valid_results = {k: v for k, v in results.items() if v.get('skipped', False) == False}
    n_skipped = len(results) - len(valid_results)
    
    if not valid_results:
        return {
            'n_ranges': len(results),
            'n_skipped': n_skipped,
            'periods': {},
            'mean_p_value': None,
            'median_p_value': None,
            'consistency': None
        }
    
    # Count best periods
    periods = {}
    p_values = []
    phases = []
    amplitudes = []
    
    for result in valid_results.values():
        period = result.get('best_period')
        if period is not None:
            periods[period] = periods.get(period, 0) + 1
        
        p_val = result.get('p_value')
        if p_val is not None:
            p_values.append(p_val)
        
        phase = result.get('phase')
        if phase is not None:
            phases.append(phase)
        
        amp = result.get('amplitude')
        if amp is not None:
            amplitudes.append(amp)
    
    # Phase consistency: check if phases cluster
    phase_consistency = None
    if len(phases) >= 2:
        phases = np.array(phases)
        # Compute pairwise phase differences (modulo 2π)
        phase_diffs = []
        for i in range(len(phases)):
            for j in range(i + 1, len(phases)):
                diff = abs(phases[i] - phases[j])
                diff = min(diff, 2 * np.pi - diff)  # Wrap to [0, π]
                phase_diffs.append(diff)
        
        phase_consistency = {
            'mean_phase_diff': float(np.mean(phase_diffs)),
            'max_phase_diff': float(np.max(phase_diffs)),
            'consistent_within_pi_2': float(np.max(phase_diffs)) < np.pi / 2
        }
    
    summary = {
        'n_ranges': len(results),
        'n_valid': len(valid_results),
        'n_skipped': n_skipped,
        'periods': periods,
        'mean_p_value': float(np.mean(p_values)) if p_values else None,
        'median_p_value': float(np.median(p_values)) if p_values else None,
        'min_p_value': float(np.min(p_values)) if p_values else None,
        'max_p_value': float(np.max(p_values)) if p_values else None,
        'phase_consistency': phase_consistency
    }
    
    return summary
