# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
ubt_cmb_cl.py
=============
CMB angular power spectrum C_l from UBT primordial power spectrum.

Converts the UBT-modified primordial spectrum P_UBT(k) to the CMB
temperature (TT) angular power spectrum C_l using the standard
transfer function formalism.

Theory
------
The CMB angular power spectrum is:

    C_l = (2/π) ∫ dk k² P(k) [Δ_l^T(k)]²

where Δ_l^T(k) is the radiation transfer function (temperature).

In the Sachs-Wolfe approximation (valid for l ≤ 10, large scales):

    Δ_l^T(k) ≈ j_l(k η_0) / 3

where j_l is the spherical Bessel function and η_0 is the conformal
distance to the last scattering surface (~14 Gpc in ΛCDM).

For UBT:
    C_l^UBT = (2/π) ∫ dk k² P_UBT(k) [Δ_l^T(k)]²

The ratio C_l^UBT / C_l^ΛCDM ≈ F̄_ψ(k_l) where k_l ~ l/η_0 is the
characteristic wavenumber corresponding to multipole l and F̄_ψ is
the ψ-compactification correction averaged over the transfer function.

Focus: Low-l anomaly
--------------------
The Planck 2018 data shows suppression of power at l=2,3 relative to
ΛCDM predictions.  This script tests whether UBT Scenario B/C
(R_ψ ~ Hubble scale) predicts comparable suppression.

Planck 2018 low-l values (Planck Collaboration 2018, Table 1,
l(l+1)C_l/(2π) in μK²):
    l=2:  Planck ≈ 1160,   ΛCDM best-fit ≈ 1800   (ratio ~ 0.64)
    l=3:  Planck ≈ 1060,   ΛCDM best-fit ≈ 1480   (ratio ~ 0.72)
    l=4:  Planck ≈ 1060,   ΛCDM best-fit ≈ 1560   (ratio ~ 0.68)
These are approximate values from the literature; exact values require
Planck data files.

Usage
-----
    python ubt_cmb_cl.py

Outputs C_l comparison table and JSON summary.

