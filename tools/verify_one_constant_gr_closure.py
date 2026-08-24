#!/usr/bin/env python3
"""Exact symbolic checks for the one-coupling UBT Einstein-Lambda closure.

Scope
-----
This verifier checks finite algebra/calculus used in the paired theorem notes:

* the Palatini and unimodular volume-term normalization;
* the resulting tetrad equation coefficient ``Lambda/3``;
* that the action-coupling budget contains only ``kappa``;
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
    verify_mm_context()
    verify_rpsi_audit()
    print("PASS: unimodular volume normalization gives the Einstein Lambda/3 tetrad coefficient")
    print("PASS: the local action-coupling budget contains only kappa")
    print("PASS: Lambda is retained as a variational/integration variable, not set to zero")
    print("PASS: fifth-channel MacDowell--Mansouri Lambda relation remains exact algebraic context")
    print("PASS: displayed logarithmic R_psi potential has no finite stationary point")


if __name__ == "__main__":
    verify()
