"""
symbols.py - Sympy symbol definitions for twistor theory

Provides commonly used symbols for spacetime coordinates, spinors, etc.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sympy as sp
from sympy import symbols, I


# Spacetime coordinates (real)
x0, x1, x2, x3 = symbols('x^0 x^1 x^2 x^3', real=True)

# Alternative notation
t, x, y, z = symbols('t x y z', real=True)

# Spinor components (complex)
omega_A0, omega_A1 = symbols('omega^A_0 omega^A_1', complex=True)
pi_Ap0, pi_Ap1 = symbols('pi_A^{prime}_0 pi_A^{prime}_1', complex=True)

# Generic complex parameters
alpha, beta, gamma, delta = symbols('alpha beta gamma delta', complex=True)

# Real parameters
lambda_real, mu_real = symbols('lambda mu', real=True)

# Twistor components (generic)
Z_alpha = symbols('Z^alpha_0:4', complex=True)  # Z⁰, Z¹, Z², Z³

# Matrix elements
a, b, c, d = symbols('a b c d', complex=True)

# UBT-specific: complex time parameter
psi = symbols('psi', real=True)  # Imaginary time component in τ = t + iψ


def get_spacetime_coords():
    """
    Get standard spacetime coordinates.
    
    Returns
    -------
    tuple
        (x⁰, x¹, x², x³) or equivalently (t, x, y, z)
    """
    return (x0, x1, x2, x3)


def get_minkowski_coords():
    """
    Get Minkowski coordinates in (t, x, y, z) notation.
    
    Returns
    -------
    tuple
        (t, x, y, z)
    """
    return (t, x, y, z)


def get_spinor_omega():
    """
    Get unprimed spinor components ω^A.
    
    Returns
    -------
    tuple
        (ω^A_0, ω^A_1)
    """
    return (omega_A0, omega_A1)


def get_spinor_pi():
    """
    Get primed spinor components π_{A'}.
    
    Returns
    -------
    tuple
        (π_{A'}_0, π_{A'}_1)
    """
    return (pi_Ap0, pi_Ap1)


def get_twistor_components():
    """
    Get generic twistor components Z^α.
    
    Returns
    -------
    tuple
        (Z⁰, Z¹, Z², Z³)
    """
    return tuple(Z_alpha)


# Export commonly used symbols
__all__ = [
    'x0', 'x1', 'x2', 'x3',
    't', 'x', 'y', 'z',
    'omega_A0', 'omega_A1',
    'pi_Ap0', 'pi_Ap1',
    'alpha', 'beta', 'gamma', 'delta',
    'lambda_real', 'mu_real',
    'Z_alpha',
    'a', 'b', 'c', 'd',
    'psi',
    'I',
    'get_spacetime_coords',
    'get_minkowski_coords',
    'get_spinor_omega',
    'get_spinor_pi',
    'get_twistor_components',
]
