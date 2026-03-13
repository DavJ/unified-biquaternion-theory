#!/usr/bin/env python3
"""
e03_associativity_advantage.py — Associativity of ℂ⊗ℍ vs. octonion failure.

Demonstrates:
1. ℂ⊗ℍ ≅ Mat(2,ℂ) is associative: (AB)C = A(BC) symbolically proved.
2. Octonions are non-associative: classic counterexample e₁·(e₂·e₄) ≠ (e₁·e₂)·e₄.
3. Summary of why this matters for QFT compatibility.

Run with:
    python -m THEORY_COMPARISONS.dimensional_economy.experiments.e03_associativity_advantage

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys

from THEORY_COMPARISONS.dimensional_economy.dim_economy_core.associativity import (
    verify_mat2c_associativity,
    demonstrate_octonion_non_associativity,
    verify_octonions_non_associative,
    associativity_comparison_summary,
)


def run():
    """Run associativity advantage demonstration."""
    print("=" * 70)
    print("E03 — ASSOCIATIVITY: ℂ⊗ℍ (UBT) vs ℂ⊗𝕆 (FUREY)")
    print("=" * 70)
    print()

    # 1. Mat(2,ℂ) associativity
    print("1. Mat(2,ℂ) associativity: (AB)C = A(BC) for symbolic A,B,C ∈ Mat(2,ℂ)")
    ok_mat = verify_mat2c_associativity()
    print(f"   Result: {'✓ PROVED symbolically' if ok_mat else '✗ FAILED'}")
    print()

    # 2. Octonion non-associativity
    print("2. Octonion non-associativity counterexample: e₁·(e₂·e₄) vs (e₁·e₂)·e₄")
    result = demonstrate_octonion_non_associativity()
    lhs = result['lhs']
    rhs = result['rhs']
    diff = [lhs[k] - rhs[k] for k in range(8)]
    print(f"   e₁·(e₂·e₄) = {lhs}")
    print(f"   (e₁·e₂)·e₄ = {rhs}")
    print(f"   Difference  = {diff}")
    if not result['is_associative']:
        print("   ✓ Confirmed: e₁·(e₂·e₄) ≠ (e₁·e₂)·e₄  →  octonions NON-ASSOCIATIVE")
    else:
        print("   ✗ Unexpected: products are equal (check table)")
    print()

    ok_oct = verify_octonions_non_associative()
    print(f"   Non-associativity verified: {'✓ YES' if ok_oct else '✗ NO'}")
    print()

    # 3. Summary
    print("3. Associativity advantage summary:")
    summary = associativity_comparison_summary()
    print(f"   Mat(2,ℂ) associative : {summary['mat2c_associative']}")
    print(f"   Octonions associative: {summary['octonions_associative']}")
    print()
    print("   UBT ADVANTAGE:")
    print(f"   {summary['ubt_advantage']}")
    print()

    all_ok = ok_mat and ok_oct

    print("=" * 70)
    print("CONCLUSION:")
    print("  UBT's algebra ℂ⊗ℍ ≅ Mat(2,ℂ) is associative by construction.")
    print("  Standard QFT path integral, Wick's theorem, and renormalization")
    print("  all apply without modification.")
    print("  Furey's ℂ⊗𝕆 requires additional structure to handle the")
    print("  non-associativity of octonions — an open problem in her programme.")
    print(f"  Overall: {'ALL CHECKS PASSED ✓' if all_ok else 'SOME CHECKS FAILED ✗'}")
    print("=" * 70)
    print()

    return all_ok


if __name__ == '__main__':
    success = run()
    sys.exit(0 if success else 1)
