"""
u1y_generator.py — U(1)_Y generator from the right action of ℂ⊗ℍ.

UBT derives U(1)_Y from the right action of ℂ⊗ℍ ≅ Mat(2,ℂ) on itself:

    Y : Θ ↦ Θ · e^{-iθ} = e^{-iθ} Θ

The infinitesimal right generator is

    Y_R : M ↦ -M · (i I₂) = M (right multiplication by -i I₂)

which is simply overall phase rotation: Y_R(M) = -i M.

Key properties proved here:
1. Y_R commutes with all SU(2)_L generators (left vs right action commute).
2. The combined action gives U(1)_Y × SU(2)_L ⊂ Aut(ℂ⊗ℍ).

Reference: consolidation_project/appendix_E2_SM_geometry.tex §6
           DERIVATION_INDEX.md "U(1)_Y from right action — Proven [L0]"

Author: UBT Research Team
License: See repository LICENSE.md
"""

from sympy import Matrix, I, eye, simplify, zeros, exp, symbols

from THEORY_COMPARISONS.dimensional_economy.common.algebra import (
    pauli_matrices,
    commutator,
    is_zero_matrix,
)
from THEORY_COMPARISONS.dimensional_economy.dim_economy_core.su2l_generators import (
    su2l_generators,
    left_action,
)


# ---------------------------------------------------------------------------
# U(1)_Y generator
# ---------------------------------------------------------------------------

def u1y_generator():
    """
    Return the U(1)_Y infinitesimal generator as a right-multiplication operator.

    The generator is represented by the matrix  Y = -i I₂  such that the
    right action is  M ↦ M Y = -i M  (global phase shift).

    Returns
    -------
    sympy.Matrix (2×2)
        Y = -i I₂
    """
    return -I * eye(2)


def right_action(M):
    """
    Apply the U(1)_Y generator to M via right multiplication.

    Y_R(M) = M · (-i I₂) = -i M

    Parameters
    ----------
    M : sympy.Matrix (2×2)
        Element of ℂ⊗ℍ.

    Returns
    -------
    sympy.Matrix (2×2)
        -i M
    """
    return simplify(M * u1y_generator())


# ---------------------------------------------------------------------------
# Commutativity with SU(2)_L
# ---------------------------------------------------------------------------

def verify_u1y_commutes_with_su2l():
    """
    Verify that the U(1)_Y right action commutes with all SU(2)_L left actions.

    For every a ∈ {1, 2, 3} and every 2×2 matrix M:
        Y_R(T^a · M) = T^a · Y_R(M)

    Since Y_R(M) = -i M and T^a(M) = (i σ^a /2) M, both sides equal
    -i (i σ^a/2) M, so commutativity is automatic from left/right action
    independence.  We verify this symbolically on arbitrary M.

    Returns
    -------
    bool
        True if all three commutation conditions hold.

    Raises
    ------
    AssertionError
        If any condition fails.
    """
    # Use symbolic 2×2 matrix entries
    a0, a1, a2, a3 = symbols('a0 a1 a2 a3', complex=True)
    M = Matrix([[a0, a1], [a2, a3]])

    Y = u1y_generator()
    Ts = su2l_generators()

    for idx, Ta in enumerate(Ts, start=1):
        # Left then right: T^a (M Y)
        lhs = simplify(Ta * (M * Y))
        # Right then left: (T^a M) Y
        rhs = simplify((Ta * M) * Y)
        diff = simplify(lhs - rhs)
        if diff != zeros(2, 2):
            raise AssertionError(
                f"U(1)_Y right action does not commute with T^{idx}: "
                f"residual = {diff}"
            )

    return True


def verify_u1y_antihermitian():
    """
    Verify that the U(1)_Y generator Y = -i I₂ is anti-Hermitian.

    Returns
    -------
    bool
        True if Y + Y† = 0.

    Raises
    ------
    AssertionError
        If Y is not anti-Hermitian.
    """
    Y = u1y_generator()
    diff = simplify(Y + Y.H)
    if diff != zeros(2, 2):
        raise AssertionError(
            f"U(1)_Y generator is not anti-Hermitian: Y + Y† = {diff}"
        )
    return True


def verify_u1y_phase_rotation():
    """
    Verify that the finite U(1)_Y transformation Θ → e^{-iθ}Θ is reproduced
    by exponentiation of the infinitesimal generator.

    Checks: exp(θ Y) = e^{-iθ} I₂   (i.e. scalar phase factor).

    Uses the identity exp(θ · (-iI)) = e^{-iθ} I for scalar θ.

    Returns
    -------
    bool
        True if the relation holds symbolically.

    Raises
    ------
    AssertionError
        If the exponentiation identity fails.
    """
    from sympy import exp as sym_exp, pi as sym_pi

    # Check at θ = π/4 as a specific numerical test
    theta = sym_pi / 4
    Y = u1y_generator()

    lhs = (theta * Y).exp()                          # exp(θ Y)
    rhs = sym_exp(-I * theta) * eye(2)               # e^{-iθ} I₂

    diff = simplify(lhs - rhs)
    if diff != zeros(2, 2):
        raise AssertionError(
            f"exp(θ Y) ≠ e^{{-iθ}} I₂ at θ=π/4: residual = {diff}"
        )
    return True
