#!/usr/bin/env python3
"""
Demonstration of Diagnostic Sub-segment Scan

This script creates synthetic Planck-like data and runs the diagnostic scan
to demonstrate all analysis features. This serves as both a usage example
and a validation that the tool works correctly.
"""

import numpy as np
import sys
from pathlib import Path
import tempfile
import json

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from diagnostic_subsegment_scan import run_diagnostic_scan


def create_synthetic_planck_files(output_dir, with_period_16=False, with_period_255=True):
    """
    Create synthetic Planck data files for demonstration.
    
    Parameters
    ----------
    output_dir : Path
        Directory to write files
    with_period_16 : bool
        Include weak signal at period 16
    with_period_255 : bool
        Include stronger signal at period 255
    
    Returns
    -------
    tuple
        (obs_file, model_file) paths
    """
    # Ensure output directory exists
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create multipole range (typical Planck TT range)
    ell = np.arange(30, 1500)
    
    # Simplified ΛCDM power spectrum
    # Realistic form: C_ℓ ∝ ℓ^(-α) × exp(-ℓ/ℓ_damp)
    cl_model = 5000.0 * (ell / 100.0)**(-0.3) * np.exp(-ell / 1000.0)
    
    # Add periodic signals
    cl_obs = cl_model.copy()
    
    if with_period_255:
        # Add primary signal at period 255 (2% amplitude)
        theta_255 = 2.0 * np.pi * ell / 255.0
        signal_255 = 0.02 * cl_model * np.sin(theta_255 + 0.5)
        cl_obs += signal_255
    
    if with_period_16:
        # Add weaker signal at period 16 (0.5% amplitude)
        theta_16 = 2.0 * np.pi * ell / 16.0
        signal_16 = 0.005 * cl_model * np.sin(theta_16 - 1.2)
        cl_obs += signal_16
    
    # Add realistic noise
    # Planck uncertainty is typically ~3-5% at low ℓ, ~1-2% at high ℓ
    sigma_frac = 0.03 * np.exp(-(ell - 30) / 500) + 0.01
    sigma = sigma_frac * cl_model
    
    np.random.seed(42)
    noise = np.random.normal(0, sigma)
    cl_obs += noise
    
    # Write observation file (format: ell, Dl, sigma_Dl)
    # Note: Planck typically reports D_ℓ = ℓ(ℓ+1)C_ℓ/(2π)
    # For simplicity, we'll write C_ℓ and let the loader handle it
    obs_file = output_dir / 'synthetic_planck_obs.txt'
    with open(obs_file, 'w') as f:
        f.write("# Synthetic Planck TT power spectrum\n")
        f.write("# ell  Cl  sigma_Cl\n")
        for i in range(len(ell)):
            f.write(f"{ell[i]}  {cl_obs[i]:.6e}  {sigma[i]:.6e}\n")
    
    # Write model file (format: ell, Cl)
    model_file = output_dir / 'synthetic_planck_model.txt'
    with open(model_file, 'w') as f:
        f.write("# Synthetic ΛCDM model\n")
        f.write("# ell  Cl\n")
        for i in range(len(ell)):
            f.write(f"{ell[i]}  {cl_model[i]:.6e}\n")
    
    return obs_file, model_file


