#!/usr/bin/env python3
"""
Unit tests for units detection and conversion in Planck loader.

Tests the enhanced units handling including:
- Detection of Dl vs Cl format
- Automatic conversion from Dl to Cl
- Symmetric sigma calculation from asymmetric error bars
- Units metadata in results
- Sanity checks for catastrophic units mismatch
"""

import sys
import numpy as np
import tempfile
from pathlib import Path
import pytest

# Add parent directories to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'loaders'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'cmb_comb'))

import planck
import cmb_comb


def test_load_planck_tt_full_format_dl_units():
    """Test loading Planck TT-full format file with Dl units."""
    # Create synthetic TT-full format data (Dl units)
    ell = np.arange(30, 50)
    # Dl values ~ 1000-5000 μK² (typical for CMB at these multipoles)
    dl = 1000.0 + 100.0 * np.sin(ell / 10.0)
    # Asymmetric errors
    minus_ddl = -10.0 * np.ones_like(ell)
    plus_ddl = 12.0 * np.ones_like(ell)
    
    # Write to temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("# l Dl -dDl +dDl\n")
        for i in range(len(ell)):
            f.write(f"{ell[i]} {dl[i]} {minus_ddl[i]} {plus_ddl[i]}\n")
        temp_file = f.name
    
    try:
        # Load data
        ell_loaded, cl_loaded, sigma_loaded, units = planck._load_planck_tt_full_format(Path(temp_file))
        
        # Check ell matches
        np.testing.assert_array_equal(ell_loaded, ell, "ell should match")
        
        # Check units detected as Dl
        assert units == "Dl", "TT-full format should be detected as Dl"
        
        # Check Dl was converted to Cl: Cl = Dl * 2π / [l(l+1)]
        expected_cl = dl * (2.0 * np.pi) / (ell * (ell + 1.0))
        np.testing.assert_allclose(cl_loaded, expected_cl, rtol=1e-10, 
                                   err_msg="Dl should be converted to Cl")
        
        # Check symmetric sigma calculation: sigma = 0.5 * (|+dDl| + |-dDl|)
        expected_sigma_dl = 0.5 * (np.abs(plus_ddl) + np.abs(minus_ddl))
        expected_sigma = expected_sigma_dl * (2.0 * np.pi) / (ell * (ell + 1.0))
        np.testing.assert_allclose(sigma_loaded, expected_sigma, rtol=1e-10,
                                   err_msg="Sigma should be symmetric average")
        
        # Verify sigma is average, not max
        max_sigma_dl = np.maximum(np.abs(plus_ddl), np.abs(minus_ddl))
        max_sigma_cl = max_sigma_dl * (2.0 * np.pi) / (ell * (ell + 1.0))
        assert not np.allclose(sigma_loaded, max_sigma_cl, rtol=1e-10), \
            "Sigma should NOT be the maximum (old behavior)"
        
        print("✓ test_load_planck_tt_full_format_dl_units passed")
        
    finally:
        # Clean up
        Path(temp_file).unlink()


def test_load_planck_text_cl_units():
    """Test loading simple text file with Cl units (small values)."""
    # Create synthetic data in Cl units (small values ~ 10-1000)
    ell = np.arange(30, 50)
    cl = 500.0 + 50.0 * np.sin(ell / 10.0)  # Typical Cl values
    sigma = 5.0 * np.ones_like(ell)
    
    # Write to temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("# ell Cl sigma\n")
        for i in range(len(ell)):
            f.write(f"{ell[i]} {cl[i]} {sigma[i]}\n")
        temp_file = f.name
    
    try:
        # Load data (skip size validation for small test file)
        ell_loaded, cl_loaded, sigma_loaded, units = planck._load_planck_text(
            Path(temp_file), _skip_size_validation=True
        )
        
        # Check units detected as Cl
        assert units == "Cl", "Small values should be detected as Cl format"
        
        # Check no conversion occurred (values should match)
        np.testing.assert_array_equal(ell_loaded, ell)
        np.testing.assert_allclose(cl_loaded, cl, rtol=1e-10,
                                   err_msg="Cl values should not be converted")
        np.testing.assert_allclose(sigma_loaded, sigma, rtol=1e-10)
        
        print("✓ test_load_planck_text_cl_units passed")
        
    finally:
        Path(temp_file).unlink()


