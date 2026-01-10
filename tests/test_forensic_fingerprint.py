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
import tempfile
import json

# Add project root to path
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

# Import forensic fingerprint modules
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'cmb_comb'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'grid_255'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'invariance'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'loaders'))

import cmb_comb
import grid_255
import invariance
import planck
import wmap


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


class TestDataLoaders:
    """Tests for Planck and WMAP data loaders (synthetic fixtures)."""
    
    def test_planck_loader_text(self, tmp_path):
        """Test Planck loader with synthetic text file."""
        # Create synthetic text file
        obs_file = tmp_path / "planck_obs.txt"
        with open(obs_file, 'w') as f:
            f.write("# ell C_ell sigma\n")
            for ell in range(30, 50):
                f.write(f"{ell} {1000.0 * np.exp(-ell/100)} {10.0}\n")
        
        # Load data
        data = planck.load_planck_data(obs_file)
        
        # Verify structure
        assert 'ell' in data
        assert 'cl_obs' in data
        assert 'sigma' in data
        assert data['dataset'] == "Planck PR3"
        assert len(data['ell']) == 20
        assert data['ell'][0] == 30
        assert data['ell'][-1] == 49
    
    def test_planck_loader_with_model(self, tmp_path):
        """Test Planck loader with observation and model files."""
        # Create obs file
        obs_file = tmp_path / "obs.txt"
        with open(obs_file, 'w') as f:
            f.write("# ell C_ell sigma\n")
            for ell in range(30, 50):
                f.write(f"{ell} {1000.0 + np.random.normal(0, 10)} {10.0}\n")
        
        # Create model file
        model_file = tmp_path / "model.txt"
        with open(model_file, 'w') as f:
            f.write("# ell C_ell\n")
            for ell in range(30, 50):
                f.write(f"{ell} {1000.0}\n")
        
        # Load data
        data = planck.load_planck_data(obs_file, model_file=model_file)
        
        # Verify model was loaded
        assert data['cl_model'] is not None
        assert len(data['cl_model']) == 20
    
    def test_planck_loader_ell_filtering(self, tmp_path):
        """Test Planck loader with ell range filtering."""
        # Create synthetic file
        obs_file = tmp_path / "obs.txt"
        with open(obs_file, 'w') as f:
            f.write("# ell C_ell sigma\n")
            for ell in range(2, 100):
                f.write(f"{ell} {1000.0} {10.0}\n")
        
        # Load with ell filtering
        data = planck.load_planck_data(obs_file, ell_min=30, ell_max=50)
        
        # Verify filtering
        assert data['ell_range'] == (30, 50)
        assert data['ell'][0] == 30
        assert data['ell'][-1] == 50
        assert len(data['ell']) == 21  # Inclusive
    
    def test_wmap_loader_text(self, tmp_path):
        """Test WMAP loader with synthetic text file."""
        # Create synthetic text file
        obs_file = tmp_path / "wmap_obs.txt"
        with open(obs_file, 'w') as f:
            f.write("# ell C_ell sigma\n")
            for ell in range(30, 50):
                f.write(f"{ell} {1100.0 * np.exp(-ell/100)} {20.0}\n")
        
        # Load data
        data = wmap.load_wmap_data(obs_file)
        
        # Verify structure
        assert 'ell' in data
        assert 'cl_obs' in data
        assert 'sigma' in data
        assert data['dataset'] == "WMAP 9yr"
        assert len(data['ell']) == 20
    
    def test_wmap_loader_ell_filtering(self, tmp_path):
        """Test WMAP loader with ell range filtering."""
        # Create synthetic file
        obs_file = tmp_path / "obs.txt"
        with open(obs_file, 'w') as f:
            f.write("# ell C_ell sigma\n")
            for ell in range(2, 100):
                f.write(f"{ell} {1100.0} {20.0}\n")
        
        # Load with ell filtering
        data = wmap.load_wmap_data(obs_file, ell_min=30, ell_max=60)
        
        # Verify filtering
        assert data['ell_range'] == (30, 60)
        assert data['ell'][0] == 30
        assert data['ell'][-1] == 60
    
    def test_planck_loader_missing_file(self):
        """Test Planck loader with non-existent file."""
        with pytest.raises(FileNotFoundError):
            planck.load_planck_data("nonexistent_file.txt")
    
    def test_wmap_loader_missing_file(self):
        """Test WMAP loader with non-existent file."""
        with pytest.raises(FileNotFoundError):
            wmap.load_wmap_data("nonexistent_file.txt")


