#!/usr/bin/env python3
"""
test_ubt_generators_clifford.py - Tests for UBT-derived sigma matrices

Tests the derivation of sigma matrices from biquaternion basis and
verifies Clifford relations, determinant properties, and null vectors.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import pytest
from sympy import symbols, Matrix, I, simplify, eye
from THEORY_COMPARISONS.penrose_twistor.twistor_core.ubt_generators import (
    get_biquaternion_basis_2x2,
    get_sigma_matrices,
    get_bar_sigma_matrices,
    verify_pauli_relations,
    verify_clifford_relations,
    verify_determinant_minkowski_form,
    get_null_vector_example,
    verify_null_vector_determinant,
    compute_X_from_coordinates,
    verify_hermiticity_of_X,
    minkowski_metric,
)


def test_biquaternion_basis_size():
    """Test that basis has 4 elements."""
    basis = get_biquaternion_basis_2x2()
    assert len(basis) == 4, "Basis should have 4 elements"
    print("✓ Biquaternion basis has 4 elements")


def test_biquaternion_basis_are_2x2():
    """Test that all basis elements are 2×2 matrices."""
    basis = get_biquaternion_basis_2x2()
    for i, mat in enumerate(basis):
        assert mat.shape == (2, 2), f"Basis element {i} is not 2×2"
    print("✓ All basis elements are 2×2 matrices")


def test_pauli_relations():
    """Test Pauli matrix relations."""
    assert verify_pauli_relations(), "Pauli matrix relations failed"
    print("✓ Pauli matrix relations verified")


def test_sigma_i_squared():
    """Test σᵢ² = I for all i=1,2,3."""
    _, sigma_1, sigma_2, sigma_3 = get_biquaternion_basis_2x2()
    I2 = eye(2)
    
    for i, sigma_i in enumerate([sigma_1, sigma_2, sigma_3], 1):
        sigma_i_squared = simplify(sigma_i * sigma_i)
        assert sigma_i_squared == I2, f"σ_{i}² should equal I"
    
    print("✓ σᵢ² = I for all i")


def test_sigma_commutation():
    """Test σ₁σ₂ = iσ₃, σ₂σ₃ = iσ₁, σ₃σ₁ = iσ₂."""
    _, sigma_1, sigma_2, sigma_3 = get_biquaternion_basis_2x2()
    
    # σ₁σ₂ = iσ₃
    s12 = simplify(sigma_1 * sigma_2)
    assert s12 == I*sigma_3, "σ₁σ₂ should equal iσ₃"
    
    # σ₂σ₃ = iσ₁
    s23 = simplify(sigma_2 * sigma_3)
    assert s23 == I*sigma_1, "σ₂σ₃ should equal iσ₁"
    
    # σ₃σ₁ = iσ₂
    s31 = simplify(sigma_3 * sigma_1)
    assert s31 == I*sigma_2, "σ₃σ₁ should equal iσ₂"
    
    print("✓ Pauli commutation relations verified")


def test_sigma_matrices_count():
    """Test that we have 4 sigma matrices."""
    sigma = get_sigma_matrices()
    assert len(sigma) == 4, "Should have 4 sigma matrices"
    print("✓ 4 sigma matrices returned")


def test_sigma_0_is_identity():
    """Test that sigma_0 is the identity matrix."""
    sigma_0, _, _, _ = get_sigma_matrices()
    I2 = eye(2)
    assert sigma_0 == I2, "sigma_0 should be identity"
    print("✓ σ₀ = I")


def test_bar_sigma_spatial_sign_flip():
    """Test that bar_sigma_i = -sigma_i for i=1,2,3."""
    sigma = get_sigma_matrices()
    bar_sigma = get_bar_sigma_matrices()
    
    # bar_sigma_0 = sigma_0
    assert bar_sigma[0] == sigma[0], "bar_sigma_0 should equal sigma_0"
    
    # bar_sigma_i = -sigma_i for i=1,2,3
    for i in range(1, 4):
        assert bar_sigma[i] == -sigma[i], f"bar_sigma_{i} should equal -sigma_{i}"
    
    print("✓ Bar sigma sign flips verified")


def test_clifford_relations_all():
    """Test all Clifford relations."""
    clifford_results = verify_clifford_relations()
    
    all_pass = all(passes for _, passes in clifford_results.values())
    
    assert all_pass, "Not all Clifford relations passed"
    print("✓ All Clifford relations verified")


def test_clifford_relation_00():
    """Test specific Clifford relation: σ_0 σ̄_0 + σ_0 σ̄_0 = 2I."""
    sigma = get_sigma_matrices()
    bar_sigma = get_bar_sigma_matrices()
    I2 = eye(2)
    
    lhs = sigma[0] * bar_sigma[0] + sigma[0] * bar_sigma[0]
    rhs = 2 * I2  # eta_00 = 1
    
    diff = simplify(lhs - rhs)
    assert diff == Matrix.zeros(2, 2), "Clifford relation (0,0) failed"
    print("✓ Clifford (0,0) verified")


def test_clifford_relation_11():
    """Test specific Clifford relation: σ_1 σ̄_1 + σ_1 σ̄_1 = -2I."""
    sigma = get_sigma_matrices()
    bar_sigma = get_bar_sigma_matrices()
    I2 = eye(2)
    
    lhs = sigma[1] * bar_sigma[1] + sigma[1] * bar_sigma[1]
    rhs = 2 * (-1) * I2  # eta_11 = -1
    
    diff = simplify(lhs - rhs)
    assert diff == Matrix.zeros(2, 2), "Clifford relation (1,1) failed"
    print("✓ Clifford (1,1) verified")


def test_clifford_relation_01():
    """Test specific Clifford relation: σ_0 σ̄_1 + σ_1 σ̄_0 = 0."""
    sigma = get_sigma_matrices()
    bar_sigma = get_bar_sigma_matrices()
    
    lhs = sigma[0] * bar_sigma[1] + sigma[1] * bar_sigma[0]
    rhs = Matrix.zeros(2, 2)  # eta_01 = 0
    
    diff = simplify(lhs - rhs)
    assert diff == Matrix.zeros(2, 2), "Clifford relation (0,1) failed"
    print("✓ Clifford (0,1) verified")


def test_determinant_symbolic():
    """Test determinant equals Minkowski interval symbolically."""
    t, x, y, z = symbols('t x y z', real=True)
    det_X, interval_sq, diff = verify_determinant_minkowski_form(t, x, y, z)
    
    assert diff == 0, "Determinant does not match Minkowski interval"
    print("✓ det(X) = Minkowski interval (symbolic)")


def test_determinant_numeric_timelike():
    """Test determinant for a timelike point."""
    # Timelike: t² > |x|²
    x0, x1, x2, x3 = 2, 1, 0, 0
    det_X, interval_sq, diff = verify_determinant_minkowski_form(x0, x1, x2, x3)
    
    assert abs(complex(diff)) < 1e-10, "Determinant mismatch for timelike point"
    assert complex(interval_sq) > 0, "Timelike point should have positive interval"
    print("✓ Timelike point: det(X) = interval² > 0")


def test_determinant_numeric_spacelike():
    """Test determinant for a spacelike point."""
    # Spacelike: t² < |x|²
    x0, x1, x2, x3 = 1, 2, 0, 0
    det_X, interval_sq, diff = verify_determinant_minkowski_form(x0, x1, x2, x3)
    
    assert abs(complex(diff)) < 1e-10, "Determinant mismatch for spacelike point"
    assert complex(interval_sq) < 0, "Spacelike point should have negative interval"
    print("✓ Spacelike point: det(X) = interval² < 0")


def test_null_vector_determinant():
    """Test null vector gives det(X) = 0."""
    assert verify_null_vector_determinant(), "Null vector test failed"
    print("✓ Null vector: det(X) = 0")


def test_null_vector_rank():
    """Test null vector matrix has rank 1."""
    x0, x1, x2, x3 = get_null_vector_example()
    X = compute_X_from_coordinates(x0, x1, x2, x3)
    
    rank = X.rank()
    assert rank == 1, f"Null vector matrix should have rank 1, got {rank}"
    print("✓ Null vector matrix has rank 1")


def test_X_is_hermitian():
    """Test that X is Hermitian for real coordinates."""
    t, x, y, z = symbols('t x y z', real=True)
    assert verify_hermiticity_of_X(t, x, y, z), "X is not Hermitian"
    print("✓ X is Hermitian for real coordinates")


def test_X_numeric_hermitian():
    """Test X is Hermitian numerically."""
    x0, x1, x2, x3 = 1.5, 0.5, -1.0, 2.0
    X = compute_X_from_coordinates(x0, x1, x2, x3)
    X_dag = X.H
    
    diff = simplify(X - X_dag)
    assert diff == Matrix.zeros(2, 2), "X is not Hermitian numerically"
    print("✓ X is Hermitian (numeric test)")


def test_sigma_matrices_are_hermitian():
    """Test that sigma matrices are Hermitian."""
    sigma = get_sigma_matrices()
    
    for i, sig in enumerate(sigma):
        sig_dag = sig.H
        diff = simplify(sig - sig_dag)
        assert diff == Matrix.zeros(2, 2), f"sigma_{i} is not Hermitian"
    
    print("✓ All sigma matrices are Hermitian")


def test_minkowski_metric_signature():
    """Test Minkowski metric has correct signature."""
    eta = minkowski_metric()
    
    # Check diagonal
    assert eta[0, 0] == 1, "eta_00 should be +1"
    assert eta[1, 1] == -1, "eta_11 should be -1"
    assert eta[2, 2] == -1, "eta_22 should be -1"
    assert eta[3, 3] == -1, "eta_33 should be -1"
    
    # Check off-diagonal are zero
    for i in range(4):
        for j in range(4):
            if i != j:
                assert eta[i, j] == 0, f"eta_{i}{j} should be 0"
    
    print("✓ Minkowski metric has signature (+---)")


def test_origin_point():
    """Test origin point X = 0."""
    x0, x1, x2, x3 = 0, 0, 0, 0
    X = compute_X_from_coordinates(x0, x1, x2, x3)
    
    assert X == Matrix.zeros(2, 2), "Origin should give zero matrix"
    print("✓ Origin gives zero matrix")


def test_time_axis_point():
    """Test point on time axis (t, 0, 0, 0)."""
    x0, x1, x2, x3 = 1, 0, 0, 0
    X = compute_X_from_coordinates(x0, x1, x2, x3)
    
    # Should be proportional to identity
    I2 = eye(2)
    assert simplify(X - x0 * I2) == Matrix.zeros(2, 2), "Time axis point failed"
    print("✓ Time axis point: X = t I")


def run_all_tests():
    """Run all UBT generator tests."""
    print("=" * 70)
    print("UBT GENERATORS AND CLIFFORD RELATIONS TESTS")
    print("=" * 70)
    print()
    
    tests = [
        test_biquaternion_basis_size,
        test_biquaternion_basis_are_2x2,
        test_pauli_relations,
        test_sigma_i_squared,
        test_sigma_commutation,
        test_sigma_matrices_count,
        test_sigma_0_is_identity,
        test_bar_sigma_spatial_sign_flip,
        test_clifford_relations_all,
        test_clifford_relation_00,
        test_clifford_relation_11,
        test_clifford_relation_01,
        test_determinant_symbolic,
        test_determinant_numeric_timelike,
        test_determinant_numeric_spacelike,
        test_null_vector_determinant,
        test_null_vector_rank,
        test_X_is_hermitian,
        test_X_numeric_hermitian,
        test_sigma_matrices_are_hermitian,
        test_minkowski_metric_signature,
        test_origin_point,
        test_time_axis_point,
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
    print("ALL UBT GENERATOR TESTS PASSED")
    print("=" * 70)


if __name__ == '__main__':
    run_all_tests()
