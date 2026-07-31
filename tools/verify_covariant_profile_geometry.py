#!/usr/bin/env python3
"""Exact algebra checks for the covariant free-profile geometry candidate.

This verifier checks only finite-dimensional algebraic statements:

* the sharp-symmetrised product of two arbitrary biquaternions is central;
* its coefficient is generally complex and becomes Lorentz-real on W_L;
* the sharp-antisymmetric part is quaternion-vector valued and antisymmetric;
* an ambient Lorentz/Krein infinitesimal frame transformation preserves the
  profile Gram matrix to first order.

It does not prove the analytic free-embedding theorem, flat-bundle existence,
or the master-action origin of the candidate branch.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class Quaternion:
    scalar: sp.Expr
    vector: sp.Matrix

    def sharp(self) -> "Quaternion":
        return Quaternion(self.scalar, -self.vector)


def qmul(left: Quaternion, right: Quaternion) -> Quaternion:
    scalar = sp.expand(left.scalar * right.scalar - left.vector.dot(right.vector))
    vector = sp.simplify(
        left.scalar * right.vector
        + right.scalar * left.vector
        + left.vector.cross(right.vector)
    )
    return Quaternion(scalar, vector)


def qadd(left: Quaternion, right: Quaternion) -> Quaternion:
    return Quaternion(
        sp.expand(left.scalar + right.scalar),
        sp.simplify(left.vector + right.vector),
    )


def qsub(left: Quaternion, right: Quaternion) -> Quaternion:
    return Quaternion(
        sp.expand(left.scalar - right.scalar),
        sp.simplify(left.vector - right.vector),
    )


def qscale(value: sp.Expr, q: Quaternion) -> Quaternion:
    return Quaternion(sp.expand(value * q.scalar), sp.simplify(value * q.vector))


def centrality_check() -> tuple[sp.Expr, sp.Matrix, sp.Matrix]:
    z = sp.symbols("z0:4")
    w = sp.symbols("w0:4")
    q = Quaternion(z[0], sp.Matrix(z[1:]))
    r = Quaternion(w[0], sp.Matrix(w[1:]))

    qsr = qmul(q.sharp(), r)
    rsq = qmul(r.sharp(), q)
    symmetric = qscale(sp.Rational(1, 2), qadd(qsr, rsq))
    antisymmetric = qscale(sp.Rational(1, 2), qsub(qsr, rsq))

    expected = sp.expand(sum(z[index] * w[index] for index in range(4)))
    assert sp.simplify(symmetric.scalar - expected) == 0
    assert symmetric.vector == sp.zeros(3, 1)

    expected_antisymmetric = sp.Matrix(
        [
            z[0] * w[1] - w[0] * z[1] - (z[2] * w[3] - z[3] * w[2]),
            z[0] * w[2] - w[0] * z[2] - (z[3] * w[1] - z[1] * w[3]),
            z[0] * w[3] - w[0] * z[3] - (z[1] * w[2] - z[2] * w[1]),
        ]
    )
    assert sp.simplify(antisymmetric.vector - expected_antisymmetric) == sp.zeros(3, 1)
    return symmetric.scalar, symmetric.vector, antisymmetric.vector


def lorentz_slice_check() -> sp.Expr:
    x = sp.symbols("x0:4", real=True)
    y = sp.symbols("y0:4", real=True)
    q = Quaternion(sp.I * x[0], sp.Matrix(x[1:]))
    r = Quaternion(sp.I * y[0], sp.Matrix(y[1:]))
    symmetric = qscale(
        sp.Rational(1, 2),
        qadd(qmul(q.sharp(), r), qmul(r.sharp(), q)),
    )
    expected = -x[0] * y[0] + sum(x[index] * y[index] for index in range(1, 4))
    assert sp.simplify(symmetric.scalar - expected) == 0
    assert symmetric.vector == sp.zeros(3, 1)
    return symmetric.scalar


def ambient_frame_check() -> sp.Matrix:
    """Check an infinitesimal O(13,1) boost preserves the Gram form."""
    eta = sp.diag(-1, *([1] * 13))
    a = sp.symbols("a", real=True)
    generator = sp.zeros(14, 14)
    generator[0, 1] = a
    generator[1, 0] = a
    compatibility = sp.simplify(generator.T * eta + eta * generator)
    assert compatibility == sp.zeros(14, 14)
    return compatibility


def run_checks() -> None:
    scalar, vector, antisymmetric = centrality_check()
    lorentz = lorentz_slice_check()
    compatibility = ambient_frame_check()

    print("PASS: sharp-symmetrised product is central for arbitrary biquaternions.")
    print(f"PASS: central coefficient is the complex bilinear {scalar}.")
    print(f"PASS: symmetric quaternion-vector part vanishes: {list(vector)}.")
    print(f"PASS: antisymmetric channel retains quaternion-vector data: {list(antisymmetric)}.")
    print(f"PASS: W_L restriction gives Lorentz-real coefficient {lorentz}.")
    print(f"PASS: sample ambient boost is pairing-compatible: rank={compatibility.rank()}.")
    print("NOT TESTED: analytic free-embedding existence or master-action origin.")


if __name__ == "__main__":
    run_checks()
