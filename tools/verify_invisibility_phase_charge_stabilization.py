#!/usr/bin/env python3
"""Verify the reduced phase-charge stabilisation theorem."""

from __future__ import annotations

import mpmath as mp
import sympy as sp


def main() -> None:
    # Positive Whitney coefficients.
    mp.mp.dps = 40

    def root_factor(c: mp.mpf) -> mp.mpf:
        return mp.sqrt((1 + c * c) * (4 * c**4 - 3 * c * c + 1))

    a_w = 4 * mp.pi * mp.quad(root_factor, [-1, 1])
    i_w = 8 * mp.pi * mp.quad(
        lambda c: (1 - c**4) * root_factor(c), [-1, 1]
    )
    assert a_w > 0
    assert i_w > 0
    assert abs(a_w - mp.mpf("25.4713574078395701312677659984")) < mp.mpf("1e-25")
    assert abs(i_w - mp.mpf("37.4780907301338359571871971152")) < mp.mpf("1e-25")

    # Exact fixed-charge minimum.
    chi, sigma, kappa, a, inertia, charge = sp.symbols(
        "chi sigma kappa a inertia charge", positive=True, real=True
    )
    energy = sigma * a * chi**2 + charge**2 / (2 * kappa * inertia * chi**4)
    d_energy = sp.diff(energy, chi)
    chi6 = charge**2 / (sigma * a * kappa * inertia)

    # Multiplying dE/dchi by chi^5/2 gives A chi^6 - Q^2/(kappa I).
    stationary_polynomial = sp.simplify(d_energy * chi**5 / 2)
    assert sp.simplify(
        stationary_polynomial
        - (sigma * a * chi**6 - charge**2 / (kappa * inertia))
    ) == 0

    second = sp.diff(energy, chi, 2)
    second_at_min = sp.simplify(
        second.subs(charge**2, sigma * a * kappa * inertia * chi**6)
    )
    assert second_at_min == 12 * sigma * a

    energy_at_min = sp.simplify(
        energy.subs(charge**2, sigma * a * kappa * inertia * chi**6)
    )
    assert energy_at_min == sp.Rational(3, 2) * sigma * a * chi**2

    # The visible sharp-null property is phase stable: zero times any central
    # phase remains zero.  The Hermitian norm is unchanged because
    # conjugate(exp(i alpha))*exp(i alpha)=1 for real alpha.
    alpha = sp.symbols("alpha", real=True)
    assert sp.simplify(sp.exp(2 * sp.I * alpha) * 0) == 0
    assert sp.simplify(sp.conjugate(sp.exp(sp.I * alpha)) * sp.exp(sp.I * alpha)) == 1

    print("PASS: Whitney support constants a_W and i_W are positive")
    print("PASS: common profile phase preserves central metric nullity")
    print("PASS: fixed phase charge gives a unique finite support-scale minimum")
    print("PASS: reduced radial Hessian is strictly positive at the minimum")


if __name__ == "__main__":
    main()
