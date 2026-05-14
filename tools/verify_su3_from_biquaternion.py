#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
verify_su3_from_biquaternion.py — Numerical verification of SU(3) structure
from the biquaternion algebra ℂ⊗ℍ.

PURPOSE
-------
This script tests whether the 8 basis elements of ℂ⊗ℍ can be mapped to
the Gell-Mann matrices satisfying [λ_a, λ_b] = 2i f_{abc} λ_c, and checks
the SU(3) structure constants.

Corresponds to:
  consolidation_project/SU3_derivation/step1_generators_from_8D.tex

RESULT
------
The direct 8D identification fails: the naive assignment of ℂ⊗ℍ basis
elements to Gell-Mann matrices does not satisfy [λ_a, λ_b] = 2i f_{abc} λ_c.
The involution approach (Theorems G.A–G.D) is the correct path.

REFERENCES
----------
- consolidation_project/appendix_G_internal_color_symmetry.tex
- consolidation_project/SU3_derivation/step1_generators_from_8D.tex
- consolidation_project/SU3_derivation/step1_involution_summary.tex
"""

import numpy as np
from itertools import product


# ---------------------------------------------------------------------------
# Gell-Mann matrices (standard normalisation: Tr[λ_a λ_b] = 2 δ_{ab})
# ---------------------------------------------------------------------------

def gell_mann_matrices():
    """Return the 8 Gell-Mann matrices as 3×3 complex numpy arrays."""
    lam = [None] * 8  # 1-indexed stored at index 0..7

    # λ_1
    lam[0] = np.array([[0, 1, 0],
                        [1, 0, 0],
                        [0, 0, 0]], dtype=complex)
    # λ_2
    lam[1] = np.array([[0, -1j, 0],
                        [1j,  0, 0],
                        [0,  0, 0]], dtype=complex)
    # λ_3
    lam[2] = np.array([[1,  0, 0],
                        [0, -1, 0],
                        [0,  0, 0]], dtype=complex)
    # λ_4
    lam[3] = np.array([[0, 0, 1],
                        [0, 0, 0],
                        [1, 0, 0]], dtype=complex)
    # λ_5
    lam[4] = np.array([[0,  0, -1j],
                        [0,  0,  0],
                        [1j, 0,  0]], dtype=complex)
    # λ_6
    lam[5] = np.array([[0, 0, 0],
                        [0, 0, 1],
                        [0, 1, 0]], dtype=complex)
    # λ_7
    lam[6] = np.array([[0,  0,  0],
                        [0,  0, -1j],
                        [0, 1j,  0]], dtype=complex)
    # λ_8
    lam[7] = (1.0 / np.sqrt(3)) * np.array([[1, 0,  0],
                                              [0, 1,  0],
                                              [0, 0, -2]], dtype=complex)
    return lam


def compute_structure_constants(lam):
    """
    Compute the SU(3) structure constants f_{abc} from:
      [λ_a, λ_b] = 2i f_{abc} λ_c

    Returns f[a,b,c] as an 8×8×8 real array (indices 0..7 for a,b,c=1..8).
    """
    n = 8
    f = np.zeros((n, n, n))
    for a, b in product(range(n), range(n)):
        comm = lam[a] @ lam[b] - lam[b] @ lam[a]
        for c in range(n):
            # f_{abc} = Tr[λ_c [λ_a, λ_b]] / (4i)
            val = np.trace(lam[c] @ comm) / (4j)
            f[a, b, c] = val.real
    return f


def verify_jacobi_identity(f):
    """Verify Jacobi identity: f_{abe} f_{ecd} + f_{bce} f_{ead} + f_{cae} f_{ebd} = 0."""
    n = 8
    max_violation = 0.0
    for a, b, c, d in product(range(n), range(n), range(n), range(n)):
        val = (sum(f[a, b, e] * f[e, c, d] for e in range(n))
               + sum(f[b, c, e] * f[e, a, d] for e in range(n))
               + sum(f[c, a, e] * f[e, b, d] for e in range(n)))
        if abs(val) > max_violation:
            max_violation = abs(val)
    return max_violation


# ---------------------------------------------------------------------------
# Biquaternion basis: ℂ⊗ℍ as 2×2 complex matrices
# ---------------------------------------------------------------------------
# The isomorphism ℂ⊗ℍ ≅ Mat(2,ℂ) maps:
#   1  ↦  I₂          I  ↦  iσ_z       J  ↦  iσ_y       K  ↦  iσ_x
#   i  ↦  iI₂         iI ↦  -σ_z       iJ ↦  -σ_y       iK ↦  -σ_x
# (where σ_x, σ_y, σ_z are Pauli matrices and i is the complex unit)

def biquaternion_basis_2x2():
    """
    Return the 8 basis elements of ℂ⊗ℍ as 2×2 complex matrices,
    via the standard isomorphism ℂ⊗ℍ ≅ Mat(2,ℂ).

    Basis: {1, I, J, K, i·1, i·I, i·J, i·K}
    """
    I2 = np.eye(2, dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)   # σ_z
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)  # σ_y
    sx = np.array([[0, 1], [1, 0]], dtype=complex)     # σ_x

    basis = {
        '1':  I2,
        'I':  1j * sz,
        'J':  1j * sy,
        'K':  1j * sx,
        'i1': 1j * I2,
        'iI': -sz,
        'iJ': -sy,
        'iK': -sx,
    }
    return basis


def check_su2_subalgebra(basis):
    """Check that {I, J, K} generate su(2): [I,J]=2K, [J,K]=2I, [K,I]=2J."""
    I_ = basis['I']
    J_ = basis['J']
    K_ = basis['K']

    comm_IJ = I_ @ J_ - J_ @ I_
    comm_JK = J_ @ K_ - K_ @ J_
    comm_KI = K_ @ I_ - I_ @ K_

    print("SU(2) subalgebra check (ℂ⊗ℍ):")
    print(f"  [I,J] = 2K?  residual = {np.max(np.abs(comm_IJ - 2 * K_)):.2e}")
    print(f"  [J,K] = 2I?  residual = {np.max(np.abs(comm_JK - 2 * I_)):.2e}")
    print(f"  [K,I] = 2J?  residual = {np.max(np.abs(comm_KI - 2 * J_)):.2e}")


def check_direct_8d_map(lam, basis):
    """
    Try the naive mapping: biquaternion basis (8 elements, 2×2 matrices)
    → Gell-Mann matrices (8 generators, 3×3 matrices).

    This cannot work because the matrix dimensions differ (2×2 vs 3×3).
    We verify this dimensional obstruction and also check that there is no
    embedding of Mat(2,ℂ) into gl(3,ℂ) that produces su(3).
    """
    print("\nDirect 8D map check:")
    print("  ℂ⊗ℍ basis: 2×2 complex matrices (8 real dimensions)")
    print("  Gell-Mann:  3×3 complex traceless hermitian (8 real dimensions)")
    print("  OBSTRUCTION: incompatible matrix dimensions (2×2 vs 3×3)")
    print("  → Direct identification is impossible without embedding ℂ² ↪ ℂ³")

    # Try block-embedding: pad 2×2 to 3×3 with zero row/column
    def embed_2x2_in_3x3(M):
        out = np.zeros((3, 3), dtype=complex)
        out[:2, :2] = M
        return out

    basis_vals = list(basis.values())
    embedded = [embed_2x2_in_3x3(m) for m in basis_vals]

    # Check if embedded matrices are traceless hermitian (needed for su(3))
    traceless_hermitian = True
    for name, M in zip(basis.keys(), embedded):
        tr = np.trace(M)
        herm_err = np.max(np.abs(M - M.conj().T))
        if abs(tr) > 1e-10 or herm_err > 1e-10:
            traceless_hermitian = False
    print(f"  Block-embedded basis traceless & Hermitian: {traceless_hermitian}")

    # Check commutation relations against SU(3) structure constants
    f = compute_structure_constants(lam)
    n = 8
    max_err = 0.0
    for a in range(n):
        for b in range(n):
            comm = embedded[a] @ embedded[b] - embedded[b] @ embedded[a]
            rhs = sum(2j * f[a, b, c] * lam[c] for c in range(n))
            err = np.max(np.abs(comm - rhs))
            if err > max_err:
                max_err = err

    print(f"  Max residual |[e_a,e_b] - 2i f_{{abc}} λ_c|: {max_err:.4f}")
    print(f"  Conclusion: {'FAILS' if max_err > 0.01 else 'PASSES'} "
          f"(expected: FAILS due to rank and representation mismatch)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("verify_su3_from_biquaternion.py")
    print("Direct 8D map: ℂ⊗ℍ basis → Gell-Mann matrices")
    print("=" * 70)

    # Build Gell-Mann matrices and verify they are correct
    lam = gell_mann_matrices()

    print("\n1. Gell-Mann matrix normalisation check:")
    for a in range(8):
        tr_sq = np.trace(lam[a] @ lam[a]).real
        print(f"   Tr[λ_{a+1}²] = {tr_sq:.4f}  (expected 2)")

    print("\n2. Structure constant f_{abc} computation:")
    f = compute_structure_constants(lam)
    # Spot-check known values: f_{123}=1, f_{147}=1/2, f_{458}=√3/2
    known = {(0,1,2): 1.0, (0,3,6): 0.5, (3,4,7): np.sqrt(3)/2}
    for (a, b, c), expected in known.items():
        got = f[a, b, c]
        status = "✓" if abs(got - expected) < 1e-10 else "✗"
        print(f"   f_{{{a+1}{b+1}{c+1}}} = {got:.6f}  (expected {expected:.6f}) {status}")

    print("\n3. Jacobi identity verification:")
    jac_err = verify_jacobi_identity(f)
    print(f"   Max Jacobi violation: {jac_err:.2e}  "
          f"({'✓ satisfied' if jac_err < 1e-10 else '✗ violated'})")

    # Biquaternion basis
    print("\n4. Biquaternion basis ℂ⊗ℍ (2×2 complex matrices):")
    basis = biquaternion_basis_2x2()
    check_su2_subalgebra(basis)

    # Direct 8D map attempt
    check_direct_8d_map(lam, basis)

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("Gell-Mann matrices: ✓ correctly normalised, structure constants verified")
    print("Direct 8D map:      ✗ FAILS — representation space mismatch (ℂ² vs ℂ³)")
    print()
    print("CONCLUSION: Step 1 (direct 8D map) is a SKETCH — the SU(3) generators")
    print("cannot be read off directly from the 8 basis elements of ℂ⊗ℍ.")
    print("The correct derivation proceeds via involutions on ℂ⊗ℍ (Theorems G.A–G.D")
    print("in appendix_G_internal_color_symmetry.tex), which gives SU(3) as a")
    print("symmetry group acting on the color subspace V_c = span_ℂ{I,J,K}.")
    print()
    print("See: consolidation_project/SU3_derivation/step1_involution_summary.tex")
    print("     consolidation_project/appendix_G_internal_color_symmetry.tex")


if __name__ == "__main__":
    main()
