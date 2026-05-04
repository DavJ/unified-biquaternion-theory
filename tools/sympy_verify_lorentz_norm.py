#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
sympy_verify_lorentz_norm.py — Symbolic verification of Lorentz invariance.

PURPOSE
-------
Verifies symbolically (via SymPy) that the Minkowski spacetime interval

    s² = -t² + x² + y² + z²

is preserved under a Lorentz boost:

    t' = γ(t - v·x)
    x' = γ(x - v·t)
    y' = y
    z' = z

where γ = 1/√(1-v²).

The verification is exact (polynomial identity), with no floating-point
approximations.

Additionally verifies:
  1. Spacetime interval invariance
  2. Quaternion norm multiplicativity  ||q₁q₂||² = ||q₁||² · ||q₂||²
  3. Lorentz boost as a quaternion sandwich product

USAGE
-----
    python tools/sympy_verify_lorentz_norm.py [--verbose]

EXIT CODE
---------
    0 — all identities verified
    1 — a violation was found
"""

from __future__ import annotations

import argparse
import sys


def _require_sympy() -> None:
    try:
        import sympy  # noqa: F401
    except ImportError:
        print("ERROR: sympy is required.  Install with:  pip install sympy>=1.12",
              file=sys.stderr)
        sys.exit(2)


def verify_lorentz_boost_interval(verbose: bool = False) -> bool:
    """
    Verify that s'² = s² under a Lorentz boost along the x-axis.

    Uses SymPy rational arithmetic for exact verification.
    """
    import sympy as sp

    t, x, y, z, v = sp.symbols("t x y z v", real=True)

    # Assume 0 < v < 1 (subluminal boost)
    gamma = 1 / sp.sqrt(1 - v**2)

    # Lorentz boost transformations
    t_prime = gamma * (t - v * x)
    x_prime = gamma * (x - v * t)
    y_prime = y
    z_prime = z

    # Spacetime intervals
    s_sq       = -t**2 + x**2 + y**2 + z**2
    s_prime_sq = -t_prime**2 + x_prime**2 + y_prime**2 + z_prime**2

    # Difference should be zero
    diff = sp.simplify(sp.expand(s_prime_sq - s_sq))

    passed = diff == 0

    if verbose:
        print("Lorentz boost interval invariance:")
        print(f"  s²  = -t² + x² + y² + z²")
        print(f"  s'² = {sp.expand(s_prime_sq)}")
        print(f"  s'² - s² = {diff}  {'(= 0 ✓)' if passed else '(≠ 0 ✗)'}")

    return passed


def verify_quaternion_norm_multiplicativity(verbose: bool = False) -> bool:
    """
    Verify that the quaternion norm is multiplicative:

        N(q₁ q₂) = N(q₁) · N(q₂)

    where N(q) = a² + b² + c² + d² for q = a + bI + cJ + dK.

    This is an exact polynomial identity (Euler's four-square identity).
    """
    import sympy as sp

    # Components of q₁ and q₂
    a1, b1, c1, d1 = sp.symbols("a1 b1 c1 d1", real=True)
    a2, b2, c2, d2 = sp.symbols("a2 b2 c2 d2", real=True)

    def quat_product(q1: tuple, q2: tuple) -> tuple:
        """Hamilton product of two quaternions given as (a,b,c,d)."""
        a1_, b1_, c1_, d1_ = q1
        a2_, b2_, c2_, d2_ = q2
        return (
            a1_*a2_ - b1_*b2_ - c1_*c2_ - d1_*d2_,
            a1_*b2_ + b1_*a2_ + c1_*d2_ - d1_*c2_,
            a1_*c2_ - b1_*d2_ + c1_*a2_ + d1_*b2_,
            a1_*d2_ + b1_*c2_ - c1_*b2_ + d1_*a2_,
        )

    def norm_sq(q: tuple) -> sp.Expr:
        return sum(x**2 for x in q)

    q1 = (a1, b1, c1, d1)
    q2 = (a2, b2, c2, d2)
    q12 = quat_product(q1, q2)

    lhs = sp.expand(norm_sq(q12))
    rhs = sp.expand(norm_sq(q1) * norm_sq(q2))

    diff = sp.expand(lhs - rhs)
    passed = diff == 0

    if verbose:
        print("Quaternion norm multiplicativity N(q₁q₂) = N(q₁)·N(q₂):")
        print(f"  N(q₁q₂) - N(q₁)·N(q₂) = {diff}  "
              f"{'(= 0 ✓ Euler four-square identity)' if passed else '(≠ 0 ✗)'}")

    return passed


def verify_boost_as_sandwich(verbose: bool = False) -> bool:
    """
    Verify that a Lorentz boost in the (t,x)-plane is realised as a
    biquaternion sandwich product via the SL(2,ℂ) isomorphism:

        v' = L · v_matrix · L†

    where:
      - v_matrix = t·I₂ + x·σ₁  (Hermitian 2×2 matrix encoding the 4-vector)
      - L = [[cosh(α/2), sinh(α/2)],
             [sinh(α/2), cosh(α/2)]]  (SL(2,ℂ) boost matrix)
      - L† is the Hermitian conjugate of L

    This is the standard realisation of Lorentz boosts via the covering group
    SL(2,ℂ) ≅ Spin(3,1), which is exactly the matrix subalgebra of ℂ⊗ℍ.

    Expected result:
      t' = t·cosh(α) - x·sinh(α)   (from Tr(v')/2)
      x' = -t·sinh(α) + x·cosh(α)  (from Tr(σ₁·v')/2)
    """
    import sympy as sp

    t, x, alpha = sp.symbols("t x alpha", real=True)

    # Pauli matrices as sympy matrices
    I2 = sp.eye(2)
    sigma1 = sp.Matrix([[0, 1], [1, 0]])

    # 4-vector as 2×2 Hermitian matrix (t,x component)
    # v = t·I₂ + x·σ₁  (reduced 1+1D: only time and x-direction)
    v_mat = t * I2 + x * sigma1

    # SL(2,ℂ) boost matrix for boost along σ₁-direction
    ch = sp.cosh(alpha / 2)
    sh = sp.sinh(alpha / 2)
    L = sp.Matrix([[ch, sh], [sh, ch]])
    # L† = L.H (Hermitian conjugate; L is real here, so L† = L^T = L)
    L_dag = L.T  # L is symmetric real, so L† = L

    # Boost action: v' = L · v_mat · L†
    v_prime = sp.simplify(L * v_mat * L_dag)

    # Extract t' from Tr(v')/2 and x' from Tr(σ₁·v')/2
    t_prime = sp.simplify(v_prime.trace() / 2)
    x_prime = sp.simplify((sigma1 * v_prime).trace() / 2)

    # Expected Lorentz boost in rapidity form (active boost: object moves in +x)
    # The SL(2,ℂ) sandwich L·v·L† with L = [[ch,sh],[sh,ch]] gives an ACTIVE
    # boost in the +x direction:
    #   t' = t·cosh(α) + x·sinh(α)
    #   x' = t·sinh(α) + x·cosh(α)
    # This is physically equivalent to the passive boost (swap signs of off-diagonals),
    # both are valid Lorentz transformations.
    t_expected = t * sp.cosh(alpha) + x * sp.sinh(alpha)
    x_expected = t * sp.sinh(alpha) + x * sp.cosh(alpha)

    diff_t = sp.simplify(t_prime - t_expected)
    diff_x = sp.simplify(x_prime - x_expected)

    passed = (diff_t == 0) and (diff_x == 0)

    if verbose:
        print("Lorentz boost as SL(2,ℂ) sandwich L·v·L† (ℂ⊗ℍ matrix rep):")
        print(f"  t' = Tr(v')/2       = {t_prime}")
        print(f"  t' expected         = {t_expected}")
        print(f"  t' error            = {diff_t}  {'(= 0 ✓)' if diff_t == 0 else '(≠ 0 ✗)'}")
        print(f"  x' = Tr(σ₁·v')/2   = {x_prime}")
        print(f"  x' expected         = {x_expected}")
        print(f"  x' error            = {diff_x}  {'(= 0 ✓)' if diff_x == 0 else '(≠ 0 ✗)'}")

    return passed


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Symbolic verification of Lorentz invariance."
    )
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    _require_sympy()

    print("=" * 65)
    print("Symbolic Lorentz Invariance Verification  (SymPy)")
    print("=" * 65)

    results: dict[str, bool] = {}

    print("\n1. Spacetime interval  s'² = s²  under Lorentz boost")
    results["interval_invariance"] = verify_lorentz_boost_interval(verbose=True)

    print("\n2. Quaternion norm multiplicativity  N(q₁q₂) = N(q₁)N(q₂)")
    results["norm_multiplicativity"] = verify_quaternion_norm_multiplicativity(
        verbose=True
    )

    print("\n3. Lorentz boost as SL(2,ℂ) sandwich  L·v·L† (matrix rep of ℂ⊗ℍ)")
    results["sandwich_boost"] = verify_boost_as_sandwich(verbose=True)

    print("\n" + "=" * 65)
    all_passed = all(results.values())
    for name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"  {status}  {name}")
    print("=" * 65)

    if all_passed:
        print("\n✓ ALL LORENTZ INVARIANCE IDENTITIES VERIFIED SYMBOLICALLY.")
    else:
        print("\n✗ SOME IDENTITIES FAILED — check above.")

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
