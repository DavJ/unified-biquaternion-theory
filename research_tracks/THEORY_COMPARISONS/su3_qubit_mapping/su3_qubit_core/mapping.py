"""
mapping.py – Homomorphism su(3) → End(ℂ²⊗ℂ²⊗ℂ²) via one-hot color encoding.

Construction
------------
One-hot color encoding:  φ: ℂ³ → ℂ²⊗ℂ²⊗ℂ²

    |r⟩  →  |100⟩  (qubit index 4)
    |g⟩  →  |010⟩  (qubit index 2)
    |b⟩  →  |001⟩  (qubit index 1)

The 3-qubit basis is ordered |q₁q₂q₃⟩ with index = 4q₁+2q₂+q₃ (big-endian).

Embedding matrix P (8×3):
    P[:, 0] = e₄   (r column)
    P[:, 1] = e₂   (g column)
    P[:, 2] = e₁   (b column)

Lifted generator: L_a = P λ_a Pᵀ  (8×8 matrix, acts only on color subspace)

Algebra preservation proof
--------------------------
Because Pᵀ P = I₃ (columns are orthonormal in ℂ⁸):
    [L_a, L_b] = P [λ_a, λ_b] Pᵀ = 2i f_{abc} L_c  ✓

The map λ_a → L_a is therefore a Lie algebra homomorphism
    φ: su(3) → End(ℂ²⊗ℂ²⊗ℂ²),   φ(λ_a) = L_a.

9 → 8 constraint (color neutrality)
-------------------------------------
u(3) on the color subspace has 9 generators {|α⟩⟨β| : α,β ∈ {r,g,b}}.
The three diagonal projectors D_r, D_g, D_b satisfy

    D_r + D_g + D_b = Π_color   (the projector onto the 3-dim color subspace)

This one constraint identifies the u(1) direction (overall phase generator),
and the remaining 8 generators span su(3).

In qubit language, the single-qubit σ_z operators restricted to the color
subspace satisfy:
    σ_z^(1)|_color = diag(-1,+1,+1)_{rgb}
    σ_z^(2)|_color = diag(+1,-1,+1)_{rgb}
    σ_z^(3)|_color = diag(+1,+1,-1)_{rgb}
    sum             = I₃  (identity on color subspace = the constraint)

The two traceless combinations give the Cartan generators:
    H₃ ∝ σ_z^(1) - σ_z^(2)  →  diag(-2,+2, 0) ∝ λ₃
    H₈ ∝ σ_z^(1)+σ_z^(2)-2σ_z^(3)  →  diag(-2,-2,+4) ∝ λ₈

Author: UBT Research Team
License: See repository LICENSE.md
"""

import numpy as np
from itertools import product as iproduct

from .gell_mann import gell_mann_matrices, structure_constants
from .qubit_ops import pauli_decompose, tensor3, pauli_matrices


# ---------------------------------------------------------------------------
# Embedding
# ---------------------------------------------------------------------------

def embedding_matrix():
    """Return the 8×3 one-hot color embedding matrix P.

    Column assignment:
        P[:, 0] = e₄  → |r⟩ maps to |100⟩
        P[:, 1] = e₂  → |g⟩ maps to |010⟩
        P[:, 2] = e₁  → |b⟩ maps to |001⟩

    Satisfies Pᵀ P = I₃ (isometric embedding).

    Returns
    -------
    numpy.ndarray, shape (8, 3), dtype complex
    """
    P = np.zeros((8, 3), dtype=complex)
    P[4, 0] = 1.0   # r → |100⟩
    P[2, 1] = 1.0   # g → |010⟩
    P[1, 2] = 1.0   # b → |001⟩
    return P


def color_projector():
    """Return the 8×8 projector Π onto the 3-dimensional color subspace.

    Π = |100⟩⟨100| + |010⟩⟨010| + |001⟩⟨001| = P Pᵀ

    Returns
    -------
    numpy.ndarray, shape (8, 8), dtype complex
    """
    P = embedding_matrix()
    return P @ P.T.conj()


