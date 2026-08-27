#!/usr/bin/env python3
"""Exact and numerical checks for the adelic prime-decomposition audit.

The checks cover classical arithmetic and finite-dimensional approximations.
They do not derive prime sectors from UBT and do not test the Riemann hypothesis.
"""

from __future__ import annotations

import cmath
import itertools
import math


TAU = 2.0 * math.pi


def prime_power_factors(value: int) -> tuple[int, ...]:
    """Return the pairwise-coprime maximal prime-power factors of value."""
    if value < 1:
        raise ValueError("value must be positive")
    remaining = value
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor:
            divisor = 3 if divisor == 2 else divisor + 2
            continue
        power = 1
        while remaining % divisor == 0:
            remaining //= divisor
            power *= divisor
        factors.append(power)
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append(remaining)
    return tuple(factors)


def prime_base(prime_power: int) -> int:
    """Recover the unique prime base of a positive prime power."""
    if prime_power < 2:
        raise ValueError("prime_power must be at least two")
    for candidate in range(2, math.isqrt(prime_power) + 1):
        if prime_power % candidate == 0:
            return candidate
    return prime_power


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def primes_up_to(limit: int) -> tuple[int, ...]:
    primes: list[int] = []
    for candidate in range(2, limit + 1):
        if all(candidate % prime for prime in primes if prime * prime <= candidate):
            primes.append(candidate)
    return tuple(primes)


def check_valuation_fock_bijection() -> None:
    primes = primes_up_to(5000)
    for value in range(1, 5001):
        exponents = tuple(valuation(value, prime) for prime in primes)
        reconstructed = math.prod(
            prime**exponent for prime, exponent in zip(primes, exponents)
        )
        if reconstructed != value:
            raise AssertionError(("valuation reconstruction", value, reconstructed))
        energy = math.fsum(
            exponent * math.log(prime)
            for prime, exponent in zip(primes, exponents)
        )
        if not math.isclose(energy, math.log(value), rel_tol=2e-15, abs_tol=2e-15):
            raise AssertionError(("logarithmic Fock energy", value, energy))


def check_local_radial_trace() -> None:
    for prime in (2, 3, 5, 11):
        for sigma in (0.4, 1.25, 2.0):
            ratio = prime ** (-sigma)
            for cutoff in (0, 1, 4, 20):
                direct = math.fsum(ratio**mode for mode in range(cutoff + 1))
                closed = (1.0 - ratio ** (cutoff + 1)) / (1.0 - ratio)
                if not math.isclose(direct, closed, rel_tol=2e-15, abs_tol=2e-15):
                    raise AssertionError(("local geometric trace", prime, sigma, cutoff))
            infinite = 1.0 / (1.0 - ratio)
            truncated = math.fsum(ratio**mode for mode in range(400))
            if not math.isclose(truncated, infinite, rel_tol=2e-14, abs_tol=2e-14):
                raise AssertionError(("local Tate factor", prime, sigma))


def check_finite_tensor_trace() -> None:
    primes = (2, 3, 5)
    sigma = 1.7
    occupation_cutoff = 5
    state_sum = 0.0
    for occupations in itertools.product(
        range(occupation_cutoff + 1), repeat=len(primes)
    ):
        energy = math.fsum(
            mode * math.log(prime) for prime, mode in zip(primes, occupations)
        )
        state_sum += math.exp(-sigma * energy)
    factorized = math.prod(
        math.fsum(prime ** (-sigma * mode) for mode in range(occupation_cutoff + 1))
        for prime in primes
    )
    if not math.isclose(state_sum, factorized, rel_tol=3e-15, abs_tol=3e-15):
        raise AssertionError(("finite tensor trace", state_sum, factorized))


def check_self_adjoint_core_truncation() -> None:
    """Numerical graph-norm sanity check for the finite-support core proof."""
    previous = math.inf
    for cutoff in (8, 16, 32, 64, 128, 256, 512):
        tail = math.fsum(
            (1.0 + math.log(value) ** 2) / value**4
            for value in range(cutoff + 1, 20000)
        )
        if not tail < previous:
            raise AssertionError(("graph-norm core tail", cutoff, tail, previous))
        previous = tail
    if previous > 2e-7:
        raise AssertionError(("graph-norm tail too large", previous))


def crt_idempotents(moduli: tuple[int, ...]) -> tuple[int, ...]:
    modulus = math.prod(moduli)
    result = []
    for local_modulus in moduli:
        complement = modulus // local_modulus
        inverse = pow(complement, -1, local_modulus)
        result.append((complement * inverse) % modulus)
    return tuple(result)


def crt_reconstruct(coordinates: tuple[int, ...], moduli: tuple[int, ...]) -> int:
    modulus = math.prod(moduli)
    return sum(
        coordinate * idempotent
        for coordinate, idempotent in zip(coordinates, crt_idempotents(moduli))
    ) % modulus


