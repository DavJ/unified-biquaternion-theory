#!/usr/bin/env python3
"""
Unit Tests for synthetic/lcdm.py Module
========================================

Tests synthetic ΛCDM spectrum generation and mock observation creation.

License: MIT
Author: UBT Research Team
"""

import pytest
import numpy as np
from pathlib import Path
import tempfile
import sys

# Add modules to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'synthetic'))

from lcdm import (
    generate_lcdm_spectrum,
    generate_mock_observation
)


class TestLCDMSpectrumGeneration:
    """Test ΛCDM spectrum generation."""
    
    def test_generate_tt_spectrum(self):
        """Test generating TT spectrum."""
        ell = np.arange(30, 201)
        
        Cl_tt = generate_lcdm_spectrum(ell, channel='TT')
        
        assert len(Cl_tt) == len(ell)
        assert np.all(Cl_tt > 0)  # TT should be positive
        assert np.all(np.isfinite(Cl_tt))
    
    def test_generate_ee_spectrum(self):
        """Test generating EE spectrum."""
        ell = np.arange(30, 201)
        
        Cl_ee = generate_lcdm_spectrum(ell, channel='EE')
        
        assert len(Cl_ee) == len(ell)
        assert np.all(Cl_ee > 0)  # EE should be positive
        
        # EE should be smaller than TT at most ell
        Cl_tt = generate_lcdm_spectrum(ell, channel='TT')
        assert np.mean(Cl_ee) < np.mean(Cl_tt)
    
    def test_generate_te_spectrum(self):
        """Test generating TE spectrum."""
        ell = np.arange(30, 201)
        
        Cl_te = generate_lcdm_spectrum(ell, channel='TE')
        
        assert len(Cl_te) == len(ell)
        # TE can be positive or negative
        assert np.all(np.isfinite(Cl_te))
    
    def test_generate_bb_spectrum(self):
        """Test generating BB spectrum."""
        ell = np.arange(30, 201)
        
        Cl_bb = generate_lcdm_spectrum(ell, channel='BB')
        
        assert len(Cl_bb) == len(ell)
        # BB should be very small (near zero in ΛCDM)
        assert np.all(Cl_bb < 1.0)
    
    def test_generate_unknown_channel(self):
        """Test error for unknown channel."""
        ell = np.arange(30, 201)
        
        with pytest.raises(ValueError, match="Unknown channel"):
            generate_lcdm_spectrum(ell, channel='XY')
    
    def test_spectrum_acoustic_oscillations(self):
        """Test that TT spectrum has acoustic oscillations."""
        ell = np.arange(30, 500)
        Cl_tt = generate_lcdm_spectrum(ell, channel='TT')
        
        # Should have local maxima and minima (oscillations)
        # Find peaks and troughs
        diff = np.diff(Cl_tt)
        sign_changes = np.where(np.diff(np.sign(diff)))[0]
        
        # Should have multiple oscillations
        assert len(sign_changes) > 2
    
    def test_spectrum_damping(self):
        """Test that spectrum shows damping at high ell."""
        ell_low = np.arange(30, 200)
        ell_high = np.arange(1000, 1500)
        
        Cl_low = generate_lcdm_spectrum(ell_low, channel='TT')
        Cl_high = generate_lcdm_spectrum(ell_high, channel='TT')
        
        # High-ell should have lower amplitude due to damping
        assert np.mean(Cl_high) < np.mean(Cl_low)


