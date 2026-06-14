#!/usr/bin/env python3
"""Reproduce the final G137-B bridge-level closure numbers."""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 80


def eta_i(rho: mp.mpf) -> mp.mpf:
    q = mp.e ** (-2 * mp.pi * rho)
    return q ** (mp.mpf(1) / 24) * mp.nprod(lambda k: 1 - q**k, [1, mp.inf])


def z_compact(rho: mp.mpf) -> mp.mpf:
    q = mp.e ** (-mp.pi * rho)
    eta = eta_i(rho)
    return mp.jtheta(2, 0, q) * mp.jtheta(3, 0, q) * mp.jtheta(4, 0, q) / eta**2


def B_of_rho(rho: mp.mpf) -> mp.mpf:
    return mp.mpf(12) ** (mp.mpf(3) / 2) * z_compact(rho) ** (mp.mpf(1) / 4)


def root_self_dual() -> mp.mpf:
    B = B_of_rho(mp.mpf(1))
    return mp.findroot(lambda n: 2*n/(mp.log(n)+1)-B, 137)


def main() -> None:
    rho = mp.mpf(1)
    z = z_compact(rho)
    eta = eta_i(rho)
    B = B_of_rho(rho)
    n0 = root_self_dual()
    print("G137-B final bridge closure check")
    print("=================================")
    print(f"Z_compact(i) = theta2 theta3 theta4 / eta^2 = {mp.nstr(z, 60)}")
    print(f"2 eta(i)                                     = {mp.nstr(2*eta, 60)}")
    print(f"difference                                   = {mp.nstr(z-2*eta, 30)}")
    print(f"B(1) = 12^(3/2) Z_compact(i)^(1/4)           = {mp.nstr(B, 60)}")
    print(f"self-dual root                               = {mp.nstr(n0, 60)}")
    print()
    print("Status")
    print("------")
    print("G137-B is closed at bridge level if the compact Layer2 spin-structure")
    print("measure and the four-channel geometric mean are accepted as canonical.")


if __name__ == "__main__":
    main()
