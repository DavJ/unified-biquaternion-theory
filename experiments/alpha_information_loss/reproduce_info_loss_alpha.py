#!/usr/bin/env python3
"""Reproduce the UBT alpha information-loss research-track numbers.

This script is intentionally dependency-light.  It uses mpmath only.
It does not use the experimental fine-structure constant as an input for the
C_Q=4 prediction.  The experimental value is used only for the post-check that
computes the target C_Q.
"""

import mpmath as mp

mp.mp.dps = 80


def eta_i(rho: mp.mpf) -> mp.mpf:
    """Dedekind eta at tau = i*rho using the product definition."""
    q = mp.e ** (-2 * mp.pi * rho)
    product = mp.nprod(lambda k: 1 - q**k, [1, mp.inf])
    return q ** (mp.mpf(1) / 24) * product


def B_of_rho(rho: mp.mpf) -> mp.mpf:
    return mp.mpf(12) ** (mp.mpf(3) / 2) * (2 * eta_i(rho)) ** (mp.mpf(1) / 4)


def stationarity_residual(n: mp.mpf, C_Q: mp.mpf = mp.mpf(4)) -> mp.mpf:
    rho = mp.e ** (-C_Q / (2 * mp.pi * n))
    return 2 * n / (mp.log(n) + 1) - B_of_rho(rho)


def solve_n(C_Q: mp.mpf = mp.mpf(4), seed: mp.mpf = mp.mpf(137)) -> mp.mpf:
    return mp.findroot(lambda x: stationarity_residual(x, C_Q), seed)


def solve_C_for_target_n(n_target: mp.mpf, seed: mp.mpf = mp.mpf(4)) -> mp.mpf:
    B_target = 2 * n_target / (mp.log(n_target) + 1)
    return mp.findroot(
        lambda c: B_of_rho(mp.e ** (-c / (2 * mp.pi * n_target))) - B_target,
        seed,
    )


def main() -> None:
    C_Q = mp.mpf(4)
    n = solve_n(C_Q)
    alpha = 1 / n
    delta_I = C_Q / (2 * mp.pi * n)
    rho = mp.e ** (-delta_I)

    n_uncorrected = mp.findroot(lambda x: 2 * x / (mp.log(x) + 1) - B_of_rho(1), 137)

    alpha_exp_inv = mp.mpf("137.035999084")
    C_target = solve_C_for_target_n(alpha_exp_inv)
    delta_target = C_target / (2 * mp.pi * alpha_exp_inv)
    rho_target = mp.e ** (-delta_target)

    print("UBT alpha information-loss research-track reproduction")
    print("--------------------------------------------------------")
    print(f"B(1)                         = {mp.nstr(B_of_rho(1), 30)}")
    print(f"n at rho=1                   = {mp.nstr(n_uncorrected, 30)}")
    print()
    print("Minimal four-channel prediction")
    print(f"C_Q                           = {C_Q}")
    print(f"n = alpha^-1                  = {mp.nstr(n, 30)}")
    print(f"alpha                         = {mp.nstr(alpha, 30)}")
    print(f"Delta I_Q                     = {mp.nstr(delta_I, 30)}")
    print(f"rho = exp(-Delta I_Q)         = {mp.nstr(rho, 30)}")
    print(f"delta = 1-rho                 = {mp.nstr(1-rho, 30)}")
    print()
    print("Post-check against Thomson-limit alpha^-1")
    print(f"alpha_exp^-1                  = {alpha_exp_inv}")
    print(f"difference n_pred - n_exp     = {mp.nstr(n-alpha_exp_inv, 30)}")
    print(f"relative difference           = {mp.nstr((n-alpha_exp_inv)/alpha_exp_inv, 30)}")
    print(f"C_Q required for target        = {mp.nstr(C_target, 30)}")
    print(f"4 - C_Q_target                = {mp.nstr(4-C_target, 30)}")
    print(f"relative correction to 4       = {mp.nstr((4-C_target)/4, 30)}")
    print(f"target Delta I_Q              = {mp.nstr(delta_target, 30)}")
    print(f"target rho                    = {mp.nstr(rho_target, 30)}")


if __name__ == "__main__":
    main()
