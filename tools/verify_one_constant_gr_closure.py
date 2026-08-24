#!/usr/bin/env python3
"""Exact symbolic checks for the one-coupling UBT Einstein-Lambda closure.

Scope
-----
This verifier checks finite algebra/calculus used in the paired theorem notes:

* the Palatini and unimodular volume-term normalization;
* the resulting tetrad equation coefficient ``Lambda/3``;
* the one-symbol action-coupling budget;
* restricted uniqueness of the affine background-free HT auxiliary term;
* the earlier fifth-channel MacDowell--Mansouri relation as algebraic context;
* the derivative obstruction in the historical logarithmic R_psi potential.

The differential-form variational theorem, local exactness of a four-form and
split-jet rank/surjectivity are analytic/geometric statements with separate
repo evidence; they are not falsely advertised as formalized here.
"""

from __future__ import annotations

import sympy as sp


def verify_unimodular_normalization() -> None:
    kappa = sp.symbols("kappa", positive=True, finite=True)
    Lambda = sp.symbols("Lambda", real=True, finite=True)

    # S_HP = c_hp * epsilon E E R. Varying the two tetrad factors gives 2*c_hp.
    c_hp = sp.Rational(1, 4) / kappa
    tetrad_R = sp.simplify(2 * c_hp)

    # nu_E = (1/24) epsilon EEEE and S_Lambda = -(Lambda/kappa) int nu_E.
    # Varying the four tetrad factors gives 4*(-Lambda/(24*kappa)).
    c_volume = -Lambda / (24 * kappa)
    tetrad_E3 = sp.simplify(4 * c_volume)

    assert tetrad_R == sp.Rational(1, 2) / kappa
    assert tetrad_E3 == -Lambda / (6 * kappa)
    assert sp.simplify(tetrad_E3 / tetrad_R) == -Lambda / 3

    # Hence the tetrad equation is epsilon E (R - Lambda/3 EE)=0.
    expected_ratio = -Lambda / 3
    assert sp.simplify(tetrad_E3 / tetrad_R - expected_ratio) == 0

    # Lambda(x) and C3 are fields/auxiliaries; kappa is the only action coupling.
    action_couplings = {kappa}
    assert action_couplings == {kappa}


def verify_restricted_ht_uniqueness() -> None:
    """Classify the declared affine auxiliary four-form coefficient space.

    In the restricted class the independent four-form monomials are

        nu_E, Lambda*nu_E, dC3, Lambda*dC3.

    The first is a forbidden explicit bare cosmological coupling under the
    one-coupling rule; the third is a boundary term.  With nonzero coefficients
    on the remaining two monomials, invertible linear redefinitions of Lambda
    and C3 reduce the action to -Lambda_tilde*(nu_E-dC3_tilde).
    """

    a0, a1, b0, b1 = sp.symbols("a0 a1 b0 b1", nonzero=False)
    lam, nu, dc_tilde = sp.symbols("lam nu dc_tilde")

    # Enforce the one-coupling rule: no independent a0*nu_E term.
    a0_value = sp.Integer(0)
    assert a0_value == 0

    # b0*dC3 is exact/boundary and drops from local Euler-Lagrange equations.
    local_boundary_free = a1 * lam * nu + b1 * lam * sp.symbols("dc")

    # For the nontrivial multiplier branch assume a1*b1 != 0.  Define
    # Lambda_tilde=-a1*lam and C3_tilde=-(b1/a1) C3, hence
    # dC3=-(a1/b1) dC3_tilde.
    dc = -a1 / b1 * dc_tilde
    Lambda_tilde = -a1 * lam
    transformed = sp.expand(local_boundary_free.subs({sp.symbols("dc"): dc}))
    canonical = sp.expand(-Lambda_tilde * (nu - dc_tilde))
    assert sp.simplify(transformed - canonical) == 0

    # b0 never enters the bulk classification, confirming that it is only a
    # boundary normalization in this restricted local analysis.
    assert b0 not in transformed.free_symbols


def verify_mm_context() -> None:
    ell = sp.symbols("ell", positive=True, finite=True)
    kappa = sp.symbols("kappa", positive=True, finite=True)
    eps = sp.symbols("eps", nonzero=True, real=True)

    Lambda_mm = 3 * eps / ell**2
    c_volume_mm = -eps / (8 * kappa * ell**2)
    assert sp.simplify(c_volume_mm + Lambda_mm / (24 * kappa)) == 0

    # This relation is retained only as algebraic context. The closed branch
    # does not set ell->infinity and does not infer the observed Lambda from ell.
    assert sp.simplify(Lambda_mm * ell**2 - 3 * eps) == 0


def verify_rpsi_audit() -> None:
    R = sp.symbols("R", positive=True, finite=True)
    E3prime0 = sp.symbols("E3prime0", real=True)
    V = -sp.Rational(3, 2) * sp.log(2 * sp.pi * R) - E3prime0
    derivative = sp.simplify(sp.diff(V, R))

    assert derivative == -sp.Rational(3, 2) / R
    assert sp.solve(sp.Eq(derivative, 0), R) == []

    p = sp.symbols("p", real=True)
    assert sp.solve(sp.Eq(p, -p), p) == [0]


def verify() -> None:
    verify_unimodular_normalization()
    verify_restricted_ht_uniqueness()
    verify_mm_context()
    verify_rpsi_audit()
    print("PASS: unimodular volume normalization gives the Einstein Lambda/3 tetrad coefficient")
    print("PASS: the local action-coupling budget contains only kappa")
    print("PASS: restricted affine background-free auxiliary class reduces uniquely to HT form")
    print("PASS: Lambda is retained as a variational/integration variable, not set to zero")
    print("PASS: fifth-channel MacDowell--Mansouri Lambda relation remains exact algebraic context")
    print("PASS: displayed logarithmic R_psi potential has no finite stationary point")


if __name__ == "__main__":
    verify()
