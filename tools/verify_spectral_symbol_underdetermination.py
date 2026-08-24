#!/usr/bin/env python3
"""Exact formal heat-coefficient shift under P -> P + u I."""

import sympy as sp


def verify():
    t, u = sp.symbols("t u")
    a0, a2, a4, a6 = sp.symbols("a0 a2 a4 a6")
    heat = a0 / t**2 + a2 / t + a4 + a6 * t
    shifted = sp.series(sp.exp(-u * t) * heat, t, 0, 2).removeO().expand()

    assert sp.simplify(shifted.coeff(t, -2) - a0) == 0
    assert sp.simplify(shifted.coeff(t, -1) - (a2 - u * a0)) == 0
    assert sp.simplify(shifted.coeff(t, 0) - (a4 - u * a2 + u**2 * a0 / 2)) == 0

    print("Spectral scalar-shift heat coefficients: PASS")


if __name__ == "__main__":
    verify()
