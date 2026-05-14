#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - Cross-Dataset Invariance Test
=========================================================

Test #3: Check consistency of UBT-predicted invariants across independent datasets.

This script tests whether UBT-predicted invariant quantities (derived from
cosmological parameters via fixed UBT formulae) agree across different datasets
(Planck, BAO, SNe, lensing), supporting theoretical coherence.

Protocol: See ../PROTOCOL.md
Author: UBT Research Team
License: MIT
"""

import numpy as np
import sys
from pathlib import Path


def ubt_invariant_kappa(omega_b_h2):
    """
    Compute UBT invariant κ from baryon density.
    
    This is a PLACEHOLDER function. Replace with actual UBT formula
    from the theory once specified.
    
    For demonstration, using a simple linear mapping:
        κ = (ω_b - ω_b^ref) / σ_ref
    
    where ω_b^ref and σ_ref are UBT-predicted reference values.
    
    Parameters
    ----------
    omega_b_h2 : float
        Baryon density parameter Ω_b h²
    
    Returns
    -------
    kappa : float
        UBT invariant κ
    """
    # PLACEHOLDER: Replace with actual UBT formula
    # Example: κ = f(ω_b) where f is derived from biquaternionic mapping
    
    omega_b_ref = 0.02237  # Planck 2018 best-fit
    sigma_ref = 0.00015    # Typical uncertainty
    
    # Simple linear transformation (REPLACE THIS)
    kappa = (omega_b_h2 - omega_b_ref) / sigma_ref
    
    return kappa


def ubt_invariant_eta(n_s):
    """
    Compute UBT invariant η from spectral index.
    
    This is a PLACEHOLDER function. Replace with actual UBT formula
    from complex-time phase mapping.
    
    For demonstration, using:
        η = (n_s - 1) / Δn_ref
    
    where Δn_ref is a UBT-predicted scale.
    
    Parameters
    ----------
    n_s : float
        Scalar spectral index
    
    Returns
    -------
    eta : float
        UBT invariant η (phase index)
    """
    # PLACEHOLDER: Replace with actual UBT formula
    # Example: η = g(n_s) from Im(τ) phase dynamics
    
    delta_n_ref = 0.004  # UBT-predicted tilt scale
    
    # Simple transformation (REPLACE THIS)
    eta = (n_s - 1.0) / delta_n_ref
    
    return eta


def propagate_uncertainty(param_value, param_sigma, invariant_func):
    """
    Propagate uncertainty through invariant function.
    
    Uses linear approximation: σ_κ ≈ |dκ/dθ| × σ_θ
    
    Parameters
    ----------
    param_value : float
        Parameter value
    param_sigma : float
        Parameter uncertainty
    invariant_func : callable
        Function mapping parameter to invariant
    
    Returns
    -------
    inv_value : float
        Invariant value
    inv_sigma : float
        Invariant uncertainty
    """
    # Compute invariant at central value
    inv_value = invariant_func(param_value)
    
    # Numerical derivative
    epsilon = param_sigma * 1e-4
    inv_plus = invariant_func(param_value + epsilon)
    inv_minus = invariant_func(param_value - epsilon)
    
    derivative = (inv_plus - inv_minus) / (2 * epsilon)
    
    # Propagate uncertainty
    inv_sigma = abs(derivative) * param_sigma
    
    return inv_value, inv_sigma


def compute_weighted_mean(values, sigmas):
    """
    Compute inverse-variance weighted mean.
    
    Parameters
    ----------
    values : array-like
        Measured values
    sigmas : array-like
        Uncertainties
    
    Returns
    -------
    mean : float
        Weighted mean
    mean_sigma : float
        Uncertainty on weighted mean
    """
    values = np.array(values)
    sigmas = np.array(sigmas)
    
    weights = 1.0 / sigmas**2
    
    mean = np.sum(weights * values) / np.sum(weights)
    mean_sigma = 1.0 / np.sqrt(np.sum(weights))
    
    return mean, mean_sigma


def compute_chi_square(values, sigmas, mean=None):
    """
    Compute chi-square statistic for consistency.
    
    χ² = Σᵢ (κᵢ - κ̄)² / σᵢ²
    
    where κ̄ is the weighted mean.
    
    Parameters
    ----------
    values : array-like
        Invariant estimates from each dataset
    sigmas : array-like
        Uncertainties
    mean : float, optional
        Mean to compare against (if None, use weighted mean)
    
    Returns
    -------
    chi2 : float
        Chi-square statistic
    dof : int
        Degrees of freedom
    """
    values = np.array(values)
    sigmas = np.array(sigmas)
    
    if mean is None:
        mean, _ = compute_weighted_mean(values, sigmas)
    
    chi2 = np.sum((values - mean)**2 / sigmas**2)
    dof = len(values) - 1  # N datasets, 1 constraint (weighted mean)
    
    return chi2, dof


def chi2_p_value(chi2, dof):
    """
    Compute p-value from chi-square distribution.
    
    Parameters
    ----------
    chi2 : float
        Chi-square statistic
    dof : int
        Degrees of freedom
    
    Returns
    -------
    p_value : float
        P-value (probability of chi2 or larger under H0)
    """
    try:
        from scipy.stats import chi2 as chi2_dist
        p_value = 1.0 - chi2_dist.cdf(chi2, dof)
    except ImportError:
        # Fallback: simple approximation for large dof
        # Using Wilson-Hilferty transformation
        z = ((chi2 / dof)**(1/3) - (1 - 2/(9*dof))) / np.sqrt(2/(9*dof))
        
        # Standard normal CDF approximation
        from math import erf
        p_value = 0.5 * (1 - erf(z / np.sqrt(2)))
    
    return p_value


def run_invariance_test(datasets, invariant_func, invariant_name='kappa', output_dir=None):
    """
    Run cross-dataset invariance test.
    
    Parameters
    ----------
    datasets : list of dict
        Each dict contains:
        - 'name': Dataset name
        - 'param_value': Parameter estimate
        - 'param_sigma': Parameter uncertainty
    invariant_func : callable
        Function mapping parameter to invariant
    invariant_name : str
        Name of invariant (for labeling)
    output_dir : str or Path, optional
        Directory to save outputs
    
    Returns
    -------
    results : dict
        Dictionary containing:
        - 'invariants': List of (name, value, sigma) for each dataset
        - 'weighted_mean': Weighted mean of invariants
        - 'weighted_sigma': Uncertainty on weighted mean
        - 'chi2': Chi-square statistic
        - 'dof': Degrees of freedom
        - 'p_value': P-value
        - 'consistent': Boolean (p > 0.05)
    """
    print(f"\nTesting UBT invariant: {invariant_name}")
    print(f"Number of datasets: {len(datasets)}")
    
    # Step 1: Compute invariant for each dataset
    invariants = []
    for ds in datasets:
        inv_value, inv_sigma = propagate_uncertainty(
            ds['param_value'], ds['param_sigma'], invariant_func
        )
        invariants.append({
            'name': ds['name'],
            'value': inv_value,
            'sigma': inv_sigma
        })
        print(f"  {ds['name']}: {invariant_name} = {inv_value:.6f} ± {inv_sigma:.6f}")
    
    # Step 2: Compute weighted mean
    values = np.array([inv['value'] for inv in invariants])
    sigmas = np.array([inv['sigma'] for inv in invariants])
    
    weighted_mean, weighted_sigma = compute_weighted_mean(values, sigmas)
    print(f"\nWeighted mean: {invariant_name} = {weighted_mean:.6f} ± {weighted_sigma:.6f}")
    
    # Step 3: Compute chi-square
    chi2, dof = compute_chi_square(values, sigmas)
    p_value = chi2_p_value(chi2, dof)
    
    print(f"χ² = {chi2:.3f} (dof = {dof})")
    print(f"P-value = {p_value:.6f}")
    
    # Step 4: Assess consistency
    consistent = p_value > 0.05  # Fail to reject consistency
    
    # Prepare results
    results = {
        'invariant_name': invariant_name,
        'invariants': invariants,
        'weighted_mean': weighted_mean,
        'weighted_sigma': weighted_sigma,
        'chi2': chi2,
        'dof': dof,
        'p_value': p_value,
        'consistent': consistent
    }
    
    # Print summary
    print("\n" + "="*60)
    print(f"CROSS-DATASET INVARIANCE TEST: {invariant_name}")
    print("="*60)
    print(f"χ² / dof = {chi2:.3f} / {dof} = {chi2/dof:.3f}")
    print(f"P-value = {p_value:.6f}")
    
    if consistent:
        print("Result: CONSISTENT across datasets (supports UBT)")
        if p_value > 0.32:
            print("  (Strong agreement, χ² < expected)")
    else:
        print("Result: INCONSISTENT - UBT mapping potentially falsified")
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
        Results from run_invariance_test
    output_dir : str or Path
        Output directory
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    inv_name = results['invariant_name']
    
    # Save summary
    with open(output_dir / f'invariance_{inv_name}_results.txt', 'w') as f:
        f.write(f"CROSS-DATASET INVARIANCE TEST: {inv_name}\n")
        f.write("="*60 + "\n\n")
        
        f.write("Dataset estimates:\n")
        for inv in results['invariants']:
            f.write(f"  {inv['name']:20s}: {inv['value']:10.6f} ± {inv['sigma']:.6f}\n")
        
        f.write(f"\nWeighted mean: {results['weighted_mean']:.6f} ± {results['weighted_sigma']:.6f}\n")
        f.write(f"χ² = {results['chi2']:.3f}\n")
        f.write(f"dof = {results['dof']}\n")
        f.write(f"χ² / dof = {results['chi2']/results['dof']:.3f}\n")
        f.write(f"P-value = {results['p_value']:.6f}\n")
        f.write(f"Consistent: {results['consistent']}\n")
    
    # Save table for plotting
    with open(output_dir / f'invariance_{inv_name}_table.txt', 'w') as f:
        f.write("# Dataset  Value  Sigma\n")
        for inv in results['invariants']:
            f.write(f"{inv['name']}  {inv['value']:.6f}  {inv['sigma']:.6f}\n")
    
    print(f"Results saved to {output_dir}")


def plot_results(results, output_dir):
    """
    Generate forest plot (requires matplotlib).
    
    Parameters
    ----------
    results : dict
        Results from run_invariance_test
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
    
    inv_name = results['invariant_name']
    
    # Forest plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    invariants = results['invariants']
    n_datasets = len(invariants)
    
    names = [inv['name'] for inv in invariants]
    values = [inv['value'] for inv in invariants]
    sigmas = [inv['sigma'] for inv in invariants]
    
    y_pos = np.arange(n_datasets)
    
    # Plot each dataset with error bars
    ax.errorbar(values, y_pos, xerr=sigmas, fmt='o', markersize=8,
                capsize=5, capthick=2, label='Dataset estimates')
    
    # Plot weighted mean
    weighted_mean = results['weighted_mean']
    weighted_sigma = results['weighted_sigma']
    
    ax.axvline(weighted_mean, color='r', linestyle='--', linewidth=2,
               label=f'Weighted mean ± 1σ')
    ax.axvspan(weighted_mean - weighted_sigma, weighted_mean + weighted_sigma,
               alpha=0.2, color='r')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names)
    ax.set_xlabel(f'UBT Invariant {inv_name}')
    ax.set_title(f'Cross-Dataset Consistency: {inv_name}\n' +
                 f'χ²/dof = {results["chi2"]:.2f}/{results["dof"]} = {results["chi2"]/results["dof"]:.2f}, ' +
                 f'p = {results["p_value"]:.4f}')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig(output_dir / f'invariance_{inv_name}_forest.png', dpi=150)
    plt.close()
    
    print(f"Plot saved to {output_dir}")


