#!/usr/bin/env python3
"""Check A1 complete spin-structure trace identity."""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 60


def eta_i(rho: mp.mpf) -> mp.mpf:
    q = mp.e ** (-2 * mp.pi * rho)
    return q ** (mp.mpf(1)/24) * mp.nprod(lambda k: 1 - q**k, [1, mp.inf])


def main() -> None:
    print("A1 complete spin-structure trace check")
    print("=======================================")
    for rho in [mp.mpf("0.9"), mp.mpf("1.0"), mp.mpf("1.1")]:
        q = mp.e ** (-mp.pi*rho)
        eta = eta_i(rho)
        th2 = mp.jtheta(2, 0, q)
        th3 = mp.jtheta(3, 0, q)
        th4 = mp.jtheta(4, 0, q)
        z = th2*th3*th4/eta**2
        print(f"rho={rho}: Z=theta2 theta3 theta4 / eta^2 = {mp.nstr(z, 40)}")
        print(f"         2 eta                         = {mp.nstr(2*eta, 40)}")
        print(f"         diff                          = {mp.nstr(z-2*eta, 20)}")
    print("\nA1 checks the algebraic identity. The physics audit concerns why UBT's")
    print("Layer2 compact trace must include the complete theta2/theta3/theta4 product.")


if __name__ == "__main__":
    main()
