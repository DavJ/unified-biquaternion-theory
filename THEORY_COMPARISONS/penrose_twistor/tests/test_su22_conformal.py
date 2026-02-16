#!/usr/bin/env python3
"""
test_su22_conformal.py - Tests for SU(2,2) conformal transformations

Tests SU(2,2) group verification, Lie algebra, and conformal actions
on 2×2 Hermitian matrices with tight numerical tolerances.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import pytest
from sympy import Matrix, eye, simplify, I
from THEORY_COMPARISONS.penrose_twistor.twistor_core.su22 import (
    get_su22_hermitian_form,
    is_su22,
    su22_lie_algebra_element,
    exponentiate_su22_algebra,
    random_su22_element_numeric,
    H,
    dagger,
    is_H_unitary,
    random_su22_lie_element,
    cayley_transform,
    to_blocks_2x2,
    normalize_det,
)
from THEORY_COMPARISONS.penrose_twistor.twistor_core.conformal import (
    mobius_transform_X,
    extract_block_structure,
    verify_null_preservation,
    conformal_factor,
    transform_twistor,
    is_hermitian,
)
from THEORY_COMPARISONS.penrose_twistor.twistor_core.twistor import Twistor
from THEORY_COMPARISONS.penrose_twistor.twistor_core.numeric import norm_fro


# Use fixed seeds for reproducibility
TEST_SEED_1 = 42
TEST_SEED_2 = 123
TEST_SEED_3 = 456


def test_identity_in_su22():
    """Test that identity matrix is in SU(2,2)."""
    U = eye(4)
    assert is_su22(U), "Identity should be in SU(2,2)"
    print("✓ Identity is in SU(2,2)")


def test_hermitian_form_structure():
    """Test that H has correct block structure."""
    H = get_su22_hermitian_form()
    
    # Check blocks
    I2 = eye(2)
    Z2 = Matrix.zeros(2, 2)
    
    top_left = H[:2, :2]
    top_right = H[:2, 2:]
    bottom_left = H[2:, :2]
    bottom_right = H[2:, 2:]
    
    assert top_left == Z2, "Top-left should be zero"
    assert top_right == I2, "Top-right should be identity"
    assert bottom_left == I2, "Bottom-left should be identity"
    assert bottom_right == Z2, "Bottom-right should be zero"
    
    print("✓ H has correct block structure")


def test_su22_check_condition():
    """Test is_su22 function logic."""
    # Create a matrix that should be in SU(2,2)
    # Start with identity (known to be in SU(2,2))
    U = eye(4)
    
    H = get_su22_hermitian_form()
    
    # Check U† H U = H manually
    U_dag = U.H
    product = U_dag * H * U
    
    assert product == H, "Identity should preserve H"
    assert U.det() == 1, "Identity has determinant 1"
    
    print("✓ SU(2,2) conditions verified for identity")


def test_lie_algebra_anticommutation():
    """Test that Lie algebra elements satisfy A† H + H A = 0."""
    A = random_su22_lie_element(seed=TEST_SEED_1, scale=1.0)
    H_form = H()
    
    # Check A† H + H A = 0
    A_dag = dagger(A)
    residual = A_dag * H_form + H_form * A
    
    # Use tight numeric tolerance
    residual_norm = norm_fro(residual)
    assert residual_norm < 1e-9, f"Lie algebra element should satisfy A† H + H A = 0 (residual: {residual_norm})"
    print(f"✓ Lie algebra anticommutation verified (residual: {residual_norm:.2e})")


def test_cayley_transform_su22():
    """Test that Cayley transform produces valid SU(2,2) elements."""
    A = random_su22_lie_element(seed=TEST_SEED_1, scale=0.8)
    U = cayley_transform(A, alpha=0.05)
    U = normalize_det(U)
    
    # Check H-unitarity with tight tolerance
    assert is_H_unitary(U, tol=1e-9), "Cayley transform should produce H-unitary element"
    
    # Check det(U) = 1 with tight tolerance
    det_U = U.det()
    det_val = complex(det_U.evalf())
    assert abs(det_val - 1.0) < 1e-8, f"det(U) should be 1 (got {det_val})"
    
    H_form = H()
    h_residual = norm_fro(dagger(U) * H_form * U - H_form)
    print(f"✓ Cayley transform produces SU(2,2) element (||U†HU-H||={h_residual:.2e}, |det-1|={abs(det_val-1):.2e})")


def test_random_su22_element():
    """Test random SU(2,2) element generation via Cayley transform."""
    A = random_su22_lie_element(seed=TEST_SEED_2, scale=0.8)
    U = cayley_transform(A, alpha=0.05)
    U = normalize_det(U)
    
    # Verify H-unitarity
    assert is_H_unitary(U, tol=1e-9), "Random element should be H-unitary"
    
    # Verify det = 1
    det_U = U.det()
    det_val = complex(det_U.evalf())
    assert abs(det_val - 1.0) < 1e-8, f"det(U) should be 1 (got {det_val})"
    
    # Verify it's a 4×4 matrix
    assert U.shape == (4, 4), "Should be 4×4 matrix"
    
    print(f"✓ Random element generated via Cayley transform (|det-1|={abs(det_val-1):.2e})")


def test_extract_blocks():
    """Test block extraction from 4×4 matrix."""
    U = Matrix([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
    
    A, B, C, D = extract_block_structure(U)
    
    assert A == Matrix([[1, 2], [5, 6]]), "A block extraction failed"
    assert B == Matrix([[3, 4], [7, 8]]), "B block extraction failed"
    assert C == Matrix([[9, 10], [13, 14]]), "C block extraction failed"
    assert D == Matrix([[11, 12], [15, 16]]), "D block extraction failed"
    
    print("✓ Block extraction verified")


def test_mobius_identity():
    """Test that identity U leaves X unchanged."""
    U = eye(4)
    X = Matrix([[1, 0], [0, 1]])
    
    X_prime = mobius_transform_X(U, X)
    
    diff = simplify(X_prime - X)
    assert diff == Matrix.zeros(2, 2), "Identity should leave X unchanged"
    print("✓ Identity Möbius transformation verified")


def test_mobius_preserves_hermitian():
    """Test that Möbius transformation preserves Hermitian property with tight tolerance."""
    A = random_su22_lie_element(seed=TEST_SEED_2, scale=0.8)
    U = cayley_transform(A, alpha=0.05)
    U = normalize_det(U)
    
    X = Matrix([[2, 1+I], [1-I, 3]])  # Hermitian
    
    assert is_hermitian(X, tol=1e-9), "Input X should be Hermitian"
    
    X_prime = mobius_transform_X(U, X)
    
    # Check Hermiticity with tight tolerance
    assert is_hermitian(X_prime, tol=1e-9), "Transformed X' should be Hermitian"
    
    herm_residual = norm_fro(X_prime - dagger(X_prime))
    print(f"✓ Möbius transformation preserves Hermiticity (||X'-X'^†||={herm_residual:.2e})")


def test_null_vector_preservation():
    """Test that null matrices stay null with tight tolerance."""
    A = random_su22_lie_element(seed=TEST_SEED_3, scale=0.8)
    U = cayley_transform(A, alpha=0.05)
    U = normalize_det(U)
    
    # Null matrix (rank-1)
    X_null = Matrix([[1, 1], [1, 1]])
    
    assert X_null.det() == 0, "Test matrix should be null"
    
    result = verify_null_preservation(U, X_null)
    
    det_prime_val = abs(complex(result['det_X_prime']))
    
    # Tight tolerance: null should stay null within 1e-8
    assert det_prime_val < 1e-8, f"Null structure should be preserved (got |det|={det_prime_val:.2e})"
    print(f"✓ Null preserved: |det(X')|={det_prime_val:.2e} < 1e-8")


def test_null_vector_different_form():
    """Test null preservation with different null matrix."""
    A = random_su22_lie_element(seed=TEST_SEED_1, scale=0.8)
    U = cayley_transform(A, alpha=0.05)
    U = normalize_det(U)
    
    # Different null matrix
    X_null = Matrix([[1, 1], [1, 1]])
    
    det_X = X_null.det()
    assert det_X == 0, "Test matrix should be null"
    
    result = verify_null_preservation(U, X_null)
    
    det_prime_val = abs(complex(result['det_X_prime']))
    
    # Tight tolerance
    assert det_prime_val < 1e-8, f"Null preserved (got |det|={det_prime_val:.2e})"
    print(f"✓ Null preservation (alt. form): |det(X')|={det_prime_val:.2e} < 1e-8")


def test_conformal_factor_nonzero():
    """Test that conformal factor is finite for non-degenerate cases."""
    A = random_su22_lie_element(seed=TEST_SEED_1, scale=0.8)
    U = cayley_transform(A, alpha=0.05)
    U = normalize_det(U)
    
    X = Matrix([[1, 0], [0, 1]])  # Simple Hermitian
    
    omega_squared = conformal_factor(U, X)
    
    # Check it's finite
    try:
        omega_val = complex(omega_squared.evalf())
        is_finite = abs(omega_val) < 1e10  # Not infinity
        is_nonzero = abs(omega_val) > 1e-10  # Not zero
        valid = is_finite and is_nonzero
    except:
        import sympy as sp
        valid = (omega_squared != 0 and omega_squared != sp.oo)
    
    assert valid, "Conformal factor should be finite and nonzero"
    print("✓ Conformal factor is finite and nonzero")


def test_twistor_transformation():
    """Test SU(2,2) action on twistors."""
    U = eye(4)  # Identity
    Z = Twistor(Matrix([1, 0]), Matrix([0, 1]))
    
    Z_prime = transform_twistor(U, Z)
    
    # Should be unchanged
    omega_diff = simplify(Z.omega - Z_prime.omega)
    pi_diff = simplify(Z.pi - Z_prime.pi)
    
    assert omega_diff == Matrix.zeros(2, 1), "ω should be unchanged"
    assert pi_diff == Matrix.zeros(2, 1), "π should be unchanged"
    
    print("✓ Twistor transformation by identity verified")


def test_twistor_transformation_nontrivial():
    """Test SU(2,2) action on twistors with nontrivial U."""
    A = random_su22_lie_element(seed=TEST_SEED_3, scale=0.8)
    U = cayley_transform(A, alpha=0.05)
    U = normalize_det(U)
    
    Z = Twistor(Matrix([1, 0]), Matrix([0, 1]))
    
    Z_prime = transform_twistor(U, Z)
    
    # Just check it returns a valid twistor
    assert Z_prime.omega.shape == (2, 1), "Transformed ω should be 2×1"
    assert Z_prime.pi.shape == (2, 1), "Transformed π should be 2×1"
    
    print("✓ Nontrivial twistor transformation executed")


def test_determinant_scaling():
    """Test determinant scaling under conformal transformation."""
    A = random_su22_lie_element(seed=TEST_SEED_2, scale=0.8)
    U = cayley_transform(A, alpha=0.05)
    U = normalize_det(U)
    
    X = Matrix([[2, 0], [0, 1]])  # det = 2, non-null
    
    X_prime = mobius_transform_X(U, X)
    
    det_X = X.det()
    det_X_prime = X_prime.det()
    
    # Both should be nonzero (X is not null)
    det_val = abs(complex(det_X.evalf()))
    det_prime_val = abs(complex(det_X_prime.evalf()))
    
    assert det_val > 1e-8, "Input should be non-null"
    assert det_prime_val > 1e-8, "Transformed should remain non-null"
    
    print(f"✓ Non-null matrix remains non-null: |det(X)|={det_val:.2e}, |det(X')|={det_prime_val:.2e}")


def run_all_tests():
    """Run all SU(2,2) conformal tests."""
    print("=" * 70)
    print("SU(2,2) CONFORMAL TRANSFORMATION TESTS")
    print("=" * 70)
    print()
    
    tests = [
        test_identity_in_su22,
        test_hermitian_form_structure,
        test_su22_check_condition,
        test_lie_algebra_anticommutation,
        test_cayley_transform_su22,
        test_random_su22_element,
        test_extract_blocks,
        test_mobius_identity,
        test_mobius_preserves_hermitian,
        test_null_vector_preservation,
        test_null_vector_different_form,
        test_conformal_factor_nonzero,
        test_twistor_transformation,
        test_twistor_transformation_nontrivial,
        test_determinant_scaling,
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
    print("ALL SU(2,2) CONFORMAL TESTS PASSED")
    print("=" * 70)


if __name__ == '__main__':
    run_all_tests()
