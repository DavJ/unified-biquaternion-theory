"""
conformal.py - Conformal transformations on spacetime via SU(2,2)

Implements the action of SU(2,2) on twistor space and the induced
conformal (Möbius) transformations on 2×2 Hermitian matrices representing
spacetime points.

Key transformations:
- U : Z → UZ  (linear action on twistors)
- Induced action on X:  X → X' = (AX + B)(CX + D)^{-1}
  where U = [[A, B], [C, D]] in 2×2 block form

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sympy as sp
from sympy import Matrix, eye, simplify, I

from THEORY_COMPARISONS.penrose_twistor.twistor_core.twistor import Twistor
from THEORY_COMPARISONS.penrose_twistor.twistor_core.su22 import (
    get_su22_hermitian_form,
    is_su22,
)


def transform_twistor(U, Z):
    """
    Apply SU(2,2) transformation U to twistor Z.
    
    Z' = U Z
    
    Parameters
    ----------
    U : sympy.Matrix (4×4)
        SU(2,2) transformation matrix
    Z : Twistor
        Input twistor
    
    Returns
    -------
    Twistor
        Transformed twistor Z' = UZ
    
    Examples
    --------
    >>> from sympy import eye, Matrix
    >>> U = eye(4)  # Identity transformation
    >>> Z = Twistor(Matrix([1, 0]), Matrix([0, 1]))
    >>> Z_transformed = transform_twistor(U, Z)
    """
    # Convert Z to 4-vector
    vec = Z.to_vector()
    
    # Apply transformation
    vec_transformed = U * vec
    
    # Convert back to twistor
    Z_transformed = Twistor.from_vector(vec_transformed)
    
    return Z_transformed


def extract_block_structure(U):
    """
    Extract 2×2 blocks from a 4×4 matrix U.
    
    U = [[A, B],
         [C, D]]
    
    where A, B, C, D are 2×2 blocks.
    
    Parameters
    ----------
    U : sympy.Matrix (4×4)
        Matrix to decompose
    
    Returns
    -------
    tuple of sympy.Matrix
        (A, B, C, D) as 2×2 matrices
    """
    A = U[:2, :2]
    B = U[:2, 2:]
    C = U[2:, :2]
    D = U[2:, 2:]
    
    return A, B, C, D


def mobius_transform_X(U, X):
    """
    Apply induced conformal (Möbius) transformation to 2×2 Hermitian matrix X.
    
    Given U in SU(2,2) with block structure:
        U = [[A, B],
             [C, D]]
    
    The induced action on X is:
        X' = (A X + B)(C X + D)^{-1}
    
    This is the standard fractional linear transformation preserving
    the conformal structure (null cone).
    
    Parameters
    ----------
    U : sympy.Matrix (4×4)
        SU(2,2) transformation matrix
    X : sympy.Matrix (2×2)
        Hermitian matrix representing spacetime point
    
    Returns
    -------
    sympy.Matrix (2×2)
        Transformed Hermitian matrix X'
    
    Notes
    -----
    Null structure is preserved: if det(X) = 0, then det(X') = 0
    (up to an overall conformal factor).
    
    Examples
    --------
    >>> from sympy import eye, Matrix
    >>> U = eye(4)  # Identity
    >>> X = Matrix([[1, 0], [0, 1]])
    >>> X_prime = mobius_transform_X(U, X)
    >>> X_prime == X  # Identity transformation
    True
    """
    # Extract blocks
    A, B, C, D = extract_block_structure(U)
    
    # Compute AX + B
    numerator = A * X + B
    
    # Compute CX + D
    denominator = C * X + D
    
    # Check if denominator is invertible
    det_denom = denominator.det()
    det_simplified = simplify(det_denom)
    
    if det_simplified == 0:
        raise ValueError("Denominator (CX + D) is not invertible for this X and U")
    
    # Compute inverse
    denominator_inv = denominator.inv()
    
    # Compute X' = (AX + B)(CX + D)^{-1}
    X_prime = numerator * denominator_inv
    
    return simplify(X_prime)


def verify_null_preservation(U, X):
    """
    Verify that null structure is preserved under conformal transformation.
    
    If det(X) = 0, then det(X') should also be 0 (up to numerical precision).
    
    Parameters
    ----------
    U : sympy.Matrix (4×4)
        SU(2,2) transformation
    X : sympy.Matrix (2×2)
        Hermitian matrix (should be null: det(X) = 0)
    
    Returns
    -------
    dict
        Dictionary with:
            'det_X': determinant of X
            'det_X_prime': determinant of X'
            'null_preserved': True if both are zero (within tolerance)
    
    Notes
    -----
    Conformal transformations preserve the light cone structure:
        det(X') = det(X) / |det(CX + D)|^2
    
    So if det(X) = 0, then det(X') = 0.
    """
    # Compute det(X)
    det_X = X.det()
    det_X_simplified = simplify(det_X)
    
    # Transform X
    try:
        X_prime = mobius_transform_X(U, X)
    except ValueError as e:
        return {
            'det_X': det_X_simplified,
            'det_X_prime': None,
            'null_preserved': False,
            'error': str(e)
        }
    
    # Compute det(X')
    det_X_prime = X_prime.det()
    det_X_prime_simplified = simplify(det_X_prime)
    
    # Check if both are zero (within tolerance if numeric)
    def is_zero(val, tol=1e-10):
        """Check if value is zero."""
        if val == 0:
            return True
        try:
            val_numeric = complex(val.evalf())
            return abs(val_numeric) < tol
        except:
            return False
    
    X_is_null = is_zero(det_X_simplified)
    X_prime_is_null = is_zero(det_X_prime_simplified)
    
    null_preserved = X_is_null and X_prime_is_null
    
    return {
        'det_X': det_X_simplified,
        'det_X_prime': det_X_prime_simplified,
        'null_preserved': null_preserved,
        'X_is_null': X_is_null,
        'X_prime_is_null': X_prime_is_null,
    }


def conformal_factor(U, X):
    """
    Compute the conformal scaling factor for the transformation.
    
    Under X → X', determinants transform as:
        det(X') = det(X) / |det(CX + D)|^2
    
    The conformal factor is Ω² = 1 / |det(CX + D)|^2
    
    Parameters
    ----------
    U : sympy.Matrix (4×4)
        SU(2,2) transformation
    X : sympy.Matrix (2×2)
        Hermitian matrix
    
    Returns
    -------
    sympy expression
        Conformal factor Ω²
    
    Notes
    -----
    For null X (det(X) = 0), the conformal factor doesn't affect
    the null property: det(X') = 0 regardless of Ω.
    """
    # Extract blocks
    A, B, C, D = extract_block_structure(U)
    
    # Compute CX + D
    CX_plus_D = C * X + D
    
    # Compute det(CX + D)
    det_CX_D = CX_plus_D.det()
    det_simplified = simplify(det_CX_D)
    
    # Compute |det(CX + D)|^2
    from sympy import conjugate
    det_abs_squared = simplify(det_simplified * conjugate(det_simplified))
    
    # Conformal factor Ω² = 1 / |det(CX + D)|^2
    if det_abs_squared == 0:
        return sp.oo  # Infinity (degenerate case)
    
    conformal_factor_val = simplify(1 / det_abs_squared)
    
    return conformal_factor_val


def test_conformal_transformation_identity():
    """
    Test that identity transformation leaves X unchanged.
    
    Returns
    -------
    bool
        True if test passes
    """
    U = eye(4)
    X = Matrix([[1, 0], [0, 1]])
    
    X_prime = mobius_transform_X(U, X)
    
    return simplify(X_prime - X) == Matrix.zeros(2, 2)


def test_conformal_transformation_null_preservation():
    """
    Test that null matrices stay null under conformal transformation.
    
    Returns
    -------
    bool
        True if test passes
    """
    # Create a simple SU(2,2) element (small perturbation from identity)
    U = eye(4) + Matrix([
        [0, 0, 0.1, 0],
        [0, 0, 0, 0.1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ])
    
    # Null matrix (rank-1): X = [[1, 1], [1, 1]]
    X_null = Matrix([[1, 1], [1, 1]])
    
    result = verify_null_preservation(U, X_null)
    
    return result['null_preserved']


def main():
    """
    Run conformal transformation tests.
    """
    print("=" * 70)
    print("CONFORMAL TRANSFORMATIONS TEST")
    print("=" * 70)
    print()
    
    # Test 1: Identity
    print("1. Testing identity transformation...")
    if test_conformal_transformation_identity():
        print("   ✓ Identity transformation verified")
    else:
        print("   ✗ Identity transformation FAILED")
    print()
    
    # Test 2: Null preservation
    print("2. Testing null structure preservation...")
    if test_conformal_transformation_null_preservation():
        print("   ✓ Null structure preserved")
    else:
        print("   ✗ Null structure NOT preserved")
    print()
    
    print("=" * 70)
    print("CONFORMAL TRANSFORMATIONS TEST COMPLETE")
    print("=" * 70)


if __name__ == '__main__':
    main()