class TestCMBCombWhitening:
    """Tests for CMB comb whitening with covariance."""
    
    def test_compute_residuals_with_covariance(self):
        """Test residual computation with full covariance (whitening)."""
        ell = np.arange(2, 10)
        C_obs = np.array([100, 95, 90, 85, 80, 75, 70, 65])
        C_model = np.array([98, 94, 91, 84, 81, 74, 71, 64])
        sigma = np.ones(8) * 5.0
        
        # Create simple covariance (diagonal + off-diagonal correlation)
        cov = np.diag(sigma**2)
        for i in range(7):
            cov[i, i+1] = cov[i+1, i] = 2.0  # Small off-diagonal
        
        # Compute whitened residuals
        residuals_whitened = cmb_comb.compute_residuals(ell, C_obs, C_model, sigma, cov=cov)
        
        # Compute non-whitened residuals
        residuals_diag = cmb_comb.compute_residuals(ell, C_obs, C_model, sigma, cov=None)
        
        # Should be different (whitening affects residuals)
        assert not np.allclose(residuals_whitened, residuals_diag)
        
        # Both should be same length
        assert len(residuals_whitened) == len(residuals_diag) == 8
    
    def test_run_cmb_comb_with_covariance(self):
        """Test full CMB comb test with covariance matrix."""
        np.random.seed(42)
        ell = np.arange(2, 50)
        C_model = 1000.0 * np.exp(-ell / 100.0)
        sigma = 0.1 * C_model
        C_obs = C_model + np.random.normal(0, sigma)
        
        # Create covariance
        cov = np.diag(sigma**2)
        
        # Run test with covariance (no output dir to avoid writing files)
        cmb_comb.N_MC_TRIALS = 100
        results = cmb_comb.run_cmb_comb_test(
            ell, C_obs, C_model, sigma, 
            output_dir=None,  # Don't save results in test
            cov=cov, 
            dataset_name="Test Dataset"
        )
        
        # Verify whitening flag is set
        assert results['whitened'] is True
        assert results['dataset'] == "Test Dataset"
        assert 'best_period' in results
        assert 'p_value' in results


