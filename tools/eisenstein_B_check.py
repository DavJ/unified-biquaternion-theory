#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Check the Eisenstein-series and discriminant routes for Gap G137-B."""

from __future__ import annotations

import math


def sigma_3(n: int) -> int:
    """Return σ₃(n)."""
    return sum(divisor**3 for divisor in range(1, n + 1) if n % divisor == 0)


def e4_at_i(n_terms: int = 200) -> float:
    """Compute E₄(i) from its q-series."""
    q = math.exp(-2.0 * math.pi)
    total = 1.0
    for n in range(1, n_terms + 1):
        total += 240.0 * sigma_3(n) * (q**n)
    return total


def eta_at_i() -> float:
    """Return η(i) from the standard CM-value formula."""
    return math.gamma(0.25) / (2.0 * math.pi ** 0.75)


def b_target() -> float:
    """Return the phenomenological target coefficient."""
    return 12.0**1.5 * (2.0 * eta_at_i()) ** 0.25


def b_via_e4() -> float:
    """Return the Eisenstein-series candidate."""
    return 12.0**1.5 * e4_at_i() ** (1.0 / 16.0)


def b_via_delta(k: int) -> float:
    """Return the discriminant candidate for integer k >= 1."""
    delta_i = eta_at_i() ** 24
    return 12.0**1.5 * abs(delta_i) ** (1.0 / (12.0 * k))


def main() -> None:
    e4_i = e4_at_i()
    eta_i = eta_at_i()
    target = b_target()
    via_e4 = b_via_e4()

    print(f"E_4(i) = {e4_i:.12f}")
    print(f"E_4(i)^(1/16) = {e4_i ** (1.0 / 16.0):.12f}")
    print(f"eta(i) = {eta_i:.12f}")
    print(f"B via E4 = {via_e4:.12f}")
    print(f"B_target = {target:.12f}")
    print(f"ratio(E4/target) = {via_e4 / target:.12f}")

    print("\nDelta-route scan:")
    for k in range(1, 13):
        via_delta = b_via_delta(k)
        print(f"  k={k:2d}: B = {via_delta:.12f}, ratio = {via_delta / target:.12f}")

    if abs(via_e4 - target) / target < 1e-3:
        print("\nVerdict: Eisenstein E4 route is numerically viable.")
    else:
        print("\nVerdict: Eisenstein E4 route is NO-GO at the tested normalization.")


if __name__ == "__main__":
    main()
