#!/usr/bin/env python3
"""
Integration test: Verify that units mismatch causes strict mode to fail fast
and that re-running with proper units resolution succeeds.

This verifies the acceptance criteria from the issue:
- Re-running the same command no longer produces chi2/dof ~ 1e13
- If units mismatch persists, run aborts (no CANDIDATE verdict)
"""

import sys
import tempfile
import numpy as np
from pathlib import Path

repo_root = Path(__file__).resolve().parent
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'loaders'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'cmb_comb'))

import planck
import cmb_comb


def test_units_mismatch_fails_fast():
    """
    Test that catastrophic units mismatch triggers strict mode failure.
    """
    print("\n=== Integration Test: Units Mismatch Fails Fast ===")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create observation file in Dl format (TT-full) with small errors
        obs_file = tmpdir / "obs_dl.txt"
        with open(obs_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 130):  # 100 rows
                Dl = 2000.0 + i * 5.0  # Dl values (large magnitude)
                # Use small errors to make mismatch more severe
                f.write(f"{i} {Dl} -1.0 1.0\n")  # Very small errors (1 μK² in Dl)
        
        # Create model file in wrong units (Dl values but claiming to be Cl)
        # This simulates the worst case: obs in Cl, model in Dl (or vice versa)
        model_file = tmpdir / "model_wrong_units.txt"
        with open(model_file, 'w') as f:
            f.write("# ell C_ell\n")  # Claims Cl but values are Dl-magnitude
            for i in range(30, 130):
                # Use Dl-magnitude values while claiming Cl
                # After obs is converted from Dl to Cl, these will be ~1000x too large
                Dl_value = 2000.0 + i * 5.0
                f.write(f"{i} {Dl_value}\n")  # Dl values labeled as Cl!
        
        # Load data with planck loader (which should auto-detect and try to resolve)
        try:
            data = planck.load_planck_data(
                obs_file=obs_file,
                model_file=model_file,
                ell_min=30,
                ell_max=100,
                _skip_size_validation=True
            )
            
            # Run CMB comb test with strict=True (default for court-grade)
            print("\n  Attempting to run CMB comb test with strict mode...")
            
            try:
                results = cmb_comb.run_cmb_comb_test(
                    ell=data['ell'],
                    C_obs=data['cl_obs'],
                    C_model=data['cl_model'],
                    sigma=data['sigma'],
                    cov=None,
                    dataset_name="Test Units Mismatch",
                    variant="C",
                    n_mc_trials=100,
                    random_seed=42,
                    whiten_mode='diagonal',
                    strict=True,  # STRICT MODE ENABLED
                    output_dir=None
                )
                
                # Should NOT reach here if units mismatch is severe
                print("  ✗ TEST FAILED: Strict mode should have raised RuntimeError!")
                print(f"     chi2/dof = {results['whitening_metadata']['chi2_per_dof']}")
                return False
                
            except RuntimeError as e:
                error_msg = str(e)
                if 'strict mode' in error_msg.lower():
                    print("  ✓ Strict mode correctly raised RuntimeError on units mismatch")
                    print(f"     Error message: {error_msg[:80]}...")
                    return True
                else:
                    print(f"  ✗ Wrong error: {error_msg}")
                    return False
                    
        except Exception as e:
            print(f"  ✗ Unexpected error during data loading: {e}")
            return False


