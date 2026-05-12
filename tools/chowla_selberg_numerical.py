#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Numerical checks for the Chowla-Selberg / theta3 bridge in Gap G137-B."""

from __future__ import annotations

try:
    import mpmath as mp
except ModuleNotFoundError:  # pragma: no cover - environment dependent
    mp = None


def z_z2_at_1() -> "mp.mpf":
    """Compute Z_{Z^2}(1) analytic target value for square lattice."""
    return mp.pi


def z_t2_at_1(radius: "mp.mpf") -> "mp.mpf":
    """Compute Z_{T^2}(1)=Z_{Z^2}(1)/R^2 for square torus radius R."""
    return z_z2_at_1() / (radius**2)


def main() -> None:
    if mp is None:
        print("mpmath is not installed; cannot run Chowla-Selberg numeric checks.")
        return

    mp.mp.dps = 80

    # Dirichlet beta = L(s, chi_{-4})
    L0 = mp.dirichlet(0, [0, 1, 0, -1])
    z0 = mp.zeta(0)
    zp0 = mp.diff(mp.zeta, 0)
    Lp0 = mp.diff(lambda s: mp.dirichlet(s, [0, 1, 0, -1]), 0)

    zprime_z2 = 4 * (zp0 * L0 + z0 * Lp0)

    eta_i = mp.qp(mp.e ** (-2 * mp.pi), mp.e ** (-2 * mp.pi)) * mp.e ** (mp.pi / 12)
    theta3_i = mp.jtheta(3, 0, mp.e ** (-mp.pi))

    b_target = 12 ** (mp.mpf("1.5")) * 2 ** (mp.mpf("0.125")) * theta3_i ** (mp.mpf("0.25"))

    R = mp.mpf("1")
    z_z2_1 = z_z2_at_1()
    z_t2_1 = z_t2_at_1(R)

    print(f"L(0,chi_-4)             = {L0}")
    print(f"L'(0,chi_-4)            = {Lp0}")
    print(f"zeta'(0)                = {zp0}")
    print(f"Z'_Z2(0)                = {zprime_z2}")
    print(f"Z_Z2(1)                  = {z_z2_1}")
    print(f"Z_T2(1) for R=1          = {z_t2_1}")
    print(f"theta3(0|i)             = {theta3_i}")
    print(f"eta(i)                  = {eta_i}")
    print(f"theta3/eta              = {theta3_i / eta_i}")
    print(f"ln(theta3)              = {mp.log(theta3_i)}")
    print(f"B_target(theta3)        = {b_target}")


if __name__ == "__main__":
    main()
