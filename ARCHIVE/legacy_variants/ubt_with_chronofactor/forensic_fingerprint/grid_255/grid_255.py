#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - Grid 255 Quantization Test
======================================================

Test #2: Search for alignment of cosmological parameters to rational grid m/255.

This script tests whether MCMC posterior samples show statistically significant
clustering near multiples of 1/255, which could suggest quantization on a
byte-like grid structure.

Protocol: See ../PROTOCOL.md
Author: UBT Research Team
License: MIT
"""

import numpy as np
import sys
from pathlib import Path


# Fixed random seed for reproducibility (pre-registered)
RANDOM_SEED = 137

# Pre-fixed grid denominator (locked in protocol)
GRID_DENOMINATOR = 255

# Monte Carlo parameters
N_MC_TRIALS = 10000

# Significance thresholds (pre-registered)
THRESHOLD_CANDIDATE = 0.01
THRESHOLD_STRONG = 2.9e-7


def compute_grid_distance(samples, denominator=GRID_DENOMINATOR):
    """
    Compute distance to nearest grid point m/denominator.
    
    For each sample x, computes:
        d(x) = min_{m ∈ ℤ} |x - m/denominator|
    
    Parameters
    ----------
    samples : array-like
        Parameter samples from MCMC
    denominator : int
        Grid denominator (default: 255)
    
    Returns
    -------
    distances : ndarray
        Distance to nearest grid point for each sample
    """
    # For each sample, find nearest grid point
    # Grid points: ..., -2/255, -1/255, 0, 1/255, 2/255, ...
    
    # Round to nearest integer after scaling
    m_nearest = np.round(samples * denominator)
    
    # Compute distance
    grid_points = m_nearest / denominator
    distances = np.abs(samples - grid_points)
    
    return distances


def compute_summary_statistics(distances):
    """
    Compute summary statistics for grid distance distribution.
    
    Two statistics:
    1. S₁ = median(d) - robust to outliers
    2. S₂ = mean(log₁₀ d) - sensitive to clustering near grid
    
    Parameters
    ----------
    distances : array-like
        Grid distances
    
    Returns
    -------
    S1 : float
        Median distance
    S2 : float
        Mean of log₁₀(distance)
    """
    # Handle zero distances (exact grid alignment)
    # Add small epsilon to avoid log(0)
    distances_safe = np.maximum(distances, 1e-10)
    
    S1 = np.median(distances)
    S2 = np.mean(np.log10(distances_safe))
    
    return S1, S2


def fit_kde(samples):
    """
    Fit Kernel Density Estimate to samples.
    
    Uses Gaussian kernel with bandwidth from Scott's rule.
    
    Parameters
    ----------
    samples : array-like
        MCMC samples
    
    Returns
    -------
    kde_func : callable
        Function that returns KDE density at given points
    bandwidth : float
        Bandwidth used
    """
    try:
        from scipy.stats import gaussian_kde
        
        kde = gaussian_kde(samples)
        bandwidth = kde.factor * samples.std(ddof=1)
        
        return kde, bandwidth
        
    except ImportError:
        # Fallback: use simple Gaussian approximation
        mean = np.mean(samples)
        std = np.std(samples, ddof=1)
        
        def gaussian_kde_approx(x):
            return np.random.normal(mean, std, size=len(x))
        
        class FallbackKDE:
            def resample(self, size):
                return np.random.normal(mean, std, size=size)
        
        return FallbackKDE(), std


def generate_null_distribution(samples, n_trials=N_MC_TRIALS):
    """
    Generate null distribution of summary statistics.
    
    For each trial:
    1. Fit smooth distribution (KDE) to samples
    2. Resample from fitted distribution
    3. Compute grid distances and summary statistics
    
    This tests H0: samples are smooth, no grid alignment.
    
    Parameters
    ----------
    samples : array-like
        Observed MCMC samples
    n_trials : int
        Number of Monte Carlo trials
    
    Returns
    -------
    S1_null : ndarray
        Null distribution of S₁ (median distance)
    S2_null : ndarray
        Null distribution of S₂ (mean log distance)
    """
    np.random.seed(RANDOM_SEED)
    
    # Fit KDE to observed samples
    kde, bandwidth = fit_kde(samples)
    
    print(f"  KDE bandwidth: {bandwidth:.6f}")
    
    S1_null = np.zeros(n_trials)
    S2_null = np.zeros(n_trials)
    
    n_samples = len(samples)
    
    for i in range(n_trials):
        # Resample from KDE
        if hasattr(kde, 'resample'):
            resampled = kde.resample(n_samples).flatten()
        else:
            # Fallback for scipy kde
            resampled = kde.resample(n_samples)[0]
        
        # Compute grid distances
        distances = compute_grid_distance(resampled)
        
        # Compute statistics
        S1_null[i], S2_null[i] = compute_summary_statistics(distances)
    
    return S1_null, S2_null


def compute_p_values(S1_obs, S2_obs, S1_null, S2_null):
    """
    Compute p-values from null distributions.
    
    For grid alignment, we expect:
    - Small S₁ (median distance close to 0)
    - Small S₂ (mean log distance negative)
    
    So we compute one-tailed p-values (observed ≤ null).
    
    Parameters
    ----------
    S1_obs, S2_obs : float
        Observed statistics
    S1_null, S2_null : array-like
        Null distributions
    
    Returns
    -------
    p1 : float
        P-value for S₁
    p2 : float
        P-value for S₂
    """
    n_trials = len(S1_null)
    
    # One-tailed test: fraction of null trials with statistic ≤ observed
    p1 = np.sum(S1_null <= S1_obs) / n_trials
    p2 = np.sum(S2_null <= S2_obs) / n_trials
    
    # Ensure not exactly zero
    if p1 == 0:
        p1 = 1.0 / n_trials
    if p2 == 0:
        p2 = 1.0 / n_trials
    
    return p1, p2


def run_grid_255_test(samples, parameter_name='parameter', output_dir=None):
    """
    Run full grid 255 quantization test.
    
    Parameters
    ----------
    samples : array-like
        MCMC samples for a single parameter
    parameter_name : str
        Name of parameter (for labeling)
    output_dir : str or Path, optional
        Directory to save outputs
    
    Returns
    -------
    results : dict
        Dictionary containing:
        - 'S1_obs': Observed median distance
        - 'S2_obs': Observed mean log distance
        - 'p1': P-value for S₁
        - 'p2': P-value for S₂
        - 'significance': 'null', 'candidate', or 'strong'
        - 'S1_null', 'S2_null': Null distributions
    """
    print(f"\nTesting parameter: {parameter_name}")
    print(f"Number of samples: {len(samples)}")
    print(f"Range: [{np.min(samples):.6f}, {np.max(samples):.6f}]")
    
    # Step 1: Compute grid distances
    distances = compute_grid_distance(samples)
    
    # Step 2: Compute observed statistics
    S1_obs, S2_obs = compute_summary_statistics(distances)
    
    print(f"Observed S₁ (median distance): {S1_obs:.6e}")
    print(f"Observed S₂ (mean log distance): {S2_obs:.6f}")
    
    # Step 3: Generate null distribution
    print("Generating null distribution...")
    S1_null, S2_null = generate_null_distribution(samples)
    
    # Step 4: Compute p-values
    p1, p2 = compute_p_values(S1_obs, S2_obs, S1_null, S2_null)
    
    # Step 5: Assess significance (use minimum p-value)
    p_min = min(p1, p2)
    
    if p_min < THRESHOLD_STRONG:
        significance = 'strong'
    elif p_min < THRESHOLD_CANDIDATE:
        significance = 'candidate'
    else:
        significance = 'null'
    
    # Prepare results
    results = {
        'parameter_name': parameter_name,
        'n_samples': len(samples),
        'S1_obs': S1_obs,
        'S2_obs': S2_obs,
        'p1': p1,
        'p2': p2,
        'p_min': p_min,
        'significance': significance,
        'S1_null': S1_null,
        'S2_null': S2_null,
        'distances': distances,
        'samples': samples
    }
    
    # Print summary
    print("\n" + "="*60)
    print(f"GRID 255 TEST RESULTS: {parameter_name}")
    print("="*60)
    print(f"S₁ (median distance): {S1_obs:.6e}")
    print(f"S₂ (mean log dist):   {S2_obs:.6f}")
    print(f"P-value (S₁): {p1:.6e}")
    print(f"P-value (S₂): {p2:.6e}")
    print(f"P-value (min): {p_min:.6e}")
    print(f"Significance: {significance.upper()}")
    print("="*60)
    
    if significance == 'null':
        print("Result: No significant grid alignment (H0 not rejected)")
    elif significance == 'candidate':
        print("Result: CANDIDATE grid signal - check other parameters")
    else:
        print("Result: STRONG grid signal - verify with independent chains")
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
        Results from run_grid_255_test
    output_dir : str or Path
        Output directory
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    param_name = results['parameter_name']
    
    # Save summary
    with open(output_dir / f'grid_255_{param_name}_results.txt', 'w') as f:
        f.write(f"GRID 255 TEST RESULTS: {param_name}\n")
        f.write("="*60 + "\n")
        f.write(f"Grid denominator: {GRID_DENOMINATOR}\n")
        f.write(f"Number of samples: {results['n_samples']}\n")
        f.write(f"S₁ (median distance): {results['S1_obs']:.6e}\n")
        f.write(f"S₂ (mean log dist):   {results['S2_obs']:.6f}\n")
        f.write(f"P-value (S₁): {results['p1']:.6e}\n")
        f.write(f"P-value (S₂): {results['p2']:.6e}\n")
        f.write(f"Significance: {results['significance']}\n")
        f.write(f"Random seed: {RANDOM_SEED}\n")
        f.write(f"MC trials: {N_MC_TRIALS}\n")
    
    # Save null distributions
    np.savetxt(output_dir / f'grid_255_{param_name}_null_S1.txt', 
               results['S1_null'],
               header='Null distribution of S₁ (median distance)')
    np.savetxt(output_dir / f'grid_255_{param_name}_null_S2.txt',
               results['S2_null'],
               header='Null distribution of S₂ (mean log distance)')
    
    # Save distances
    np.savetxt(output_dir / f'grid_255_{param_name}_distances.txt',
               results['distances'],
               header='Distance to nearest m/255 grid point')
    
    print(f"Results saved to {output_dir}")


def plot_results(results, output_dir):
    """
    Generate diagnostic plots (requires matplotlib).
    
    Parameters
    ----------
    results : dict
        Results from run_grid_255_test
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
    
    param_name = results['parameter_name']
    
    # Plot 1: Histogram of distances
    fig, ax = plt.subplots(figsize=(10, 6))
    
    distances = results['distances']
    
    ax.hist(distances, bins=50, alpha=0.7, edgecolor='black', density=True,
            label='Observed')
    
    # Expected uniform distribution on [0, 1/(2*255)]
    max_dist = 1.0 / (2 * GRID_DENOMINATOR)
    ax.axvline(max_dist, color='r', linestyle='--', 
               label=f'Max possible (1/{2*GRID_DENOMINATOR})')
    
    # Median
    ax.axvline(results['S1_obs'], color='g', linestyle='--', linewidth=2,
               label=f'Median (S₁={results["S1_obs"]:.4e})')
    
    ax.set_xlabel(f'Distance to nearest m/{GRID_DENOMINATOR} grid point')
    ax.set_ylabel('Density')
    ax.set_title(f'Grid Distance Distribution: {param_name}')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / f'grid_255_{param_name}_distances.png', dpi=150)
    plt.close()
    
    # Plot 2: Null distributions
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # S₁ null distribution
    ax1.hist(results['S1_null'], bins=50, alpha=0.7, edgecolor='black')
    ax1.axvline(results['S1_obs'], color='r', linestyle='--', linewidth=2,
                label=f'Observed (p={results["p1"]:.4e})')
    ax1.set_xlabel('S₁ (median distance)')
    ax1.set_ylabel('Frequency')
    ax1.set_title('Null Distribution of S₁')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # S₂ null distribution
    ax2.hist(results['S2_null'], bins=50, alpha=0.7, edgecolor='black')
    ax2.axvline(results['S2_obs'], color='r', linestyle='--', linewidth=2,
                label=f'Observed (p={results["p2"]:.4e})')
    ax2.set_xlabel('S₂ (mean log₁₀ distance)')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Null Distribution of S₂')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / f'grid_255_{param_name}_null.png', dpi=150)
    plt.close()
    
    print(f"Plots saved to {output_dir}")


