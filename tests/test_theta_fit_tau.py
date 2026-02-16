"""
Tests for theta_fit_tau tool

Copyright (c) 2025 Ing. David Jaroš
Licensed under the MIT License
"""

import json
import tempfile
from pathlib import Path

import numpy as np
import pytest

from forensic_fingerprint.tools.theta_fit_tau import (
    compute_derived_params,
    compute_goodness_of_fit,
    fit_gauss_envelope,
    fit_theta3_envelope,
    gauss_envelope,
    load_csv,
    theta3_envelope,
)


def test_gauss_envelope_shape():
    """Test Gaussian envelope produces expected shape."""
    k = np.arange(100, 150)
    baseline = 1.0
    A = 2.0
    k0 = 125.0
    sigma = 5.0

    psd = gauss_envelope(k, baseline, A, k0, sigma)

    # Check baseline at far edges
    assert np.isclose(psd[0], baseline, atol=0.1)
    assert np.isclose(psd[-1], baseline, atol=0.1)

    # Check peak at k0
    peak_idx = np.argmax(psd)
    assert np.isclose(k[peak_idx], k0, atol=1.0)
    assert np.isclose(psd[peak_idx], baseline + A, atol=0.1)


def test_theta3_envelope_shape():
    """Test theta3 envelope produces expected shape."""
    k = np.arange(100, 150)
    baseline = 1.0
    A = 0.5
    k0 = 125.0
    a = 0.1

    psd = theta3_envelope(k, baseline, A, k0, a, M=6, K=1.0)

    # Should be centered around k0
    assert np.isclose(psd[25], psd.max(), atol=0.5)  # k=125 is index 25


def test_load_csv_valid(tmp_path):
    """Test CSV loading with valid data."""
    csv_path = tmp_path / "test.csv"

    # Write test CSV
    with open(csv_path, "w") as f:
        f.write("kind,channel,label,raw,n,psd_obs\n")
        f.write("scan,TT,n=100,100,100,1.5\n")
        f.write("scan,TT,n=101,101,101,2.0\n")
        f.write("scan,TT,n=102,102,102,1.8\n")

    k, psd_obs = load_csv(csv_path)

    assert len(k) == 3
    assert len(psd_obs) == 3
    assert k[0] == 100
    assert k[1] == 101
    assert k[2] == 102
    assert np.isclose(psd_obs[0], 1.5)
    assert np.isclose(psd_obs[1], 2.0)
    assert np.isclose(psd_obs[2], 1.8)


def test_load_csv_missing_column(tmp_path):
    """Test CSV loading fails with missing column."""
    csv_path = tmp_path / "test.csv"

    # Write CSV without psd_obs column
    with open(csv_path, "w") as f:
        f.write("kind,channel,n\n")
        f.write("scan,TT,100\n")

    with pytest.raises(ValueError, match="psd_obs"):
        load_csv(csv_path)


def test_fit_gauss_envelope_synthetic():
    """Test Gaussian fit on synthetic data."""
    # Generate synthetic Gaussian
    k = np.arange(100, 150)
    true_params = [1.0, 2.0, 125.0, 5.0]  # baseline, A, k0, sigma
    psd_obs = gauss_envelope(k, *true_params)

    # Add small noise
    rng = np.random.default_rng(42)
    psd_obs += rng.normal(0, 0.1, size=len(k))

    # Fit
    popt, pcov = fit_gauss_envelope(k, psd_obs, kmin=110, kmax=140)

    # Check parameters are close to true values
    assert np.allclose(popt, true_params, rtol=0.2)

    # Check sigma is positive
    assert popt[3] > 0


def test_fit_theta3_envelope_synthetic():
    """Test theta3 fit on synthetic data."""
    # Generate synthetic theta3
    k = np.arange(100, 150)
    true_params = [1.0, 0.5, 125.0, 0.2]  # baseline, A, k0, a
    psd_obs = theta3_envelope(k, *true_params, M=6, K=1.0)

    # Add small noise
    rng = np.random.default_rng(42)
    psd_obs += rng.normal(0, 0.05, size=len(k))

    # Fit
    popt, pcov = fit_theta3_envelope(k, psd_obs, kmin=115, kmax=135, M=6, K=1.0)

    # Check parameters are reasonable (may not match exactly due to model complexity)
    assert popt[0] > 0  # baseline
    assert popt[1] > 0  # A
    assert 115 <= popt[2] <= 135  # k0
    assert popt[3] > 0  # a


