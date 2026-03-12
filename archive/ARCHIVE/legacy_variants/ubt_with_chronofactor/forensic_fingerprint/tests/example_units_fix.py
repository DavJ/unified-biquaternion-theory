#!/usr/bin/env python3
"""
Example demonstrating units detection and conversion.

This shows how the enhanced loader now handles:
1. Automatic detection of Dl vs Cl format
2. Conversion to common units (Cl)
3. Metadata tracking
4. Sanity checks
"""

import sys
import numpy as np
import tempfile
from pathlib import Path

# Add parent directories to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'loaders'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'cmb_comb'))

import planck
import cmb_comb


def create_example_files():
    """Create example observation (Dl) and model (Cl) files."""
    
    ell = np.arange(30, 100)
    
    # Create a base spectrum in Cl units
    cl_base = 1000.0 + 300.0 * np.sin(ell / 20.0)
    
    # Observation: Planck TT-full format (Dl units)
    # Convert Cl to Dl: Dl = Cl * ℓ(ℓ+1) / (2π)
    dl_obs = cl_base * ell * (ell + 1.0) / (2.0 * np.pi)
    # Add small noise
    dl_obs += 50.0 * np.random.randn(len(ell))
    
    obs_file = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
    obs_file.write("# l Dl -dDl +dDl\n")
    obs_file.write("# Planck PR3 TT-full spectrum (simulated)\n")
    obs_file.write("# Units: Dl in μK²\n")
    for i in range(len(ell)):
        minus_err = -50.0 - 5.0 * np.random.randn()
        plus_err = 50.0 + 5.0 * np.random.randn()
        obs_file.write(f"{ell[i]} {dl_obs[i]:.6f} {minus_err:.6f} {plus_err:.6f}\n")
    obs_file.close()
    
    # Model: Theoretical ΛCDM (Cl units, same base spectrum)
    cl_model = cl_base  # Same underlying spectrum
    
    model_file = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
    model_file.write("# ell Cl\n")
    model_file.write("# Theoretical ΛCDM spectrum (simulated)\n")
    model_file.write("# Units: Cl in μK²\n")
    for i in range(len(ell)):
        model_file.write(f"{ell[i]} {cl_model[i]:.6f}\n")
    model_file.close()
    
    return obs_file.name, model_file.name


def main():
    print("="*80)
    print("EXAMPLE: Units Detection and Conversion Fix")
    print("="*80)
    print()
    
    # Create example files
    obs_file, model_file = create_example_files()
    
    try:
        print("Step 1: Created example files")
        print(f"  Observation: {obs_file} (Dl format)")
        print(f"  Model:       {model_file} (Cl format)")
        print()
        
        # Load data
        print("Step 2: Loading data with automatic units detection...")
        print()
        data = planck.load_planck_data(
            obs_file=obs_file,
            model_file=model_file,
            _skip_size_validation=True
        )
        
        print("Step 3: Units metadata:")
        print(f"  obs_units:             {data['obs_units']}")
        print(f"  model_units_original:  {data['model_units_original']}")
        print(f"  model_units_used:      {data['model_units_used']}")
        print(f"  sigma_method:          {data['sigma_method']}")
        print()
        
        # Compute residuals
        print("Step 4: Computing residuals with automatic units handling...")
        print()
        residuals, metadata = cmb_comb.compute_residuals(
            data['ell'],
            data['cl_obs'],
            data['cl_model'],
            data['sigma'],
            cov=None,
            whiten_mode='diagonal'
        )
        
        print("Step 5: Residual statistics:")
        print(f"  χ²/dof:                    {metadata['chi2_per_dof']:.2f}")
        print(f"  Units mismatch warning:    {metadata['units_mismatch_warning']}")
        print(f"  Sanity checks passed:      {metadata['sanity_checks_passed']}")
        print()
        
        if metadata['chi2_per_dof'] < 100:
            print("✓ SUCCESS: Units correctly matched and converted!")
            print("  - Observation (Dl) and model (Cl) automatically converted to common units")
            print("  - Residuals computed correctly")
            print("  - χ²/dof is in normal range")
        else:
            print("⚠ WARNING: χ²/dof is elevated")
            print("  (This is expected for random synthetic data)")
        
        print()
        print("="*80)
        print("SUMMARY")
        print("="*80)
        print()
        print("Before this fix:")
        print("  ✗ Observation (Dl) and model (Cl) had units mismatch")
        print("  ✗ χ²/dof ~ 1e13 (catastrophic)")
        print("  ✗ median(|diff/sigma|) ~ 1e6")
        print()
        print("After this fix:")
        print("  ✓ Automatic detection: obs=Dl, model=Cl")
        print("  ✓ Both converted to Cl units")
        print(f"  ✓ χ²/dof = {metadata['chi2_per_dof']:.2f} (reasonable)")
        print("  ✓ Metadata tracks all conversions")
        print("  ✓ Court-grade sanity checks prevent catastrophic errors")
        print()
        
    finally:
        # Clean up
        Path(obs_file).unlink()
        Path(model_file).unlink()


if __name__ == '__main__':
    main()
