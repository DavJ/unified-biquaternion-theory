"""
twistor.py - Twistor objects and incidence relation

Implements:
1. Twistor dataclass Z^α = (ω^A, π_{A'})
2. Incidence relation: ω = i X π
3. Construction of twistors from spacetime points

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sympy as sp
from sympy import Matrix, I, simplify
from dataclasses import dataclass

from THEORY_COMPARISONS.penrose_twistor.common.linalg import vec_to_column, inner_product
from THEORY_COMPARISONS.penrose_twistor.twistor_core.minkowski_spinor import x_to_X


@dataclass
class Twistor:
    """
    A twistor Z^α = (ω^A, π_{A'}) in ℂ⁴.
    
    Attributes
    ----------
    omega : sympy.Matrix (2×1)
        Unprimed spinor ω^A
    pi : sympy.Matrix (2×1)
        Primed spinor π_{A'}
    
    Examples
    --------
    >>> from sympy import Matrix, I
    >>> omega = Matrix([1, 2])
    >>> pi = Matrix([3, 4*I])
    >>> Z = Twistor(omega, pi)
    >>> Z.to_vector()
    Matrix([[1], [2], [3], [4*I]])
    """
    omega: Matrix
    pi: Matrix
    
    def __post_init__(self):
        """Validate twistor components."""
        if self.omega.shape != (2, 1):
            raise ValueError(f"omega must be 2×1, got {self.omega.shape}")
        if self.pi.shape != (2, 1):
            raise ValueError(f"pi must be 2×1, got {self.pi.shape}")
    
    def to_vector(self):
        """
        Convert twistor to 4-component column vector.
        
        Returns
        -------
        sympy.Matrix (4×1)
            [ω⁰, ω¹, π₀', π₁']
        """
        return Matrix([
            self.omega[0],
            self.omega[1],
            self.pi[0],
            self.pi[1]
        ])
    
    @classmethod
    def from_vector(cls, vec):
        """
        Create twistor from 4-component vector.
        
        Parameters
        ----------
        vec : sympy.Matrix (4×1) or list/tuple
            [ω⁰, ω¹, π₀', π₁']
        
        Returns
        -------
        Twistor
        """
        if not isinstance(vec, Matrix):
            vec = vec_to_column(vec)
        
        if vec.shape[0] != 4:
            raise ValueError(f"Vector must have 4 components, got {vec.shape[0]}")
        
        omega = Matrix([vec[0], vec[1]])
        pi = Matrix([vec[2], vec[3]])
        
        return cls(omega, pi)
    
    def __repr__(self):
        """String representation."""
        return f"Twistor(ω={self.omega.T}, π={self.pi.T})"


def incidence(X, pi):
    """
    Compute ω from incidence relation: ω = i X π.
    
    Given a spacetime point X (as 2×2 Hermitian matrix) and a spinor π,
    compute the corresponding ω.
    
    Parameters
    ----------
    X : sympy.Matrix (2×2)
        Hermitian matrix representing spacetime point
    pi : sympy.Matrix (2×1)
        Primed spinor π_{A'}
    
    Returns
    -------
    sympy.Matrix (2×1)
        Unprimed spinor ω^A = i X π
    
    Examples
    --------
    >>> from sympy import symbols, Matrix, I
    >>> from THEORY_COMPARISONS.penrose_twistor.twistor_core.minkowski_spinor import x_to_X
    >>> t, x, y, z = symbols('t x y z', real=True)
    >>> X = x_to_X(t, x, y, z)
    >>> pi = Matrix([1, 0])
    >>> omega = incidence(X, pi)
    """
    omega = I * X * pi
    return simplify(omega)


def twistor_from_X_pi(X, pi):
    """
    Construct a twistor incident with spacetime point X and spinor π.
    
    Uses incidence relation: ω = i X π.
    
    Parameters
    ----------
    X : sympy.Matrix (2×2)
        Hermitian matrix representing spacetime point
    pi : sympy.Matrix (2×1)
        Primed spinor π_{A'}
    
    Returns
    -------
    Twistor
        Twistor Z = (ω, π) incident with X
    
    Examples
    --------
    >>> from sympy import Matrix
    >>> from THEORY_COMPARISONS.penrose_twistor.twistor_core.minkowski_spinor import x_to_X
    >>> X = x_to_X(1, 0, 0, 0)  # Origin in time
    >>> pi = Matrix([1, 0])
    >>> Z = twistor_from_X_pi(X, pi)
    """
    omega = incidence(X, pi)
    return Twistor(omega, pi)


def twistor_from_point_and_spinor(x0, x1, x2, x3, pi):
    """
    Construct a twistor from Minkowski coordinates and a spinor.
    
    Convenience function combining x_to_X and twistor_from_X_pi.
    
    Parameters
    ----------
    x0, x1, x2, x3 : sympy expressions or numbers
        Minkowski coordinates
    pi : sympy.Matrix (2×1)
        Primed spinor π_{A'}
    
    Returns
    -------
    Twistor
        Twistor Z = (ω, π) incident with point (x⁰, x¹, x², x³)
    """
    X = x_to_X(x0, x1, x2, x3)
    return twistor_from_X_pi(X, pi)


def check_incidence(Z, X):
    """
    Verify that twistor Z is incident with spacetime point X.
    
    Checks if Z.omega = i X Z.pi holds.
    
    Parameters
    ----------
    Z : Twistor
        Twistor to check
    X : sympy.Matrix (2×2)
        Hermitian matrix representing spacetime point
    
    Returns
    -------
    bool
        True if incident, False otherwise
    """
    omega_expected = incidence(X, Z.pi)
    diff = simplify(Z.omega - omega_expected)
    
    return diff == Matrix.zeros(2, 1)


def are_twistors_independent(Z1, Z2):
    """
    Check if two twistors are linearly independent.
    
    Two twistors are independent if their π components are independent.
    
    Parameters
    ----------
    Z1, Z2 : Twistor
        Twistors to check
    
    Returns
    -------
    bool
        True if independent, False otherwise
    """
    # Stack π vectors as columns of a matrix
    pi_matrix = Matrix.hstack(Z1.pi, Z2.pi)
    
    # Check if determinant is non-zero
    det = pi_matrix.det()
    
    return simplify(det) != 0


def reconstruct_X_from_twistors(Z1, Z2):
    """
    Reconstruct spacetime point X from two incident twistors.
    
    Given Z1, Z2 both incident with the same X, solve:
        ω₁ = i X π₁
        ω₂ = i X π₂
    
    for X.
    
    Parameters
    ----------
    Z1, Z2 : Twistor
        Two independent twistors incident with the same point
    
    Returns
    -------
    sympy.Matrix (2×2) or None
        Reconstructed Hermitian matrix X, or None if reconstruction fails
    
    Notes
    -----
    This requires π₁ and π₂ to be linearly independent.
    The reconstruction uses the fact that X is Hermitian, so it has
    4 real degrees of freedom, which can be determined from the
    4 complex equations (2 from each twistor).
    """
    # Check independence
    if not are_twistors_independent(Z1, Z2):
        return None
    
    # Stack equations: [ω₁ ω₂] = i X [π₁ π₂]
    # So: X = -i [ω₁ ω₂] [π₁ π₂]^(-1)
    
    omega_matrix = Matrix.hstack(Z1.omega, Z2.omega)
    pi_matrix = Matrix.hstack(Z1.pi, Z2.pi)
    
    try:
        pi_inv = pi_matrix.inv()
        X = simplify(-I * omega_matrix * pi_inv)
        return X
    except Exception:
        return None


# Convenience functions for creating spinors
def spinor(component0, component1):
    """
    Create a 2-component spinor.
    
    Parameters
    ----------
    component0, component1 : sympy expressions or numbers
        Spinor components
    
    Returns
    -------
    sympy.Matrix (2×1)
        Spinor as column vector
    """
    return Matrix([component0, component1])


def random_spinor_numeric(seed=None):
    """
    Generate a random numeric spinor for testing.
    
    Parameters
    ----------
    seed : int, optional
        Random seed for reproducibility
    
    Returns
    -------
    sympy.Matrix (2×1)
        Random spinor with complex components
    """
    import random
    if seed is not None:
        random.seed(seed)
    
    # Generate random complex numbers
    re0, im0 = random.random(), random.random()
    re1, im1 = random.random(), random.random()
    
    return Matrix([re0 + I*im0, re1 + I*im1])
