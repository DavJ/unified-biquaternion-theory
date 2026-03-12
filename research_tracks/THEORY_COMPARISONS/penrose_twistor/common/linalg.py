"""
linalg.py - Linear algebra utilities for twistor computations

Provides helper functions for matrix operations using sympy.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sympy as sp
from sympy import Matrix, I, conjugate, simplify, eye


def is_hermitian(M):
    """
    Check if a matrix is Hermitian (M† = M).
    
    Parameters
    ----------
    M : sympy.Matrix
        Matrix to check
    
    Returns
    -------
    bool
        True if M is Hermitian, False otherwise
    """
    return simplify(M - M.H) == Matrix.zeros(*M.shape)


def hermitian_conjugate(M):
    """
    Compute Hermitian conjugate (conjugate transpose) of a matrix.
    
    Parameters
    ----------
    M : sympy.Matrix
        Input matrix
    
    Returns
    -------
    sympy.Matrix
        M† = (M*)^T
    """
    return M.H


def pauli_matrices():
    """
    Return the Pauli matrices σ₀, σ₁, σ₂, σ₃.
    
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
    
    return (sigma0, sigma1, sigma2, sigma3)


def vec_to_column(v):
    """
    Convert a list/tuple to a column vector (sympy Matrix).
    
    Parameters
    ----------
    v : list or tuple
        Components of the vector
    
    Returns
    -------
    sympy.Matrix
        Column vector (n×1 matrix)
    """
    return Matrix(v)


def outer_product(v1, v2):
    """
    Compute outer product of two vectors: v1 ⊗ v2.
    
    Parameters
    ----------
    v1 : sympy.Matrix
        First column vector (n×1)
    v2 : sympy.Matrix
        Second column vector (m×1)
    
    Returns
    -------
    sympy.Matrix
        Outer product matrix (n×m)
    """
    # v1 is n×1, v2† is 1×m, product is n×m
    return v1 * v2.H


def inner_product(v1, v2):
    """
    Compute inner product of two vectors: v1† v2.
    
    Parameters
    ----------
    v1 : sympy.Matrix
        First column vector
    v2 : sympy.Matrix
        Second column vector
    
    Returns
    -------
    sympy expression
        Inner product (scalar)
    """
    return (v1.H * v2)[0, 0]


def norm_squared(v):
    """
    Compute squared norm: ||v||² = v† v.
    
    Parameters
    ----------
    v : sympy.Matrix
        Column vector
    
    Returns
    -------
    sympy expression
        Squared norm (non-negative real)
    """
    return inner_product(v, v)


def commutator(A, B):
    """
    Compute commutator [A, B] = AB - BA.
    
    Parameters
    ----------
    A, B : sympy.Matrix
        Matrices to commute
    
    Returns
    -------
    sympy.Matrix
        Commutator
    """
    return A * B - B * A


def anticommutator(A, B):
    """
    Compute anticommutator {A, B} = AB + BA.
    
    Parameters
    ----------
    A, B : sympy.Matrix
        Matrices to anticommute
    
    Returns
    -------
    sympy.Matrix
        Anticommutator
    """
    return A * B + B * A


def trace(M):
    """
    Compute trace of a matrix.
    
    Parameters
    ----------
    M : sympy.Matrix
        Square matrix
    
    Returns
    -------
    sympy expression
        Trace (sum of diagonal elements)
    """
    return M.trace()


def determinant(M):
    """
    Compute determinant of a matrix.
    
    Parameters
    ----------
    M : sympy.Matrix
        Square matrix
    
    Returns
    -------
    sympy expression
        Determinant
    """
    return M.det()


def solve_linear(A, b):
    """
    Solve linear system Ax = b.
    
    Parameters
    ----------
    A : sympy.Matrix
        Coefficient matrix (m×n)
    b : sympy.Matrix
        Right-hand side (m×1)
    
    Returns
    -------
    sympy.Matrix or None
        Solution x (n×1) if exists, None otherwise
    """
    try:
        x = A.solve(b)
        return x
    except Exception:
        return None


def is_invertible(M):
    """
    Check if a square matrix is invertible (non-zero determinant).
    
    Parameters
    ----------
    M : sympy.Matrix
        Square matrix
    
    Returns
    -------
    bool
        True if invertible, False otherwise
    """
    if M.rows != M.cols:
        return False
    return simplify(M.det()) != 0


def matrix_inverse(M):
    """
    Compute matrix inverse if it exists.
    
    Parameters
    ----------
    M : sympy.Matrix
        Square matrix
    
    Returns
    -------
    sympy.Matrix or None
        Inverse matrix if exists, None otherwise
    """
    if not is_invertible(M):
        return None
    return M.inv()
