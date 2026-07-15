#!/usr/bin/env python3
"""Exact checks for the partial GAP-10I closure.

Verifies:
1. The affine Minkowski Theta representer gives the canonical Lorentz tetrad
   and has vanishing second derivatives.
2. Right multiplication by an invertible biquaternion/matrix is injective,
   which is the algebraic core of the one-sided flatness obstruction.
3. A polynomial 2x2-matrix example satisfies the exact two-sided curvature
   identity [D_mu,D_nu]Theta = F^A_mu_nu Theta - Theta F^B_mu_nu.

This does NOT prove curved-space existence, uniqueness, global continuation,
or derivation of the left/right connections from the UBT action.
"""
from __future__ import annotations

import sympy as sp


def qmul(a: tuple[sp.Expr, sp.Matrix], b: tuple[sp.Expr, sp.Matrix]):
    s, u = a
    t, v = b
    return sp.expand(s * t - u.dot(v)), sp.simplify(s * v + t * u + u.cross(v))


def qsharp(a: tuple[sp.Expr, sp.Matrix]):
    s, u = a
    return s, -u


def minkowski_affine_representer_check() -> None:
    x = sp.symbols("x0:4", real=True)
    n0 = sp.symbols("N0", positive=True)
    # Theta = sqrt(N0) * (i x0, (x1,x2,x3)) + constant.
    theta_scalar = sp.sqrt(n0) * sp.I * x[0]
    theta_vec = sp.sqrt(n0) * sp.Matrix(x[1:4])
    E = []
    for mu in range(4):
        E.append(
            (
                sp.simplify(sp.diff(theta_scalar, x[mu]) / sp.sqrt(n0)),
                sp.simplify(theta_vec.diff(x[mu]) / sp.sqrt(n0)),
            )
        )

    eta = sp.diag(-1, 1, 1, 1)
    g = sp.zeros(4)
    for mu in range(4):
        for nu in range(4):
            a = qmul(qsharp(E[mu]), E[nu])
            b = qmul(qsharp(E[nu]), E[mu])
            scalar = sp.simplify((a[0] + b[0]) / 2)
            vector = sp.simplify((a[1] + b[1]) / 2)
            assert vector == sp.zeros(3, 1)
            g[mu, nu] = scalar
    assert g == eta

    for mu in range(4):
        for nu in range(4):
            assert sp.diff(theta_scalar, x[mu], x[nu]) == 0
            assert theta_vec.diff(x[mu], x[nu]) == sp.zeros(3, 1)


def one_sided_injectivity_check() -> None:
    # Biquaternions are represented faithfully by 2x2 complex matrices.
    # For invertible Theta, F -> F Theta must be injective.
    theta = sp.Matrix([[1, 2], [3, 5]])  # det = -1
    f00, f01, f10, f11 = sp.symbols("f00 f01 f10 f11")
    F = sp.Matrix([[f00, f01], [f10, f11]])
    equations = list(F * theta)
    A, _ = sp.linear_eq_to_matrix(equations, [f00, f01, f10, f11])
    assert theta.det() != 0
    assert A.rank() == 4


def matrix_simplify(M: sp.Matrix) -> sp.Matrix:
    return M.applyfunc(sp.simplify)


def two_sided_curvature_check() -> None:
    x, y = sp.symbols("x y", real=True)
    theta = sp.Matrix([[1 + x, y], [x * y, 2 - x + y]])
    A0 = sp.Matrix([[x, 1], [y, -x]])
    A1 = sp.Matrix([[0, x], [1 + y, y]])
    B0 = sp.Matrix([[y, x], [0, -y]])
    B1 = sp.Matrix([[x * y, 1], [x, -x * y]])

    variables = [x, y]
    As = [A0, A1]
    Bs = [B0, B1]

    def D(mu: int, X: sp.Matrix) -> sp.Matrix:
        return matrix_simplify(X.diff(variables[mu]) + As[mu] * X - X * Bs[mu])

    comm = matrix_simplify(D(0, D(1, theta)) - D(1, D(0, theta)))
    FA = matrix_simplify(A1.diff(x) - A0.diff(y) + A0 * A1 - A1 * A0)
    FB = matrix_simplify(B1.diff(x) - B0.diff(y) + B0 * B1 - B1 * B0)
    expected = matrix_simplify(FA * theta - theta * FB)
    assert matrix_simplify(comm - expected) == sp.zeros(2)


def main() -> None:
    minkowski_affine_representer_check()
    one_sided_injectivity_check()
    two_sided_curvature_check()
    print("GAP-10I INTEGRABILITY CHECK: ALL CHECKS PASSED")
    print("  affine Theta representer: Minkowski metric and zero second derivatives")
    print("  one-sided obstruction: F Theta = 0 with invertible Theta implies F = 0")
    print("  two-sided derivative: exact left/right curvature identity verified")
    print("  NOT TESTED: curved-space existence, uniqueness, action, or global closure")


if __name__ == "__main__":
    main()
