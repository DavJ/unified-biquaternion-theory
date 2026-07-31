#!/usr/bin/env python3
"""Exact finite-dimensional checks for the free-profile GR completion candidate.

The script verifies the algebraic transfer used in
research_tracks/T1_GR/free_fiber_completion/gap_10r_free_fiber_embedding_completion.tex:

* one W_L-valued periodic profile contains an exact R^(13,1) block;
* a free 4D two-jet transfers to four tangent and ten independent normal
  profile vectors;
* the induced profile metric is Lorentzian;
* the Gauss scalar computed from the Riemann tensor equals the contracted
  second-fundamental-form expression.

It does not numerically prove the local free-isometric-embedding theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

import sympy as sp

PAIR_ORDER = (
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 2),
    (2, 3),
    (3, 3),
)


@dataclass(frozen=True)
class ProfileCarrier:
    metric: sp.Matrix
    inclusion: sp.Matrix


def build_profile_carrier() -> ProfileCarrier:
    """Construct fourteen orthonormal profiles in a finite Fourier carrier.

    Carrier coordinates are (mode, trig, Lorentz direction).  The constant
    mode has weight 1 and nonzero sine/cosine modes have Haar weight 1/2.
    The internal Lorentz metric is diag(-1,+1,+1,+1).
    """

    coordinates: list[tuple[int, str, int]] = []
    weights: list[sp.Expr] = []

    # Constant mode.
    for direction in range(4):
        coordinates.append((0, "c", direction))
        weights.append(sp.Integer(-1 if direction == 0 else 1))

    # Three nonzero Fourier numbers; each has cos and sin copies.
    for mode in range(1, 4):
        for trig in ("c", "s"):
            for direction in range(4):
                coordinates.append((mode, trig, direction))
                sign = -1 if direction == 0 else 1
                weights.append(sp.Rational(1, 2) * sign)

    carrier_metric = sp.diag(*weights)
    index = {coordinate: i for i, coordinate in enumerate(coordinates)}

    profiles: list[sp.Matrix] = []

    # One unit timelike constant profile.
    f0 = sp.zeros(len(coordinates), 1)
    f0[index[(0, "c", 0)], 0] = 1
    profiles.append(f0)

    # Thirteen unit spacelike profiles from distinct Fourier/trig/direction
    # labels. sqrt(2) compensates the Haar weight 1/2.
    positive_labels = [
        (mode, trig, direction)
        for mode in range(1, 4)
        for trig in ("c", "s")
        for direction in (1, 2, 3)
    ][:13]
    for label in positive_labels:
        profile = sp.zeros(len(coordinates), 1)
        profile[index[label], 0] = sp.sqrt(2)
        profiles.append(profile)

    inclusion = sp.Matrix.hstack(*profiles)
    return ProfileCarrier(metric=carrier_metric, inclusion=inclusion)


def ambient_metric() -> sp.Matrix:
    return sp.diag(-1, *([1] * 13))


def free_jet_matrices() -> tuple[sp.Matrix, sp.Matrix]:
    """Return ambient tangent (14x4) and normal-second (14x10) blocks."""
    tangents = sp.zeros(14, 4)
    seconds = sp.zeros(14, 10)
    for mu in range(4):
        tangents[mu, mu] = 1
    for column in range(10):
        seconds[4 + column, column] = 1
    return tangents, seconds


def profile_metric_and_rank() -> tuple[sp.Matrix, int, int, sp.Matrix]:
    carrier = build_profile_carrier()
    eta14 = ambient_metric()
    tangents, seconds = free_jet_matrices()

    gram14 = sp.simplify(carrier.inclusion.T * carrier.metric * carrier.inclusion)
    profile_tangents = carrier.inclusion * tangents
    profile_seconds = carrier.inclusion * seconds
    g4 = sp.simplify(profile_tangents.T * carrier.metric * profile_tangents)
    osculating = profile_tangents.row_join(profile_seconds)
    return g4, profile_seconds.rank(), osculating.rank(), gram14


def b_vector(seconds: sp.Matrix, mu: int, nu: int) -> sp.Matrix:
    pair = (mu, nu) if mu <= nu else (nu, mu)
    return seconds[:, PAIR_ORDER.index(pair)]


def gauss_checks() -> tuple[sp.Expr, sp.Expr, bool, bool, bool]:
    eta14 = ambient_metric()
    g = sp.diag(-1, 1, 1, 1)
    ginv = g.inv()
    _, seconds = free_jet_matrices()

    def inner(u: sp.Matrix, v: sp.Matrix) -> sp.Expr:
        return sp.expand((u.T * eta14 * v)[0])

    def riemann(mu: int, nu: int, rho: int, sigma: int) -> sp.Expr:
        return sp.expand(
            inner(b_vector(seconds, mu, rho), b_vector(seconds, nu, sigma))
            - inner(b_vector(seconds, mu, sigma), b_vector(seconds, nu, rho))
        )

    scalar_from_riemann = sp.Integer(0)
    for mu, nu, rho, sigma in product(range(4), repeat=4):
        scalar_from_riemann += (
            ginv[mu, rho] * ginv[nu, sigma] * riemann(mu, nu, rho, sigma)
        )
    scalar_from_riemann = sp.simplify(scalar_from_riemann)

    b_trace = sp.zeros(14, 1)
    for mu, nu in product(range(4), repeat=2):
        b_trace += ginv[mu, nu] * b_vector(seconds, mu, nu)

    b_norm = sp.Integer(0)
    for mu, nu, rho, sigma in product(range(4), repeat=4):
        b_norm += (
            ginv[mu, rho]
            * ginv[nu, sigma]
            * inner(b_vector(seconds, mu, nu), b_vector(seconds, rho, sigma))
        )
    scalar_from_b = sp.simplify(inner(b_trace, b_trace) - b_norm)

    antisym_first = all(
        sp.simplify(riemann(mu, nu, rho, sigma) + riemann(nu, mu, rho, sigma)) == 0
        for mu, nu, rho, sigma in product(range(4), repeat=4)
    )
    pair_exchange = all(
        sp.simplify(riemann(mu, nu, rho, sigma) - riemann(rho, sigma, mu, nu)) == 0
        for mu, nu, rho, sigma in product(range(4), repeat=4)
    )
    first_bianchi = all(
        sp.simplify(
            riemann(mu, nu, rho, sigma)
            + riemann(mu, rho, sigma, nu)
            + riemann(mu, sigma, nu, rho)
        )
        == 0
        for mu, nu, rho, sigma in product(range(4), repeat=4)
    )

    return (
        scalar_from_riemann,
        scalar_from_b,
        antisym_first,
        pair_exchange,
        first_bianchi,
    )


def run_checks() -> None:
    g4, closure_rank, osculating_rank, gram14 = profile_metric_and_rank()
    scalar_r, scalar_b, anti, exchange, bianchi = gauss_checks()

    assert gram14 == ambient_metric()
    assert g4 == sp.diag(-1, 1, 1, 1)
    assert closure_rank == 10
    assert osculating_rank == 14
    assert scalar_r == scalar_b
    assert anti and exchange and bianchi

    print("PASS: fourteen explicit W_L-valued Fourier profiles realize R^(13,1).")
    print("PASS: induced tangent Gram matrix is diag(-1,+1,+1,+1).")
    print("PASS: ten normal second profiles have exact closure rank 10.")
    print("PASS: the full osculating two-jet has rank 14 (free).")
    print(f"PASS: Gauss scalar identity agrees exactly (R = {scalar_r}).")
    print("PASS: sample Gauss Riemann tensor has the required algebraic symmetries.")
    print("NOT TESTED: the analytic free-embedding existence theorem itself.")
    print("NOT TESTED: dynamic selection or stability of the profile branch.")


if __name__ == "__main__":
    run_checks()
