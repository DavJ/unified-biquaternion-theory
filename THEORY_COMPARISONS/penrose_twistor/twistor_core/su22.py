"""
su22.py - SU(2,2) Hermitian form and invariants

Implements the natural Hermitian form on twistor space ℂ⁴:

    H = [[0,  I₂],
         [I₂, 0 ]]

and the associated twistor inner product:

    ⟨Z₁, Z₂⟩ = Z₁† H Z₂

This is preserved under SU(2,2) transformations (conformal group).

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sympy as sp
from sympy import Matrix, eye, simplify, conjugate, I

from THEORY_COMPARISONS.penrose_twistor.common.linalg import hermitian_conjugate
from THEORY_COMPARISONS.penrose_twistor.twistor_core.twistor import Twistor


def get_su22_hermitian_form():
    """
    Return the SU(2,2) Hermitian form H.
    
    H = [[0,  I₂],
         [I₂, 0 ]]
    
    where I₂ is the 2×2 identity matrix.
    
    Returns
    -------
    sympy.Matrix (4×4)
        Hermitian form H
    
    Notes
    -----
    This is the standard invariant form for SU(2,2), the conformal group
    of compactified Minkowski space.
    """
    I2 = eye(2)
    Z2 = Matrix.zeros(2, 2)
    
    # Block matrix:
    # H = [[0,  I₂],
    #      [I₂, 0 ]]
    H = Matrix.vstack(
        Matrix.hstack(Z2, I2),
        Matrix.hstack(I2, Z2)
    )
    
    return H


def twistor_inner(Z1, Z2):
    """
    Compute SU(2,2) inner product of two twistors.
    
    ⟨Z₁, Z₂⟩ = Z₁† H Z₂
    
    where H is the SU(2,2) Hermitian form.
    
    Parameters
    ----------
    Z1, Z2 : Twistor
        Twistors to compute inner product of
    
    Returns
    -------
    sympy expression
        Inner product (complex scalar)
    
    Examples
    --------
    >>> from sympy import Matrix
    >>> from THEORY_COMPARISONS.penrose_twistor.twistor_core.twistor import Twistor
    >>> Z1 = Twistor(Matrix([1, 0]), Matrix([0, 1]))
    >>> Z2 = Twistor(Matrix([0, 1]), Matrix([1, 0]))
    >>> inner = twistor_inner(Z1, Z2)
    """
    H = get_su22_hermitian_form()
    
    # Convert twistors to 4-vectors
    vec1 = Z1.to_vector()  # 4×1 column vector
    vec2 = Z2.to_vector()  # 4×1 column vector
    
    # Compute ⟨Z₁, Z₂⟩ = vec1† H vec2
    # vec1† is (1×4) row vector, H is 4×4, vec2 is 4×1 column vector
    # Result is 1×1
    vec1_dag = vec1.H  # Hermitian conjugate: conjugate transpose, now 1×4
    result = (vec1_dag * H * vec2)[0, 0]
    
    return simplify(result)


def twistor_norm_squared(Z):
    """
    Compute squared norm of a twistor: ⟨Z, Z⟩.
    
    Parameters
    ----------
    Z : Twistor
        Twistor to compute norm of
    
    Returns
    -------
    sympy expression
        Squared norm ⟨Z, Z⟩
    
    Notes
    -----
    For the SU(2,2) form, the norm can be positive, negative, or zero.
    - Positive: timelike twistor
    - Negative: spacelike twistor  
    - Zero: null twistor
    """
    return twistor_inner(Z, Z)


def is_hermitian_form(H):
    """
    Verify that H is Hermitian: H† = H.
    
    Parameters
    ----------
    H : sympy.Matrix
        Matrix to check
    
    Returns
    -------
    bool
        True if Hermitian, False otherwise
    """
    return simplify(H - hermitian_conjugate(H)) == Matrix.zeros(*H.shape)


def verify_su22_form_hermitian():
    """
    Verify that the SU(2,2) form H is Hermitian.
    
    Returns
    -------
    bool
        True if H is Hermitian
    """
    H = get_su22_hermitian_form()
    return is_hermitian_form(H)


def twistor_inner_conjugate_symmetry(Z1, Z2):
    """
    Verify conjugate symmetry: ⟨Z₁, Z₂⟩* = ⟨Z₂, Z₁⟩.
    
    Parameters
    ----------
    Z1, Z2 : Twistor
        Twistors to test
    
    Returns
    -------
    bool
        True if conjugate symmetry holds
    """
    inner12 = twistor_inner(Z1, Z2)
    inner21 = twistor_inner(Z2, Z1)
    
    diff = simplify(conjugate(inner12) - inner21)
    
    return diff == 0


def twistor_inner_linearity_test(Z1, Z2, Z3, alpha, beta):
    """
    Verify linearity in second argument:
    ⟨Z₁, αZ₂ + βZ₃⟩ = α⟨Z₁, Z₂⟩ + β⟨Z₁, Z₃⟩
    
    Parameters
    ----------
    Z1, Z2, Z3 : Twistor
        Test twistors
    alpha, beta : sympy expressions
        Complex coefficients
    
    Returns
    -------
    bool
        True if linearity holds
    """
    # Construct αZ₂ + βZ₃
    omega_combined = alpha * Z2.omega + beta * Z3.omega
    pi_combined = alpha * Z2.pi + beta * Z3.pi
    Z_combined = Twistor(omega_combined, pi_combined)
    
    # Compute both sides
    lhs = twistor_inner(Z1, Z_combined)
    rhs = alpha * twistor_inner(Z1, Z2) + beta * twistor_inner(Z1, Z3)
    
    diff = simplify(lhs - rhs)
    
    return diff == 0


def su22_transformation_preserves_inner(U, Z1, Z2):
    """
    Verify that SU(2,2) transformation U preserves inner product.
    
    An SU(2,2) matrix U satisfies: U† H U = H
    
    This test checks: ⟨UZ₁, UZ₂⟩ = ⟨Z₁, Z₂⟩
    
    Parameters
    ----------
    U : sympy.Matrix (4×4)
        Transformation matrix (should be in SU(2,2))
    Z1, Z2 : Twistor
        Test twistors
    
    Returns
    -------
    bool
        True if inner product is preserved
    
    Notes
    -----
    This function does NOT verify that U is actually in SU(2,2).
    It only checks if the transformation preserves the inner product.
    """
    H = get_su22_hermitian_form()
    
    # First verify U is SU(2,2): U† H U = H
    is_su22 = simplify(hermitian_conjugate(U).T * H * U - H) == Matrix.zeros(4, 4)
    
    if not is_su22:
        return False
    
    # Transform twistors
    vec1 = Z1.to_vector()
    vec2 = Z2.to_vector()
    
    vec1_transformed = U * vec1
    vec2_transformed = U * vec2
    
    Z1_transformed = Twistor.from_vector(vec1_transformed)
    Z2_transformed = Twistor.from_vector(vec2_transformed)
    
    # Check preservation
    inner_original = twistor_inner(Z1, Z2)
    inner_transformed = twistor_inner(Z1_transformed, Z2_transformed)
    
    diff = simplify(inner_original - inner_transformed)
    
    return diff == 0


def twistor_orthogonal(Z1, Z2):
    """
    Check if two twistors are orthogonal: ⟨Z₁, Z₂⟩ = 0.
    
    Parameters
    ----------
    Z1, Z2 : Twistor
        Twistors to check
    
    Returns
    -------
    bool
        True if orthogonal, False otherwise
    """
    inner = twistor_inner(Z1, Z2)
    return simplify(inner) == 0


def create_orthogonal_twistor(Z1):
    """
    Create a twistor orthogonal to Z1 (if possible).
    
    Uses the fact that for H with block anti-diagonal structure:
    If Z₁ = (ω₁, π₁), then Z₂ = (π₁, -ω₁) is orthogonal.
    
    This is because: ⟨Z₁, Z₂⟩ = ω₁†π₁ + π₁†(-ω₁) = ω₁†π₁ - π₁†ω₁ = 0
    (since ω₁†π₁ is a scalar, it equals (π₁†ω₁)†  = (π₁†ω₁)* = conjugate transpose).
    
    Parameters
    ----------
    Z1 : Twistor
        Reference twistor
    
    Returns
    -------
    Twistor
        Orthogonal twistor Z₂
    
    Examples
    --------
    >>> from sympy import Matrix
    >>> from THEORY_COMPARISONS.penrose_twistor.twistor_core.twistor import Twistor
    >>> Z1 = Twistor(Matrix([1, 0]), Matrix([0, 1]))
    >>> Z2 = create_orthogonal_twistor(Z1)
    >>> twistor_orthogonal(Z1, Z2)
    True
    """
    # Swap ω and π and negate the new π to get orthogonal twistor
    return Twistor(Z1.pi, -Z1.omega)


def get_su22_signature():
    """
    Get the signature of the SU(2,2) Hermitian form.
    
    Returns
    -------
    tuple
        (n_positive, n_negative, n_zero) eigenvalue counts
    
    Notes
    -----
    For SU(2,2), the signature should be (2, 2, 0).
    """
    H = get_su22_hermitian_form()
    eigenvals = H.eigenvals()
    
    n_positive = 0
    n_negative = 0
    n_zero = 0
    
    for eigval, multiplicity in eigenvals.items():
        eigval_simplified = simplify(eigval)
        if eigval_simplified > 0:
            n_positive += multiplicity
        elif eigval_simplified < 0:
            n_negative += multiplicity
        else:
            n_zero += multiplicity
    
    return (n_positive, n_negative, n_zero)
