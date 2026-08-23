#!/usr/bin/env python3
"""Independent exact spot checks for the Theta-potential invariant basis.

This checker uses only Python's standard-library Fraction type and a separate
matrix implementation.  It checks finite nonunitary SL(2,C) transformations
and a rational U(1) phase.  It does not establish completeness of the basis;
that is the job of verify_theta_potential_invariants.py.
"""

from __future__ import annotations

from fractions import Fraction as F


ComplexQ = tuple[F, F]
Matrix2 = tuple[tuple[ComplexQ, ComplexQ], tuple[ComplexQ, ComplexQ]]

ZERO: ComplexQ = (F(0), F(0))
ONE: ComplexQ = (F(1), F(0))


def add(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return a[0] + b[0], a[1] + b[1]


def neg(a: ComplexQ) -> ComplexQ:
    return -a[0], -a[1]


def sub(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return add(a, neg(b))


def mul(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def conjugate(a: ComplexQ) -> ComplexQ:
    return a[0], -a[1]


def matmul(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(
        tuple(add(mul(a[i][0], b[0][j]), mul(a[i][1], b[1][j])) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def dagger(a: Matrix2) -> Matrix2:
    return tuple(tuple(conjugate(a[j][i]) for j in range(2)) for i in range(2))  # type: ignore[return-value]


def scale(u: ComplexQ, a: Matrix2) -> Matrix2:
    return tuple(tuple(mul(u, a[i][j]) for j in range(2)) for i in range(2))  # type: ignore[return-value]


def determinant(a: Matrix2) -> ComplexQ:
    return sub(mul(a[0][0], a[1][1]), mul(a[0][1], a[1][0]))


def sharp(a: Matrix2) -> Matrix2:
    return ((a[1][1], neg(a[0][1])), (neg(a[1][0]), a[0][0]))


def trace(a: Matrix2) -> ComplexQ:
    return add(a[0][0], a[1][1])


def norm_squared(a: ComplexQ) -> F:
    return a[0] ** 2 + a[1] ** 2


def h_invariant(a: Matrix2) -> F:
    value = trace(matmul(sharp(a), dagger(a)))
    assert value[1] == 0
    return value[0]


def determinant_norm(a: Matrix2) -> F:
    return norm_squared(determinant(a))


def hilbert_schmidt(a: Matrix2) -> F:
    value = trace(matmul(dagger(a), a))
    assert value[1] == 0
    return value[0]


def transformed(s: Matrix2, u: ComplexQ, x: Matrix2) -> Matrix2:
    return scale(u, matmul(matmul(s, x), dagger(s)))


def main() -> None:
    representatives: list[Matrix2] = [
        (((F(2), F(0)), ZERO), (ZERO, (F(1, 2), F(0)))),
        ((((F(1), F(1))), ONE), (((F(0), F(1))), ONE)),
    ]
    fields: list[Matrix2] = [
        ((ONE, ZERO), (ZERO, ONE)),
        ((((F(1, 3), F(2, 5))), ((F(-2), F(1)))), (((F(3, 2), F(-1, 4))), ((F(5, 3), F(7, 6))))),
        ((ZERO, ONE), (ZERO, ZERO)),
    ]
    phase: ComplexQ = (F(3, 5), F(4, 5))
    assert norm_squared(phase) == 1

    for s in representatives:
        assert determinant(s) == ONE
        for x in fields:
            image = transformed(s, phase, x)
            assert h_invariant(image) == h_invariant(x)
            assert determinant_norm(image) == determinant_norm(x)

    identity = fields[0]
    boost = representatives[0]
    boosted_identity = transformed(boost, ONE, identity)
    assert hilbert_schmidt(identity) == 2
    assert hilbert_schmidt(boosted_identity) == F(257, 16)

    print("PASS: independent Fraction checks preserve H and |det X|^2")
    print("PASS: nonunitary boost changes Tr(X^dagger X) from 2 to 257/16")
    print("NOT TESTED: completeness/uniqueness of the invariant basis")


if __name__ == "__main__":
    main()
