#!/usr/bin/env python3
"""
UBT Planck Validation - Statistical Metrics

This module implements statistical metrics for evaluating UBT predictions
against Planck 2018 observations.

Protocol Version: 1.0
Date: 2026-01-10
License: MIT License
"""

import numpy as np
from scipy import stats


def sigma_deviation(prediction, observation, sigma):
    """
    Compute sigma deviation (z-score) between prediction and observation.
    
    Parameters
    ----------
    prediction : float
        UBT-predicted value
    observation : float
        Observed value from Planck 2018
    sigma : float
        1-sigma uncertainty on observation
    
    Returns
    -------
    float
        Z-score: (prediction - observation) / sigma
        
        Interpretation:
        - |z| < 1: Agreement within 1σ (good)
        - |z| < 2: Agreement within 2σ (acceptable)
        - |z| < 3: Agreement within 3σ (marginal)
        - |z| > 3: Disagreement (potential falsification)
    
    Examples
    --------
    >>> sigma_deviation(0.02237, 0.02237, 0.00015)
    0.0
    >>> sigma_deviation(0.02250, 0.02237, 0.00015)
    0.8667  # Less than 1σ, good agreement
    """
    z = (prediction - observation) / sigma
    return z


def chi2_single(prediction, observation, sigma):
    """
    Compute chi-square contribution for a single parameter.
    
    Parameters
    ----------
    prediction : float
        UBT-predicted value
    observation : float
        Observed value
    sigma : float
        1-sigma uncertainty
    
    Returns
    -------
    float
        Chi-square contribution: ((prediction - observation) / sigma)^2
    """
    z = sigma_deviation(prediction, observation, sigma)
    return z**2


def chi2_vector(predictions, observations, sigmas):
    """
    Compute total chi-square over multiple parameters.
    
    Parameters
    ----------
    predictions : array-like
        UBT-predicted values for multiple parameters
    observations : array-like
        Observed values from Planck 2018
    sigmas : array-like
        1-sigma uncertainties on observations
    
    Returns
    -------
    float
        Total chi-square: Σ((pred - obs) / sigma)^2
    
    Notes
    -----
    This assumes diagonal covariance matrix (uncorrelated parameters).
    If parameters are correlated, this is an approximation.
    
    Examples
    --------
    >>> predictions = [0.02231, 0.1192, 0.9647]
    >>> observations = [0.02237, 0.1200, 0.9649]
    >>> sigmas = [0.00015, 0.0012, 0.0042]
    >>> chi2_vector(predictions, observations, sigmas)
    0.84  # Good agreement (chi2 < 3 for 3 parameters)
    """
    predictions = np.asarray(predictions)
    observations = np.asarray(observations)
    sigmas = np.asarray(sigmas)
    
    # Validate same length
    if not (len(predictions) == len(observations) == len(sigmas)):
        raise ValueError(
            f"Length mismatch: predictions={len(predictions)}, "
            f"observations={len(observations)}, sigmas={len(sigmas)}"
        )
    
    # Compute z-scores
    z_scores = (predictions - observations) / sigmas
    
    # Sum of squares
    chi2 = np.sum(z_scores**2)
    
    return chi2


def chi2_pvalue(chi2, dof):
    """
    Compute p-value from chi-square statistic.
    
    Parameters
    ----------
    chi2 : float
        Chi-square statistic
    dof : int
        Degrees of freedom (number of parameters)
    
    Returns
    -------
    float
        P-value: probability of obtaining chi2 this large or larger
        under the null hypothesis (model is correct)
        
        Interpretation:
        - p > 0.05: Good agreement (fail to reject model)
        - p < 0.05: Some tension
        - p < 0.01: Significant disagreement
    
    Examples
    --------
    >>> chi2_pvalue(0.84, dof=3)
    0.840  # High p-value = good agreement
    >>> chi2_pvalue(15.0, dof=3)
    0.002  # Low p-value = poor agreement
    """
    # Survival function: P(X > chi2) for chi2 distribution with dof degrees of freedom
    pvalue = stats.chi2.sf(chi2, dof)
    return pvalue


def success_criterion(z_scores, threshold=1.0):
    """
    Check if all predictions satisfy success criterion.
    
    Parameters
    ----------
    z_scores : array-like
        Z-scores for each predicted parameter
    threshold : float, optional
        Maximum allowed |z| for success (default: 1.0)
    
    Returns
    -------
    bool
        True if all |z| <= threshold, False otherwise
    
    Notes
    -----
    Pre-registered success criterion (Protocol v1.0):
    - All implemented parameters must have |z| <= 1.0 (within 1σ)
    - This is a STRICT criterion to avoid post-hoc rationalization
    
    Examples
    --------
    >>> success_criterion([0.4, -0.67, 0.05])
    True  # All within 1σ
    >>> success_criterion([0.4, 1.5, 0.05])
    False  # One exceeds 1σ
    """
    z_scores = np.asarray(z_scores)
    return bool(np.all(np.abs(z_scores) <= threshold))


