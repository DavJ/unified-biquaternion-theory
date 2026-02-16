"""
minkowski_spinor.py - Mapping between Minkowski spacetime and 2×2 Hermitian matrices

Implements the bijection:
    x = (x⁰, x¹, x², x³) ↔ X = x^μ σ_μ

where σ_μ are Pauli matrices (with σ₀ = Identity).

Key property: det(X) = (x⁰)² - |x|² = s² (Minkowski interval squared)

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sympy as sp
from sympy import Matrix, simplify, eye, I
import sys
from pathlib import Path

# Add parent directories to path for imports
repo_root = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(repo_root))

from THEORY_COMPARISONS.penrose_twistor.common.linalg import (
    pauli_matrices, is_hermitian, trace, determinant
)


def x_to_X(x0, x1, x2, x3):
    """
    Convert Minkowski coordinates to 2×2 Hermitian matrix.
    
    X = x⁰ σ₀ + x¹ σ₁ + x² σ₂ + x³ σ₃
    
    where:
        σ₀ = [[1, 0], [0, 1]]
        σ₁ = [[0, 1], [1, 0]]
        σ₂ = [[0, -i], [i, 0]]
        σ₃ = [[1, 0], [0, -1]]
    
    Parameters
    ----------
    x0, x1, x2, x3 : sympy expressions or numbers
        Minkowski coordinates (x⁰, x¹, x², x³)
    
    Returns
    -------
    sympy.Matrix (2×2)
        Hermitian matrix X
    
    Examples
    --------
    >>> from sympy import symbols
    >>> x0, x1, x2, x3 = symbols('x0 x1 x2 x3', real=True)
    >>> X = x_to_X(x0, x1, x2, x3)
    >>> X
    Matrix([[x0 + x3, x1 - I*x2], [x1 + I*x2, x0 - x3]])
    """
    sigma0, sigma1, sigma2, sigma3 = pauli_matrices()
    
    X = x0 * sigma0 + x1 * sigma1 + x2 * sigma2 + x3 * sigma3
    
    return simplify(X)


def X_to_x(X):
    """
    Extract Minkowski coordinates from 2×2 Hermitian matrix.
    
    Inverse of x_to_X. Given X, recover (x⁰, x¹, x², x³).
    
    Uses:
        x⁰ = Tr(X) / 2
        x¹ = Re(X₀₁)
        x² = -Im(X₀₁)
        x³ = (X₀₀ - X₁₁) / 2
    
    Parameters
    ----------
    X : sympy.Matrix (2×2)
        Hermitian matrix
    
    Returns
    -------
    tuple
        (x⁰, x¹, x², x³) as sympy expressions
    
    Examples
    --------
    >>> from sympy import symbols, Matrix, I
    >>> a, b = symbols('a b', real=True)
    >>> X = Matrix([[a, b], [b, a]])
    >>> X_to_x(X)
    (a, b, 0, 0)
    """
    # Extract matrix elements
    X00 = X[0, 0]
    X01 = X[0, 1]
    X10 = X[1, 0]
    X11 = X[1, 1]
    
    # Compute coordinates
    # For Hermitian X: X₁₀ = X₀₁*
    x0 = simplify((X00 + X11) / 2)  # Tr(X) / 2
    x1 = simplify((X01 + X10) / 2)  # Re(X₀₁) = (X₀₁ + X₀₁*)/2
    x2 = simplify((X10 - X01) / (2*I))  # Im(X₀₁) = (X₀₁ - X₀₁*)/(2i)
    x3 = simplify((X00 - X11) / 2)
    
    return (x0, x1, x2, x3)


def minkowski_interval_squared(x0, x1, x2, x3):
    """
    Compute Minkowski interval squared: s² = (x⁰)² - (x¹)² - (x²)² - (x³)².
    
    Parameters
    ----------
    x0, x1, x2, x3 : sympy expressions or numbers
        Minkowski coordinates
    
    Returns
    -------
    sympy expression
        Interval squared s²
    """
    return simplify(x0**2 - x1**2 - x2**2 - x3**2)


def X_determinant_as_interval(x0, x1, x2, x3):
    """
    Verify that det(X) = s² for X = x^μ σ_μ.
    
    Parameters
    ----------
    x0, x1, x2, x3 : sympy expressions or numbers
        Minkowski coordinates
    
    Returns
    -------
    sympy expression
        det(X), which should equal (x⁰)² - |x|²
    """
    X = x_to_X(x0, x1, x2, x3)
    return simplify(determinant(X))


def verify_roundtrip(x0, x1, x2, x3):
    """
    Verify roundtrip: x → X → x gives back original coordinates.
    
    Parameters
    ----------
    x0, x1, x2, x3 : sympy expressions or numbers
        Original Minkowski coordinates
    
    Returns
    -------
    bool
        True if roundtrip is exact, False otherwise
    """
    X = x_to_X(x0, x1, x2, x3)
    x0_back, x1_back, x2_back, x3_back = X_to_x(X)
    
    # Check if we get back original values
    diff0 = simplify(x0 - x0_back)
    diff1 = simplify(x1 - x1_back)
    diff2 = simplify(x2 - x2_back)
    diff3 = simplify(x3 - x3_back)
    
    return (diff0 == 0) and (diff1 == 0) and (diff2 == 0) and (diff3 == 0)


def numeric_x_to_X(x0, x1, x2, x3):
    """
    Convert numeric Minkowski coordinates to numeric 2×2 Hermitian matrix.
    
    Uses complex arithmetic, suitable for numerical experiments.
    
    Parameters
    ----------
    x0, x1, x2, x3 : float or complex
        Numeric Minkowski coordinates
    
    Returns
    -------
    numpy-like 2×2 array (as sympy Matrix with numeric entries)
        Hermitian matrix X
    """
    X = x_to_X(x0, x1, x2, x3)
    return X.evalf()


def numeric_X_to_x(X_numeric):
    """
    Extract numeric Minkowski coordinates from numeric 2×2 matrix.
    
    Parameters
    ----------
    X_numeric : sympy.Matrix (2×2) with numeric entries
        Hermitian matrix
    
    Returns
    -------
    tuple of floats
        (x⁰, x¹, x², x³)
    """
    x0, x1, x2, x3 = X_to_x(X_numeric)
    
    # Convert to float (taking real part to handle numerical precision)
    x0_val = complex(x0).real
    x1_val = complex(x1).real
    x2_val = complex(x2).real
    x3_val = complex(x3).real
    
    return (x0_val, x1_val, x2_val, x3_val)


# Convenience function for common cases
def timelike_point(t_val, spatial_vec=None):
    """
    Create a timelike spacetime point.
    
    Parameters
    ----------
    t_val : float
        Time coordinate
    spatial_vec : tuple or list, optional
        (x, y, z) spatial coordinates. Defaults to (0, 0, 0)
    
    Returns
    -------
    tuple
        (x⁰, x¹, x², x³) with x⁰ = t_val
    """
    if spatial_vec is None:
        spatial_vec = (0, 0, 0)
    
    return (t_val, spatial_vec[0], spatial_vec[1], spatial_vec[2])


def spacelike_point(spatial_vec, t_val=0):
    """
    Create a spacelike spacetime point.
    
    Parameters
    ----------
    spatial_vec : tuple or list
        (x, y, z) spatial coordinates
    t_val : float, optional
        Time coordinate. Defaults to 0
    
    Returns
    -------
    tuple
        (x⁰, x¹, x², x³)
    """
    return (t_val, spatial_vec[0], spatial_vec[1], spatial_vec[2])
