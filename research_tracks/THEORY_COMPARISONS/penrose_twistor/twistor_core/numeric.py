"""
numeric.py - Numeric utilities for SU(2,2) and conformal transformations

Provides centralized numeric utilities for:
- Matrix norms (Frobenius)
- Tolerance-based comparisons
- Seeded random number generation for reproducibility

Author: UBT Research Team
License: See repository LICENSE.md
"""

import random
from sympy import Matrix, conjugate, sqrt


def norm_fro(M):
    """
    Compute Frobenius norm of a matrix: ||M||_F = sqrt(sum(|M_ij|^2))
    
    Parameters
    ----------
    M : sympy.Matrix
        Matrix to compute norm of
    
    Returns
    -------
    float
        Frobenius norm
    
    Examples
    --------
    >>> from sympy import Matrix
    >>> M = Matrix([[1, 2], [3, 4]])
    >>> norm = norm_fro(M)
    """
    rows, cols = M.shape
    sum_squares = sum(
        abs(complex(M[i, j].evalf())) ** 2
        for i in range(rows)
        for j in range(cols)
    )
    return float(sqrt(sum_squares))


def max_abs(M):
    """
    Compute maximum absolute value of matrix entries: max|M_ij|
    
    Parameters
    ----------
    M : sympy.Matrix
        Matrix to compute max of
    
    Returns
    -------
    float
        Maximum absolute value
    
    Examples
    --------
    >>> from sympy import Matrix
    >>> M = Matrix([[1, -5], [3, 2]])
    >>> max_val = max_abs(M)  # Returns 5.0
    """
    rows, cols = M.shape
    return max(
        abs(complex(M[i, j].evalf()))
        for i in range(rows)
        for j in range(cols)
    )


def close_matrix(A, B, tol=1e-9):
    """
    Check if two matrices are close within tolerance.
    
    Uses Frobenius norm: ||A - B||_F < tol
    
    Parameters
    ----------
    A, B : sympy.Matrix
        Matrices to compare
    tol : float, optional
        Tolerance (default 1e-9)
    
    Returns
    -------
    bool
        True if matrices are close
    
    Examples
    --------
    >>> from sympy import Matrix, eye
    >>> A = eye(2)
    >>> B = eye(2) + Matrix([[1e-10, 0], [0, 0]])
    >>> close_matrix(A, B, tol=1e-9)  # True
    """
    if A.shape != B.shape:
        return False
    
    diff = A - B
    return norm_fro(diff) < tol


def seeded_rng(seed):
    """
    Create a seeded random number generator for reproducibility.
    
    Parameters
    ----------
    seed : int
        Random seed
    
    Returns
    -------
    random.Random
        Seeded random number generator
    
    Examples
    --------
    >>> rng = seeded_rng(42)
    >>> val = rng.uniform(-1, 1)
    """
    rng = random.Random(seed)
    return rng


def random_complex(rng, scale=1.0):
    """
    Generate a random complex number with given scale.
    
    Parameters
    ----------
    rng : random.Random
        Random number generator
    scale : float, optional
        Scale factor (default 1.0)
    
    Returns
    -------
    complex
        Random complex number with |z| ~ scale
    
    Examples
    --------
    >>> rng = seeded_rng(42)
    >>> z = random_complex(rng, scale=0.5)
    """
    real_part = rng.uniform(-scale, scale)
    imag_part = rng.uniform(-scale, scale)
    return complex(real_part, imag_part)


def tolerance_check(value, target, tol=1e-9):
    """
    Check if a value is close to target within tolerance.
    
    Parameters
    ----------
    value : float or complex
        Value to check
    target : float or complex
        Target value
    tol : float, optional
        Tolerance (default 1e-9)
    
    Returns
    -------
    bool
        True if |value - target| < tol
    
    Examples
    --------
    >>> tolerance_check(1.0000000001, 1.0, tol=1e-9)  # True
    >>> tolerance_check(1.001, 1.0, tol=1e-9)  # False
    """
    try:
        val = complex(value)
        tgt = complex(target)
        return abs(val - tgt) < tol
    except:
        return False