def main():
    """
    Main function for command-line usage.
    
    For demonstration, uses example datasets.
    In real analysis, load from files or command-line arguments.
    """
    print("UBT Cross-Dataset Invariance Test")
    print("="*60)
    print("\nNOTE: This is a demonstration with placeholder invariant functions.")
    print("Replace ubt_invariant_kappa() and ubt_invariant_eta() with actual")
    print("UBT formulae from the theory.\n")
    
    # Example datasets (replace with real data)
    # Testing invariant κ from Ω_b h²
    datasets_omega_b = [
        {
            'name': 'Planck TT+TE+EE',
            'param_value': 0.02237,
            'param_sigma': 0.00015
        },
        {
            'name': 'Planck TT+TE+EE+lensing',
            'param_value': 0.02242,
            'param_sigma': 0.00014
        },
        {
            'name': 'Planck+BAO',
            'param_value': 0.02233,
            'param_sigma': 0.00013
        },
        {
            'name': 'Planck+BAO+Pantheon',
            'param_value': 0.02240,
            'param_sigma': 0.00012
        }
    ]
    
    # Run test for κ
    output_dir = sys.argv[1] if len(sys.argv) > 1 else '../out'
    
    results_kappa = run_invariance_test(
        datasets_omega_b,
        ubt_invariant_kappa,
        invariant_name='kappa',
        output_dir=output_dir
    )
    
    # Generate plot if matplotlib available
    plot_results(results_kappa, output_dir)
    
    # Example: Test invariant η from n_s
    datasets_n_s = [
        {
            'name': 'Planck TT+TE+EE',
            'param_value': 0.9649,
            'param_sigma': 0.0042
        },
        {
            'name': 'Planck+lensing',
            'param_value': 0.9665,
            'param_sigma': 0.0038
        },
        {
            'name': 'Planck+BAO',
            'param_value': 0.9651,
            'param_sigma': 0.0041
        }
    ]
    
    results_eta = run_invariance_test(
        datasets_n_s,
        ubt_invariant_eta,
        invariant_name='eta',
        output_dir=output_dir
    )
    
    plot_results(results_eta, output_dir)
    
    return results_kappa, results_eta


if __name__ == '__main__':
    main()
