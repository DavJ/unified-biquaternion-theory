#!/usr/bin/env python3
"""Verify the metric-free polynomial-action exactness identity.

The check uses a nontrivial affine biquaternionic field for which K wedge K is
nonzero.  It verifies that K=d(Theta^sharp dTheta), dK=0, and
K wedge K=d[(Theta^sharp dTheta) wedge K].  It also checks the product-rule
remainder for a nonconstant central weight Xi.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Dict, Tuple

import sympy as sp


@dataclass(frozen=True)
class Q:
    s: sp.Expr
    x: sp.Expr
    y: sp.Expr
    z: sp.Expr

    def values(self) -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
        return self.s, self.x, self.y, self.z

    def __add__(self, other: "Q") -> "Q":
        return Q(*(sp.expand(a + b) for a, b in zip(self.values(), other.values())))

    def __neg__(self) -> "Q":
        return Q(*(-a for a in self.values()))

    def __sub__(self, other: "Q") -> "Q":
        return self + (-other)

    def scale(self, c: sp.Expr) -> "Q":
        return Q(*(sp.expand(c * a) for a in self.values()))

    def sharp(self) -> "Q":
        return Q(self.s, -self.x, -self.y, -self.z)

    def __mul__(self, other: "Q") -> "Q":
        a0, a1, a2, a3 = self.values()
        b0, b1, b2, b3 = other.values()
        return Q(
            sp.expand(a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3),
            sp.expand(a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2),
            sp.expand(a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1),
            sp.expand(a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0),
        )

    def simplify(self) -> "Q":
        return Q(*(sp.simplify(a) for a in self.values()))

    def is_zero(self) -> bool:
        return all(sp.simplify(a) == 0 for a in self.values())


ZERO = Q(sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(0))
Form = Dict[Tuple[int, ...], Q]


def permutation_sign(values: tuple[int, ...]) -> int:
    inversions = sum(
        1
        for i in range(len(values))
        for j in range(i + 1, len(values))
        if values[i] > values[j]
    )
    return -1 if inversions % 2 else 1


def add_forms(left: Form, right: Form) -> Form:
    result: Form = dict(left)
    for key, value in right.items():
        result[key] = (result.get(key, ZERO) + value).simplify()
        if result[key].is_zero():
            del result[key]
    return result


def scale_form(form: Form, scalar: sp.Expr) -> Form:
    return {
        key: value.scale(scalar).simplify()
        for key, value in form.items()
        if not value.scale(scalar).simplify().is_zero()
    }


def wedge(left: Form, right: Form) -> Form:
    result: Form = {}
    for left_key, left_value in left.items():
        for right_key, right_value in right.items():
            if set(left_key).intersection(right_key):
                continue
            joined = left_key + right_key
            ordered = tuple(sorted(joined))
            sign = permutation_sign(joined)
            term = (left_value * right_value).scale(sign).simplify()
            result[ordered] = (result.get(ordered, ZERO) + term).simplify()
            if result[ordered].is_zero():
                del result[ordered]
    return result


def exterior_derivative(form: Form, coordinates: tuple[sp.Symbol, ...]) -> Form:
    result: Form = {}
    for key, value in form.items():
        for index, coordinate in enumerate(coordinates):
            if index in key:
                continue
            derivative = Q(*(sp.diff(component, coordinate) for component in value.values()))
            if derivative.is_zero():
                continue
            result = add_forms(result, wedge({(index,): Q(1, 0, 0, 0)}, {key: derivative}))
    return result


def multiply_zero_form(value: Q, form: Form) -> Form:
    return {key: (value * coefficient).simplify() for key, coefficient in form.items()}


def sharp_form(form: Form) -> Form:
    return {key: value.sharp() for key, value in form.items()}


def main() -> None:
    t, x, y, z = sp.symbols("t x y z", real=True)
    coordinates = (t, x, y, z)

    theta = Q(t, x, y, z)
    dtheta: Form = {
        (0,): Q(1, 0, 0, 0),
        (1,): Q(0, 1, 0, 0),
        (2,): Q(0, 0, 1, 0),
        (3,): Q(0, 0, 0, 1),
    }

    alpha = multiply_zero_form(theta.sharp(), dtheta)
    k_from_alpha = exterior_derivative(alpha, coordinates)
    k_direct = wedge(sharp_form(dtheta), dtheta)
    assert k_from_alpha == k_direct
    assert exterior_derivative(k_direct, coordinates) == {}

    k_squared = wedge(k_direct, k_direct)
    assert (0, 1, 2, 3) in k_squared
    assert k_squared[(0, 1, 2, 3)].simplify() == Q(24, 0, 0, 0)

    boundary_current = wedge(alpha, k_direct)
    assert exterior_derivative(boundary_current, coordinates) == k_squared

    # Nonconstant central weight Xi=t: Xi K^2 differs from a boundary term by
    # the explicit bulk product dXi wedge alpha wedge K.
    xi = t
    xi_k_squared = scale_form(k_squared, xi)
    xi_boundary = scale_form(boundary_current, xi)
    d_xi_boundary = exterior_derivative(xi_boundary, coordinates)
    d_xi: Form = {(0,): Q(1, 0, 0, 0)}
    bulk_remainder = wedge(d_xi, boundary_current)
    reconstructed = add_forms(d_xi_boundary, scale_form(bulk_remainder, -1))
    assert reconstructed == xi_k_squared
    assert bulk_remainder != {}

    print("PASS: K_Theta = d(Theta^sharp dTheta)")
    print("PASS: d K_Theta = 0")
    print("PASS: K_Theta wedge K_Theta is an exact nonzero four-form")
    print("PASS: constant sharp-quartic action has no bulk selection equation")
    print("PASS: nonconstant central weighting creates an explicit bulk remainder")


if __name__ == "__main__":
    main()
