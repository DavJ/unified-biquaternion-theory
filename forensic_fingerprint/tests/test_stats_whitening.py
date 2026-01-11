#!/usr/bin/env python3
"""
Unit Tests for stats/whitening.py Module
=========================================

Tests whitening functions for numerical correctness and stability.

License: MIT
Author: UBT Research Team
"""

import pytest
import numpy as np
from pathlib import Path
import tempfile


# Add modules to path
import sys
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'stats'))

from whitening import (
    load_covariance,
    align_cov_to_ell,
    cholesky_whitener,
    whiten_residuals,
    validate_and_regularize_covariance
)


class TestCovarianceLoading:
    """Test covariance matrix loading from files."""
    
    def test_load_npy(self):
        """Test loading .npy covariance file."""
        # Create temporary covariance matrix
        C = np.eye(10) * 2.0  # Diagonal covariance
        
        with tempfile.NamedTemporaryFile(suffix='.npy', delete=False) as f:
            np.save(f, C)
            temp_path = Path(f.name)
        
        try:
            ell, C_loaded = load_covariance(temp_path)
            assert C_loaded.shape == (10, 10)
            assert np.allclose(C_loaded, C)
            assert ell is None  # .npy doesn't store ell metadata
        finally:
            temp_path.unlink()
    
    def test_load_txt(self):
        """Test loading .txt covariance file."""
        C = np.eye(5) * 3.0
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            np.savetxt(f, C)
            temp_path = Path(f.name)
        
        try:
            ell, C_loaded = load_covariance(temp_path)
            assert C_loaded.shape == (5, 5)
            assert np.allclose(C_loaded, C)
        finally:
            temp_path.unlink()
    
    def test_load_nonexistent_file(self):
        """Test error handling for missing file."""
        with pytest.raises(FileNotFoundError):
            load_covariance("nonexistent_file.npy")
    
    def test_load_unsupported_format(self):
        """Test error for unsupported file format."""
        with tempfile.NamedTemporaryFile(suffix='.fits', delete=False) as f:
            temp_path = Path(f.name)
        
        try:
            with pytest.raises(ValueError, match="Unsupported covariance file format"):
                load_covariance(temp_path)
        finally:
            temp_path.unlink()


class TestCovarianceAlignment:
    """Test alignment of covariance to target ell range."""
    
    def test_align_subset(self):
        """Test extracting subset of covariance."""
        # 10x10 covariance for ell = 10, 20, 30, ..., 100
        C_full = np.eye(10) * 2.0
        ell_cov = np.arange(10, 101, 10)
        
        # Extract subset for ell = 30, 40, 50
        ell_target = np.array([30, 40, 50])
        
        C_aligned = align_cov_to_ell(C_full, ell_cov, ell_target)
        
        assert C_aligned.shape == (3, 3)
        assert np.allclose(C_aligned, np.eye(3) * 2.0)
    
    def test_align_no_ell_metadata(self):
        """Test alignment when ell_cov is None (size check only)."""
        C = np.eye(5)
        ell_target = np.arange(5)
        
        C_aligned = align_cov_to_ell(C, None, ell_target)
        assert np.array_equal(C_aligned, C)
    
    def test_align_size_mismatch(self):
        """Test error when sizes don't match and no ell metadata."""
        C = np.eye(5)
        ell_target = np.arange(10)
        
        with pytest.raises(ValueError, match="doesn't match target ell count"):
            align_cov_to_ell(C, None, ell_target)
    
    def test_align_missing_ell(self):
        """Test error when target ell not in covariance."""
        C = np.eye(5)
        ell_cov = np.array([10, 20, 30, 40, 50])
        ell_target = np.array([15, 25])  # Not in ell_cov
        
        with pytest.raises(ValueError, match="not found in covariance"):
            align_cov_to_ell(C, ell_cov, ell_target)


class TestCovarianceValidation:
    """Test covariance validation and regularization."""
    
    def test_validate_symmetric_positive_definite(self):
        """Test validation of good covariance."""
        C = np.diag([1.0, 2.0, 3.0, 4.0, 5.0])
        ell = np.arange(5)
        
        C_val, metadata = validate_and_regularize_covariance(C, ell)
        
        assert metadata['is_symmetric'] is True
        assert metadata['is_positive_definite'] is True
        assert metadata['needs_regularization'] is False
        assert metadata['regularization_applied'] is False
        assert np.allclose(C_val, C)
    
    def test_validate_auto_symmetrize(self):
        """Test auto-symmetrization of slightly asymmetric matrix."""
        C = np.eye(5)
        C[0, 1] = 0.1
        C[1, 0] = 0.1 + 1e-8  # Tiny asymmetry
        
        C_val, metadata = validate_and_regularize_covariance(C, auto_symmetrize=True)
        
        assert metadata['was_symmetrized'] is True
        assert np.allclose(C_val, C_val.T)
    
    def test_validate_ill_conditioned(self):
        """Test regularization of ill-conditioned matrix."""
        # Create ill-conditioned covariance
        eigenvalues = np.array([1.0, 0.5, 0.1, 1e-6, 1e-12])
        Q = np.linalg.qr(np.random.randn(5, 5))[0]  # Random orthogonal matrix
        C = Q @ np.diag(eigenvalues) @ Q.T
        
        C_val, metadata = validate_and_regularize_covariance(C, target_condition=1e8)
        
        assert metadata['needs_regularization'] is True
        assert metadata['regularization_applied'] is True
        assert metadata['lambda_ridge'] is not None
        assert metadata['final_condition_number'] < metadata['condition_number']
    
    def test_validate_not_positive_definite(self):
        """Test regularization of non-positive-definite matrix."""
        # Create matrix with negative eigenvalue
        C = np.diag([2.0, 1.0, 0.5, -0.1])
        
        C_val, metadata = validate_and_regularize_covariance(C)
        
        assert metadata['is_positive_definite'] is False
        assert metadata['regularization_applied'] is True
        
        # After regularization, should be positive definite
        eigs = np.linalg.eigvalsh(C_val)
        assert np.all(eigs > 0)
    
    def test_validate_asymmetric_error(self):
        """Test error for significantly asymmetric matrix."""
        C = np.eye(5)
        C[0, 1] = 1.0
        C[1, 0] = 0.0  # Significantly asymmetric
        
        with pytest.raises(ValueError, match="significantly asymmetric"):
            validate_and_regularize_covariance(C, auto_symmetrize=True)


