#!/usr/bin/env python3
"""Exact checks for the GAP-10Omega classical connection theorem.

Verifies:
1. Cartesian Minkowski tetrad gives Gamma = omega = 0.
2. A flat cylindrical/polar tetrad gives nonzero omega but zero curvature.
3. The linear uniqueness system for a Lorentz-valued torsion difference has
   full rank 24 at an orthonormal tetrad.
4. The exact contorsion formula reconstructs arbitrary antisymmetric torsion
   and is Lorentz-metric compatible.

This does NOT test the UBT action, torsion dynamics, or existence of Theta
solving E_mu = D_mu Theta / sqrt(N0).
"""
from __future__ import annotations

import sympy as sp


def christoffel(coords: list[sp.Symbol], g: sp.Matrix):
    n = len(coords)
    ginv = sp.simplify(g.inv())
    Gamma = [[ [sp.S.Zero for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for rho in range(n):
        for mu in range(n):
            for nu in range(n):
                expr = sp.S.Zero
                for sig in range(n):
                    expr += ginv[rho, sig] * (
                        sp.diff(g[nu, sig], coords[mu])
                        + sp.diff(g[mu, sig], coords[nu])
                        - sp.diff(g[mu, nu], coords[sig])
                    ) / 2
                Gamma[rho][mu][nu] = sp.simplify(expr)
    return Gamma


def spin_connection(coords: list[sp.Symbol], e: sp.Matrix, eta: sp.Matrix):
    """e[mu,a] is a coframe; returns omega[mu][a][b]."""
    n = len(coords)
    g = sp.simplify(e * eta * e.T)
    Gamma = christoffel(coords, g)
    einv = sp.simplify(e.inv())  # einv[b,nu] = e_b^nu
    omega = [[ [sp.S.Zero for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for mu in range(n):
        for a in range(n):
            for b in range(n):
                expr = sp.S.Zero
                for nu in range(n):
                    inner = -sp.diff(e[nu, a], coords[mu])
                    for rho in range(n):
                        inner += Gamma[rho][mu][nu] * e[rho, a]
                    expr += einv[b, nu] * inner
                omega[mu][a][b] = sp.simplify(expr)
    return g, Gamma, omega


def curvature(coords: list[sp.Symbol], omega):
    n = len(coords)
    R = [[[[sp.S.Zero for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for mu in range(n):
        for nu in range(n):
            for a in range(n):
                for b in range(n):
                    expr = sp.diff(omega[nu][a][b], coords[mu]) - sp.diff(
                        omega[mu][a][b], coords[nu]
                    )
                    for c in range(n):
                        expr += omega[mu][a][c] * omega[nu][c][b]
                        expr -= omega[nu][a][c] * omega[mu][c][b]
                    R[mu][nu][a][b] = sp.simplify(expr)
    return R


def assert_all_zero(items):
    for item in items:
        assert sp.simplify(item) == 0, item


def flatten4(x):
    for a in x:
        for b in a:
            for c in b:
                for d in c:
                    yield d


def test_minkowski():
    t, x, y, z = sp.symbols("t x y z", real=True)
    coords = [t, x, y, z]
    eta = sp.diag(-1, 1, 1, 1)
    e = sp.eye(4)
    g, Gamma, omega = spin_connection(coords, e, eta)
    assert g == eta
    assert_all_zero(Gamma[r][m][n] for r in range(4) for m in range(4) for n in range(4))
    assert_all_zero(omega[m][a][b] for m in range(4) for a in range(4) for b in range(4))


def test_flat_polar_frame():
    t, r, phi, z = sp.symbols("t r phi z", real=True, positive=True)
    coords = [t, r, phi, z]
    eta = sp.diag(-1, 1, 1, 1)
    e = sp.diag(1, 1, r, 1)
    g, _, omega = spin_connection(coords, e, eta)
    assert g == sp.diag(-1, 1, r**2, 1)
    nonzero = {
        (mu, a, b): val
        for mu in range(4)
        for a in range(4)
        for b in range(4)
        if (val := sp.simplify(omega[mu][a][b])) != 0
    }
    assert nonzero == {(2, 1, 2): -1, (2, 2, 1): 1}, nonzero
    R = curvature(coords, omega)
    assert_all_zero(flatten4(R))



def test_contorsion_reconstruction():
    # T_{a b c} is antisymmetric in its last two indices.
    symbols = {}
    vars_ = []
    for a in range(4):
        for b in range(4):
            for c in range(b + 1, 4):
                v = sp.symbols(f"t{a}{b}{c}")
                symbols[(a, b, c)] = v
                vars_.append(v)

    def T(a, b, c):
        if b == c:
            return sp.S.Zero
        if b < c:
            return symbols[(a, b, c)]
        return -symbols[(a, c, b)]

    # Convention: T^a = de^a + omega^a_b wedge e^b and
    # K_{abc} = 1/2 (T_{cab} - T_{abc} - T_{bca}).
    def K(a, b, c):
        return sp.simplify((T(c, a, b) - T(a, b, c) - T(b, c, a)) / 2)

    # Metric compatibility: K_{abc} = -K_{bac}.
    for a in range(4):
        for b in range(4):
            for c in range(4):
                assert sp.simplify(K(a, b, c) + K(b, a, c)) == 0

    # Torsion reconstruction: T_{abc} = K_{acb} - K_{abc}.
    for a in range(4):
        for b in range(4):
            for c in range(4):
                assert sp.simplify(T(a, b, c) - (K(a, c, b) - K(a, b, c))) == 0


def test_uniqueness_rank():
    # Unknown K_mu^{ab} with a<b: 4*6 = 24 Lorentz-valued components.
    pairs = [(a, b) for a in range(4) for b in range(a + 1, 4)]
    variables = sp.symbols("k0:24")
    idx = {(mu, a, b): 6 * mu + pairs.index((a, b)) for mu in range(4) for a, b in pairs}

    def K(mu, a, b):
        if a == b:
            return sp.S.Zero
        if a < b:
            return variables[idx[(mu, a, b)]]
        return -variables[idx[(mu, b, a)]]

    # At e_nu^b = delta_nu^b, equality of torsions gives
    # K_mu^a_nu - K_nu^a_mu = 0 for each a and mu<nu.
    equations = []
    for a in range(4):
        for mu in range(4):
            for nu in range(mu + 1, 4):
                equations.append(K(mu, a, nu) - K(nu, a, mu))
    A, _ = sp.linear_eq_to_matrix(equations, variables)
    assert A.shape == (24, 24)
    assert A.rank() == 24


if __name__ == "__main__":
    test_minkowski()
    test_flat_polar_frame()
    test_uniqueness_rank()
    test_contorsion_reconstruction()
    print("GAP-10OMEGA CONNECTION CHECK: ALL CHECKS PASSED")
    print("  Minkowski Cartesian frame: Gamma = omega = 0")
    print("  Flat polar frame: omega != 0 but curvature = 0")
    print("  torsion-free Lorentz connection uniqueness system: rank 24/24")
    print("  arbitrary torsion: exact contorsion reconstruction verified")
    print("  NOT TESTED: torsion dynamics or Theta integrability")
