#!/usr/bin/env python3
# tests/test_planck_units_and_strict_mode.py
# SPDX-License-Identifier: MIT
"""
Test: Planck Units Detection, Auto-Resolution, and Strict Mode
===============================================================

Tests for the enhanced unit detection, automatic resolution, and strict mode
features added to prevent false CANDIDATE results due to units/model mismatch.

Covers:
- Variant keyword detection for Dl (D_ell, Dℓ, D_l, DlTT, etc.)
- Magnitude-based heuristics (median and 90th percentile for ell > 30)
- Automatic unit resolution with chi2 precheck
- Strict mode enforcement (raises RuntimeError on catastrophic mismatch)
"""
import sys
import tempfile
import numpy as np
from pathlib import Path

# Ensure imports work
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

# Add forensic_fingerprint loaders to path
loaders_path = repo_root / 'forensic_fingerprint' / 'loaders'
if str(loaders_path) not in sys.path:
    sys.path.insert(0, str(loaders_path))

cmb_comb_path = repo_root / 'forensic_fingerprint' / 'cmb_comb'
if str(cmb_comb_path) not in sys.path:
    sys.path.insert(0, str(cmb_comb_path))

import planck
import cmb_comb


def test_variant_keyword_detection():
    """
    Test that variant Dl keywords are correctly detected.
    """
    print("\n=== Test: Variant Keyword Detection ===")
    
    # Test various Dl variant keywords
    test_cases = [
        ("# l D_ell sigma", "Dl", "D_ell"),
        ("# ell Dℓ error", "Dl", "Dℓ"),
        ("# L D_l -dDl +dDl", "Dl", "D_l"),
        ("# multipole DlTT DlEE", "Dl", "DlTT"),
        ("# l DLTT", "Dl", "DLTT"),
        ("# ell C_ell sigma", "Cl", "C_ell"),
        ("# l ClTT", "Cl", "ClTT"),
    ]
    
    ell = np.arange(2, 100, dtype=int)
    values_dl = np.ones(len(ell)) * 2000.0  # Dl-like magnitude
    values_cl = np.ones(len(ell)) * 0.5     # Cl-like magnitude
    
    for header, expected_units, keyword in test_cases:
        header_lines = [header]
        
        # Use Dl-like values for Dl headers, Cl-like for Cl headers
        values = values_dl if expected_units == "Dl" else values_cl
        
        detected = planck.detect_units_from_header_or_magnitude(header_lines, ell, values)
        
        assert detected == expected_units, \
            f"Failed for keyword '{keyword}': expected {expected_units}, got {detected}"
        print(f"✓ Correctly detected '{keyword}' as {detected}")
    
    print("✓ All variant keyword tests passed")


def test_magnitude_heuristic_ell_cutoff():
    """
    Test that magnitude heuristic uses ell > 30 cutoff and both median and 90th percentile.
    """
    print("\n=== Test: Magnitude Heuristic with ell > 30 Cutoff ===")
    
    # Create data with low-ell anomaly but Dl-like values at ell > 30
    ell = np.arange(2, 200, dtype=int)
    values = np.ones(len(ell))
    
    # Low-ell values are small (Cl-like)
    values[ell <= 30] = 0.1
    
    # High-ell values are large (Dl-like)
    values[ell > 30] = 3000.0
    
    # No header, should rely on magnitude
    header_lines = ["# l spectrum"]
    
    detected = planck.detect_units_from_header_or_magnitude(header_lines, ell, values)
    
    assert detected == "Dl", \
        f"Should detect Dl based on ell > 30 values, got {detected}"
    print(f"✓ Correctly used ell > 30 cutoff, detected: {detected}")
    
    # Test 90th percentile detection
    ell2 = np.arange(2, 200, dtype=int)
    values2 = np.ones(len(ell2)) * 500.0  # Borderline
    
    # Make 90th percentile clearly Dl
    values2[int(len(values2) * 0.85):] = 5000.0
    
    header_lines2 = ["# l data"]
    detected2 = planck.detect_units_from_header_or_magnitude(header_lines2, ell2, values2)
    
    assert detected2 == "Dl", \
        f"Should detect Dl based on 90th percentile, got {detected2}"
    print(f"✓ Correctly used 90th percentile, detected: {detected2}")
    
    print("✓ Magnitude heuristic tests passed")


