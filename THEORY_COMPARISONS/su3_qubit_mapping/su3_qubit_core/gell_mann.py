"""
gell_mann.py – Standard Gell-Mann matrices and su(3) structure constants.

Conventions
-----------
  Normalisation:   Tr[λ_a λ_b] = 2 δ_{ab}
  Commutation:     [λ_a, λ_b] = 2i f_{abc} λ_c
  Anti-commutation:{λ_a, λ_b} = (4/3) δ_{ab} I₃ + 2 d_{abc} λ_c

Indices throughout are 0-based (a=0..7 corresponds to λ₁..λ₈).

Author: UBT Research Team
License: See repository LICENSE.md
"""

import numpy as np
from itertools import product as iproduct


# ---------------------------------------------------------------------------
# Gell-Mann matrices
# ---------------------------------------------------------------------------

def gell_mann_matrices():
    """Return the 8 Gell-Mann matrices λ₁..λ₈ as 3×3 complex numpy arrays.

    Index convention: lam[0] = λ₁, ..., lam[7] = λ₈.
    Normalisation: Tr[λ_a λ_b] = 2 δ_{ab}.

    Returns
    -------
    list of 8 numpy.ndarray, each of shape (3, 3) and dtype complex
    """
    lam = [None] * 8

    lam[0] = np.array([[0, 1, 0],
                        [1, 0, 0],
                        [0, 0, 0]], dtype=complex)            # λ₁

    lam[1] = np.array([[0, -1j, 0],
                        [1j,  0, 0],
                        [0,   0, 0]], dtype=complex)           # λ₂

    lam[2] = np.array([[1,  0, 0],
                        [0, -1, 0],
                        [0,  0, 0]], dtype=complex)            # λ₃

    lam[3] = np.array([[0, 0, 1],
                        [0, 0, 0],
                        [1, 0, 0]], dtype=complex)             # λ₄

    lam[4] = np.array([[0,   0, -1j],
                        [0,   0,   0],
                        [1j,  0,   0]], dtype=complex)         # λ₅

    lam[5] = np.array([[0, 0, 0],
                        [0, 0, 1],
                        [0, 1, 0]], dtype=complex)             # λ₆

    lam[6] = np.array([[0,  0,   0],
                        [0,  0, -1j],
                        [0, 1j,   0]], dtype=complex)          # λ₇

    lam[7] = (1.0 / np.sqrt(3)) * np.array([[1, 0,  0],
                                              [0, 1,  0],
                                              [0, 0, -2]], dtype=complex)  # λ₈

    return lam


# ---------------------------------------------------------------------------
# Structure constants
# ---------------------------------------------------------------------------

def structure_constants(lam=None):
    """Compute the antisymmetric structure constants f_{abc}.

    Defined via  [λ_a, λ_b] = 2i f_{abc} λ_c  (sum over c).

    Extraction formula:
        f_{abc} = Tr[λ_c [λ_a, λ_b]] / (4i)

    Parameters
    ----------
    lam : list of ndarray, optional
        Gell-Mann matrices; computed fresh if None.

    Returns
    -------
    numpy.ndarray of shape (8, 8, 8), dtype float
        f[a, b, c] = f_{(a+1)(b+1)(c+1)}.
    """
    if lam is None:
        lam = gell_mann_matrices()
    n = 8
    f = np.zeros((n, n, n), dtype=float)
    for a, b in iproduct(range(n), range(n)):
        comm = lam[a] @ lam[b] - lam[b] @ lam[a]
        for c in range(n):
            val = np.trace(lam[c] @ comm) / (4j)
            f[a, b, c] = float(val.real)
    return f


def symmetric_d_tensor(lam=None):
    """Compute the symmetric structure constants d_{abc}.

    Defined via  {λ_a, λ_b} = (4/3) δ_{ab} I₃ + 2 d_{abc} λ_c  (sum over c).

    Extraction formula:
        d_{abc} = Tr[λ_c {λ_a, λ_b}] / 4

    Parameters
    ----------
    lam : list of ndarray, optional
        Gell-Mann matrices; computed fresh if None.

    Returns
    -------
    numpy.ndarray of shape (8, 8, 8), dtype float
        d[a, b, c] = d_{(a+1)(b+1)(c+1)}.
    """
    if lam is None:
        lam = gell_mann_matrices()
    n = 8
    d = np.zeros((n, n, n), dtype=float)
    for a, b in iproduct(range(n), range(n)):
        anticomm = lam[a] @ lam[b] + lam[b] @ lam[a]
        for c in range(n):
            val = np.trace(lam[c] @ anticomm) / 4.0
            d[a, b, c] = float(val.real)
    return d


# ---------------------------------------------------------------------------
# Verification helpers
# ---------------------------------------------------------------------------

def verify_normalisation(lam=None):
    """Check Tr[λ_a λ_b] = 2 δ_{ab}.

    Returns
    -------
    float
        Maximum absolute residual; should be < 1e-12.
    """
    if lam is None:
        lam = gell_mann_matrices()
    n = 8
    max_err = 0.0
    for a, b in iproduct(range(n), range(n)):
        tr = np.trace(lam[a] @ lam[b]).real
        expected = 2.0 if a == b else 0.0
        max_err = max(max_err, abs(tr - expected))
    return max_err


def verify_lie_algebra(lam=None, f=None):
    """Check [λ_a, λ_b] = 2i f_{abc} λ_c for all a, b.

    Returns
    -------
    float
        Maximum entry-wise absolute residual; should be < 1e-12.
    """
    if lam is None:
        lam = gell_mann_matrices()
    if f is None:
        f = structure_constants(lam)
    n = 8
    max_err = 0.0
    for a, b in iproduct(range(n), range(n)):
        comm = lam[a] @ lam[b] - lam[b] @ lam[a]
        rhs = sum(2j * f[a, b, c] * lam[c] for c in range(n))
        err = float(np.max(np.abs(comm - rhs)))
        max_err = max(max_err, err)
    return max_err


def verify_hermitian_traceless(lam=None):
    """Check that every Gell-Mann matrix is Hermitian and traceless.

    Returns
    -------
    float
        Maximum combined residual; should be < 1e-12.
    """
    if lam is None:
        lam = gell_mann_matrices()
    max_err = 0.0
    for l in lam:
        err_herm = float(np.max(np.abs(l - l.conj().T)))
        err_tr = abs(np.trace(l))
        max_err = max(max_err, err_herm, err_tr)
    return max_err


def verify_jacobi(f=None):
    """Check Jacobi identity: f_{abe}f_{ecd} + f_{bce}f_{ead} + f_{cae}f_{ebd} = 0.

    Returns
    -------
    float
        Maximum absolute violation; should be < 1e-12.
    """
    if f is None:
        f = structure_constants()
    n = 8
    max_err = 0.0
    for a, b, c, d in iproduct(range(n), range(n), range(n), range(n)):
        val = (sum(f[a, b, e] * f[e, c, d] for e in range(n))
               + sum(f[b, c, e] * f[e, a, d] for e in range(n))
               + sum(f[c, a, e] * f[e, b, d] for e in range(n)))
        max_err = max(max_err, abs(val))
    return max_err
