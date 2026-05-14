"""
Layer 2 Fingerprint - Statistical Metrics

This module provides statistical metrics for evaluating Layer 2 configurations.

IMPORTANT: This module uses "hit-rate" and "rarity bits" terminology.
We do NOT compute or mention "p-values" unless a null hypothesis and
correction method are clearly defined.

Metrics:
--------
- Hit-rate: Fraction of configurations matching observables within tolerance
- Rarity bits: Information-theoretic measure of rarity (-log2(hit_rate))
- Normalized error: Error scaled by tolerance

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

from __future__ import annotations

import math
from typing import Dict, List
import numpy as np


def normalize_error(predicted: float, observed: float, tolerance: float) -> float:
    """
    Compute normalized error: |predicted - observed| / tolerance
    
    Parameters
    ----------
    predicted : float
        Predicted value
    observed : float
        Observed/experimental value
    tolerance : float
        Tolerance threshold
        
    Returns
    -------
    float
        Normalized error (0 = perfect match, 1 = at threshold, >1 = beyond threshold)
    """
    if tolerance <= 0:
        raise ValueError("Tolerance must be positive")
    
    return abs(predicted - observed) / tolerance


def combined_score(errors: Dict[str, float], weights: Dict[str, float] = None) -> float:
    """
    Compute combined score from multiple error metrics.
    
    Default: RMS (root mean square) of normalized errors.
    
    Parameters
    ----------
    errors : Dict[str, float]
        Dictionary of {observable_name: normalized_error}
    weights : Dict[str, float], optional
        Dictionary of {observable_name: weight}
        If None, equal weights are used
        
    Returns
    -------
    float
        Combined score (lower is better)
    """
    if not errors:
        return float('inf')
    
    if weights is None:
        weights = {k: 1.0 for k in errors.keys()}
    
    # Weighted RMS
    weighted_sum = sum(weights.get(k, 1.0) * v**2 for k, v in errors.items())
    total_weight = sum(weights.get(k, 1.0) for k in errors.keys())
    
    return math.sqrt(weighted_sum / total_weight)


def is_hit(errors: Dict[str, float], threshold: float = 1.0) -> bool:
    """
    Check if a configuration is a "hit" (all normalized errors <= threshold).
    
    Parameters
    ----------
    errors : Dict[str, float]
        Dictionary of {observable_name: normalized_error}
    threshold : float, optional
        Threshold for hit (default: 1.0 means within tolerance)
        
    Returns
    -------
    bool
        True if all errors <= threshold
    """
    return all(e <= threshold for e in errors.values())


def compute_hit_rate(n_hits: int, n_total: int) -> float:
    """
    Compute hit-rate: fraction of configurations matching observables.
    
    Parameters
    ----------
    n_hits : int
        Number of configurations matching within tolerance
    n_total : int
        Total number of configurations sampled
        
    Returns
    -------
    float
        Hit-rate in [0, 1]
    """
    if n_total <= 0:
        raise ValueError("n_total must be positive")
    if n_hits < 0 or n_hits > n_total:
        raise ValueError(f"n_hits ({n_hits}) must be in [0, {n_total}]")
    
    return n_hits / n_total


def compute_rarity_bits(hit_rate: float) -> float:
    """
    Compute rarity in bits: -log2(hit_rate)
    
    This is an information-theoretic measure of how rare a matching
    configuration is. Higher values = rarer.
    
    Examples:
    ---------
    - hit_rate = 0.5 (50%) → 1 bit
    - hit_rate = 0.01 (1%) → ~6.64 bits
    - hit_rate = 0.001 (0.1%) → ~9.97 bits
    - hit_rate = 0 → inf (infinitely rare)
    
    Parameters
    ----------
    hit_rate : float
        Hit-rate in [0, 1]
        
    Returns
    -------
    float
        Rarity in bits (inf if hit_rate == 0)
    """
    if hit_rate < 0 or hit_rate > 1:
        raise ValueError("hit_rate must be in [0, 1]")
    
    if hit_rate == 0:
        return float('inf')
    
    return -math.log2(hit_rate)


def compute_statistics(scores: List[float]) -> Dict[str, float]:
    """
    Compute summary statistics for a list of scores.
    
    Parameters
    ----------
    scores : List[float]
        List of configuration scores
        
    Returns
    -------
    Dict[str, float]
        Dictionary with mean, median, std, min, max
    """
    if not scores:
        return {
            'mean': float('nan'),
            'median': float('nan'),
            'std': float('nan'),
            'min': float('nan'),
            'max': float('nan'),
        }
    
    arr = np.array(scores)
    
    return {
        'mean': float(np.mean(arr)),
        'median': float(np.median(arr)),
        'std': float(np.std(arr)),
        'min': float(np.min(arr)),
        'max': float(np.max(arr)),
    }


def rank_configuration(
    score: float, 
    all_scores: List[float], 
    lower_is_better: bool = True
) -> Dict[str, float]:
    """
    Rank a configuration against a population.
    
    Parameters
    ----------
    score : float
        Score of configuration to rank
    all_scores : List[float]
        Scores of all configurations in population
    lower_is_better : bool, optional
        If True, lower scores are better (default)
        
    Returns
    -------
    Dict[str, float]
        Dictionary with rank, percentile, fraction_better
    """
    if not all_scores:
        return {
            'rank': 0,
            'percentile': 0.0,
            'fraction_better': 0.0,
        }
    
    arr = np.array(all_scores)
    
    if lower_is_better:
        better = np.sum(arr <= score)
    else:
        better = np.sum(arr >= score)
    
    rank = better - 1  # 0-indexed rank (0 = best)
    percentile = (rank / len(all_scores)) * 100 if all_scores else 0.0
    fraction_better = better / len(all_scores) if all_scores else 0.0
    
    return {
        'rank': int(rank),
        'percentile': float(percentile),
        'fraction_better': float(fraction_better),
    }
