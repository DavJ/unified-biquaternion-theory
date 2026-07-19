#!/usr/bin/env python3
"""Exact checks for the GAP-10I torsionful local-representer theorem.

Verifies:
1. The composite K_{nu mu rho} is antisymmetric in its metric indices.
2. K^nu_{mu rho} V^rho = W_mu^nu when W_{mu nu} V^nu = 0.
3. On an explicit curved Lorentzian warped metric with a Gaussian coordinate,
   Gamma=Gamma_LC+K satisfies nabla^Gamma_mu V^nu=delta_mu^nu exactly.
4. On a Schwarzschild exterior patch, proper radial distance obeys the needed
   eikonal/norm-gradient identities.

This verifier does NOT prove canonical action selection, physical
non-propagation after variation, global continuation, horizon regularity, or
Einstein dynamics.
"""
from __future__ import annotations

import sympy as sp


def christoffel(g: sp.Matrix, coords: tuple[sp.Symbol, ...]):
    """Return Levi-Civita Christoffel symbols Gamma^a_{mn}."""
    dim = len(coords)
    g_inv = sp.simplify(g.inv())
    gamma = [
        [[sp.S.Zero for _ in range(dim)] for _ in range(dim)]
        for _ in range(dim)
    ]
    for a in range(dim):
        for mu in range(dim):
            for nu in range(dim):
                gamma[a][mu][nu] = sp.simplify(
                    sp.Rational(1, 2)
                    * sum(
                        g_inv[a, b]
                        * (
                            sp.diff(g[b, nu], coords[mu])
                            + sp.diff(g[b, mu], coords[nu])
                            - sp.diff(g[mu, nu], coords[b])
                        )
                        for b in range(dim)
                    )
                )
    return gamma


def abstract_algebra_check() -> None:
    """Check the K algebra with exact rational data in four dimensions."""
    dim = 4
    g = sp.diag(-2, 3, 5, 7)
    g_inv = g.inv()
    V = sp.Matrix([1, 2, -1, 3])
    V_cov = g * V
    V2 = sp.simplify((V.T * g * V)[0])
    assert V2 != 0

    # Build an exact W whose second index is orthogonal to V.
    raw = sp.Matrix(
        [
            [1, 2, 0, -1],
            [0, 1, 3, 2],
            [2, -2, 1, 0],
            [1, 0, -1, 4],
        ]
    )
    n_cov = V_cov / V2  # n_nu V^nu = 1
    W = sp.MutableDenseMatrix(dim, dim, [0] * (dim * dim))
    for mu in range(dim):
        residual = sp.simplify(sum(raw[mu, nu] * V[nu] for nu in range(dim)))
        for nu in range(dim):
            W[mu, nu] = sp.simplify(raw[mu, nu] - residual * n_cov[nu])
    assert all(
        sp.simplify(sum(W[mu, nu] * V[nu] for nu in range(dim))) == 0
        for mu in range(dim)
    )

    K = [
        [[sp.S.Zero for _ in range(dim)] for _ in range(dim)]
        for _ in range(dim)
    ]
    for nu in range(dim):
        for mu in range(dim):
            for rho in range(dim):
                K[nu][mu][rho] = sp.simplify(
                    (W[mu, nu] * V_cov[rho] - V_cov[nu] * W[mu, rho]) / V2
                )

    for nu in range(dim):
        for mu in range(dim):
            for rho in range(dim):
                assert sp.simplify(K[nu][mu][rho] + K[rho][mu][nu]) == 0

    for mu in range(dim):
        for nu in range(dim):
            contracted = sp.simplify(
                sum(
                    g_inv[nu, a] * K[a][mu][rho] * V[rho]
                    for a in range(dim)
                    for rho in range(dim)
                )
            )
            target = sp.simplify(
                sum(g_inv[nu, a] * W[mu, a] for a in range(dim))
            )
            assert sp.simplify(contracted - target) == 0


