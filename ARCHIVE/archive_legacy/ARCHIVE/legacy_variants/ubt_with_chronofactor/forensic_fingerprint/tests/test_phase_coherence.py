#!/usr/bin/env python3
"""
Test for Phase Coherence Stress Test

This test validates that the phase coherence script:
1. Can extract phases from synthetic data
2. Correctly computes circular statistics
3. Produces proper PASS/FAIL verdicts

License: MIT
"""

import sys
import tempfile
import shutil
from pathlib import Path
import numpy as np

# Add parent directories to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'stress_tests'))

import test_5_phase_coherence as phase_test


def create_synthetic_dataset(ell_min=30, ell_max=500, period=255, phase_deg=45, amplitude=0.5):
    """
    Create synthetic CMB-like dataset with known periodic signal.
    
    Parameters
    ----------
    ell_min, ell_max : int
        Multipole range
    period : int
        Period of sinusoidal signal
    phase_deg : float
        Phase in degrees
    amplitude : float
        Signal amplitude
    
    Returns
    -------
    filename : str
        Path to temporary file with synthetic data
    """
    ell = np.arange(ell_min, ell_max + 1)
    n = len(ell)
    
    # Create fake power spectrum
    cl_theory = 5000 * (ell / 100.0)**(-0.5) * np.exp(-ell / 1000.0)
    
    # Add periodic signal
    phase_rad = np.radians(phase_deg)
    theta = 2.0 * np.pi * ell / period
    signal = amplitude * np.sin(theta + phase_rad)
    
    # Add noise
    np.random.seed(42)
    sigma = 0.1 * cl_theory
    noise = np.random.normal(0, sigma)
    
    cl_obs = cl_theory * (1 + signal) + noise
    
    # Create temporary file
    tmpfile = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
    
    # Write data (ell, cl_obs, sigma)
    for i in range(n):
        tmpfile.write(f"{ell[i]} {cl_obs[i]:.6e} {sigma[i]:.6e}\n")
    
    tmpfile.close()
    return tmpfile.name


def test_phase_extraction():
    """
    Test that phase can be extracted from synthetic data with known phase.
    """
    print("\n" + "="*70)
    print("TEST: Phase Extraction from Synthetic Data")
    print("="*70)
    
    # Create synthetic data with known phase
    known_phase_deg = 45.0
    
    obs_file = create_synthetic_dataset(phase_deg=known_phase_deg, amplitude=0.5)
    model_file = create_synthetic_dataset(phase_deg=0, amplitude=0.0)  # No signal in model
    
    try:
        # Extract phase
        results = phase_test.extract_phase_from_dataset(
            obs_file=obs_file,
            model_file=model_file,
            cov_file=None,
            dataset_name="Synthetic Test",
            ell_min=30,
            ell_max=500,
            whiten_modes=['diagonal'],
            target_period=255,
            n_mc_trials=100  # Reduced for speed
        )
        
        # Check phase was extracted
        assert 'diagonal' in results
        extracted_phase = results['diagonal']['phase_deg']
        
        # Phase should be reasonably close (within ~30°) due to noise
        phase_diff = abs(extracted_phase - known_phase_deg)
        if phase_diff > 180:
            phase_diff = 360 - phase_diff
        
        print(f"\nKnown phase: {known_phase_deg:.2f}°")
        print(f"Extracted phase: {extracted_phase:.2f}°")
        print(f"Difference: {phase_diff:.2f}°")
        
        # We expect some deviation due to noise, but should be < 90°
        assert phase_diff < 90, f"Phase extraction too far off: {phase_diff:.2f}° > 90°"
        
        print("✓ PASS: Phase extraction works")
        
    finally:
        # Cleanup
        Path(obs_file).unlink()
        Path(model_file).unlink()


def test_circular_statistics():
    """
    Test that circular statistics are computed correctly.
    """
    print("\n" + "="*70)
    print("TEST: Circular Statistics")
    print("="*70)
    
    # Create synthetic phase results with known coherence
    phase_results = {
        'Dataset1': {
            'mode1': {'phase_rad': 0.5, 'phase_deg': np.degrees(0.5), 'amplitude': 0.3, 
                     'delta_chi2': 10, 'best_period': 255, 'p_value': 0.01},
            'mode2': {'phase_rad': 0.6, 'phase_deg': np.degrees(0.6), 'amplitude': 0.25,
                     'delta_chi2': 9, 'best_period': 255, 'p_value': 0.02}
        },
        'Dataset2': {
            'mode1': {'phase_rad': 0.55, 'phase_deg': np.degrees(0.55), 'amplitude': 0.28,
                     'delta_chi2': 11, 'best_period': 255, 'p_value': 0.015}
        }
    }
    
    # Compute statistics
    stats = phase_test.compute_phase_statistics(phase_results)
    
    print(f"\nCircular mean: {stats['circular_mean_deg']:.2f}°")
    print(f"Circular std: {stats['circular_std_deg']:.2f}°")
    print(f"Coherence score: {stats['coherence_score']:.3f}")
    print(f"Number of measurements: {stats['n_measurements']}")
    
    # Should have 3 measurements
    assert stats['n_measurements'] == 3
    
    # Circular mean should be near 0.55 rad ≈ 31.5°
    expected_mean_deg = np.degrees(0.55)
    mean_diff = abs(stats['circular_mean_deg'] - expected_mean_deg)
    assert mean_diff < 10, f"Circular mean off by {mean_diff:.2f}°"
    
    # Coherence should be high (phases are close)
    assert stats['coherence_score'] > 0.9, f"Coherence too low: {stats['coherence_score']:.3f}"
    
    # Pairwise differences should exist
    assert len(stats['pairwise_differences']) == 3  # C(3,2) = 3 pairs
    
    print("✓ PASS: Circular statistics computed correctly")


