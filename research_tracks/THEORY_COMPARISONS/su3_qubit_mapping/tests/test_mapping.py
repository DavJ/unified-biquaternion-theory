"""
test_mapping.py – Verify the SU(3) → 3-qubit lifting and algebraic properties.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import numpy as np
import pytest

from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.mapping import (
    embedding_matrix,
    color_projector,
    lift_to_8d,
    lift_gell_mann,
    all_gell_mann_qubit_decompositions,
    analytical_pauli_forms,
    color_neutrality_constraint,
    verify_su3_algebra_8d,
    verify_hermitian_traceless_8d,
    verify_embedding_isometric,
)
from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.qubit_ops import (
    pauli_matrices,
    tensor3,
    pauli_decompose,
    format_pauli_decomp,
)
from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.gell_mann import (
    gell_mann_matrices,
    structure_constants,
)


# ---------------------------------------------------------------------------
# Embedding matrix
# ---------------------------------------------------------------------------

def test_embedding_shape():
    """P has shape (8, 3)."""
    P = embedding_matrix()
    assert P.shape == (8, 3)


def test_embedding_isometric():
    """Pᵀ P = I₃ (isometric embedding)."""
    err = verify_embedding_isometric()
    assert err < 1e-14, f"P^† P ≠ I₃, max_err={err:.2e}"


def test_embedding_column_positions():
    """Color states embed at the correct qubit indices."""
    P = embedding_matrix()
    # r → |100⟩ = index 4
    assert P[4, 0] == 1.0 and np.sum(np.abs(P[:, 0])) == 1.0
    # g → |010⟩ = index 2
    assert P[2, 1] == 1.0 and np.sum(np.abs(P[:, 1])) == 1.0
    # b → |001⟩ = index 1
    assert P[1, 2] == 1.0 and np.sum(np.abs(P[:, 2])) == 1.0


# ---------------------------------------------------------------------------
# Color projector
# ---------------------------------------------------------------------------

def test_color_projector_is_projector():
    """Π² = Π (idempotent)."""
    Pi = color_projector()
    diff = Pi @ Pi - Pi
    assert np.allclose(diff, 0), "Π is not idempotent"


def test_color_projector_hermitian():
    """Π = Π†."""
    Pi = color_projector()
    assert np.allclose(Pi, Pi.conj().T), "Π is not Hermitian"


def test_color_projector_rank():
    """Π has rank 3 (projects onto the 3-dim color subspace)."""
    Pi = color_projector()
    rank = int(np.round(np.linalg.matrix_rank(Pi)))
    assert rank == 3, f"Expected rank 3, got {rank}"


# ---------------------------------------------------------------------------
# Lifted generators
# ---------------------------------------------------------------------------

def test_lifted_generators_count():
    """There are exactly 8 lifted generators."""
    L = lift_gell_mann()
    assert len(L) == 8


def test_lifted_generators_shape():
    """Each lifted generator is 8×8."""
    L = lift_gell_mann()
    for a, La in enumerate(L):
        assert La.shape == (8, 8), f"L_{a+1} has wrong shape"


def test_lifted_generators_hermitian_traceless():
    """Each L_a is Hermitian and traceless."""
    err = verify_hermitian_traceless_8d()
    assert err < 1e-12, f"Hermitian/traceless check failed: max_err={err:.2e}"


def test_lifted_generators_supported_on_color_subspace():
    """Each L_a satisfies Π L_a Π = L_a (acts only within color subspace)."""
    L = lift_gell_mann()
    Pi = color_projector()
    for a, La in enumerate(L):
        diff = Pi @ La @ Pi - La
        assert np.allclose(diff, 0), \
            f"L_{a+1} acts outside color subspace: max_err={np.max(np.abs(diff)):.2e}"


def test_su3_algebra_preserved():
    """[L_a, L_b] = 2i f_{abc} L_c for all a, b."""
    err = verify_su3_algebra_8d()
    assert err < 1e-12, f"SU(3) algebra not preserved in 8D: max_err={err:.2e}"


# ---------------------------------------------------------------------------
# Specific lifted generators (spot-checks)
# ---------------------------------------------------------------------------

def test_L1_explicit():
    """L₁ = |100⟩⟨010| + |010⟩⟨100| (connects r↔g with qubit 3 = |0⟩)."""
    L = lift_gell_mann()
    L1 = L[0]
    # The only non-zero entries should be at (4,2) and (2,4)
    assert abs(L1[4, 2] - 1.0) < 1e-14
    assert abs(L1[2, 4] - 1.0) < 1e-14
    # All other entries should be zero
    M = L1.copy()
    M[4, 2] = 0
    M[2, 4] = 0
    assert np.allclose(M, 0), "L₁ has unexpected non-zero entries"


def test_L3_diagonal():
    """L₃ = |100⟩⟨100| − |010⟩⟨010| (diagonal in color subspace)."""
    L = lift_gell_mann()
    L3 = L[2]
    assert abs(L3[4, 4] - 1.0) < 1e-14    # ⟨r| entry
    assert abs(L3[2, 2] + 1.0) < 1e-14    # ⟨g| entry
    assert abs(L3[1, 1]) < 1e-14           # ⟨b| entry (zero)
    # Off-diagonal color entries are zero
    assert abs(L3[4, 2]) < 1e-14
    assert abs(L3[2, 4]) < 1e-14


# ---------------------------------------------------------------------------
# Pauli decomposition
# ---------------------------------------------------------------------------

def test_pauli_decomposition_nonzero():
    """Every lifted generator has a non-empty Pauli decomposition."""
    decomps = all_gell_mann_qubit_decompositions()
    for a, d in enumerate(decomps):
        assert len(d) > 0, f"L_{a+1} has empty Pauli decomposition"


def test_pauli_decomposition_hermitian_reality():
    """Pauli decomposition coefficients of each Hermitian L_a are all real.

    For any Hermitian M = Σ c_{abc} σ_a⊗σ_b⊗σ_c, taking M = M† yields
    c_{abc} = c*_{abc} because (σ_a⊗σ_b⊗σ_c)† = σ_a⊗σ_b⊗σ_c for
    Hermitian Paulis.  Hence all expansion coefficients must be real.
    """
    decomps = all_gell_mann_qubit_decompositions(threshold=1e-12)
    for a, d in enumerate(decomps):
        for (i, j, k), coeff in d.items():
            assert abs(coeff.imag) < 1e-10, \
                f"L_{a+1}: non-real Pauli coeff for {(i,j,k)}: {coeff}"


def test_pauli_decomposition_reconstruction():
    """Reconstruct each L_a from its Pauli decomposition."""
    paulis = pauli_matrices()
    L = lift_gell_mann()
    decomps = all_gell_mann_qubit_decompositions(threshold=1e-12)
    for a, (La, d) in enumerate(zip(L, decomps)):
        reconstructed = sum(
            coeff * tensor3(paulis[i], paulis[j], paulis[k])
            for (i, j, k), coeff in d.items()
        )
        assert np.allclose(reconstructed, La, atol=1e-10), \
            f"Reconstruction of L_{a+1} failed"


def test_L1_analytical_pauli_form():
    """L₁ = ¼(σ_x⊗σ_x⊗I + σ_x⊗σ_x⊗σ_z + σ_y⊗σ_y⊗I + σ_y⊗σ_y⊗σ_z)."""
    paulis = pauli_matrices()
    I, X, Y, Z_ = paulis
    q = 0.25
    L1_analytic = q * (
        tensor3(X, X, I) + tensor3(X, X, Z_) +
        tensor3(Y, Y, I) + tensor3(Y, Y, Z_)
    )
    L = lift_gell_mann()
    assert np.allclose(L1_analytic, L[0], atol=1e-12), \
        "Analytical formula for L₁ does not match numerical result"


def test_L3_analytical_pauli_form():
    """L₃ = ¼(I⊗σ_z⊗I + I⊗σ_z⊗σ_z − σ_z⊗I⊗I − σ_z⊗I⊗σ_z)."""
    paulis = pauli_matrices()
    I, X, Y, Zp = paulis
    q = 0.25
    L3_analytic = q * (
        tensor3(I, Zp, I) + tensor3(I, Zp, Zp) -
        tensor3(Zp, I, I) - tensor3(Zp, I, Zp)
    )
    L = lift_gell_mann()
    assert np.allclose(L3_analytic, L[2], atol=1e-12), \
        "Analytical formula for L₃ does not match numerical result"


# ---------------------------------------------------------------------------
# Color neutrality constraint (9 → 8)
# ---------------------------------------------------------------------------

def test_color_neutrality_constraint_satisfied():
    """D_r + D_g + D_b = Π_color."""
    data = color_neutrality_constraint()
    assert data['constraint_ok'], "D_r + D_g + D_b ≠ Π_color"


def test_nine_generators_present():
    """The nine u(3) generators are returned."""
    data = color_neutrality_constraint()
    assert len(data['nine_generators']) == 9


def test_z_sum_in_color_subspace():
    """σ_z^(1) + σ_z^(2) + σ_z^(3) = I₃ in the color subspace."""
    data = color_neutrality_constraint()
    I3 = np.eye(3, dtype=complex)
    assert np.allclose(data['Zsum_in_color'], I3, atol=1e-12), \
        "σ_z sum in color subspace ≠ I₃"


def test_diagonal_generators_eigenvalues():
    """σ_z^(i) in the color subspace has the expected diagonal eigenvalues."""
    data = color_neutrality_constraint()
    # In (r,g,b) order:
    # Z1_color = diag(-1,+1,+1),  Z2 = diag(+1,-1,+1),  Z3 = diag(+1,+1,-1)
    expected_diags = {
        'Z1_color': np.array([-1., +1., +1.]),
        'Z2_color': np.array([+1., -1., +1.]),
        'Z3_color': np.array([+1., +1., -1.]),
    }
    for key, expected in expected_diags.items():
        diag_got = np.diag(data[key]).real
        assert np.allclose(diag_got, expected, atol=1e-12), \
            f"{key} diagonal {diag_got} ≠ expected {expected}"


def test_cartan_generators_proportional_to_gell_mann():
    """H₃ ∝ L₃ and H₈ ∝ L₈."""
    data = color_neutrality_constraint()
    L = lift_gell_mann()
    assert np.allclose(data['cartan_H3'], L[2], atol=1e-12), \
        "cartan_H3 ≠ L₃"
    assert np.allclose(data['cartan_H8'], L[7], atol=1e-12), \
        "cartan_H8 ≠ L₈"


def test_analytical_pauli_forms_match_numeric():
    """Verify that all 8 analytical Pauli forms match the numeric decompositions."""
    paulis = pauli_matrices()
    L = lift_gell_mann()
    analytic_forms = analytical_pauli_forms()
    for a, (La, form) in enumerate(zip(L, analytic_forms)):
        if form is None:
            continue
        # Reconstruct L_a from analytical form
        reconstructed = sum(
            coeff * tensor3(paulis[i], paulis[j], paulis[k])
            for (i, j, k), coeff in form.items()
        )
        assert np.allclose(reconstructed, La, atol=1e-10), \
            f"Analytical form for L_{a+1} does not match numerical result"


def test_off_diagonal_generators_zero_trace_in_color():
    """Off-diagonal lifted generators are traceless."""
    L = lift_gell_mann()
    for a in range(8):
        tr = np.trace(L[a])
        assert abs(tr) < 1e-12, f"L_{a+1} is not traceless: Tr={tr}"