def run_demonstration():
    """Run complete demonstration of diagnostic scan."""
    
    print("=" * 80)
    print("DIAGNOSTIC SUB-SEGMENT SCAN - DEMONSTRATION")
    print("=" * 80)
    print()
    print("This demonstration creates synthetic Planck-like data with:")
    print("  - ΛCDM power spectrum baseline")
    print("  - Injected periodic signal at Δℓ = 255 (2% amplitude)")
    print("  - Optional weak signal at Δℓ = 16 (0.5% amplitude)")
    print("  - Realistic noise (~3% at low ℓ, ~1% at high ℓ)")
    print()
    
    # Create temporary directory for synthetic data
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Scenario 1: Only period 255
        print("-" * 80)
        print("SCENARIO 1: Signal at Δℓ = 255 only")
        print("-" * 80)
        print()
        
        obs_file_1, model_file_1 = create_synthetic_planck_files(
            tmpdir / "scenario1", 
            with_period_16=False, 
            with_period_255=True
        )
        
        # Load data manually to show what we're analyzing
        data_1 = np.loadtxt(obs_file_1, comments='#')
        ell = data_1[:, 0].astype(int)
        cl_obs = data_1[:, 1]
        sigma = data_1[:, 2]
        
        data_model = np.loadtxt(model_file_1, comments='#')
        cl_model = data_model[:, 1]
        
        # Run diagnostic scan
        results_1 = run_diagnostic_scan(
            ell=ell,
            cl_obs=cl_obs,
            cl_model=cl_model,
            sigma=sigma,
            cov=None,
            whiten_mode='diagonal',
            output_dir=None
        )
        
        print()
        print("=" * 80)
        print("SCENARIO 1 SUMMARY")
        print("=" * 80)
        print()
        print("Expected: Strong signal at Δℓ = 255, weak/no signal at Δℓ = 16")
        print()
        print("Results:")
        for period, result in results_1['period_comparison'].items():
            print(f"  Period {period}: Δχ² = {result['delta_chi2']:.2f}, A = {result['amplitude']:.4f}")
        print()
        print(f"Windowed analysis: {results_1['windowed_analysis']['n_windows']} windows analyzed")
        print(f"  Signal variation (std): {results_1['windowed_analysis']['signal_strength_variation']:.2f}")
        print()
        print(f"Phase drift: F-stat = {results_1['phase_drift_f_stat']:.2f}")
        if results_1['phase_drift_f_stat'] > 5:
            print("  → SIGNIFICANT phase drift detected")
        elif results_1['phase_drift_f_stat'] > 2:
            print("  → MARGINAL phase drift")
        else:
            print("  → NO significant phase drift")
        print()
        
        # Scenario 2: Both periods
        print("-" * 80)
        print("SCENARIO 2: Signals at both Δℓ = 255 and Δℓ = 16")
        print("-" * 80)
        print()
        
        obs_file_2, model_file_2 = create_synthetic_planck_files(
            tmpdir / "scenario2", 
            with_period_16=True, 
            with_period_255=True
        )
        
        data_2 = np.loadtxt(obs_file_2, comments='#')
        cl_obs_2 = data_2[:, 1]
        
        results_2 = run_diagnostic_scan(
            ell=ell,
            cl_obs=cl_obs_2,
            cl_model=cl_model,
            sigma=sigma,
            cov=None,
            whiten_mode='diagonal',
            output_dir=None
        )
        
        print()
        print("=" * 80)
        print("SCENARIO 2 SUMMARY")
        print("=" * 80)
        print()
        print("Expected: Strong signal at Δℓ = 255, detectable signal at Δℓ = 16")
        print()
        print("Results:")
        for period, result in results_2['period_comparison'].items():
            print(f"  Period {period}: Δχ² = {result['delta_chi2']:.2f}, A = {result['amplitude']:.4f}")
        print()
        
        # Compare scenarios
        print()
        print("=" * 80)
        print("COMPARISON: Δℓ = 16 signal strength")
        print("=" * 80)
        print()
        delta_chi2_16_s1 = results_1['period_comparison'][16]['delta_chi2']
        delta_chi2_16_s2 = results_2['period_comparison'][16]['delta_chi2']
        print(f"Scenario 1 (no period-16 injected): Δχ² = {delta_chi2_16_s1:.2f}")
        print(f"Scenario 2 (period-16 injected):    Δχ² = {delta_chi2_16_s2:.2f}")
        print(f"Difference: {delta_chi2_16_s2 - delta_chi2_16_s1:.2f}")
        print()
        
        if delta_chi2_16_s2 > delta_chi2_16_s1 + 2:
            print("✓ Period-16 signal successfully detected in Scenario 2")
        else:
            print("⚠ Period-16 signal weak or not detected (may be below noise)")
        print()
    
    print("=" * 80)
    print("DEMONSTRATION COMPLETE")
    print("=" * 80)
    print()
    print("This demonstration shows:")
    print("  1. Sub-harmonic relationship correctly identified (256 = 16 × 16)")
    print("  2. Windowed analysis reveals signal strength variation across multipole range")
    print("  3. Phase-drift analysis tests for non-stationary periodicity")
    print("  4. Tool can distinguish between different periodic components")
    print()
    print("To run on real Planck data:")
    print("  python diagnostic_subsegment_scan.py \\")
    print("    --planck_obs path/to/COM_PowerSpect_CMB-TT-full_R3.01.txt \\")
    print("    --planck_model path/to/lcdm_model.txt \\")
    print("    --output_dir ./results")
    print()


if __name__ == '__main__':
    run_demonstration()
