#!/usr/bin/env python3
"""Exact checks for the GAP-10I paired-connection audit.

Verifies:
1. Lorentz-slice preservation forces B=-A^dagger+cI with real c.
2. Metric compatibility removes the real dilation and the common central
   one-form cancels, leaving D X = dX + Omega X + X Omega^dagger.
3. The paired derivative commutes with J(X)=-X^dagger.
4. A proper homothety is incompatible with Schwarzschild f=1-2M/r, M != 0.

This verifier is intentionally restricted to the torsion-free branch.  A
separate exact verifier constructs a local composite-contortion representer;
neither verifier closes the canonical action/Einstein bridge.
"""
from __future__ import annotations

import sympy as sp


def msimplify(m: sp.Matrix) -> sp.Matrix:
    return m.applyfunc(sp.simplify)


def slice_preservation_check() -> None:
    # Necessity: P=A+B^dagger must be a real scalar.  The X=iI equation makes
    # P Hermitian; commutation with the three anti-Hermitian Pauli directions
    # then removes every traceless Hermitian component.
    p0, p1, p2, p3 = sp.symbols("p0:4", real=True)
    sigma1 = sp.Matrix([[0, 1], [1, 0]])
    sigma2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sigma3 = sp.Matrix([[1, 0], [0, -1]])
    P = p0 * sp.eye(2) + p1 * sigma1 + p2 * sigma2 + p3 * sigma3
    equations = []
    for Xbasis in (sp.I * sigma1, sp.I * sigma2, sp.I * sigma3):
        equations.extend(list(msimplify(P * Xbasis - Xbasis * P)))
    sol = sp.solve(equations, (p1, p2, p3), dict=True)
    assert sol == [{p1: 0, p2: 0, p3: 0}]

    # Sufficiency for generic complex A and anti-Hermitian X.
    ar = sp.symbols("ar0:4", real=True)
    ai = sp.symbols("ai0:4", real=True)
    xr = sp.symbols("xr0:4", real=True)
    c = sp.symbols("c", real=True)

    A = sp.Matrix(
        [
            [ar[0] + sp.I * ai[0], ar[1] + sp.I * ai[1]],
            [ar[2] + sp.I * ai[2], ar[3] + sp.I * ai[3]],
        ]
    )
    # General anti-Hermitian 2x2 matrix.
    X = sp.Matrix(
        [
            [sp.I * xr[0], xr[1] + sp.I * xr[2]],
            [-xr[1] + sp.I * xr[2], sp.I * xr[3]],
        ]
    )
    assert msimplify(X.conjugate().T + X) == sp.zeros(2)

    B = -A.conjugate().T + c * sp.eye(2)
    C = msimplify(A * X - X * B)
    assert msimplify(C.conjugate().T + C) == sp.zeros(2)


def central_cancellation_and_J_check() -> None:
    # Generic traceless Omega, generic complex central alpha.
    wr = sp.symbols("wr0:3", real=True)
    wi = sp.symbols("wi0:3", real=True)
    alpha_r, alpha_i = sp.symbols("alpha_r alpha_i", real=True)
    alpha = alpha_r + sp.I * alpha_i
    Omega = sp.Matrix(
        [
            [wr[0] + sp.I * wi[0], wr[1] + sp.I * wi[1]],
            [wr[2] + sp.I * wi[2], -wr[0] - sp.I * wi[0]],
        ]
    )
    x = sp.Matrix(2, 2, sp.symbols("x0:4"))

    A = Omega + alpha * sp.eye(2)
    B = -Omega.conjugate().T + alpha * sp.eye(2)
    paired = msimplify(A * x - x * B)
    expected = msimplify(Omega * x + x * Omega.conjugate().T)
    assert msimplify(paired - expected) == sp.zeros(2)

    # A residual real scalar lambda would dilate the quadratic form at rate
    # 2 lambda, so metric compatibility requires lambda=0.
    lam = sp.symbols("lambda", real=True)
    u = sp.Matrix(2, 2, sp.symbols("u0:4"))
    v = sp.Matrix(2, 2, sp.symbols("v0:4"))
    bilinear_rate = sp.expand(
        sp.trace((lam * u).conjugate().T * v + u.conjugate().T * (lam * v))
    )
    baseline = sp.expand(sp.trace(u.conjugate().T * v))
    assert sp.simplify(bilinear_rate - 2 * lam * baseline) == 0

    # J(X)=-X^dagger commutes with the paired connection action.
    J_paired = -paired.conjugate().T
    Jx = -x.conjugate().T
    paired_Jx = msimplify(Omega * Jx + Jx * Omega.conjugate().T)
    assert msimplify(J_paired - paired_Jx) == sp.zeros(2)


def schwarzschild_homothety_no_go_check() -> None:
    r, M = sp.symbols("r M", positive=True)
    f = 1 - 2 * M / r

    # Angular homothety equation forces R=r.  The rr equation then has
    # residual -r f'/f^2, which must vanish but does not for M != 0.
    residual_rr = sp.simplify(-r * sp.diff(f, r) / f**2)
    assert sp.simplify(residual_rr + 2 * M / (r * f**2)) == 0
    assert residual_rr != 0


def main() -> None:
    slice_preservation_check()
    central_cancellation_and_J_check()
    schwarzschild_homothety_no_go_check()
    print("GAP-10I PAIRED-CONNECTION AUDIT: ALL CHECKS PASSED")
    print("  Lorentz slice: preservation iff B=-A^dagger+cI, c real")
    print("  metric-compatible action: central term cancels; one Omega remains")
    print("  paired derivative: J-equivariant")
    print("  Schwarzschild M!=0: torsion-free homothety/concurrent branch excluded")
    print("  NOT TESTED: composite torsion branch, action selection, or full GAP-10D closure")


if __name__ == "__main__":
    main()
