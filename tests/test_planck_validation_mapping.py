#!/usr/bin/env python3
"""
Test suite for UBT Planck Validation mappings.

These tests enforce the pre-registered protocol:
1. Constants must match locked values
2. Mappings must produce exact pre-registered predictions
3. TBD mappings must raise NotImplementedError (to prevent silent fitting)
4. Z-scores must match expected values for Planck 2018 data

Run with: pytest tests/test_planck_validation_mapping.py -v
"""

import sys
from pathlib import Path
import pytest
import numpy as np

# Add project root to path
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

from tools.planck_validation import constants, mapping, metrics


class TestConstants:
    """Test that pre-registered constants are locked."""
    
    def test_rs_n_locked(self):
        """RS_N must be 255 (LOCKED)."""
        assert constants.RS_N == 255, "RS_N has been modified from locked value 255"
    
    def test_rs_k_locked(self):
        """RS_K must be 200 (LOCKED)."""
        assert constants.RS_K == 200, "RS_K has been modified from locked value 200"
    
    def test_ofdm_channels_locked(self):
        """OFDM_CHANNELS must be 16 (LOCKED)."""
        assert constants.OFDM_CHANNELS == 16, "OFDM_CHANNELS has been modified from locked value 16"
    
    def test_derived_parity(self):
        """RS_PARITY must equal RS_N - RS_K."""
        assert constants.RS_PARITY == 55
        assert constants.RS_PARITY == constants.RS_N - constants.RS_K
    
    def test_validate_constants(self):
        """Validate function must not raise."""
        # Should not raise if constants are correct
        constants.validate_constants()


class TestMappingImplemented:
    """Test implemented mappings produce exact pre-registered values."""
    
    def test_m_payload_exact_value(self):
        """M_payload must return exact pre-registered prediction."""
        omega_b_h2 = mapping.M_payload()
        expected = 0.02231
        
        # Allow tiny floating-point tolerance
        assert abs(omega_b_h2 - expected) < 1e-6, \
            f"M_payload() = {omega_b_h2}, expected {expected}"
    
    def test_m_payload_with_locked_params(self):
        """M_payload with explicit locked params must return same value."""
        omega_b_h2 = mapping.M_payload(R=255, D=200)
        expected = 0.02231
        assert abs(omega_b_h2 - expected) < 1e-6
    
    def test_m_payload_rejects_non_locked_params(self):
        """M_payload must reject non-locked parameter values."""
        with pytest.raises(ValueError, match="Only locked values"):
            mapping.M_payload(R=256, D=200)
        
        with pytest.raises(ValueError, match="Only locked values"):
            mapping.M_payload(R=255, D=201)
    
    def test_m_parity_exact_value(self):
        """M_parity must return exact pre-registered prediction."""
        omega_c_h2 = mapping.M_parity()
        expected = 0.1192
        
        assert abs(omega_c_h2 - expected) < 1e-6, \
            f"M_parity() = {omega_c_h2}, expected {expected}"
    
    def test_m_parity_rejects_non_locked_params(self):
        """M_parity must reject non-locked parameter values."""
        with pytest.raises(ValueError, match="Only locked values"):
            mapping.M_parity(R=256, D=200)
    
    def test_m_ns_exact_value(self):
        """M_ns must return exact pre-registered prediction."""
        n_s = mapping.M_ns()
        expected_exact = 1.0 - 9.0/255.0  # Exact formula
        
        # This should be exact (no intermediate approximations)
        assert abs(n_s - expected_exact) < 1e-12, \
            f"M_ns() = {n_s:.15f}, expected {expected_exact:.15f}"
    
    def test_m_ns_expected_value(self):
        """M_ns should be approximately 0.9647."""
        n_s = mapping.M_ns()
        assert abs(n_s - 0.9647) < 1e-4
    
    def test_m_ns_rejects_non_locked_params(self):
        """M_ns must reject non-locked parameter values."""
        with pytest.raises(ValueError, match="Only locked value"):
            mapping.M_ns(R=256)