def test_tt_full_parsing_with_sigma():
    """
    Test that TT-full format is parsed correctly with sigma conversion.
    """
    print("\n=== Test: TT-Full Format Parsing ===")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create TT-full format file (4 columns: ell, Dl, -dDl, +dDl)
        tt_full_file = tmpdir / "tt_full_spectrum.txt"
        with open(tt_full_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 130):  # 100 rows
                Dl = 1000.0 + i * 10.0
                minus_err = -50.0
                plus_err = 50.0
                f.write(f"{i} {Dl} {minus_err} {plus_err}\n")
        
        # Load with skip validation
        ell, cl, sigma, units = planck._load_planck_text(tt_full_file, _skip_size_validation=True)
        
        # Verify units detected as Dl
        assert units == "Dl", f"TT-full should be detected as Dl, got {units}"
        
        # Verify conversion applied: Cl = Dl * 2π / [l(l+1)]
        # For ell=30, Dl=1300, Cl should be ~ 1300 * 2π / (30*31) ~ 8.79
        expected_cl_30 = 1300.0 * (2.0 * np.pi) / (30.0 * 31.0)
        actual_cl_30 = cl[0]
        
        assert abs(actual_cl_30 - expected_cl_30) / expected_cl_30 < 0.01, \
            f"Cl conversion incorrect: expected {expected_cl_30}, got {actual_cl_30}"
        
        # Verify sigma conversion: sigma = 0.5 * (|+dDl| + |-dDl|) * conversion
        # sigma_Dl = 0.5 * (50 + 50) = 50
        # sigma_Cl = 50 * 2π / (30*31) ~ 0.338
        expected_sigma_30 = 50.0 * (2.0 * np.pi) / (30.0 * 31.0)
        actual_sigma_30 = sigma[0]
        
        assert abs(actual_sigma_30 - expected_sigma_30) / expected_sigma_30 < 0.01, \
            f"Sigma conversion incorrect: expected {expected_sigma_30}, got {actual_sigma_30}"
        
        # Verify sigma is positive
        assert np.all(sigma > 0), "All sigma values must be positive"
        
        print(f"✓ TT-full format parsed correctly")
        print(f"  ell[0]={ell[0]}, cl[0]={cl[0]:.4f}, sigma[0]={sigma[0]:.4f}")
        print(f"  Units detected: {units}")
        print(f"  Dl->Cl conversion verified")


def test_auto_resolution_with_chi2():
    """
    Test automatic unit resolution using chi2 precheck.
    """
    print("\n=== Test: Auto-Resolution with Chi2 Precheck ===")
    
    # Create synthetic data
    ell = np.arange(30, 100, dtype=int)
    n = len(ell)
    
    # Generate true Cl values (small magnitude)
    Cl_true = 1.0 / (ell + 10.0)  # Decaying spectrum, O(0.01..0.1)
    
    # Observation = true + noise
    sigma = 0.01 * np.ones(n)
    Cl_obs = Cl_true + np.random.normal(0, sigma)
    
    # Model file contains Dl (large magnitude)
    # We'll test that auto_resolve_model_units correctly converts it
    Dl_model = Cl_true * ell * (ell + 1.0) / (2.0 * np.pi)
    
    # Call auto_resolve_model_units
    model_cl, units_used, metadata = planck.auto_resolve_model_units(
        ell, Dl_model, Cl_obs, sigma, units_detected="Cl"  # Wrongly detected as Cl
    )
    
    # Should have chosen Dl interpretation
    assert units_used == "Dl", \
        f"Auto-resolution should choose Dl interpretation, got {units_used}"
    
    # Chi2 for Dl interpretation should be reasonable (O(1))
    chi2_dl = metadata['chi2_dof_interp_dl']
    assert chi2_dl < 10.0, \
        f"Chi2/dof for Dl interpretation should be reasonable, got {chi2_dl}"
    
    # Chi2 for Cl interpretation should be catastrophic (model is Dl, obs is Cl)
    chi2_cl = metadata['chi2_dof_interp_cl']
    assert chi2_cl > 1e5, \
        f"Chi2/dof for Cl interpretation should be catastrophic, got {chi2_cl}"
    
    print(f"✓ Auto-resolution correctly chose: {units_used}")
    print(f"  chi2/dof (Cl): {chi2_cl:.2e}")
    print(f"  chi2/dof (Dl): {chi2_dl:.2e}")
    print(f"  Auto-resolution applied: {metadata['auto_resolution_applied']}")


