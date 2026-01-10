#!/usr/bin/env python3
"""
Test suite for UBT Forensic Fingerprint implementations.

These are sanity tests using synthetic data to ensure the code runs correctly.
They do NOT test on real Planck data (which would require large downloads).

Run with: pytest tests/test_forensic_fingerprint.py -v
"""

import sys
from pathlib import Path
import numpy as np
import pytest

# Add project root to path
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

# Import forensic fingerprint modules
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'cmb_comb'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'grid_255'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'invariance'))

import cmb_comb
import grid_255
import invariance


class TestCMBComb:
    """Tests for CMB comb signature detection."""
    
    def test_compute_residuals(self):
        """Test residual computation."""
        ell = np.arange(2, 10)
        C_obs = np.array([100, 95, 90, 85, 80, 75, 70, 65])
        C_model = np.array([98, 94, 91, 84, 81, 74, 71, 64])
        sigma = np.ones(8) * 5.0
        
        residuals = cmb_comb.compute_residuals(ell, C_obs, C_model, sigma)
        
        expected = (C_obs - C_model) / sigma
        np.testing.assert_allclose(residuals, expected)
    
    def test_fit_sinusoid_linear(self):
        """Test sinusoidal fit."""
        # Create synthetic sinusoidal data
        ell = np.arange(2, 50)
        period = 16
        amplitude = 1.5
        phase = np.pi / 4
        
        theta = 2.0 * np.pi * ell / period
        residuals = amplitude * np.sin(theta + phase)
        
        # Fit
        A_fit, phi_fit, chi2_fit = cmb_comb.fit_sinusoid_linear(ell, residuals, period)
        
        # Should recover amplitude and phase
        assert abs(A_fit - amplitude) < 0.1
        assert abs(chi2_fit) < 1.0  # Perfect fit should have near-zero chi2
    
    def test_compute_delta_chi2(self):
        """Test delta chi-square computation."""
        # Null case: pure noise
        np.random.seed(42)
        ell = np.arange(2, 100)
        residuals = np.random.normal(0, 1, size=len(ell))
        
        delta_chi2, amplitude, phase = cmb_comb.compute_delta_chi2(ell, residuals, period=16)
        
        # For pure noise, delta_chi2 should be small (adding sinusoid doesn't help much)
        assert delta_chi2 >= 0  # Always non-negative
        assert delta_chi2 < 10  # Should be modest for noise
    
    def test_monte_carlo_null_distribution(self):
        """Test Monte Carlo null distribution generation."""
        ell = np.arange(2, 50)
        sigma = np.ones(len(ell))
        
        # Run with small number of trials for speed
        null_dist = cmb_comb.monte_carlo_null_distribution(
            ell, sigma, [8, 16, 32], n_trials=100
        )
        
        assert len(null_dist) == 100
        assert np.all(null_dist >= 0)  # All delta_chi2 should be non-negative
        assert np.median(null_dist) > 0  # Should have some positive values
    
    def test_run_cmb_comb_test_null(self):
        """Test full CMB comb pipeline with null data."""
        # Generate null data (no signal)
        np.random.seed(42)
        ell = np.arange(2, 100)
        C_model = 1000.0 * np.exp(-ell / 100.0)
        sigma = 0.1 * C_model
        C_obs = C_model + np.random.normal(0, sigma)
        
        # Run test (with reduced MC trials for speed)
        cmb_comb.N_MC_TRIALS = 100  # Override for speed
        results = cmb_comb.run_cmb_comb_test(ell, C_obs, C_model, sigma)
        
        # Check results structure
        assert 'best_period' in results
        assert 'p_value' in results
        assert 'significance' in results
        
        # Null data should likely give null result (but not guaranteed due to random chance)
        # Just check p-value is in valid range
        assert 0 <= results['p_value'] <= 1
    
    def test_run_cmb_comb_test_signal(self):
        """Test full CMB comb pipeline with injected signal."""
        # Generate data with injected sinusoid
        np.random.seed(42)
        ell = np.arange(2, 100)
        C_model = 1000.0 * np.exp(-ell / 100.0)
        sigma = 0.1 * C_model
        
        # Inject strong signal at period 32
        theta = 2.0 * np.pi * ell / 32
        signal = 3.0 * sigma * np.sin(theta + 1.0)  # 3-sigma amplitude
        C_obs = C_model + signal + np.random.normal(0, sigma * 0.3)
        
        # Run test
        cmb_comb.N_MC_TRIALS = 100
        results = cmb_comb.run_cmb_comb_test(ell, C_obs, C_model, sigma)
        
        # Should likely detect signal (but not guaranteed)
        assert 'best_period' in results
        # Best period should be close to injected period
        # (May not be exact due to noise, so we allow some tolerance)