def compute_metrics_summary(predictions, observations, sigmas, parameter_names):
    """
    Compute comprehensive metrics summary for all parameters.
    
    Parameters
    ----------
    predictions : array-like
        UBT-predicted values
    observations : array-like
        Planck 2018 observed values
    sigmas : array-like
        1-sigma uncertainties
    parameter_names : list of str
        Names of parameters (e.g., ['omega_b_h2', 'omega_c_h2', 'n_s'])
    
    Returns
    -------
    dict
        Dictionary containing:
        - 'parameters': list of dicts with per-parameter metrics
        - 'chi2_total': total chi-square
        - 'dof': degrees of freedom
        - 'pvalue': p-value from chi2 test
        - 'success': bool, whether success criterion met
        - 'n_parameters': number of parameters evaluated
    
    Examples
    --------
    >>> predictions = [0.02231, 0.1192, 0.9647]
    >>> observations = [0.02237, 0.1200, 0.9649]
    >>> sigmas = [0.00015, 0.0012, 0.0042]
    >>> names = ['omega_b_h2', 'omega_c_h2', 'n_s']
    >>> summary = compute_metrics_summary(predictions, observations, sigmas, names)
    >>> summary['success']
    True
    >>> summary['chi2_total'] < 3
    True
    """
    predictions = np.asarray(predictions)
    observations = np.asarray(observations)
    sigmas = np.asarray(sigmas)
    
    n_params = len(predictions)
    
    # Compute per-parameter metrics
    parameters = []
    for i, name in enumerate(parameter_names):
        z = sigma_deviation(predictions[i], observations[i], sigmas[i])
        chi2_contrib = z**2
        
        parameters.append({
            'name': name,
            'predicted': predictions[i],
            'observed': observations[i],
            'sigma': sigmas[i],
            'z_score': z,
            'chi2_contribution': chi2_contrib,
            'within_1sigma': abs(z) <= 1.0,
            'within_2sigma': abs(z) <= 2.0,
            'within_3sigma': abs(z) <= 3.0
        })
    
    # Compute combined metrics
    chi2_total = chi2_vector(predictions, observations, sigmas)
    dof = n_params
    pvalue = chi2_pvalue(chi2_total, dof)
    
    # Check success criterion
    z_scores = [p['z_score'] for p in parameters]
    success = success_criterion(z_scores, threshold=1.0)
    
    summary = {
        'parameters': parameters,
        'chi2_total': chi2_total,
        'dof': dof,
        'pvalue': pvalue,
        'success': success,
        'n_parameters': n_params
    }
    
    return summary


def format_metrics_table(summary):
    """
    Format metrics summary as a readable text table.
    
    Parameters
    ----------
    summary : dict
        Output from compute_metrics_summary()
    
    Returns
    -------
    str
        Formatted table string
    """
    lines = []
    lines.append("=" * 90)
    lines.append("UBT Planck Validation - Metrics Summary")
    lines.append("=" * 90)
    lines.append("")
    
    # Header
    lines.append(f"{'Parameter':<15} {'Predicted':<12} {'Observed':<12} {'Sigma':<10} {'Z-score':<10} {'Status':<10}")
    lines.append("-" * 90)
    
    # Per-parameter rows
    for p in summary['parameters']:
        status = "✓ 1σ" if p['within_1sigma'] else ("✓ 2σ" if p['within_2sigma'] else ("✓ 3σ" if p['within_3sigma'] else "✗ >3σ"))
        lines.append(
            f"{p['name']:<15} {p['predicted']:<12.6f} {p['observed']:<12.6f} "
            f"{p['sigma']:<10.6f} {p['z_score']:<10.3f} {status:<10}"
        )
    
    lines.append("-" * 90)
    
    # Combined metrics
    lines.append(f"Chi-square total: {summary['chi2_total']:.3f} (dof = {summary['dof']})")
    lines.append(f"P-value: {summary['pvalue']:.4f}")
    lines.append(f"Success criterion (all |z| <= 1): {'YES ✓' if summary['success'] else 'NO ✗'}")
    lines.append("")
    lines.append("=" * 90)
    
    return "\n".join(lines)
