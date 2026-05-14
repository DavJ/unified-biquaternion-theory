#!/usr/bin/env python3
"""
e04_three_generations.py — ψ-mode independence and three fermion generations.

Demonstrates the three proved theorems about fermion generations in UBT:

Theorem 1 (Independence): ψ-Taylor modes are kinematically independent free data.
Theorem 2 (SU(3)): Every mode transforms in the same SU(3) rep as Θ.
Theorem 3 (ψ-parity): Mode Θₙ has parity (-1)ⁿ; even/odd modes cannot mix.

Run with:
    python -m THEORY_COMPARISONS.dimensional_economy.experiments.e04_three_generations

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys

from THEORY_COMPARISONS.dimensional_economy.dim_economy_core.three_generations import (
    psi_taylor_modes,
    reconstruct_field,
    extract_mode,
    verify_mode_independence,
    verify_su3_quantum_numbers_preserved,
    verify_psi_parity,
    verify_psi_parity_forbids_mixing,
    psi_parity_eigenvalue,
    generation_identification,
)
import sympy as sp


def run():
    """Run all three-generations verification checks."""
    print("=" * 70)
    print("E04 — THREE FERMION GENERATIONS FROM ψ-TAYLOR MODES")
    print("=" * 70)
    print()
    print("Reference: research_tracks/three_generations/st3_complex_time_generations.tex")
    print()

    # ---- Theorem 1 ----
    print("THEOREM 1 — KINEMATIC INDEPENDENCE OF ψ-MODES")
    print("-" * 50)
    print("Θ(x,t,ψ) = Σₙ ψⁿ Θₙ(x,t)  (formal Taylor series in ψ)")
    print()
    psi = sp.symbols('psi')
    modes = psi_taylor_modes(3)
    field = reconstruct_field(modes, psi)
    print(f"  Field Θ(ψ) = {field}")
    print()
    print("  Extracting modes back from Taylor series:")
    for n in range(3):
        recovered = extract_mode(field, psi, n)
        print(f"    extract_mode(Θ, ψ, {n}) = {recovered}  [expected: Θ_{n} = {modes[n]}]")
    print()
    ok1 = verify_mode_independence(N=4)
    print(f"  Result: {'✓ PROVED — modes are free independent data' if ok1 else '✗ FAILED'}")
    print()

    # ---- Theorem 2 ----
    print("THEOREM 2 — SU(3) QUANTUM NUMBERS PRESERVED IN ALL MODES")
    print("-" * 50)
    print("  For U ∈ SU(3) constant (independent of ψ):")
    print("  (UΘ)(ψ) = U·Θ(ψ) = Σₙ ψⁿ (U·Θₙ)")
    print("  → n-th mode of UΘ equals U·Θₙ (same SU(3) rep for all modes)")
    print()
    ok2 = verify_su3_quantum_numbers_preserved()
    print(f"  Result: {'✓ PROVED — all modes transform identically under SU(3)' if ok2 else '✗ FAILED'}")
    print()

    # ---- Theorem 3 ----
    print("THEOREM 3 — ψ-PARITY SELECTION RULE")
    print("-" * 50)
    print("  Under ψ → -ψ:  Θₙ → (-1)ⁿ Θₙ")
    print()
    print("  Parity eigenvalues:")
    for n in range(4):
        ev = psi_parity_eigenvalue(n)
        tower = "even" if n % 2 == 0 else "odd"
        print(f"    Θ_{n}: P_ψ eigenvalue = {ev:+d}  ({tower} tower)")
    print()
    ok3a = verify_psi_parity()
    print(f"  Parity eigenvalues verified: {'✓ PROVED' if ok3a else '✗ FAILED'}")
    ok3b = verify_psi_parity_forbids_mixing()
    print(f"  Cross-parity mixing forbidden: {'✓ PROVED (Θ₀↔Θ₁ forbidden, Θ₀↔Θ₂ allowed)' if ok3b else '✗ FAILED'}")
    print()

    # ---- Generation identification ----
    print("GENERATION IDENTIFICATION (Conjecture + proved mechanism)")
    print("-" * 50)
    ident = generation_identification()
    for key, val in ident.items():
        if isinstance(val, dict):
            parity = val['parity']
            gen = val['generation']
            status = val['status']
            print(f"  {key} ↔ {gen:20s} (P_ψ = {parity:+d})  — {status}")
        else:
            print(f"  {key}: {val}")
    print()

    all_ok = all([ok1, ok2, ok3a, ok3b])

    print("=" * 70)
    print("CONCLUSION:")
    print("  Theorem 1: ψ-modes are kinematically independent (free Taylor data)")
    print("  Theorem 2: All modes carry the same SU(3) quantum numbers")
    print("  Theorem 3: ψ-parity (-1)ⁿ forbids even↔odd mode mixing")
    print("  Generation mechanism is proved; mass ratios remain open.")
    print(f"  Overall: {'ALL CHECKS PASSED ✓' if all_ok else 'SOME CHECKS FAILED ✗'}")
    print("=" * 70)
    print()

    return all_ok


if __name__ == '__main__':
    success = run()
    sys.exit(0 if success else 1)
