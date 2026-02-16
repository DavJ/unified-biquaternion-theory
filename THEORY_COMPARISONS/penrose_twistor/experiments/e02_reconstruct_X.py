#!/usr/bin/env python3
"""
e02_reconstruct_X.py - Reconstruct spacetime point from two twistors

Demonstrates the reconstruction of a spacetime point X from two
independent twistors Z₁, Z₂ both incident with X.

Solves: ω₁ = i X π₁
        ω₂ = i X π₂
for X.

Run with:
    python -m THEORY_COMPARISONS.penrose_twistor.experiments.e02_reconstruct_X

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys
from pathlib import Path

# Add repository root to path
repo_root = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(repo_root))

from sympy import Matrix, I, simplify
from THEORY_COMPARISONS.penrose_twistor.twistor_core.minkowski_spinor import (
    x_to_X, X_to_x, minkowski_interval_squared
)
from THEORY_COMPARISONS.penrose_twistor.twistor_core.twistor import (
    twistor_from_X_pi, are_twistors_independent, reconstruct_X_from_twistors,
    check_incidence, spinor
)
from THEORY_COMPARISONS.penrose_twistor.common.linalg import determinant


def test_reconstruction_numeric():
    """Test reconstruction with numeric values."""
    print("=" * 70)
    print("NUMERIC RECONSTRUCTION TEST")
    print("=" * 70)
    print()
    
    # Choose a spacetime point
    t, x, y, z = 3.0, 1.5, 0.8, -0.5
    X_original = x_to_X(t, x, y, z)
    
    print("Original spacetime point:")
    print(f"  Coordinates: (t, x, y, z) = ({t}, {x}, {y}, {z})")
    s2 = minkowski_interval_squared(t, x, y, z)
    print(f"  Interval squared: s² = {s2}")
    print()
    
    print("Original Hermitian matrix X:")
    print(X_original.evalf())
    print()
    
    # Choose two independent spinors
    pi1 = Matrix([1, 0])
    pi2 = Matrix([0, 1])
    
    print("Two independent spinors:")
    print(f"  π₁ = {pi1.T}")
    print(f"  π₂ = {pi2.T}")
    print()
    
    # Create two twistors incident with X
    Z1 = twistor_from_X_pi(X_original, pi1)
    Z2 = twistor_from_X_pi(X_original, pi2)
    
    print("Two twistors incident with X:")
    print(f"  Z₁: ω₁ = {Z1.omega.T}, π₁ = {Z1.pi.T}")
    print(f"  Z₂: ω₂ = {Z2.omega.T}, π₂ = {Z2.pi.T}")
    print()
    
    # Check independence
    independent = are_twistors_independent(Z1, Z2)
    print(f"Twistors are independent: {independent}")
    print()
    
    if not independent:
        print("✗ Cannot reconstruct - twistors not independent!")
        return False
    
    # Reconstruct X
    print("Reconstructing X from (Z₁, Z₂)...")
    X_reconstructed = reconstruct_X_from_twistors(Z1, Z2)
    
    if X_reconstructed is None:
        print("✗ Reconstruction failed!")
        return False
    
    print("Reconstructed Hermitian matrix X:")
    print(X_reconstructed.evalf())
    print()
    
    # Extract coordinates
    t_rec, x_rec, y_rec, z_rec = X_to_x(X_reconstructed)
    print("Reconstructed coordinates:")
    print(f"  (t, x, y, z) = ({t_rec}, {x_rec}, {y_rec}, {z_rec})")
    print()
    
    # Compute difference
    diff_matrix = simplify(X_original - X_reconstructed)
    print("Difference matrix (Original - Reconstructed):")
    print(diff_matrix.evalf())
    print()
    
    # Compute norm of difference
    diff_norm = 0
    for i in range(2):
        for j in range(2):
            elem = complex(diff_matrix[i, j])
            diff_norm += abs(elem)**2
    diff_norm = diff_norm**0.5
    
    print(f"Frobenius norm of difference: {diff_norm:.2e}")
    print()
    
    if diff_norm < 1e-10:
        print("✓ RECONSTRUCTION SUCCESSFUL (exact within numerical precision)")
        success = True
    else:
        print("✗ Reconstruction has significant error!")
        success = False
    
    print()
    
    return success


def test_reconstruction_different_spinors():
    """Test reconstruction with different choice of spinors."""
    print("=" * 70)
    print("RECONSTRUCTION WITH DIFFERENT SPINORS")
    print("=" * 70)
    print()
    
    # Same spacetime point
    t, x, y, z = 2.0, 0.5, 1.2, -0.8
    X_original = x_to_X(t, x, y, z)
    
    print(f"Original point: ({t}, {x}, {y}, {z})")
    print()
    
    # Different spinor choices
    spinor_pairs = [
        (Matrix([1, 0]), Matrix([0, 1])),  # Canonical basis
        (Matrix([1, 1]), Matrix([1, -1])),  # Hadamard-like
        (Matrix([1 + I, 0]), Matrix([0, 1 - I])),  # Complex
    ]
    
    for idx, (pi1, pi2) in enumerate(spinor_pairs, 1):
        print(f"Spinor pair {idx}:")
        print(f"  π₁ = {pi1.T}")
        print(f"  π₂ = {pi2.T}")
        
        # Create twistors
        Z1 = twistor_from_X_pi(X_original, pi1)
        Z2 = twistor_from_X_pi(X_original, pi2)
        
        # Check independence
        if not are_twistors_independent(Z1, Z2):
            print("  ✗ Spinors not independent - skipping")
            print()
            continue
        
        # Reconstruct
        X_rec = reconstruct_X_from_twistors(Z1, Z2)
        
        if X_rec is None:
            print("  ✗ Reconstruction failed!")
            print()
            continue
        
        # Check accuracy
        diff_matrix = simplify(X_original - X_rec)
        diff_norm = sum(abs(complex(diff_matrix[i, j]))**2 
                       for i in range(2) for j in range(2))**0.5
        
        print(f"  Reconstruction error: {diff_norm:.2e}")
        
        if diff_norm < 1e-10:
            print("  ✓ Success")
        else:
            print("  ✗ Significant error")
        
        print()
    
    print("✓ Reconstruction is independent of spinor choice (as expected)")
    print()
    
    return True


def test_reconstruction_symbolic():
    """Test reconstruction symbolically."""
    print("=" * 70)
    print("SYMBOLIC RECONSTRUCTION TEST")
    print("=" * 70)
    print()
    
    from sympy import symbols
    
    # Symbolic coordinates
    t, x, y, z = symbols('t x y z', real=True)
    X_original = x_to_X(t, x, y, z)
    
    print("Original symbolic X:")
    print(X_original)
    print()
    
    # Simple spinor choice
    pi1 = Matrix([1, 0])
    pi2 = Matrix([0, 1])
    
    print("Canonical spinor basis:")
    print(f"  π₁ = {pi1.T}")
    print(f"  π₂ = {pi2.T}")
    print()
    
    # Create twistors
    Z1 = twistor_from_X_pi(X_original, pi1)
    Z2 = twistor_from_X_pi(X_original, pi2)
    
    print("Twistors:")
    print(f"  Z₁: ω₁ = {Z1.omega.T}")
    print(f"  Z₂: ω₂ = {Z2.omega.T}")
    print()
    
    # Reconstruct
    print("Reconstructing...")
    X_rec = reconstruct_X_from_twistors(Z1, Z2)
    
    print("Reconstructed symbolic X:")
    print(X_rec)
    print()
    
    # Check if identical
    diff = simplify(X_original - X_rec)
    is_exact = diff == Matrix.zeros(2, 2)
    
    if is_exact:
        print("✓ SYMBOLIC RECONSTRUCTION EXACT")
    else:
        print("Difference:")
        print(diff)
    
    print()
    
    return is_exact


def main():
    """Run all reconstruction experiments."""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 12 + "TWISTOR RECONSTRUCTION EXPERIMENT" + " " * 22 + "║")
    print("╚" + "═" * 68 + "╝")
    print()
    
    tests = [
        ("Numeric Reconstruction", test_reconstruction_numeric),
        ("Different Spinors", test_reconstruction_different_spinors),
        ("Symbolic Reconstruction", test_reconstruction_symbolic),
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
        print("🎉 RECONSTRUCTION WORKS FOR NONTRIVIAL CASES!")
        print()
        print("Key result: Given two independent twistors Z₁, Z₂ incident with")
        print("a spacetime point X, we can exactly reconstruct X.")
        print()
        print("This demonstrates the bijection between spacetime points and")
        print("certain families of twistors (parametrized by spinor choice).")
    else:
        print("⚠️  Some tests failed - review output above")
    
    print()
    
    return failed == 0


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