# ---------------------------------------------------------------------------
# Lifting
# ---------------------------------------------------------------------------

def lift_to_8d(M3):
    """Lift a 3×3 matrix to an 8×8 matrix via the one-hot embedding.

    L = P M Pᵀ

    The result acts non-trivially only within the 3-dimensional color subspace
    spanned by {|100⟩, |010⟩, |001⟩}.

    Parameters
    ----------
    M3 : numpy.ndarray, shape (3, 3), dtype complex
        Matrix in the color basis (row/column order: r, g, b).

    Returns
    -------
    numpy.ndarray, shape (8, 8), dtype complex
    """
    P = embedding_matrix()
    return P @ M3 @ P.T.conj()


def lift_gell_mann():
    """Return the 8 lifted Gell-Mann generators L₁..L₈ as 8×8 matrices.

    L_a = P λ_a Pᵀ  satisfies  [L_a, L_b] = 2i f_{abc} L_c.

    Returns
    -------
    list of 8 numpy.ndarray, each shape (8, 8), dtype complex
        Index 0 → L₁, ..., 7 → L₈.
    """
    lam = gell_mann_matrices()
    return [lift_to_8d(l) for l in lam]


# ---------------------------------------------------------------------------
# Qubit (Pauli) decomposition of each lifted generator
# ---------------------------------------------------------------------------

def all_gell_mann_qubit_decompositions(threshold=1e-10):
    """Decompose each lifted generator L_a in the 3-qubit Pauli basis.

    L_a = Σ_{ijk} c_a[i,j,k] · (σ_i ⊗ σ_j ⊗ σ_k)

    where c_a[i,j,k] = Tr[L_a · (σ_i⊗σ_j⊗σ_k)] / 8.

    Parameters
    ----------
    threshold : float
        Coefficients with |c| < threshold are omitted.

    Returns
    -------
    list of dict
        decomps[a] maps (i,j,k) → coefficient for generator λ_{a+1}.
    """
    L = lift_gell_mann()
    return [pauli_decompose(La, threshold=threshold) for La in L]


# ---------------------------------------------------------------------------
# Analytical Pauli expressions (exact closed form for each generator)
# ---------------------------------------------------------------------------

