#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - CMB Comb Test
=========================================

Test #1: Search for periodic "comb" signatures in CMB power spectrum residuals.

This script implements a pre-registered protocol to test whether CMB residuals
(observed - ΛCDM model) contain sinusoidal oscillations at candidate periods,
which could indicate discrete spacetime architecture.

Protocol: See ../PROTOCOL.md
Author: UBT Research Team
License: MIT
"""

import numpy as np
import sys
from pathlib import Path


# Fixed random seed for reproducibility (pre-registered)
RANDOM_SEED = 42

# Pre-fixed candidate periods (locked in protocol)
CANDIDATE_PERIODS = [8, 16, 32, 64, 128, 255]

# Monte Carlo parameters
N_MC_TRIALS = 10000

# Significance thresholds (pre-registered)
THRESHOLD_CANDIDATE = 0.01  # p < 0.01 for "candidate signal"
THRESHOLD_STRONG = 2.9e-7   # p < 2.9e-7 for "strong signal" (~5σ)


def compute_residuals(ell, C_obs, C_model, sigma):
    """
    Compute normalized residuals.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    C_obs : array-like
        Observed C_ℓ power spectrum
    C_model : array-like
        ΛCDM model prediction C_ℓ
    sigma : array-like
        Uncertainty (diagonal covariance assumed)
    
    Returns
    -------
    residuals : ndarray
        Normalized residuals r_ℓ = (C_obs - C_model) / sigma
    """
    return (C_obs - C_model) / sigma


def fit_sinusoid_linear(ell, residuals, period):
    """
    Fit sinusoid r_ℓ ≈ A sin(2πℓ/Δℓ + φ) using linear regression.
    
    Parameterize as: r_ℓ = a cos(2πℓ/Δℓ) + b sin(2πℓ/Δℓ)
    Then: A = √(a² + b²), φ = arctan2(a, b)
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    residuals : array-like
        Residual values
    period : float
        Period Δℓ to fit
    
    Returns
    -------
    amplitude : float
        Fitted amplitude A
    phase : float
        Fitted phase φ (radians)
    chi2_fit : float
        χ² of fit (sum of squared residuals after removing sinusoid)
    """
    # Design matrix: [cos(2πℓ/Δℓ), sin(2πℓ/Δℓ)]
    theta = 2.0 * np.pi * ell / period
    X = np.column_stack([np.cos(theta), np.sin(theta)])
    
    # Least squares: solve X^T X β = X^T y
    # Using numpy for numerical stability
    beta, _, _, _ = np.linalg.lstsq(X, residuals, rcond=None)
    a, b = beta
    
    # Convert to amplitude and phase
    amplitude = np.sqrt(a**2 + b**2)
    phase = np.arctan2(a, b)
    
    # Compute χ² of fit
    fit = a * np.cos(theta) + b * np.sin(theta)
    chi2_fit = np.sum((residuals - fit)**2)
    
    return amplitude, phase, chi2_fit


def compute_delta_chi2(ell, residuals, period):
    """
    Compute Δχ² improvement from adding sinusoid.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    residuals : array-like
        Residual values
    period : float
        Period Δℓ to test
    
    Returns
    -------
    delta_chi2 : float
        Δχ² = χ²(H0) - χ²(H1)
    amplitude : float
        Best-fit amplitude
    phase : float
        Best-fit phase
    """
    # H0: no sinusoid, χ² = sum of squared residuals
    chi2_h0 = np.sum(residuals**2)
    
    # H1: with sinusoid
    amplitude, phase, chi2_h1 = fit_sinusoid_linear(ell, residuals, period)
    
    # Improvement
    delta_chi2 = chi2_h0 - chi2_h1
    
    return delta_chi2, amplitude, phase


def monte_carlo_null_distribution(ell, sigma, candidate_periods, n_trials=N_MC_TRIALS):
    """
    Generate null distribution of max(Δχ²) under H0.
    
    For each trial:
    1. Generate Gaussian residuals with given sigma
    2. Compute Δχ² for all candidate periods
    3. Record maximum
    
    This implements look-elsewhere correction via max statistic.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    sigma : array-like
        Uncertainties (same shape as residuals)
    candidate_periods : list
        List of periods to test
    n_trials : int
        Number of Monte Carlo trials
    
    Returns
    -------
    max_delta_chi2_null : ndarray
        Distribution of max(Δχ²) under H0 (shape: n_trials)
    """
    np.random.seed(RANDOM_SEED)
    
    max_delta_chi2_null = np.zeros(n_trials)
    
    for i in range(n_trials):
        # Generate null residuals: Gaussian with mean 0, std = sigma/sigma
        # (Normalized, so sigma=1 per multipole)
        null_residuals = np.random.normal(0, 1, size=len(ell))
        
        # Compute Δχ² for all candidate periods
        delta_chi2_values = []
        for period in candidate_periods:
            delta_chi2, _, _ = compute_delta_chi2(ell, null_residuals, period)
            delta_chi2_values.append(delta_chi2)
        
        # Record maximum
        max_delta_chi2_null[i] = np.max(delta_chi2_values)
    
    return max_delta_chi2_null


def compute_p_value(observed_max, null_distribution):
    """
    Compute p-value from empirical null distribution.
    
    P-value = fraction of null trials with statistic ≥ observed
    
    Parameters
    ----------
    observed_max : float
        Observed max(Δχ²)
    null_distribution : array-like
        MC null distribution of max(Δχ²)
    
    Returns
    -------
    p_value : float
        Empirical p-value
    """
    n_trials = len(null_distribution)
    n_exceed = np.sum(null_distribution >= observed_max)
    p_value = n_exceed / n_trials
    
    # Ensure p-value is not exactly zero (limited by MC trials)
    if p_value == 0:
        p_value = 1.0 / n_trials  # Upper limit
    
    return p_value


def run_cmb_comb_test(ell, C_obs, C_model, sigma, output_dir=None):
    """
    Run full CMB comb test protocol.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    C_obs : array-like
        Observed power spectrum
    C_model : array-like
        ΛCDM model prediction
    sigma : array-like
        Uncertainties
    output_dir : str or Path, optional
        Directory to save output files
    
    Returns
    -------
    results : dict
        Dictionary containing:
        - 'best_period': Best-fit period Δℓ
        - 'amplitude': Best-fit amplitude
        - 'phase': Best-fit phase
        - 'max_delta_chi2': Observed max(Δχ²)
        - 'p_value': P-value
        - 'significance': 'null', 'candidate', or 'strong'
        - 'null_distribution': MC null distribution (for plotting)
    """
    # Step 1: Compute residuals
    residuals = compute_residuals(ell, C_obs, C_model, sigma)
    
    # Step 2: Test all candidate periods
    results_per_period = {}
    for period in CANDIDATE_PERIODS:
        delta_chi2, amplitude, phase = compute_delta_chi2(ell, residuals, period)
        results_per_period[period] = {
            'delta_chi2': delta_chi2,
            'amplitude': amplitude,
            'phase': phase
        }
    
    # Step 3: Find maximum Δχ²
    best_period = max(results_per_period.keys(), 
                     key=lambda p: results_per_period[p]['delta_chi2'])
    max_delta_chi2 = results_per_period[best_period]['delta_chi2']
    amplitude = results_per_period[best_period]['amplitude']
    phase = results_per_period[best_period]['phase']
    
    # Step 4: Generate null distribution
    print("Generating null distribution (this may take a moment)...")
    null_distribution = monte_carlo_null_distribution(ell, sigma, CANDIDATE_PERIODS)
    
    # Step 5: Compute p-value
    p_value = compute_p_value(max_delta_chi2, null_distribution)
    
    # Step 6: Assess significance
    if p_value < THRESHOLD_STRONG:
        significance = 'strong'
    elif p_value < THRESHOLD_CANDIDATE:
        significance = 'candidate'
    else:
        significance = 'null'
    
    # Prepare results
    results = {
        'best_period': best_period,
        'amplitude': amplitude,
        'phase': phase,
        'max_delta_chi2': max_delta_chi2,
        'p_value': p_value,
        'significance': significance,
        'null_distribution': null_distribution,
        'residuals': residuals,
        'ell': ell,
        'all_periods': results_per_period
    }
    
    # Print summary
    print("\n" + "="*60)
    print("CMB COMB TEST RESULTS")
    print("="*60)
    print(f"Best period: Δℓ = {best_period}")
    print(f"Amplitude: A = {amplitude:.4f}")
    print(f"Phase: φ = {phase:.4f} rad ({np.degrees(phase):.2f}°)")
    print(f"Max Δχ²: {max_delta_chi2:.2f}")
    print(f"P-value: {p_value:.6e}")
    print(f"Significance: {significance.upper()}")
    print("="*60)
    
    if significance == 'null':
        print("Result: No significant periodic signal detected (H0 not rejected)")
    elif significance == 'candidate':
        print("Result: CANDIDATE signal detected - replication required")
    else:
        print("Result: STRONG signal detected - immediate independent verification needed")
    print("="*60 + "\n")
    
    # Save results if output directory provided
    if output_dir is not None:
        save_results(results, output_dir)
    
    return results


def save_results(results, output_dir):
    """
    Save results to output directory.
    
    Parameters
    ----------
    results : dict
        Results dictionary from run_cmb_comb_test
    output_dir : str or Path
        Output directory
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save summary statistics
    with open(output_dir / 'cmb_comb_results.txt', 'w') as f:
        f.write("CMB COMB TEST RESULTS\n")
        f.write("="*60 + "\n")
        f.write(f"Best period: Δℓ = {results['best_period']}\n")
        f.write(f"Amplitude: A = {results['amplitude']:.6f}\n")
        f.write(f"Phase: φ = {results['phase']:.6f} rad\n")
        f.write(f"Max Δχ²: {results['max_delta_chi2']:.6f}\n")
        f.write(f"P-value: {results['p_value']:.6e}\n")
        f.write(f"Significance: {results['significance']}\n")
        f.write(f"Random seed: {RANDOM_SEED}\n")
        f.write(f"MC trials: {N_MC_TRIALS}\n")
    
    # Save null distribution
    np.savetxt(output_dir / 'null_distribution.txt', results['null_distribution'],
               header='Max Δχ² values under H0 (null hypothesis)')
    
    # Save residuals and fitted sinusoid
    ell = results['ell']
    residuals = results['residuals']
    period = results['best_period']
    amplitude = results['amplitude']
    phase = results['phase']
    
    theta = 2.0 * np.pi * ell / period
    fitted_sinusoid = amplitude * np.sin(theta + phase)
    
    np.savetxt(output_dir / 'residuals_and_fit.txt',
               np.column_stack([ell, residuals, fitted_sinusoid]),
               header='ℓ   residual   fitted_sinusoid')
    
    print(f"Results saved to {output_dir}")


