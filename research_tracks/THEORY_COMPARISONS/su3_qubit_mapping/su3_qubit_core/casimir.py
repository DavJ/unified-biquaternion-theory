"""
casimir.py – Casimir operators of su(3) in the 3D and 8D representations.

Definitions
-----------
Quadratic Casimir:  C₁ = (1/4) Σ_a λ_a²
    Fundamental (3D):  C₁ = (4/3) I₃
    Lifted (8D):       C₁^(8) = (4/3) Π_color

Cubic Casimir:  C₂ = d_{abc} λ_a λ_b λ_c   (sum over all a,b,c)
    d_{abc} are the fully symmetric structure constants.
    Fundamental (3D):  C₂ = c₂ I₃  for some constant c₂ (computed numerically)
    Lifted (8D):       C₂^(8) = c₂ Π_color

Both Casimirs commute with all generators: [C, L_a] = 0.

In the qubit representation, the Casimirs are expressed via the Pauli
decomposition of Π_color:

    Π_color = (1/8)[3·I⊗I⊗I
                    + I⊗I⊗Z + I⊗Z⊗I + Z⊗I⊗I
                    − I⊗Z⊗Z − Z⊗I⊗Z − Z⊗Z⊗I
                    − 3·Z⊗Z⊗Z]

Author: UBT Research Team
License: See repository LICENSE.md
"""

import numpy as np
from itertools import product as iproduct

from .gell_mann import gell_mann_matrices, symmetric_d_tensor
from .mapping import (lift_gell_mann, color_projector, embedding_matrix,
                      lift_to_8d)
from .qubit_ops import pauli_decompose


# ---------------------------------------------------------------------------
# 3×3 Casimirs (fundamental representation)
# ---------------------------------------------------------------------------

def casimir_c1_3d(lam=None):
    """Quadratic Casimir C₁ = (1/4) Σ_a λ_a² in the 3×3 fundamental rep.

    Expected result: C₁ = (4/3) I₃.

    Parameters
    ----------
    lam : list of ndarray, optional
        Gell-Mann matrices; computed fresh if None.

    Returns
    -------
    numpy.ndarray, shape (3, 3), dtype complex
    """
    if lam is None:
        lam = gell_mann_matrices()
    return (1.0 / 4.0) * sum(l @ l for l in lam)


def casimir_c2_3d(lam=None, d=None):
    """Cubic Casimir C₂ = d_{abc} λ_a λ_b λ_c in the 3×3 fundamental rep.

    The sum runs over all a, b, c ∈ {0,..,7}.
    Expected result: C₂ = c₂ I₃ for constant c₂ (characteristic of the rep).

    Parameters
    ----------
    lam : list of ndarray, optional
        Gell-Mann matrices; computed fresh if None.
    d   : ndarray (8,8,8), optional
        Symmetric d-tensor; computed fresh if None.

    Returns
    -------
    numpy.ndarray, shape (3, 3), dtype complex
    """
    if lam is None:
        lam = gell_mann_matrices()
    if d is None:
        d = symmetric_d_tensor(lam)
    C2 = np.zeros((3, 3), dtype=complex)
    for a, b, c in iproduct(range(8), range(8), range(8)):
        dabc = d[a, b, c]
        if abs(dabc) > 1e-12:
            C2 += dabc * (lam[a] @ lam[b] @ lam[c])
    return C2


# ---------------------------------------------------------------------------
# 8×8 Casimirs (lifted representation)
# ---------------------------------------------------------------------------

def casimir_c1_8d():
    """Quadratic Casimir C₁^(8) = (1/4) Σ_a L_a² in the 8×8 lifted rep.

    Expected result: C₁^(8) = (4/3) Π_color.

    Returns
    -------
    numpy.ndarray, shape (8, 8), dtype complex
    """
    L = lift_gell_mann()
    return (1.0 / 4.0) * sum(La @ La for La in L)


