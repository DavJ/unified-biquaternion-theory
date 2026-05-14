# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
ubt_dark_radiation.py — UBT Dark Radiation and ΔN_eff estimation.

Estimates the contribution of massless Θ-field zero modes to the
effective neutrino number N_eff.

Physical derivation (no curve fitting)
---------------------------------------
The standard radiation energy density formula:

    ρ_rad = ρ_γ [1 + (7/8)(4/11)^{4/3} N_eff]

For a new bosonic species X with g_X internal DoF that decoupled from
the SM thermal bath at temperature T_D >> T_BBN, its contribution is:

    ΔN_eff = (8/7) × (11/4)^{4/3} × (g_X / 2) × (T_X / T_γ)^4

where the temperature ratio at late times is determined by entropy
conservation:

    T_X / T_γ = [g_{*S}(T_γ,0) / g_{*S}(T_D)]^{1/3}

Here:
    g_{*S}(T_γ,0) = 2   (photons only after e+e- annihilation)
    g_{*S}(T_ν^-)  = 10.75  (photons + e+e- + 3ν flavors at T ~ 2 MeV)

The ratio T_X / T_ν accounts for the neutrino temperature:
    T_ν = (4/11)^{1/3} T_γ  (after e+e- annihilation)

So:
    T_X / T_ν = (T_X / T_γ) / (T_ν / T_γ) = (T_X / T_γ) × (11/4)^{1/3}

For UBT Θ zero modes:
    g_X = N_THETA_DOF = 8  (8 real biquaternion components, each has a zero mode)
    (or conservatively g_X = 2 for a single complex scalar zero mode)

Reproducibility
---------------
All constants are from PDG/Planck 2018; no parameter fitting.

Run:
    python simulations/cosmology_models/ubt_dark_radiation.py

References:
    UBT_v28_cosmo_hecke_neff (this task)
    Kolb & Turner, "The Early Universe" (1990)
    Planck 2018 results VI, arXiv:1807.06209
