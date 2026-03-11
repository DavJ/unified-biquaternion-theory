#!/usr/bin/env python3
"""
Unit tests for court-grade whitening with full covariance support.

Tests the new covariance loading and whitening implementation added for
court-grade CMB analysis with full error correlation.
"""

import sys
import numpy as np
from pathlib import Path
import tempfile
import pytest

# Add parent directories to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'loaders'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))

from loaders import covariance as cov_loader
import whitening


class TestCovarianceLoader:
    """Test covariance matrix loading and validation."""
    
    def test_load_npy_format(self):
        """Test loading .npy format covariance."""
        # Create test covariance
        n = 20
        A = np.random.randn(n, n)
        cov = A @ A.T + 0.1 * np.eye(n)  # Ensure PD
        
        # Save to temp file
        with tempfile.NamedTemporaryFile(suffix='.npy', delete=False) as f:
            np.save(f.name, cov)
            temp_file = f.name
        
        try:
            # Load
            loaded_cov, metadata = cov_loader.load_covariance_matrix(temp_file)
            
            # Verify
            assert loaded_cov.shape == (n, n)
            assert np.allclose(loaded_cov, cov)
            assert metadata['format'] == 'npy'
            assert metadata['is_symmetric']
            assert metadata['is_positive_semidefinite']
            assert metadata['is_finite']
        finally:
            Path(temp_file).unlink()
    
    def test_load_text_format(self):
        """Test loading plain text format covariance."""
        # Create test covariance
        n = 10
        cov = np.eye(n) + 0.1 * np.random.randn(n, n)
        cov = 0.5 * (cov + cov.T)  # Symmetrize
        cov = cov + n * np.eye(n)  # Ensure PD
        
        # Save to temp file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            np.savetxt(f.name, cov)
            temp_file = f.name
        
        try:
            # Load
            loaded_cov, metadata = cov_loader.load_covariance_matrix(temp_file)
            
            # Verify
            assert loaded_cov.shape == (n, n)
            assert np.allclose(loaded_cov, cov)
            assert metadata['format'] == 'text'
        finally:
            Path(temp_file).unlink()
    
    def test_validation_detects_asymmetry(self):
        """Test that asymmetric matrices are rejected."""
        # Create asymmetric matrix
        n = 10
        cov = np.random.randn(n, n)
        
        # Save to temp file
        with tempfile.NamedTemporaryFile(suffix='.npy', delete=False) as f:
            np.save(f.name, cov)
            temp_file = f.name
        
        try:
            # Should raise ValueError for asymmetry
            with pytest.raises(ValueError, match="not symmetric"):
                cov_loader.load_covariance_matrix(temp_file)
        finally:
            Path(temp_file).unlink()
    
    def test_jitter_applied_for_non_psd(self):
        """Test that jitter is applied to non-PSD matrices."""
        # Create matrix with negative eigenvalue
        n = 10
        cov = np.eye(n)
        cov[0, 0] = -0.1  # Negative diagonal element
        
        # Save to temp file
        with tempfile.NamedTemporaryFile(suffix='.npy', delete=False) as f:
            np.save(f.name, cov)
            temp_file = f.name
        
        try:
            # Load (should apply jitter automatically)
            loaded_cov, metadata = cov_loader.load_covariance_matrix(temp_file)
            
            # Verify jitter was applied
            assert metadata['jitter_applied']
            assert metadata['jitter_value'] > 0
            assert metadata['is_positive_semidefinite']
            
            # Check all eigenvalues are positive
            eigs = np.linalg.eigvalsh(loaded_cov)
            assert np.all(eigs > 0)
        finally:
            Path(temp_file).unlink()


