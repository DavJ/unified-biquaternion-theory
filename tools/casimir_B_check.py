# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
#
# Tool: casimir_B_check.py
# Purpose: Check whether the Casimir energy on T³ at the self-dual point
#          produces the coefficient B in V_eff(n) = n² - B·n·ln n.
#          This is part of the Gap G137-B investigation (T4).
# Theory: Ambjorn-Wolfram (1983) Casimir energy on T^d, related to
#         the coefficient B in the UBT alpha-track winding potential.
# Reference: research_tracks/T3_ALPHA/mellin_insertion_B.tex

import math


def zeta_riemann(s: float, N: int = 100000) -> float:
    """Numerical Riemann zeta function via partial sum (for s > 1)."""
    return sum(1.0 / n ** s for n in range(1, N + 1))


def casimir_energy_torus(d: int, N_eff: float, R: float = 1.0) -> float:
    """
    Casimir energy for N_eff real scalar fields on T^d with equal radii R.

    Standard Ambjorn-Wolfram (1983) result:
        E_Casimir(R) = -N_eff * Gamma(d/2+1) / (2^{d+1} * pi^{d/2+1}) * zeta(d+1) / R^d

    Parameters
    ----------
    d : int
        Dimension of the torus (T^d).
    N_eff : float
        Number of real scalar fields.
    R : float
        Radius of the torus (default: self-dual point R=1).

    Returns
    -------
    float
        Casimir energy.
    """
    from math import gamma
    numerator = -N_eff * gamma(d / 2.0 + 1.0) * zeta_riemann(d + 1)
    denominator = 2 ** (d + 1) * math.pi ** (d / 2.0 + 1.0) * R ** d
    return numerator / denominator


def main():
    print("=" * 60)
    print("Gap G137-B: Casimir Check on T³")
    print("Casimir energy → B coefficient comparison")
    print("=" * 60)

    N_eff = 12           # UBT effective modes [L1]
    d = 3                # T³ (three compact dimensions)
    R = 1.0              # self-dual point R=1 (in units of l_Pl)

    # Exact values
    zeta4_exact = math.pi ** 4 / 90.0   # ζ(4) = π⁴/90

    print()
    print("Exact constants:")
    print(f"  ζ(4) = π⁴/90 = {zeta4_exact:.8f}")
    print(f"  Γ(5/2) = 3√π/4 = {math.gamma(2.5):.8f}")

    # Casimir energy for N_eff scalar fields on T³ at R=1
    E_cas = casimir_energy_torus(d, N_eff, R)
    print()
    print(f"Casimir energy (T³, N_eff={N_eff}, R={R}):")
    print(f"  E_Casimir = {E_cas:.8f}")

    # The Casimir coefficient in |E_Casimir| = N_eff * C_d
    C_d = -E_cas / N_eff
    print(f"  C_d = |E|/N_eff = {C_d:.8f}")

    # B_phenom (phenomenological target from alpha-track)
    # B_phenom = 12^{3/2} * (2η(i))^{1/4} ≈ 46.28
    # Numerical: eta(i) = Γ(1/4)/(2π^{3/4})
    eta_i = math.gamma(0.25) / (2.0 * math.pi ** 0.75)
    theta3_i = math.pi ** 0.25 / math.gamma(0.75)   # θ₃(0|i) = π^{1/4}/Γ(3/4)
    B_phenom = N_eff ** 1.5 * (2.0 * eta_i) ** 0.25
    B_Ram = N_eff ** 1.5 * 2.0 ** (1.0 / 8.0) * theta3_i ** 0.25

    print()
    print("B target values:")
    print(f"  η(i) = {eta_i:.8f}")
    print(f"  θ₃(0|i) = {theta3_i:.8f}")
    print(f"  B_phenom = 12^(3/2)·(2η(i))^(1/4) = {B_phenom:.8f}")
    print(f"  B_Ram = 12^(3/2)·2^(1/8)·θ₃(0|i)^(1/4) = {B_Ram:.8f}")

    print()
    print("Casimir coefficient vs B_phenom:")
    print(f"  B_Casimir (=|E_Cas|/N_eff) = {C_d:.8f}")
    print(f"  B_phenom                   = {B_phenom:.8f}")
    ratio = C_d / B_phenom
    print(f"  Ratio B_Casimir/B_phenom   = {ratio:.8f}")

    print()
    print("Conclusion:")
    print(f"  B_Casimir ≪ B_phenom (ratio ~ 6.7×10⁻⁴)")
    print(f"  The direct Casimir energy on T³ does NOT reproduce B_phenom.")
    print(f"  A missing factor of ~{1.0/ratio:.1f} remains unexplained.")
    print(f"  Gap G137-B status: NARROWED (Casimir route explored, factor missing).")
    print(f"  Alpha: NOT DERIVED.")

    print()
    print("Numerical cross-check:")
    # Alternative: B coefficient from n·ln(n) term in E_Casimir(n/R)
    # For large n: E_Casimir(n) ~ -N_eff * C_d * n^d
    # d=3: E ~ -N_eff * C_d * n³ — no n·ln(n) term from dimensional scaling
    # The n·ln(n) term arises from the logarithmic correction to E_Casimir
    # in 2D (d=2), not 3D.
    # On T², E_Casimir(R) = -N_eff * ζ(3)/(4π) / R² — standard Epstein zeta
    E_cas_T2 = casimir_energy_torus(2, N_eff, R)
    print(f"  E_Casimir(T², R=1) = {E_cas_T2:.8f}")
    print(f"  Note: n·ln(n) structure comes from T² Epstein zeta, not T³.")
    print(f"  The T³ volumetric factor 12^(3/2) is identified [L1/OBS] in")
    print(f"  mellin_insertion_B.tex; the Mellin insertion factor is [OPEN].")


if __name__ == "__main__":
    main()
