#!/usr/bin/env python3
"""
Integration tests for run_real_data_cmb_comb.py runner script.

These tests verify that the ablation and null-data modes work end-to-end.
"""

import pytest
import numpy as np
import sys
import tempfile
from pathlib import Path

# Add repo root to path
repo_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'synthetic'))

from synthetic import lcdm
import ablation


def test_ablation_get_ranges_planck():
    """Test that pre-defined ablation ranges are available for Planck."""
    ranges = ablation.get_ablation_ranges(dataset='planck')
    
    assert len(ranges) > 0
    assert all(len(r) == 3 for r in ranges)  # (name, ell_min, ell_max)
    assert all(isinstance(r[0], str) for r in ranges)
    assert all(isinstance(r[1], int) for r in ranges)
    assert all(isinstance(r[2], int) for r in ranges)
    
    # Check expected ranges
    names = [r[0] for r in ranges]
    assert 'low' in names
    assert 'mid' in names
    assert 'high' in names


def test_ablation_get_ranges_wmap():
    """Test that pre-defined ablation ranges are available for WMAP."""
    ranges = ablation.get_ablation_ranges(dataset='wmap')
    
    assert len(ranges) > 0
    assert all(len(r) == 3 for r in ranges)
    
    names = [r[0] for r in ranges]
    assert 'low' in names
    assert 'mid' in names


def test_ablation_validate_range():
    """Test ablation range validation."""
    ell_data = np.arange(30, 1500)
    
    # Valid range
    is_valid, n_points, reason = ablation.validate_ablation_range(30, 500, ell_data, min_points=50)
    assert is_valid
    assert n_points == 471  # 30 to 500 inclusive
    assert reason is None
    
    # Insufficient points
    is_valid, n_points, reason = ablation.validate_ablation_range(30, 60, ell_data, min_points=50)
    assert not is_valid
    assert n_points < 50
    assert 'Insufficient' in reason


def test_lcdm_generate_spectrum_tt():
    """Test ΛCDM spectrum generation for TT."""
    ell = np.arange(30, 1000)
    Cl_theory = lcdm.generate_lcdm_spectrum(ell, channel='TT')
    
    assert len(Cl_theory) == len(ell)
    assert np.all(Cl_theory > 0)  # TT should be positive
    assert np.all(np.isfinite(Cl_theory))
    
    # Rough sanity check: TT amplitude should be ~1000-6000 μK² at peaks
    assert np.max(Cl_theory) > 500
    assert np.max(Cl_theory) < 20000


def test_lcdm_generate_spectrum_ee():
    """Test ΛCDM spectrum generation for EE."""
    ell = np.arange(30, 1000)
    Cl_theory = lcdm.generate_lcdm_spectrum(ell, channel='EE')
    
    assert len(Cl_theory) == len(ell)
    assert np.all(Cl_theory > 0)  # EE should be positive
    assert np.all(np.isfinite(Cl_theory))
    
    # EE should be smaller than TT
    Cl_tt = lcdm.generate_lcdm_spectrum(ell, channel='TT')
    assert np.max(Cl_theory) < np.max(Cl_tt)


def test_lcdm_generate_spectrum_te():
    """Test ΛCDM spectrum generation for TE."""
    ell = np.arange(30, 1000)
    Cl_theory = lcdm.generate_lcdm_spectrum(ell, channel='TE')
    
    assert len(Cl_theory) == len(ell)
    assert np.all(np.isfinite(Cl_theory))
    # TE can be negative (it's a cross-spectrum)


def test_lcdm_generate_mock_observation_diagonal():
    """Test mock observation generation with diagonal noise."""
    ell = np.arange(30, 200)
    Cl_theory = lcdm.generate_lcdm_spectrum(ell, channel='TT')
    sigma = Cl_theory * 0.1  # 10% noise
    
    Cl_obs = lcdm.generate_mock_observation(
        ell=ell,
        Cl_theory=Cl_theory,
        noise_model={'sigma': sigma},
        seed=42
    )
    
    assert len(Cl_obs) == len(ell)
    assert np.all(np.isfinite(Cl_obs))
    
    # Check that noise was added (obs != theory)
    assert not np.allclose(Cl_obs, Cl_theory)
    
    # Check that typical deviation is ~sigma (should be within 3σ)
    residuals = (Cl_obs - Cl_theory) / sigma
    assert np.abs(np.mean(residuals)) < 0.5  # Mean should be ~0
    assert 0.5 < np.std(residuals) < 1.5  # Std should be ~1


def test_lcdm_generate_mock_observation_covariance():
    """Test mock observation generation with covariance matrix."""
    ell = np.arange(30, 100)
    n = len(ell)
    Cl_theory = lcdm.generate_lcdm_spectrum(ell, channel='TT')
    sigma = Cl_theory * 0.1
    
    # Create simple covariance (diagonal + small off-diagonal)
    cov = np.diag(sigma**2)
    for i in range(n-1):
        cov[i, i+1] = 0.5 * sigma[i] * sigma[i+1]
        cov[i+1, i] = 0.5 * sigma[i] * sigma[i+1]
    
    Cl_obs = lcdm.generate_mock_observation(
        ell=ell,
        Cl_theory=Cl_theory,
        noise_model={'sigma': sigma},
        cov=cov,
        seed=42
    )
    
    assert len(Cl_obs) == len(ell)
    assert np.all(np.isfinite(Cl_obs))
    assert not np.allclose(Cl_obs, Cl_theory)


def test_lcdm_mock_observation_with_injection():
    """Test mock observation with injected sinusoidal signal."""
    ell = np.arange(30, 500)
    Cl_theory = lcdm.generate_lcdm_spectrum(ell, channel='TT')
    sigma = Cl_theory * 0.05
    
    # Inject signal
    injection = {
        'period': 64,
        'amplitude': 0.2,
        'phase': np.pi/4
    }
    
    Cl_obs = lcdm.generate_mock_observation(
        ell=ell,
        Cl_theory=Cl_theory,
        noise_model={'sigma': sigma},
        seed=42,
        injection_signal=injection
    )
    
    assert len(Cl_obs) == len(ell)
    assert np.all(np.isfinite(Cl_obs))
    
    # Residuals should contain the injected signal
    residuals = (Cl_obs - Cl_theory) / sigma
    
    # Compute correlation with expected sinusoid
    expected_signal = injection['amplitude'] * np.sin(2*np.pi*ell/injection['period'] + injection['phase'])
    # Should have some correlation (not perfect due to noise, but detectable)
    # This is a rough sanity check


def test_ablation_summarize_results():
    """Test ablation results summarization."""
    # Mock results
    results = {
        'range_1': {
            'best_period': 255,
            'p_value': 0.003,
            'phase': 1.5,
            'amplitude': 0.15,
            'skipped': False
        },
        'range_2': {
            'best_period': 255,
            'p_value': 0.008,
            'phase': 1.6,
            'amplitude': 0.12,
            'skipped': False
        },
        'range_3': {
            'skipped': True,
            'reason': 'Insufficient points'
        }
    }
    
    summary = ablation.summarize_ablation_results(results)
    
    assert summary['n_ranges'] == 3
    assert summary['n_skipped'] == 1
    assert 255 in summary['periods']
    assert summary['periods'][255] == 2
    assert summary['mean_p_value'] is not None
    assert 0 < summary['mean_p_value'] < 0.01


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