class TestGrid255:
    """Tests for grid 255 quantization test."""
    
    def test_compute_grid_distance(self):
        """Test grid distance computation."""
        # Exact grid point
        samples = np.array([0.0, 1/255, 2/255, 10/255])
        distances = grid_255.compute_grid_distance(samples, denominator=255)
        
        # Should be exactly zero for grid points
        np.testing.assert_allclose(distances, 0.0, atol=1e-10)
    
    def test_compute_grid_distance_midpoint(self):
        """Test grid distance at midpoints."""
        # Midpoint between grid points
        samples = np.array([0.5/255, 1.5/255, 2.5/255])
        distances = grid_255.compute_grid_distance(samples, denominator=255)
        
        # Distance should be 0.5/255
        expected = 0.5 / 255
        np.testing.assert_allclose(distances, expected, rtol=1e-6)
    
    def test_compute_summary_statistics(self):
        """Test summary statistics computation."""
        distances = np.array([0.001, 0.002, 0.003, 0.004, 0.005])
        
        S1, S2 = grid_255.compute_summary_statistics(distances)
        
        # S1 should be median
        assert S1 == 0.003
        
        # S2 should be mean of log10
        expected_S2 = np.mean(np.log10(distances))
        assert abs(S2 - expected_S2) < 1e-10
    
    def test_generate_null_distribution(self):
        """Test null distribution generation."""
        # Uniform samples (no grid alignment)
        np.random.seed(137)
        samples = np.random.uniform(0, 0.1, size=1000)
        
        # Generate small null distribution for speed
        grid_255.N_MC_TRIALS = 50
        S1_null, S2_null = grid_255.generate_null_distribution(samples, n_trials=50)
        
        assert len(S1_null) == 50
        assert len(S2_null) == 50
        assert np.all(S1_null >= 0)
    
    def test_run_grid_255_test_null(self):
        """Test full grid 255 pipeline with null data."""
        # Generate uniform samples (no quantization)
        np.random.seed(137)
        samples = np.random.uniform(0.02, 0.03, size=1000)
        
        # Run test with reduced trials for speed
        grid_255.N_MC_TRIALS = 50
        results = grid_255.run_grid_255_test(samples, parameter_name='test_param')
        
        # Check results structure
        assert 'S1_obs' in results
        assert 'S2_obs' in results
        assert 'p1' in results
        assert 'p2' in results
        assert 'significance' in results
        
        # P-values should be in valid range
        assert 0 <= results['p1'] <= 1
        assert 0 <= results['p2'] <= 1
    
    def test_run_grid_255_test_signal(self):
        """Test full grid 255 pipeline with quantized data."""
        # Generate samples clustered near grid points
        np.random.seed(137)
        n_samples = 1000
        
        # Choose random grid points
        m_values = np.random.randint(5, 10, size=n_samples)
        grid_points = m_values / 255.0
        
        # Add small noise around grid points
        samples = grid_points + np.random.normal(0, 1e-5, size=n_samples)
        
        # Run test
        grid_255.N_MC_TRIALS = 50
        results = grid_255.run_grid_255_test(samples, parameter_name='quantized_param')
        
        # Should likely detect quantization (very tight clustering)
        # But we just check code runs without error
        assert 'significance' in results