def test_coherence_assessment():
    """
    Test PASS/FAIL assessment logic.
    """
    print("\n" + "="*70)
    print("TEST: Coherence Assessment")
    print("="*70)
    
    # Test PASS case: high coherence, low std
    stats_pass = {
        'coherence_score': 0.95,
        'circular_std_deg': 10.0
    }
    
    verdict, detail = phase_test.assess_phase_coherence(
        stats_pass, threshold_coherence=0.9, threshold_std_deg=15.0
    )
    
    print(f"\nTest case 1 (should PASS):")
    print(f"  Verdict: {verdict}")
    print(f"  Coherence: {stats_pass['coherence_score']:.3f}")
    print(f"  Std: {stats_pass['circular_std_deg']:.1f}°")
    
    assert verdict == 'PASS', f"Expected PASS, got {verdict}"
    assert detail['coherence_pass'] == True
    assert detail['std_pass'] == True
    
    # Test FAIL case: low coherence
    stats_fail = {
        'coherence_score': 0.5,
        'circular_std_deg': 10.0
    }
    
    verdict, detail = phase_test.assess_phase_coherence(
        stats_fail, threshold_coherence=0.9, threshold_std_deg=15.0
    )
    
    print(f"\nTest case 2 (should FAIL - low coherence):")
    print(f"  Verdict: {verdict}")
    print(f"  Coherence: {stats_fail['coherence_score']:.3f}")
    
    assert verdict == 'FAIL', f"Expected FAIL, got {verdict}"
    assert detail['coherence_pass'] == False
    
    # Test FAIL case: high std
    stats_fail2 = {
        'coherence_score': 0.95,
        'circular_std_deg': 50.0
    }
    
    verdict, detail = phase_test.assess_phase_coherence(
        stats_fail2, threshold_coherence=0.9, threshold_std_deg=15.0
    )
    
    print(f"\nTest case 3 (should FAIL - high std):")
    print(f"  Verdict: {verdict}")
    print(f"  Std: {stats_fail2['circular_std_deg']:.1f}°")
    
    assert verdict == 'FAIL', f"Expected FAIL, got {verdict}"
    assert detail['std_pass'] == False
    
    print("✓ PASS: Assessment logic works correctly")


def test_report_generation():
    """
    Test that report can be generated without errors.
    """
    print("\n" + "="*70)
    print("TEST: Report Generation")
    print("="*70)
    
    # Create minimal synthetic results
    phase_results = {
        'Test Dataset': {
            'diagonal': {'phase_rad': 0.5, 'phase_deg': 28.6, 'amplitude': 0.3,
                        'delta_chi2': 10, 'best_period': 255, 'p_value': 0.01}
        }
    }
    
    stats = phase_test.compute_phase_statistics(phase_results)
    verdict, verdict_detail = phase_test.assess_phase_coherence(stats)
    
    # Create temporary output directory
    tmpdir = Path(tempfile.mkdtemp())
    
    try:
        # Generate report
        phase_test.generate_phase_stability_report(
            phase_results, stats, verdict_detail, tmpdir
        )
        
        # Check report was created
        report_file = tmpdir / 'phase_stability_report.md'
        assert report_file.exists(), "Report file not created"
        
        # Check report contains expected sections
        report_content = report_file.read_text()
        
        assert "Phase Coherence Test" in report_content
        assert "Skeptic Statement" in report_content
        assert "Verdict" in report_content
        assert "Phase Measurements" in report_content
        assert "Phase Coherence Statistics" in report_content
        assert "Pairwise Phase Differences" in report_content
        assert "PASS/FAIL Criteria" in report_content
        
        print(f"\nReport generated successfully at: {report_file}")
        print(f"Report size: {len(report_content)} characters")
        print("✓ PASS: Report generation works")
        
    finally:
        # Cleanup
        shutil.rmtree(tmpdir)


def main():
    """
    Run all tests.
    """
    print("\n" + "="*70)
    print("PHASE COHERENCE TEST - VALIDATION SUITE")
    print("="*70)
    
    tests = [
        test_phase_extraction,
        test_circular_statistics,
        test_coherence_assessment,
        test_report_generation
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"\n✗ FAIL: {test.__name__}")
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
            failed += 1
    
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Passed: {passed}/{len(tests)}")
    print(f"Failed: {failed}/{len(tests)}")
    
    if failed == 0:
        print("\n✓ ALL TESTS PASSED")
        return 0
    else:
        print(f"\n✗ {failed} TEST(S) FAILED")
        return 1


if __name__ == '__main__':
    sys.exit(main())
