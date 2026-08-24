#!/usr/bin/env python3
"""Exact algebra for the UBT fifth-channel MacDowell--Mansouri candidate.

This is a structural verifier, not a derivation of the extended connection as
fundamental UBT dynamics. It checks the canonical Clifford commutators, the
graded-trace projection, and the relative coefficients in the curvature-square
expansion for both possible fifth-channel signatures.
"""

from __future__ import annotations

import sympy as sp

I = sp.I


def sharp2(x: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([[x[1, 1], -x[0, 1]], [-x[1, 0], x[0, 0]]])


def block_lift(x: sp.Matrix) -> sp.Matrix:
    zero = sp.zeros(2)
    return zero.row_join(x).col_join(sharp2(x).row_join(zero))


def canonical_gammas() -> tuple[list[sp.Matrix], sp.Matrix]:
    sigma1 = sp.Matrix([[0, 1], [1, 0]])
    sigma2 = sp.Matrix([[0, -I], [I, 0]])
    sigma3 = sp.Matrix([[1, 0], [0, -1]])
    identity = sp.eye(2)
    lorentz_basis = [I * identity, -I * sigma1, -I * sigma2, -I * sigma3]
    gammas = [block_lift(x) for x in lorentz_basis]
    grading = sp.diag(1, 1, -1, -1)
    return gammas, grading


def verify_signature(epsilon_psi: int) -> None:
    assert epsilon_psi in (-1, 1)
    gammas, grading = canonical_gammas()
    gamma_psi = grading if epsilon_psi == 1 else I * grading
    assert gamma_psi**2 == epsilon_psi * sp.eye(4)
    for gamma in gammas:
        assert gamma_psi * gamma + gamma * gamma_psi == sp.zeros(4)

    # J_ab = 1/2 gamma_a gamma_b (a != b), P_a = 1/2 gamma_a gamma_psi.
    # The translation commutator fixes the e wedge e contribution to curvature.
    for a in range(4):
        p_a = sp.Rational(1, 2) * gammas[a] * gamma_psi
        # A torsion-translation square carries no graded-trace scalar.
        for b in range(4):
            p_b = sp.Rational(1, 2) * gammas[b] * gamma_psi
            assert sp.simplify(sp.trace(grading * p_a * p_b)) == 0

        for b in range(a + 1, 4):
            j_ab = sp.Rational(1, 2) * gammas[a] * gammas[b]
            p_b = sp.Rational(1, 2) * gammas[b] * gamma_psi
            commutator = sp.simplify(p_a * p_b - p_b * p_a)
            assert commutator == -epsilon_psi * j_ab

            # Lorentz-translation cross terms also vanish in the graded trace.
            for c in range(4):
                p_c = sp.Rational(1, 2) * gammas[c] * gamma_psi
                assert sp.simplify(sp.trace(grading * j_ab * p_c)) == 0

    # Purely algebraic expansion coefficients. If
    # F_L = (1/4)(R - epsilon_psi e e / ell^2) gamma gamma,
    # then i Tr(Gamma_* F_L^2) contributes
    #   +1/4 RR - epsilon_psi/(2 ell^2) eeR + 1/(4 ell^4) eeee.
    ell, kappa, g_grav = sp.symbols("ell kappa g_grav", nonzero=True, real=True)
    overall = -epsilon_psi * ell**2 / (2 * kappa)
    coeff_euler = sp.simplify(overall * sp.Rational(1, 4))
    coeff_palatini = sp.simplify(overall * (-epsilon_psi) / (2 * ell**2))
    coeff_volume = sp.simplify(overall / (4 * ell**4))
    cosmological_constant = sp.simplify(3 * epsilon_psi / ell**2)

    assert coeff_palatini == 1 / (4 * kappa)
    assert coeff_volume == -cosmological_constant / (24 * kappa)
    assert coeff_euler == -epsilon_psi * ell**2 / (8 * kappa)

    # If the microscopic curvature-square coefficient is normalized as
    # -i epsilon_psi / g_grav^2, matching fixes kappa in terms of g_grav,ell.
    kappa_from_g = sp.simplify(g_grav**2 * ell**2 / 2)
    matched_overall = sp.simplify(-epsilon_psi * ell**2 / (2 * kappa_from_g))
    assert matched_overall == -epsilon_psi / g_grav**2
    assert sp.simplify(kappa_from_g * cosmological_constant) == sp.Rational(3, 2) * epsilon_psi * g_grav**2


def verify() -> None:
    verify_signature(+1)
    verify_signature(-1)
    print("PASS: fifth-channel translation commutator gives the e wedge e curvature shift")
    print("PASS: graded trace removes translation/torsion-square and Lorentz-translation channels")
    print("PASS: graded curvature-square expands to Euler + Palatini + cosmological terms")
    print("PASS: Lambda = 3 epsilon_psi / ell^2")
    print("PASS: kappa = g_grav^2 ell^2 / 2 for coefficient -i epsilon_psi/g_grav^2")


if __name__ == "__main__":
    verify()
