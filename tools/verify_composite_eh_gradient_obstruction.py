#!/usr/bin/env python3
"""Exact symbolic check of the affine pure-gradient composite-metric variation."""

import sympy as sp


def verify():
    # Constant Lorentz tetrad E_mu^a and arbitrary first derivatives
    # P_mu^a = partial_mu(delta X^a).  The background metric variation is
    # delta g_mn = eta_ab (P_m^a E_n^b + E_m^a P_n^b).
    E = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"E{i}{j}"))
    P = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"P{i}{j}"))
    eta = sp.diag(-1, 1, 1, 1)

    dg = P * eta * E.T + E * eta * P.T

    # xi_n = eta_ab E_n^a delta X^b.  Since E is constant,
    # partial_m xi_n = P_m^b eta_ab E_n^a = (P eta E^T)_mn.
    dxi = P * eta * E.T
    lie = dxi + dxi.T
    assert sp.simplify(dg - lie) == sp.zeros(4)

    # Symmetric contraction with an arbitrary symmetric tensor Q is twice the
    # contraction Q^{mn} partial_m xi_n before integration by parts.
    q = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"q{min(i,j)}{max(i,j)}"))
    lhs = sp.expand(sum(q[i, j] * dg[i, j] for i in range(4) for j in range(4)))
    rhs = sp.expand(2 * sum(q[i, j] * dxi[i, j] for i in range(4) for j in range(4)))
    assert sp.simplify(lhs - rhs) == 0

    print("Composite EH pure-gradient variation = Lie derivative: PASS")
    print("Symmetric contraction reduces to divergence after integration by parts: PASS")


if __name__ == "__main__":
    verify()
