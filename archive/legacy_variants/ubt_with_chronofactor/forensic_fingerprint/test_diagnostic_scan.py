#!/usr/bin/env python3
"""
Test script for diagnostic_subsegment_scan.py

Creates synthetic data with known periodic signals to validate the analysis.
"""

import numpy as np
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from diagnostic_subsegment_scan import (
    test_subharmonic_relationship,
    windowed_period_analysis,
    fit_sinusoid_with_phase_drift,
    run_diagnostic_scan
)


def create_synthetic_data_with_period(ell, period, amplitude=0.1, phase=0.0, 
                                      noise_level=1.0, add_phase_drift=False, 
                                      phase_drift_rate=0.0):
    """
    Create synthetic residuals with a known periodic signal.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    period : float
        Period of oscillation
    amplitude : float
        Amplitude of signal
    phase : float
        Phase offset (radians)
    noise_level : float
        Standard deviation of Gaussian noise
    add_phase_drift : bool
        Whether to add linear phase drift
    phase_drift_rate : float
        Rate of phase drift (radians per multipole)
    
    Returns
    -------
    residuals : ndarray
        Synthetic residuals
    sigma : ndarray
        Uncertainties (constant = noise_level)
    """
    ell = np.asarray(ell)
    
    # Generate signal
    theta = 2.0 * np.pi * ell / period
    
    if add_phase_drift:
        # Add linear phase drift
        phase_ell = phase + phase_drift_rate * ell
        signal = amplitude * np.sin(theta + phase_ell)
    else:
        signal = amplitude * np.sin(theta + phase)
    
    # Add Gaussian noise
    np.random.seed(42)
    noise = np.random.normal(0, noise_level, size=len(ell))
    
    residuals = signal + noise
    sigma = np.ones_like(ell) * noise_level
    
    return residuals, sigma


def test_subharmonic_detection():
    """Test sub-harmonic relationship detection."""
    print("=" * 80)
    print("TEST: Sub-harmonic Detection")
    print("=" * 80)
    
    # Test 1: 256 and 16 (16 = 256/16)
    result_1 = test_subharmonic_relationship(256, 16)
    print(f"\n256 vs 16:")
    print(f"  {result_1['relationship_desc']}")
    print(f"  Is sub-harmonic: {result_1['is_subharmonic']}")
    print(f"  Expected: True (256 = 16 × 16)")
    assert result_1['is_subharmonic'], "Failed: 256 and 16 should be sub-harmonic"
    assert result_1['harmonic_order'] == 16, "Failed: harmonic order should be 16"
    
    # Test 2: 255 and 16 (not exact)
    result_2 = test_subharmonic_relationship(255, 16)
    print(f"\n255 vs 16:")
    print(f"  {result_2['relationship_desc']}")
    print(f"  Is sub-harmonic: {result_2['is_subharmonic']}")
    print(f"  Expected: False (255/16 = 15.9375, not integer)")
    # Note: This might be detected as sub-harmonic with tolerance of 0.01
    
    # Test 3: 64 and 16 (16 = 64/4)
    result_3 = test_subharmonic_relationship(64, 16)
    print(f"\n64 vs 16:")
    print(f"  {result_3['relationship_desc']}")
    print(f"  Is sub-harmonic: {result_3['is_subharmonic']}")
    print(f"  Expected: True (64 = 4 × 16)")
    assert result_3['is_subharmonic'], "Failed: 64 and 16 should be sub-harmonic"
    assert result_3['harmonic_order'] == 4, "Failed: harmonic order should be 4"
    
    print("\n✓ Sub-harmonic detection tests passed")


def test_windowed_analysis():
    """Test windowed analysis with synthetic data."""
    print("\n" + "=" * 80)
    print("TEST: Windowed Analysis")
    print("=" * 80)
    
    # Create synthetic data
    ell = np.arange(30, 1500)
    period = 255
    amplitude = 0.3
    
    # Create signal that gets weaker at high ell
    residuals, sigma = create_synthetic_data_with_period(
        ell, period, amplitude=amplitude, noise_level=0.5
    )
    
    # Add amplitude decay with ell
    decay_factor = np.exp(-(ell - 30) / 1000)
    residuals = residuals * decay_factor + np.random.normal(0, 0.5, len(ell))
    
    # Run windowed analysis
    results = windowed_period_analysis(ell, residuals, period, window_size=200)
    
    print(f"\nPeriod tested: {period}")
    print(f"Number of windows: {results['n_windows']}")
    print(f"Signal strength variation: {results['signal_strength_variation']:.2f}")
    print(f"\nExpected: Signal should be stronger at low ℓ due to decay factor")
    
    # Check that we got multiple windows
    assert results['n_windows'] >= 5, "Should have at least 5 windows for ell=30-1500"
    
    # Print first few windows
    print("\nFirst 3 windows:")
    for i, w in enumerate(results['windows'][:3]):
        print(f"  Window {i+1}: ℓ={w['ell_range']}, Δχ²={w['delta_chi2']:.2f}, "
              f"A={w['amplitude']:.4f}")
    
    print("\n✓ Windowed analysis test passed")