def load_mcmc_chain(filename, parameter_index=0, skip_header=0, delimiter=None):
    """
    Load MCMC chain from file.
    
    Parameters
    ----------
    filename : str or Path
        Path to chain file
    parameter_index : int
        Column index of parameter to extract (0-based)
    skip_header : int
        Number of header lines to skip
    delimiter : str, optional
        Column delimiter (default: whitespace)
    
    Returns
    -------
    samples : ndarray
        Parameter samples
    """
    data = np.loadtxt(filename, skiprows=skip_header, delimiter=delimiter)
    
    if data.ndim == 1:
        # Single column
        samples = data
    else:
        # Multiple columns
        samples = data[:, parameter_index]
    
    return samples


def main():
    """
    Main function for command-line usage.
    """
    if len(sys.argv) < 2:
        print("Usage: python grid_255.py <chain_file> [param_index] [output_dir]")
        print("\nchain_file: MCMC chain file (text format)")
        print("param_index: Column index of parameter (default: 0)")
        print("output_dir: Output directory (default: ../out/)")
        print("\nExample: python grid_255.py planck_chains.txt 2 ../out/")
        sys.exit(1)
    
    chain_file = sys.argv[1]
    param_index = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    output_dir = sys.argv[3] if len(sys.argv) > 3 else '../out'
    
    # Load chain
    print(f"Loading MCMC chain from {chain_file}...")
    samples = load_mcmc_chain(chain_file, parameter_index=param_index)
    print(f"Loaded {len(samples)} samples")
    
    # Run test
    param_name = f"param_{param_index}"
    results = run_grid_255_test(samples, parameter_name, output_dir)
    
    # Generate plots if matplotlib available
    plot_results(results, output_dir)
    
    return results


if __name__ == '__main__':
    main()
