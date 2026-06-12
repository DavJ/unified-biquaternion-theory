#!/usr/bin/env python3
"""Reproduce the UBT alpha Layer2 kernel-refinement research-track numbers.

Models:
1. Self-dual eta-winding: rho = 1.
2. Minimal four-channel information loss: C_Q = 4.
3. Sharp Layer2 eta-spectral projection: r_L2 = 3.
4. First Layer2 eta-kernel refinement:
   r_L2 = 3 * (1 + Omega_eta(1)).

The CODATA value is used only for comparison, not as input.
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 80

CODATA_ALPHA_INV = mp.mpf("137.035999177")
CODATA_SIGMA = mp.mpf("0.000000021")


def eta_i(rho: mp.mpf) -> mp.mpf:
    q = mp.e ** (-2 * mp.pi * rho)
    product = mp.nprod(lambda k: 1 - q**k, [1, mp.inf])
    return q ** (mp.mpf(1) / 24) * product


def B_of_rho(rho: mp.mpf) -> mp.mpf:
    return mp.mpf(12) ** (mp.mpf(3) / 2) * (2 * eta_i(rho)) ** (mp.mpf(1) / 4)


def stationarity_residual_with_rho(n: mp.mpf, rho: mp.mpf) -> mp.mpf:
    return 2 * n / (mp.log(n) + 1) - B_of_rho(rho)


def solve_self_dual(seed: mp.mpf = mp.mpf(137)) -> mp.mpf:
    return mp.findroot(lambda x: stationarity_residual_with_rho(x, mp.mpf(1)), seed)


def omega_eta_self_dual() -> mp.mpf:
    return mp.mpf(1) / 24 - mp.mpf(1) / (8 * mp.pi)


def eta_spectral_subtraction() -> mp.mpf:
    return (mp.pi - 3) / 2


def C_minimal(_: mp.mpf) -> mp.mpf:
    return mp.mpf(4)


def C_with_rank(n: mp.mpf, r_eff: mp.mpf) -> mp.mpf:
    eps = eta_spectral_subtraction()
    return 4 - eps * ((n - r_eff) / n)


def C_sharp_layer2(n: mp.mpf) -> mp.mpf:
    return C_with_rank(n, mp.mpf(3))


def r_layer2_kernel() -> mp.mpf:
    return 3 * (1 + omega_eta_self_dual())


def C_layer2_kernel(n: mp.mpf) -> mp.mpf:
    return C_with_rank(n, r_layer2_kernel())


def solve_information_loss(C_func, seed: mp.mpf = mp.mpf(137)) -> mp.mpf:
    def residual(n: mp.mpf) -> mp.mpf:
        C = C_func(n)
        rho = mp.e ** (-C / (2 * mp.pi * n))
        return stationarity_residual_with_rho(n, rho)

    return mp.findroot(residual, seed)


def solve_C_for_target_n(n_target: mp.mpf, seed: mp.mpf = mp.mpf(4)) -> mp.mpf:
    B_target = 2 * n_target / (mp.log(n_target) + 1)
    return mp.findroot(
        lambda c: B_of_rho(mp.e ** (-c / (2 * mp.pi * n_target))) - B_target,
        seed,
    )


def solve_r_eff_for_target_n(n_target: mp.mpf) -> mp.mpf:
    C_target = solve_C_for_target_n(n_target)
    eps = eta_spectral_subtraction()
    # C = 4 - eps * ((n-r)/n)
    return n_target * (1 - (4 - C_target) / eps)


def print_model(name: str, n: mp.mpf, C: mp.mpf | None = None, r: mp.mpf | None = None) -> None:
    diff = n - CODATA_ALPHA_INV
    sigma = diff / CODATA_SIGMA
    print(name)
    print("-" * len(name))
    if r is not None:
        print(f"r_eff                         = {mp.nstr(r, 50)}")
    if C is not None:
        rho = mp.e ** (-C / (2 * mp.pi * n))
        print(f"C_Q                           = {mp.nstr(C, 50)}")
        print(f"rho                           = {mp.nstr(rho, 50)}")
        print(f"Delta I_Q                     = {mp.nstr(-mp.log(rho), 50)}")
    print(f"n = alpha^-1                  = {mp.nstr(n, 50)}")
    print(f"alpha                         = {mp.nstr(1/n, 50)}")
    print(f"diff from CODATA 2022         = {mp.nstr(diff, 40)}")
    print(f"sigma vs CODATA 2022          = {mp.nstr(sigma, 25)}")
    print()


def main() -> None:
    n_self = solve_self_dual()
    n_C4 = solve_information_loss(C_minimal)
    n_sharp = solve_information_loss(C_sharp_layer2)
    n_kernel = solve_information_loss(C_layer2_kernel)

    omega = omega_eta_self_dual()
    eps_eta = eta_spectral_subtraction()
    r_kernel = r_layer2_kernel()
    C_target = solve_C_for_target_n(CODATA_ALPHA_INV)
    r_target = solve_r_eff_for_target_n(CODATA_ALPHA_INV)

    print("UBT alpha Layer2 kernel refinement reproduction")
    print("===============================================")
    print(f"B(1)                         = {mp.nstr(B_of_rho(1), 50)}")
    print(f"Omega_eta(1)                 = {mp.nstr(omega, 50)}")
    print(f"12*pi*Omega_eta(1)           = {mp.nstr(12*mp.pi*omega, 50)}")
    print(f"(pi-3)/2                     = {mp.nstr(eps_eta, 50)}")
    print(f"r_kernel = 3*(1+Omega_eta)   = {mp.nstr(r_kernel, 50)}")
    print()

    print_model("Self-dual eta-winding (rho=1)", n_self)
    print_model("Minimal four-channel information loss (C_Q=4)", n_C4, mp.mpf(4))
    print_model("Sharp Layer2 projection (r_eff=3)", n_sharp, C_sharp_layer2(n_sharp), mp.mpf(3))
    print_model("First Layer2 eta-kernel refinement", n_kernel, C_layer2_kernel(n_kernel), r_kernel)

    print("Post-check against CODATA 2022")
    print("------------------------------")
    print(f"CODATA alpha^-1               = {CODATA_ALPHA_INV}")
    print(f"CODATA sigma                  = {CODATA_SIGMA}")
    print(f"C_Q required for exact CODATA = {mp.nstr(C_target, 50)}")
    print(f"r_eff required for CODATA     = {mp.nstr(r_target, 50)}")
    print(f"r_kernel - r_target           = {mp.nstr(r_kernel-r_target, 50)}")


if __name__ == "__main__":
    main()