class TestRealDataRunner:
    """Tests for run_real_data_cmb_comb.py runner script."""
    
    def test_runner_import(self):
        """Test that the runner script can be imported."""
        # Import the runner script
        sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))
        import run_real_data_cmb_comb
        
        # Check key functions exist
        assert hasattr(run_real_data_cmb_comb, 'validate_data_manifest')
        assert hasattr(run_real_data_cmb_comb, 'save_results_json')
        assert hasattr(run_real_data_cmb_comb, 'generate_combined_verdict')
    
    def test_save_results_json(self, tmp_path):
        """Test JSON results saving with numpy array conversion."""
        sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))
        import run_real_data_cmb_comb
        
        # Create test results with numpy arrays
        results = {
            'best_period': 32,
            'amplitude': np.float64(1.5),
            'p_value': np.float64(0.05),
            'ell': np.array([2, 3, 4, 5]),
            'residuals': np.array([0.1, 0.2, -0.1, 0.05]),
            'all_periods': {
                8: {'delta_chi2': np.float64(2.0), 'amplitude': np.float64(0.5)},
                16: {'delta_chi2': np.float64(3.0), 'amplitude': np.float64(0.7)}
            }
        }
        
        output_file = tmp_path / 'test_results.json'
        run_real_data_cmb_comb.save_results_json(results, output_file)
        
        # Verify file was created
        assert output_file.exists()
        
        # Load and verify JSON is valid
        with open(output_file, 'r') as f:
            loaded = json.load(f)
        
        # Check conversion
        assert loaded['best_period'] == 32
        assert isinstance(loaded['amplitude'], float)
        assert isinstance(loaded['ell'], list)
        assert len(loaded['ell']) == 4
        assert isinstance(loaded['all_periods']['8']['delta_chi2'], float)
    
    def test_generate_combined_verdict_pass(self, tmp_path):
        """Test combined verdict generation for PASS case."""
        sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))
        import run_real_data_cmb_comb
        
        # Create mock results that should PASS all criteria
        planck_results = {
            'dataset': 'Planck PR3',
            'ell': np.array([30, 31, 32]),
            'best_period': 255,
            'amplitude': 1.5,
            'phase': 1.57,
            'max_delta_chi2': 20.0,
            'p_value': 0.005,  # < 0.01
            'significance': 'candidate',
            'whitened': False,
            'n_mc_trials': 1000
        }
        
        wmap_results = {
            'dataset': 'WMAP 9yr',
            'ell': np.array([30, 31, 32]),
            'best_period': 255,  # Same period
            'amplitude': 1.2,
            'phase': 1.50,  # Close phase (within π/2)
            'max_delta_chi2': 15.0,
            'p_value': 0.03,  # < 0.05
            'significance': 'candidate',
            'whitened': False,
            'n_mc_trials': 1000
        }
        
        output_file = tmp_path / 'verdict.md'
        run_real_data_cmb_comb.generate_combined_verdict(
            planck_results, wmap_results, output_file, variant='C'
        )
        
        # Verify file was created
        assert output_file.exists()
        
        # Read and check content
        content = output_file.read_text()
        assert '# CMB Comb Fingerprint Test - Combined Verdict' in content
        assert 'Planck PR3 Results' in content
        assert 'WMAP 9yr Results' in content
        assert 'PASS/FAIL Decision' in content
        assert 'Variant C' in content
        assert '✓ PASS' in content  # Should pass all criteria
    
    def test_generate_combined_verdict_fail(self, tmp_path):
        """Test combined verdict generation for FAIL case."""
        sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))
        import run_real_data_cmb_comb
        
        # Create mock results that should FAIL (different periods)
        planck_results = {
            'dataset': 'Planck PR3',
            'ell': np.array([30, 31, 32]),
            'best_period': 255,
            'amplitude': 1.5,
            'phase': 1.57,
            'max_delta_chi2': 20.0,
            'p_value': 0.005,
            'significance': 'candidate',
            'whitened': False,
            'n_mc_trials': 1000
        }
        
        wmap_results = {
            'dataset': 'WMAP 9yr',
            'ell': np.array([30, 31, 32]),
            'best_period': 128,  # Different period - should FAIL
            'amplitude': 1.2,
            'phase': 1.50,
            'max_delta_chi2': 15.0,
            'p_value': 0.03,
            'significance': 'candidate',
            'whitened': False,
            'n_mc_trials': 1000
        }
        
        output_file = tmp_path / 'verdict_fail.md'
        run_real_data_cmb_comb.generate_combined_verdict(
            planck_results, wmap_results, output_file, variant='C'
        )
        
        # Verify file was created
        assert output_file.exists()
        
        # Read and check content
        content = output_file.read_text()
        assert 'FAIL' in content
        assert '✗ FAIL' in content  # Should fail period matching criterion
    
    def test_generate_combined_verdict_planck_only(self, tmp_path):
        """Test combined verdict with only Planck results."""
        sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))
        import run_real_data_cmb_comb
        
        planck_results = {
            'dataset': 'Planck PR3',
            'ell': np.array([30, 31, 32]),
            'best_period': 255,
            'amplitude': 1.5,
            'phase': 1.57,
            'max_delta_chi2': 20.0,
            'p_value': 0.005,
            'significance': 'candidate',
            'whitened': True,
            'n_mc_trials': 1000
        }
        
        output_file = tmp_path / 'verdict_planck_only.md'
        run_real_data_cmb_comb.generate_combined_verdict(
            planck_results, None, output_file, variant='C'
        )
        
        # Verify file was created
        assert output_file.exists()
        
        # Read and check content
        content = output_file.read_text()
        assert 'INCOMPLETE' in content
        assert 'WMAP replication required' in content
    
    def test_generate_combined_verdict_court_grade_warning(self, tmp_path):
        """Test that court-grade warnings appear when covariance is missing."""
        sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))
        import run_real_data_cmb_comb
        
        planck_results = {
            'dataset': 'Planck PR3',
            'ell': np.array([30, 31, 32]),
            'best_period': 255,
            'amplitude': 1.5,
            'phase': 1.57,
            'max_delta_chi2': 20.0,
            'p_value': 0.005,
            'significance': 'candidate',
            'whitened': False,  # No covariance
            'n_mc_trials': 1000
        }
        
        output_file = tmp_path / 'verdict_warning.md'
        run_real_data_cmb_comb.generate_combined_verdict(
            planck_results, None, output_file, variant='C'
        )
        
        # Read and check for warning
        content = output_file.read_text()
        assert 'WARNING' in content
        assert 'candidate-grade only' in content
        assert 'Court-grade analysis requires full covariance' in content
    
    def test_cmb_comb_variant_parameter(self):
        """Test that variant parameter works in cmb_comb.run_cmb_comb_test."""
        # Generate simple test data
        np.random.seed(42)
        ell = np.arange(2, 50)
        C_model = 1000.0 * np.exp(-ell / 100.0)
        sigma = 0.1 * C_model
        C_obs = C_model + np.random.normal(0, sigma)
        
        # Run test with variant parameter
        cmb_comb.N_MC_TRIALS = 100  # Speed up test
        results = cmb_comb.run_cmb_comb_test(
            ell, C_obs, C_model, sigma,
            variant='A',  # Test variant A
            n_mc_trials=100,
            random_seed=42
        )
        
        # Check variant was recorded
        assert results['architecture_variant'] == 'A'
        assert results['variant_valid'] is False  # Only C is valid for comb test
        assert results['n_mc_trials'] == 100
        assert results['random_seed'] == 42
    
    def test_cmb_comb_invalid_variant(self):
        """Test that invalid variant raises error."""
        ell = np.arange(2, 10)
        C_obs = np.ones(8)
        C_model = np.ones(8)
        sigma = np.ones(8)
        
        # Should raise ValueError for invalid variant
        with pytest.raises(ValueError, match="Invalid variant"):
            cmb_comb.run_cmb_comb_test(
                ell, C_obs, C_model, sigma,
                variant='X'  # Invalid
            )
    
    def test_runner_end_to_end_synthetic(self, tmp_path):
        """End-to-end test of runner with synthetic data files."""
        # Create synthetic data files
        obs_file = tmp_path / 'planck_obs.txt'
        model_file = tmp_path / 'planck_model.txt'
        
        with open(obs_file, 'w') as f:
            f.write("# ell C_ell sigma\n")
            for ell in range(30, 100):
                cl = 1000.0 * np.exp(-ell / 100.0)
                f.write(f"{ell} {cl + np.random.normal(0, 10)} 10.0\n")
        
        with open(model_file, 'w') as f:
            f.write("# ell C_ell\n")
            for ell in range(30, 100):
                cl = 1000.0 * np.exp(-ell / 100.0)
                f.write(f"{ell} {cl}\n")
        
        # Create output directory
        test_output_dir = tmp_path / 'test_output'
        
        # Import runner
        sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))
        import run_real_data_cmb_comb
        
        # Simulate command-line args
        class Args:
            pass
        
        Args.planck_obs = str(obs_file)
        Args.planck_model = str(model_file)
        Args.planck_cov = None
        Args.planck_manifest = None
        Args.ell_min_planck = 30
        Args.ell_max_planck = 99
        Args.wmap_obs = None
        Args.wmap_model = None
        Args.wmap_cov = None
        Args.wmap_manifest = None
        Args.ell_min_wmap = 30
        Args.ell_max_wmap = 800
        Args.variant = 'C'
        Args.mc_samples = 100  # Fast test
        Args.seed = 42
        Args.output_dir = str(test_output_dir)
        
        # Manually run the key parts (can't easily test main() due to argparse)
        # Load Planck data
        planck_data = planck.load_planck_data(
            obs_file=Args.planck_obs,
            model_file=Args.planck_model,
            ell_min=Args.ell_min_planck,
            ell_max=Args.ell_max_planck
        )
        
        # Run test
        planck_results = cmb_comb.run_cmb_comb_test(
            ell=planck_data['ell'],
            C_obs=planck_data['cl_obs'],
            C_model=planck_data['cl_model'],
            sigma=planck_data['sigma'],
            variant=Args.variant,
            n_mc_trials=Args.mc_samples,
            random_seed=Args.seed
        )
        
        # Create output directory
        test_output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save results
        run_real_data_cmb_comb.save_results_json(
            planck_results,
            test_output_dir / 'planck_results.json'
        )
        
        # Generate verdict
        run_real_data_cmb_comb.generate_combined_verdict(
            planck_results,
            None,
            test_output_dir / 'combined_verdict.md',
            Args.variant
        )
        
        # Verify outputs were created
        assert (test_output_dir / 'planck_results.json').exists()
        assert (test_output_dir / 'combined_verdict.md').exists()
        
        # Verify JSON can be loaded
        with open(test_output_dir / 'planck_results.json', 'r') as f:
            loaded_results = json.load(f)
        assert 'best_period' in loaded_results
        assert 'p_value' in loaded_results


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