def test_compute_derived_params_gauss():
    """Test derived parameter computation for Gaussian model."""
    popt = np.array([1.0, 2.0, 125.0, 5.0])  # baseline, A, k0, sigma
    perr = np.array([0.1, 0.1, 1.0, 0.5])

    derived = compute_derived_params("gauss_envelope", popt, perr)

    assert "sigma" in derived
    assert "sigma_uncertainty" in derived
    assert "tau_hat" in derived
    assert "tau_hat_uncertainty" in derived

    # Check sigma matches input
    assert np.isclose(derived["sigma"], 5.0)

    # Check tau_hat = 1 / (2 * sigma^2)
    expected_tau_hat = 1.0 / (2 * 5.0**2)
    assert np.isclose(derived["tau_hat"], expected_tau_hat)

    # Check tau_hat > 0
    assert derived["tau_hat"] > 0


def test_compute_derived_params_theta3():
    """Test derived parameter computation for theta3 model."""
    popt = np.array([1.0, 0.5, 125.0, 0.2])  # baseline, A, k0, a
    perr = np.array([0.1, 0.05, 1.0, 0.02])

    derived = compute_derived_params("theta3_envelope", popt, perr)

    assert "a" in derived
    assert "a_uncertainty" in derived
    assert "tau_eff" in derived
    assert "tau_eff_uncertainty" in derived

    # Check a matches input
    assert np.isclose(derived["a"], 0.2)

    # Check tau_eff = a / (4π^2)
    expected_tau_eff = 0.2 / (4 * np.pi**2)
    assert np.isclose(derived["tau_eff"], expected_tau_eff)

    # Check tau_eff > 0
    assert derived["tau_eff"] > 0


def test_compute_goodness_of_fit():
    """Test goodness of fit computation."""
    psd_obs = np.array([1.0, 2.0, 3.0, 2.0, 1.0])
    psd_fit = np.array([1.1, 1.9, 3.1, 2.1, 0.9])
    mask = np.array([True, True, True, True, True])

    goodness = compute_goodness_of_fit(psd_obs, psd_fit, mask)

    assert "rmse" in goodness
    assert "r2" in goodness
    assert "residual_mean" in goodness
    assert "residual_std" in goodness
    assert "residual_max_abs" in goodness

    # Check RMSE is positive
    assert goodness["rmse"] > 0

    # Check R^2 is reasonable
    assert 0 <= goodness["r2"] <= 1


def test_integration_with_real_csv():
    """Integration test with actual CSV if it exists."""
    csv_path = Path("scans/tt_scan_int_100_200.csv")

    if not csv_path.exists():
        pytest.skip("CSV file not found: scans/tt_scan_int_100_200.csv")

    # Load CSV
    k, psd_obs = load_csv(csv_path)

    assert len(k) > 0
    assert len(psd_obs) == len(k)
    assert k.min() >= 100
    assert k.max() <= 200

    # Try fitting in narrow window around 137
    try:
        popt, pcov = fit_gauss_envelope(k, psd_obs, kmin=134, kmax=143)

        # Check we got 4 parameters
        assert len(popt) == 4

        # Check sigma > 0
        assert popt[3] > 0

        # Compute derived params
        perr = np.sqrt(np.diag(pcov))
        derived = compute_derived_params("gauss_envelope", popt, perr)

        # Check tau_hat > 0
        assert derived["tau_hat"] > 0

        print(f"\nIntegration test results:")
        print(f"  Fitted parameters: {popt}")
        print(f"  sigma: {derived['sigma']:.3f}")
        print(f"  tau_hat: {derived['tau_hat']:.4f}")

    except Exception as e:
        pytest.fail(f"Fit failed on real data: {e}")
