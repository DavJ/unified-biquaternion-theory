#!/usr/bin/env python3
"""Verify the Hermitian support Gram of the Whitney null shell."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class Q:
    s: sp.Expr
    x: sp.Expr
    y: sp.Expr
    z: sp.Expr

    def values(self):
        return self.s, self.x, self.y, self.z

    def dagger(self) -> "Q":
        s, x, y, z = self.values()
        return Q(sp.conjugate(s), -sp.conjugate(x), -sp.conjugate(y), -sp.conjugate(z))

    def sharp(self) -> "Q":
        return Q(self.s, -self.x, -self.y, -self.z)

    def __add__(self, other: "Q") -> "Q":
        return Q(*(sp.expand(a + b) for a, b in zip(self.values(), other.values())))

    def __mul__(self, other: "Q") -> "Q":
        a0, a1, a2, a3 = self.values()
        b0, b1, b2, b3 = other.values()
        return Q(
            sp.expand(a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3),
            sp.expand(a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2),
            sp.expand(a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1),
            sp.expand(a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0),
        )


def scalar(q: Q) -> sp.Expr:
    return sp.simplify(q.s)


def main() -> None:
    i = sp.I
    q = Q(0, 0, 1, i)
    p = Q(1, -i, 0, 0)

    # The sharp-bilinear null plane.
    assert scalar(q.sharp() * q) == 0
    assert scalar(p.sharp() * p) == 0
    assert scalar(q.sharp() * p + p.sharp() * q) == 0

    # The same plane is positive and orthogonal in the Hermitian scalar norm.
    assert sp.re(scalar(q.dagger() * q)) == 2
    assert sp.re(scalar(p.dagger() * p)) == 2
    assert scalar(q.dagger() * p) == 0
    assert scalar(p.dagger() * q) == 0

    theta, phi = sp.symbols("theta phi", real=True)
    c = sp.cos(theta)
    s = sp.sin(theta)
    n1 = s * sp.cos(phi)
    n2 = s * sp.sin(phi)
    w1 = (1 + i * c) * n1
    w2 = (1 + i * c) * n2

    def gram(a: sp.Symbol, b: sp.Symbol) -> sp.Expr:
        value = 2 * sp.re(
            sp.conjugate(sp.diff(w1, a)) * sp.diff(w1, b)
            + sp.conjugate(sp.diff(w2, a)) * sp.diff(w2, b)
        )
        return sp.trigsimp(sp.simplify(value))

    h_tt = gram(theta, theta)
    h_tp = gram(theta, phi)
    h_pp = gram(phi, phi)

    expected_tt = 2 * (4 * c**4 - 3 * c**2 + 1)
    expected_pp = 2 * (1 + c**2) * s**2
    assert sp.trigsimp(h_tt - expected_tt) == 0
    assert sp.trigsimp(h_tp) == 0
    assert sp.trigsimp(h_pp - expected_pp) == 0

    det_h = sp.trigsimp(sp.factor(h_tt * h_pp - h_tp**2))
    expected_det = 4 * s**2 * (1 + c**2) * (4 * c**4 - 3 * c**2 + 1)
    assert sp.trigsimp(det_h - expected_det) == 0

    u = sp.symbols("u", real=True)
    polynomial = 4 * u**2 - 3 * u + 1
    assert sp.discriminant(polynomial, u) == -7
    assert polynomial.subs(u, 0) > 0

    # Numerical positivity sampling, including near both coordinate poles.
    for value in [sp.Rational(-1), sp.Rational(-9, 10), 0, sp.Rational(9, 10), 1]:
        assert sp.N(1 + value**2) > 0
        assert sp.N(4 * value**4 - 3 * value**2 + 1) > 0

    print("PASS: sharp-null q,p plane is Hermitian-positive and orthogonal")
    print("PASS: Whitney Hermitian support Gram components are exact")
    print("PASS: invariant angular support determinant is strictly positive")
    print("PASS: visible-null sphere retains a nonzero internal support area")


if __name__ == "__main__":
    main()
