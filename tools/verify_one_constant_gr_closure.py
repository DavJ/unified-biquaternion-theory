#!/usr/bin/env python3
"""Exact symbolic checks for the one-constant UBT GR closure branch.

Scope
-----
This verifier checks only finite algebra/calculus used in the paired theorem
notes:

* the coefficient relations of the merged fifth-channel MacDowell--Mansouri
  candidate;
* subtraction of the Euler topological density and the ell -> infinity
  Poincare contraction;
* the resulting one-symbol local gravity coefficient set;
* the derivative obstruction in the historical logarithmic R_psi potential;
* the elementary fixed-point consequence of an exactly inversion-invariant
  differentiable potential.

It does not formalize the full differential-form variational theorem or the
split-jet rank theorem, which have separate verifiers in the repository.
"""

from __future__ import annotations

import sympy as sp


def verify_mm_contraction() -> None:
    ell = sp.symbols("ell", positive=True, finite=True)
    kappa = sp.symbols("kappa", positive=True, finite=True)
    eps = sp.symbols("eps", nonzero=True, real=True)

    Lambda = 3 * eps / ell**2
    c_euler = -eps * ell**2 / (8 * kappa)
    c_palatini = 1 / (4 * kappa)
    c_volume = -eps / (8 * kappa * ell**2)

    assert sp.simplify(c_volume + Lambda / (24 * kappa)) == 0

    # Topological subtraction removes c_euler from the local action.
    local_coefficients = {
        "EER": c_palatini,
        "EEEE": c_volume,
    }

    assert sp.limit(Lambda, ell, sp.oo) == 0
    assert sp.limit(local_coefficients["EEEE"], ell, sp.oo) == 0
    assert sp.limit(local_coefficients["EER"], ell, sp.oo) == c_palatini

    contracted = sp.simplify(sp.limit(local_coefficients["EER"], ell, sp.oo))
    assert contracted.free_symbols == {kappa}

    # The de Sitter/anti-de Sitter translation commutator scale contracts away.
    assert sp.limit(1 / ell**2, ell, sp.oo) == 0

    # The divergent Euler coefficient is harmless only after the explicitly
    # stated topological subtraction / fixed-topology local-EOM restriction.
    assert sp.limit(abs(c_euler), ell, sp.oo) == sp.oo


def verify_rpsi_audit() -> None:
    R = sp.symbols("R", positive=True, finite=True)
    E3prime0 = sp.symbols("E3prime0", real=True)
    V = -sp.Rational(3, 2) * sp.log(2 * sp.pi * R) - E3prime0
    derivative = sp.simplify(sp.diff(V, R))

    assert derivative == -sp.Rational(3, 2) / R
    assert sp.solve(sp.Eq(derivative, 0), R) == []

    # If a completed differentiable potential obeys V(x)=V(1/x), then
    # differentiation implies V'(x)=-(1/x^2)V'(1/x). At x=1 this is
    # p=-p, hence p=0. Keep this as exact scalar algebra rather than assuming
    # any particular completed potential.
    p = sp.symbols("p", real=True)
    assert sp.solve(sp.Eq(p, -p), p) == [0]


def verify() -> None:
    verify_mm_contraction()
    verify_rpsi_audit()
    print("PASS: Euler-subtracted fifth-channel action has a finite Poincare limit")
    print("PASS: contracted local gravity coefficients contain only kappa")
    print("PASS: bare Lambda tends to zero as ell -> infinity")
    print("PASS: displayed logarithmic R_psi potential has no finite stationary point")
    print("PASS: exact inversion symmetry forces stationarity at the self-dual ratio")


if __name__ == "__main__":
    verify()
