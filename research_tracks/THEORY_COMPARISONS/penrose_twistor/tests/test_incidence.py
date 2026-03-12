#!/usr/bin/env python3
"""
test_incidence.py - Test incidence relation ω = i X π

Validates the fundamental incidence relation and twistor construction.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import pytest
from sympy import symbols, Matrix, I, simplify
from THEORY_COMPARISONS.penrose_twistor.twistor_core.minkowski_spinor import x_to_X
from THEORY_COMPARISONS.penrose_twistor.twistor_core.twistor import (
    incidence, twistor_from_X_pi, check_incidence, spinor,
    are_twistors_independent, reconstruct_X_from_twistors, Twistor
)


def test_incidence_symbolic():
    """Test incidence relation with symbolic values."""
    t, x, y, z = symbols('t x y z', real=True)
    a, b = symbols('a b', complex=True)
    
    X = x_to_X(t, x, y, z)
    pi = Matrix([a, b])
    
    # Compute ω
    omega = incidence(X, pi)
    
    # Verify it's a 2×1 matrix
    assert omega.shape == (2, 1), "ω should be 2×1"
    
    # Create twistor and check incidence
    Z = twistor_from_X_pi(X, pi)
    assert check_incidence(Z, X), "Incidence check failed"
    
    print("✓ Symbolic incidence test passed")


def test_incidence_numeric():
    """Test incidence relation with numeric values."""
    # Spacetime point
    X = x_to_X(1.5, 0.8, -0.3, 0.5)
    
    # Spinor
    pi = Matrix([1 + 0.5*I, 0.7 - 0.2*I])
    
    # Create twistor
    Z = twistor_from_X_pi(X, pi)
    
    # Verify incidence
    assert check_incidence(Z, X), "Numeric incidence check failed"
    
    print("✓ Numeric incidence test passed")


def test_different_spinors_same_point():
    """Test that different spinors give different twistors for same point."""
    X = x_to_X(2.0, 1.0, 0.5, -0.3)
    
    pi1 = Matrix([1, 0])
    pi2 = Matrix([0, 1])
    pi3 = Matrix([1, 1])
    
    Z1 = twistor_from_X_pi(X, pi1)
    Z2 = twistor_from_X_pi(X, pi2)
    Z3 = twistor_from_X_pi(X, pi3)
    
    # All should be incident with X
    assert check_incidence(Z1, X), "Z1 not incident"
    assert check_incidence(Z2, X), "Z2 not incident"
    assert check_incidence(Z3, X), "Z3 not incident"
    
    # ω components should be different
    assert Z1.omega != Z2.omega, "Z1 and Z2 should have different ω"
    assert Z2.omega != Z3.omega, "Z2 and Z3 should have different ω"
    
    print("✓ Different spinors test passed")


def test_twistor_independence():
    """Test twistor independence checking."""
    pi1 = Matrix([1, 0])
    pi2 = Matrix([0, 1])
    pi3 = Matrix([1, 1])  # Linear combination of pi1 and pi2
    
    X = x_to_X(1, 0, 0, 0)
    
    Z1 = twistor_from_X_pi(X, pi1)
    Z2 = twistor_from_X_pi(X, pi2)
    Z3 = twistor_from_X_pi(X, pi3)
    
    # Z1 and Z2 should be independent
    assert are_twistors_independent(Z1, Z2), "Z1 and Z2 should be independent"
    
    # Z1 and Z3 should be independent
    assert are_twistors_independent(Z1, Z3), "Z1 and Z3 should be independent"
    
    # Create dependent twistors
    Z1_copy = Twistor(Z1.omega, Z1.pi)
    assert not are_twistors_independent(Z1, Z1_copy), "Identical twistors should be dependent"
    
    print("✓ Twistor independence test passed")


def test_reconstruction_simple():
    """Test reconstruction from two twistors."""
    # Original point
    t, x, y, z = 2.0, 1.0, 0.5, -0.3
    X_original = x_to_X(t, x, y, z)
    
    # Two independent spinors
    pi1 = Matrix([1, 0])
    pi2 = Matrix([0, 1])
    
    # Create twistors
    Z1 = twistor_from_X_pi(X_original, pi1)
    Z2 = twistor_from_X_pi(X_original, pi2)
    
    # Reconstruct
    X_reconstructed = reconstruct_X_from_twistors(Z1, Z2)
    
    assert X_reconstructed is not None, "Reconstruction failed"
    
    # Check equality (within numerical precision)
    diff = simplify(X_original - X_reconstructed)
    
    # All elements should be zero (or very small)
    for i in range(2):
        for j in range(2):
            elem_diff = abs(complex(diff[i, j]))
            assert elem_diff < 1e-10, f"Reconstruction error at ({i},{j}): {elem_diff}"
    
    print("✓ Simple reconstruction test passed")


def test_reconstruction_symbolic():
    """Test reconstruction symbolically."""
    t, x, y, z = symbols('t x y z', real=True)
    X_original = x_to_X(t, x, y, z)
    
    pi1 = Matrix([1, 0])
    pi2 = Matrix([0, 1])
    
    Z1 = twistor_from_X_pi(X_original, pi1)
    Z2 = twistor_from_X_pi(X_original, pi2)
    
    X_reconstructed = reconstruct_X_from_twistors(Z1, Z2)
    
    assert X_reconstructed is not None, "Symbolic reconstruction failed"
    
    # Should be exactly equal
    diff = simplify(X_original - X_reconstructed)
    assert diff == Matrix.zeros(2, 2), "Symbolic reconstruction not exact"
    
    print("✓ Symbolic reconstruction test passed")


def test_reconstruction_different_bases():
    """Test reconstruction with different spinor bases."""
    X_original = x_to_X(1.5, 0.8, -0.4, 0.6)
    
    # Different bases
    bases = [
        (Matrix([1, 0]), Matrix([0, 1])),  # Standard
        (Matrix([1, 1]), Matrix([1, -1])),  # Hadamard-like
        (Matrix([1 + I, 0]), Matrix([0, 1 - I])),  # Complex
    ]
    
    for pi1, pi2 in bases:
        Z1 = twistor_from_X_pi(X_original, pi1)
        Z2 = twistor_from_X_pi(X_original, pi2)
        
        if not are_twistors_independent(Z1, Z2):
            continue  # Skip dependent pairs
        
        X_rec = reconstruct_X_from_twistors(Z1, Z2)
        
        assert X_rec is not None, f"Reconstruction failed for basis {pi1.T}, {pi2.T}"
        
        # Check accuracy
        diff = simplify(X_original - X_rec)
        max_diff = max(abs(complex(diff[i, j])) for i in range(2) for j in range(2))
        
        assert max_diff < 1e-10, f"Reconstruction error with basis {pi1.T}, {pi2.T}: {max_diff}"
    
    print("✓ Different bases reconstruction test passed")


def test_incidence_linearity():
    """Test that incidence is linear in π."""
    t, x, y, z = symbols('t x y z', real=True)
    alpha, beta = symbols('alpha beta', complex=True)
    
    X = x_to_X(t, x, y, z)
    
    pi1 = Matrix([1, 0])
    pi2 = Matrix([0, 1])
    
    # ω(απ₁ + βπ₂) should equal α·ω(π₁) + β·ω(π₂)
    pi_combined = alpha * pi1 + beta * pi2
    omega_combined = incidence(X, pi_combined)
    
    omega1 = incidence(X, pi1)
    omega2 = incidence(X, pi2)
    omega_linear = alpha * omega1 + beta * omega2
    
    diff = simplify(omega_combined - omega_linear)
    
    assert diff == Matrix.zeros(2, 1), "Incidence not linear in π"
    
    print("✓ Incidence linearity test passed")


def run_all_tests():
    """Run all incidence tests."""
    print("=" * 70)
    print("INCIDENCE TESTS")
    print("=" * 70)
    print()
    
    tests = [
        test_incidence_symbolic,
        test_incidence_numeric,
        test_different_spinors_same_point,
        test_twistor_independence,
        test_reconstruction_simple,
        test_reconstruction_symbolic,
        test_reconstruction_different_bases,
        test_incidence_linearity,
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
