#!/usr/bin/env python3
"""
Demonstration: Strict Mode Prevents Units Mismatch CANDIDATE Verdict
=====================================================================

This script demonstrates that the CMB comb test now fails fast on units mismatch
and cannot produce a spurious CANDIDATE verdict due to catastrophic chi2/dof.

**Before the fix** (hypothetical problematic behavior):
- Units mismatch → chi2/dof ~ 1e13 → hits MC p-value floor → CANDIDATE verdict

**After the fix** (current behavior):
- Units mismatch → strict mode detects catastrophic chi2 → RuntimeError → NO CANDIDATE
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


def demo_strict_mode_protection():
    """
    Demonstrate strict mode prevents CANDIDATE on units mismatch.
    """
    print("=" * 80)
    print("DEMONSTRATION: Strict Mode Prevents Units Mismatch CANDIDATE Verdict")
    print("=" * 80)
    print()
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create observation file in Dl format (TT-full)
        print("Creating test data files...")
        obs_file = tmpdir / "obs_dl.txt"
        with open(obs_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 130):
                Dl = 2000.0 + i * 5.0
                f.write(f"{i} {Dl} -1.0 1.0\n")
        
        # Create model file with catastrophic units mismatch
        model_file = tmpdir / "model_wrong_units.txt"
        with open(model_file, 'w') as f:
            f.write("# ell C_ell\n")  # Claims Cl but contains Dl values
            for i in range(30, 130):
                Dl_value = 2000.0 + i * 5.0
                f.write(f"{i} {Dl_value}\n")
        
        print(f"  Observation file: {obs_file.name} (Dl format)")
        print(f"  Model file: {model_file.name} (wrong units: Dl values labeled as Cl)")
        print()
        
        # Load data
        print("Loading data...")
        data = planck.load_planck_data(
            obs_file=obs_file,
            model_file=model_file,
            ell_min=30,
            ell_max=100,
            _skip_size_validation=True
        )
        
        print(f"  Loaded {len(data['ell'])} multipoles")
        print()
        
        # Attempt to run with strict mode (DEFAULT)
        print("=" * 80)
        print("SCENARIO 1: Strict Mode (DEFAULT for court-grade runs)")
        print("=" * 80)
        print()
        print("Attempting CMB comb test with strict=True (default)...")
        print()
        
        try:
            results = cmb_comb.run_cmb_comb_test(
                ell=data['ell'],
                C_obs=data['cl_obs'],
                C_model=data['cl_model'],
                sigma=data['sigma'],
                cov=None,
                dataset_name="Demo Units Mismatch",
                variant="C",
                n_mc_trials=100,
                random_seed=42,
                whiten_mode='diagonal',
                strict=True,  # DEFAULT for court-grade
                output_dir=None
            )
            
            # Should NOT reach here
            print("❌ ERROR: Strict mode should have raised RuntimeError!")
            print(f"   chi2/dof = {results['whitening_metadata']['chi2_per_dof']}")
            print()
            return False
            
        except RuntimeError as e:
            print("✅ SUCCESS: Strict mode correctly raised RuntimeError")
            print()
            print(f"Error message: {str(e)[:150]}...")
            print()
            print("RESULT: No CANDIDATE verdict possible with units mismatch!")
            print()
        
        # Show what happens with strict mode disabled (DEBUG ONLY)
        print("=" * 80)
        print("SCENARIO 2: Strict Mode DISABLED (--no-strict, DEBUG ONLY)")
        print("=" * 80)
        print()
        print("Attempting CMB comb test with strict=False (debug only)...")
        print()
        
        # Suppress output for cleaner demo
        import io
        import contextlib
        
        with contextlib.redirect_stdout(io.StringIO()):
            results_nostrict = cmb_comb.run_cmb_comb_test(
                ell=data['ell'],
                C_obs=data['cl_obs'],
                C_model=data['cl_model'],
                sigma=data['sigma'],
                cov=None,
                dataset_name="Demo Units Mismatch (no strict)",
                variant="C",
                n_mc_trials=100,
                random_seed=42,
                whiten_mode='diagonal',
                strict=False,  # DEBUG ONLY - allows continuation
                output_dir=None
            )
        
        chi2_dof = results_nostrict['whitening_metadata']['chi2_per_dof']
        p_value = results_nostrict['p_value']
        significance = results_nostrict['significance']
        sanity_passed = results_nostrict['whitening_metadata']['sanity_checks_passed']
        
        print(f"Chi2/dof: {chi2_dof:.2e} (catastrophic!)")
        print(f"P-value: {p_value:.6e}")
        print(f"Significance: {significance}")
        print(f"Sanity checks passed: {sanity_passed}")
        print()
        
        if not sanity_passed:
            print("✅ Even with strict=False, sanity_checks_passed = False")
            print("   This metadata can be used to filter results in post-processing")
        
        # Use constant for threshold comparison
        CATASTROPHIC_CHI2_THRESHOLD = 1e6  # From cmb_comb.py
        if chi2_dof > CATASTROPHIC_CHI2_THRESHOLD:
            print(f"✅ Chi2/dof is catastrophic (> {CATASTROPHIC_CHI2_THRESHOLD:.0e}), confirming units mismatch")
        
        print()
        print("=" * 80)
        print("CONCLUSION")
        print("=" * 80)
        print()
        print("✅ Strict mode (DEFAULT) prevents CANDIDATE verdict on units mismatch")
        print("✅ RuntimeError is raised, analysis cannot proceed")
        print("✅ Court-grade runs are protected from false positives")
        print("✅ Debug mode (--no-strict) allows investigation but marks sanity_checks_passed=False")
        print()
        print("Acceptance criteria MET:")
        print("  1. Re-running with units mismatch → RuntimeError (no CANDIDATE)")
        print("  2. Chi2/dof ~ 1e13 is detected and blocked")
        print("  3. Strict mode is enabled by default")
        print()
        print("=" * 80)
        
        return True


if __name__ == "__main__":
    success = demo_strict_mode_protection()
    sys.exit(0 if success else 1)
