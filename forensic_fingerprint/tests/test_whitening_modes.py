#!/usr/bin/env python3
"""
Unit tests for whitening modes and covariance validation.

Tests the enhanced covariance whitening implementation including:
- Covariance matrix validation
- Ridge regularization
- New 'cov_diag' mode
- Metadata output
"""

import sys
import numpy as np
from pathlib import Path

# Add parent directories to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'cmb_comb'))

import cmb_comb


def test_validate_covariance_symmetric():
    """Test that covariance validation detects symmetry."""
    n = 10
    ell = np.arange(2, 2 + n)
    
    # Create symmetric covariance
    cov_sym = np.random.randn(n, n)
    cov_sym = 0.5 * (cov_sym + cov_sym.T)
    cov_sym += n * np.eye(n)  # Make positive definite
    
    metadata = cmb_comb.validate_covariance(cov_sym, ell)
    
    assert metadata['is_symmetric'], "Symmetric matrix should be detected as symmetric"
    assert metadata['is_positive_definite'], "PD matrix should be detected as PD"
    assert metadata['condition_number'] > 0, "Condition number should be positive"
    assert metadata['ell_range'] == (2, 11), "ell range should match input"
    
    print("✓ test_validate_covariance_symmetric passed")


def test_validate_covariance_not_positive_definite():
    """Test that covariance validation detects non-positive definiteness."""
    n = 10
    ell = np.arange(2, 2 + n)
    
    # Create non-positive definite matrix
    cov_npd = np.eye(n)
    cov_npd[0, 0] = -1.0  # Make first eigenvalue negative
    
    metadata = cmb_comb.validate_covariance(cov_npd, ell)
    
    assert not metadata['is_positive_definite'], "Non-PD matrix should be detected"
    assert metadata['needs_regularization'], "Non-PD matrix should need regularization"
    assert metadata['min_eigenvalue'] < 0, "Minimum eigenvalue should be negative"
    
    print("✓ test_validate_covariance_not_positive_definite passed")


def test_ridge_regularization():
    """Test that ridge regularization makes matrix positive definite."""
    n = 10
    
    # Create ill-conditioned matrix
    cov = np.eye(n)
    cov[0, 0] = 1e-12  # Very small eigenvalue
    
    cov_reg, lambda_ridge = cmb_comb.apply_ridge_regularization(cov)
    
    # Check that regularization was applied
    assert lambda_ridge > 0, "Ridge parameter should be positive"
    
    # Check that result is positive definite
    eigenvalues = np.linalg.eigvalsh(cov_reg)
    assert np.all(eigenvalues > 0), "Regularized matrix should be positive definite"
    
    print("✓ test_ridge_regularization passed")


def test_compute_residuals_diagonal():
    """Test diagonal whitening mode."""
    n = 50
    ell = np.arange(2, 2 + n)
    C_obs = np.random.randn(n) + 100
    C_model = np.random.randn(n) + 100
    sigma = np.ones(n) * 0.1
    
    residuals, metadata = cmb_comb.compute_residuals(
        ell, C_obs, C_model, sigma, cov=None, whiten_mode='diagonal'
    )
    
    assert len(residuals) == n, "Residuals should have same length as input"
    assert metadata['whiten_mode'] == 'diagonal', "Metadata should reflect mode"
    assert not metadata['regularization_used'], "No regularization for diagonal mode"
    
    # Check that residuals are properly normalized
    expected = (C_obs - C_model) / sigma
    np.testing.assert_allclose(residuals, expected, rtol=1e-10)
    
    print("✓ test_compute_residuals_diagonal passed")


def test_compute_residuals_cov_diag():
    """Test cov_diag whitening mode."""
    n = 50
    ell = np.arange(2, 2 + n)
    C_obs = np.random.randn(n) + 100
    C_model = np.random.randn(n) + 100
    sigma = np.ones(n) * 0.1
    
    # Create covariance with specific diagonal
    cov_diag_values = np.random.rand(n) * 0.5 + 0.5
    cov = np.diag(cov_diag_values)
    
    residuals, metadata = cmb_comb.compute_residuals(
        ell, C_obs, C_model, sigma, cov=cov, whiten_mode='cov_diag'
    )
    
    assert len(residuals) == n, "Residuals should have same length as input"
    assert metadata['whiten_mode'] == 'cov_diag', "Metadata should reflect mode"
    assert metadata['cov_metadata'] is not None, "Should have cov metadata"
    assert metadata['cov_metadata']['source'] == 'diagonal from covariance'
    
    # Check that residuals use diagonal from covariance
    expected = (C_obs - C_model) / np.sqrt(cov_diag_values)
    np.testing.assert_allclose(residuals, expected, rtol=1e-10)
    
    print("✓ test_compute_residuals_cov_diag passed")