Note on precision
-----------------
This implementation uses the Sachs-Wolfe approximation and is
APPROXIMATE for illustrative purposes.  A precise calculation requires
a Boltzmann code (CAMB or CLASS) with the UBT primordial spectrum as
input.  See docs/predictions/cmb_prediction.md for the falsifiable
prediction derived from these approximate results.
"""

from __future__ import annotations

import math
import json
from pathlib import Path
from typing import Dict, List, Tuple

# Import from the companion script in the same directory
import sys
_here = Path(__file__).parent
sys.path.insert(0, str(_here))
from ubt_primordial_spectrum import (
    ubt_spectrum,
    standard_spectrum,
    f_psi,
    HUBBLE_LENGTH_MPC,
    K_HUBBLE_MPC,
)


# ---------------------------------------------------------------------------
# ΛCDM and cosmological parameters
# ---------------------------------------------------------------------------

# Conformal distance to last scattering surface (η_0 in Mpc)
ETA_0_MPC = 14000.0   # ~ 14 Gpc = 14000 Mpc (comoving distance to CMB)

# Matter-radiation equality wavenumber (sets scale where T(k) starts falling)
# k_eq ~ 0.015 Mpc^-1 (Planck 2018)
K_EQ_MPC = 0.015   # Mpc^-1

# Planck 2018 approximate low-l C_l values (l(l+1)C_l/2π, μK²)
# Source: Planck Collaboration 2018 (arXiv:1807.06205), Figure 1
# These are approximate values read from the published figure.
PLANCK_2018_LOW_L = {
    2:  {"observed": 1160.0, "lcdm_bestfit": 1800.0},
    3:  {"observed": 1060.0, "lcdm_bestfit": 1480.0},
    4:  {"observed": 1060.0, "lcdm_bestfit": 1560.0},
    5:  {"observed": 1500.0, "lcdm_bestfit": 1600.0},
    6:  {"observed": 1700.0, "lcdm_bestfit": 1780.0},
    10: {"observed": 2300.0, "lcdm_bestfit": 2400.0},
}


# ---------------------------------------------------------------------------
# Spherical Bessel function j_l(x)
# ---------------------------------------------------------------------------

def _jl_recurrence(l_max: int, x: float) -> List[float]:
    """
    Compute j_l(x) for l = 0, 1, ..., l_max by upward recurrence.

    j_0(x) = sin(x)/x
    j_1(x) = sin(x)/x² - cos(x)/x
    j_{l+1}(x) = (2l+1)/x * j_l(x) - j_{l-1}(x)

    Returns list of length l_max+1.
    """
    if x < 1e-10:
        # j_0(0) = 1, j_l(0) = 0 for l > 0
        result = [0.0] * (l_max + 1)
        result[0] = 1.0
        return result

    j = [0.0] * (l_max + 1)
    j[0] = math.sin(x) / x
    if l_max >= 1:
        j[1] = math.sin(x) / (x * x) - math.cos(x) / x
    for ll in range(1, l_max):
        j[ll + 1] = (2 * ll + 1) / x * j[ll] - j[ll - 1]
    return j


def matter_transfer(k: float) -> float:
    """
    Simplified matter transfer function T(k).

    Accounts for suppression of sub-equality-scale perturbations.
    Uses a simplified fitting formula:

        T(k) = 1 / (1 + (k/k_eq)^4)^(1/2)

    where k_eq ~ 0.015 Mpc^-1 is the equality wavenumber.

    For k << k_eq: T(k) ≈ 1 (large-scale modes unaffected)
    For k >> k_eq: T(k) ≈ (k_eq/k)^2 (Meszaros suppression)

    This is essential for the CMB C_l integral to converge properly:
    without T(k), the SW integral is dominated by k >> k_eq modes
    that are unphysically large.
    """
    x = k / K_EQ_MPC
    return 1.0 / math.sqrt(1.0 + x ** 4)



def spherical_bessel(l: int, x: float) -> float:
    """Return j_l(x)."""
    return _jl_recurrence(l, x)[l]




# ---------------------------------------------------------------------------
# C_l computation (Sachs-Wolfe approximation)
# ---------------------------------------------------------------------------

def compute_cl_sw(
    l: int,
    r_psi_mpc: float,
    k_min: float = 1e-5,
    k_max: float = 0.1,
    n_points: int = 300,
) -> Tuple[float, float]:
    """
    Compute C_l^UBT and C_l^ΛCDM in the Sachs-Wolfe approximation
    with a simplified matter transfer function.

    C_l = (2/π) ∫ dk k² P(k) T²(k) [j_l(k η_0) / 3]²

    where T(k) = 1/sqrt(1 + (k/k_eq)^4) suppresses sub-equality modes
    to prevent the integral from being dominated by high-k oscillatory
    tails of j_l (which are unphysical in the real CMB).

    Parameters
    ----------
    l          : multipole moment
    r_psi_mpc  : R_ψ in Mpc (for UBT spectrum)
    k_min      : minimum wavenumber for integration (Mpc^-1)
    k_max      : maximum wavenumber for integration (Mpc^-1)
    n_points   : number of integration points

    Returns
    -------
    (C_l_ubt, C_l_lcdm) in arbitrary units (same normalisation)
    """
    # Logarithmic grid in k
    log_k_min = math.log(k_min)
    log_k_max = math.log(k_max)
    d_log_k = (log_k_max - log_k_min) / (n_points - 1)

    cl_ubt = 0.0
    cl_lcdm = 0.0

    for i in range(n_points):
        log_k = log_k_min + i * d_log_k
        k = math.exp(log_k)
        jl = spherical_bessel(l, k * ETA_0_MPC)
        tk = matter_transfer(k)
        transfer_sq = (jl * tk / 3.0) ** 2

        p_ubt = ubt_spectrum(k, r_psi_mpc)
        p_std = standard_spectrum(k)

        # Integrand: (2/π) k² P(k) T²(k) [j_l(k η_0) / 3]² dk
        # On log grid: dk = k d(log k)
        integrand_ubt = k * k * p_ubt * transfer_sq * k * d_log_k
        integrand_std = k * k * p_std * transfer_sq * k * d_log_k

        cl_ubt += integrand_ubt
        cl_lcdm += integrand_std

    cl_ubt *= 2.0 / math.pi
    cl_lcdm *= 2.0 / math.pi
    return cl_ubt, cl_lcdm


def cl_to_dl(l: int, cl: float) -> float:
    """Convert C_l to D_l = l(l+1)C_l/(2π)."""
    return l * (l + 1) * cl / (2.0 * math.pi)


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------

def analyse_low_l(
    l_values: List[int],
    r_psi_mpc: float,
    scenario_name: str,
) -> Dict:
    """
    Compute C_l^UBT / C_l^ΛCDM for given R_ψ and compare with Planck 2018.

    Returns dict with results for each l.
    """
    results = {}
    for l in l_values:
        cl_ubt, cl_lcdm = compute_cl_sw(l, r_psi_mpc)
        if cl_lcdm > 0:
            ratio = cl_ubt / cl_lcdm
        else:
            ratio = float("nan")

        dl_ubt = cl_to_dl(l, cl_ubt)
        dl_lcdm = cl_to_dl(l, cl_lcdm)

        planck = PLANCK_2018_LOW_L.get(l, {})
        planck_observed = planck.get("observed")
        planck_lcdm = planck.get("lcdm_bestfit")
        if planck_lcdm and planck_lcdm > 0:
            planck_ratio = planck_observed / planck_lcdm
        else:
            planck_ratio = None

        results[l] = {
            "C_l_ubt": cl_ubt,
            "C_l_lcdm": cl_lcdm,
            "D_l_ubt": dl_ubt,
            "D_l_lcdm": dl_lcdm,
            "ubt_lcdm_ratio": ratio,
            "planck_observed": planck_observed,
            "planck_lcdm_bestfit": planck_lcdm,
            "planck_obs_lcdm_ratio": planck_ratio,
            "consistent_with_planck": (
                abs(ratio - planck_ratio) < 0.2
                if (planck_ratio is not None and not math.isnan(ratio))
                else None
            ),
        }

    return results


def main() -> None:
    print("=" * 65)
    print("UBT CMB Angular Power Spectrum C_l — Low-l Analysis")
    print("=" * 65)
    print()
    print("Method: Sachs-Wolfe approximation (l ≤ 10)")
    print("WARNING: Approximate results only. Boltzmann code needed for precision.")
    print()

    l_values = [2, 3, 4, 5, 6, 10]

    scenarios = {
        "B_hubble": {
            "R_psi_mpc": HUBBLE_LENGTH_MPC,
            "label": "Scenario B: R_ψ = c/H_0 = {:.0f} Mpc".format(HUBBLE_LENGTH_MPC),
        },
        "C_fitted": {
            "R_psi_mpc": 3000.0,
            "label": "Scenario C: R_ψ = 3000 Mpc (free parameter)",
        },
    }

    all_results = {}
    for sc_name, sc in scenarios.items():
        r = sc["R_psi_mpc"]
        print(f"[{sc['label']}]")
        print(f"  k_min = 1/R_ψ = {1.0/r:.3e} Mpc^-1")
        print()
        res = analyse_low_l(l_values, r, sc_name)
        all_results[sc_name] = {
            "R_psi_mpc": r,
            "label": sc["label"],
            "results_by_l": {str(l): v for l, v in res.items()},
        }

        # Print table
        print(f"  {'l':>4}  {'C_UBT/C_ΛCDM':>14}  {'Planck/ΛCDM':>12}  {'Consistent':>10}")
        print(f"  {'-'*4}  {'-'*14}  {'-'*12}  {'-'*10}")
        for l in l_values:
            r_ubt = res[l]["ubt_lcdm_ratio"]
            r_pl = res[l]["planck_obs_lcdm_ratio"]
            cons = res[l]["consistent_with_planck"]
            r_ubt_str = f"{r_ubt:.3f}" if not math.isnan(r_ubt) else "NaN"
            r_pl_str = f"{r_pl:.3f}" if r_pl else "  N/A"
            cons_str = ("YES" if cons else "NO") if cons is not None else "N/A"
            print(f"  {l:>4}  {r_ubt_str:>14}  {r_pl_str:>12}  {cons_str:>10}")
        print()

    # Save results
    out_dir = Path(__file__).parent
    out_file = out_dir / "ubt_cmb_cl_results.json"

    output = {
        "model": "UBT_CMB_angular_power_spectrum_low_l",
        "method": "Sachs-Wolfe approximation",
        "warning": (
            "APPROXIMATE: Sachs-Wolfe valid for l <= 10 only. "
            "Full precision requires CAMB/CLASS with UBT primordial spectrum."
        ),
        "eta_0_mpc": ETA_0_MPC,
        "planck_2018_low_l": PLANCK_2018_LOW_L,
        "scenarios": all_results,
        "status": "CONJECTURE — quantitative result pending Boltzmann code integration",
        "reference": "docs/predictions/cmb_prediction.md",
    }

    with open(out_file, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Results written to {out_file}")
    print()
    print("See docs/predictions/cmb_prediction.md for the falsifiable prediction.")


if __name__ == "__main__":
    main()
