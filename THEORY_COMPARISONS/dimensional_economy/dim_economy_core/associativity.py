"""
associativity.py — Associativity of ℂ⊗ℍ ≅ Mat(2,ℂ) vs. octonion non-associativity.

ℂ⊗ℍ ≅ Mat(2,ℂ) is a matrix algebra; matrix multiplication is always
associative: (AB)C = A(BC) for all A, B, C ∈ Mat(2,ℂ).

Furey's construction uses ℂ⊗𝕆 which involves the octonions 𝕆.  Octonions are
the only non-associative normed division algebra.  The classic counterexample is
    e₁ · (e₂ · e₄) ≠ (e₁ · e₂) · e₄
using the standard Cayley multiplication table.

This module:
1. Proves associativity of Mat(2,ℂ) symbolically.
2. Demonstrates octonion non-associativity via an explicit numeric example.
3. Provides a summary function that returns both results.

Reference: Problem statement §"The Associativity Advantage"

Author: UBT Research Team
License: See repository LICENSE.md
"""

from sympy import Matrix, I, symbols, simplify, zeros, eye


# ---------------------------------------------------------------------------
# Mat(2,ℂ) associativity
# ---------------------------------------------------------------------------

def verify_mat2c_associativity():
    """
    Prove that Mat(2,ℂ) multiplication is associative: (AB)C = A(BC).

    Uses symbolic 2×2 matrices with generic complex entries.

    Returns
    -------
    bool
        True if (AB)C = A(BC) holds symbolically.

    Raises
    ------
    AssertionError
        If associativity fails.
    """
    # Symbolic entries for three generic 2×2 matrices
    a00, a01, a10, a11 = symbols('a00 a01 a10 a11', complex=True)
    b00, b01, b10, b11 = symbols('b00 b01 b10 b11', complex=True)
    c00, c01, c10, c11 = symbols('c00 c01 c10 c11', complex=True)

    A = Matrix([[a00, a01], [a10, a11]])
    B = Matrix([[b00, b01], [b10, b11]])
    C = Matrix([[c00, c01], [c10, c11]])

    lhs = simplify((A * B) * C)
    rhs = simplify(A * (B * C))
    diff = simplify(lhs - rhs)

    if diff != zeros(2, 2):
        raise AssertionError(
            f"Mat(2,ℂ) is NOT associative: (AB)C - A(BC) = {diff}"
        )

    return True


# ---------------------------------------------------------------------------
# Octonion basis and multiplication
# ---------------------------------------------------------------------------

# Cayley-Dickson octonion multiplication table (indices 0–7).
# e₀ = 1, e₁..e₇ = imaginary units.
# Entry OCTONION_MULT[i][j] = (sign, k) meaning  eᵢ · eⱼ = sign · eₖ.
# Fano plane encoding; cross-checked against standard table.
_OCTONION_SIGN_TABLE = [
    # e0  e1  e2  e3  e4  e5  e6  e7
    [(+1,0),(+1,1),(+1,2),(+1,3),(+1,4),(+1,5),(+1,6),(+1,7)],   # e0·ej
    [(+1,1),(-1,0),(+1,3),(-1,2),(+1,5),(-1,4),(-1,7),(+1,6)],   # e1·ej
    [(+1,2),(-1,3),(-1,0),(+1,1),(+1,6),(+1,7),(-1,4),(-1,5)],   # e2·ej
    [(+1,3),(+1,2),(-1,1),(-1,0),(+1,7),(-1,6),(+1,5),(-1,4)],   # e3·ej
    [(+1,4),(-1,5),(-1,6),(-1,7),(-1,0),(+1,1),(+1,2),(+1,3)],   # e4·ej
    [(+1,5),(+1,4),(-1,7),(+1,6),(-1,1),(-1,0),(-1,3),(+1,2)],   # e5·ej
    [(+1,6),(+1,7),(+1,4),(-1,5),(-1,2),(+1,3),(-1,0),(-1,1)],   # e6·ej
    [(+1,7),(-1,6),(+1,5),(+1,4),(-1,3),(-1,2),(+1,1),(-1,0)],   # e7·ej
]


def octonion_mult(a, b):
    """
    Multiply two octonions represented as 8-element lists of floats.

    Uses the standard Cayley multiplication table (Fano plane convention).

    Parameters
    ----------
    a, b : list of float, length 8
        Octonion coefficients [a₀, a₁, …, a₇] and [b₀, b₁, …, b₇].

    Returns
    -------
    list of float, length 8
        Product a · b.
    """
    result = [0.0] * 8
    for i in range(8):
        for j in range(8):
            sign, k = _OCTONION_SIGN_TABLE[i][j]
            result[k] += sign * a[i] * b[j]
    return result


def demonstrate_octonion_non_associativity():
    """
    Demonstrate that octonion multiplication is non-associative.

    Classic counterexample using basis elements:
        e₁ · (e₂ · e₄) ≠ (e₁ · e₂) · e₄

    Returns
    -------
    dict
        {
          'lhs':  e₁ · (e₂ · e₄),
          'rhs':  (e₁ · e₂) · e₄,
          'equal': bool,
          'is_associative': False  (expected)
        }
    """
    # Basis vectors
    def basis(k):
        v = [0.0] * 8
        v[k] = 1.0
        return v

    e1 = basis(1)
    e2 = basis(2)
    e4 = basis(4)

    lhs = octonion_mult(e1, octonion_mult(e2, e4))     # e1·(e2·e4)
    rhs = octonion_mult(octonion_mult(e1, e2), e4)     # (e1·e2)·e4

    equal = (lhs == rhs)

    return {
        'lhs': lhs,
        'rhs': rhs,
        'equal': equal,
        'is_associative': equal,
    }


def verify_octonions_non_associative():
    """
    Assert that the classic octonion counterexample demonstrates non-associativity.

    Returns
    -------
    bool
        True if non-associativity is confirmed.

    Raises
    ------
    AssertionError
        If the products happen to be equal (which would be unexpected).
    """
    result = demonstrate_octonion_non_associativity()
    if result['is_associative']:
        raise AssertionError(
            "Expected octonion non-associativity but e1·(e2·e4) == (e1·e2)·e4. "
            "Check multiplication table."
        )
    return True


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

def associativity_comparison_summary():
    """
    Return a summary dict comparing associativity of ℂ⊗ℍ and ℂ⊗𝕆.

    Returns
    -------
    dict
        {
          'mat2c_associative': bool,
          'octonions_associative': bool,
          'ubt_advantage': str
        }
    """
    mat2c_ok = verify_mat2c_associativity()
    octonion_result = demonstrate_octonion_non_associativity()

    return {
        'mat2c_associative': mat2c_ok,
        'octonions_associative': octonion_result['is_associative'],
        'ubt_advantage': (
            "ℂ⊗ℍ ≅ Mat(2,ℂ) is associative — standard QFT machinery applies "
            "without modification.  Furey's ℂ⊗𝕆 is non-associative, creating "
            "fundamental tension with path-integral QFT."
        ),
    }