def check_crt_projectors() -> None:
    for modulus in (12, 45, 60, 140, 225):
        moduli = prime_power_factors(modulus)
        if math.prod(moduli) != modulus:
            raise AssertionError(("prime-power product", modulus, moduli))
        if any(math.gcd(left, right) != 1 for left, right in itertools.combinations(moduli, 2)):
            raise AssertionError(("prime powers not coprime", modulus, moduli))
        idempotents = crt_idempotents(moduli)
        if sum(idempotents) % modulus != 1:
            raise AssertionError(("CRT identity resolution", modulus, idempotents))
        for index, idempotent in enumerate(idempotents):
            if (idempotent * idempotent - idempotent) % modulus:
                raise AssertionError(("CRT idempotence", modulus, idempotent))
            for other, local_modulus in enumerate(moduli):
                expected = 1 if index == other else 0
                if idempotent % local_modulus != expected:
                    raise AssertionError(("CRT orthogonality", modulus, index, other))
        seen = {
            crt_reconstruct(tuple(coordinates), moduli)
            for coordinates in itertools.product(*(range(item) for item in moduli))
        }
        if seen != set(range(modulus)):
            raise AssertionError(("CRT bijection", modulus, len(seen)))


def quadratic_phase(coefficient: int, residue: int, modulus: int) -> complex:
    return cmath.exp(1j * TAU * coefficient * residue * residue / modulus)


def gauss_sum(coefficient: int, modulus: int) -> complex:
    return sum(
        quadratic_phase(coefficient, residue, modulus)
        for residue in range(modulus)
    )


def check_revival_phase_factorization() -> None:
    for modulus, coefficient in ((12, 1), (45, 2), (140, 3), (225, 7)):
        moduli = prime_power_factors(modulus)
        complements = tuple(modulus // item for item in moduli)
        inverses = tuple(
            pow(complement, -1, item)
            for complement, item in zip(complements, moduli)
        )
        for residue in range(modulus):
            coordinates = tuple(residue % item for item in moduli)
            global_phase = quadratic_phase(coefficient, residue, modulus)
            local_phase = math.prod(
                quadratic_phase(coefficient * inverse, coordinate, item)
                for inverse, coordinate, item in zip(inverses, coordinates, moduli)
            )
            if abs(global_phase - local_phase) > 5e-12:
                raise AssertionError(("revival phase CRT", modulus, residue))
        global_sum = gauss_sum(coefficient, modulus)
        local_product = math.prod(
            gauss_sum(coefficient * inverse, item)
            for inverse, item in zip(inverses, moduli)
        )
        if abs(global_sum - local_product) > 2e-11:
            raise AssertionError(("Gauss-sum CRT", modulus, global_sum, local_product))


def theta_standard(time: float) -> float:
    """theta_3(0|i time) with the standard exp(-pi*n^2*time) convention."""
    if time <= 0:
        raise ValueError("time must be positive")
    if time < 1.0:
        return theta_standard(1.0 / time) / math.sqrt(time)
    total = 1.0
    for mode in range(1, 10000):
        term = math.exp(-math.pi * mode * mode * time)
        total += 2.0 * term
        if term < 1e-16:
            break
    return total


def simpson(function, left: float, right: float, intervals: int) -> float:
    if intervals % 2:
        raise ValueError("Simpson interval count must be even")
    step = (right - left) / intervals
    total = function(left) + function(right)
    total += 4.0 * math.fsum(function(left + step * index) for index in range(1, intervals, 2))
    total += 2.0 * math.fsum(function(left + step * index) for index in range(2, intervals, 2))
    return total * step / 3.0


def check_archimedean_mellin_completion() -> None:
    # At s=2, the completed theta Mellin integral is pi^-1*zeta(2)=pi/6.
    def log_integrand(log_time: float) -> float:
        time = math.exp(log_time)
        return 0.5 * (theta_standard(time) - 1.0) * time

    middle = simpson(log_integrand, -24.0, 5.0, 12000)
    # For x -> -infinity, theta(e^x)-1 = e^{-x/2}-1 plus exponentially
    # small terms. Integrate the two elementary tail terms exactly.
    left = -24.0
    lower_tail = math.exp(left / 2.0) - 0.5 * math.exp(left)
    value = lower_tail + middle
    expected = math.pi / 6.0
    if not math.isclose(value, expected, rel_tol=2e-8, abs_tol=2e-8):
        raise AssertionError(("theta Mellin completion", value, expected))


def check_factorization_output_gate() -> None:
    """The maximal prime-power output itself reconstructs the factorization."""
    for value in range(2, 1000):
        powers = prime_power_factors(value)
        bases = tuple(prime_base(power) for power in powers)
        reconstructed = math.prod(
            base ** valuation(value, base) for base in bases
        )
        if reconstructed != value:
            raise AssertionError(("factorization-output gate", value, powers, bases))


def main() -> None:
    check_valuation_fock_bijection()
    check_local_radial_trace()
    check_finite_tensor_trace()
    check_self_adjoint_core_truncation()
    check_crt_projectors()
    check_revival_phase_factorization()
    check_archimedean_mellin_completion()
    check_factorization_output_gate()
    print(
        "PASS: valuation/Fock bijection, local radial Tate traces, finite tensor trace, "
        "self-adjoint-core truncation, CRT idempotents, rational-revival phase and "
        "Gauss-sum factorization, archimedean theta Mellin completion, and the "
        "factorization-output gate"
    )
    print(
        "LIMITATION: these checks verify classical arithmetic and finite/numerical "
        "consequences only; they do not derive rational denominators, prime sectors, "
        "or a Hilbert--Polya operator from UBT."
    )


if __name__ == "__main__":
    main()
