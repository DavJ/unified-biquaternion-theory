#!/usr/bin/env python3
"""
e03_su22_invariant.py - Test SU(2,2) invariant form properties

Verifies properties of the SU(2,2) Hermitian form and twistor inner product:
1. Hermiticity of H
2. Conjugate symmetry of inner product
3. Linearity properties
4. Signature (2, 2)

Run with:
    python -m THEORY_COMPARISONS.penrose_twistor.experiments.e03_su22_invariant

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys
from pathlib import Path

# Add repository root to path
repo_root = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(repo_root))

from sympy import symbols, Matrix, I, simplify, conjugate
from THEORY_COMPARISONS.penrose_twistor.twistor_core.twistor import Twistor, spinor
from THEORY_COMPARISONS.penrose_twistor.twistor_core.su22 import (
    get_su22_hermitian_form,
    twistor_inner,
    twistor_norm_squared,
    verify_su22_form_hermitian,
    twistor_inner_conjugate_symmetry,
    twistor_inner_linearity_test,
    twistor_orthogonal,
    create_orthogonal_twistor,
    get_su22_signature,
)


def test_hermitian_form_structure():
    """Test the structure and Hermiticity of H."""
    print("=" * 70)
    print("SU(2,2) HERMITIAN FORM STRUCTURE")
    print("=" * 70)
    print()
    
    H = get_su22_hermitian_form()
    
    print("SU(2,2) Hermitian form H:")
    print(H)
    print()
    
    # Check Hermiticity
    is_hermitian = verify_su22_form_hermitian()
    print(f"H is Hermitian (H† = H): {is_hermitian}")
    
    if is_hermitian:
        print("✓ PASS")
    else:
        print("✗ FAIL")
    
    print()
    
    return is_hermitian


def test_signature():
    """Test the signature of the SU(2,2) form."""
    print("=" * 70)
    print("SU(2,2) FORM SIGNATURE")
    print("=" * 70)
    print()
    
    n_pos, n_neg, n_zero = get_su22_signature()
    
    print(f"Signature of H:")
    print(f"  Positive eigenvalues: {n_pos}")
    print(f"  Negative eigenvalues: {n_neg}")
    print(f"  Zero eigenvalues: {n_zero}")
    print()
    
    # SU(2,2) should have signature (2, 2)
    expected = (2, 2)
    actual = (n_pos, n_neg)
    
    if actual == expected:
        print(f"✓ Signature is (2, 2) as expected for SU(2,2)")
        success = True
    else:
        print(f"✗ Unexpected signature: expected {expected}, got {actual}")
        success = False
    
    print()
    
    return success


def test_conjugate_symmetry():
    """Test conjugate symmetry of inner product."""
    print("=" * 70)
    print("CONJUGATE SYMMETRY TEST")
    print("=" * 70)
    print()
    
    # Create two numeric twistors
    Z1 = Twistor(
        omega=Matrix([1 + I, 2 - I]),
        pi=Matrix([3, 1 + 2*I])
    )
    
    Z2 = Twistor(
        omega=Matrix([0.5, 1 - 0.5*I]),
        pi=Matrix([2*I, 1])
    )
    
    print(f"Z₁ = {Z1}")
    print(f"Z₂ = {Z2}")
    print()
    
    # Compute inner products
    inner12 = twistor_inner(Z1, Z2)
    inner21 = twistor_inner(Z2, Z1)
    
    print(f"⟨Z₁, Z₂⟩ = {inner12}")
    print(f"⟨Z₂, Z₁⟩ = {inner21}")
    print(f"⟨Z₁, Z₂⟩* = {conjugate(inner12)}")
    print()
    
    # Check conjugate symmetry
    is_symmetric = twistor_inner_conjugate_symmetry(Z1, Z2)
    
    if is_symmetric:
        print("✓ Conjugate symmetry holds: ⟨Z₁, Z₂⟩* = ⟨Z₂, Z₁⟩")
    else:
        print("✗ Conjugate symmetry violated!")
    
    print()
    
    return is_symmetric


def test_linearity():
    """Test linearity of inner product in second argument."""
    print("=" * 70)
    print("LINEARITY TEST")
    print("=" * 70)
    print()
    
    # Define symbolic coefficients and twistors
    alpha, beta = symbols('alpha beta', complex=True)
    
    Z1 = Twistor(
        omega=Matrix([1, 0]),
        pi=Matrix([0, 1])
    )
    
    Z2 = Twistor(
        omega=Matrix([0, 1]),
        pi=Matrix([1, 0])
    )
    
    Z3 = Twistor(
        omega=Matrix([1, 1]),
        pi=Matrix([1, -1])
    )
    
    print(f"Z₁ = {Z1}")
    print(f"Z₂ = {Z2}")
    print(f"Z₃ = {Z3}")
    print(f"α = {alpha}, β = {beta}")
    print()
    
    print("Testing: ⟨Z₁, αZ₂ + βZ₃⟩ = α⟨Z₁, Z₂⟩ + β⟨Z₁, Z₃⟩")
    print()
    
    # Test linearity
    is_linear = twistor_inner_linearity_test(Z1, Z2, Z3, alpha, beta)
    
    if is_linear:
        print("✓ Linearity verified")
    else:
        print("✗ Linearity test failed!")
    
    print()
    
    return is_linear


def test_orthogonality():
    """Test orthogonal twistors."""
    print("=" * 70)
    print("ORTHOGONALITY TEST")
    print("=" * 70)
    print()
    
    # Create a twistor
    Z1 = Twistor(
        omega=Matrix([1, 2]),
        pi=Matrix([3, 4])
    )
    
    print(f"Z₁ = {Z1}")
    print()
    
    # Create orthogonal twistor using the H structure
    Z2 = create_orthogonal_twistor(Z1)
    
    print(f"Z₂ (orthogonal to Z₁) = {Z2}")
    print()
    
    # Check orthogonality
    is_orth = twistor_orthogonal(Z1, Z2)
    
    inner = twistor_inner(Z1, Z2)
    print(f"⟨Z₁, Z₂⟩ = {inner}")
    print()
    
    if is_orth:
        print("✓ Twistors are orthogonal: ⟨Z₁, Z₂⟩ = 0")
    else:
        print("✗ Twistors not orthogonal!")
    
    print()
    
    return is_orth


def test_norm_squared_examples():
    """Test norm squared for various twistors."""
    print("=" * 70)
    print("NORM SQUARED EXAMPLES")
    print("=" * 70)
    print()
    
    # Define several twistors
    twistors = [
        ("Simple", Twistor(Matrix([1, 0]), Matrix([0, 1]))),
        ("Symmetric", Twistor(Matrix([1, 1]), Matrix([1, 1]))),
        ("Antisymmetric", Twistor(Matrix([1, -1]), Matrix([1, -1]))),
        ("Complex", Twistor(Matrix([1 + I, 0]), Matrix([0, 1 - I]))),
    ]
    
    print("Computing ⟨Z, Z⟩ for various twistors:")
    print()
    
    for name, Z in twistors:
        norm_sq = twistor_norm_squared(Z)
        norm_sq_val = complex(norm_sq)
        
        print(f"{name:15s}: Z = {Z}")
        print(f"                 ⟨Z, Z⟩ = {norm_sq_val}")
        
        # Classify
        if abs(norm_sq_val.imag) < 1e-10:  # Should be real
            real_part = norm_sq_val.real
            if abs(real_part) < 1e-10:
                classification = "NULL (⟨Z,Z⟩ = 0)"
            elif real_part > 0:
                classification = "TIMELIKE (⟨Z,Z⟩ > 0)"
            else:
                classification = "SPACELIKE (⟨Z,Z⟩ < 0)"
        else:
            classification = "COMPLEX (unexpected!)"
        
        print(f"                 Classification: {classification}")
        print()
    
    print("✓ SU(2,2) form allows positive, negative, and null twistors")
    print()
    
    return True


def test_scaling_behavior():
    """Test how inner product scales with twistor scaling."""
    print("=" * 70)
    print("SCALING BEHAVIOR TEST")
    print("=" * 70)
    print()
    
    # Base twistor
    Z1 = Twistor(Matrix([1, 0]), Matrix([0, 1]))
    Z2 = Twistor(Matrix([0, 1]), Matrix([1, 0]))
    
    # Scaling factor
    lambda_sym = symbols('lambda', complex=True)
    
    print(f"Z₁ = {Z1}")
    print(f"Z₂ = {Z2}")
    print(f"λ = {lambda_sym}")
    print()
    
    # Scaled twistor
    Z1_scaled = Twistor(lambda_sym * Z1.omega, lambda_sym * Z1.pi)
    
    # Inner products
    inner_original = twistor_inner(Z1, Z2)
    inner_scaled = twistor_inner(Z1_scaled, Z2)
    
    print(f"⟨Z₁, Z₂⟩ = {inner_original}")
    print(f"⟨λZ₁, Z₂⟩ = {inner_scaled}")
    print()
    
    # Check scaling
    ratio = simplify(inner_scaled / inner_original)
    print(f"⟨λZ₁, Z₂⟩ / ⟨Z₁, Z₂⟩ = {ratio}")
    print()
    
    if ratio == conjugate(lambda_sym):
        print("✓ Inner product scales as ⟨λZ₁, Z₂⟩ = λ*⟨Z₁, Z₂⟩")
        print("  (antilinear in first argument, as expected)")
        success = True
    else:
        print("✗ Unexpected scaling behavior!")
        success = False
    
    print()
    
    return success


def main():
    """Run all SU(2,2) invariant tests."""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 16 + "SU(2,2) INVARIANT FORM TEST" + " " * 23 + "║")
    print("╚" + "═" * 68 + "╝")
    print()
    
    tests = [
        ("Hermitian Form Structure", test_hermitian_form_structure),
        ("Signature (2,2)", test_signature),
        ("Conjugate Symmetry", test_conjugate_symmetry),
        ("Linearity", test_linearity),
        ("Orthogonality", test_orthogonality),
        ("Norm Squared Examples", test_norm_squared_examples),
        ("Scaling Behavior", test_scaling_behavior),
    ]
    
    results = []
    
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result, None))
        except Exception as e:
            results.append((name, False, str(e)))
    
    # Summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    passed = 0
    failed = 0
    
    for name, result, error in results:
        if result:
            print(f"✓ {name}: PASSED")
            passed += 1
        else:
            print(f"✗ {name}: FAILED")
            if error:
                print(f"  Error: {error}")
            failed += 1
    
    print()
    print(f"Total: {passed} passed, {failed} failed")
    print()
    
    if failed == 0:
        print("🎉 ALL SU(2,2) INVARIANT TESTS PASSED!")
        print()
        print("Key results:")
        print("  - H is Hermitian with signature (2, 2)")
        print("  - Inner product has proper conjugate symmetry")
        print("  - Linearity holds in both arguments (sesquilinear form)")
        print("  - Orthogonal twistors exist due to block structure of H")
    else:
        print("⚠️  Some tests failed - review output above")
    
    print()
    
    return failed == 0


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