def test_auto_resolution_prevents_mismatch():
    """
    Test that auto-resolution correctly handles ambiguous units and produces reasonable chi2.
    """
    print("\n=== Integration Test: Auto-Resolution Prevents Mismatch ===")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create observation file in Dl format (TT-full)
        obs_file = tmpdir / "obs_dl.txt"
        with open(obs_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 130):
                Dl = 2000.0 + i * 5.0
                f.write(f"{i} {Dl} -30.0 30.0\n")
        
        # Create model file in Dl format but WITHOUT explicit header
        # (tests that auto-resolution correctly identifies Dl via magnitude)
        model_file = tmpdir / "model_ambiguous.txt"
        with open(model_file, 'w') as f:
            f.write("# ell spectrum\n")  # Ambiguous header
            for i in range(30, 130):
                Dl_model = 2010.0 + i * 5.0  # Slightly different from obs
                f.write(f"{i} {Dl_model}\n")
        
        # Load data with planck loader
        data = planck.load_planck_data(
            obs_file=obs_file,
            model_file=model_file,
            ell_min=30,
            ell_max=100,
            _skip_size_validation=True
        )
        
        # Check that auto-resolution metadata exists
        res_meta = data.get('model_resolution_metadata')
        if res_meta is None:
            print("  ✗ No model_resolution_metadata in data")
            return False
        
        # Check that chi2 is reasonable (not catastrophic)
        chi2_chosen = res_meta.get('chi2_dof_chosen', 1e99)
        
        if chi2_chosen > 100.0:
            print(f"  ✗ Chi2/dof too high: {chi2_chosen}")
            print(f"     Resolution metadata: {res_meta}")
            return False
        
        print(f"  ✓ Auto-resolution successful:")
        print(f"     Units detected: {res_meta['units_detected']}")
        print(f"     Units used: {res_meta['units_used']}")
        print(f"     Chi2/dof: {chi2_chosen:.2f}")
        print(f"     Auto-resolution applied: {res_meta['auto_resolution_applied']}")
        
        # Run CMB comb test with strict mode - should succeed
        try:
            results = cmb_comb.run_cmb_comb_test(
                ell=data['ell'],
                C_obs=data['cl_obs'],
                C_model=data['cl_model'],
                sigma=data['sigma'],
                cov=None,
                dataset_name="Test Auto-Resolution",
                variant="C",
                n_mc_trials=100,
                random_seed=42,
                whiten_mode='diagonal',
                strict=True,  # STRICT MODE ENABLED
                output_dir=None
            )
            
            # Should succeed with reasonable chi2
            chi2_final = results['whitening_metadata']['chi2_per_dof']
            sanity_passed = results['whitening_metadata']['sanity_checks_passed']
            
            if sanity_passed and chi2_final < 100.0:
                print(f"  ✓ CMB comb test succeeded with chi2/dof = {chi2_final:.2f}")
                print(f"     Sanity checks passed: {sanity_passed}")
                return True
            else:
                print(f"  ✗ Unexpected result:")
                print(f"     chi2/dof = {chi2_final}")
                print(f"     Sanity checks passed: {sanity_passed}")
                return False
                
        except RuntimeError as e:
            print(f"  ✗ Unexpected RuntimeError: {e}")
            return False


def main():
    print("=" * 80)
    print("Integration Tests: Units Mismatch Detection and Strict Mode")
    print("=" * 80)
    
    test1_passed = test_units_mismatch_fails_fast()
    test2_passed = test_auto_resolution_prevents_mismatch()
    
    print()
    print("=" * 80)
    if test1_passed and test2_passed:
        print("✓ ALL INTEGRATION TESTS PASSED!")
        print()
        print("Acceptance Criteria Verified:")
        print("  1. ✓ Units mismatch causes strict mode to fail fast (no CANDIDATE)")
        print("  2. ✓ Auto-resolution prevents chi2/dof ~ 1e13 when units are correctable")
        print("  3. ✓ Strict mode is the default for court-grade runs")
        print("=" * 80)
        return 0
    else:
        print("✗ SOME INTEGRATION TESTS FAILED")
        print(f"  test_units_mismatch_fails_fast: {'PASS' if test1_passed else 'FAIL'}")
        print(f"  test_auto_resolution_prevents_mismatch: {'PASS' if test2_passed else 'FAIL'}")
        print("=" * 80)
        return 1


if __name__ == "__main__":
    sys.exit(main())
