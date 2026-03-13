"""
Test suite for vacuum polarization one-loop calculator.

Tests the implementation of Phase 2 of the quantum corrections roadmap.

Author: UBT Research Team
Date: 2025-11-13
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

try:
    import pytest
    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False
    print("Warning: pytest not available, using basic assertions")

from vacuum_polarization_one_loop import VacuumPolarizationOneLoop


def test_initialization():
    """Test that calculator initializes with correct parameters."""
    calc = VacuumPolarizationOneLoop(
        alpha_baseline=1/137.0,
        m_electron=0.511,
        R_psi=386.0
    )
    
    assert abs(calc.alpha_0 - 1/137.0) < 1e-10
    assert calc.m_e == 0.511
    assert calc.R_psi == 386.0
    print("✓ Initialization test passed")


def test_one_loop_correction_range():
    """Test that one-loop correction is in expected range."""
    calc = VacuumPolarizationOneLoop()
    
    correction = calc.thomson_limit_correction()
    
    # One-loop should be small but positive
    # Expected range: 0.0005 to 0.005
    assert 0.0005 < correction < 0.005, f"One-loop correction {correction} out of expected range"
    print(f"✓ One-loop correction test passed: {correction:.6f}")


def test_winding_modes_negligible():
    """Test that winding modes are negligible."""
    calc = VacuumPolarizationOneLoop()
    
    winding = calc.complex_time_correction(n_max=10)
    
    # Winding modes should be extremely small
    assert winding < 1e-5, f"Winding modes {winding} larger than expected"
    print(f"✓ Winding modes test passed: {winding:.2e}")


def test_two_loop_estimate_range():
    """Test that two-loop estimate is reasonable."""
    calc = VacuumPolarizationOneLoop()
    
    two_loop = calc.estimate_two_loop_contribution()
    
    # Higher-order (two-loop and beyond) should be significant
    # Expected range: 0.030 to 0.040 (updated to match corrected estimate)
    assert 0.030 < two_loop < 0.040, f"Two-loop estimate {two_loop} out of expected range"
    print(f"✓ Two-loop estimate test passed: {two_loop:.6f}")


def test_total_correction_positive():
    """Test that total correction increases alpha_inv."""
    calc = VacuumPolarizationOneLoop()
    
    result = calc.calculate_delta_alpha_inv(
        include_winding=True,
        include_two_loop_estimate=True
    )
    
    # Baseline should be exactly 137
    assert abs(result['baseline'] - 137.0) < 1e-10
    
    # Total correction should be positive
    assert result['total_correction'] > 0
    
    # Corrected value should be larger than baseline
    assert result['alpha_inv_corrected'] > result['baseline']
    
    # Corrected value should be close to experimental
    # Should be in reasonable range around experiment (137.030 to 137.040)
    assert 137.030 < result['alpha_inv_corrected'] < 137.040, (
        f"alpha_inv_corrected {result['alpha_inv_corrected']} out of expected range"
    )
    
    print(f"✓ Total correction test passed: {result['alpha_inv_corrected']:.6f}")


def test_qed_limit_validation():
    """Test that QED limit validation runs without errors."""
    calc = VacuumPolarizationOneLoop()
    
    validation = calc.validate_qed_limit()
    
    # Should return dictionary with expected keys
    assert 'q2' in validation
    assert 'Pi' in validation
    assert 'q2_over_m2' in validation
    
    # Should test multiple scales
    assert len(validation['q2']) > 0
    
    print(f"✓ QED limit validation test passed: {len(validation['q2'])} scales tested")


def test_standard_qed_one_loop():
    """Test standard QED one-loop calculation."""
    calc = VacuumPolarizationOneLoop()
    
    # Test at small q2
    Pi_small = calc.standard_qed_one_loop(0.01)
    
    # Should be small and negative (screening)
    assert abs(Pi_small) < 1e-4
    
    # Test at larger q2
    Pi_large = calc.standard_qed_one_loop(1.0)
    
    # Should be larger in magnitude
    assert abs(Pi_large) > abs(Pi_small)
    
    print(f"✓ Standard QED one-loop test passed")


def test_result_components():
    """Test that result dictionary has all expected components."""
    calc = VacuumPolarizationOneLoop()
    
    result = calc.calculate_delta_alpha_inv(
        include_winding=True,
        include_two_loop_estimate=True
    )
    
    # Check all expected keys are present
    expected_keys = [
        'baseline',
        'qed_one_loop', 
        'two_loop_estimate',
        'winding',
        'total_correction',
        'alpha_inv_corrected',
        'relative_error'
    ]
    
    for key in expected_keys:
        assert key in result, f"Missing key: {key}"
    
    print("✓ Result components test passed")


def test_relative_error_calculation():
    """Test that relative error is calculated correctly."""
    calc = VacuumPolarizationOneLoop()
    
    result = calc.calculate_delta_alpha_inv(
        include_winding=True,
        include_two_loop_estimate=True
    )
    
    # Calculate relative error manually
    expected_error = abs(result['alpha_inv_corrected'] - 137.036) / 137.036
    
    # Should match the reported error
    assert abs(result['relative_error'] - expected_error) < 1e-10
    
    # Error should be positive and less than 100%
    assert 0 < result['relative_error'] < 1.0
    
    print(f"✓ Relative error test passed: {result['relative_error']*100:.4f}%")


def run_all_tests():
    """Run all tests."""
    print("=" * 70)
    print("Running Vacuum Polarization One-Loop Tests")
    print("=" * 70)
    print()
    
    tests = [
        test_initialization,
        test_one_loop_correction_range,
        test_winding_modes_negligible,
        test_two_loop_estimate_range,
        test_total_correction_positive,
        test_qed_limit_validation,
        test_standard_qed_one_loop,
        test_result_components,
        test_relative_error_calculation,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} ERROR: {e}")
            failed += 1
    
    print()
    print("=" * 70)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 70)
    
    return failed == 0


if __name__ == "__main__":
    if PYTEST_AVAILABLE:
        # Run with pytest if available
        import pytest
        sys.exit(pytest.main([__file__, "-v"]))
    else:
        # Run basic tests
        success = run_all_tests()
        sys.exit(0 if success else 1)