def test_strict_mode_raises_on_mismatch():
    """
    Test that strict mode raises RuntimeError on catastrophic units mismatch.
    """
    print("\n=== Test: Strict Mode Raises on Mismatch ===")
    
    # Create intentionally mismatched data
    ell = np.arange(30, 100, dtype=int)
    n = len(ell)
    
    # Observation in Cl units (small)
    Cl_obs = 0.1 * np.ones(n)
    sigma = 0.01 * np.ones(n)
    
    # Model in Dl units (large) - catastrophic mismatch
    Dl_model = 3000.0 * np.ones(n)
    
    # Call compute_residuals with strict=True
    try:
        residuals, metadata = cmb_comb.compute_residuals(
            ell, Cl_obs, Dl_model, sigma,
            cov=None,
            whiten_mode='diagonal',
            strict=True
        )
        
        # Should NOT reach here
        assert False, "Strict mode should have raised RuntimeError on catastrophic mismatch"
        
    except RuntimeError as e:
        error_msg = str(e)
        assert 'strict mode' in error_msg.lower(), \
            f"Error should mention strict mode, got: {error_msg}"
        print(f"✓ Strict mode correctly raised RuntimeError")
        print(f"  Error: {error_msg[:100]}...")
    
    # Test that strict=False allows continuation
    residuals, metadata = cmb_comb.compute_residuals(
        ell, Cl_obs, Dl_model, sigma,
        cov=None,
        whiten_mode='diagonal',
        strict=False
    )
    
    # Should succeed but metadata should indicate warning
    assert metadata['units_mismatch_warning'] == True, \
        "Should have units mismatch warning even in non-strict mode"
    assert metadata['sanity_checks_passed'] == False, \
        "Sanity checks should fail on catastrophic mismatch"
    assert metadata['strict_mode'] == False, \
        "Strict mode should be recorded as False"
    
    print(f"✓ Non-strict mode allowed continuation with warnings")
    print(f"  chi2/dof: {metadata['chi2_per_dof']:.2e}")
    print(f"  Sanity checks passed: {metadata['sanity_checks_passed']}")


def test_load_planck_data_with_auto_resolution():
    """
    Test load_planck_data with model file requiring auto-resolution.
    """
    print("\n=== Test: load_planck_data with Auto-Resolution ===")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create observation file in Dl format
        obs_file = tmpdir / "obs.txt"
        with open(obs_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 130):  # 100 rows
                Dl = 1000.0 + i * 10.0
                f.write(f"{i} {Dl} -50.0 50.0\n")
        
        # Create model file with Dl values but ambiguous header
        model_file = tmpdir / "model.txt"
        with open(model_file, 'w') as f:
            f.write("# ell spectrum\n")  # No Dl/Cl keyword
            for i in range(30, 130):
                Dl_model = 1010.0 + i * 10.0  # Slightly different
                f.write(f"{i} {Dl_model}\n")
        
        # Load with auto-resolution
        data = planck.load_planck_data(
            obs_file=obs_file,
            model_file=model_file,
            ell_min=30,
            ell_max=100,
            _skip_size_validation=True
        )
        
        # Verify auto-resolution metadata exists
        assert data['model_resolution_metadata'] is not None, \
            "Model resolution metadata should exist"
        
        res_meta = data['model_resolution_metadata']
        
        # Should have detected Dl (based on magnitude)
        assert res_meta['units_detected'] == "Dl", \
            f"Should detect Dl, got {res_meta['units_detected']}"
        
        # Auto-resolution may choose either Cl or Dl based on chi2
        # The important thing is that the chosen interpretation has reasonable chi2
        chi2 = res_meta['chi2_dof_chosen']
        assert chi2 < 100.0, \
            f"Chi2/dof should be reasonable, got {chi2}"
        
        # Verify both interpretations were tested
        assert 'chi2_dof_interp_cl' in res_meta, "Should have tested Cl interpretation"
        assert 'chi2_dof_interp_dl' in res_meta, "Should have tested Dl interpretation"
        
        print(f"✓ load_planck_data with auto-resolution successful")
        print(f"  Obs units: {data['obs_units']}")
        print(f"  Model units detected: {res_meta['units_detected']}")
        print(f"  Model units used: {res_meta['units_used']}")
        print(f"  Chi2/dof (chosen): {chi2:.2f}")
        print(f"  Chi2/dof (Cl): {res_meta['chi2_dof_interp_cl']:.2e}")
        print(f"  Chi2/dof (Dl): {res_meta['chi2_dof_interp_dl']:.2e}")


if __name__ == "__main__":
    print("=" * 80)
    print("Testing Planck Units Detection, Auto-Resolution, and Strict Mode")
    print("=" * 80)
    
    test_variant_keyword_detection()
    test_magnitude_heuristic_ell_cutoff()
    test_tt_full_parsing_with_sigma()
    test_auto_resolution_with_chi2()
    test_strict_mode_raises_on_mismatch()
    test_load_planck_data_with_auto_resolution()
    
    print()
    print("=" * 80)
    print("✓ ALL TESTS PASSED!")
    print("=" * 80)
