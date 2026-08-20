#!/usr/bin/env python3
"""Exact checks for the generalized-Dirac action-origin obstruction.

This verifier is intentionally small and exact.  It checks only:
1. a nondegenerate quadratic first-derivative kinetic term has nonzero
   velocity Hessian, hence a second-order Euler-Lagrange principal coefficient;
2. exact factorisation of a second-order operator does not imply either
   first-order factor as an equation of motion;
3. a finite-dimensional Kronecker model of the canonical kinetic principal
   Hessian is nondegenerate whenever both spacetime and field-space pairings
   are nondegenerate.

It does NOT derive the physical UBT action or prove PDE well-posedness.
"""

import sympy as sp


def verify_scalar_velocity_hessian() -> None:
    q, v, a, m = sp.symbols("q v a m", nonzero=True)
    lagrangian = sp.Rational(1, 2) * a * v**2 - sp.Rational(1, 2) * m**2 * q**2
    velocity_hessian = sp.diff(lagrangian, v, 2)
    assert sp.simplify(velocity_hessian - a) == 0


def verify_factorisation_counterexample() -> None:
    x = sp.symbols("x", real=True)
    m = sp.symbols("m", nonzero=True)

    def d_plus(f):
        return sp.diff(f, x) + m * f

    def d_minus(f):
        return sp.diff(f, x) - m * f

    def second_order(f):
        return sp.simplify(d_minus(d_plus(f)))

    f_plus = sp.exp(m * x)
    f_minus = sp.exp(-m * x)

    assert second_order(f_plus) == 0
    assert second_order(f_minus) == 0
    assert sp.simplify(d_plus(f_minus)) == 0
    assert sp.simplify(d_plus(f_plus)) != 0


def verify_kronecker_principal_hessian() -> None:
    g0, g1, h0, h1 = sp.symbols("g0 g1 h0 h1", nonzero=True)
    spacetime = sp.diag(g0, g1)
    fieldspace = sp.diag(h0, h1)
    principal = sp.kronecker_product(spacetime, fieldspace)
    expected = (g0 * g1) ** 2 * (h0 * h1) ** 2
    assert sp.factor(principal.det() - expected) == 0


def main() -> None:
    verify_scalar_velocity_hessian()
    verify_factorisation_counterexample()
    verify_kronecker_principal_hessian()
    print("PASS: exact generalized-Dirac action-order checks")
    print("- quadratic kinetic velocity Hessian is nonzero exactly")
    print("- factorised second-order equation has solutions outside one first-order branch")
    print("- Kronecker principal Hessian determinant is exactly nonzero under nondegeneracy")


if __name__ == "__main__":
    main()