def casimir_c2_8d(d=None):
    """Cubic Casimir C₂^(8) = d_{abc} L_a L_b L_c in the 8×8 lifted rep.

    Expected result: C₂^(8) = c₂ Π_color (c₂ same as in 3D rep).

    Parameters
    ----------
    d : ndarray (8,8,8), optional
        Symmetric d-tensor; computed fresh if None.

    Returns
    -------
    numpy.ndarray, shape (8, 8), dtype complex
    """
    L = lift_gell_mann()
    if d is None:
        d = symmetric_d_tensor()
    C2 = np.zeros((8, 8), dtype=complex)
    for a, b, c in iproduct(range(8), range(8), range(8)):
        dabc = d[a, b, c]
        if abs(dabc) > 1e-12:
            C2 += dabc * (L[a] @ L[b] @ L[c])
    return C2


# ---------------------------------------------------------------------------
# Qubit representation of the Casimirs
# ---------------------------------------------------------------------------

def casimir_c1_qubit_decomp(threshold=1e-10):
    """Pauli decomposition of C₁^(8) in the 3-qubit basis.

    C₁^(8) = (4/3) Π_color, so the Pauli decomposition follows from Π_color.

    Returns
    -------
    dict mapping (int, int, int) → float
        Non-zero Pauli coefficients of C₁^(8).
    """
    C1 = casimir_c1_8d()
    return pauli_decompose(C1, threshold=threshold)


def casimir_c2_qubit_decomp(threshold=1e-10):
    """Pauli decomposition of C₂^(8) in the 3-qubit basis.

    Returns
    -------
    dict mapping (int, int, int) → float
        Non-zero Pauli coefficients of C₂^(8).
    """
    C2 = casimir_c2_8d()
    return pauli_decompose(C2, threshold=threshold)


def casimir_eigenvalue_c1():
    """Return the eigenvalue of C₁ in the fundamental (color) subspace.

    C₁|ψ⟩ = eigenvalue · |ψ⟩  for any |ψ⟩ in the color subspace.

    Returns
    -------
    float
        Expected: 4/3.
    """
    C1 = casimir_c1_8d()
    Pi = color_projector()
    # C1 = ev * Pi; extract ev from the (4,4) entry which is non-zero in Pi
    # (row 4, col 4 corresponds to |100⟩ = |r⟩)
    ev = (C1[4, 4] / Pi[4, 4]).real
    return float(ev)


def casimir_eigenvalue_c2():
    """Return the eigenvalue of C₂ in the fundamental (color) subspace.

    Returns
    -------
    float
    """
    C2 = casimir_c2_8d()
    Pi = color_projector()
    ev = (C2[4, 4] / Pi[4, 4]).real
    return float(ev)


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_c1_commutes_with_generators(tol=1e-10):
    """Check [C₁^(8), L_a] = 0 for all a.

    Returns
    -------
    float
        Maximum entry-wise absolute residual; should be < tol.
    """
    C1 = casimir_c1_8d()
    L = lift_gell_mann()
    max_err = 0.0
    for La in L:
        comm = C1 @ La - La @ C1
        max_err = max(max_err, float(np.max(np.abs(comm))))
    return max_err


def verify_c2_commutes_with_generators(tol=1e-10):
    """Check [C₂^(8), L_a] = 0 for all a.

    Returns
    -------
    float
        Maximum entry-wise absolute residual; should be < tol.
    """
    C2 = casimir_c2_8d()
    L = lift_gell_mann()
    max_err = 0.0
    for La in L:
        comm = C2 @ La - La @ C2
        max_err = max(max_err, float(np.max(np.abs(comm))))
    return max_err


def verify_c1_proportional_to_projector(tol=1e-10):
    """Check C₁^(8) = (4/3) Π_color.

    Returns
    -------
    float
        Maximum entry-wise absolute residual; should be < tol.
    """
    C1 = casimir_c1_8d()
    Pi = color_projector()
    diff = C1 - (4.0 / 3.0) * Pi
    return float(np.max(np.abs(diff)))


def verify_c2_proportional_to_projector(tol=1e-10):
    """Check C₂^(8) = c₂ · Π_color for some scalar c₂.

    Returns
    -------
    tuple (float, float)
        (c₂, max_residual).  If max_residual < tol the check passes.
    """
    C2 = casimir_c2_8d()
    Pi = color_projector()
    # Extract c₂ from a non-zero diagonal entry of Π
    ev = float(C2[4, 4].real / Pi[4, 4].real)
    diff = C2 - ev * Pi
    return ev, float(np.max(np.abs(diff)))
