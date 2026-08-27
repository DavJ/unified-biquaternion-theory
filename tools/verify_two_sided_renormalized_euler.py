#!/usr/bin/env python3
"""Checks for the two-sided renormalized Euler-product audit.

The script verifies finite identities, convergence signatures, reflection
normalization, and finite nonlocal-translation norm bounds.  It does not test
analytic continuation, construct a UBT operator, or test RH.
"""

from __future__ import annotations

import cmath
import math


def primes_up_to(limit: int) -> tuple[int, ...]:
    """Return all primes not exceeding limit with an Eratosthenes sieve."""
    if limit < 2:
        return ()
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for candidate in range(2, math.isqrt(limit) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            sieve[start : limit + 1 : candidate] = b"\x00" * (
                (limit - start) // candidate + 1
            )
    return tuple(index for index, flag in enumerate(sieve) if flag)


def finite_euler_log(primes: tuple[int, ...], value: complex) -> complex:
    return sum(-cmath.log(1.0 - prime ** (-value)) for prime in primes)


def finite_prime_layers(
    primes: tuple[int, ...], value: complex, layers: int
) -> complex:
    return sum(
        prime ** (-mode * value) / mode
        for prime in primes
        for mode in range(1, layers + 1)
    )


def finite_remainder_log(
    primes: tuple[int, ...], value: complex, layers: int
) -> complex:
    return sum(
        -cmath.log(1.0 - prime ** (-value))
        - sum(prime ** (-mode * value) / mode for mode in range(1, layers + 1))
        for prime in primes
    )


def real_remainder_log(primes: tuple[int, ...], sigma: float, layers: int) -> float:
    return math.fsum(
        -math.log1p(-(prime ** (-sigma)))
        - math.fsum(prime ** (-mode * sigma) / mode for mode in range(1, layers + 1))
        for prime in primes
    )


def check_finite_maclaurin_factorization() -> None:
    primes = primes_up_to(97)
    for value in (1.3 + 0.4j, 1.8 - 1.1j, 2.2 + 2.7j):
        for layers in (1, 2, 4):
            direct = finite_euler_log(primes, value)
            split = finite_prime_layers(primes, value, layers)
            split += finite_remainder_log(primes, value, layers)
            if abs(direct - split) > 2e-13:
                raise AssertionError(("finite Maclaurin factorization", value, layers))
            product = cmath.exp(direct)
            if abs(product) < 1e-12:
                raise AssertionError(("finite Euler product unexpectedly zero", value))


def check_remainder_convergence_signatures() -> None:
    primes = primes_up_to(100_000)
    cutoffs = (100, 1_000, 10_000, 100_000)

    def values(sigma: float, layers: int) -> tuple[float, ...]:
        return tuple(
            real_remainder_log(tuple(p for p in primes if p <= cutoff), sigma, layers)
            for cutoff in cutoffs
        )

    for sigma, layers in ((0.6, 1), (0.4, 2)):
        sequence = values(sigma, layers)
        increments = tuple(sequence[index + 1] - sequence[index] for index in range(3))
        if not (increments[2] < increments[1] < increments[0]):
            raise AssertionError(("convergent remainder signature", sigma, layers, sequence))

    below = values(0.30, 2)
    if not all(right > left for left, right in zip(below, below[1:])):
        raise AssertionError(("sub-threshold remainder growth", below))


def check_two_sided_reflection() -> None:
    for value in (-2.0 + 3.0j, 0.2 - 7.0j, 0.49 + 11.0j, 1.7 - 2.0j):
        reflected = 1.0 - value
        if abs((1.0 - reflected) - value) > 1e-15:
            raise AssertionError(("reflection involution", value))
        if not math.isclose(reflected.real, 1.0 - value.real, abs_tol=1e-15):
            raise AssertionError(("reflected real part", value))

    # Known exact normalization: xi(2)=xi(-1)=pi/6.
    zeta_two = math.pi**2 / 6.0
    c_two = 1.0 / math.pi
    zeta_minus_one = -1.0 / 12.0
    c_minus_one = -2.0 * math.pi
    if not math.isclose(c_two * zeta_two, math.pi / 6.0, rel_tol=2e-15):
        raise AssertionError("xi(2) normalization")
    if not math.isclose(c_minus_one * zeta_minus_one, math.pi / 6.0, rel_tol=2e-15):
        raise AssertionError("xi(-1) normalization")


def translation_multiplier(
    primes: tuple[int, ...], sigma: float, frequency: float
) -> complex:
    return sum(
        prime ** (-sigma) * cmath.exp(1j * frequency * math.log(prime))
        for prime in primes
    )


def check_first_layer_operator_norm() -> None:
    primes = primes_up_to(10_000)
    for cutoff in (100, 1_000, 10_000):
        selected = tuple(prime for prime in primes if prime <= cutoff)
        for sigma in (0.75, 1.2):
            coefficient_sum = math.fsum(prime ** (-sigma) for prime in selected)
            zero_multiplier = abs(translation_multiplier(selected, sigma, 0.0))
            if not math.isclose(zero_multiplier, coefficient_sum, rel_tol=3e-15):
                raise AssertionError(("zero-frequency norm saturation", cutoff, sigma))
            for frequency in (0.17, 0.9, 2.3, 7.0):
                if abs(translation_multiplier(selected, sigma, frequency)) > coefficient_sum + 1e-12:
                    raise AssertionError(("translation triangle bound", cutoff, sigma, frequency))

    unsafe = tuple(
        math.fsum(prime ** (-0.75) for prime in primes if prime <= cutoff)
        for cutoff in (100, 1_000, 10_000)
    )
    if not unsafe[0] < unsafe[1] < unsafe[2]:
        raise AssertionError(("unsafe first-layer growth", unsafe))


def check_higher_layer_norm_bound() -> None:
    primes = primes_up_to(100_000)
    sigma = 0.6
    values = []
    for cutoff in (100, 1_000, 10_000, 100_000):
        selected = tuple(prime for prime in primes if prime <= cutoff)
        values.append(real_remainder_log(selected, sigma, 1))
    increments = tuple(values[index + 1] - values[index] for index in range(3))
    if not increments[2] < increments[1] < increments[0]:
        raise AssertionError(("higher-layer norm convergence", values))


def von_mangoldt(value: int) -> float:
    for prime in primes_up_to(value):
        power = prime
        while power < value:
            power *= prime
        if power == value:
            return math.log(prime)
    return 0.0


def check_prime_power_log_derivative() -> None:
    limit = 500
    value = 1.7
    integer_sum = math.fsum(
        von_mangoldt(integer) * integer ** (-value)
        for integer in range(2, limit + 1)
    )
    prime_power_sum = 0.0
    for prime in primes_up_to(limit):
        power = prime
        while power <= limit:
            prime_power_sum += math.log(prime) * power ** (-value)
            power *= prime
    if not math.isclose(integer_sum, prime_power_sum, rel_tol=3e-15, abs_tol=3e-15):
        raise AssertionError(("finite logarithmic derivative", integer_sum, prime_power_sum))


def main() -> None:
    check_finite_maclaurin_factorization()
    check_remainder_convergence_signatures()
    check_two_sided_reflection()
    check_first_layer_operator_norm()
    check_higher_layer_norm_bound()
    check_prime_power_log_derivative()
    print(
        "PASS: finite Maclaurin factorization, renormalized-remainder thresholds, "
        "two-sided reflection, first- and higher-layer translation norm bounds, "
        "and the finite prime-power logarithmic derivative"
    )
    print(
        "LIMITATION: finite checks do not construct analytic continuation, a "
        "critical-line boundary operator, a UBT derivation, or an RH proof."
    )


if __name__ == "__main__":
    main()
