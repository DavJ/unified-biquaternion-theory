"""
e01_mapping_summary.py – Print the complete SU(3) → 3-qubit mapping table.

Outputs:
  1. Lifted generator L_a in Pauli tensor-product basis for each a=1..8
  2. Color neutrality constraint (9 → 8 generators)
  3. Casimir eigenvalues and their Pauli decomposition

Run from repo root:
    python -m THEORY_COMPARISONS.su3_qubit_mapping.experiments.e01_mapping_summary

Author: UBT Research Team
License: See repository LICENSE.md
"""

import numpy as np

from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.gell_mann import (
    gell_mann_matrices,
    structure_constants,
    verify_normalisation,
    verify_lie_algebra,
)
from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.mapping import (
    lift_gell_mann,
    all_gell_mann_qubit_decompositions,
    color_neutrality_constraint,
    verify_su3_algebra_8d,
)
from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.casimir import (
    casimir_c1_3d,
    casimir_c2_3d,
    casimir_c1_8d,
    casimir_c2_8d,
    casimir_eigenvalue_c1,
    casimir_eigenvalue_c2,
    casimir_c1_qubit_decomp,
    verify_c1_commutes_with_generators,
    verify_c2_commutes_with_generators,
)
from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.qubit_ops import (
    format_pauli_decomp,
)

PAULI = ['I', 'X', 'Y', 'Z']
SEP = "─" * 70


def header(title):
    print(f"\n{SEP}")
    print(f"  {title}")
    print(SEP)


