"""
algebra.py — Shared algebra utilities for dimensional economy comparison.

Provides Pauli matrices, commutator, anti-commutator, and related helpers
used across dim_economy_core modules.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sympy as sp
from sympy import Matrix, I, eye, simplify, zeros


def pauli_matrices():
    """
    Return the four Pauli matrices σ₀, σ₁, σ₂, σ₃.

    σ₀ = Identity
    σ₁ = [[0, 1], [1, 0]]
    σ₂ = [[0, -i], [i, 0]]
    σ₃ = [[1, 0], [0, -1]]

    Returns
    -------
    tuple of sympy.Matrix
        (σ₀, σ₁, σ₂, σ₃)
    """
    sigma0 = eye(2)
    sigma1 = Matrix([[0, 1], [1, 0]])
    sigma2 = Matrix([[0, -I], [I, 0]])
    sigma3 = Matrix([[1, 0], [0, -1]])
    return sigma0, sigma1, sigma2, sigma3


def commutator(A, B):
    """
    Compute the commutator [A, B] = AB - BA.

    Parameters
    ----------
    A, B : sympy.Matrix
        Square matrices of the same size.

    Returns
    -------
    sympy.Matrix
        [A, B]
    """
    return simplify(A * B - B * A)


def anticommutator(A, B):
    """
    Compute the anti-commutator {A, B} = AB + BA.

    Parameters
    ----------
    A, B : sympy.Matrix
        Square matrices of the same size.

    Returns
    -------
    sympy.Matrix
        {A, B}
    """
    return simplify(A * B + B * A)


def levi_civita(a, b, c):
    """
    Return the Levi-Civita symbol ε_{abc} for indices a, b, c ∈ {1, 2, 3}.

    Parameters
    ----------
    a, b, c : int
        Indices 1, 2, or 3.

    Returns
    -------
    int
        +1, -1, or 0.
    """
    if (a, b, c) in ((1, 2, 3), (2, 3, 1), (3, 1, 2)):
        return 1
    if (a, b, c) in ((3, 2, 1), (1, 3, 2), (2, 1, 3)):
        return -1
    return 0


def is_zero_matrix(M, tol=0):
    """
    Check whether a sympy Matrix is the zero matrix (symbolically exact).

    Parameters
    ----------
    M : sympy.Matrix
        Matrix to check.
    tol : int
        Tolerance (kept for API symmetry; symbolic check requires 0).

    Returns
    -------
    bool
    """
    simplified = simplify(M)
    return simplified == zeros(*M.shape)
