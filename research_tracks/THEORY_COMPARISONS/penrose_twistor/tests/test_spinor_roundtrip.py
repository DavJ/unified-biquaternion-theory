#!/usr/bin/env python3
"""
test_spinor_roundtrip.py - Test Minkowski ↔ 2×2 Hermitian roundtrip

Validates that the mapping x → X → x is exact.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import pytest
from sympy import symbols, simplify, Matrix
from THEORY_COMPARISONS.penrose_twistor.twistor_core.minkowski_spinor import (
    x_to_X, X_to_x, verify_roundtrip, minkowski_interval_squared, 
    X_determinant_as_interval, is_hermitian
)


def test_symbolic_roundtrip():
    """Test roundtrip with symbolic coordinates."""
    t, x, y, z = symbols('t x y z', real=True)
    
    # Verify roundtrip
    assert verify_roundtrip(t, x, y, z), "Symbolic roundtrip failed"
    
    print("✓ Symbolic roundtrip test passed")


def test_numeric_roundtrip():
    """Test roundtrip with numeric values."""
    test_points = [
        (0, 0, 0, 0),  # Origin
        (1, 0, 0, 0),  # Time direction
        (0, 1, 0, 0),  # x direction
        (0, 0, 1, 0),  # y direction
        (0, 0, 0, 1),  # z direction
        (1, 1, 1, 1),  # Generic point
        (2.5, -1.3, 0.7, -0.4),  # Random point
    ]
    
    for x0, x1, x2, x3 in test_points:
        X = x_to_X(x0, x1, x2, x3)
        x0_back, x1_back, x2_back, x3_back = X_to_x(X)
        
        # Check differences (should be zero or numerical precision)
        diff0 = abs(complex(x0 - x0_back))
        diff1 = abs(complex(x1 - x1_back))
        diff2 = abs(complex(x2 - x2_back))
        diff3 = abs(complex(x3 - x3_back))
        
        max_diff = max(diff0, diff1, diff2, diff3)
        
        assert max_diff < 1e-10, f"Roundtrip failed for ({x0}, {x1}, {x2}, {x3}): max diff = {max_diff}"
    
    print(f"✓ Numeric roundtrip test passed for {len(test_points)} points")


def test_hermiticity():
    """Test that x_to_X produces Hermitian matrices."""
    t, x, y, z = symbols('t x y z', real=True)
    X = x_to_X(t, x, y, z)
    
    # Check Hermiticity: X† = X
    X_dag = X.H
    diff = simplify(X - X_dag)
    
    assert diff == Matrix.zeros(2, 2), "X is not Hermitian"
    
    print("✓ Hermiticity test passed")


def test_determinant_equals_interval():
    """Test that det(X) = s² (Minkowski interval squared)."""
    t, x, y, z = symbols('t x y z', real=True)
    
    # Compute both
    det_X = X_determinant_as_interval(t, x, y, z)
    s_squared = minkowski_interval_squared(t, x, y, z)
    
    # They should be equal
    diff = simplify(det_X - s_squared)
    
    assert diff == 0, f"det(X) ≠ s²: difference = {diff}"
    
    print("✓ Determinant = interval² test passed")


def test_pauli_basis():
    """Test that Pauli matrices form the correct basis."""
    from THEORY_COMPARISONS.penrose_twistor.common.linalg import pauli_matrices
    from sympy import I, eye
    
    sigma0, sigma1, sigma2, sigma3 = pauli_matrices()
    
    # Check σ₀ = I
    assert sigma0 == eye(2), "σ₀ should be identity"
    
    # Check σ₁
    expected_sigma1 = Matrix([[0, 1], [1, 0]])
    assert sigma1 == expected_sigma1, "σ₁ incorrect"
    
    # Check σ₂
    expected_sigma2 = Matrix([[0, -I], [I, 0]])
    assert sigma2 == expected_sigma2, "σ₂ incorrect"
    
    # Check σ₃
    expected_sigma3 = Matrix([[1, 0], [0, -1]])
    assert sigma3 == expected_sigma3, "σ₃ incorrect"
    
    print("✓ Pauli matrices test passed")


def test_commutation_relations():
    """Test Pauli matrix commutation relations."""
    from THEORY_COMPARISONS.penrose_twistor.common.linalg import pauli_matrices, commutator
    from sympy import I
    
    sigma0, sigma1, sigma2, sigma3 = pauli_matrices()
    
    # [σ₁, σ₂] = 2i σ₃
    comm12 = commutator(sigma1, sigma2)
    expected = 2*I*sigma3
    assert simplify(comm12 - expected) == Matrix.zeros(2, 2), "[σ₁, σ₂] ≠ 2iσ₃"
    
    # [σ₂, σ₃] = 2i σ₁
    comm23 = commutator(sigma2, sigma3)
    expected = 2*I*sigma1
    assert simplify(comm23 - expected) == Matrix.zeros(2, 2), "[σ₂, σ₃] ≠ 2iσ₁"
    
    # [σ₃, σ₁] = 2i σ₂
    comm31 = commutator(sigma3, sigma1)
    expected = 2*I*sigma2
    assert simplify(comm31 - expected) == Matrix.zeros(2, 2), "[σ₃, σ₁] ≠ 2iσ₂"
    
    print("✓ Pauli commutation relations test passed")


def test_trace_property():
    """Test that Tr(X) = 2x⁰."""
    from THEORY_COMPARISONS.penrose_twistor.common.linalg import trace
    
    t, x, y, z = symbols('t x y z', real=True)
    X = x_to_X(t, x, y, z)
    
    tr = trace(X)
    expected = 2*t
    
    diff = simplify(tr - expected)
    
    assert diff == 0, f"Tr(X) ≠ 2t: got {tr}"
    
    print("✓ Trace property test passed")


def run_all_tests():
    """Run all spinor roundtrip tests."""
    print("=" * 70)
    print("SPINOR ROUNDTRIP TESTS")
    print("=" * 70)
    print()
    
    tests = [
        test_symbolic_roundtrip,
        test_numeric_roundtrip,
        test_hermiticity,
        test_determinant_equals_interval,
        test_pauli_basis,
        test_commutation_relations,
        test_trace_property,
    ]
    
    for test_func in tests:
        try:
            test_func()
        except AssertionError as e:
            print(f"✗ {test_func.__name__}: {e}")
            raise
        except Exception as e:
            print(f"✗ {test_func.__name__}: Unexpected error: {e}")
            raise
    
    print()
    print("=" * 70)
    print("ALL TESTS PASSED")
    print("=" * 70)


if __name__ == '__main__':
    run_all_tests()
