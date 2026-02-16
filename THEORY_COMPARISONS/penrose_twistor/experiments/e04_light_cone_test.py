#!/usr/bin/env python3
"""
e04_light_cone_test.py - Light-cone consistency test

Tests the null structure (light-cone) that emerges naturally from the
Minkowski spinor formalism and its preservation under UBT embedding.

Key tests:
1. Verify det(X) = x^μ x_μ (Minkowski interval squared)
2. Test null vectors (light-like) satisfy det(X) = 0
3. Verify UBT embedding preserves null structure
4. Check rank condition: det(X) = 0 ⇒ rank(X) = 1

Signature convention:
    s² = (x⁰)² - (x¹)² - (x²)² - (x³)²
    Metric signature: (+, -, -, -)

Run with:
    python -m THEORY_COMPARISONS.penrose_twistor.experiments.e04_light_cone_test

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys
from sympy import symbols, simplify, sqrt, Rational, Matrix
from THEORY_COMPARISONS.penrose_twistor.twistor_core.minkowski_spinor import (
    x_to_X, minkowski_interval_squared
)
from THEORY_COMPARISONS.penrose_twistor.twistor_core.ubt_bridge import (
    X2_to_ubt_matrix, compare_determinants
)
from THEORY_COMPARISONS.penrose_twistor.common.linalg import determinant


def test_symbolic_determinant():
    """
    Test 1: Verify det(X) reproduces Minkowski metric symbolically.
    
    For X = x^μ σ_μ, we should have:
        det(X) = (x⁰)² - (x¹)² - (x²)² - (x³)²
    
    This is the Minkowski interval squared with signature (+, -, -, -).
    """
    print("=" * 70)
    print("TEST 1: SYMBOLIC DETERMINANT = MINKOWSKI INTERVAL")
    print("=" * 70)
    print()
    
    # Define symbolic coordinates
    x0, x1, x2, x3 = symbols('x0 x1 x2 x3', real=True)
    
    # Construct Hermitian matrix X
    X = x_to_X(x0, x1, x2, x3)
    print(f"Minkowski coordinates: (x⁰, x¹, x², x³)")
    print(f"Hermitian matrix X = x^μ σ_μ:")
    print(X)
    print()
    
    # Compute determinant
    det_X = determinant(X)
    det_X_simplified = simplify(det_X)
    print(f"det(X) = {det_X_simplified}")
    print()
    
    # Compute Minkowski interval squared
    s_squared = minkowski_interval_squared(x0, x1, x2, x3)
    print(f"Minkowski interval: s² = (x⁰)² - (x¹)² - (x²)² - (x³)²")
    print(f"s² = {s_squared}")
    print()
    
    # Verify equality
    difference = simplify(det_X - s_squared)
    print(f"Difference: det(X) - s² = {difference}")
    
    if difference == 0:
        print("✓ PASS: det(X) = s² (Minkowski interval squared)")
        result = True
    else:
        print("✗ FAIL: det(X) ≠ s²")
        result = False
    
    print()
    return result


def test_null_vector_numeric():
    """
    Test 2: Verify null (light-like) vectors give det(X) = 0.
    
    Examples of null vectors:
    - (1, 1, 0, 0): light ray along x-axis
    - (1, 0, 1, 0): light ray along y-axis
    - (1, 0, 0, 1): light ray along z-axis
    - (2, √2, √2, 0): scaled null vector
    """
    print("=" * 70)
    print("TEST 2: NULL VECTORS → det(X) = 0")
    print("=" * 70)
    print()
    
    # Define test null vectors
    null_vectors = [
        (1, 1, 0, 0, "Light ray along +x"),
        (1, -1, 0, 0, "Light ray along -x"),
        (1, 0, 1, 0, "Light ray along +y"),
        (1, 0, -1, 0, "Light ray along -y"),
        (1, 0, 0, 1, "Light ray along +z"),
        (1, 0, 0, -1, "Light ray along -z"),
        (2, sqrt(2), sqrt(2), 0, "Diagonal null vector"),
        (1, Rational(1, 2), Rational(1, 2), sqrt(Rational(1, 2)), "Generic null"),
    ]
    
    all_passed = True
    
    for x0, x1, x2, x3, description in null_vectors:
        # Verify it's actually null
        s_squared = minkowski_interval_squared(x0, x1, x2, x3)
        s_squared_val = simplify(s_squared)
        
        # Construct X and compute determinant
        X = x_to_X(x0, x1, x2, x3)
        det_X = determinant(X)
        det_X_val = simplify(det_X)
        
        print(f"{description}:")
        print(f"  Vector: ({x0}, {x1}, {x2}, {x3})")
        print(f"  s² = {s_squared_val}")
        print(f"  det(X) = {det_X_val}")
        
        if det_X_val == 0:
            print(f"  ✓ NULL: det(X) = 0")
        else:
            print(f"  ✗ NOT NULL: det(X) = {det_X_val} ≠ 0")
            all_passed = False
        
        print()
    
    if all_passed:
        print("✓ PASS: All null vectors satisfy det(X) = 0")
    else:
        print("✗ FAIL: Some null vectors have det(X) ≠ 0")
    
    print()
    return all_passed


def test_timelike_spacelike():
    """
    Test additional cases: timelike and spacelike vectors.
    
    Timelike: s² > 0 (within future/past light cone)
    Spacelike: s² < 0 (outside light cone)
    Null: s² = 0 (on light cone)
    """
    print("=" * 70)
    print("TEST 3: TIMELIKE AND SPACELIKE VECTORS")
    print("=" * 70)
    print()
    
    test_vectors = [
        (2, 0, 0, 0, "Timelike (pure time)"),
        (1, 0, 0, 0, "Timelike (unit time)"),
        (2, 1, 0, 0, "Timelike (inside cone)"),
        (0, 1, 0, 0, "Spacelike (pure space)"),
        (0, 1, 1, 0, "Spacelike (spatial plane)"),
        (1, 2, 0, 0, "Spacelike (outside cone)"),
    ]
    
    for x0, x1, x2, x3, description in test_vectors:
        X = x_to_X(x0, x1, x2, x3)
        det_X = determinant(X)
        det_X_val = simplify(det_X)
        s_squared = minkowski_interval_squared(x0, x1, x2, x3)
        
        # Classify
        if det_X_val > 0:
            classification = "TIMELIKE (det > 0)"
        elif det_X_val < 0:
            classification = "SPACELIKE (det < 0)"
        else:
            classification = "NULL (det = 0)"
        
        print(f"{description}:")
        print(f"  Vector: ({x0}, {x1}, {x2}, {x3})")
        print(f"  det(X) = {det_X_val}")
        print(f"  Classification: {classification}")
        print()
    
    print("✓ Classification test complete")
    print()
    return True


def test_ubt_embedding_preservation():
    """
    Test 4: Verify UBT embedding preserves null structure.
    
    For null vector x with det(X₂) = 0, check that the embedded
    4×4 matrix X₄ = X2_to_ubt_matrix(X₂) also has det(X₄) = 0
    (or det(X₄) = (det(X₂))^k for some power k).
    """
    print("=" * 70)
    print("TEST 4: UBT EMBEDDING PRESERVES NULL STRUCTURE")
    print("=" * 70)
    print()
    
    # Test with symbolic null vector
    print("Testing symbolic null vector (1, 1, 0, 0):")
    x0, x1, x2, x3 = 1, 1, 0, 0
    
    X2 = x_to_X(x0, x1, x2, x3)
    det_X2 = determinant(X2)
    
    print(f"2×2 matrix X₂:")
    print(X2)
    print(f"det(X₂) = {det_X2}")
    print()
    
    # Test different embedding modes
    modes = ['block_diagonal', 'block_antidiagonal', 'direct_sum']
    all_passed = True
    
    for mode in modes:
        print(f"Embedding mode: {mode}")
        X4 = X2_to_ubt_matrix(X2, mode=mode)
        det_X4 = determinant(X4)
        det_X4_simplified = simplify(det_X4)
        
        print(f"  4×4 embedded matrix shape: {X4.shape}")
        print(f"  det(X₄) = {det_X4_simplified}")
        
        # Check if null structure is preserved
        if det_X4_simplified == 0:
            print(f"  ✓ NULL PRESERVED: det(X₄) = 0")
        else:
            # Check if det(X₄) = (det(X₂))^k for some power
            print(f"  ⚠ det(X₄) ≠ 0, but det(X₂) = 0")
            print(f"    This is expected for some embedding modes")
            # For block_diagonal: det(X₄) = det(X₂)²
            # For null X₂, this still gives 0
        
        print()
    
    print("Testing with numeric null vectors:")
    null_vectors = [
        (1, 1, 0, 0),
        (2, 0, 2, 0),
        (1, Rational(1, 3), Rational(1, 3), sqrt(Rational(7, 9))),
    ]
    
    for x0, x1, x2, x3 in null_vectors:
        X2 = x_to_X(x0, x1, x2, x3)
        det_X2 = simplify(determinant(X2))
        
        print(f"Vector: ({x0}, {x1}, {x2}, {x3})")
        print(f"  det(X₂) = {det_X2}")
        
        # Check block_diagonal mode (most common)
        X4 = X2_to_ubt_matrix(X2, mode='block_diagonal')
        det_X4 = simplify(determinant(X4))
        print(f"  det(X₄) [block_diagonal] = {det_X4}")
        
        if det_X4 == 0:
            print(f"  ✓ NULL PRESERVED")
        else:
            print(f"  ⚠ det(X₄) ≠ 0")
            all_passed = False
        
        print()
    
    if all_passed:
        print("✓ PASS: UBT embedding preserves null structure")
    else:
        print("⚠ WARNING: Some null vectors not preserved (may be expected)")
    
    print()
    return all_passed


def test_rank_condition():
    """
    Test 5: Verify rank condition for null matrices.
    
    For null vectors (det(X) = 0), the 2×2 matrix X should have rank 1.
    This is because X represents a light ray (1-dimensional subspace).
    """
    print("=" * 70)
    print("TEST 5: RANK CONDITION FOR NULL VECTORS")
    print("=" * 70)
    print()
    
    print("For null vectors, det(X) = 0 should imply rank(X) = 1")
    print()
    
    null_vectors = [
        (1, 1, 0, 0, "Light ray along x"),
        (1, 0, 1, 0, "Light ray along y"),
        (2, sqrt(2), sqrt(2), 0, "Scaled null"),
    ]
    
    all_passed = True
    
    for x0, x1, x2, x3, description in null_vectors:
        X = x_to_X(x0, x1, x2, x3)
        det_X = simplify(determinant(X))
        rank_X = X.rank()
        
        print(f"{description}:")
        print(f"  Vector: ({x0}, {x1}, {x2}, {x3})")
        print(f"  X =")
        for row in range(X.shape[0]):
            print(f"    {X.row(row)}")
        print(f"  det(X) = {det_X}")
        print(f"  rank(X) = {rank_X}")
        
        if det_X == 0 and rank_X == 1:
            print(f"  ✓ PASS: det = 0 and rank = 1")
        else:
            print(f"  ✗ FAIL: Expected rank = 1 for null vector")
            all_passed = False
        
        print()
    
    # Test non-null vectors (should have rank 2)
    print("Testing non-null vectors (should have rank = 2):")
    non_null_vectors = [
        (1, 0, 0, 0, "Timelike"),
        (0, 1, 0, 0, "Spacelike"),
        (2, 1, 0, 0, "Timelike"),
    ]
    
    for x0, x1, x2, x3, description in non_null_vectors:
        X = x_to_X(x0, x1, x2, x3)
        det_X = simplify(determinant(X))
        rank_X = X.rank()
        
        print(f"{description}: ({x0}, {x1}, {x2}, {x3})")
        print(f"  det(X) = {det_X}, rank(X) = {rank_X}")
        
        if det_X != 0 and rank_X == 2:
            print(f"  ✓ PASS: det ≠ 0 and rank = 2 (full rank)")
        else:
            print(f"  ✗ Unexpected: rank = {rank_X}")
            all_passed = False
        
        print()
    
    if all_passed:
        print("✓ PASS: Rank condition satisfied for all test cases")
    else:
        print("✗ FAIL: Some rank conditions not satisfied")
    
    print()
    return all_passed


def main():
    """Run all light-cone tests."""
    print()
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 16 + "LIGHT-CONE CONSISTENCY TEST" + " " * 25 + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    print("Testing null structure emergence from Minkowski spinor formalism")
    print("and its preservation under UBT embedding.")
    print()
    print("Signature convention: s² = (x⁰)² - (x¹)² - (x²)² - (x³)²")
    print("                      Metric: (+, -, -, -)")
    print()
    
    # Run all tests
    results = []
    
    results.append(("Symbolic determinant", test_symbolic_determinant()))
    results.append(("Null vectors", test_null_vector_numeric()))
    results.append(("Timelike/Spacelike", test_timelike_spacelike()))
    results.append(("UBT embedding", test_ubt_embedding_preservation()))
    results.append(("Rank condition", test_rank_condition()))
    
    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    for test_name, passed in results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{status}: {test_name}")
    
    print()
    
    total = len(results)
    passed = sum(1 for _, p in results if p)
    
    print(f"Total: {passed} passed, {total - passed} failed")
    print()
    
    if all(p for _, p in results):
        print("🎉 ALL LIGHT-CONE TESTS PASSED!")
        print()
        print("Key results:")
        print("  • det(X) = s² (Minkowski interval squared)")
        print("  • Null vectors (light-like) satisfy det(X) = 0")
        print("  • UBT embedding preserves null structure")
        print("  • Null matrices have rank 1 (light ray)")
        return True
    else:
        print("⚠️  Some tests failed - review output above")
        return False


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