def analytical_pauli_forms():
    """Return the exact analytical Pauli-tensor decomposition for each L_a.

    These are derived from the one-hot encoding and verified numerically.
    Each formula is given as a dict mapping (i,j,k) → exact rational/algebraic
    coefficient (stored as float).

    Derivation sketch for L₁ (λ₁ = |r⟩⟨g| + |g⟩⟨r|):
        L₁ = (σ⁺⊗σ⁻ + σ⁻⊗σ⁺) ⊗ P₀
           = ¼(σ_x⊗σ_x⊗I + σ_x⊗σ_x⊗σ_z + σ_y⊗σ_y⊗I + σ_y⊗σ_y⊗σ_z)

    where  σ⁺ = (σ_x − iσ_y)/2,  σ⁻ = (σ_x + iσ_y)/2,  P₀ = (I+σ_z)/2.

    Returns
    -------
    list of dict mapping (int, int, int) → float
        Length 8; index a corresponds to λ_{a+1}.
    """
    # Indices: I=0, X=1, Y=2, Z=3
    I, X, Y, Z = 0, 1, 2, 3
    q = 0.25  # universal prefactor 1/4

    forms = [
        # L₁ = λ₁ lifted:  ¼(XX⊗I + XX⊗Z + YY⊗I + YY⊗Z)
        {(X, X, I): q, (X, X, Z): q, (Y, Y, I): q, (Y, Y, Z): q},

        # L₂ = λ₂ lifted:  ¼(XY⊗I + XY⊗Z − YX⊗I − YX⊗Z)
        {(X, Y, I): q, (X, Y, Z): q, (Y, X, I): -q, (Y, X, Z): -q},

        # L₃ = λ₃ lifted:  ¼(I⊗Z⊗I + I⊗Z⊗Z − Z⊗I⊗I − Z⊗I⊗Z)
        {(I, Z, I): q, (I, Z, Z): q, (Z, I, I): -q, (Z, I, Z): -q},

        # L₄ = λ₄ lifted:  ¼(X⊗I⊗X + X⊗Z⊗X + Y⊗I⊗Y + Y⊗Z⊗Y)
        {(X, I, X): q, (X, Z, X): q, (Y, I, Y): q, (Y, Z, Y): q},

        # L₅ = λ₅ lifted:  ¼(X⊗I⊗Y + X⊗Z⊗Y − Y⊗I⊗X − Y⊗Z⊗X)
        {(X, I, Y): q, (X, Z, Y): q, (Y, I, X): -q, (Y, Z, X): -q},

        # L₆ = λ₆ lifted:  ¼(I⊗X⊗X + Z⊗X⊗X + I⊗Y⊗Y + Z⊗Y⊗Y)
        {(I, X, X): q, (Z, X, X): q, (I, Y, Y): q, (Z, Y, Y): q},

        # L₇ = λ₇ lifted:  ¼(I⊗X⊗Y − I⊗Y⊗X + Z⊗X⊗Y − Z⊗Y⊗X)
        {(I, X, Y): q, (I, Y, X): -q, (Z, X, Y): q, (Z, Y, X): -q},

        # L₈ = λ₈ lifted (coefficient 1/(2√3)):
        # (1/8√3)[I⊗I⊗I − 3·I⊗I⊗Z − I⊗Z⊗I + I⊗Z⊗Z
        #         − Z⊗I⊗I + Z⊗I⊗Z + Z⊗Z⊗I − Z⊗Z⊗Z − 4·...  ]
        # (computed numerically and stored below)
        None,   # filled by numeric fallback below
    ]

    # L₈ has a more involved pattern; fill from numeric decomposition.
    L8 = lift_to_8d(gell_mann_matrices()[7])
    forms[7] = pauli_decompose(L8, threshold=1e-12)

    return forms


# ---------------------------------------------------------------------------
# Color neutrality constraint
# ---------------------------------------------------------------------------