def plot_results(results, output_dir):
    """
    Generate diagnostic plots (requires matplotlib).
    
    Parameters
    ----------
    results : dict
        Results dictionary from run_cmb_comb_test
    output_dir : str or Path
        Output directory
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Matplotlib not available - skipping plots")
        return
    
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Plot 1: Residuals with fitted sinusoid
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ell = results['ell']
    residuals = results['residuals']
    period = results['best_period']
    amplitude = results['amplitude']
    phase = results['phase']
    
    theta = 2.0 * np.pi * ell / period
    fitted_sinusoid = amplitude * np.sin(theta + phase)
    
    ax.scatter(ell, residuals, s=10, alpha=0.5, label='Residuals')
    ax.plot(ell, fitted_sinusoid, 'r-', linewidth=2, 
            label=f'Best fit (Δℓ={period}, A={amplitude:.3f})')
    ax.axhline(0, color='k', linestyle='--', alpha=0.3)
    ax.set_xlabel('Multipole ℓ')
    ax.set_ylabel('Normalized Residual')
    ax.set_title('CMB Power Spectrum Residuals with Fitted Comb')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'residuals_with_fit.png', dpi=150)
    plt.close()
    
    # Plot 2: Null distribution histogram
    fig, ax = plt.subplots(figsize=(10, 6))
    
    null_dist = results['null_distribution']
    max_delta_chi2 = results['max_delta_chi2']
    p_value = results['p_value']
    
    ax.hist(null_dist, bins=50, alpha=0.7, edgecolor='black', label='H0 null distribution')
    ax.axvline(max_delta_chi2, color='r', linestyle='--', linewidth=2,
               label=f'Observed (p={p_value:.4e})')
    ax.set_xlabel('max(Δχ²)')
    ax.set_ylabel('Frequency')
    ax.set_title('Monte Carlo Null Distribution of max(Δχ²)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'null_distribution.png', dpi=150)
    plt.close()
    
    print(f"Plots saved to {output_dir}")


def load_data(obs_file, model_file, cov_file=None):
    """
    Load CMB data from files.
    
    Expected format: Text files with columns [ell, C_ell, sigma_ell]
    
    Parameters
    ----------
    obs_file : str or Path
        Observed power spectrum file
    model_file : str or Path
        Model prediction file
    cov_file : str or Path, optional
        Covariance file (if None, use diagonal sigma)
    
    Returns
    -------
    ell : ndarray
        Multipole moments
    C_obs : ndarray
        Observed power spectrum
    C_model : ndarray
        Model prediction
    sigma : ndarray
        Uncertainties
    """
    # Load observed data
    obs_data = np.loadtxt(obs_file)
    ell_obs = obs_data[:, 0].astype(int)
    C_obs = obs_data[:, 1]
    sigma_obs = obs_data[:, 2] if obs_data.shape[1] > 2 else None
    
    # Load model data
    model_data = np.loadtxt(model_file)
    ell_model = model_data[:, 0].astype(int)
    C_model = model_data[:, 1]
    
    # Ensure ell arrays match
    if not np.array_equal(ell_obs, ell_model):
        raise ValueError("Multipole ranges in obs and model files don't match")
    
    ell = ell_obs
    
    # Handle uncertainties
    if sigma_obs is not None:
        sigma = sigma_obs
    elif cov_file is not None:
        # Load covariance and extract diagonal
        cov = np.loadtxt(cov_file)
        sigma = np.sqrt(np.diag(cov))
    else:
        raise ValueError("Must provide sigma in obs file or covariance file")
    
    return ell, C_obs, C_model, sigma


def main():
    """
    Main function for command-line usage.
    """
    if len(sys.argv) < 3:
        print("Usage: python cmb_comb.py <obs_file> <model_file> [output_dir]")
        print("\nFiles should be text format with columns: ell C_ell sigma_ell")
        print("Example: python cmb_comb.py planck_obs.txt lcdm_model.txt ../out/")
        sys.exit(1)
    
    obs_file = sys.argv[1]
    model_file = sys.argv[2]
    output_dir = sys.argv[3] if len(sys.argv) > 3 else '../out'
    
    # Load data
    print(f"Loading data from {obs_file} and {model_file}...")
    ell, C_obs, C_model, sigma = load_data(obs_file, model_file)
    print(f"Loaded {len(ell)} multipoles (ℓ = {ell[0]} to {ell[-1]})")
    
    # Run test
    results = run_cmb_comb_test(ell, C_obs, C_model, sigma, output_dir)
    
    # Generate plots if matplotlib available
    plot_results(results, output_dir)
    
    return results


if __name__ == '__main__':
    main()