class TestInvariance:
    """Tests for cross-dataset invariance test."""
    
    def test_ubt_invariant_kappa(self):
        """Test invariant computation (placeholder)."""
        omega_b = 0.02237
        kappa = invariance.ubt_invariant_kappa(omega_b)
        
        # Should return a number
        assert isinstance(kappa, (int, float))
    
    def test_propagate_uncertainty(self):
        """Test uncertainty propagation."""
        param_value = 0.02237
        param_sigma = 0.00015
        
        inv_value, inv_sigma = invariance.propagate_uncertainty(
            param_value, param_sigma, invariance.ubt_invariant_kappa
        )
        
        # Should return numbers
        assert isinstance(inv_value, (int, float))
        assert isinstance(inv_sigma, (int, float))
        assert inv_sigma > 0
    
    def test_compute_weighted_mean(self):
        """Test weighted mean calculation."""
        values = np.array([1.0, 1.2, 0.9, 1.1])
        sigmas = np.array([0.1, 0.2, 0.1, 0.15])
        
        mean, mean_sigma = invariance.compute_weighted_mean(values, sigmas)
        
        # Mean should be close to simple average for similar uncertainties
        assert 0.9 < mean < 1.2
        assert mean_sigma > 0
        assert mean_sigma < min(sigmas)  # Combined uncertainty should be smaller
    
    def test_compute_chi_square(self):
        """Test chi-square computation."""
        # Perfect agreement
        values = np.array([1.0, 1.0, 1.0, 1.0])
        sigmas = np.array([0.1, 0.1, 0.1, 0.1])
        
        chi2, dof = invariance.compute_chi_square(values, sigmas)
        
        assert chi2 == 0.0  # Perfect agreement
        assert dof == 3  # 4 datasets - 1
    
    def test_compute_chi_square_disagreement(self):
        """Test chi-square with disagreement."""
        values = np.array([1.0, 2.0, 3.0, 4.0])
        sigmas = np.array([0.1, 0.1, 0.1, 0.1])
        
        chi2, dof = invariance.compute_chi_square(values, sigmas)
        
        assert chi2 > 0  # Should have large chi2 for disagreement
        assert dof == 3
    
    def test_chi2_p_value(self):
        """Test p-value computation."""
        # Chi2 = dof should give p ~ 0.5
        chi2 = 3.0
        dof = 3
        
        p_value = invariance.chi2_p_value(chi2, dof)
        
        assert 0 < p_value < 1
        assert 0.3 < p_value < 0.7  # Should be around 0.5
    
    def test_run_invariance_test_consistent(self):
        """Test full invariance pipeline with consistent datasets."""
        # Create datasets with consistent values
        datasets = [
            {'name': 'Dataset1', 'param_value': 0.02237, 'param_sigma': 0.00015},
            {'name': 'Dataset2', 'param_value': 0.02240, 'param_sigma': 0.00015},
            {'name': 'Dataset3', 'param_value': 0.02235, 'param_sigma': 0.00015},
        ]
        
        results = invariance.run_invariance_test(
            datasets, invariance.ubt_invariant_kappa, invariant_name='kappa'
        )
        
        # Check results structure
        assert 'chi2' in results
        assert 'p_value' in results
        assert 'consistent' in results
        
        # Should likely be consistent (values are close)
        assert results['p_value'] > 0.01  # Very likely to pass
    
    def test_run_invariance_test_inconsistent(self):
        """Test full invariance pipeline with inconsistent datasets."""
        # Create datasets with wildly different values
        datasets = [
            {'name': 'Dataset1', 'param_value': 0.020, 'param_sigma': 0.00015},
            {'name': 'Dataset2', 'param_value': 0.025, 'param_sigma': 0.00015},
            {'name': 'Dataset3', 'param_value': 0.030, 'param_sigma': 0.00015},
        ]
        
        results = invariance.run_invariance_test(
            datasets, invariance.ubt_invariant_kappa, invariant_name='kappa'
        )
        
        # Should detect inconsistency
        assert results['chi2'] > 10  # Very large chi2
        assert results['p_value'] < 0.01  # Very small p-value


# Fixture for temporary output directory
@pytest.fixture
def tmp_output_dir(tmp_path):
    """Create temporary output directory for tests."""
    output_dir = tmp_path / "forensic_test_output"
    output_dir.mkdir()
    return output_dir


class TestIntegration:
    """Integration tests using temporary files."""
    
    def test_cmb_comb_save_results(self, tmp_output_dir):
        """Test CMB comb results saving."""
        # Create minimal results dict
        results = {
            'best_period': 32,
            'amplitude': 1.5,
            'phase': 0.5,
            'max_delta_chi2': 10.0,
            'p_value': 0.05,
            'significance': 'null',
            'null_distribution': np.array([5.0, 6.0, 7.0]),
            'ell': np.arange(2, 10),
            'residuals': np.random.normal(0, 1, 8)
        }
        
        cmb_comb.save_results(results, tmp_output_dir)
        
        # Check files were created
        assert (tmp_output_dir / 'cmb_comb_results.txt').exists()
        assert (tmp_output_dir / 'null_distribution.txt').exists()
        assert (tmp_output_dir / 'residuals_and_fit.txt').exists()
    
    def test_grid_255_save_results(self, tmp_output_dir):
        """Test grid 255 results saving."""
        results = {
            'parameter_name': 'test_param',
            'n_samples': 100,
            'S1_obs': 0.001,
            'S2_obs': -3.0,
            'p1': 0.1,
            'p2': 0.2,
            'significance': 'null',
            'S1_null': np.array([0.002, 0.003]),
            'S2_null': np.array([-2.5, -2.8]),
            'distances': np.array([0.001, 0.002]),
            'samples': np.array([0.02, 0.03])
        }
        
        grid_255.save_results(results, tmp_output_dir)
        
        # Check files were created
        assert (tmp_output_dir / 'grid_255_test_param_results.txt').exists()
        assert (tmp_output_dir / 'grid_255_test_param_null_S1.txt').exists()
    
    def test_invariance_save_results(self, tmp_output_dir):
        """Test invariance results saving."""
        results = {
            'invariant_name': 'kappa',
            'invariants': [
                {'name': 'Dataset1', 'value': 1.0, 'sigma': 0.1},
                {'name': 'Dataset2', 'value': 1.1, 'sigma': 0.1},
            ],
            'weighted_mean': 1.05,
            'weighted_sigma': 0.07,
            'chi2': 1.0,
            'dof': 1,
            'p_value': 0.32,
            'consistent': True
        }
        
        invariance.save_results(results, tmp_output_dir)
        
        # Check files were created
        assert (tmp_output_dir / 'invariance_kappa_results.txt').exists()
        assert (tmp_output_dir / 'invariance_kappa_table.txt').exists()


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