def color_neutrality_constraint():
    """Return data describing the 9→8 algebraic constraint.

    The 9 generators of u(3) on the 3-dimensional color subspace are:

        Off-diagonal (6):  L₁, L₂ (rg), L₄, L₅ (rb), L₆, L₇ (gb)
        Diagonal     (3):  D_r = |r⟩⟨r|, D_g = |g⟩⟨g|, D_b = |b⟩⟨b|

    The constraint that reduces u(3) → su(3):

        D_r + D_g + D_b = Π_color

    This identifies the single u(1) direction (overall-phase generator) and
    leaves 8 independent traceless generators = su(3).

    In single-qubit terms (within the color subspace):
        σ_z^(1)|_color + σ_z^(2)|_color + σ_z^(3)|_color = I₃

    The two linearly independent traceless combinations give the Cartan basis:
        H₃ = (1/2)(σ_z^(1) − σ_z^(2))|_color  ∝ λ₃
        H₈ = (1/(2√3))(σ_z^(1)+σ_z^(2)−2σ_z^(3))|_color  ∝ λ₈

    Returns
    -------
    dict with keys:
        'D_r', 'D_g', 'D_b' : ndarray (8,8) – color projectors
        'color_projector'    : ndarray (8,8) – Π = D_r+D_g+D_b
        'constraint_ok'      : bool – True if D_r+D_g+D_b = Π
        'u1_generator'       : ndarray (8,8) – the removed u(1) direction
        'cartan_H3'          : ndarray (8,8) – proportional to L₃
        'cartan_H8'          : ndarray (8,8) – proportional to L₈
        'Zsum_in_color'      : ndarray (3,3) – (Z₁+Z₂+Z₃) in color basis = I₃
        'Z1_color', 'Z2_color', 'Z3_color' : ndarray (3,3) – individual Z_i
        'nine_generators'    : list of 9 ndarray (8,8)
    """
    P = embedding_matrix()
    Pi = color_projector()

    # Diagonal color projectors
    D_r = lift_to_8d(np.diag([1., 0., 0.]).astype(complex))
    D_g = lift_to_8d(np.diag([0., 1., 0.]).astype(complex))
    D_b = lift_to_8d(np.diag([0., 0., 1.]).astype(complex))

    constraint_ok = bool(np.allclose(D_r + D_g + D_b, Pi))

    # Cartan generators (traceless combinations)
    #   H₃ ∝ D_r - D_g  (= L₃ since λ₃ = diag(1,-1,0) = e_rr - e_gg)
    #   H₈ ∝ (D_r+D_g-2D_b)/√3  (= L₈ since λ₈ = diag(1,1,-2)/√3)
    L = lift_gell_mann()
    cartan_H3 = L[2]   # L₃
    cartan_H8 = L[7]   # L₈

    # Single-qubit σ_z operators restricted to color subspace (3×3 matrices)
    I2 = np.eye(2, dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    Z1_full = tensor3(sz, I2, I2)
    Z2_full = tensor3(I2, sz, I2)
    Z3_full = tensor3(I2, I2, sz)

    Z1_color = P.T.conj() @ Z1_full @ P   # 3×3
    Z2_color = P.T.conj() @ Z2_full @ P   # 3×3
    Z3_color = P.T.conj() @ Z3_full @ P   # 3×3

    # Nine u(3) generators (as 8×8 matrices)
    nine = [L[0], L[1], L[3], L[4], L[5], L[6], D_r, D_g, D_b]

    return {
        'D_r': D_r,
        'D_g': D_g,
        'D_b': D_b,
        'color_projector': Pi,
        'constraint_ok': constraint_ok,
        'u1_generator': Pi,          # = D_r+D_g+D_b, the removed generator
        'cartan_H3': cartan_H3,
        'cartan_H8': cartan_H8,
        'Z1_color': Z1_color,
        'Z2_color': Z2_color,
        'Z3_color': Z3_color,
        'Zsum_in_color': Z1_color + Z2_color + Z3_color,   # = I₃
        'nine_generators': nine,
    }


# ---------------------------------------------------------------------------
# Algebra verification
# ---------------------------------------------------------------------------

def verify_su3_algebra_8d():
    """Verify [L_a, L_b] = 2i f_{abc} L_c for all a, b.

    Returns
    -------
    float
        Maximum entry-wise absolute residual; should be < 1e-12.
    """
    L = lift_gell_mann()
    f = structure_constants()
    n = 8
    max_err = 0.0
    for a, b in iproduct(range(n), range(n)):
        comm = L[a] @ L[b] - L[b] @ L[a]
        rhs = sum(2j * f[a, b, c] * L[c] for c in range(n))
        err = float(np.max(np.abs(comm - rhs)))
        max_err = max(max_err, err)
    return max_err


def verify_hermitian_traceless_8d():
    """Verify that each lifted generator L_a is Hermitian and traceless.

    Returns
    -------
    float
        Maximum combined residual; should be < 1e-12.
    """
    L = lift_gell_mann()
    max_err = 0.0
    for La in L:
        err_herm = float(np.max(np.abs(La - La.conj().T)))
        err_tr = abs(np.trace(La))
        max_err = max(max_err, err_herm, err_tr)
    return max_err


def verify_embedding_isometric():
    """Verify P^† P = I₃ (the embedding columns are orthonormal).

    Returns
    -------
    float
        Max deviation from identity; should be < 1e-15.
    """
    P = embedding_matrix()
    diff = P.T.conj() @ P - np.eye(3, dtype=complex)
    return float(np.max(np.abs(diff)))