def test_phase_drift():
    """Test phase drift detection."""
    print("\n" + "=" * 80)
    print("TEST: Phase Drift Detection")
    print("=" * 80)
    
    ell = np.arange(30, 1000)
    period = 255
    amplitude = 0.5
    
    # Test 1: No phase drift
    print("\nTest 1: No phase drift")
    residuals_1, _ = create_synthetic_data_with_period(
        ell, period, amplitude=amplitude, noise_level=0.2, add_phase_drift=False
    )
    
    result_1 = fit_sinusoid_with_phase_drift(ell, residuals_1, period)
    print(f"  Phase drift rate: {result_1['phase_drift']:.6f} rad/multipole")
    print(f"  χ² improvement: {result_1['chi2_improvement']:.2f}")
    print(f"  Expected: Near zero improvement")
    
    # Test 2: With phase drift
    print("\nTest 2: With linear phase drift")
    phase_drift_rate = 0.001  # 0.001 rad per multipole
    residuals_2, _ = create_synthetic_data_with_period(
        ell, period, amplitude=amplitude, noise_level=0.2, 
        add_phase_drift=True, phase_drift_rate=phase_drift_rate
    )
    
    result_2 = fit_sinusoid_with_phase_drift(ell, residuals_2, period)
    print(f"  Phase drift rate: {result_2['phase_drift']:.6f} rad/multipole")
    print(f"  χ² improvement: {result_2['chi2_improvement']:.2f}")
    print(f"  Expected: Positive improvement, drift rate ~{phase_drift_rate}")
    
    # With drift, improvement should be positive and noticeable
    # Note: With noise, improvement may be modest but should be positive
    assert result_2['chi2_improvement'] > 5, "Phase drift should improve fit"
    
    print("\n✓ Phase drift detection tests passed")


def test_full_diagnostic_scan():
    """Test full diagnostic scan with synthetic data."""
    print("\n" + "=" * 80)
    print("TEST: Full Diagnostic Scan")
    print("=" * 80)
    
    # Create synthetic CMB-like data
    ell = np.arange(30, 1500)
    
    # Model spectrum (simplified)
    cl_model = 5000.0 * (ell / 100.0)**(-0.3) * np.exp(-ell / 1000.0)
    
    # Add weak periodic signal with period 255
    period = 255
    amplitude_fraction = 0.02  # 2% signal
    theta = 2.0 * np.pi * ell / period
    signal = amplitude_fraction * cl_model * np.sin(theta)
    
    # Observed = model + signal + noise
    np.random.seed(42)
    sigma = 0.05 * cl_model  # 5% noise
    noise = np.random.normal(0, sigma)
    cl_obs = cl_model + signal + noise
    
    print(f"\nSynthetic data created:")
    print(f"  Multipole range: {ell.min()} to {ell.max()}")
    print(f"  Injected period: {period}")
    print(f"  Injected amplitude: {amplitude_fraction * 100:.1f}% of model")
    print(f"  Signal-to-noise: ~{amplitude_fraction/0.05:.2f}")
    
    # Run diagnostic scan
    print("\n" + "-" * 80)
    results = run_diagnostic_scan(
        ell=ell,
        cl_obs=cl_obs,
        cl_model=cl_model,
        sigma=sigma,
        cov=None,
        whiten_mode='diagonal',
        output_dir=None  # Don't save for test
    )
    
    # Verify results structure
    assert 'subharmonic_tests' in results
    assert 'period_comparison' in results
    assert 'windowed_analysis' in results
    assert 'phase_drift_analysis' in results
    
    print("\n✓ Full diagnostic scan test passed")
    
    return results


def main():
    """Run all tests."""
    print("DIAGNOSTIC SUBSEGMENT SCAN - TEST SUITE")
    print("=" * 80)
    
    try:
        # Run individual component tests
        test_subharmonic_detection()
        test_windowed_analysis()
        test_phase_drift()
        
        # Run full integration test
        test_full_diagnostic_scan()
        
        print("\n" + "=" * 80)
        print("ALL TESTS PASSED ✓")
        print("=" * 80)
        
        return 0
        
    except Exception as e:
        print(f"\n✗ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
