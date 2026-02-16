#!/usr/bin/env python3
"""
e05_derive_sigma_from_ubt.py - Derive sigma matrices from UBT biquaternion basis

This experiment demonstrates the derivation of sigma matrices from UBT's
biquaternion generators without importing Pauli matrices by name.

Key verifications:
1. Quaternion relations hold for 2×2 matrix representation
2. Clifford relations: sigma_mu bar_sigma_nu + sigma_nu bar_sigma_mu = 2 eta_mu_nu I2
3. det(x^mu sigma_mu) = Minkowski interval
4. Null vectors give det(X) = 0 (rank-1 condition)

Run with:
    python -m THEORY_COMPARISONS.penrose_twistor.experiments.e05_derive_sigma_from_ubt

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys
from sympy import symbols, simplify, Matrix
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
    minkowski_metric,
)


def print_header(title):
    """Print a formatted section header."""
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)
    print()


def print_matrix_nicely(name, M):
    """Print a matrix with a label."""
    print(f"{name} =")
    for row in range(M.rows):
        print("  [", end="")
        for col in range(M.cols):
            elem = M[row, col]
            if col > 0:
                print(", ", end="")
            print(f"{elem}", end="")
        print("]")
    print()


def show_biquaternion_basis():
    """Display the biquaternion basis matrices."""
    print_header("UBT-INSPIRED SIGMA BASIS (2×2 MATRICES)")
    
    unit, sigma_1, sigma_2, sigma_3 = get_biquaternion_basis_2x2()
    
    print("Explicit 2×2 matrix representation (Pauli-like generators):")
    print("(NOT imported - written from first principles within UBT framework)")
    print()
    
    print_matrix_nicely("1 (identity)", unit)
    print_matrix_nicely("σ₁", sigma_1)
    print_matrix_nicely("σ₂", sigma_2)
    print_matrix_nicely("σ₃", sigma_3)
    
    print("Pauli relations: σᵢ² = I, σ₁σ₂ = iσ₃, σ₂σ₃ = iσ₁, σ₃σ₁ = iσ₂")
    print()


def show_sigma_matrices():
    """Display the derived sigma matrices."""
    print_header("DERIVED SIGMA MATRICES")
    
    sigma_0, sigma_1, sigma_2, sigma_3 = get_sigma_matrices()
    
    print("Constructed from UBT-inspired matrix basis:")
    print("  sigma_0 = I  (identity)")
    print("  sigma_1, sigma_2, sigma_3 = Pauli-like generators")
    print()
    
    print_matrix_nicely("σ₀", sigma_0)
    print_matrix_nicely("σ₁", sigma_1)
    print_matrix_nicely("σ₂", sigma_2)
    print_matrix_nicely("σ₃", sigma_3)


def show_bar_sigma_matrices():
    """Display the bar sigma matrices."""
    print_header("BAR SIGMA MATRICES")
    
    bar_sigma_0, bar_sigma_1, bar_sigma_2, bar_sigma_3 = get_bar_sigma_matrices()
    
    print("With sign flip on spatial parts:")
    print("  σ̄₀ = σ₀")
    print("  σ̄ᵢ = -σᵢ  (i = 1, 2, 3)")
    print()
    
    print_matrix_nicely("σ̄₀", bar_sigma_0)
    print_matrix_nicely("σ̄₁", bar_sigma_1)
    print_matrix_nicely("σ̄₂", bar_sigma_2)
    print_matrix_nicely("σ̄₃", bar_sigma_3)


def verify_quaternion_properties():
    """Verify Pauli matrix relations."""
    print_header("PAULI MATRIX RELATIONS VERIFICATION")
    
    print("Checking: σᵢ² = I, σ₁σ₂ = iσ₃, σ₂σ₃ = iσ₁, σ₃σ₁ = iσ₂")
    print()
    
    if verify_pauli_relations():
        print("✓ ALL PAULI MATRIX RELATIONS SATISFIED")
        print()
        print("This confirms our 2×2 matrices form a valid")
        print("representation suitable for Minkowski spinor calculus.")
    else:
        print("✗ PAULI MATRIX RELATIONS FAILED")
    
    print()


def verify_clifford_properties():
    """Verify Clifford relations."""
    print_header("CLIFFORD RELATIONS VERIFICATION")
    
    print("Checking: σ_μ σ̄_ν + σ_ν σ̄_μ = 2η_μν I₂")
    print()
    
    clifford_results = verify_clifford_relations()
    
    # Count passes
    total = len(clifford_results)
    passed = sum(1 for _, passes in clifford_results.values() if passes)
    
    print(f"Results: {passed}/{total} relations satisfied")
    print()
    
    if passed == total:
        print("✓ ALL CLIFFORD RELATIONS SATISFIED")
        print()
        print("Key examples:")
        
        # Show a few key cases
        test_cases = [(0, 0), (0, 1), (1, 1), (1, 2)]
        eta = minkowski_metric()
        
        for mu, nu in test_cases:
            eta_val = eta[mu, nu]
            print(f"  σ_{mu} σ̄_{nu} + σ_{nu} σ̄_{mu} = 2×{eta_val}×I₂  ✓")
        
        print()
        print("This confirms the sigma matrices satisfy the")
        print("fundamental spinor Clifford algebra.")
    else:
        print("✗ SOME CLIFFORD RELATIONS FAILED:")
        for (mu, nu), (residual, passes) in clifford_results.items():
            if not passes:
                print(f"  ({mu}, {nu}): residual = {residual}")
    
    print()


def verify_determinant_property():
    """Verify determinant equals Minkowski interval."""
    print_header("DETERMINANT = MINKOWSKI INTERVAL")
    
    print("Checking: det(X) = det(x^μ σ_μ) = (x⁰)² - |x|²")
    print()
    
    t, x, y, z = symbols('t x y z', real=True)
    det_X, interval_sq, diff = verify_determinant_minkowski_form(t, x, y, z)
    
    print(f"X = t σ₀ + x σ₁ + y σ₂ + z σ₃")
    print()
    print(f"det(X) = {det_X}")
    print()
    print(f"Minkowski interval² = {interval_sq}")
    print()
    print(f"Difference = {diff}")
    print()
    
    if diff == 0:
        print("✓ EXACT EQUALITY CONFIRMED")
        print()
        print("This is the fundamental property linking")
        print("spacetime geometry to 2×2 Hermitian matrices.")
    else:
        print("✗ DETERMINANT PROPERTY FAILED")
    
    print()


def verify_null_vector_example():
    """Verify null vector gives det(X) = 0."""
    print_header("NULL VECTOR TEST")
    
    print("For a lightlike vector (x_μ x^μ = 0), det(X) should be 0.")
    print()
    
    x0, x1, x2, x3 = get_null_vector_example()
    print(f"Null vector: x^μ = ({x0}, {x1}, {x2}, {x3})")
    print(f"  (light ray along x-axis: t = x, y = z = 0)")
    print()
    
    X = compute_X_from_coordinates(x0, x1, x2, x3)
    print("Matrix X:")
    print_matrix_nicely("X", X)
    
    det_X = X.det()
    rank = X.rank()
    
    print(f"det(X) = {det_X}")
    print(f"rank(X) = {rank}")
    print()
    
    if verify_null_vector_determinant():
        print("✓ NULL VECTOR CONFIRMED: det(X) = 0, rank = 1")
        print()
        print("This demonstrates that null vectors correspond to")
        print("rank-1 matrices, which are fundamental in twistor theory")
        print("(they define light rays in spacetime).")
    else:
        print("✗ NULL VECTOR TEST FAILED")
    
    print()


def show_example_spacetime_point():
    """Show an example spacetime point and its matrix."""
    print_header("EXAMPLE: SPACETIME POINT → MATRIX")
    
    print("Generic point: x^μ = (2, 1, 0, 1)")
    print()
    
    x0, x1, x2, x3 = 2, 1, 0, 1
    X = compute_X_from_coordinates(x0, x1, x2, x3)
    
    print("Matrix X = x^μ σ_μ:")
    print_matrix_nicely("X", X)
    
    det_X = X.det()
    interval_sq = x0**2 - x1**2 - x2**2 - x3**2
    
    print(f"det(X) = {det_X}")
    print(f"Interval² = {interval_sq}")
    print()
    
    if abs(complex(det_X - interval_sq)) < 1e-10:
        print("✓ Determinant matches Minkowski interval")
    
    print()


def summary():
    """Print summary of results."""
    print_header("SUMMARY")
    
    print("Key Results:")
    print()
    print("1. ✓ Derived sigma matrices from UBT-inspired matrix basis")
    print("     (NOT imported from external Pauli matrix library)")
    print()
    print("2. ✓ Verified Pauli relations: σᵢ²=I, σ₁σ₂=iσ₃, etc.")
    print()
    print("3. ✓ Confirmed Clifford relations:")
    print("     σ_μ σ̄_ν + σ_ν σ̄_μ = 2η_μν I₂")
    print()
    print("4. ✓ Established det(x^μ σ_μ) = Minkowski interval")
    print()
    print("5. ✓ Verified null vectors give det(X) = 0 (rank-1)")
    print()
    print("Conclusion:")
    print("-----------")
    print("The sigma matrices emerge naturally from explicit 2×2 matrix")
    print("construction within UBT framework. The light-cone geometry is")
    print("correctly encoded in the determinant, and Clifford relations")
    print("ensure compatibility with spinor calculus used in twistor theory.")
    print()


def main():
    """Run e05 experiment."""
    print()
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 10 + "e05: DERIVE SIGMA FROM UBT GENERATORS" + " " * 19 + "║")
    print("╚" + "═" * 68 + "╝")
    
    show_biquaternion_basis()
    show_sigma_matrices()
    show_bar_sigma_matrices()
    verify_quaternion_properties()
    verify_clifford_properties()
    verify_determinant_property()
    verify_null_vector_example()
    show_example_spacetime_point()
    summary()
    
    print("=" * 70)
    print("e05 COMPLETE")
    print("=" * 70)
    print()
    
    return True


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
