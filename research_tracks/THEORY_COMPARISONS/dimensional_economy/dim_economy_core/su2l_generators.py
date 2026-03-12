"""
su2l_generators.py — SU(2)_L generators from the left action of ℂ⊗ℍ.

UBT derives SU(2)_L from the left action of ℂ⊗ℍ ≅ Mat(2,ℂ) on itself:

    T^a : M ↦ (i σ^a / 2) M,   a ∈ {1, 2, 3}

The generators T^a satisfy the su(2) commutation relations

    [T^a, T^b] = ε^{abc} T^c

(Note: using physicists' convention where [T^a, T^b] = i ε^{abc} T^c would
require a factor of i in the structure constants; here we use the
mathematician's convention [T^a, T^b] = ε^{abc} T^c with
T^a = iσ^a/2 already incorporating the i.)

Reference: consolidation_project/appendix_E2_SM_geometry.tex §6
           DERIVATION_INDEX.md "SU(2)_L from left action — Proven [L0]"

Author: UBT Research Team
License: See repository LICENSE.md
"""

from sympy import Matrix, I, eye, simplify, zeros, symbols

from THEORY_COMPARISONS.dimensional_economy.common.algebra import (
    pauli_matrices,
    commutator,
    levi_civita,
    is_zero_matrix,
)


# ---------------------------------------------------------------------------
# Generator construction
# ---------------------------------------------------------------------------

def su2l_generators():
    """
    Return the three SU(2)_L generators as left-multiplication operators.

    T^a is represented as the 2×2 matrix  -(i/2) σ^a.  The left action
    on a generic M ∈ Mat(2,ℂ) is  M ↦ T^a M = (-(i/2)σ^a) M.

    This sign convention (anti-Hermitian generators L^a = -i J^a where
    J^a = σ^a/2 are the standard Hermitian generators) ensures that the
    Lie algebra relation

        [T^a, T^b] = ε^{abc} T^c

    holds with the standard (positive) Levi-Civita structure constants.

    Derivation: [T^a, T^b] = [-(i/2)σ^a, -(i/2)σ^b]
                            = (-i/2)²[σ^a, σ^b]
                            = (-1/4) · 2i ε^{abc} σ^c
                            = (-i/2) ε^{abc} σ^c
                            = ε^{abc} · (-(i/2)σ^c)
                            = ε^{abc} T^c.  ✓

    Returns
    -------
    tuple of sympy.Matrix
        (T1, T2, T3), each a 2×2 complex matrix equal to -(i/2) σ^a.
    """
    _, sigma1, sigma2, sigma3 = pauli_matrices()
    T1 = -I * sigma1 / 2
    T2 = -I * sigma2 / 2
    T3 = -I * sigma3 / 2
    return T1, T2, T3


# ---------------------------------------------------------------------------
# Verification helpers
# ---------------------------------------------------------------------------

def verify_su2_commutation_relations():
    """
    Verify [T^a, T^b] = ε^{abc} T^c for all a, b ∈ {1, 2, 3}.

    The relation is checked symbolically for all 9 pairs (a, b).

    Returns
    -------
    bool
        True if all 9 commutation relations hold exactly.

    Raises
    ------
    AssertionError
        With a descriptive message for any failing pair.
    """
    T = su2l_generators()            # T[0] = T1, T[1] = T2, T[2] = T3

    for a in range(1, 4):
        for b in range(1, 4):
            lhs = commutator(T[a - 1], T[b - 1])
            rhs = zeros(2, 2)
            for c in range(1, 4):
                rhs += levi_civita(a, b, c) * T[c - 1]
            rhs = simplify(rhs)
            diff = simplify(lhs - rhs)
            if diff != zeros(2, 2):
                raise AssertionError(
                    f"[T^{a}, T^{b}] = ε^{{{a}{b}c}} T^c FAILED: "
                    f"residual = {diff}"
                )

    return True


def verify_generators_traceless():
    """
    Verify that all T^a are traceless (required for su(2) ⊂ sl(2,ℂ)).

    Returns
    -------
    bool
        True if all three generators have zero trace.

    Raises
    ------
    AssertionError
        If any generator is not traceless.
    """
    for a, Ta in enumerate(su2l_generators(), start=1):
        tr = simplify(Ta.trace())
        if tr != 0:
            raise AssertionError(
                f"T^{a} is not traceless: trace = {tr}"
            )
    return True


def verify_generators_antihermitian():
    """
    Verify that T^a are anti-Hermitian: (T^a)† = -T^a.

    Anti-Hermiticity is the infinitesimal condition for unitarity (e^{θ T^a}
    is unitary when T^a is anti-Hermitian).

    Returns
    -------
    bool
        True if all three generators are anti-Hermitian.

    Raises
    ------
    AssertionError
        If any generator fails the condition.
    """
    for a, Ta in enumerate(su2l_generators(), start=1):
        diff = simplify(Ta + Ta.H)   # T^a + (T^a)† should be zero
        if diff != zeros(2, 2):
            raise AssertionError(
                f"T^{a} is not anti-Hermitian: T^{a} + (T^{a})† = {diff}"
            )
    return True


def left_action(generator_index, M):
    """
    Apply SU(2)_L generator T^a to matrix M by left multiplication.

    T^a · M = (-(i/2) σ^a) M

    Parameters
    ----------
    generator_index : int
        1, 2, or 3 for T^1, T^2, T^3.
    M : sympy.Matrix (2×2)
        Element of ℂ⊗ℍ ≅ Mat(2,ℂ).

    Returns
    -------
    sympy.Matrix (2×2)
        T^a M
    """
    T = su2l_generators()
    return simplify(T[generator_index - 1] * M)
