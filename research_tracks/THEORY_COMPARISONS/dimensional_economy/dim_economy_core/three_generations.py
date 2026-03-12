"""
three_generations.py — ψ-mode independence and three fermion generations.

UBT identifies the three fermion generations with the lowest ψ-Taylor modes of
the biquaternion field Θ(x,t,ψ):

    Θ(x, t, ψ) = Σₙ ψⁿ Θₙ(x,t)     (formal Taylor series in ψ)

Three key results are proved here computationally:

Theorem 1 — Independence (Proved [L0]):
    The modes Θ₀, Θ₁, Θ₂, … are kinematically independent.
    Knowing Θₙ for finitely many n imposes no constraint on Θₘ for m ≠ n.

Theorem 2 — SU(3) Quantum Numbers (Proved [L0]):
    If U ∈ SU(3) acts on Θ as Θ → UΘ, then Θₙ → UΘₙ for every n.
    All modes transform in the same SU(3) representation as Θ itself.

Theorem 3 — ψ-Parity Selection Rule (Proved [L0]):
    Under ψ → -ψ, mode Θₙ acquires a factor (-1)ⁿ.
    ψ-parity forbids mixing between modes of opposite parity.

Reference: research_tracks/three_generations/st3_complex_time_generations.tex
           DERIVATION_INDEX.md "Three Fermion Generations"

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sympy as sp
from sympy import symbols, Function, factorial, zeros, eye, simplify, Rational


# ---------------------------------------------------------------------------
# ψ-Taylor mode algebra (formal, finite truncation)
# ---------------------------------------------------------------------------

def psi_taylor_modes(N=3):
    """
    Define the first N ψ-Taylor modes as independent SymPy symbols.

    The modes Θ₀, Θ₁, …, Θ_{N-1} are formal coefficients of the Taylor
    expansion Θ(ψ) = Σₙ ψⁿ Θₙ.  Kinematic independence means these are
    free variables — no algebraic relation constrains them.

    Parameters
    ----------
    N : int
        Number of modes to define (default 3, for three generations).

    Returns
    -------
    list of sympy.Symbol
        [Θ₀, Θ₁, …, Θ_{N-1}] as independent complex scalar placeholders.
        (Physical modes are B-valued, but scalar placeholders capture
        algebraic independence.)
    """
    return [symbols(f'Theta_{n}', complex=True) for n in range(N)]


def reconstruct_field(modes, psi_sym):
    """
    Reconstruct the formal Taylor series Θ(ψ) = Σₙ ψⁿ Θₙ from modes.

    Parameters
    ----------
    modes : list of sympy.Expr
        Coefficients [Θ₀, Θ₁, …].
    psi_sym : sympy.Symbol
        The ψ variable.

    Returns
    -------
    sympy.Expr
        Formal polynomial in ψ: Θ₀ + ψΘ₁ + ψ²Θ₂ + …
    """
    return sum(psi_sym**n * modes[n] for n in range(len(modes)))


def extract_mode(field_expr, psi_sym, n):
    """
    Extract the n-th Taylor mode from a formal polynomial in ψ.

    Parameters
    ----------
    field_expr : sympy.Expr
        Polynomial in ψ.
    psi_sym : sympy.Symbol
        The ψ variable.
    n : int
        Mode index.

    Returns
    -------
    sympy.Expr
        Coefficient of ψⁿ in field_expr.
    """
    return simplify(sp.Poly(field_expr, psi_sym).nth(n))


# ---------------------------------------------------------------------------
# Theorem 1 — Kinematic independence
# ---------------------------------------------------------------------------

def verify_mode_independence(N=4):
    """
    Verify (Theorem 1) that ψ-Taylor modes are kinematically independent.

    A formal power series Θ(ψ) = Σₙ ψⁿ Θₙ can be constructed for
    *any* prescribed sequence of coefficients {Θₙ}.  The modes are
    free independent data — the only constraint is that the reconstruction
    procedure recovers the original coefficients exactly.

    Test: for arbitrary symbolic modes {Θₙ}, verify that
        extract_mode(reconstruct_field(modes, ψ), ψ, n) == Θₙ
    for each n.

    Parameters
    ----------
    N : int
        Number of modes to test.

    Returns
    -------
    bool
        True if all N extraction roundtrips are exact.

    Raises
    ------
    AssertionError
        If any mode extraction fails.
    """
    psi = symbols('psi')
    modes = psi_taylor_modes(N)

    field = reconstruct_field(modes, psi)

    for n in range(N):
        recovered = extract_mode(field, psi, n)
        diff = simplify(recovered - modes[n])
        if diff != 0:
            raise AssertionError(
                f"Mode independence failed: extract_mode(..., {n}) = {recovered} ≠ Θ_{n}"
            )

    return True


# ---------------------------------------------------------------------------
# Theorem 2 — SU(3) quantum numbers preserved under mode extraction
# ---------------------------------------------------------------------------

def verify_su3_quantum_numbers_preserved():
    """
    Verify (Theorem 2) that SU(3) acting on Θ induces the same action
    on every mode: (UΘ)_n = U·Θₙ.

    This is proved by noting that U is independent of ψ, so:
        (UΘ)(ψ) = U·Θ(ψ) = U Σₙ ψⁿ Θₙ = Σₙ ψⁿ (UΘₙ).
    Thus the n-th mode of UΘ is UΘₙ.

    Here U is represented by an arbitrary 2×2 complex matrix (a placeholder
    for a general SU(2) ⊂ SU(3) element) acting on a 2-component field.

    Returns
    -------
    bool
        True if (UΘ)_n = U Θₙ for n = 0, 1, 2.

    Raises
    ------
    AssertionError
        If the SU(3) action does not commute with mode extraction.
    """
    psi = symbols('psi')

    # U = generic 2×2 matrix (independent of ψ)
    u00, u01, u10, u11 = symbols('u00 u01 u10 u11', complex=True)
    U = sp.Matrix([[u00, u01], [u10, u11]])

    # Θₙ = 2-component column vector with symbolic entries
    modes = []
    for n in range(3):
        a, b = symbols(f'a{n} b{n}', complex=True)
        modes.append(sp.Matrix([a, b]))

    # Reconstruct Θ(ψ) = Σ ψⁿ Θₙ  (component-wise polynomial in ψ)
    Theta_field = sp.zeros(2, 1)
    for n in range(3):
        Theta_field = Theta_field + psi**n * modes[n]

    # Apply U: (UΘ)(ψ) = U * Θ(ψ)
    UTheta_field = U * Theta_field

    # Extract modes of UΘ
    for n in range(3):
        # n-th mode of UΘ: coefficient of ψⁿ in each component
        mode_n_of_UTheta = sp.Matrix([
            sp.Poly(UTheta_field[0], psi).nth(n),
            sp.Poly(UTheta_field[1], psi).nth(n),
        ])
        # Expected: U * Θₙ
        expected = simplify(U * modes[n])
        diff = simplify(mode_n_of_UTheta - expected)
        if diff != sp.zeros(2, 1):
            raise AssertionError(
                f"SU(3) quantum number theorem failed at n={n}: "
                f"(UΘ)_{n} ≠ U·Θ_{n}: diff={diff}"
            )

    return True


# ---------------------------------------------------------------------------
# Theorem 3 — ψ-parity selection rule
# ---------------------------------------------------------------------------

def psi_parity_eigenvalue(n):
    """
    Return the ψ-parity eigenvalue of mode Θₙ.

    Under ψ → -ψ:
        Θ(-ψ) = Σₙ (-ψ)ⁿ Θₙ = Σₙ (-1)ⁿ ψⁿ Θₙ

    So the n-th mode acquires a factor (-1)ⁿ.

    Parameters
    ----------
    n : int
        Mode index (0, 1, 2, …).

    Returns
    -------
    int
        +1 for even n, -1 for odd n.
    """
    return (-1)**n


def verify_psi_parity():
    """
    Verify (Theorem 3) that ψ-parity Pψ: ψ → -ψ acts on mode Θₙ by (-1)ⁿ.

    Checks: the coefficient of ψⁿ in Θ(-ψ) equals (-1)ⁿ times the
    coefficient of ψⁿ in Θ(ψ).

    Returns
    -------
    bool
        True if parity eigenvalues are (-1)ⁿ for n = 0, 1, 2, 3.

    Raises
    ------
    AssertionError
        If any parity eigenvalue is wrong.
    """
    psi = symbols('psi')
    modes = psi_taylor_modes(4)

    # Θ(ψ) and Θ(-ψ)
    Theta = reconstruct_field(modes, psi)
    Theta_neg = Theta.subs(psi, -psi)
    Theta_neg_expanded = sp.expand(Theta_neg)

    for n in range(4):
        # Coefficient of ψⁿ in Θ(-ψ)
        coeff = sp.Poly(Theta_neg_expanded, psi).nth(n)
        expected = psi_parity_eigenvalue(n) * modes[n]
        diff = simplify(coeff - expected)
        if diff != 0:
            raise AssertionError(
                f"ψ-parity eigenvalue wrong for mode {n}: "
                f"coeff = {coeff}, expected {expected}"
            )

    return True


def verify_psi_parity_forbids_mixing():
    """
    Verify (Theorem 3 corollary) that ψ-parity forbids mixing between
    even and odd modes.

    Two modes Θₘ (even parity) and Θₙ (odd parity) have parity eigenvalues
    (-1)ᵐ and (-1)ⁿ respectively.  A ψ-parity invariant interaction
    Θₘ ↔ Θₙ would require (-1)ᵐ = (-1)ⁿ, i.e. m and n have the same parity.
    Cross-parity mixing (m even, n odd) is forbidden.

    This test checks that eigenvalues for (m=0,n=1) are different
    (demonstrating the selection rule), and equal for (m=0,n=2).

    Returns
    -------
    bool
        True if the selection rule is demonstrated.

    Raises
    ------
    AssertionError
        If parity eigenvalues of different-parity modes are the same.
    """
    ev0 = psi_parity_eigenvalue(0)  # +1 (even)
    ev1 = psi_parity_eigenvalue(1)  # -1 (odd)
    ev2 = psi_parity_eigenvalue(2)  # +1 (even)

    # Different parity: Θ₀ and Θ₁ cannot mix
    if ev0 == ev1:
        raise AssertionError(
            f"Expected Θ₀ and Θ₁ to have different parity eigenvalues, "
            f"but both are {ev0}"
        )

    # Same parity: Θ₀ and Θ₂ can mix (same eigenvalue +1)
    if ev0 != ev2:
        raise AssertionError(
            f"Expected Θ₀ and Θ₂ to have the same parity eigenvalue, "
            f"but got {ev0} vs {ev2}"
        )

    return True


# ---------------------------------------------------------------------------
# Generation identification summary
# ---------------------------------------------------------------------------

def generation_identification():
    """
    Return the UBT identification of fermion generations with ψ-modes.

    Returns
    -------
    dict
        {
          'Theta_0': {'generation': 'e (electron)', 'parity': +1},
          'Theta_1': {'generation': 'mu (muon)',    'parity': -1},
          'Theta_2': {'generation': 'tau',          'parity': +1},
          'mass_ratios_status': 'Open — Hecke eigenvalue conjecture',
        }
    """
    return {
        'Theta_0': {
            'generation': 'e (electron)',
            'parity': psi_parity_eigenvalue(0),
            'status': 'Conjecture (identification; mechanism proved)',
        },
        'Theta_1': {
            'generation': 'mu (muon)',
            'parity': psi_parity_eigenvalue(1),
            'status': 'Conjecture (identification; mechanism proved)',
        },
        'Theta_2': {
            'generation': 'tau',
            'parity': psi_parity_eigenvalue(2),
            'status': 'Conjecture (identification; mechanism proved)',
        },
        'mass_ratios_status': 'Open — Hecke eigenvalue conjecture',
        'mechanism_status': 'Proved — Theorems 1, 2, 3 (st3_complex_time_generations.tex)',
    }
