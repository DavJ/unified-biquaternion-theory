#!/usr/bin/env python3
"""
e02_su2l_derivation.py — Derive SU(2)_L and U(1)_Y from ℂ⊗ℍ automorphisms.

Verifies that:
1. T^a = (i/2) σ^a are the SU(2)_L generators (left action on ℂ⊗ℍ).
2. [T^a, T^b] = ε^{abc} T^c holds exactly (proved by direct computation).
3. Y = -i I₂ generates U(1)_Y via right action.
4. SU(2)_L and U(1)_Y commute (left and right actions commute).

Run with:
    python -m THEORY_COMPARISONS.dimensional_economy.experiments.e02_su2l_derivation

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys

from sympy import simplify, zeros

from THEORY_COMPARISONS.dimensional_economy.dim_economy_core.su2l_generators import (
    su2l_generators,
    verify_su2_commutation_relations,
    verify_generators_traceless,
    verify_generators_antihermitian,
    left_action,
)
from THEORY_COMPARISONS.dimensional_economy.dim_economy_core.u1y_generator import (
    u1y_generator,
    right_action,
    verify_u1y_commutes_with_su2l,
    verify_u1y_antihermitian,
    verify_u1y_phase_rotation,
)
from THEORY_COMPARISONS.dimensional_economy.common.algebra import (
    pauli_matrices,
    levi_civita,
)


def run():
    """Run all SU(2)_L and U(1)_Y derivation checks."""
    print("=" * 70)
    print("E02 — SU(2)_L AND U(1)_Y DERIVATION FROM ℂ⊗ℍ AUTOMORPHISMS")
    print("=" * 70)
    print()

    # 1. Show generators
    T1, T2, T3 = su2l_generators()
    print("1. SU(2)_L generators T^a = (i/2) σ^a:")
    for a, Ta in enumerate([T1, T2, T3], start=1):
        print(f"   T^{a} = {Ta.tolist()}")
    print()

    # 2. Commutation relations
    print("2. Verifying [T^a, T^b] = ε^{abc} T^c for all a,b ∈ {1,2,3} ...")
    ok_comm = verify_su2_commutation_relations()
    print(f"   Result: {'✓ PROVED — all 9 commutators verified' if ok_comm else '✗ FAILED'}")
    print()

    # 3. Traceless check
    print("3. Verifying generators are traceless (su(2) ⊂ sl(2,ℂ)) ...")
    ok_trace = verify_generators_traceless()
    print(f"   Result: {'✓ PROVED — all T^a traceless' if ok_trace else '✗ FAILED'}")
    print()

    # 4. Anti-Hermitian check
    print("4. Verifying generators are anti-Hermitian (T^a)† = -T^a ...")
    ok_ah = verify_generators_antihermitian()
    print(f"   Result: {'✓ PROVED — all T^a anti-Hermitian' if ok_ah else '✗ FAILED'}")
    print()

    # 5. Show explicit non-trivial commutator
    from THEORY_COMPARISONS.dimensional_economy.common.algebra import commutator
    comm12 = commutator(T1, T2)
    print("5. Explicit check: [T^1, T^2] = ε^{12c} T^c = T^3")
    print(f"   [T^1, T^2] = {comm12.tolist()}")
    print(f"   T^3        = {T3.tolist()}")
    diff = simplify(comm12 - T3)
    print(f"   Residual   = {diff.tolist()}")
    print(f"   {'✓ Confirmed' if diff == zeros(2,2) else '✗ Mismatch'}")
    print()

    # 6. U(1)_Y generator
    Y = u1y_generator()
    print("6. U(1)_Y generator Y = -i I₂:")
    print(f"   Y = {Y.tolist()}")
    print()

    # 7. U(1)_Y anti-Hermitian
    print("7. Verifying Y is anti-Hermitian ...")
    ok_y_ah = verify_u1y_antihermitian()
    print(f"   Result: {'✓ PROVED' if ok_y_ah else '✗ FAILED'}")
    print()

    # 8. U(1)_Y commutes with SU(2)_L
    print("8. Verifying U(1)_Y right action commutes with SU(2)_L left actions ...")
    ok_comm_y = verify_u1y_commutes_with_su2l()
    print(f"   Result: {'✓ PROVED — left and right actions commute' if ok_comm_y else '✗ FAILED'}")
    print()

    # 9. Phase rotation
    print("9. Verifying exp(θ Y) = e^{-iθ} I₂ (finite U(1) transformation) ...")
    ok_phase = verify_u1y_phase_rotation()
    print(f"   Result: {'✓ PROVED at θ = π/4' if ok_phase else '✗ FAILED'}")
    print()

    all_ok = all([ok_comm, ok_trace, ok_ah, ok_y_ah, ok_comm_y, ok_phase])

    print("=" * 70)
    print("CONCLUSION:")
    print("  SU(2)_L generators derived from left action of ℂ⊗ℍ on itself.")
    print("  U(1)_Y generator derived from right action of ℂ⊗ℍ on itself.")
    print("  Commutation relations [T^a,T^b]=ε^{abc}T^c verified by direct")
    print("  computation — no postulates required.")
    print(f"  Overall: {'ALL CHECKS PASSED ✓' if all_ok else 'SOME CHECKS FAILED ✗'}")
    print("=" * 70)
    print()

    return all_ok


if __name__ == '__main__':
    success = run()
    sys.exit(0 if success else 1)
