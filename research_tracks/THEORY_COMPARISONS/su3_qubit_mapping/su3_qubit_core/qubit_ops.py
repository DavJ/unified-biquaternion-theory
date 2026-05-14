"""
qubit_ops.py – 3-qubit Pauli operator utilities.

The 3-qubit space ℂ²⊗ℂ²⊗ℂ² has computational basis:
    |q₁q₂q₃⟩,  q_i ∈ {0,1},  index = 4q₁ + 2q₂ + q₃  (big-endian)

Conventions
-----------
    |0⟩ = (1,0)ᵀ,  |1⟩ = (0,1)ᵀ
    σ₀ = I₂,  σ₁ = σ_x,  σ₂ = σ_y,  σ₃ = σ_z

Basis operators: σ_a ⊗ σ_b ⊗ σ_c,  a,b,c ∈ {0,1,2,3}  (64 total)

Decomposition: M = Σ_{abc} coeff(a,b,c) · σ_a⊗σ_b⊗σ_c
               coeff(a,b,c) = Tr[M · (σ_a⊗σ_b⊗σ_c)] / 8

Author: UBT Research Team
License: See repository LICENSE.md
"""

import numpy as np
from itertools import product as iproduct

# Labels for Pauli indices
_PAULI_LABELS = ['I', 'X', 'Y', 'Z']


# ---------------------------------------------------------------------------
# Pauli matrices
# ---------------------------------------------------------------------------

def pauli_matrices():
    """Return [σ₀, σ_x, σ_y, σ_z] as 2×2 complex numpy arrays.

    Returns
    -------
    list of 4 numpy.ndarray, each shape (2, 2), dtype complex
        Index 0 → I,  1 → σ_x,  2 → σ_y,  3 → σ_z.
    """
    I2 = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return [I2, sx, sy, sz]


# ---------------------------------------------------------------------------
# Tensor products
# ---------------------------------------------------------------------------

def tensor3(A, B, C):
    """Compute A ⊗ B ⊗ C as an 8×8 complex matrix.

    Parameters
    ----------
    A, B, C : numpy.ndarray, shape (2, 2)
        Qubit operators (qubit 1, qubit 2, qubit 3).

    Returns
    -------
    numpy.ndarray, shape (8, 8), dtype complex
    """
    return np.kron(np.kron(A, B), C)


# ---------------------------------------------------------------------------
# Pauli basis and decomposition
# ---------------------------------------------------------------------------

def pauli_basis_3qubit():
    """Return all 64 Pauli tensor-product basis operators for 3 qubits.

    Returns
    -------
    list of ((int, int, int), numpy.ndarray)
        Each entry is ((a, b, c), matrix) where matrix = σ_a ⊗ σ_b ⊗ σ_c.
    """
    paulis = pauli_matrices()
    return [((a, b, c), tensor3(paulis[a], paulis[b], paulis[c]))
            for a, b, c in iproduct(range(4), range(4), range(4))]


def pauli_decompose(M, threshold=1e-12):
    """Decompose an 8×8 matrix in the 3-qubit Pauli tensor-product basis.

    M = Σ_{a,b,c} coeff(a,b,c) · (σ_a ⊗ σ_b ⊗ σ_c)

    where  coeff(a,b,c) = Tr[M · (σ_a ⊗ σ_b ⊗ σ_c)] / 8.

    Parameters
    ----------
    M : numpy.ndarray, shape (8, 8)
        Matrix to decompose.
    threshold : float, optional
        Coefficients with |coeff| < threshold are omitted (default 1e-12).

    Returns
    -------
    dict mapping (int, int, int) → complex
        Keys (a, b, c) with a, b, c ∈ {0, 1, 2, 3}; values are the
        (possibly complex) expansion coefficients.
    """
    paulis = pauli_matrices()
    result = {}
    for a, b, c in iproduct(range(4), range(4), range(4)):
        basis_op = tensor3(paulis[a], paulis[b], paulis[c])
        coeff = np.trace(M @ basis_op) / 8.0
        if abs(coeff) > threshold:
            result[(a, b, c)] = coeff
    return result


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def format_pauli_term(a, b, c, coeff, threshold=1e-10):
    """Format a single Pauli term as a human-readable string.

    Parameters
    ----------
    a, b, c : int
        Pauli indices (0=I, 1=X, 2=Y, 3=Z).
    coeff : complex
        Coefficient.
    threshold : float
        If imaginary part is smaller than this, treat as real (and vice versa).

    Returns
    -------
    str
    """
    label = (f"σ{_PAULI_LABELS[a]}⊗σ{_PAULI_LABELS[b]}⊗σ{_PAULI_LABELS[c]}")
    re, im = coeff.real, coeff.imag
    if abs(im) < threshold:
        return f"{re:+.6f} · {label}"
    if abs(re) < threshold:
        return f"{im:+.6f}i · {label}"
    return f"({re:+.6f}{im:+.6f}i) · {label}"


def format_pauli_decomp(decomp, threshold=1e-10):
    """Format a full Pauli decomposition as a multi-line string.

    Parameters
    ----------
    decomp : dict mapping (int, int, int) → complex
        Output of :func:`pauli_decompose`.
    threshold : float
        Coefficients smaller than this are skipped.

    Returns
    -------
    str
    """
    terms = []
    for (a, b, c), coeff in sorted(decomp.items(),
                                    key=lambda x: -abs(x[1])):
        if abs(coeff) < threshold:
            continue
        terms.append("  " + format_pauli_term(a, b, c, coeff, threshold))
    return "\n".join(terms) if terms else "  0"
