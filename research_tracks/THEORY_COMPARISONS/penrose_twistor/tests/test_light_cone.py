#!/usr/bin/env python3
"""
test_light_cone.py - Pytest for null interval equivalence

Tests that the light-cone structure (null intervals) is correctly
represented in the Minkowski spinor formalism.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import pytest
from sympy import symbols, simplify, sqrt, Rational
from THEORY_COMPARISONS.penrose_twistor.twistor_core.minkowski_spinor import (
    x_to_X, minkowski_interval_squared
)
from THEORY_COMPARISONS.penrose_twistor.twistor_core.ubt_bridge import (
    X2_to_ubt_matrix
)
from THEORY_COMPARISONS.penrose_twistor.common.linalg import determinant


def test_determinant_equals_interval_symbolic():
    """Test that det(X) = s² symbolically."""
    x0, x1, x2, x3 = symbols('x0 x1 x2 x3', real=True)
    
    X = x_to_X(x0, x1, x2, x3)
    det_X = determinant(X)
    s_squared = minkowski_interval_squared(x0, x1, x2, x3)
    
    difference = simplify(det_X - s_squared)
    
    assert difference == 0, f"det(X) ≠ s²: difference = {difference}"


def test_null_vector_determinant_zero():
    """Test that null vectors give det(X) = 0."""
    # Light ray along x-axis
    X = x_to_X(1, 1, 0, 0)
    det_X = simplify(determinant(X))
    assert det_X == 0, f"Expected det(X) = 0 for null vector (1,1,0,0), got {det_X}"
    
    # Light ray along y-axis
    X = x_to_X(1, 0, 1, 0)
    det_X = simplify(determinant(X))
    assert det_X == 0, f"Expected det(X) = 0 for null vector (1,0,1,0), got {det_X}"
    
    # Light ray along z-axis
    X = x_to_X(1, 0, 0, 1)
    det_X = simplify(determinant(X))
    assert det_X == 0, f"Expected det(X) = 0 for null vector (1,0,0,1), got {det_X}"


def test_timelike_vector_positive_determinant():
    """Test that timelike vectors give det(X) > 0."""
    # Pure time
    X = x_to_X(1, 0, 0, 0)
    det_X = determinant(X)
    assert det_X > 0, f"Expected det(X) > 0 for timelike vector (1,0,0,0), got {det_X}"
    
    # Inside light cone
    X = x_to_X(2, 1, 0, 0)
    det_X = determinant(X)
    assert det_X > 0, f"Expected det(X) > 0 for timelike vector (2,1,0,0), got {det_X}"


def test_spacelike_vector_negative_determinant():
    """Test that spacelike vectors give det(X) < 0."""
    # Pure space
    X = x_to_X(0, 1, 0, 0)
    det_X = determinant(X)
    assert det_X < 0, f"Expected det(X) < 0 for spacelike vector (0,1,0,0), got {det_X}"
    
    # Outside light cone
    X = x_to_X(1, 2, 0, 0)
    det_X = determinant(X)
    assert det_X < 0, f"Expected det(X) < 0 for spacelike vector (1,2,0,0), got {det_X}"


def test_null_vector_rank_one():
    """Test that null vectors produce rank-1 matrices."""
    null_vectors = [
        (1, 1, 0, 0),
        (1, 0, 1, 0),
        (1, 0, 0, 1),
        (2, sqrt(2), sqrt(2), 0),
    ]
    
    for x0, x1, x2, x3 in null_vectors:
        X = x_to_X(x0, x1, x2, x3)
        det_X = simplify(determinant(X))
        rank_X = X.rank()
        
        assert det_X == 0, f"Expected det = 0 for null vector ({x0},{x1},{x2},{x3})"
        assert rank_X == 1, f"Expected rank = 1 for null vector ({x0},{x1},{x2},{x3}), got {rank_X}"


def test_non_null_vector_rank_two():
    """Test that non-null vectors produce rank-2 (full rank) matrices."""
    non_null_vectors = [
        (1, 0, 0, 0),  # Timelike
        (0, 1, 0, 0),  # Spacelike
        (2, 1, 0, 0),  # Timelike
        (1, 2, 0, 0),  # Spacelike
    ]
    
    for x0, x1, x2, x3 in non_null_vectors:
        X = x_to_X(x0, x1, x2, x3)
        det_X = simplify(determinant(X))
        rank_X = X.rank()
        
        assert det_X != 0, f"Expected det ≠ 0 for non-null vector ({x0},{x1},{x2},{x3})"
        assert rank_X == 2, f"Expected rank = 2 for non-null vector ({x0},{x1},{x2},{x3}), got {rank_X}"


def test_ubt_embedding_null_preservation_block_diagonal():
    """Test that block_diagonal embedding preserves null structure."""
    # Null vector
    x0, x1, x2, x3 = 1, 1, 0, 0
    X2 = x_to_X(x0, x1, x2, x3)
    det_X2 = simplify(determinant(X2))
    
    assert det_X2 == 0, "Initial vector should be null"
    
    # Embed to 4×4
    X4 = X2_to_ubt_matrix(X2, mode='block_diagonal')
    det_X4 = simplify(determinant(X4))
    
    # For block diagonal [[X, 0], [0, X†]], det(X4) = det(X)²
    # So if det(X) = 0, then det(X4) = 0
    assert det_X4 == 0, f"Expected det(X₄) = 0 for null vector, got {det_X4}"


def test_ubt_embedding_preserves_structure_multiple_modes():
    """Test that different embedding modes handle null vectors correctly."""
    # Null vector
    x0, x1, x2, x3 = 1, 0, 1, 0
    X2 = x_to_X(x0, x1, x2, x3)
    det_X2 = simplify(determinant(X2))
    
    assert det_X2 == 0, "Initial vector should be null"
    
    # Test multiple embedding modes
    modes = ['block_diagonal', 'block_antidiagonal', 'direct_sum']
    
    for mode in modes:
        X4 = X2_to_ubt_matrix(X2, mode=mode)
        det_X4 = simplify(determinant(X4))
        
        # The structure should be preserved (det should remain 0 or be a power of det(X2))
        # For null X2, this means det(X4) should be 0
        assert det_X4 == 0, f"Mode {mode}: Expected det(X₄) = 0, got {det_X4}"


def test_signature_convention():
    """Test that the signature convention is correctly applied."""
    # For vector (1, 0, 0, 0): s² = 1² - 0² - 0² - 0² = 1 (timelike)
    X = x_to_X(1, 0, 0, 0)
    det_X = determinant(X)
    assert det_X == 1, f"Expected det = 1 for (1,0,0,0), got {det_X}"
    
    # For vector (0, 1, 0, 0): s² = 0² - 1² - 0² - 0² = -1 (spacelike)
    X = x_to_X(0, 1, 0, 0)
    det_X = determinant(X)
    assert det_X == -1, f"Expected det = -1 for (0,1,0,0), got {det_X}"
    
    # For vector (1, 1, 0, 0): s² = 1² - 1² - 0² - 0² = 0 (null)
    X = x_to_X(1, 1, 0, 0)
    det_X = determinant(X)
    assert det_X == 0, f"Expected det = 0 for (1,1,0,0), got {det_X}"


def test_scaled_null_vectors():
    """Test that scaled null vectors remain null."""
    # Base null vector
    x0, x1, x2, x3 = 1, 1, 0, 0
    
    # Test various scalings
    scales = [1, 2, Rational(1, 2), 3, Rational(3, 2)]
    
    for scale in scales:
        X = x_to_X(scale * x0, scale * x1, scale * x2, scale * x3)
        det_X = simplify(determinant(X))
        
        # det(X) scales as scale⁴ (since X = scale * x^μ σ_μ, det scales as scale²)
        # But for null vectors, 0 * scale² = 0
        assert det_X == 0, f"Expected det = 0 for scaled null vector (scale={scale}), got {det_X}"


if __name__ == '__main__':
    # Run all tests manually (can also use pytest)
    import sys
    
    print("Running light-cone tests...")
    print()
    
    tests = [
        test_determinant_equals_interval_symbolic,
        test_null_vector_determinant_zero,
        test_timelike_vector_positive_determinant,
        test_spacelike_vector_negative_determinant,
        test_null_vector_rank_one,
        test_non_null_vector_rank_two,
        test_ubt_embedding_null_preservation_block_diagonal,
        test_ubt_embedding_preserves_structure_multiple_modes,
        test_signature_convention,
        test_scaled_null_vectors,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        test_name = test_func.__name__
        try:
            test_func()
            print(f"✓ {test_name}")
            passed += 1
        except AssertionError as e:
            print(f"✗ {test_name}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test_name}: Unexpected error: {e}")
            failed += 1
    
    print()
    print(f"Results: {passed} passed, {failed} failed")
    
    sys.exit(0 if failed == 0 else 1)