"""

from __future__ import annotations

import math

# ---------------------------------------------------------------------------
# Physical constants (PDG 2022)
# ---------------------------------------------------------------------------

# Standard Model effective relativistic DoF at key temperatures
# Source: Kolb & Turner Table 3.1; Mangano et al. arXiv:hep-ph/0512250
G_STAR_TABLE = {
    # T [GeV] : g_*S (entropy DoF)
    1e4:   110.75,   # T >> EW scale (all SM)
    1e3:   106.75,   # T > EW phase transition
    1e2:   106.75,   # 100 GeV — full SM
    50.0:   96.25,   # top quark has decoupled
    10.0:   86.25,
    5.0:    75.75,   # b quark threshold
    2.0:    61.75,   # c quark, gluons still present
    1.0:    61.75,
    0.5:    17.25,   # QCD transition complete
    0.15:   17.25,   # just after QCD
    0.10:   10.75,   # pion threshold
    0.01:   10.75,   # below pion: photon + e + 3nu
    0.001:  10.75,   # ~ MeV scale
    2e-3:   10.75,   # just before nu decoupling
    1e-3:    3.91,   # after nu decoupling (photon + e+e-)
    5e-4:    2.00,   # after e+e- annihilation (photons only)
}

G_STAR_NU_DECOUPLING  = 10.75   # g_*S at neutrino decoupling (~2 MeV)
G_STAR_PHOTON_ONLY    = 2.0     # g_*S after e+e- annihilation (photons only)

# (4/11)^{1/3}: neutrino temperature ratio after e+e- annihilation
T_NU_OVER_T_GAMMA = (4.0 / 11.0) ** (1.0 / 3.0)

# UBT Θ field degrees of freedom
N_THETA_DOF_FULL        = 8   # 8 real DoF (full biquaternion)
N_THETA_DOF_SINGLE_MODE = 1   # conservative: one real massless scalar zero mode
N_THETA_DOF_COMPLEX     = 2   # single complex massless scalar


def delta_neff_from_light_boson(g_X: float, g_star_decoupling: float) -> float:
    """
    Compute ΔN_eff for g_X bosonic DoF decoupled at g_star_decoupling.

    Formula (derivation in docstring above):
        T_X / T_γ  = (g_star_photon / g_star_decoupling)^{1/3}
        T_X / T_ν  = (T_X / T_γ) × (11/4)^{1/3}
        ΔN_eff     = (8/7) × (11/4)^{4/3} × (g_X / 2) × (T_X / T_γ)^4

    Parameters
    ----------
    g_X : float
        Number of bosonic DoF of the new light species.
    g_star_decoupling : float
        Effective entropic DoF at decoupling temperature T_D.

    Returns
    -------
    float : ΔN_eff contribution
    """
    # Temperature ratio at late times (after e+e- annihilation)
    T_X_over_T_gamma = (G_STAR_PHOTON_ONLY / g_star_decoupling) ** (1.0 / 3.0)
    T_X_over_T_nu    = T_X_over_T_gamma / T_NU_OVER_T_GAMMA  # = T_X_over_T_gamma × (11/4)^{1/3}

    # Energy density of X relative to photons
    # For a boson: rho_X = (pi^2/30) g_X T_X^4
    # For photons: rho_gamma = (pi^2/30) × 2 × T_gamma^4
    rho_X_over_rho_gamma = (g_X / 2.0) * T_X_over_T_gamma**4

    # Convert to ΔN_eff using  rho_X = (7/8)(4/11)^{4/3} ΔN_eff × rho_gamma
    delta_neff = rho_X_over_rho_gamma / ((7.0 / 8.0) * (4.0 / 11.0)**(4.0 / 3.0))

    return delta_neff


def scan_decoupling_temperatures() -> list:
    """
    Scan ΔN_eff as a function of decoupling temperature T_D for UBT Θ modes.

    Returns list of dicts with T_D, g_star, delta_neff_single, delta_neff_full.
    """
    rows = []
    # Representative decoupling temperatures [GeV]
    T_D_values = [1e4, 1e3, 1e2, 2.0, 0.5, 0.15, 0.01, 2e-3]

    for T_D in T_D_values:
        # Find the nearest g_*S in our table
        g_star = _lookup_gstar(T_D)

        dn_single = delta_neff_from_light_boson(g_X=N_THETA_DOF_SINGLE_MODE,
                                                g_star_decoupling=g_star)
        dn_complex = delta_neff_from_light_boson(g_X=N_THETA_DOF_COMPLEX,
                                                  g_star_decoupling=g_star)
        dn_full = delta_neff_from_light_boson(g_X=N_THETA_DOF_FULL,
                                               g_star_decoupling=g_star)

        rows.append({
            'T_D_GeV':      T_D,
            'g_star_S':     g_star,
            'dN_single':    dn_single,
            'dN_complex':   dn_complex,
            'dN_full':      dn_full,
            'T_X_over_Tnu': (G_STAR_PHOTON_ONLY / g_star)**(1.0/3.0) / T_NU_OVER_T_GAMMA,
        })

    return rows


def _lookup_gstar(T_GeV: float) -> float:
    """Return g_*S for temperature T [GeV] from lookup table."""
    temps = sorted(G_STAR_TABLE.keys(), reverse=True)
    for T_key in temps:
        if T_GeV >= T_key:
            return G_STAR_TABLE[T_key]
    return G_STAR_TABLE[min(G_STAR_TABLE.keys())]


def rho_rad_formula(rho_gamma: float, N_eff: float) -> float:
    """
    Total radiation energy density from the standard formula.

        rho_rad = rho_gamma × [1 + (7/8)(4/11)^{4/3} N_eff]

    Parameters
    ----------
    rho_gamma : float  (any units)
    N_eff : float

    Returns
    -------
    float : rho_rad in same units as rho_gamma
    """
    return rho_gamma * (1.0 + (7.0 / 8.0) * (4.0 / 11.0)**(4.0 / 3.0) * N_eff)


def run_estimation(verbose: bool = True) -> dict:
    """
    Run the full ΔN_eff estimation and return results dict.
    """
    rows = scan_decoupling_temperatures()

    # Best-estimate scenario: Θ zero modes decouple at T_D ~ 1 GeV
    # (after confinement of UBT sector but before QCD transition)
    # Using g_star = 61.75 (quarks still relativistic)
    g_star_best = 61.75
    T_D_best    = 2.0   # GeV

    dn_best_single  = delta_neff_from_light_boson(N_THETA_DOF_SINGLE_MODE, g_star_best)
    dn_best_complex = delta_neff_from_light_boson(N_THETA_DOF_COMPLEX,     g_star_best)
    dn_best_full    = delta_neff_from_light_boson(N_THETA_DOF_FULL,        g_star_best)

    # Standard N_eff (SM prediction)
    N_eff_SM = 3.044   # from Cielo et al., Phys.Rev.Lett. 2023

    # Total with UBT contribution (single complex zero mode)
    N_eff_UBT = N_eff_SM + dn_best_complex

    results = {
        'scan': rows,
        'T_D_best_GeV':      T_D_best,
        'g_star_best':       g_star_best,
        'dN_best_single':    dn_best_single,
        'dN_best_complex':   dn_best_complex,
        'dN_best_full':      dn_best_full,
        'N_eff_SM':          N_eff_SM,
        'N_eff_UBT_central': N_eff_UBT,
        'target_sensitivity': 0.03,
        'detectable':        dn_best_complex >= 0.03,
    }

    if verbose:
        _print_report(results)

    return results


def _print_report(results: dict) -> None:
    sep = "=" * 72
    print(sep)
    print("UBT DARK RADIATION  —  Delta N_eff ESTIMATION  (v28)")
    print(sep)
    print()
    print("Formula:  rho_rad = rho_gamma × [1 + (7/8)(4/11)^{4/3} N_eff]")
    print()

    print("Scan over decoupling temperatures:")
    print(f"  {'T_D [GeV]':>12}  {'g*S':>6}  {'dN(1 real)':>12}  "
          f"{'dN(complex)':>12}  {'dN(full Theta)':>14}")
    print("  " + "-" * 66)
    for row in results['scan']:
        print(f"  {row['T_D_GeV']:>12.2e}  {row['g_star_S']:>6.2f}  "
              f"{row['dN_single']:>12.4f}  {row['dN_complex']:>12.4f}  "
              f"{row['dN_full']:>14.4f}")
    print()

    print("Best estimate (T_D = {:.1f} GeV, g*S = {:.2f}):".format(
        results['T_D_best_GeV'], results['g_star_best']))
    print(f"  Delta N_eff (1 real scalar)   = {results['dN_best_single']:.5f}")
    print(f"  Delta N_eff (complex scalar)  = {results['dN_best_complex']:.5f}")
    print(f"  Delta N_eff (full Theta, 8dof)= {results['dN_best_full']:.5f}")
    print()
    print(f"  SM N_eff (Cielo+2023)         = {results['N_eff_SM']:.4f}")
    print(f"  N_eff(UBT) central estimate   = {results['N_eff_UBT_central']:.4f}")
    print()

    detectable = results['detectable']
    print(f"  Target sensitivity (CMB-S4):  Delta N_eff >= {results['target_sensitivity']:.2f}")
    print(f"  Detectable (complex mode)?    {'YES' if detectable else 'NO (below threshold)'}")
    print()
    print(sep)


if __name__ == '__main__':
    run_estimation(verbose=True)
