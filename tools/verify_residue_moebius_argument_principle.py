#!/usr/bin/env python3
"""Independent finite/numerical checks for the residue–Möbius RH note.

This script checks selected classical consequences only.  It does not prove
the Riemann hypothesis and does not verify a UBT-specific physical bridge.
"""

from __future__ import annotations

import argparse
import cmath
import math


def factorization(n: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    remainder = n
    p = 2
    while p * p <= remainder:
        while remainder % p == 0:
            factors[p] = factors.get(p, 0) + 1
            remainder //= p
        p += 1
    if remainder > 1:
        factors[remainder] = factors.get(remainder, 0) + 1
    return factors


def mobius(n: int) -> int:
    factors = factorization(n)
    return 0 if any(e > 1 for e in factors.values()) else (-1) ** len(factors)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def check_dirichlet_coefficients(cutoff: int) -> None:
    for n in range(1, cutoff + 1):
        inverse_coefficient = sum(mobius(d) for d in divisors(n))
        expected_inverse = 1 if n == 1 else 0
        if inverse_coefficient != expected_inverse:
            raise AssertionError(("Dirichlet inverse", n, inverse_coefficient))

        # Represent log(n/d) exactly by its vector of prime exponents.
        # The expected vector is one copy of log(p) for a prime power p^k,
        # and the zero vector otherwise.
        coefficient: dict[int, int] = {}
        for d in divisors(n):
            mu_d = mobius(d)
            for p, exponent in factorization(n // d).items():
                coefficient[p] = coefficient.get(p, 0) + mu_d * exponent
        coefficient = {p: e for p, e in coefficient.items() if e}
        n_factors = factorization(n)
        expected = {next(iter(n_factors)): 1} if len(n_factors) == 1 else {}
        if coefficient != expected:
            raise AssertionError(("mu*log", n, coefficient, expected))


def check_partial_summation(cutoff: int, s: complex, tolerance: float) -> None:
    mertens = 0
    lhs = 0j
    integral = 0j
    for n in range(1, cutoff + 1):
        mu_n = mobius(n)
        mertens += mu_n
        lhs += mu_n * n ** (-s)
        if n < cutoff:
            integral += mertens * (
                n ** (-s) - (n + 1) ** (-s)
            ) / s
    rhs = mertens * cutoff ** (-s) + s * integral
    if abs(lhs - rhs) > tolerance:
        raise AssertionError(("partial summation", lhs, rhs))


def winding(values: list[complex]) -> int:
    total = 0.0
    for left, right in zip(values, values[1:] + values[:1]):
        total += cmath.phase(right / left)
    return round(total / (2 * math.pi))


def circle(center: complex, radius: float, samples: int) -> list[complex]:
    return [
        center + radius * cmath.exp(2j * math.pi * k / samples)
        for k in range(samples)
    ]


def zeta_hasse(s: complex, terms: int = 72) -> complex:
    """Evaluate zeta via the Euler-transformed eta (Hasse) series."""
    eta = 0j
    for n in range(terms):
        inner = sum(
            (-1) ** k * math.comb(n, k) * (k + 1) ** (-s)
            for k in range(n + 1)
        )
        eta += inner / (2 ** (n + 1))
    return eta / (1 - 2 ** (1 - s))


def check_winding(samples: int) -> None:
    pole_curve = [zeta_hasse(z) for z in circle(1.0 + 0j, 0.08, samples)]
    if winding(pole_curve) != -1:
        raise AssertionError("zeta pole winding at s=1")

    rho1 = complex(0.5, 14.134725141734694)
    zero_curve = [zeta_hasse(z) for z in circle(rho1, 0.02, samples)]
    if winding(zero_curve) != 1:
        raise AssertionError("zeta zero winding at first nontrivial zero")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoff", type=int, default=250)
    parser.add_argument("--samples", type=int, default=1024)
    args = parser.parse_args()

    check_dirichlet_coefficients(args.cutoff)
    check_partial_summation(args.cutoff, 1.37 + 0.41j, 2e-12)
    check_winding(args.samples)
    print(
        "PASS: Dirichlet inverse, mu*log=Lambda, finite Abel summation, "
        "and zeta pole/zero winding diagnostics"
    )


if __name__ == "__main__":
    main()
