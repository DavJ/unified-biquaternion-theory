#!/usr/bin/env python3
"""Exact checks for the UBT covariant-tetrad metric and rank theorem."""
from __future__ import annotations

import sympy as sp


def qmul(a: tuple[sp.Expr, sp.Matrix], b: tuple[sp.Expr, sp.Matrix]):
    """Quaternion product with complex scalar coefficients."""
    s, u = a
    t, v = b
    return sp.expand(s * t - (u.dot(v))), sp.simplify(s * v + t * u + u.cross(v))


def qsharp(a: tuple[sp.Expr, sp.Matrix]):
    s, u = a
    return s, -u


def central_jordan_check() -> None:
    x0, y0 = sp.symbols("x0 y0", real=True)
    xs = sp.Matrix(sp.symbols("x1:4", real=True))
    ys = sp.Matrix(sp.symbols("y1:4", real=True))
    X = (sp.I * x0, xs)
    Y = (sp.I * y0, ys)
    p1 = qmul(qsharp(X), Y)
    p2 = qmul(qsharp(Y), X)
    scalar = sp.simplify((p1[0] + p2[0]) / 2)
    vector = sp.simplify((p1[1] + p2[1]) / 2)
    expected = -x0 * y0 + xs.dot(ys)
    assert sp.simplify(scalar - expected) == 0
    assert vector == sp.zeros(3, 1)


def rank_check() -> tuple[int, int]:
    # Evaluate at the identity tetrad. Rank is invariant on the open GL(4) orbit.
    eta = sp.diag(-1, 1, 1, 1)
    variables = sp.symbols("d0:16")
    de = sp.Matrix(4, 4, variables)
    dg = sp.simplify(de * eta + eta * de.T)
    components = []
    for mu in range(4):
        for nu in range(mu, 4):
            components.append(dg[mu, nu])
    jac = sp.Matrix(components).jacobian(sp.Matrix(variables))
    rank = jac.rank()
    nullity = 16 - rank
    assert rank == 10
    assert nullity == 6
    return rank, nullity


def arbitrary_metric_variation_check() -> None:
    eta = sp.diag(-1, 1, 1, 1)
    hsymbols = sp.symbols("h00 h01 h02 h03 h11 h12 h13 h22 h23 h33")
    h00, h01, h02, h03, h11, h12, h13, h22, h23, h33 = hsymbols
    h = sp.Matrix([
        [h00, h01, h02, h03],
        [h01, h11, h12, h13],
        [h02, h12, h22, h23],
        [h03, h13, h23, h33],
    ])
    # At e=I, e^{rho a}=eta^{a rho}; de = 1/2 h eta.
    de = sp.Rational(1, 2) * h * eta
    dg = sp.simplify(de * eta + eta * de.T)
    assert sp.simplify(dg - h) == sp.zeros(4)


def main() -> None:
    central_jordan_check()
    rank, nullity = rank_check()
    arbitrary_metric_variation_check()
    print("COVARIANT TETRAD CHECK: ALL CHECKS PASSED")
    print("  central anticommutator: Lorentz scalar times unit")
    print(f"  tetrad-to-metric differential: rank {rank}, kernel {nullity}")
    print("  arbitrary symmetric metric variation: explicitly reachable")
    print("  NOT TESTED: dynamical derivation of Omega or on-shell integrability")


if __name__ == "__main__":
    main()