class TestMappingTBD:
    """Test that TBD mappings raise NotImplementedError."""
    
    def test_m_phase_not_implemented(self):
        """M_phase must raise NotImplementedError."""
        with pytest.raises(NotImplementedError, match="M_phase"):
            mapping.M_phase()
    
    def test_m_snr_not_implemented(self):
        """M_SNR must raise NotImplementedError."""
        with pytest.raises(NotImplementedError, match="M_SNR"):
            mapping.M_SNR()
    
    def test_tbd_error_messages_mention_no_fitting(self):
        """TBD error messages must mention no-fitting policy."""
        with pytest.raises(NotImplementedError, match="NO additional tunable parameters"):
            mapping.M_phase()
        
        with pytest.raises(NotImplementedError, match="NO additional tunable parameters"):
            mapping.M_SNR()


class TestGetAllPredictions:
    """Test get_all_predictions utility function."""
    
    def test_returns_dict(self):
        """get_all_predictions must return dict."""
        predictions = mapping.get_all_predictions()
        assert isinstance(predictions, dict)
    
    def test_has_all_keys(self):
        """Must have keys for all 5 parameters."""
        predictions = mapping.get_all_predictions()
        expected_keys = {'omega_b_h2', 'omega_c_h2', 'n_s', 'theta_star', 'sigma_8'}
        assert set(predictions.keys()) == expected_keys
    
    def test_implemented_not_none(self):
        """Implemented predictions must not be None."""
        predictions = mapping.get_all_predictions()
        assert predictions['omega_b_h2'] is not None
        assert predictions['omega_c_h2'] is not None
        assert predictions['n_s'] is not None
    
    def test_tbd_are_none(self):
        """TBD predictions must be None."""
        predictions = mapping.get_all_predictions()
        assert predictions['theta_star'] is None
        assert predictions['sigma_8'] is None


class TestMetrics:
    """Test statistical metrics functions."""
    
    def test_sigma_deviation_zero(self):
        """Perfect agreement should give z=0."""
        z = metrics.sigma_deviation(0.02237, 0.02237, 0.00015)
        assert abs(z) < 1e-10
    
    def test_sigma_deviation_positive(self):
        """Overprediction should give positive z."""
        z = metrics.sigma_deviation(0.02250, 0.02237, 0.00015)
        assert z > 0
        # Should be approximately 0.87
        assert abs(z - 0.8667) < 0.01
    
    def test_sigma_deviation_negative(self):
        """Underprediction should give negative z."""
        z = metrics.sigma_deviation(0.02220, 0.02237, 0.00015)
        assert z < 0
        # Should be approximately -1.13
        assert abs(z - (-1.1333)) < 0.01
    
    def test_chi2_single(self):
        """chi2_single should return z^2."""
        chi2 = metrics.chi2_single(0.02250, 0.02237, 0.00015)
        z = metrics.sigma_deviation(0.02250, 0.02237, 0.00015)
        assert abs(chi2 - z**2) < 1e-10
    
    def test_chi2_vector(self):
        """chi2_vector should sum individual chi2 contributions."""
        predictions = [0.02231, 0.1192, 0.9647]
        observations = [0.02237, 0.1200, 0.9649]
        sigmas = [0.00015, 0.0012, 0.0042]
        
        chi2 = metrics.chi2_vector(predictions, observations, sigmas)
        
        # Should be small (all predictions close to observations)
        assert chi2 >= 0
        assert chi2 < 5  # For 3 parameters, chi2 < 5 is good agreement
    
    def test_success_criterion_pass(self):
        """Success criterion should pass for all |z| <= 1."""
        z_scores = [0.4, -0.67, 0.05]
        assert metrics.success_criterion(z_scores, threshold=1.0) is True
    
    def test_success_criterion_fail(self):
        """Success criterion should fail if any |z| > threshold."""
        z_scores = [0.4, 1.5, 0.05]
        assert metrics.success_criterion(z_scores, threshold=1.0) is False
    
    def test_success_criterion_boundary(self):
        """Success criterion at exact boundary."""
        z_scores = [1.0, -1.0, 0.0]
        assert metrics.success_criterion(z_scores, threshold=1.0) is True
        
        z_scores = [1.0001, 0.0, 0.0]
        assert metrics.success_criterion(z_scores, threshold=1.0) is False


