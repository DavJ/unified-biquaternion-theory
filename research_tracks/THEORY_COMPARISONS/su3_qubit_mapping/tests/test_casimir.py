"""
test_casimir.py – Verify Casimir operators in 3D and 8D representations.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import numpy as np
import pytest

from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.casimir import (
    casimir_c1_3d,
    casimir_c2_3d,
    casimir_c1_8d,
    casimir_c2_8d,
    casimir_c1_qubit_decomp,
    casimir_c2_qubit_decomp,
    casimir_eigenvalue_c1,
    casimir_eigenvalue_c2,
    verify_c1_commutes_with_generators,
    verify_c2_commutes_with_generators,
    verify_c1_proportional_to_projector,
    verify_c2_proportional_to_projector,
)
from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.mapping import (
    color_projector,
    lift_gell_mann,
)
from THEORY_COMPARISONS.su3_qubit_mapping.su3_qubit_core.qubit_ops import (
    pauli_matrices,
    tensor3,
)


# ---------------------------------------------------------------------------
# 3×3 quadratic Casimir
# ---------------------------------------------------------------------------

def test_c1_3d_proportional_to_identity():
    """C₁ = (1/4)Σλ_a² = (4/3) I₃ in the fundamental representation."""
    C1 = casimir_c1_3d()
    I3 = np.eye(3, dtype=complex)
    diff = C1 - (4.0 / 3.0) * I3
    assert np.allclose(diff, 0, atol=1e-12), \
        f"C₁ ≠ (4/3)I₃, max_diff={np.max(np.abs(diff)):.2e}"


def test_c1_3d_eigenvalue():
    """Eigenvalue of C₁ in the fundamental rep is 4/3."""
    C1 = casimir_c1_3d()
    evs = np.linalg.eigvalsh(C1.real)
    assert np.allclose(evs, 4.0 / 3.0, atol=1e-12), \
        f"C₁ eigenvalues {evs} ≠ 4/3"


# ---------------------------------------------------------------------------
# 3×3 cubic Casimir
# ---------------------------------------------------------------------------

def test_c2_3d_proportional_to_identity():
    """C₂ = d_{abc}λ_aλ_bλ_c is proportional to I₃ in the fundamental rep."""
    C2 = casimir_c2_3d()
    # The off-diagonal entries must be zero
    off_diag = C2 - np.diag(np.diag(C2))
    assert np.allclose(off_diag, 0, atol=1e-10), \
        f"C₂ off-diagonal nonzero: max={np.max(np.abs(off_diag)):.2e}"
    # All diagonal entries must be equal
    diag = np.diag(C2).real
    assert np.allclose(diag, diag[0], atol=1e-10), \
        f"C₂ diagonal entries not equal: {diag}"


# ---------------------------------------------------------------------------
# 8×8 quadratic Casimir
# ---------------------------------------------------------------------------

def test_c1_8d_proportional_to_color_projector():
    """C₁^(8) = (4/3) Π_color."""
    err = verify_c1_proportional_to_projector()
    assert err < 1e-12, f"C₁^(8) ≠ (4/3)Π_color, max_err={err:.2e}"


def test_c1_8d_eigenvalue_in_color_subspace():
    """C₁^(8) has eigenvalue 4/3 on the color subspace."""
    ev = casimir_eigenvalue_c1()
    assert abs(ev - 4.0 / 3.0) < 1e-12, \
        f"C₁ eigenvalue {ev:.6f} ≠ 4/3"


def test_c1_8d_zero_outside_color():
    """C₁^(8) is zero outside the color subspace."""
    C1 = casimir_c1_8d()
    Pi = color_projector()
    # C1 = (4/3) Pi, so C1 (I-Pi) = 0
    I8 = np.eye(8, dtype=complex)
    proj_comp = I8 - Pi
    outside = C1 @ proj_comp
    assert np.allclose(outside, 0, atol=1e-12), \
        f"C₁^(8) nonzero outside color subspace"


def test_c1_commutes_with_all_generators():
    """[C₁^(8), L_a] = 0 for all a."""
    err = verify_c1_commutes_with_generators()
    assert err < 1e-12, f"[C₁, L_a] ≠ 0, max_err={err:.2e}"


# ---------------------------------------------------------------------------
# 8×8 cubic Casimir
# ---------------------------------------------------------------------------

def test_c2_8d_proportional_to_color_projector():
    """C₂^(8) = c₂ · Π_color for some constant c₂."""
    c2, err = verify_c2_proportional_to_projector()
    assert err < 1e-10, \
        f"C₂^(8) not proportional to Π_color: max_err={err:.2e}"


def test_c2_commutes_with_all_generators():
    """[C₂^(8), L_a] = 0 for all a."""
    err = verify_c2_commutes_with_generators()
    assert err < 1e-10, f"[C₂, L_a] ≠ 0, max_err={err:.2e}"


# ---------------------------------------------------------------------------
# Qubit (Pauli) decomposition of Casimirs
# ---------------------------------------------------------------------------

def test_c1_qubit_decomp_nonempty():
    """C₁^(8) has a non-empty Pauli decomposition."""
    d = casimir_c1_qubit_decomp()
    assert len(d) > 0, "C₁ Pauli decomposition is empty"


def test_c2_qubit_decomp_nonempty():
    """C₂^(8) has a non-empty Pauli decomposition."""
    d = casimir_c2_qubit_decomp()
    assert len(d) > 0, "C₂ Pauli decomposition is empty"


def test_c1_qubit_decomp_reconstruction():
    """Reconstruct C₁^(8) from its Pauli decomposition."""
    paulis = pauli_matrices()
    C1 = casimir_c1_8d()
    d = casimir_c1_qubit_decomp(threshold=1e-12)
    reconstructed = sum(
        coeff * tensor3(paulis[i], paulis[j], paulis[k])
        for (i, j, k), coeff in d.items()
    )
    assert np.allclose(reconstructed, C1, atol=1e-10), \
        "C₁ reconstruction from Pauli decomp failed"


def test_c1_qubit_decomp_analytical():
    """C₁^(8) Pauli decomposition matches analytical formula for Π_color.

    C₁^(8) = (4/3) Π_color
    Π_color = (1/8)[3·I⊗I⊗I + I⊗I⊗Z + I⊗Z⊗I + Z⊗I⊗I
                    − I⊗Z⊗Z − Z⊗I⊗Z − Z⊗Z⊗I − 3·Z⊗Z⊗Z]

    Derivation: Π = P₁⊗P₀⊗P₀ + P₀⊗P₁⊗P₀ + P₀⊗P₀⊗P₁ with
    P₀=(I+Z)/2 and P₁=(I−Z)/2.  Expanding and collecting terms gives
    the coefficients 3, 1, 1, 1, −1, −1, −1, −3 for the 8 Pauli products.
    """
    paulis = pauli_matrices()
    I, X, Y, Z = paulis
    # Π_color from the Pauli basis (coefficient of Z⊗Z⊗Z is −3, not −1)
    Pi_analytic = (1.0 / 8.0) * (
        3 * tensor3(I, I, I)
        + tensor3(I, I, Z)
        + tensor3(I, Z, I)
        + tensor3(Z, I, I)
        - tensor3(I, Z, Z)
        - tensor3(Z, I, Z)
        - tensor3(Z, Z, I)
        - 3 * tensor3(Z, Z, Z)
    )
    Pi = color_projector()
    assert np.allclose(Pi_analytic, Pi, atol=1e-12), \
        "Analytical Π_color formula does not match numerical result"

    C1 = casimir_c1_8d()
    C1_analytic = (4.0 / 3.0) * Pi_analytic
    assert np.allclose(C1_analytic, C1, atol=1e-12), \
        "Analytical C₁ formula does not match numerical result"


def test_casimir_eigenvalues_consistent():
    """The C₁ and C₂ eigenvalues in 3D and 8D representations are consistent."""
    ev_c1_3d = float(np.diag(casimir_c1_3d()).real[0])
    ev_c1_8d = casimir_eigenvalue_c1()
    assert abs(ev_c1_3d - ev_c1_8d) < 1e-12, \
        f"C₁ eigenvalue mismatch: 3D={ev_c1_3d}, 8D={ev_c1_8d}"

    ev_c2_3d = float(np.diag(casimir_c2_3d()).real[0])
    ev_c2_8d = casimir_eigenvalue_c2()
    assert abs(ev_c2_3d - ev_c2_8d) < 1e-9, \
        f"C₂ eigenvalue mismatch: 3D={ev_c2_3d:.6f}, 8D={ev_c2_8d:.6f}"