class TestMockObservation:
    """Test mock observation generation."""
    
    def test_mock_diagonal_noise(self):
        """Test mock observation with diagonal noise."""
        np.random.seed(42)
        
        ell = np.arange(30, 101)
        Cl_theory = generate_lcdm_spectrum(ell, channel='TT')
        sigma = Cl_theory * 0.1  # 10% uncertainty
        
        Cl_obs = generate_mock_observation(
            ell=ell,
            Cl_theory=Cl_theory,
            noise_model={'sigma': sigma},
            seed=42
        )
        
        assert len(Cl_obs) == len(ell)
        assert np.all(np.isfinite(Cl_obs))
        
        # Observation should be close to theory (within ~few sigma)
        residuals = (Cl_obs - Cl_theory) / sigma
        assert np.abs(np.mean(residuals)) < 0.5  # Mean near zero
        assert np.abs(np.std(residuals) - 1.0) < 0.3  # Std near 1
    
    def test_mock_covariance_noise(self):
        """Test mock observation with covariance noise."""
        np.random.seed(42)
        
        n = 50
        ell = np.arange(30, 30 + n)
        Cl_theory = generate_lcdm_spectrum(ell, channel='TT')
        
        # Create simple covariance (diagonal + small off-diagonal)
        sigma = Cl_theory * 0.1
        cov = np.diag(sigma ** 2)
        for i in range(n - 1):
            cov[i, i + 1] = 0.3 * sigma[i] * sigma[i + 1]
            cov[i + 1, i] = 0.3 * sigma[i] * sigma[i + 1]
        
        Cl_obs = generate_mock_observation(
            ell=ell,
            Cl_theory=Cl_theory,
            noise_model={'sigma': sigma},
            cov=cov,
            seed=42
        )
        
        assert len(Cl_obs) == len(ell)
        assert np.all(np.isfinite(Cl_obs))
    
    def test_mock_deterministic_seed(self):
        """Test that same seed produces same result."""
        ell = np.arange(30, 101)
        Cl_theory = generate_lcdm_spectrum(ell, channel='TT')
        sigma = Cl_theory * 0.1
        
        Cl_obs1 = generate_mock_observation(
            ell, Cl_theory, {'sigma': sigma}, seed=123
        )
        
        Cl_obs2 = generate_mock_observation(
            ell, Cl_theory, {'sigma': sigma}, seed=123
        )
        
        assert np.array_equal(Cl_obs1, Cl_obs2)
    
    def test_mock_different_seeds(self):
        """Test that different seeds produce different results."""
        ell = np.arange(30, 101)
        Cl_theory = generate_lcdm_spectrum(ell, channel='TT')
        sigma = Cl_theory * 0.1
        
        Cl_obs1 = generate_mock_observation(
            ell, Cl_theory, {'sigma': sigma}, seed=123
        )
        
        Cl_obs2 = generate_mock_observation(
            ell, Cl_theory, {'sigma': sigma}, seed=456
        )
        
        # Should be different (very unlikely to be identical)
        assert not np.array_equal(Cl_obs1, Cl_obs2)
    
    def test_mock_signal_injection(self):
        """Test signal injection into mock observation."""
        np.random.seed(42)
        
        ell = np.arange(30, 201)
        Cl_theory = generate_lcdm_spectrum(ell, channel='TT')
        sigma = Cl_theory * 0.05
        
        # Inject signal with known parameters
        injection = {
            'period': 100.0,
            'amplitude': 50.0,
            'phase': 0.0
        }
        
        Cl_obs = generate_mock_observation(
            ell=ell,
            Cl_theory=Cl_theory,
            noise_model={'sigma': sigma},
            injection_signal=injection,
            seed=42
        )
        
        # Compute expected signal
        k = 2 * np.pi / injection['period']
        signal_expected = injection['amplitude'] * np.sin(k * ell + injection['phase'])
        
        # Residual should contain the injected signal (plus noise)
        residual = Cl_obs - Cl_theory
        
        # Signal should be visible (correlation with expected signal)
        correlation = np.corrcoef(residual, signal_expected)[0, 1]
        assert correlation > 0.8  # Strong correlation
    
    def test_mock_noise_sigma_array(self):
        """Test using sigma as array instead of dict."""
        ell = np.arange(30, 101)
        Cl_theory = generate_lcdm_spectrum(ell, channel='TT')
        sigma = Cl_theory * 0.1
        
        Cl_obs = generate_mock_observation(
            ell, Cl_theory, sigma, seed=42  # sigma as array
        )
        
        assert len(Cl_obs) == len(ell)
    
    def test_mock_size_mismatch_theory(self):
        """Test error when theory and ell sizes don't match."""
        ell = np.arange(30, 101)
        Cl_theory = np.ones(50)  # Wrong size
        sigma = np.ones(71)
        
        with pytest.raises(ValueError, match="doesn't match ell length"):
            generate_mock_observation(ell, Cl_theory, {'sigma': sigma})
    
    def test_mock_size_mismatch_sigma(self):
        """Test error when sigma and ell sizes don't match."""
        ell = np.arange(30, 101)
        Cl_theory = np.ones(71)
        sigma = np.ones(50)  # Wrong size
        
        with pytest.raises(ValueError, match="doesn't match ell length"):
            generate_mock_observation(ell, Cl_theory, {'sigma': sigma})
    
    def test_mock_size_mismatch_cov(self):
        """Test error when covariance size doesn't match."""
        ell = np.arange(30, 101)
        Cl_theory = np.ones(71)
        sigma = np.ones(71)
        cov = np.eye(50)  # Wrong size
        
        with pytest.raises(ValueError, match="doesn't match ell length"):
            generate_mock_observation(ell, Cl_theory, {'sigma': sigma}, cov=cov)
    
    def test_mock_injection_missing_params(self):
        """Test error when injection signal missing required params."""
        ell = np.arange(30, 101)
        Cl_theory = generate_lcdm_spectrum(ell, channel='TT')
        sigma = Cl_theory * 0.1
        
        with pytest.raises(ValueError, match="must have 'period' and 'amplitude'"):
            generate_mock_observation(
                ell, Cl_theory, {'sigma': sigma},
                injection_signal={'period': 100}  # Missing amplitude
            )