class TestCholeskyWhitening:
    """Test Cholesky whitening transformation."""
    
    def test_cholesky_diagonal(self):
        """Test Cholesky decomposition of diagonal matrix."""
        C = np.diag([1.0, 4.0, 9.0, 16.0])
        L = cholesky_whitener(C)
        
        # L @ L.T should equal C
        assert np.allclose(L @ L.T, C)
        
        # L should be lower triangular
        assert np.allclose(L, np.tril(L))
    
    def test_cholesky_full(self):
        """Test Cholesky decomposition of full covariance."""
        # Create random positive definite matrix
        A = np.random.randn(5, 5)
        C = A @ A.T + np.eye(5) * 0.1  # Ensure positive definite
        
        L = cholesky_whitener(C)
        
        assert np.allclose(L @ L.T, C, atol=1e-10)
    
    def test_cholesky_not_positive_definite(self):
        """Test error for non-positive-definite matrix."""
        C = np.diag([1.0, 2.0, -0.5])  # Negative eigenvalue
        
        with pytest.raises(np.linalg.LinAlgError):
            cholesky_whitener(C)
    
    def test_whiten_residuals_diagonal(self):
        """Test whitening with diagonal covariance."""
        C = np.diag([1.0, 4.0, 9.0])
        r = np.array([1.0, 2.0, 3.0])
        
        r_w = whiten_residuals(r, C)
        
        # Expected: [1.0/1.0, 2.0/2.0, 3.0/3.0] = [1.0, 1.0, 1.0]
        assert np.allclose(r_w, [1.0, 1.0, 1.0])
    
    def test_whiten_residuals_full(self):
        """Test whitening with full covariance."""
        # Create known covariance
        C = np.array([
            [2.0, 0.5, 0.0],
            [0.5, 3.0, 0.5],
            [0.0, 0.5, 1.0]
        ])
        
        r = np.array([1.0, 2.0, 1.5])
        r_w = whiten_residuals(r, C)
        
        # Check that chi-squared = r^T C^{-1} r = ||r_w||^2
        chi2_direct = r @ np.linalg.solve(C, r)
        chi2_whitened = np.dot(r_w, r_w)
        
        assert np.allclose(chi2_direct, chi2_whitened)
    
    def test_whiten_produces_unit_variance(self):
        """Test that whitening produces unit variance for Gaussian samples."""
        # Create covariance
        C = np.array([
            [1.0, 0.7, 0.3],
            [0.7, 2.0, 0.5],
            [0.3, 0.5, 1.5]
        ])
        
        # Generate many samples from N(0, C)
        np.random.seed(42)
        n_samples = 10000
        samples = np.random.multivariate_normal(np.zeros(3), C, size=n_samples)
        
        # Whiten each sample
        samples_w = np.array([whiten_residuals(s, C) for s in samples])
        
        # Whitened samples should have approximately unit variance
        cov_w = np.cov(samples_w.T)
        
        assert np.allclose(cov_w, np.eye(3), atol=0.1)  # Within statistical noise
    
    def test_whiten_size_mismatch(self):
        """Test error when residual and covariance sizes don't match."""
        C = np.eye(5)
        r = np.array([1.0, 2.0, 3.0])  # Wrong size
        
        with pytest.raises(ValueError, match="doesn't match covariance size"):
            whiten_residuals(r, C)


class TestIntegration:
    """Integration tests combining multiple functions."""
    
    def test_full_pipeline(self):
        """Test full pipeline: load → validate → whiten."""
        # Create test covariance
        np.random.seed(42)
        A = np.random.randn(10, 10)
        C_true = A @ A.T + np.eye(10) * 0.5
        
        # Save to file
        with tempfile.NamedTemporaryFile(suffix='.npy', delete=False) as f:
            np.save(f, C_true)
            temp_path = Path(f.name)
        
        try:
            # Load
            ell_cov, C = load_covariance(temp_path)
            
            # Validate
            C_val, metadata = validate_and_regularize_covariance(C)
            assert metadata['is_symmetric']
            assert metadata['is_positive_definite']
            
            # Whiten random residual
            r = np.random.randn(10)
            r_w = whiten_residuals(r, C_val)
            
            # Check chi-squared consistency
            chi2_direct = r @ np.linalg.solve(C_val, r)
            chi2_whitened = np.dot(r_w, r_w)
            assert np.allclose(chi2_direct, chi2_whitened)
            
        finally:
            temp_path.unlink()


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
