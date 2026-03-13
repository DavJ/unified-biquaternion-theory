#!/usr/bin/env python3
"""
Example: Running UBT Forensic Fingerprint Tests with Synthetic Data
====================================================================

This script demonstrates how to run all three forensic fingerprint tests
using synthetic data. It serves as a template for real analysis with
actual cosmological data.

For real analysis, replace synthetic data generation with actual:
- Planck CMB power spectra (Test #1)
- MCMC chain files (Test #2)
- Parameter estimates from published papers (Test #3)

Author: UBT Research Team
License: MIT
"""

import sys
from pathlib import Path
import numpy as np

# Add forensic_fingerprint modules to path
repo_root = Path(__file__).parent
sys.path.insert(0, str(repo_root / 'cmb_comb'))
sys.path.insert(0, str(repo_root / 'grid_255'))
sys.path.insert(0, str(repo_root / 'invariance'))

import cmb_comb
import grid_255
import invariance


def example_cmb_comb_test():
    """
    Example: CMB comb test with synthetic data.
    
    In real analysis:
    1. Download Planck 2018 power spectra from https://pla.esac.esa.int/
    2. Load observed C_ell, model C_ell, and uncertainties
    3. Run test on real data
    """
    print("\n" + "="*70)
    print("EXAMPLE 1: CMB COMB TEST")
    print("="*70 + "\n")
    
    # Generate synthetic CMB-like data
    print("Generating synthetic CMB power spectrum data...")
    np.random.seed(42)
    
    ell = np.arange(2, 200)
    
    # Simple ΛCDM-like spectrum
    C_model = 6000.0 * (ell / 10.0)**(-0.5) * np.exp(-ell / 800.0)
    
    # Add uncertainties
    sigma = 0.05 * C_model + 100.0  # Cosmic variance + noise
    
    # Generate "observed" data (null case: no signal)
    C_obs = C_model + np.random.normal(0, sigma)
    
    # Run test with reduced MC trials for speed
    print("Running CMB comb test (this may take a moment)...")
    cmb_comb.N_MC_TRIALS = 1000  # Reduced from 10000 for demo
    
    output_dir = repo_root / 'out' / 'example_cmb'
    results = cmb_comb.run_cmb_comb_test(ell, C_obs, C_model, sigma, output_dir)
    
    # Generate plots
    cmb_comb.plot_results(results, output_dir)
    
    print(f"\nResults saved to: {output_dir}")
    print("Check out the plots: residuals_with_fit.png and null_distribution.png")
    
    return results


def example_grid_255_test():
    """
    Example: Grid 255 test with synthetic data.
    
    In real analysis:
    1. Download Planck MCMC chains from https://pla.esac.esa.int/
    2. Extract parameter samples (e.g., Ω_b h²)
    3. Run test on each parameter
    """
    print("\n" + "="*70)
    print("EXAMPLE 2: GRID 255 QUANTIZATION TEST")
    print("="*70 + "\n")
    
    # Generate synthetic MCMC samples (null case: no quantization)
    print("Generating synthetic MCMC samples (Gaussian, no grid alignment)...")
    np.random.seed(137)
    
    # Simulate Ω_b h² posterior
    omega_b_mean = 0.02237
    omega_b_std = 0.00015
    samples = np.random.normal(omega_b_mean, omega_b_std, size=10000)
    
    # Run test with reduced MC trials
    print("Running grid 255 test...")
    grid_255.N_MC_TRIALS = 1000  # Reduced from 10000 for demo
    
    output_dir = repo_root / 'out' / 'example_grid'
    results = grid_255.run_grid_255_test(samples, parameter_name='omega_b_h2', 
                                         output_dir=output_dir)
    
    # Generate plots
    grid_255.plot_results(results, output_dir)
    
    print(f"\nResults saved to: {output_dir}")
    print("Check out the plots: grid_255_omega_b_h2_distances.png")
    
    return results


def example_invariance_test():
    """
    Example: Cross-dataset invariance test.
    
    In real analysis:
    1. Extract parameter estimates from published papers
    2. Define actual UBT invariant formula (replace placeholder)
    3. Run test on real datasets
    """
    print("\n" + "="*70)
    print("EXAMPLE 3: CROSS-DATASET INVARIANCE TEST")
    print("="*70 + "\n")
    
    print("NOTE: Using placeholder invariant function.")
    print("Replace ubt_invariant_kappa() with actual UBT formula!\n")
    
    # Example datasets (from Planck 2018 papers)
    datasets_omega_b = [
        {
            'name': 'Planck TT+TE+EE',
            'param_value': 0.02237,
            'param_sigma': 0.00015
        },
        {
            'name': 'Planck+lensing',
            'param_value': 0.02242,
            'param_sigma': 0.00014
        },
        {
            'name': 'Planck+BAO',
            'param_value': 0.02233,
            'param_sigma': 0.00013
        },
    ]
    
    # Run test
    print("Running cross-dataset invariance test...")
    output_dir = repo_root / 'out' / 'example_invariance'
    results = invariance.run_invariance_test(
        datasets_omega_b,
        invariance.ubt_invariant_kappa,
        invariant_name='kappa',
        output_dir=output_dir
    )
    
    # Generate plot
    invariance.plot_results(results, output_dir)
    
    print(f"\nResults saved to: {output_dir}")
    print("Check out the plot: invariance_kappa_forest.png")
    
    return results


def main():
    """
    Run all three example tests.
    """
    print("\n" + "="*70)
    print("UBT FORENSIC FINGERPRINT EXAMPLES")
    print("="*70)
    print("\nThis script demonstrates all three tests with synthetic data.")
    print("For real analysis, replace with actual cosmological data.\n")
    
    # Run examples
    results_cmb = example_cmb_comb_test()
    results_grid = example_grid_255_test()
    results_inv = example_invariance_test()
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY OF EXAMPLE RUNS")
    print("="*70)
    print(f"\nTest #1 (CMB Comb):")
    print(f"  Best period: Δℓ = {results_cmb['best_period']}")
    print(f"  P-value: {results_cmb['p_value']:.6f}")
    print(f"  Significance: {results_cmb['significance'].upper()}")
    
    print(f"\nTest #2 (Grid 255):")
    print(f"  S₁ (median dist): {results_grid['S1_obs']:.6e}")
    print(f"  P-value (min): {results_grid['p_min']:.6f}")
    print(f"  Significance: {results_grid['significance'].upper()}")
    
    print(f"\nTest #3 (Invariance):")
    print(f"  χ² / dof: {results_inv['chi2']:.3f} / {results_inv['dof']}")
    print(f"  P-value: {results_inv['p_value']:.6f}")
    print(f"  Consistent: {results_inv['consistent']}")
    
    print("\n" + "="*70)
    print("All outputs saved to: forensic_fingerprint/out/example_*/")
    print("="*70 + "\n")
    
    print("Next steps for real analysis:")
    print("1. Download Planck 2018 data from https://pla.esac.esa.int/")
    print("2. Replace synthetic data with real observations")
    print("3. Implement actual UBT invariant formulae (Test #3)")
    print("4. Run with full MC trials (N=10000)")
    print("5. Document results following PROTOCOL.md\n")


if __name__ == '__main__':
    main()