class TestIntegration:
    """Integration tests combining generation and mock observation."""
    
    def test_generate_and_observe_workflow(self):
        """Test complete workflow: generate theory → create mock obs."""
        np.random.seed(42)
        
        # Generate theory
        ell = np.arange(30, 501)
        Cl_theory = generate_lcdm_spectrum(ell, channel='TT')
        
        # Create realistic noise model
        sigma = Cl_theory * 0.05  # 5% uncertainty
        
        # Generate multiple realizations
        n_realizations = 10
        realizations = []
        
        for i in range(n_realizations):
            Cl_obs = generate_mock_observation(
                ell, Cl_theory, {'sigma': sigma}, seed=42 + i
            )
            realizations.append(Cl_obs)
        
        realizations = np.array(realizations)
        
        # Check ensemble properties
        mean_obs = np.mean(realizations, axis=0)
        std_obs = np.std(realizations, axis=0)
        
        # Mean should be close to theory
        assert np.allclose(mean_obs, Cl_theory, rtol=0.2)
        
        # Std should be close to sigma (within statistical noise)
        assert np.allclose(std_obs, sigma, rtol=0.3)
    
    def test_multichannel_generation(self):
        """Test generating multiple channels."""
        ell = np.arange(30, 201)
        
        Cl_tt = generate_lcdm_spectrum(ell, channel='TT')
        Cl_ee = generate_lcdm_spectrum(ell, channel='EE')
        Cl_te = generate_lcdm_spectrum(ell, channel='TE')
        Cl_bb = generate_lcdm_spectrum(ell, channel='BB')
        
        # All should have same length
        assert len(Cl_tt) == len(Cl_ee) == len(Cl_te) == len(Cl_bb) == len(ell)
        
        # Relative amplitudes should be reasonable
        assert np.mean(Cl_tt) > np.mean(Cl_ee)  # TT > EE
        assert np.mean(Cl_ee) > np.mean(np.abs(Cl_te))  # EE > |TE|
        assert np.mean(Cl_bb) < 1.0  # BB very small


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