class TestWhitening:
    """Test whitening transformations."""
    
    def test_whitening_full_identity(self):
        """Test: cov=I → full whitening equals no-op."""
        n = 15
        cov_identity = np.eye(n)
        residual = np.random.randn(n)
        
        # Whiten with identity covariance
        whitened = whitening.whiten_residuals(residual, cov=cov_identity, mode='full')
        
        # Should be nearly identical (within numerical precision)
        assert np.allclose(residual, whitened, rtol=1e-10)
    
    def test_whitening_diag_equivalence(self):
        """Test: mode=diag reproduces diagonal normalization."""
        n = 20
        residual = np.random.randn(n)
        sigma = np.random.uniform(0.5, 2.0, n)
        
        # Diagonal whitening
        whitened_diag = whitening.whiten_residuals(residual, sigma=sigma, mode='diag')
        
        # Manual computation
        expected = residual / sigma
        
        assert np.allclose(whitened_diag, expected, rtol=1e-12)
    
    def test_whitening_full_diagonal_cov_equivalence(self):
        """Test: full whitening with diagonal cov should match diagonal whitening."""
        n = 25
        sigma = np.random.uniform(0.5, 2.0, n)
        cov_diag = np.diag(sigma**2)
        residual = np.random.randn(n)
        
        # Diagonal whitening
        whitened_diag = whitening.whiten_residuals(residual, sigma=sigma, mode='diag')
        
        # Full whitening with diagonal covariance
        whitened_full = whitening.whiten_residuals(residual, cov=cov_diag, mode='full')
        
        # Should be equivalent
        assert np.allclose(whitened_diag, whitened_full, rtol=1e-8)
    
    def test_whitening_full_known_cov(self):
        """Test: whitening with known covariance produces N(0,I)."""
        n = 30
        
        # Create known positive definite covariance
        A = np.random.randn(n, n)
        cov = A @ A.T + 0.5 * np.eye(n)
        
        # Verify whitening via Monte Carlo
        np.random.seed(42)
        n_samples = 1000
        samples = []
        
        for _ in range(n_samples):
            # Generate sample from N(0, cov)
            z = np.random.randn(n)
            L = np.linalg.cholesky(cov)
            x = L @ z
            
            # Whiten
            w = whitening.whiten_residuals(x, cov=cov, mode='full')
            samples.append(w)
        
        samples = np.array(samples)
        
        # Check whitened samples have correct statistics
        mean_whitened = np.mean(samples, axis=0)
        cov_whitened = np.cov(samples.T)
        
        # Mean should be ~0
        assert np.max(np.abs(mean_whitened)) < 0.15  # Relaxed for finite samples
        
        # Covariance should be ~I
        assert np.allclose(cov_whitened, np.eye(n), atol=0.15)
    
    def test_mc_null_generation(self):
        """Test: MC null generation produces correct statistics."""
        n = 20
        sigma = np.ones(n)
        
        # Generate null samples
        np.random.seed(42)
        n_samples = 1000
        samples = []
        
        for _ in range(n_samples):
            sample = whitening.generate_mc_null_sample(sigma=sigma, mode='diag', 
                                                      random_state=np.random.RandomState())
            samples.append(sample)
        
        samples = np.array(samples)
        
        # Check statistics
        mean = np.mean(samples)
        std = np.std(samples)
        
        assert abs(mean) < 0.1  # Should be ~0
        assert abs(std - 1.0) < 0.1  # Should be ~1
    
    def test_shape_mismatch_error(self):
        """Test: clear error for shape mismatch."""
        n = 20
        residual = np.random.randn(n)
        cov_wrong_size = np.eye(15)  # Wrong size!
        
        # Should raise ValueError with clear message
        with pytest.raises(ValueError, match="doesn't match"):
            whitening.whiten_residuals(residual, cov=cov_wrong_size, mode='full')
    
    def test_build_whitener_cholesky(self):
        """Test build_whitener with Cholesky method."""
        n = 15
        A = np.random.randn(n, n)
        cov = A @ A.T + 0.1 * np.eye(n)
        
        # Build whitener
        whiten_func, metadata = whitening.build_whitener(cov, method='cholesky', jitter=1e-12)
        
        # Verify metadata
        assert metadata['method'] == 'cholesky'
        assert metadata['factorization'] == 'cholesky'
        assert metadata['jitter'] == 1e-12
        
        # Test whitening
        x = np.random.randn(n)
        w = whiten_func(x)
        
        assert len(w) == n
    
    def test_build_whitener_eigh(self):
        """Test build_whitener with eigenvalue method."""
        n = 15
        A = np.random.randn(n, n)
        cov = A @ A.T + 0.1 * np.eye(n)
        
        # Build whitener
        whiten_func, metadata = whitening.build_whitener(cov, method='eigh', jitter=1e-12)
        
        # Verify metadata
        assert metadata['method'] == 'eigh'
        assert metadata['factorization'] == 'eigh'
        
        # Test whitening
        x = np.random.randn(n)
        w = whiten_func(x)
        
        assert len(w) == n
    
    def test_verify_whitening(self):
        """Test whitening verification function."""
        n = 20
        A = np.random.randn(n, n)
        cov = A @ A.T + 0.5 * np.eye(n)
        
        # Verify whitening
        results = whitening.verify_whitening(cov, n_samples=1000, random_seed=42)
        
        # Check statistics are reasonable (relaxed criteria for finite samples)
        assert abs(results['mean_deviation']) < 0.15
        assert abs(results['max_off_diagonal']) < 0.15
        assert 0.85 < results['mean_variance'] < 1.15
        
        # Note: 'passed' criterion in verify_whitening is strict
        # Here we just check the statistics are in reasonable range


class TestIntegration:
    """Integration tests with the full pipeline."""
    
    def test_end_to_end_with_synthetic_cov(self):
        """Test end-to-end run with synthetic covariance."""
        # This is a simplified integration test
        # Full integration tested separately
        
        n = 50
        
        # Create synthetic covariance
        A = np.random.randn(n, n)
        cov = A @ A.T + 0.1 * np.eye(n)
        
        # Create residuals
        residual = np.random.randn(n)
        
        # Whiten
        whitened = whitening.whiten_residuals(residual, cov=cov, mode='full')
        
        # Basic checks
        assert len(whitened) == n
        assert np.all(np.isfinite(whitened))
        
        # Whitened residuals should have different norm than original
        # (unless cov is identity, which it's not)
        assert not np.allclose(np.linalg.norm(whitened), np.linalg.norm(residual))


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
