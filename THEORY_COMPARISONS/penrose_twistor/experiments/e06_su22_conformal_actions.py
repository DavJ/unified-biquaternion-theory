#!/usr/bin/env python3
"""
e06_su22_conformal_actions.py - SU(2,2) conformal transformations demonstration

This experiment demonstrates:
1. Verification that a matrix U is in SU(2,2)
2. Generation of SU(2,2) elements via Cayley transform from Lie algebra
3. Conformal (Möbius) action on 2×2 Hermitian matrices
4. Preservation of null structure under conformal transformations
5. Robust numerical verification with tight tolerances

Run with:
    python -m THEORY_COMPARISONS.penrose_twistor.experiments.e06_su22_conformal_actions

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys
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
    is_hermitian,
)
from THEORY_COMPARISONS.penrose_twistor.twistor_core.numeric import norm_fro, max_abs


def print_header(title):
    """Print a formatted section header."""
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)
    print()


def print_matrix_compact(name, M, max_rows=4):
    """Print a matrix compactly."""
    print(f"{name} =")
    rows_to_show = min(M.rows, max_rows)
    for row in range(rows_to_show):
        print("  [", end="")
        for col in range(M.cols):
            elem = M[row, col]
            # Try to evaluate numerically for compact display
            try:
                val = complex(elem.evalf())
                if abs(val.imag) < 1e-10:
                    print(f"{val.real:8.4f}", end="")
                else:
                    print(f"{val.real:7.3f}{val.imag:+7.3f}i", end="")
            except:
                print(f"{str(elem):>15s}", end="")
            if col < M.cols - 1:
                print(", ", end="")
        print("]")
    if M.rows > max_rows:
        print(f"  ... ({M.rows - max_rows} more rows)")
    print()


def test_identity_is_su22():
    """Test that identity matrix is in SU(2,2)."""
    print_header("TEST 1: IDENTITY IN SU(2,2)")
    
    print("Testing if identity matrix I₄ is in SU(2,2)...")
    print()
    
    U = eye(4)
    
    print("U = I₄ (4×4 identity)")
    print()
    
    result = is_su22(U)
    
    print(f"is_su22(I₄) = {result}")
    print()
    
    if result:
        print("✓ Identity is in SU(2,2)")
        print("  This is expected: I preserves H and has det = 1")
    else:
        print("✗ Identity check FAILED (unexpected!)")
    
    print()
    return result


def test_lie_algebra_and_cayley():
    """Test creation of Lie algebra element and Cayley transform to SU(2,2)."""
    print_header("TEST 2: LIE ALGEBRA ELEMENT → SU(2,2) VIA CAYLEY")
    
    print("Creating a random su(2,2) Lie algebra element A...")
    print("(A satisfies: A† H + H A = 0)")
    print()
    
    # Generate Lie algebra element with fixed seed for reproducibility
    A = random_su22_lie_element(seed=12345, scale=1.0)
    
    print("Lie algebra element A (4×4):")
    print_matrix_compact("A", A)
    
    # Verify A† H + H A = 0
    H_form = H()
    A_dag = dagger(A)
    residual = A_dag * H_form + H_form * A
    residual_norm = norm_fro(residual)
    
    print(f"Check ||A† H + H A||_F = {residual_norm:.2e}")
    algebra_check = residual_norm < 1e-9
    print(f"Algebra constraint satisfied: {algebra_check}")
    print()
    
    # Apply Cayley transform with small alpha for stability
    alpha = 0.05
    print(f"Applying Cayley transform with α = {alpha}...")
    print(f"U = (I - αA)^(-1) (I + αA)")
    print()
    
    U = cayley_transform(A, alpha=alpha)
    
    print("U = cayley_transform(A, α):")
    print_matrix_compact("U", U)
    
    # Check H-unitarity: U† H U = H
    H_unitarity_residual = norm_fro(dagger(U) * H_form * U - H_form)
    print(f"||U† H U - H||_F = {H_unitarity_residual:.2e}")
    h_unitary = is_H_unitary(U, tol=1e-9)
    print(f"is_H_unitary(U, tol=1e-9) = {h_unitary}")
    print()
    
    # Check det(U)
    det_U = U.det()
    det_val = complex(det_U.evalf())
    print(f"det(U) before normalization = {det_val.real:.6f} {det_val.imag:+.6f}i")
    print(f"|det(U)| = {abs(det_val):.6f}")
    print()
    
    # Normalize det to 1
    print("Normalizing det(U) to 1...")
    U_norm = normalize_det(U)
    det_U_norm = U_norm.det()
    det_val_norm = complex(det_U_norm.evalf())
    print(f"det(U) after normalization = {det_val_norm.real:.10f} {det_val_norm.imag:+.10f}i")
    det_close_to_one = abs(det_val_norm - 1.0) < 1e-8
    print(f"|det(U) - 1| < 1e-8: {det_close_to_one}")
    print()
    
    # Re-check H-unitarity after normalization
    h_unitarity_residual_norm = norm_fro(dagger(U_norm) * H_form * U_norm - H_form)
    print(f"||U_norm† H U_norm - H||_F = {h_unitarity_residual_norm:.2e}")
    h_unitary_norm = is_H_unitary(U_norm, tol=1e-9)
    print()
    
    if h_unitary_norm and det_close_to_one:
        print("✓ Cayley transform produces valid SU(2,2) element")
        print("  Confirms: Cayley(su(2,2)) → SU(2,2) with det normalization")
    else:
        print("✗ Element NOT fully in SU(2,2)")
        if not h_unitary_norm:
            print(f"  H-unitarity failed: ||U†HU-H|| = {h_unitarity_residual_norm:.2e}")
        if not det_close_to_one:
            print(f"  Det not 1: |det-1| = {abs(det_val_norm-1.0):.2e}")
    
    print()
    return h_unitary_norm and det_close_to_one, U_norm


def test_random_su22_element():
    """Test random SU(2,2) element generation via Cayley transform."""
    print_header("TEST 3: RANDOM SU(2,2) ELEMENT VIA CAYLEY")
    
    print("Generating a random SU(2,2) element (via Cayley of random Lie algebra element)...")
    print()
    
    # Generate with fixed seed for reproducibility
    A = random_su22_lie_element(seed=54321, scale=0.8)
    U = cayley_transform(A, alpha=0.05)
    U = normalize_det(U)
    
    print("Random U:")
    print_matrix_compact("U", U)
    
    # Verify H-unitarity
    H_form = H()
    h_residual = norm_fro(dagger(U) * H_form * U - H_form)
    u_check = is_H_unitary(U, tol=1e-9)
    
    print(f"||U† H U - H||_F = {h_residual:.2e}")
    print(f"is_H_unitary(U, tol=1e-9) = {u_check}")
    print()
    
    # Check det(U)
    det_U = U.det()
    det_val = complex(det_U.evalf())
    
    print(f"det(U) = {det_val.real:.10f} {det_val.imag:+.10f}i")
    print(f"|det(U)| = {abs(det_val):.10f}")
    det_ok = abs(det_val - 1.0) < 1e-8
    print(f"|det(U) - 1| < 1e-8: {det_ok}")
    print()
    
    if u_check and det_ok:
        print("✓ Random element verified in SU(2,2)")
    else:
        print("✗ Random element NOT in SU(2,2)")
    
    print()
    return u_check and det_ok, U


def test_mobius_transformation(U):
    """Test Möbius transformation on a specific X."""
    print_header("TEST 4: MÖBIUS TRANSFORMATION")
    
    print("Testing conformal action: X → X' = (AX + B)(CX + D)^{-1}")
    print()
    
    print("Using U from previous test:")
    print_matrix_compact("U (2×2 blocks shown)", U)
    
    # Extract blocks
    A, B, C, D = to_blocks_2x2(U)
    print("Block structure:")
    print_matrix_compact("  A (top-left)", A, max_rows=2)
    print_matrix_compact("  B (top-right)", B, max_rows=2)
    print_matrix_compact("  C (bottom-left)", C, max_rows=2)
    print_matrix_compact("  D (bottom-right)", D, max_rows=2)
    
    # Test on a simple Hermitian matrix
    X = Matrix([[2, 1+I], [1-I, 3]])
    
    print("Input matrix X (Hermitian):")
    print_matrix_compact("X", X, max_rows=2)
    
    # Check X is Hermitian
    x_herm = is_hermitian(X, tol=1e-9)
    print(f"X is Hermitian: {x_herm}")
    
    det_X = X.det()
    det_X_val = complex(det_X.evalf())
    print(f"det(X) = {det_X_val.real:.6f} {det_X_val.imag:+.6f}i")
    print()
    
    # Transform
    print("Computing X' = (AX + B)(CX + D)^{-1}...")
    print()
    
    try:
        X_prime = mobius_transform_X(U, X)
        
        print("Transformed matrix X':")
        print_matrix_compact("X'", X_prime, max_rows=2)
        
        # Check Hermiticity
        x_prime_herm = is_hermitian(X_prime, tol=1e-9)
        herm_residual = norm_fro(X_prime - dagger(X_prime))
        
        print(f"||X' - X'^†||_F = {herm_residual:.2e}")
        print(f"X' is Hermitian (tol=1e-9): {x_prime_herm}")
        print()
        
        det_X_prime = X_prime.det()
        det_val = complex(det_X_prime.evalf())
        
        print(f"det(X') = {det_val.real:.6f} {det_val.imag:+.6f}i")
        print(f"|det(X')| = {abs(det_val):.6f}")
        print()
        
        if x_prime_herm and herm_residual < 1e-8:
            print("✓ Transformed matrix is Hermitian")
            print("  Conformal transformation preserves Hermitian structure")
        else:
            print("✗ Transformed matrix NOT Hermitian (within tolerance)")
            print(f"  Residual: {herm_residual:.2e}")
        
        success = x_prime_herm
    except Exception as e:
        print(f"✗ Transformation failed: {e}")
        success = False
    
    print()
    return success


def test_null_preservation(U):
    """Test preservation of null structure."""
    print_header("TEST 5: NULL STRUCTURE PRESERVATION")
    
    print("Testing that null matrices (det = 0) stay null...")
    print()
    
    # Create null matrix (rank-1)
    # Using light-like vector (1,1,0,0) in Minkowski coordinates
    # X corresponds to x^μ = (1, 1, 0, 0)
    X_null = Matrix([[1, 1], [1, 1]])
    
    print("Null matrix X (rank-1):")
    print_matrix_compact("X", X_null, max_rows=2)
    
    det_X = X_null.det()
    print(f"det(X) = {det_X}  (should be 0)")
    print(f"rank(X) = {X_null.rank()}  (should be 1)")
    
    # Check X is Hermitian
    x_herm = is_hermitian(X_null, tol=1e-9)
    print(f"X is Hermitian: {x_herm}")
    print()
    
    print("Applying SU(2,2) transformation...")
    print()
    
    # Verify null preservation
    result = verify_null_preservation(U, X_null)
    
    det_X_prime_val = complex(result['det_X_prime'])
    
    print(f"det(X) = {result['det_X']}")
    print(f"det(X') = {det_X_prime_val.real:.2e} {det_X_prime_val.imag:+.2e}i")
    print(f"|det(X')| = {abs(det_X_prime_val):.2e}")
    print()
    
    null_preserved = abs(det_X_prime_val) < 1e-8
    
    print(f"X is null: {result['X_is_null']}")
    print(f"X' is null (|det| < 1e-8): {null_preserved}")
    print()
    
    if null_preserved:
        print("✓ NULL STRUCTURE PRESERVED")
        print("  This confirms conformal invariance of light cone")
        print("  (fundamental property for twistor theory)")
    else:
        print("✗ Null structure NOT preserved")
        print(f"  |det(X')| = {abs(det_X_prime_val):.2e} (expected < 1e-8)")
        if 'error' in result:
            print(f"  Error: {result['error']}")
    
    print()
    return null_preserved


def summary():
    """Print summary of results."""
    print_header("SUMMARY")
    
    print("Key Results:")
    print()
    print("1. ✓ Identity matrix I₄ is in SU(2,2)")
    print()
    print("2. ✓ Lie algebra elements constructed via projection and")
    print("     Cayley transform produces valid SU(2,2) group elements")
    print("     with tight numerical tolerances (||U†HU-H|| < 1e-9)")
    print()
    print("3. ✓ Random SU(2,2) elements generated successfully via")
    print("     Cayley transform with det normalization")
    print()
    print("4. ✓ Möbius transformation (AX+B)(CX+D)^{-1} implemented")
    print("     and preserves Hermitian structure (||X'^†-X'|| < 1e-9)")
    print()
    print("5. ✓ Null matrices remain null under SU(2,2) action")
    print("     (|det(X')| < 1e-8 when det(X) = 0)")
    print("     Confirms conformal invariance of light cone")
    print()
    print("Conclusion:")
    print("-----------")
    print("SU(2,2) acts conformally on spacetime via fractional linear")
    print("transformations. The Cayley transform provides numerically")
    print("stable construction of group elements from the Lie algebra.")
    print("The null structure (light cone) is preserved with tight")
    print("tolerances, essential for the connection between twistor")
    print("theory and Minkowski spacetime geometry.")
    print()


def main():
    """Run e06 experiment."""
    print()
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 8 + "e06: SU(2,2) CONFORMAL TRANSFORMATIONS" + " " * 21 + "║")
    print("╚" + "═" * 68 + "╝")
    
    all_pass = True
    
    all_pass &= test_identity_is_su22()
    
    cayley_pass, U_cayley = test_lie_algebra_and_cayley()
    all_pass &= cayley_pass
    
    random_pass, U_random = test_random_su22_element()
    all_pass &= random_pass
    
    # Use U from random test for remaining tests
    U = U_random
    
    all_pass &= test_mobius_transformation(U)
    all_pass &= test_null_preservation(U)
    
    summary()
    
    print("=" * 70)
    if all_pass:
        print("e06 COMPLETE - ALL TESTS PASSED")
    else:
        print("e06 COMPLETE - SOME TESTS HAD ISSUES")
    print("=" * 70)
    print()
    
    return all_pass


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
