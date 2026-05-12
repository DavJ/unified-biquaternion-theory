#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Self-consistent numerical solution for R_psi*, M_GUT, T_kin in UBT.

Solves the three-equation system from
research_tracks/EW/rpsi_from_action.tex §Step 5:

    R_psi* = sqrt(N_eff / (48*pi*T_kin))          [stationarity of S_eff]
    M_GUT  = 1 / R_psi*                           [definition]
    T_kin  = g^2 * M_GUT^4 / (16*pi^2)           [loop-suppressed ansatz]

All quantities in Planck units (M_Pl = 1).
Physical conversion: M_Pl = 1.220e19 GeV.
"""

from __future__ import annotations

import math


def analytic_mgut(g: float = 0.6, n_eff: int = 12) -> float:
    """Analytic GUT scale from the self-consistent system (Planck units).

    Derived in rpsi_from_action.tex §Step 5 Eq. (mgut_analytic):
        M_GUT = sqrt(N_eff * pi / (3 * g^2))
    """
    return math.sqrt(n_eff * math.pi / (3.0 * g**2))


def solve_self_consistent(
    g: float = 0.6,
    n_eff: int = 12,
    m_pl_gev: float = 1.220e19,
) -> tuple[float, float, float]:
    """Return (R_psi_star, M_GUT_planck, T_kin_planck) self-consistently.

    Parameters
    ----------
    g : float
        Gauge coupling at GUT scale (~0.6 in SM).
    n_eff : int
        Effective mode count from SU(2)-twist theorem [L1].
    m_pl_gev : float
        Planck mass in GeV for physical conversion.

    Returns
    -------
    tuple of (R_psi_star, M_GUT_planck, T_kin_planck) all in Planck units.
    """
    try:
        from scipy.optimize import fsolve  # type: ignore[import-untyped]

        def equations(vars: list[float]) -> list[float]:
            r, m_gut, t_kin = vars
            eq1 = r - math.sqrt(n_eff / (48.0 * math.pi * t_kin))
            eq2 = m_gut - 1.0 / r
            eq3 = t_kin - g**2 * m_gut**4 / (16.0 * math.pi**2)
            return [eq1, eq2, eq3]

        # Initial guess: analytic result
        m_gut0 = analytic_mgut(g, n_eff)
        r0 = 1.0 / m_gut0
        t_kin0 = g**2 * m_gut0**4 / (16.0 * math.pi**2)
        sol = fsolve(equations, [r0, m_gut0, t_kin0], full_output=False)
        r_star, m_gut_planck, t_kin_planck = sol[0], sol[1], sol[2]
    except ImportError:
        # Fallback: pure analytic formula (exact for this system)
        m_gut_planck = analytic_mgut(g, n_eff)
        r_star = 1.0 / m_gut_planck
        t_kin_planck = g**2 * m_gut_planck**4 / (16.0 * math.pi**2)

    return r_star, m_gut_planck, t_kin_planck


def main() -> None:
    m_pl_gev = 1.220e19  # GeV
    gut_target_gev = 2.0e16  # standard GUT window

    r_star, m_gut_planck, t_kin_planck = solve_self_consistent()
    m_gut_gev = m_gut_planck * m_pl_gev
    ratio = m_gut_gev / gut_target_gev

    print("=== Self-consistent R_psi*/M_GUT/T_kin solution (rpsi_from_action.tex §Step 5) ===")
    print(f"N_eff = 12 [L1], g = 0.6")
    print()
    print(f"R_psi*       = {r_star:.6f}  (Planck units = l_Pl)")
    print(f"M_GUT        = {m_gut_planck:.6f}  M_Pl")
    print(f"M_GUT        = {m_gut_gev:.3e}  GeV")
    print(f"T_kin        = {t_kin_planck:.6e}  M_Pl^4")
    print()
    print(f"Target GUT scale: {gut_target_gev:.1e} GeV")
    print(f"Ratio M_GUT / (2e16 GeV) = {ratio:.1f}  [FACTOR TOO LARGE: ~{ratio:.0f}x]")
    print()

    # Analytic check
    m_gut_analytic = analytic_mgut()
    print(f"Analytic M_GUT = sqrt(N_eff*pi/(3*g^2)) = {m_gut_analytic:.6f}  M_Pl")
    print(f"Matches numerical:  {abs(m_gut_planck - m_gut_analytic) < 1e-6}")
    print()
    print("=== Diagnosis ===")
    print("Self-consistent system yields M_GUT ~ 5.9 M_Pl >> 2e16 GeV.")
    print("The loop-suppressed T_kin ansatz does NOT fix M_GUT at GUT scale.")
    print("Additional suppression needed: ~(2e16/7.2e19)^2 ~ 1e-7 in T_kin.")
    print("sin^2(theta_W)(M_Z) = 0.231: [CONDITIONAL — scale modulus still OPEN]")
    print("Alpha: NOT DERIVED")


if __name__ == "__main__":
    main()
