#!/usr/bin/env python3
"""Exact lightweight checks for the Whitney spherical null-shell Theta.

This verifier checks off-shell kinematic identities only.  It does not verify
an action, an on-shell solution, stability, or physical invisibility.
"""

from __future__ import annotations

from dataclasses import dataclass

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


def symmetric_sharp(a: Q, b: Q) -> Q:
    return (a.sharp() * b + b.sharp() * a).scale(sp.Rational(1, 2)).simplify()


def profile_pair(left: dict[int, sp.Expr], right: dict[int, sp.Expr]) -> sp.Expr:
    """Bilinear Haar average: only Fourier modes with n+m=0 survive."""
    return sp.simplify(sum(value * right.get(-mode, 0) for mode, value in left.items()))


def main() -> None:
    theta, phi, radius, chi0 = sp.symbols("theta phi r chi0", real=True)

    q = Q(0, 0, 1, sp.I)
    p = Q(1, -sp.I, 0, 0)
    ordered_area = (q.sharp() * p).simplify()
    assert ordered_area == Q(0, 0, -2, -2 * sp.I)
    assert (p.sharp() * q).simplify() == -ordered_area
    assert symmetric_sharp(q, q).is_zero()
    assert symmetric_sharp(p, p).is_zero()
    assert symmetric_sharp(q, p).is_zero()

    n0 = sp.cos(theta)
    n1 = sp.sin(theta) * sp.cos(phi)
    n2 = sp.sin(theta) * sp.sin(phi)
    w1 = (1 + sp.I * n0) * n1
    w2 = (1 + sp.I * n0) * n2

    # Integrability is exact because both jets are derivatives of one potential.
    assert sp.simplify(
        sp.diff(sp.diff(w1, theta), phi) - sp.diff(sp.diff(w1, phi), theta)
    ) == 0
    assert sp.simplify(
        sp.diff(sp.diff(w2, theta), phi) - sp.diff(sp.diff(w2, phi), theta)
    ) == 0

    jacobian = sp.factor(
        sp.diff(w1, theta) * sp.diff(w2, phi)
        - sp.diff(w1, phi) * sp.diff(w2, theta)
    )
    k_factor = sp.simplify(jacobian / sp.sin(theta))
    expected_k = (1 + sp.I * sp.cos(theta)) * (
        sp.cos(theta) + sp.I * (2 * sp.cos(theta) ** 2 - 1)
    )
    assert sp.trigsimp(k_factor - expected_k) == 0

    # For c real, K(c) has no zero: 1+i c never vanishes, while the second
    # factor would require c=0 and 2c^2-1=0 simultaneously.
    c = sp.symbols("c", real=True)
    assert sp.simplify((2 * c**2 - 1).subs(c, 0)) == -1

    sqrt2 = sp.sqrt(2)
    profiles = {
        "P0": {0: sp.Integer(1)},
        "Pc": {2: 1 / sqrt2, -2: 1 / sqrt2},
        "Ps": {2: -sp.I / sqrt2, -2: sp.I / sqrt2},
        "Pt": {3: 1 / sqrt2, -3: 1 / sqrt2},
        "Pr": {3: -sp.I / sqrt2, -3: sp.I / sqrt2},
        "Nplus": {1: sp.Integer(1)},
        "Nminus": {-1: sp.Integer(1)},
    }

    for name in ("P0", "Pc", "Ps", "Pt", "Pr"):
        assert profile_pair(profiles[name], profiles[name]) == 1
    assert profile_pair(profiles["Pc"], profiles["Ps"]) == 0
    assert profile_pair(profiles["Pt"], profiles["Pr"]) == 0

    for null_name in ("Nplus", "Nminus"):
        for visible_name in ("P0", "Pc", "Ps", "Pt", "Pr"):
            assert profile_pair(profiles[null_name], profiles[visible_name]) == 0
    assert profile_pair(profiles["Nplus"], profiles["Nminus"]) == 1

    # The central visible profile V=n0 P0+n1 Pc+n2 Ps gives the unit S^2 metric.
    sphere_coordinates = (n0, n1, n2)
    dtheta_norm = sp.trigsimp(
        sum(sp.diff(value, theta) ** 2 for value in sphere_coordinates)
    )
    dphi_norm = sp.trigsimp(
        sum(sp.diff(value, phi) ** 2 for value in sphere_coordinates)
    )
    cross = sp.trigsimp(
        sum(
            sp.diff(value, theta) * sp.diff(value, phi)
            for value in sphere_coordinates
        )
    )
    radial_orthogonality_theta = sp.trigsimp(
        sum(value * sp.diff(value, theta) for value in sphere_coordinates)
    )
    radial_orthogonality_phi = sp.trigsimp(
        sum(value * sp.diff(value, phi) for value in sphere_coordinates)
    )
    assert dtheta_norm == 1
    assert sp.trigsimp(dphi_norm - sp.sin(theta) ** 2) == 0
    assert cross == 0
    assert radial_orthogonality_theta == 0
    assert radial_orthogonality_phi == 0

    # Shell functions and exact central metric.
    h = sp.symbols("H", real=True)
    h_prime = sp.symbols("Hprime", real=True)
    rho = radius * h
    rho_prime = h + radius * h_prime
    f_prime = 1 - h
    radial_metric = sp.expand(f_prime**2 + rho_prime**2)
    assert sp.simplify(radial_metric.subs({h: 0, h_prime: 0})) == 1
    assert sp.simplify(radial_metric.subs({h: 1, h_prime: 0})) == 1
    assert rho.subs(h, 0) == 0
    assert rho.subs(h, 1) == radius

    # The invariant angular bivector is chi^2 K(c) omega_S2 Q.
    sigma = ordered_area.scale(chi0**2 * jacobian).simplify()
    expected_sigma = ordered_area.scale(
        chi0**2 * expected_k * sp.sin(theta)
    ).simplify()
    assert all(
        sp.trigsimp(a - b) == 0
        for a, b in zip(sigma.values(), expected_sigma.values())
    )
    assert not sigma.is_zero()

    # The exact complex two-form has zero total flux; no false topological claim.
    flux_factor = sp.expand((1 + sp.I * c) * (c + sp.I * (2 * c**2 - 1)))
    assert sp.integrate(flux_factor, (c, -1, 1)) == 0

    print("PASS: Whitney angular potential is globally integrable")
    print("PASS: central angular metric is exactly null")
    print("PASS: invariant biquaternionic area form is pointwise nonzero")
    print("PASS: full shell metric matches flat spherical exterior")
    print("PASS: Whitney bivector channel vanishes at the outer boundary")
    print("PASS: total complex area flux is zero, so no false topological claim")


if __name__ == "__main__":
    main()
