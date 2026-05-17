# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Numerical scan for the focused modular-bootstrap route (Gap G137-B)."""

import math
import mpmath

mpmath.mp.dps = 30


def b_from_tau(tau_imag: float) -> float:
    """B = 12^(3/2) * (2*eta(i*tau))^(1/4)."""
    eta_val = float(mpmath.re(mpmath.eta(mpmath.mpc(0, tau_imag))))
    return 12**1.5 * (2 * eta_val) ** 0.25


def n_star(b_value: float) -> float:
    """Fixed-point estimate for stationarity of V_eff = n^2 - B*n*ln(n)."""
    n_val = 100.0
    for _ in range(1000):
        n_new = b_value * (math.log(n_val) + 1.0) / 2.0
        if abs(n_new - n_val) < 1e-12:
            break
        n_val = n_new
    return n_val


def main() -> None:
    print("tau_imag | B | n*")
    for tau in [0.5, 0.7, 0.9, 1.0, 1.1, 1.3, 1.5, 2.0]:
        b_value = b_from_tau(tau)
        n_val = n_star(b_value)
        print(f"tau={tau:.1f}: B={b_value:.4f}, n*={n_val:.4f}")


if __name__ == "__main__":
    main()