def test_compute_residuals_covariance():
    """Test full covariance whitening mode."""
    n = 50
    ell = np.arange(2, 2 + n)
    C_obs = np.random.randn(n) + 100
    C_model = np.random.randn(n) + 100
    sigma = np.ones(n) * 0.1
    
    # Create valid covariance matrix
    A = np.random.randn(n, n)
    cov = A @ A.T + 0.1 * np.eye(n)  # Ensure positive definite
    
    residuals, metadata = cmb_comb.compute_residuals(
        ell, C_obs, C_model, sigma, cov=cov, whiten_mode='covariance'
    )
    
    assert len(residuals) == n, "Residuals should have same length as input"
    assert metadata['whiten_mode'] == 'covariance', "Metadata should reflect mode"
    assert metadata['cov_metadata'] is not None, "Should have covariance metadata"
    assert metadata['cov_metadata']['is_symmetric'], "Covariance should be symmetric"
    assert metadata['cov_metadata']['is_positive_definite'], "Covariance should be PD"
    
    # Check that Cholesky whitening was applied correctly
    L = np.linalg.cholesky(cov)
    expected = np.linalg.solve(L, C_obs - C_model)
    np.testing.assert_allclose(residuals, expected, rtol=1e-8)
    
    print("✓ test_compute_residuals_covariance passed")


def test_compute_residuals_covariance_with_regularization():
    """Test covariance whitening with ill-conditioned matrix requiring regularization."""
    n = 50
    ell = np.arange(2, 2 + n)
    C_obs = np.random.randn(n) + 100
    C_model = np.random.randn(n) + 100
    sigma = np.ones(n) * 0.1
    
    # Create ill-conditioned covariance
    A = np.random.randn(n, n)
    cov = A @ A.T
    cov += 1e-15 * np.eye(n)  # Very small diagonal - will need regularization
    
    residuals, metadata = cmb_comb.compute_residuals(
        ell, C_obs, C_model, sigma, cov=cov, whiten_mode='covariance'
    )
    
    assert len(residuals) == n, "Residuals should have same length as input"
    assert metadata['whiten_mode'] == 'covariance', "Metadata should reflect mode"
    
    # Should have applied regularization
    if metadata['cov_metadata']['needs_regularization']:
        assert metadata['regularization_used'], "Should have used regularization"
        assert metadata['lambda_ridge'] is not None, "Should have ridge parameter"
        assert metadata['lambda_ridge'] > 0, "Ridge parameter should be positive"
    
    print("✓ test_compute_residuals_covariance_with_regularization passed")


def test_compute_residuals_none():
    """Test 'none' whitening mode (no normalization)."""
    n = 50
    ell = np.arange(2, 2 + n)
    C_obs = np.random.randn(n) + 100
    C_model = np.random.randn(n) + 100
    sigma = np.ones(n) * 0.1
    
    residuals, metadata = cmb_comb.compute_residuals(
        ell, C_obs, C_model, sigma, cov=None, whiten_mode='none'
    )
    
    assert len(residuals) == n, "Residuals should have same length as input"
    assert metadata['whiten_mode'] == 'none', "Metadata should reflect mode"
    
    # Check that no normalization was applied
    expected = C_obs - C_model
    np.testing.assert_allclose(residuals, expected, rtol=1e-10)
    
    print("✓ test_compute_residuals_none passed")


def run_all_tests():
    """Run all tests."""
    print("Running whitening mode tests...\n")
    
    test_validate_covariance_symmetric()
    test_validate_covariance_not_positive_definite()
    test_ridge_regularization()
    test_compute_residuals_diagonal()
    test_compute_residuals_cov_diag()
    test_compute_residuals_covariance()
    test_compute_residuals_covariance_with_regularization()
    test_compute_residuals_none()
    
    print("\n✓ All tests passed!")


if __name__ == '__main__':
    run_all_tests()
