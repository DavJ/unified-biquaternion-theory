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


def eta_at_i_real() -> "mp.mpf":
    """Return the real Dedekind eta value at tau=i with consistency check."""
    eta_i_complex = mp.eta(mp.mpc(0, 1))
    assert float(mp.im(eta_i_complex)) < 1e-40, (
        f"Unexpected imaginary part in eta(i): {mp.im(eta_i_complex)}"
    )
    return mp.re(eta_i_complex)


def check_theta2_ns_identity() -> None:
    """Verify Ramanujan CM identities and NS sector values at tau=i.

    Checks:
    1. Correct Ramanujan CM identity: theta3(0|i) = sqrt(2)*eta(i)  [STD, alpha20]
    2. NS sector value: Z_NS(i) = theta2(0|i)/eta(i) ≈ 1.189 (NOT sqrt(2))
    3. Z_1real = 2*eta(i) as normalization candidate [OBS]
    4. B = 12^(3/2)*(2*eta(i))^(1/4) numerically [OBS]

    See chowla_selberg_B_derivation.tex §5 for the LaTeX discussion.
    """
    if mp is None:
        print("mpmath is not installed; cannot run NS identity check.")
        return

    mp.mp.dps = 50
    # nome q = e^{i*pi*tau}; for tau=i: q = e^{-pi}
    q_nome = mp.exp(-mp.pi)

    theta2_i = mp.jtheta(2, 0, q_nome)
    theta3_i = mp.jtheta(3, 0, q_nome)
    eta_i = eta_at_i_real()   # eta(i) is real-valued

    sqrt2_eta_i = mp.sqrt(2) * eta_i

    # Correct Ramanujan CM identity: theta3 = sqrt(2)*eta
    theta3_matches = abs(float(theta3_i) - float(sqrt2_eta_i)) < 1e-10
    # Z_NS = theta2/eta (NS sector formula)
    z_ns_i = float(theta2_i) / float(eta_i)

    z_1real_i = 2 * float(eta_i)              # Z_1real = 2*eta(i) [OBS candidate]
    b_ns = 12 ** 1.5 * z_1real_i ** 0.25

    print("=== Ramanujan CM identity and NS sector check (chowla_selberg_B_derivation.tex §5) ===")
    print(f"theta2(0|i)              = {float(theta2_i):.15f}")
    print(f"theta3(0|i)              = {float(theta3_i):.15f}")
    print(f"eta(i)                   = {float(eta_i):.15f}")
    print(f"sqrt(2)*eta(i)           = {float(sqrt2_eta_i):.15f}")
    print()
    print(f"CORRECT identity: theta3(0|i) = sqrt(2)*eta(i)?  {theta3_matches}  [STD, alpha20]")
    print(f"WRONG claim:      theta2(0|i) = sqrt(2)*eta(i)?  "
          f"{abs(float(theta2_i) - float(sqrt2_eta_i)) < 1e-10}  [CORRECTED in tex]")
    print()
    print(f"Z_NS(i) = theta2(0|i)/eta(i) = {z_ns_i:.15f}  (expected ~1.189, NOT sqrt(2))")
    print(f"sqrt(2)                      = {float(mp.sqrt(2)):.15f}")
    print()
    print(f"Z_1real = 2*eta(i)       = {z_1real_i:.15f}  [OBS candidate, not derived]")
    print(f"(Z_1real)^(1/4)          = {z_1real_i ** 0.25:.15f}")
    print(f"B = 12^(3/2)*(2*eta(i))^(1/4) = {b_ns:.15f}  [OBS]")
    print(f"B_phenom                 ≈ 46.298")
    print(f"Deviation from B_phenom  ≈ {abs(b_ns - 46.298):.4f}")


def check_z2_orbifold_candidate() -> None:
    """Check the Z2-orbifold candidate factor used in Gap G137-B discussions."""
    if mp is None:
        print("mpmath is not installed; cannot run Z2-orbifold check.")
        return

    mp.mp.dps = 50
    q_nome = mp.exp(-mp.pi)

    theta3_i = mp.jtheta(3, 0, q_nome)
    theta4_i = mp.jtheta(4, 0, q_nome)
    eta_i = eta_at_i_real()

    z_orb = (theta3_i + theta4_i) / (2 * eta_i)
    sqrt2 = mp.sqrt(2)

    b_orb = 12 ** 1.5 * float(z_orb) ** 0.25
    b_req = 2 * 137 / (mp.log(137) + 1)
    b_orb_theta3 = 12 ** 1.5 * float(z_orb * theta3_i) ** 0.25
    b_2eta = 12 ** 1.5 * float(2 * eta_i) ** 0.25

    print()
    print("=== Z2-orbifold candidate check (Gap G137-B) ===")
    print(f"theta3(0|i)                = {float(theta3_i):.15f}")
    print(f"theta4(0|i)                = {float(theta4_i):.15f}")
    print(f"eta(i)                     = {float(eta_i):.15f}")
    print(f"Z_orb = (theta3+theta4)/(2eta) = {float(z_orb):.15f}")
    print(f"sqrt(2)                    = {float(sqrt2):.15f}")
    print(f"Match sqrt(2)?             = {abs(float(z_orb) - float(sqrt2)) < 1e-10}")
    print()
    print(f"B_orb = 12^(3/2)*Z_orb^(1/4)          = {float(b_orb):.15f}")
    print(f"B_req = 2*137/(ln(137)+1)             = {float(b_req):.15f}")
    print(f"Relative error (%)                    = "
          f"{abs(float(b_orb) - float(b_req)) / float(b_req) * 100:.6f}")
    print(f"B_orb_theta3 = 12^(3/2)*(Z_orb*theta3)^(1/4) = {float(b_orb_theta3):.15f}")
    print(f"B_2eta       = 12^(3/2)*(2eta)^(1/4)         = {float(b_2eta):.15f}")


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

    eta_i = eta_at_i_real()
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
    print()
    check_theta2_ns_identity()
    check_z2_orbifold_candidate()


if __name__ == "__main__":
    main()