class TestPlanckComparison:
    """Test actual comparison against Planck 2018 data."""
    
    def test_omega_b_h2_zscore(self):
        """Z-score for Omega_b h^2 should be as expected."""
        pred = mapping.M_payload()
        obs = constants.PLANCK_2018_OMEGA_B_H2
        sigma = constants.PLANCK_2018_OMEGA_B_H2_SIGMA
        
        z = metrics.sigma_deviation(pred, obs, sigma)
        
        # Pre-registered prediction 0.02231 vs observed 0.02237
        # z = (0.02231 - 0.02237) / 0.00015 = -0.4
        expected_z = (pred - obs) / sigma
        assert abs(z - expected_z) < 1e-10
        
        # Should be within 1 sigma
        assert abs(z) <= 1.0
    
    def test_omega_c_h2_zscore(self):
        """Z-score for Omega_c h^2 should be as expected."""
        pred = mapping.M_parity()
        obs = constants.PLANCK_2018_OMEGA_C_H2
        sigma = constants.PLANCK_2018_OMEGA_C_H2_SIGMA
        
        z = metrics.sigma_deviation(pred, obs, sigma)
        
        # Pre-registered prediction 0.1192 vs observed 0.1200
        # z = (0.1192 - 0.1200) / 0.0012 = -0.667
        expected_z = (pred - obs) / sigma
        assert abs(z - expected_z) < 1e-10
        
        # Should be within 1 sigma
        assert abs(z) <= 1.0
    
    def test_n_s_zscore(self):
        """Z-score for n_s should be as expected."""
        pred = mapping.M_ns()
        obs = constants.PLANCK_2018_N_S
        sigma = constants.PLANCK_2018_N_S_SIGMA
        
        z = metrics.sigma_deviation(pred, obs, sigma)
        
        # Pre-registered prediction 0.9647 vs observed 0.9649
        # z = (0.9647 - 0.9649) / 0.0042 ≈ -0.048
        expected_z = (pred - obs) / sigma
        assert abs(z - expected_z) < 1e-10
        
        # Should be well within 1 sigma
        assert abs(z) <= 1.0
    
    def test_all_implemented_within_1sigma(self):
        """All implemented predictions should be within 1σ."""
        predictions = [
            mapping.M_payload(),
            mapping.M_parity(),
            mapping.M_ns()
        ]
        observations = [
            constants.PLANCK_2018_OMEGA_B_H2,
            constants.PLANCK_2018_OMEGA_C_H2,
            constants.PLANCK_2018_N_S
        ]
        sigmas = [
            constants.PLANCK_2018_OMEGA_B_H2_SIGMA,
            constants.PLANCK_2018_OMEGA_C_H2_SIGMA,
            constants.PLANCK_2018_N_S_SIGMA
        ]
        
        z_scores = []
        for pred, obs, sigma in zip(predictions, observations, sigmas):
            z = metrics.sigma_deviation(pred, obs, sigma)
            z_scores.append(z)
            assert abs(z) <= 1.0, f"Prediction {pred} exceeds 1σ from {obs}±{sigma}"
        
        # Success criterion should be met
        assert metrics.success_criterion(z_scores, threshold=1.0) is True
    
    def test_combined_chi2(self):
        """Combined chi-square should be small."""
        predictions = [
            mapping.M_payload(),
            mapping.M_parity(),
            mapping.M_ns()
        ]
        observations = [
            constants.PLANCK_2018_OMEGA_B_H2,
            constants.PLANCK_2018_OMEGA_C_H2,
            constants.PLANCK_2018_N_S
        ]
        sigmas = [
            constants.PLANCK_2018_OMEGA_B_H2_SIGMA,
            constants.PLANCK_2018_OMEGA_C_H2_SIGMA,
            constants.PLANCK_2018_N_S_SIGMA
        ]
        
        chi2 = metrics.chi2_vector(predictions, observations, sigmas)
        
        # For 3 parameters, chi2 should be << 3*3 = 9
        # Good agreement would be chi2 ~ dof = 3
        assert chi2 < 5, f"chi2 = {chi2} is too large for good agreement"
        
        # P-value should be high (good agreement)
        pvalue = metrics.chi2_pvalue(chi2, dof=3)
        assert pvalue > 0.05, f"p-value = {pvalue} indicates tension with data"


class TestValidateMappings:
    """Test the validation function."""
    
    def test_validate_mappings(self):
        """validate_mappings should not raise if values are correct."""
        # This enforces that mappings produce exact pre-registered values
        mapping.validate_mappings()