def curved_warped_metric_check() -> None:
    """Verify the full construction on a non-flat Lorentzian metric."""
    t, x, y, z = sp.symbols("t x y z", real=True)
    c = sp.symbols("c", real=True, nonzero=True)
    coords = (t, x, y, z)
    dim = 4

    # x is a spacelike Gaussian coordinate; the y-z warp makes curvature
    # nonzero while preserving g^{xx}=1.
    g = sp.diag(-1, 1, sp.exp(2 * x), sp.exp(2 * x))
    g_inv = sp.simplify(g.inv())
    gamma = christoffel(g, coords)

    rho = x + c
    V = sp.Matrix([0, rho, 0, 0])
    V_cov = sp.simplify(g * V)
    V2 = sp.simplify((V.T * g * V)[0])
    assert sp.simplify(V2 - rho**2) == 0
    assert all(
        sp.simplify(V_cov[mu] - sp.diff(V2, coords[mu]) / 2) == 0
        for mu in range(dim)
    )

    nabla_lc_cov = sp.MutableDenseMatrix(dim, dim, [0] * (dim * dim))
    nabla_lc_contra = sp.MutableDenseMatrix(dim, dim, [0] * (dim * dim))
    for mu in range(dim):
        for nu in range(dim):
            nabla_lc_cov[mu, nu] = sp.simplify(
                sp.diff(V_cov[nu], coords[mu])
                - sum(gamma[a][mu][nu] * V_cov[a] for a in range(dim))
            )
            nabla_lc_contra[mu, nu] = sp.simplify(
                sp.diff(V[nu], coords[mu])
                + sum(gamma[nu][mu][rho_idx] * V[rho_idx] for rho_idx in range(dim))
            )

    W = sp.MutableDenseMatrix(dim, dim, [0] * (dim * dim))
    for mu in range(dim):
        for nu in range(dim):
            W[mu, nu] = sp.simplify(g[mu, nu] - nabla_lc_cov[mu, nu])
    assert all(
        sp.simplify(sum(W[mu, nu] * V[nu] for nu in range(dim))) == 0
        for mu in range(dim)
    )

    K = [
        [[sp.S.Zero for _ in range(dim)] for _ in range(dim)]
        for _ in range(dim)
    ]
    for nu in range(dim):
        for mu in range(dim):
            for rho_idx in range(dim):
                K[nu][mu][rho_idx] = sp.simplify(
                    (
                        W[mu, nu] * V_cov[rho_idx]
                        - V_cov[nu] * W[mu, rho_idx]
                    )
                    / V2
                )

    for mu in range(dim):
        for nu in range(dim):
            kv = sp.simplify(
                sum(
                    g_inv[nu, a] * K[a][mu][rho_idx] * V[rho_idx]
                    for a in range(dim)
                    for rho_idx in range(dim)
                )
            )
            expected = sp.S.One if mu == nu else sp.S.Zero
            assert sp.simplify(nabla_lc_contra[mu, nu] + kv - expected) == 0

    # Confirm the test background is genuinely curved: R^y_{x y x}=-1.
    # Compute this one component directly from the Christoffels.
    a, b, mu, nu = 2, 1, 2, 1  # R^y_{x y x}
    riemann = sp.simplify(
        sp.diff(gamma[a][b][nu], coords[mu])
        - sp.diff(gamma[a][b][mu], coords[nu])
        + sum(
            gamma[a][mu][lam] * gamma[lam][b][nu]
            - gamma[a][nu][lam] * gamma[lam][b][mu]
            for lam in range(dim)
        )
    )
    assert riemann != 0


def schwarzschild_exterior_check() -> None:
    """Check the Gaussian radial identities on r>2M."""
    r, M, rho = sp.symbols("r M rho", positive=True)
    f = 1 - 2 * M / r
    rho_prime = 1 / sp.sqrt(f)

    # V^r = rho sqrt(f), g_rr=1/f.
    V_r = sp.simplify((1 / f) * rho * sp.sqrt(f))
    half_norm_derivative = sp.simplify(rho * rho_prime)
    assert sp.simplify(V_r - half_norm_derivative) == 0

    norm = sp.simplify((1 / f) * (rho * sp.sqrt(f)) ** 2)
    assert sp.simplify(norm - rho**2) == 0


def main() -> None:
    abstract_algebra_check()
    curved_warped_metric_check()
    schwarzschild_exterior_check()
    print("GAP-10I TORSIONFUL LOCAL REPRESENTER: ALL CHECKS PASSED")
    print("  composite K: metric-compatible antisymmetry")
    print("  composite K: exact contraction K(V)=W")
    print("  curved warped metric: nabla^(LC+K)_mu V^nu = delta_mu^nu")
    print("  Schwarzschild exterior: proper-radial Gaussian identities")
    print("  NOT TESTED: action selection, physical torsion bounds, or global extension")


if __name__ == "__main__":
    main()
