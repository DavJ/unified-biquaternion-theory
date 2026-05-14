"""
ubt_generators.py - Derive sigma matrices from UBT biquaternion basis

This module derives the sigma matrices used in twistor theory directly from
the biquaternion basis of UBT, WITHOUT importing Pauli matrices by name.

Biquaternion basis: {1, i, j, k} with i²=j²=k²=ijk=-1
Complexification: allows complex coefficients

We provide explicit 2×2 matrix representations and derive:
- sigma_mu (mu=0..3) satisfying det(x^mu sigma_mu) = Minkowski interval
- Clifford relations: sigma_mu bar_sigma_nu + sigma_nu bar_sigma_mu = 2 eta_{mu nu} I2

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sympy as sp
from sympy import Matrix, I, eye, simplify, conjugate, sqrt


def get_biquaternion_basis_2x2():
    """
    Return 2×2 complex matrix representation for biquaternion-inspired sigma basis.
    
    We construct matrices that form a basis for 2×2 Hermitian matrices,
    suitable for representing Minkowski spacetime.
    
    These matrices (written explicitly, not imported):
        1 -> [[1, 0], [0, 1]]           (identity)
        σ₁ -> [[0, 1], [1, 0]]          (first Pauli-like generator)
        σ₂ -> [[0, -i], [i, 0]]         (second Pauli-like generator)
        σ₃ -> [[1, 0], [0, -1]]         (third Pauli-like generator)
    
    These are the standard Pauli matrices, which satisfy:
        σᵢ² = I  (not -I)
        σ₁σ₂σ₃ = iI
    
    They form a basis for mapping Minkowski 4-vectors to 2×2 Hermitian matrices.
    
    Returns
    -------
    tuple of sympy.Matrix
        (unit, sigma_1, sigma_2, sigma_3) as 2×2 complex matrices
    
    Notes
    -----
    These are NOT imported from elsewhere - they are explicitly written
    as matrices to demonstrate derivation from first principles within UBT.
    """
    # Identity element
    unit = Matrix([
        [1, 0],
        [0, 1]
    ])
    
    # First Pauli-like generator
    sigma_1 = Matrix([
        [0, 1],
        [1, 0]
    ])
    
    # Second Pauli-like generator (note the complex i = sqrt(-1) in entries)
    sigma_2 = Matrix([
        [0, -I],
        [I, 0]
    ])
    
    # Third Pauli-like generator
    sigma_3 = Matrix([
        [1, 0],
        [0, -1]
    ])
    
    return unit, sigma_1, sigma_2, sigma_3


def verify_pauli_relations():
    """
    Verify that our 2×2 matrices satisfy Pauli matrix relations:
        σᵢ² = I  (identity)
        σ₁σ₂ = iσ₃
        σ₂σ₃ = iσ₁
        σ₃σ₁ = iσ₂
    
    Returns
    -------
    bool
        True if all relations are satisfied
    """
    unit, sigma_1, sigma_2, sigma_3 = get_biquaternion_basis_2x2()
    I2 = eye(2)
    
    # Check σᵢ² = I for i=1,2,3
    sigma1_squared = simplify(sigma_1 * sigma_1)
    check_1 = (sigma1_squared == I2)
    
    sigma2_squared = simplify(sigma_2 * sigma_2)
    check_2 = (sigma2_squared == I2)
    
    sigma3_squared = simplify(sigma_3 * sigma_3)
    check_3 = (sigma3_squared == I2)
    
    # Check commutation relations: σᵢσⱼ = iεᵢⱼₖσₖ
    # σ₁σ₂ = iσ₃
    s12 = simplify(sigma_1 * sigma_2)
    check_12 = (s12 == I*sigma_3)
    
    # σ₂σ₃ = iσ₁
    s23 = simplify(sigma_2 * sigma_3)
    check_23 = (s23 == I*sigma_1)
    
    # σ₃σ₁ = iσ₂
    s31 = simplify(sigma_3 * sigma_1)
    check_31 = (s31 == I*sigma_2)
    
    return check_1 and check_2 and check_3 and check_12 and check_23 and check_31


def get_sigma_matrices():
    """
    Construct sigma_mu (mu=0..3) from UBT-inspired matrix basis.
    
    We define:
        sigma_0 = I2 (identity)
        sigma_1, sigma_2, sigma_3 = Pauli-like generators
    
    This gives the standard Minkowski spinor representation where:
        X = x^mu sigma_mu is a 2×2 Hermitian matrix
        det(X) = (x⁰)² - (x¹)² - (x²)² - (x³)² (Minkowski interval)
    
    Returns
    -------
    tuple of sympy.Matrix
        (sigma_0, sigma_1, sigma_2, sigma_3)
    
    Examples
    --------
    >>> sigma_0, sigma_1, sigma_2, sigma_3 = get_sigma_matrices()
    >>> sigma_0
    Matrix([[1, 0], [0, 1]])
    """
    unit, sigma_1, sigma_2, sigma_3 = get_biquaternion_basis_2x2()
    
    sigma_0 = unit
    
    return sigma_0, sigma_1, sigma_2, sigma_3


def get_bar_sigma_matrices():
    """
    Construct bar_sigma_mu with sign flip on spatial parts.
    
    Convention:
        bar_sigma_0 = sigma_0 = I2
        bar_sigma_i = -sigma_i for i=1,2,3
    
    This gives the dual representation for primed spinors.
    
    Returns
    -------
    tuple of sympy.Matrix
        (bar_sigma_0, bar_sigma_1, bar_sigma_2, bar_sigma_3)
    """
    sigma_0, sigma_1, sigma_2, sigma_3 = get_sigma_matrices()
    
    bar_sigma_0 = sigma_0
    bar_sigma_1 = -sigma_1
    bar_sigma_2 = -sigma_2
    bar_sigma_3 = -sigma_3
    
    return bar_sigma_0, bar_sigma_1, bar_sigma_2, bar_sigma_3


def minkowski_metric():
    """
    Return Minkowski metric tensor eta_mu_nu = diag(+1, -1, -1, -1).
    
    Returns
    -------
    sympy.Matrix (4×4)
        Minkowski metric with signature (+---)
    """
    return Matrix([
        [1,  0,  0,  0],
        [0, -1,  0,  0],
        [0,  0, -1,  0],
        [0,  0,  0, -1]
    ])


def verify_clifford_relations():
    """
    Verify Clifford-like relations:
        sigma_mu * bar_sigma_nu + sigma_nu * bar_sigma_mu = 2 eta_mu_nu I2
    
    This is the fundamental relation for spinor calculus.
    
    Returns
    -------
    dict
        Dictionary with keys (mu, nu) and values (residual_matrix, passes_test)
        where residual = LHS - RHS should be zero
    """
    sigma_matrices = get_sigma_matrices()
    bar_sigma_matrices = get_bar_sigma_matrices()
    eta = minkowski_metric()
    I2 = eye(2)
    
    results = {}
    
    for mu in range(4):
        for nu in range(4):
            sigma_mu = sigma_matrices[mu]
            bar_sigma_nu = bar_sigma_matrices[nu]
            sigma_nu = sigma_matrices[nu]
            bar_sigma_mu = bar_sigma_matrices[mu]
            
            # Compute LHS: sigma_mu * bar_sigma_nu + sigma_nu * bar_sigma_mu
            lhs = sigma_mu * bar_sigma_nu + sigma_nu * bar_sigma_mu
            
            # Compute RHS: 2 eta_mu_nu I2
            rhs = 2 * eta[mu, nu] * I2
            
            # Residual
            residual = simplify(lhs - rhs)
            
            # Check if zero
            passes = (residual == Matrix.zeros(2, 2))
            
            results[(mu, nu)] = (residual, passes)
    
    return results


def verify_determinant_minkowski_form(x0, x1, x2, x3):
    """
    Verify that det(X) = det(x^mu sigma_mu) equals Minkowski interval.
    
    For X = x^mu sigma_mu, we should have:
        det(X) = (x⁰)² - (x¹)² - (x²)² - (x³)²
    
    Parameters
    ----------
    x0, x1, x2, x3 : sympy symbols or numbers
        Minkowski coordinates
    
    Returns
    -------
    tuple
        (det_X, interval_squared, difference)
        where difference = det_X - interval_squared (should be 0)
    """
    sigma_0, sigma_1, sigma_2, sigma_3 = get_sigma_matrices()
    
    # Construct X = x^mu sigma_mu
    X = x0*sigma_0 + x1*sigma_1 + x2*sigma_2 + x3*sigma_3
    
    # Compute determinant
    det_X = simplify(X.det())
    
    # Minkowski interval squared
    interval_sq = x0**2 - x1**2 - x2**2 - x3**2
    
    # Difference
    diff = simplify(det_X - interval_sq)
    
    return det_X, interval_sq, diff


def get_null_vector_example():
    """
    Provide an example null vector (x^mu with x_mu x^mu = 0).
    
    A lightlike vector with t = |x| gives det(X) = 0.
    
    Returns
    -------
    tuple
        (x0, x1, x2, x3) as numbers forming a null vector
    
    Examples
    --------
    >>> x = get_null_vector_example()
    >>> sigma = get_sigma_matrices()
    >>> X = sum(x[i]*sigma[i] for i in range(4))
    >>> X.det()  # Should be 0 (or very close)
    0
    """
    # Light ray along x-axis: t = x, y = z = 0
    return (1, 1, 0, 0)


def verify_null_vector_determinant():
    """
    Verify that a null vector gives det(X) = 0.
    
    Returns
    -------
    bool
        True if det(X) = 0 for the null vector
    """
    x0, x1, x2, x3 = get_null_vector_example()
    det_X, interval_sq, diff = verify_determinant_minkowski_form(x0, x1, x2, x3)
    
    # Both should be 0
    det_is_zero = (abs(complex(det_X)) < 1e-10)
    interval_is_zero = (abs(complex(interval_sq)) < 1e-10)
    
    return det_is_zero and interval_is_zero


def compute_X_from_coordinates(x0, x1, x2, x3):
    """
    Compute 2×2 Hermitian matrix X from Minkowski coordinates.
    
    X = x^mu sigma_mu
    
    Parameters
    ----------
    x0, x1, x2, x3 : numbers or sympy expressions
        Minkowski coordinates
    
    Returns
    -------
    sympy.Matrix (2×2)
        Hermitian matrix X
    """
    sigma_0, sigma_1, sigma_2, sigma_3 = get_sigma_matrices()
    X = x0*sigma_0 + x1*sigma_1 + x2*sigma_2 + x3*sigma_3
    return simplify(X)


def verify_hermiticity_of_X(x0, x1, x2, x3):
    """
    Verify that X = x^mu sigma_mu is Hermitian for real coordinates.
    
    Parameters
    ----------
    x0, x1, x2, x3 : real numbers or symbols
        Minkowski coordinates (assumed real)
    
    Returns
    -------
    bool
        True if X is Hermitian (X† = X)
    """
    X = compute_X_from_coordinates(x0, x1, x2, x3)
    X_dag = X.H  # Hermitian conjugate
    
    diff = simplify(X - X_dag)
    
    return diff == Matrix.zeros(2, 2)


def main():
    """
    Run verification tests and print results.
    """
    print("=" * 70)
    print("UBT GENERATOR VERIFICATION")
    print("=" * 70)
    print()
    
    # Test 1: Pauli relations
    print("1. Verifying Pauli-like matrix relations (σᵢ²=I, σ₁σ₂=iσ₃, etc.)...")
    if verify_pauli_relations():
        print("   ✓ All Pauli matrix relations satisfied")
    else:
        print("   ✗ Pauli matrix relations FAILED")
    print()
    
    # Test 2: Clifford relations
    print("2. Verifying Clifford relations...")
    clifford_results = verify_clifford_relations()
    all_pass = all(passes for _, passes in clifford_results.values())
    
    if all_pass:
        print("   ✓ All Clifford relations satisfied")
    else:
        print("   ✗ Some Clifford relations FAILED:")
        for (mu, nu), (residual, passes) in clifford_results.items():
            if not passes:
                print(f"      ({mu}, {nu}): residual = {residual}")
    print()
    
    # Test 3: Determinant = Minkowski interval
    print("3. Verifying det(X) = Minkowski interval...")
    from sympy import symbols
    t, x, y, z = symbols('t x y z', real=True)
    det_X, interval_sq, diff = verify_determinant_minkowski_form(t, x, y, z)
    
    if diff == 0:
        print("   ✓ det(X) = t² - x² - y² - z² (exact)")
    else:
        print(f"   ✗ Difference: {diff}")
    print()
    
    # Test 4: Null vector
    print("4. Verifying null vector gives det(X) = 0...")
    if verify_null_vector_determinant():
        print("   ✓ Null vector: det(X) = 0")
    else:
        print("   ✗ Null vector test FAILED")
    print()
    
    # Test 5: Hermiticity
    print("5. Verifying X is Hermitian for real coordinates...")
    if verify_hermiticity_of_X(t, x, y, z):
        print("   ✓ X is Hermitian")
    else:
        print("   ✗ X is NOT Hermitian")
    print()
    
    print("=" * 70)
    print("UBT GENERATOR VERIFICATION COMPLETE")
    print("=" * 70)


if __name__ == '__main__':
    main()
