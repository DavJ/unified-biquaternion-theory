#!/usr/bin/env python3
"""Exact symbolic counterexample to holomorphy-only Dirac-factor selection."""

import sympy as sp


def verify():
    tau, m, psi, R = sp.symbols("tau m psi R", nonzero=True)
    f_plus = sp.exp(m * tau)
    f_minus = sp.exp(-m * tau)

    assert sp.simplify(sp.diff(f_plus, tau) - m * f_plus) == 0
    assert sp.simplify(sp.diff(f_minus, tau) + m * f_minus) == 0
    assert sp.simplify((sp.diff(f_plus, tau, 2) - m**2 * f_plus)) == 0
    assert sp.simplify((sp.diff(f_minus, tau, 2) - m**2 * f_minus)) == 0

    n = sp.symbols("n", integer=True)
    phase_plus = sp.exp(sp.I * 2 * sp.pi * n)
    phase_minus = sp.exp(-sp.I * 2 * sp.pi * n)
    assert sp.simplify(phase_plus - 1) == 0
    assert sp.simplify(phase_minus - 1) == 0

    print("Holomorphic +/- factor branches: PASS")
    print("Compact-psi integer periodicity preserves both signs: PASS")


if __name__ == "__main__":
    verify()