def test_load_planck_text_dl_units():
    """Test loading simple text file with Dl units (large values)."""
    # Create synthetic data in Dl units (large values ~ 1000-5000)
    ell = np.arange(30, 50)
    dl = 1500.0 + 200.0 * np.sin(ell / 10.0)  # Typical Dl values
    sigma_dl = 15.0 * np.ones_like(ell)
    
    # Write to temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("# ell Dl sigma_Dl\n")
        for i in range(len(ell)):
            f.write(f"{ell[i]} {dl[i]} {sigma_dl[i]}\n")
        temp_file = f.name
    
    try:
        # Load data
        ell_loaded, cl_loaded, sigma_loaded, units = planck._load_planck_text(
            Path(temp_file), _skip_size_validation=True
        )
        
        # Check units detected as Dl
        assert units == "Dl", "Large values should be detected as Dl format"
        
        # Check Dl was converted to Cl
        expected_cl = dl * (2.0 * np.pi) / (ell * (ell + 1.0))
        expected_sigma = sigma_dl * (2.0 * np.pi) / (ell * (ell + 1.0))
        
        np.testing.assert_allclose(cl_loaded, expected_cl, rtol=1e-10,
                                   err_msg="Dl should be converted to Cl")
        np.testing.assert_allclose(sigma_loaded, expected_sigma, rtol=1e-10,
                                   err_msg="Sigma_Dl should be converted to Sigma_Cl")
        
        print("✓ test_load_planck_text_dl_units passed")
        
    finally:
        Path(temp_file).unlink()


def test_units_metadata_in_load_planck_data():
    """Test that load_planck_data returns units metadata."""
    # Create obs file (Dl format)
    ell = np.arange(30, 50)
    dl_obs = 1500.0 + 200.0 * np.sin(ell / 10.0)
    sigma_dl = 15.0 * np.ones_like(ell)
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("# l Dl -dDl +dDl\n")
        for i in range(len(ell)):
            f.write(f"{ell[i]} {dl_obs[i]} -15.0 15.0\n")
        obs_file = f.name
    
    # Create model file (Cl format) - include dummy sigma to avoid warning
    cl_model = 500.0 + 50.0 * np.sin(ell / 10.0)
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("# ell Cl sigma\n")
        for i in range(len(ell)):
            f.write(f"{ell[i]} {cl_model[i]} 5.0\n")  # Add dummy sigma column
        model_file = f.name
    
    try:
        # Load data
        data = planck.load_planck_data(
            obs_file=obs_file,
            model_file=model_file,
            _skip_size_validation=True
        )
        
        # Check units metadata exists
        assert 'obs_units' in data, "obs_units should be in data dict"
        assert 'model_units_original' in data, "model_units_original should be in data dict"
        assert 'model_units_used' in data, "model_units_used should be in data dict"
        assert 'sigma_method' in data, "sigma_method should be in data dict"
        
        # Check units values
        assert data['obs_units'] == 'Dl', "Observation should be detected as Dl"
        assert data['model_units_original'] == 'Cl', "Model should be detected as Cl"
        assert data['model_units_used'] == 'Cl', "Final units should be Cl"
        
        # Both should be converted to Cl
        # obs: Dl -> Cl conversion should have happened
        # model: already Cl, no conversion
        
        print("✓ test_units_metadata_in_load_planck_data passed")
        
    finally:
        Path(obs_file).unlink()
        Path(model_file).unlink()


def test_catastrophic_units_mismatch_triggers():
    """Test that catastrophic units mismatch triggers RuntimeError."""
    n = 50
    ell = np.arange(30, 30 + n)
    
    # Create residuals that would result from units mismatch
    # Simulate: obs in Dl (~ 1000s), model in Cl (~ 100s), sigma ~ 10
    # Without conversion, diff would be ~ 900, sigma ~ 10
    # This gives chi2/dof ~ (900/10)^2 ~ 8100, not quite catastrophic
    # For catastrophic, we need even worse mismatch
    
    # Simulate: obs = 10000 (Dl), model = 100 (Cl, incorrectly not converted)
    C_obs = 10000.0 * np.ones(n)
    C_model = 100.0 * np.ones(n)
    sigma = 10.0 * np.ones(n)
    
    # This should trigger catastrophic check
    # chi2/dof = sum((10000-100)^2 / 10^2) / n = sum(9900^2 / 100) / n
    #          = 9900^2 / 100 = 980100 >> 1e6? No, it's close but not quite
    # Let's make it worse
    C_obs = 100000.0 * np.ones(n)
    C_model = 100.0 * np.ones(n)
    sigma = 1.0 * np.ones(n)
    # chi2/dof = (99900/1)^2 ~ 1e10 >> 1e6 ✓
    
    # Should raise RuntimeError
    with pytest.raises(RuntimeError, match="Units mismatch sanity check failed"):
        residuals, metadata = cmb_comb.compute_residuals(
            ell, C_obs, C_model, sigma, cov=None, whiten_mode='diagonal'
        )
    
    print("✓ test_catastrophic_units_mismatch_triggers passed")


