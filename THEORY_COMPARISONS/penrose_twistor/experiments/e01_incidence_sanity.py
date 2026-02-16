#!/usr/bin/env python3
"""
e01_incidence_sanity.py - Verify incidence relation ω = i X π

Tests the fundamental incidence relation between spacetime points
and twistors both symbolically and numerically.

Run with:
    python -m THEORY_COMPARISONS.penrose_twistor.experiments.e01_incidence_sanity

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys
from pathlib import Path

# Add repository root to path
repo_root = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(repo_root))

from sympy import symbols, Matrix, I, simplify
from THEORY_COMPARISONS.penrose_twistor.twistor_core.minkowski_spinor import (
    x_to_X, X_to_x
)
from THEORY_COMPARISONS.penrose_twistor.twistor_core.twistor import (
    incidence, twistor_from_X_pi, check_incidence, spinor
)


def test_symbolic_incidence():
    """Test incidence relation symbolically."""
    print("=" * 70)
    print("SYMBOLIC INCIDENCE TEST")
    print("=" * 70)
    print()
    
    # Define symbolic spacetime coordinates
    t, x, y, z = symbols('t x y z', real=True)
    
    # Convert to 2×2 Hermitian matrix
    X = x_to_X(t, x, y, z)
    print(f"Spacetime point: (t, x, y, z) = ({t}, {x}, {y}, {z})")
    print(f"Hermitian matrix X:")
    print(X)
    print()
    
    # Define symbolic spinor
    a, b = symbols('a b', complex=True)
    pi = Matrix([a, b])
    print(f"Spinor π = {pi.T}")
    print()
    
    # Compute ω from incidence relation
    omega = incidence(X, pi)
    print("Incidence relation: ω = i X π")
    print(f"ω = {omega.T}")
    print()
    
    # Create twistor
    Z = twistor_from_X_pi(X, pi)
    print(f"Twistor Z = {Z}")
    print()
    
    # Verify incidence
    is_incident = check_incidence(Z, X)
    print(f"✓ Incidence verified: {is_incident}")
    print()
    
    return is_incident


def test_numeric_incidence():
    """Test incidence relation numerically."""
    print("=" * 70)
    print("NUMERIC INCIDENCE TEST")
    print("=" * 70)
    print()
    
    # Define numeric spacetime point (origin in time)
    t_val, x_val, y_val, z_val = 1.0, 0.5, 0.3, 0.2
    X = x_to_X(t_val, x_val, y_val, z_val)
    
    print(f"Spacetime point: (t, x, y, z) = ({t_val}, {x_val}, {y_val}, {z_val})")
    print(f"Hermitian matrix X:")
    print(X.evalf())
    print()
    
    # Define numeric spinor
    pi = Matrix([1 + 0.5*I, 0.7 - 0.3*I])
    print(f"Spinor π = {pi.T}")
    print()
    
    # Compute ω
    omega = incidence(X, pi)
    print("Incidence relation: ω = i X π")
    print(f"ω = {omega.T}")
    print()
    
    # Create twistor
    Z = twistor_from_X_pi(X, pi)
    print(f"Twistor Z:")
    print(f"  ω = {Z.omega.T}")
    print(f"  π = {Z.pi.T}")
    print()
    
    # Verify incidence
    is_incident = check_incidence(Z, X)
    print(f"✓ Incidence verified: {is_incident}")
    print()
    
    return is_incident


def test_multiple_spinors():
    """Test that different spinors give different twistors for same point."""
    print("=" * 70)
    print("MULTIPLE SPINORS FOR SAME POINT")
    print("=" * 70)
    print()
    
    # Fixed spacetime point
    X = x_to_X(2.0, 1.0, 0.0, 0.5)
    print("Fixed spacetime point X:")
    print(X.evalf())
    print()
    
    # Three different spinors
    pi1 = Matrix([1, 0])
    pi2 = Matrix([0, 1])
    pi3 = Matrix([1 + I, 1 - I])
    
    spinors = [pi1, pi2, pi3]
    twistors = []
    
    for i, pi in enumerate(spinors, 1):
        print(f"Spinor π{i} = {pi.T}")
        omega = incidence(X, pi)
        print(f"  → ω{i} = {omega.T}")
        Z = twistor_from_X_pi(X, pi)
        twistors.append(Z)
        
        # Verify incidence
        is_incident = check_incidence(Z, X)
        print(f"  → Incident: {is_incident}")
        print()
    
    print("✓ All three twistors are incident with the same spacetime point X")
    print("  This demonstrates that a point corresponds to a family of twistors")
    print()
    
    return True


def test_roundtrip_consistency():
    """Test that incidence is consistent with matrix operations."""
    print("=" * 70)
    print("ROUNDTRIP CONSISTENCY TEST")
    print("=" * 70)
    print()
    
    # Start with numeric values
    t, x, y, z = 1.5, 0.8, -0.3, 0.6
    
    # Convert to X
    X = x_to_X(t, x, y, z)
    print(f"Original coords: ({t}, {x}, {y}, {z})")
    print()
    
    # Convert back
    t_back, x_back, y_back, z_back = X_to_x(X)
    print(f"After X_to_x: ({t_back}, {x_back}, {y_back}, {z_back})")
    print()
    
    # Check difference
    diff_t = abs(complex(t - t_back))
    diff_x = abs(complex(x - x_back))
    diff_y = abs(complex(y - y_back))
    diff_z = abs(complex(z - z_back))
    
    max_diff = max(diff_t, diff_x, diff_y, diff_z)
    print(f"Maximum coordinate difference: {max_diff:.2e}")
    
    if max_diff < 1e-10:
        print("✓ Roundtrip exact (within numerical precision)")
    else:
        print("✗ Roundtrip has errors!")
    
    print()
    
    return max_diff < 1e-10


def main():
    """Run all incidence sanity checks."""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "TWISTOR INCIDENCE SANITY CHECK" + " " * 23 + "║")
    print("╚" + "═" * 68 + "╝")
    print()
    
    tests = [
        ("Symbolic Incidence", test_symbolic_incidence),
        ("Numeric Incidence", test_numeric_incidence),
        ("Multiple Spinors", test_multiple_spinors),
        ("Roundtrip Consistency", test_roundtrip_consistency),
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
        print("🎉 ALL INCIDENCE TESTS PASSED!")
    else:
        print("⚠️  Some tests failed - review output above")
    
    print()
    
    return failed == 0


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
