# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
#
# Tool: delta_neff_calc.py
# Purpose: Compute ΔN_eff contribution from UBT Kaluza-Klein sector
#          decoupled at T ~ M_Pl. Used in T3 prediction card.
# Theory: Standard cosmological relic formula for light relics.
#         Delta N_eff = N_X * (43/(4 * g_*(T_dec)))^{4/3}
#         where g_*(T_dec) = SM d.o.f. at decoupling temperature.
# Reference: research_tracks/quantum_ubt/delta_neff_prediction.tex

import math

def compute_delta_neff(N_eff_KK: float, g_star_dec: float) -> float:
    """
    Compute ΔN_eff from KK modes decoupled at temperature T_dec.

    Standard cosmological formula for an extra species that decoupled
    in radiation domination at temperature T_dec:
        ΔN_eff = N_X × (43 / (4 g_*(T_dec)))^{4/3}

    This counts each bosonic degree of freedom as one unit.
    The factor 43/4 = 2 + (7/8)*6 = photons + three SM neutrino species.

    Parameters
    ----------
    N_eff_KK : float
        Number of effective KK bosonic degrees of freedom.
    g_star_dec : float
        Effective relativistic d.o.f. at decoupling (g_*(T_dec)).

    Returns
    -------
    float
        ΔN_eff contribution.
    """
    return N_eff_KK * (43.0 / (4.0 * g_star_dec)) ** (4.0 / 3.0)


def main():
    print("=" * 60)
    print("UBT ΔN_eff Calculation — T3 Prediction")
    print("=" * 60)

    # --- Parameters ---
    N_eff_KK = 12        # UBT KK modes from SU(2) twist [L1]
    g_star_SM = 106.75   # SM d.o.f. at T ~ 100 GeV (standard value)
    #   = 2(photon) + 3*2(W,Z) + 8*2*2(gluons) + 4(Higgs) + 3*2*2*2(quarks)*3 + 3*2*2(leptons)
    #   = 2 + 12 + 64 + 4 + 72 + 12 = 166 for scalars?  standard is 106.75 bosons+fermions

    # g_* = 106.75 is the standard result for the SM at T > 100 GeV:
    # bosons: photon(2) + W±,Z(9) + gluons(16) + Higgs(1) = 28
    # fermions: quarks 6*2*3*2 = 72, leptons 3*2*2=12; (7/8)*84 = 73.5
    # total: 28 + 73.5 ≈ 106.75 (standard textbook value)

    CMB_S4_sensitivity = 0.03   # CMB-S4 target σ(ΔN_eff)
    Planck_ACT_bound = 0.28     # Planck+ACT 2024 (95% CL upper bound on extra ΔN_eff)

    print()
    print("Parameters:")
    print(f"  N_eff_KK (SU(2) twist [L1])  = {N_eff_KK}")
    print(f"  g_*(T_dec) ~ g_*(T_Pl) (SM)  = {g_star_SM}")
    print()

    # Per-mode contribution
    delta_per_mode = compute_delta_neff(1.0, g_star_SM)
    print(f"ΔN_eff per KK mode           = {delta_per_mode:.6f}")

    # Total from all N_eff_KK = 12 modes
    delta_total = compute_delta_neff(N_eff_KK, g_star_SM)
    print(f"ΔN_eff (N_KK=12 modes total) = {delta_total:.6f}")

    print()
    print("Observational context:")
    print(f"  CMB-S4 sensitivity           : σ ~ {CMB_S4_sensitivity}")
    print(f"  Planck+ACT bound (95% CL)    : ΔN_eff < {Planck_ACT_bound}")
    print()
    print("Assessment:")
    print(f"  Per-mode ({delta_per_mode:.4f}) > CMB-S4 ({CMB_S4_sensitivity}): "
          f"{'YES — detectable per mode' if delta_per_mode > CMB_S4_sensitivity else 'NO'}")
    print(f"  Total ({delta_total:.4f}) > CMB-S4 ({CMB_S4_sensitivity}):    "
          f"{'YES' if delta_total > CMB_S4_sensitivity else 'NO'}")
    print(f"  Total ({delta_total:.4f}) < Planck ({Planck_ACT_bound}):    "
          f"{'YES — consistent' if delta_total < Planck_ACT_bound else 'NO — TENSION with current data'}")

    print()
    print("Note: 0.046 value in STATUS_OF_UBT.md corresponds to per-mode result.")
    print("      Total from 12 modes is ~0.562; this exceeds current Planck+ACT")
    print("      bound and requires further analysis (see tex file for caveat).")

    print()
    print("Fail criterion:")
    print("  ΔN_eff < 0 or ΔN_eff > 1 would falsify the UBT KK sector.")

    return delta_per_mode, delta_total


if __name__ == "__main__":
    delta_per_mode, delta_total = main()