def test_non_catastrophic_units_warning_no_error():
    """Test that non-catastrophic mismatch warns but doesn't error."""
    n = 50
    ell = np.arange(30, 30 + n)
    
    # Create moderate mismatch (chi2/dof ~ 1000, below catastrophic threshold)
    C_obs = 1000.0 * np.ones(n)
    C_model = 100.0 * np.ones(n)
    sigma = 30.0 * np.ones(n)
    # chi2/dof = (900/30)^2 = 900 > 100 (warning) but < 1e6 (catastrophic)
    
    # Should NOT raise error, but will print warning
    residuals, metadata = cmb_comb.compute_residuals(
        ell, C_obs, C_model, sigma, cov=None, whiten_mode='diagonal'
    )
    
    # Check metadata
    assert metadata['units_mismatch_warning'] == True, "Should flag units warning"
    assert metadata['sanity_checks_passed'] == True, "Should pass sanity checks (not catastrophic)"
    assert metadata['chi2_per_dof'] > 100.0, "chi2/dof should be elevated"
    assert metadata['chi2_per_dof'] < 1e6, "chi2/dof should be below catastrophic threshold"
    
    print("✓ test_non_catastrophic_units_warning_no_error passed")


def test_normal_residuals_no_warning():
    """Test that normal residuals don't trigger warnings."""
    n = 50
    ell = np.arange(30, 30 + n)
    
    # Create normal residuals (chi2/dof ~ 1)
    C_obs = 1000.0 + 10.0 * np.random.randn(n)
    C_model = 1000.0 * np.ones(n)
    sigma = 10.0 * np.ones(n)
    
    residuals, metadata = cmb_comb.compute_residuals(
        ell, C_obs, C_model, sigma, cov=None, whiten_mode='diagonal'
    )
    
    # Check metadata
    assert metadata['units_mismatch_warning'] == False, "Should not flag warning"
    assert metadata['sanity_checks_passed'] == True, "Should pass sanity checks"
    assert 0.1 < metadata['chi2_per_dof'] < 10.0, "chi2/dof should be reasonable"
    
    print("✓ test_normal_residuals_no_warning passed")


def test_detect_units_from_header_or_magnitude():
    """Test the units detection helper function."""
    # Test 1: Header-based detection for Dl
    header_lines_dl = ["# l Dl -dDl +dDl", "# Multipole Power Spectrum"]
    ell = np.arange(30, 50)
    values = 1500.0 + 200.0 * np.sin(ell / 10.0)  # Large values
    
    units = planck.detect_units_from_header_or_magnitude(header_lines_dl, ell, values)
    assert units == "Dl", "Should detect Dl from header"
    
    # Test 2: Header-based detection for Cl
    header_lines_cl = ["# ell Cl sigma", "# Multipole Power Spectrum"]
    values_small = 500.0 + 50.0 * np.sin(ell / 10.0)  # Small values
    
    units = planck.detect_units_from_header_or_magnitude(header_lines_cl, ell, values_small)
    assert units == "Cl", "Should detect Cl from header"
    
    # Test 3: Magnitude-based detection for Dl (no explicit header)
    header_lines_generic = ["# Multipole Power Spectrum"]
    
    units = planck.detect_units_from_header_or_magnitude(header_lines_generic, ell, values)
    assert units == "Dl", "Should detect Dl from large magnitude"
    
    # Test 4: Magnitude-based detection for Cl (no explicit header)
    units = planck.detect_units_from_header_or_magnitude(header_lines_generic, ell, values_small)
    assert units == "Cl", "Should detect Cl from small magnitude"
    
    # Test 5: Edge case - header with "dDl" (error column) should not confuse detector
    header_lines_error = ["# l Dl -dDl +dDl"]
    units = planck.detect_units_from_header_or_magnitude(header_lines_error, ell, values)
    assert units == "Dl", "Should detect Dl even with dDl error columns"
    
    print("✓ test_detect_units_from_header_or_magnitude passed")


if __name__ == '__main__':
    # Run tests
    test_load_planck_tt_full_format_dl_units()
    test_load_planck_text_cl_units()
    test_load_planck_text_dl_units()
    test_units_metadata_in_load_planck_data()
    test_catastrophic_units_mismatch_triggers()
    test_non_catastrophic_units_warning_no_error()
    test_normal_residuals_no_warning()
    test_detect_units_from_header_or_magnitude()
    
    print("\n" + "="*60)
    print("All units handling tests passed!")
    print("="*60)
