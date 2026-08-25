#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Exact and numerical checks for the graded prime-Fock Möbius bridge.

The verifier checks classical finite identities only. It does not derive
prime modes or parity from UBT and does not test the Riemann hypothesis.
"""

from __future__ import annotations

import argparse
import itertools
import math


def sieve_primes(limit: int) -> list[int]:
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if flags[p]:
            flags[p * p :: p] = b"\x00" * len(flags[p * p :: p])
    return [n for n in range(2, limit + 1) if flags[n]]


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
    if any(exponent > 1 for exponent in factors.values()):
        return 0
    return (-1) ** len(factors)


def subset_supertrace_coefficients(primes: list[int]) -> dict[int, int]:
    coefficients: dict[int, int] = {}
    for occupations in itertools.product((0, 1), repeat=len(primes)):
        n = math.prod(p for p, occupied in zip(primes, occupations) if occupied)
        sign = (-1) ** sum(occupations)
        coefficients[n] = coefficients.get(n, 0) + sign
    return coefficients


def product_expansion_coefficients(primes: list[int]) -> dict[int, int]:
    coefficients = {1: 1}
    for p in primes:
        updated = dict(coefficients)
        for n, coefficient in coefficients.items():
            updated[n * p] = updated.get(n * p, 0) - coefficient
        coefficients = updated
    return coefficients


def p_smooth_indicator(n: int, prime_set: set[int]) -> int:
    return int(set(factorization(n)).issubset(prime_set))


def truncated_mobius_coefficient(n: int, prime_set: set[int]) -> int:
    factors = factorization(n)
    return mobius(n) if set(factors).issubset(prime_set) else 0


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def check_exact_coefficients(primes: list[int]) -> None:
    by_states = subset_supertrace_coefficients(primes)
    by_product = product_expansion_coefficients(primes)
    if by_states != by_product:
        raise AssertionError("subset supertrace and product expansion disagree")
    for n, coefficient in by_states.items():
        expected = mobius(n)
        if coefficient != expected:
            raise AssertionError(("Möbius coefficient", n, coefficient, expected))


def check_dirichlet_inverse(primes: list[int], cutoff: int) -> None:
    prime_set = set(primes)
    for n in range(1, cutoff + 1):
        coefficient = sum(
            p_smooth_indicator(d, prime_set)
            * truncated_mobius_coefficient(n // d, prime_set)
            for d in divisors(n)
        )
        expected = 1 if n == 1 else 0
        if coefficient != expected:
            raise AssertionError(("finite Dirichlet inverse", n, coefficient))


def graded_product(s: float, primes: list[int]) -> float:
    return math.prod(1.0 - p ** (-s) for p in primes)


def bosonic_product(s: float, primes: list[int]) -> float:
    return math.prod(1.0 / (1.0 - p ** (-s)) for p in primes)


def ordinary_fermionic_product(s: float, primes: list[int]) -> float:
    return math.prod(1.0 + p ** (-s) for p in primes)


def check_partition_functions(primes: list[int], tolerance: float) -> None:
    coefficients = subset_supertrace_coefficients(primes)
    for s in (1.25, 1.5, 2.0, 3.0):
        by_product = graded_product(s, primes)
        by_states = math.fsum(coefficient * n ** (-s) for n, coefficient in coefficients.items())
        if not math.isclose(by_product, by_states, rel_tol=tolerance, abs_tol=tolerance):
            raise AssertionError(("graded trace", s, by_product, by_states))
        inverse = bosonic_product(s, primes) * by_product
        if not math.isclose(inverse, 1.0, rel_tol=tolerance, abs_tol=tolerance):
            raise AssertionError(("boson/graded inverse", s, inverse))
        ordinary = ordinary_fermionic_product(s, primes)
        if math.isclose(ordinary, by_product, rel_tol=tolerance, abs_tol=tolerance):
            raise AssertionError(("ordinary trace unexpectedly equals supertrace", s))


def check_zeta2_benchmark(prime_limit: int, tolerance: float) -> None:
    primes = sieve_primes(prime_limit)
    approximation = graded_product(2.0, primes)
    exact = 6.0 / (math.pi * math.pi)
    relative_error = abs(approximation - exact) / exact
    if relative_error >= tolerance:
        raise AssertionError(("1/zeta(2) benchmark", relative_error, tolerance))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state-prime-limit", type=int, default=29)
    parser.add_argument("--inverse-cutoff", type=int, default=1000)
    parser.add_argument("--benchmark-prime-limit", type=int, default=5000)
    parser.add_argument("--benchmark-tolerance", type=float, default=5e-5)
    args = parser.parse_args()

    state_primes = sieve_primes(args.state_prime_limit)
    check_exact_coefficients(state_primes)
    check_dirichlet_inverse(state_primes, args.inverse_cutoff)
    check_partition_functions(state_primes, 2e-13)
    check_zeta2_benchmark(args.benchmark_prime_limit, args.benchmark_tolerance)
    print(
        "PASS: graded coefficients, Möbius signs, finite Dirichlet inverse, "
        "boson/supertrace cancellation, and 1/zeta(2) convergence "
        f"(state_primes={len(state_primes)}, cutoff={args.inverse_cutoff})"
    )


if __name__ == "__main__":
    main()