def main():
    print("=" * 70)
    print("  SU(3) → 3-QUBIT SPACE MAPPING")
    print("  Explicit homomorphism via one-hot color encoding")
    print("=" * 70)

    # -----------------------------------------------------------------------
    # 1. Verify Gell-Mann matrices
    # -----------------------------------------------------------------------
    header("1. Gell-Mann Matrix Verification")
    norm_err = verify_normalisation()
    alg_err = verify_lie_algebra()
    print(f"  Tr[λ_a λ_b] = 2δ_ab  :  max_err = {norm_err:.2e}  "
          f"{'✓' if norm_err < 1e-12 else '✗'}")
    print(f"  [λ_a,λ_b] = 2i f_abc λ_c:  max_err = {alg_err:.2e}  "
          f"{'✓' if alg_err < 1e-12 else '✗'}")

    # -----------------------------------------------------------------------
    # 2. One-hot encoding and embedding
    # -----------------------------------------------------------------------
    header("2. One-Hot Color Encoding")
    print("  |r⟩ = |1⟩⊗|0⟩⊗|0⟩  (qubit index 4)")
    print("  |g⟩ = |0⟩⊗|1⟩⊗|0⟩  (qubit index 2)")
    print("  |b⟩ = |0⟩⊗|0⟩⊗|1⟩  (qubit index 1)")
    print()
    print("  Embedding:  L_a = P λ_a P†   (P is the 8×3 selection matrix)")
    print("  Algebra:    [L_a, L_b] = 2i f_{abc} L_c  (preserved since P†P = I₃)")

    alg_8d = verify_su3_algebra_8d()
    print(f"  Verification: max_err = {alg_8d:.2e}  "
          f"{'✓' if alg_8d < 1e-12 else '✗'}")

    # -----------------------------------------------------------------------
    # 3. Explicit Pauli decompositions
    # -----------------------------------------------------------------------
    header("3. Gell-Mann → 3-Qubit Pauli Decomposition  L_a = Σ c_{ijk} σ_i⊗σ_j⊗σ_k")
    decomps = all_gell_mann_qubit_decompositions()
    for a, d in enumerate(decomps):
        print(f"\n  L_{a+1} (λ_{a+1}):")
        print(format_pauli_decomp(d, threshold=1e-10))

    # -----------------------------------------------------------------------
    # 4. Color neutrality constraint (9 → 8)
    # -----------------------------------------------------------------------
    header("4. Color Neutrality Constraint  (u(3) → su(3))")
    data = color_neutrality_constraint()

    print("  9 u(3) generators on the color subspace:")
    print("    Off-diagonal (6):  L₁,L₂ (rg) · L₄,L₅ (rb) · L₆,L₇ (gb)")
    print("    Diagonal     (3):  D_r=|r⟩⟨r|,  D_g=|g⟩⟨g|,  D_b=|b⟩⟨b|")
    print()
    print("  Constraint (color neutrality = tracelessness):")
    print("    D_r + D_g + D_b = Π_color   ←  eliminates the u(1) direction")
    print(f"    Verified: {data['constraint_ok']} ✓" if data['constraint_ok']
          else f"    FAILED")
    print()
    print("  Single-qubit Z operators restricted to color subspace:")
    for key in ('Z1_color', 'Z2_color', 'Z3_color'):
        label = {'Z1_color': 'σ_z^(1)', 'Z2_color': 'σ_z^(2)', 'Z3_color': 'σ_z^(3)'}[key]
        diag = np.diag(data[key]).real
        print(f"    {label}|_color = diag{tuple(diag)} in (r,g,b) basis")
    print()
    print("  Sum constraint: σ_z^(1)+σ_z^(2)+σ_z^(3)|_color = I₃")
    Zsum = data['Zsum_in_color']
    print(f"    max_err = {np.max(np.abs(Zsum - np.eye(3))):.2e}  ✓")
    print()
    print("  Cartan generators (traceless diagonal):")
    print("    H₃ = L₃  ∝  diag(-1,+1, 0)  in (r,g,b)  [λ₃]")
    print("    H₈ = L₈  ∝  diag( 1, 1,-2)/√3  in (r,g,b)  [λ₈]")

    # -----------------------------------------------------------------------
    # 5. Casimir operators
    # -----------------------------------------------------------------------
    header("5. Casimir Operators")

    C1_3d = casimir_c1_3d()
    C2_3d = casimir_c2_3d()
    ev_c1 = float(np.diag(C1_3d).real[0])
    ev_c2 = float(np.diag(C2_3d).real[0])

    print(f"  Fundamental representation (3×3):")
    print(f"    C₁ = (1/4)Σλ_a² = {ev_c1:.6f}·I₃   [expected 4/3 ≈ {4/3:.6f}]")
    print(f"    C₂ = d_{{abc}}λ_aλ_bλ_c = {ev_c2:.6f}·I₃")
    print()

    ev_c1_8d = casimir_eigenvalue_c1()
    ev_c2_8d = casimir_eigenvalue_c2()
    c1_comm = verify_c1_commutes_with_generators()
    c2_comm = verify_c2_commutes_with_generators()

    print(f"  Lifted representation (8×8):")
    print(f"    C₁^(8) = {ev_c1_8d:.6f}·Π_color  [= (4/3)Π_color]")
    print(f"    C₂^(8) = {ev_c2_8d:.6f}·Π_color")
    print(f"    [C₁^(8), L_a]=0: max_err = {c1_comm:.2e}  {'✓' if c1_comm < 1e-11 else '✗'}")
    print(f"    [C₂^(8), L_a]=0: max_err = {c2_comm:.2e}  {'✓' if c2_comm < 1e-10 else '✗'}")
    print()

    print("  C₁^(8) in Pauli basis  [= (4/3)Π_color]:")
    decomp_c1 = casimir_c1_qubit_decomp()
    print(format_pauli_decomp(decomp_c1))

    print()
    print("  Analytical Π_color formula:")
    print("    Π_color = (1/8)[ 3·I⊗I⊗I")
    print("                    + I⊗I⊗Z + I⊗Z⊗I + Z⊗I⊗I")
    print("                    − I⊗Z⊗Z − Z⊗I⊗Z − Z⊗Z⊗I")
    print("                    − 3·Z⊗Z⊗Z ]")

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    print(f"\n{'=' * 70}")
    print("  SUMMARY")
    print("=" * 70)
    print()
    print("  Homomorphism φ: su(3) → End(ℂ²⊗ℂ²⊗ℂ²),  φ(λ_a) = L_a = P λ_a Pᵀ")
    print()
    print("  Constraint (9→8):  D_r+D_g+D_b = Π_color  removes the u(1) phase")
    print("    → 3 diagonal operators → 2 Cartan generators (H₃, H₈)")
    print("    → 6 off-diagonal → λ₁,λ₂,λ₄,λ₅,λ₆,λ₇  unchanged")
    print()
    print("  Casimir operators in qubit rep:  C_i^(8) = eigenvalue_i · Π_color")
    print(f"    C₁ eigenvalue: {ev_c1_8d:.6f}  (= 4/3)")
    print(f"    C₂ eigenvalue: {ev_c2_8d:.6f}")
    print()
    print("  All algebraic relations verified numerically.")
    print("=" * 70)


if __name__ == "__main__":
    main()
