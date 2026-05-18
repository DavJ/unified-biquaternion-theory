# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Numerical check for direct one-loop functional derivation path (Gap G137-B)."""

from __future__ import annotations

import math


def v1loop(d: int, r: float = 1.0, mu: float = 1.0) -> float:
    """One-loop contribution from mode d using the standard M^4 zeta result."""
    m2 = (d / r) ** 2
    return m2**2 / (32 * math.pi**2) * (2 * math.log(d / (r * mu)) - 1.5)


def coeff_nlnn(n_max: int = 500) -> float:
    """Average asymptotic coefficient of n*ln(n) in V_eff over the tail window."""
    coeffs: list[float] = []
    for n in range(2, n_max):
        v_eff = sum(v1loop(d) for d in range(1, n + 1) if n % d == 0)
        coeffs.append(v_eff / (n * math.log(n)))
    return sum(coeffs[-100:]) / 100


def main() -> None:
    b_computed = coeff_nlnn()
    b_target = 12**1.5 * (2 * 0.7682254) ** 0.25
    ratio = b_computed / b_target

    print(f"B_computed = {b_computed:.6f}")
    print(f"B_target   = {b_target:.6f}")
    print(f"Ratio      = {ratio:.6f}")


if __name__ == "__main__":
    main()
