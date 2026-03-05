#!/usr/bin/env python3
"""
e01_algebra_isomorphism.py — Demonstrate ℂ⊗ℍ ≅ Mat(2,ℂ).

Verifies the standard algebra isomorphism between biquaternions and 2×2
complex matrices, checking:
1. Quaternion identities i² = j² = k² = ijk = -1.
2. 8-dimensional real basis spans Mat(2,ℂ).

Run with:
    python -m THEORY_COMPARISONS.dimensional_economy.experiments.e01_algebra_isomorphism

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys

from THEORY_COMPARISONS.dimensional_economy.dim_economy_core.biquaternion_algebra import (
    quaternion_basis,
    biquaternion_basis,
    verify_quaternion_relations,
    basis_is_linearly_independent,
    dimension_count,
)


def run():
    """Run all algebra isomorphism checks and print results."""
    print("=" * 70)
    print("E01 — ℂ⊗ℍ ≅ Mat(2,ℂ) ISOMORPHISM VERIFICATION")
    print("=" * 70)
    print()

    # 1. Quaternion basis
    print("1. Quaternion basis elements {1, i, j, k} as 2×2 matrices:")
    basis = quaternion_basis()
    for name, mat in basis.items():
        print(f"   {name}:")
        for row in mat.tolist():
            print(f"      {row}")
    print()

    # 2. Quaternion relations
    print("2. Verifying quaternion relations i²=j²=k²=ijk=-1 ...")
    ok = verify_quaternion_relations()
    print(f"   Result: {'✓ PASSED' if ok else '✗ FAILED'}")
    print()

    # 3. 8-dimensional basis
    print("3. Checking that the 8 biquaternion basis elements are ℝ-linearly independent ...")
    ok2 = basis_is_linearly_independent()
    print(f"   Result: {'✓ PASSED — rank = 8 (spans Mat(2,ℂ) over ℝ)' if ok2 else '✗ FAILED'}")
    print()

    # 4. Dimensional inventory table
    print("4. Dimensional inventory across competing theories:")
    print()
    header = f"{'Theory':<35} {'Extra spatial':>14} {'Internal alg':>14} {'Total extra':>26} {'Assoc.':>7}"
    print("   " + header)
    print("   " + "-" * len(header))
    for row in dimension_count():
        assoc = "✅" if row['associative'] else "❌"
        line = (
            f"{row['theory']:<35} "
            f"{str(row['extra_spatial_dims']):>14} "
            f"{str(row['internal_algebra_dims']):>14} "
            f"{str(row['total_extra']):>26} "
            f"{assoc:>7}"
        )
        print("   " + line)
    print()

    print("=" * 70)
    print("CONCLUSION: ℂ⊗ℍ ≅ Mat(2,ℂ) verified. UBT uses 0 extra spatial")
    print("dimensions, 8-dimensional associative internal algebra, plus")
    print("one compact imaginary time direction.")
    print("=" * 70)
    print()

    return ok and ok2


if __name__ == '__main__':
    success = run()
    sys.exit(0 if success else 1)
