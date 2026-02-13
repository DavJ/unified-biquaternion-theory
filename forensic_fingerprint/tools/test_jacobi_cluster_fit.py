#!/usr/bin/env python3
"""
Test script for jacobi_cluster_fit.py

Creates synthetic data with Jacobi theta function structure and verifies
that the fitting routine can recover the parameters.
"""

import numpy as np
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from forensic_fingerprint.tools.jacobi_cluster_fit import (
    jacobi_theta3,
    jacobi_theta3_power_spectrum,
    fit_jacobi_cluster,
)


def test_jacobi_theta3_basic():
    """Test that Jacobi theta function evaluates correctly."""
    print("[test] Testing jacobi_theta3 basic evaluation...")
    
    # θ₃(0, 0) should be ≈ 1 (sum of q^n² with q=0 gives only n=0 term)
    z = np.array([0.0])
    q = 0.0
    result = jacobi_theta3(z, q, n_terms=10)
    assert np.allclose(result, 1.0), f"Expected ~1.0, got {result[0]}"
    print("  ✓ θ₃(0, 0) ≈ 1.0")
    
    # θ₃ should be real-valued for real z and real q
    z = np.linspace(0, 2, 10)
    q = 0.5
    result = jacobi_theta3(z, q, n_terms=50)
    assert np.all(np.abs(np.imag(result)) < 1e-10), "Expected real values for real inputs"
    print("  ✓ θ₃ is real-valued for real inputs")
    
    # θ₃ should be periodic in z with period 1
    z1 = np.array([0.25])
    z2 = np.array([1.25])
    q = 0.3
    result1 = jacobi_theta3(z1, q, n_terms=50)
    result2 = jacobi_theta3(z2, q, n_terms=50)
    assert np.allclose(result1, result2, rtol=1e-6), "θ₃ should be periodic in z"
    print("  ✓ θ₃ is periodic in z")
    
    print("[test] jacobi_theta3 basic tests PASSED\n")


def test_power_spectrum_model():
    """Test power spectrum model generation."""
    print("[test] Testing power spectrum model...")
    
    k = np.arange(130, 150)
    k0 = 137.0
    D = 0.01
    tau = 1.0
    
    psd = jacobi_theta3_power_spectrum(k, k0, D, tau, n_terms=50)
    
    assert len(psd) == len(k), "PSD length should match k array"
    assert np.all(psd >= 0), "PSD should be non-negative"
    assert np.all(np.isfinite(psd)), "PSD should be finite"
    
    # Peak should be near k0
    peak_idx = np.argmax(psd)
    peak_k = k[peak_idx]
    assert abs(peak_k - k0) <= 5, f"Peak at k={peak_k} should be near k0={k0}"
    
    print(f"  ✓ PSD model generates valid spectrum (peak at k={peak_k})")
    print("[test] Power spectrum model test PASSED\n")


def test_fit_recovery():
    """Test that fitting can recover known parameters from synthetic data."""
    print("[test] Testing parameter recovery from synthetic data...")
    
    # Generate synthetic data with known parameters
    k_true = np.arange(134, 144)
    k0_true = 137.5
    D_true = 0.015
    tau_true = 1.2
    amp_true = 1000.0
    
    psd_true = amp_true * jacobi_theta3_power_spectrum(k_true, k0_true, D_true, tau_true, n_terms=50)
    
    # Add small noise
    rng = np.random.default_rng(42)
    noise = rng.normal(0, 0.01 * np.max(psd_true), size=len(psd_true))
    psd_obs = psd_true + noise
    
    # Fit
    result = fit_jacobi_cluster(
        k_data=k_true,
        psd_data=psd_obs,
        k_min=134,
        k_max=143,
        n_terms=50
    )
    
    # Check recovery (with reasonable tolerance for grid search)
    # Note: Grid search has limited resolution, so tolerances are generous
    print(f"  True k0={k0_true:.2f}, fitted k0={result.k0_fit:.2f}")
    print(f"  True D={D_true:.6f}, fitted D={result.D_fit:.6f}")
    print(f"  True τ={tau_true:.4f}, fitted τ={result.tau_fit:.4f}")
    print(f"  χ²/dof = {result.chi2_reduced:.6f}")
    
    # Since D and τ appear as product D·τ in the nome q = exp(-D·τ),
    # they are correlated. Check the product instead of individual values.
    product_true = D_true * tau_true
    product_fit = result.D_fit * result.tau_fit
    
    print(f"  True D·τ={product_true:.6f}, fitted D·τ={product_fit:.6f}")
    
    assert abs(result.k0_fit - k0_true) < 3.0, "k0 should be recovered within 3 units"
    assert abs(product_fit - product_true) < 0.01, "D·τ product should be recovered within 0.01"
    
    # Verify fit quality by checking residuals are reasonable
    max_residual = np.max(np.abs(result.residuals))
    max_signal = np.max(psd_obs)
    relative_residual = max_residual / max_signal
    assert relative_residual < 0.5, f"Residuals should be < 50% of signal (got {relative_residual:.2%})"
    
    print("  ✓ Parameters recovered successfully")
    print("[test] Parameter recovery test PASSED\n")


def main():
    """Run all tests."""
    print("=" * 70)
    print("Testing jacobi_cluster_fit.py")
    print("=" * 70 + "\n")
    
    try:
        test_jacobi_theta3_basic()
        test_power_spectrum_model()
        test_fit_recovery()
        
        print("=" * 70)
        print("ALL TESTS PASSED ✓")
        print("=" * 70)
        return 0
        
    except AssertionError as e:
        print(f"\n[ERROR] Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
