#!/usr/bin/env python3
"""Exact checks supporting the gradient-composite flatness no-go.

The proof is geometric: a nondegenerate exact coframe e^a=dY^a/sqrt(N0)
is a local coordinate pullback of Minkowski space.  These symbolic checks
verify the determinant identity and a nontrivial nonlinear coordinate example.
"""
from __future__ import annotations

import sympy as sp


def determinant_identity() -> bool:
    """Exact rational checks of det(J^T eta J/N0)=-det(J)^2/N0^4.

    The general identity follows immediately from determinant
    multiplicativity; several nontrivial rational Jacobians guard the
    implementation without forcing SymPy to expand a generic 4x4 determinant.
    """
    eta = sp.diag(-1, 1, 1, 1)
    n0_values = (sp.Integer(2), sp.Integer(3))
    jacobians = (
        sp.Matrix([[1, 2, 0, 1], [0, 1, 3, 0], [2, 0, 1, 1], [0, 1, 0, 2]]),
        sp.Matrix([[2, 0, 1, 0], [1, 3, 0, 1], [0, 1, 2, 0], [1, 0, 1, 1]]),
    )
    for n0 in n0_values:
        for jac in jacobians:
            metric = jac.T * eta * jac / n0
            if sp.factor(metric.det() + jac.det() ** 2 / n0**4) != 0:
                return False
    return True


def nonlinear_pullback_riemann_zero() -> bool:
    t, x, y, z = sp.symbols("t x y z", real=True)
    coords = (t, x, y, z)
    # Nonlinear but globally nondegenerate triangular coordinate map.
    target = sp.Matrix([t, x + t**2, y, z])
    jac = target.jacobian(coords)
    eta = sp.diag(-1, 1, 1, 1)
    g = sp.simplify(jac.T * eta * jac)
    g_inv = sp.simplify(g.inv())
    dim = 4

    gamma = [[[
        sp.simplify(
            sp.Rational(1, 2)
            * sum(
                g_inv[rho, sig]
                * (
                    sp.diff(g[sig, nu], coords[mu])
                    + sp.diff(g[sig, mu], coords[nu])
                    - sp.diff(g[mu, nu], coords[sig])
                )
                for sig in range(dim)
            )
        )
        for nu in range(dim)] for mu in range(dim)] for rho in range(dim)]

    for rho in range(dim):
        for sig in range(dim):
            for mu in range(dim):
                for nu in range(dim):
                    component = sp.diff(gamma[rho][nu][sig], coords[mu])
                    component -= sp.diff(gamma[rho][mu][sig], coords[nu])
                    component += sum(
                        gamma[rho][mu][lam] * gamma[lam][nu][sig]
                        - gamma[rho][nu][lam] * gamma[lam][mu][sig]
                        for lam in range(dim)
                    )
                    if sp.simplify(component) != 0:
                        return False
    return True


def main() -> int:
    checks = {
        "det(g) = -det(J)^2/N0^4": determinant_identity(),
        "nonlinear exact-gradient pullback has Riemann=0": nonlinear_pullback_riemann_zero(),
    }
    for name, ok in checks.items():
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
