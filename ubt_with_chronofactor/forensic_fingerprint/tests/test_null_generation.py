#!/usr/bin/env python3
"""
Unit tests for null generation and calibration.

Tests:
- Diagonal Gaussian null generation
- Covariance Gaussian null generation
- Whitening calibration test
- Look-elsewhere MC correction
"""

import sys
import numpy as np
from pathlib import Path

# Add parent directories to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'cmb_comb'))

import cmb_comb


def test_generate_null_residuals_diagonal():
    """Test diagonal Gaussian null generation."""
    n = 100
    ell = np.arange(2, 2 + n)
    sigma = np.ones(n)
    
    # Set seed for reproducibility
    np.random.seed(42)
    
    # Generate multiple samples to check statistics
    n_samples = 10000
    samples = np.zeros((n_samples, n))
    
    for i in range(n_samples):
        samples[i, :] = cmb_comb.generate_null_residuals(
            ell, sigma, cov=None, null_type='diagonal_gaussian'
        )
    
    # Check mean and variance
    mean = np.mean(samples, axis=0)
    var = np.var(samples, axis=0)
    
    # Mean should be close to 0
    assert np.abs(np.mean(mean)) < 0.1, "Mean should be close to 0"
    
    # Variance should be close to 1
    assert np.abs(np.mean(var) - 1.0) < 0.1, "Variance should be close to 1"
    
    print("✓ test_generate_null_residuals_diagonal passed")


def test_generate_null_residuals_cov():
    """Test covariance Gaussian null generation and whitening."""
    n = 50
    ell = np.arange(2, 2 + n)
    sigma = np.ones(n)
    
    # Create a simple covariance matrix with correlations
    cov = np.eye(n)
    for i in range(n-1):
        cov[i, i+1] = 0.3
        cov[i+1, i] = 0.3
    
    # Set seed for reproducibility
    np.random.seed(42)
    
    # Generate samples
    n_samples = 10000
    samples = np.zeros((n_samples, n))
    
    for i in range(n_samples):
        samples[i, :] = cmb_comb.generate_null_residuals(
            ell, sigma, cov=cov, null_type='cov_gaussian'
        )
    
    # Whitened samples should have mean ~ 0 and variance ~ 1
    mean = np.mean(samples, axis=0)
    var = np.var(samples, axis=0)
    
    assert np.abs(np.mean(mean)) < 0.1, "Whitened mean should be close to 0"
    assert np.abs(np.mean(var) - 1.0) < 0.2, "Whitened variance should be close to 1"
    
    # Check correlation matrix
    corr = np.corrcoef(samples.T)
    off_diag = corr[~np.eye(n, dtype=bool)]
    
    # Off-diagonal correlations should be small
    assert np.mean(np.abs(off_diag)) < 0.1, "Off-diagonal correlations should be small"
    
    print("✓ test_generate_null_residuals_cov passed")


def test_calibrate_whitening():
    """Test whitening calibration function."""
    n = 100
    ell = np.arange(2, 2 + n)
    sigma = np.random.rand(n) + 0.5
    
    # Create covariance with sigma on diagonal
    cov = np.diag(sigma**2)
    
    # Add some correlations
    for i in range(n-1):
        cov[i, i+1] = 0.2 * sigma[i] * sigma[i+1]
        cov[i+1, i] = 0.2 * sigma[i] * sigma[i+1]
    
    # Run calibration
    diagnostics = cmb_comb.calibrate_whitening(ell, sigma, cov, n_trials=1000, random_seed=42)
    
    assert 'mean_variance' in diagnostics, "Should return mean variance"
    assert 'mean_correlation' in diagnostics, "Should return mean correlation"
    assert 'calibration_passed' in diagnostics, "Should return pass/fail status"
    
    # For a well-conditioned covariance, calibration should pass
    assert diagnostics['calibration_passed'], "Calibration should pass for good covariance"
    
    # Variance should be close to 1
    assert abs(diagnostics['mean_variance'] - 1.0) < 0.15, "Mean variance should be close to 1"
    
    # Correlations should be small
    assert diagnostics['mean_correlation'] < 0.15, "Mean correlation should be small"
    
    print("✓ test_calibrate_whitening passed")


def test_monte_carlo_null_with_cov():
    """Test Monte Carlo null distribution with covariance."""
    n = 50
    ell = np.arange(2, 2 + n)
    sigma = np.ones(n)
    
    # Create covariance
    cov = np.eye(n)
    
    # Candidate periods
    periods = [8, 16, 32, 64]
    
    # Generate null distribution
    np.random.seed(42)
    null_dist = cmb_comb.monte_carlo_null_distribution(
        ell, sigma, periods,
        n_trials=100,
        random_seed=42,
        cov=cov,
        null_type='cov_gaussian'
    )
    
    assert len(null_dist) == 100, "Should return correct number of trials"
    assert np.all(null_dist >= 0), "Delta chi2 should be non-negative"
    
    # Mean should be positive (some improvement expected by chance)
    assert np.mean(null_dist) > 0, "Mean null statistic should be positive"
    
    print("✓ test_monte_carlo_null_with_cov passed")


def test_look_elsewhere_correction():
    """Test that MC properly accounts for look-elsewhere effect."""
    n = 100
    ell = np.arange(2, 2 + n)
    sigma = np.ones(n)
    
    # Compare single period vs multiple periods
    np.random.seed(42)
    
    # Single period
    null_dist_single = cmb_comb.monte_carlo_null_distribution(
        ell, sigma, [32],
        n_trials=1000,
        random_seed=42,
        cov=None,
        null_type='diagonal_gaussian'
    )
    
    # Multiple periods (look-elsewhere)
    np.random.seed(42)
    null_dist_multi = cmb_comb.monte_carlo_null_distribution(
        ell, sigma, [8, 16, 32, 64, 128],
        n_trials=1000,
        random_seed=42,
        cov=None,
        null_type='diagonal_gaussian'
    )
    
    # Multiple periods should have higher max statistics (more chances)
    # This is the look-elsewhere effect
    assert np.mean(null_dist_multi) > np.mean(null_dist_single), \
        "Multi-period null should have higher mean (look-elsewhere effect)"
    
    assert np.percentile(null_dist_multi, 95) > np.percentile(null_dist_single, 95), \
        "Multi-period null should have higher 95th percentile"
    
    print("✓ test_look_elsewhere_correction passed")


def run_all_tests():
    """Run all tests in this module."""
    test_generate_null_residuals_diagonal()
    test_generate_null_residuals_cov()
    test_calibrate_whitening()
    test_monte_carlo_null_with_cov()
    test_look_elsewhere_correction()
    
    print("\n" + "="*60)
    print("ALL NULL GENERATION TESTS PASSED")
    print("="*60)


if __name__ == '__main__':
    run_all_tests()
