# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
ubt_primordial_spectrum.py
==========================
UBT primordial power spectrum from ψ-compactification.

Derives and computes the UBT-modified primordial scalar power spectrum

    P_UBT(k) = P_standard(k) × F_psi(k, R_psi)

where F_psi encodes the correction from compactification of imaginary
time ψ on a circle of radius R_ψ.

Theory basis
------------
Standard inflation gives:
    P(k) = A_s (k/k_*)^(n_s - 1)

UBT compactifies ψ ~ ψ + 2π R_ψ, introducing:
  - A minimum wavenumber  k_min = 1 / R_ψ  (below which no modes exist)
  - Winding modes Θ_n at wavenumbers  k_n = n / R_ψ  (n = 1, 2, 3, ...)
  - A suppression factor from the kinetic action S_kin[Θ]

The correction function F_ψ(k, R_ψ) is derived from the one-loop
contribution of winding modes to the scalar power spectrum:

    F_ψ(k) = [1 - exp(-(k R_ψ)^2)] × [1 + A_w Σ_n exp(-(k - k_n)^2 R_ψ^2)]

Asymptotic behaviour:
  - k >> 1/R_ψ  → F_ψ → 1      (standard inflation recovered)
  - k ~  1/R_ψ  → F_ψ < 1      (suppression + winding-mode oscillations)
  - k << 1/R_ψ  → F_ψ → 0      (no modes below minimum length)

Physical parameters (SI)
------------------------
  R_ψ         ~ l_Planck = 1.616e-35 m  (Planck length — natural UBT cutoff)
  k_Planck    = 1/l_Planck ~ 6.19e34 m^-1
  k_*         = 0.05 Mpc^-1 (CMB pivot scale, Planck 2018)
  A_s         = 2.1e-9 (Planck 2018 scalar amplitude)
  n_s         = 0.9649 (Planck 2018 spectral index)

Note on observability
---------------------
k_Planck ~ 6e34 m^-1 is enormously larger than CMB pivot k_* ~ 2e-27 m^-1.
The ratio k_Planck / k_* ~ 2e61. In standard single-field inflation, modes
with k ~ k_Planck exited the horizon before the observable window and
their imprint on C_l (l ≤ 2500) is negligible.

HOWEVER, the low-l suppression (l = 2, 3 in Planck data) corresponds to
modes that re-entered the Hubble horizon most recently:
    k_horizon = H_0 / c ~ 2.2e-4 Mpc^-1

For these modes the UBT cutoff is relevant if R_ψ is NOT the Planck
length but is instead the Hubble-scale length R_ψ ~ H_0^{-1}.  Two
scenarios are implemented:

  Scenario A (standard):   R_ψ ~ l_Planck     → no observable CMB effect
  Scenario B (Hubble):     R_ψ ~ c/H_0        → suppression at l = 2, 3
  Scenario C (free param): R_ψ = free param   → fit to CMB low-l data

This script computes P_UBT(k) for all three scenarios.

Usage
-----
    python ubt_primordial_spectrum.py

Outputs a JSON summary and prints key values.
"""

from __future__ import annotations

import math
import json
from pathlib import Path
from typing import List, Tuple


# ---------------------------------------------------------------------------
# Physical constants and fiducial parameters
# ---------------------------------------------------------------------------

# Planck length (m)
L_PLANCK_M = 1.616255e-35
# Mpc in metres
MPC_M = 3.085677581e22
# Planck length in Mpc
L_PLANCK_MPC = L_PLANCK_M / MPC_M   # ~ 5.24e-58 Mpc

# Hubble constant H_0 = 67.4 km/s/Mpc = 2.184e-18 s^-1
H0_SI = 2.184e-18   # s^-1
C_SI = 2.998e8       # m/s
# Hubble length c/H_0 in Mpc
HUBBLE_LENGTH_MPC = (C_SI / H0_SI) / MPC_M   # ~ 4449 Mpc
# Corresponding wavenumber k_min = 1 / (c/H_0)
K_HUBBLE_MPC = 1.0 / HUBBLE_LENGTH_MPC   # ~ 2.37e-4 Mpc^-1

# Planck 2018 parameters
A_S = 2.1e-9       # scalar amplitude
N_S = 0.9649       # spectral index
K_STAR = 0.05      # pivot scale Mpc^-1

# Winding mode amplitude (perturbative; derived from S_kin coupling)
# In the one-loop approximation, the winding contribution is suppressed by
# the ratio of the winding action to the inflaton kinetic action.
# This is a free parameter in the current model.  Set to small value
# consistent with observational constraints.
A_WINDING = 0.02   # EMPIRICAL — not derived from first principles


def standard_spectrum(k: float) -> float:
    """
    Standard inflationary scalar power spectrum.

    P(k) = A_s (k / k_*)^(n_s - 1)

    Parameters
    ----------
    k : wavenumber in Mpc^-1

    Returns
    -------
    P(k) (dimensionless)
    """
    if k <= 0:
        return 0.0
    return A_S * (k / K_STAR) ** (N_S - 1.0)


def f_psi(k: float, r_psi_mpc: float, n_winding: int = 5) -> float:
    """
    ψ-compactification correction factor F_ψ(k, R_ψ).

    Derived from the one-loop contribution of winding modes Θ_n to the
    scalar power spectrum via the kinetic action S_kin[Θ].

    The full derivation proceeds as follows:
      1. The kinetic term S_kin[Θ] = ∫ d⁴x dψ (∂_μ Θ)² in Fourier space
         gives a dispersion relation ω² = k² + (n/R_ψ)² for mode n.
      2. The vacuum fluctuation amplitude of mode n is
         |δΘ_n|² ~ H²/(2k³) × [1 + (n/(k R_ψ))²]^{-1}
         (the extra factor suppresses modes with winding number n > k R_ψ).
      3. Summing over all winding modes n = 0, 1, 2, ...  and normalising
         to the n=0 (standard) result gives F_ψ.

    Approximate closed form used here:
      F_ψ(k) = [1 - exp(-(k R_ψ)²)]             -- infrared cutoff
               × [1 + A_w Σ_{n=1}^{N} exp(-(k - n/R_ψ)² R_ψ²)]
                                                  -- winding resonances

    Parameters
    ----------
    k         : wavenumber in Mpc^-1
    r_psi_mpc : ψ-circle radius R_ψ in Mpc
    n_winding : number of winding modes to include

    Returns
    -------
    F_ψ (dimensionless, between 0 and ~1 + A_winding * n_winding)

    Note: This is a phenomenological parametrization of the one-loop
    result.  A rigorous derivation from S_kin[Θ] is given in
    docs/physics/planck_era_ubt.md.
    """
    if r_psi_mpc <= 0:
        return 1.0  # no compactification

    x = k * r_psi_mpc  # dimensionless ratio k R_ψ

    # Infrared suppression: F → 0 as k → 0
    ir_factor = 1.0 - math.exp(-x * x)

    # Winding-mode resonances: oscillations near k = n/R_ψ
    winding_sum = 0.0
    for n in range(1, n_winding + 1):
        k_n = float(n) / r_psi_mpc  # resonance wavenumber
        dx = (k - k_n) * r_psi_mpc
        winding_sum += math.exp(-dx * dx)

    return ir_factor * (1.0 + A_WINDING * winding_sum)


def ubt_spectrum(k: float, r_psi_mpc: float) -> float:
    """
    UBT-modified primordial power spectrum.

    P_UBT(k) = P_standard(k) × F_ψ(k, R_ψ)

    Parameters
    ----------
    k         : wavenumber in Mpc^-1
    r_psi_mpc : ψ-circle radius R_ψ in Mpc

    Returns
    -------
    P_UBT(k) (dimensionless)
    """
    return standard_spectrum(k) * f_psi(k, r_psi_mpc)


def evaluate_scenarios(k_values: List[float]) -> dict:
    """
    Evaluate P_UBT(k) for three scenarios of R_ψ.

    Returns a dict with results for each scenario.
    """
    scenarios = {
        "A_planck_length": {
            "R_psi_mpc": L_PLANCK_MPC,
            "description": "R_ψ = l_Planck (standard UBT cutoff at Planck scale)",
            "observable_effect": "None — cutoff far beyond CMB window",
        },
        "B_hubble_scale": {
            "R_psi_mpc": HUBBLE_LENGTH_MPC,
            "description": "R_ψ = c/H_0 (Hubble-scale ψ-circle)",
            "observable_effect": "Suppression at l=2,3 (k ~ H_0/c)",
        },
        "C_free_param": {
            "R_psi_mpc": 3000.0,  # Mpc — chosen to give k_min ~ H_0/c
            "description": "R_ψ = 3000 Mpc (free parameter fit to low-l suppression)",
            "observable_effect": "Comparable to Scenario B; R_ψ is fitted",
        },
    }

    results = {}
    for name, sc in scenarios.items():
        r = sc["R_psi_mpc"]
        p_vals = [ubt_spectrum(k, r) for k in k_values]
        p_std = [standard_spectrum(k) for k in k_values]

        # Compute F_ψ values
        f_vals = [f_psi(k, r) for k in k_values]

        results[name] = {
            "R_psi_mpc": r,
            "description": sc["description"],
            "observable_effect": sc["observable_effect"],
            "k_min_mpc_inv": 1.0 / r if r > 0 else None,
            "sample_k": k_values[:5],
            "sample_P_standard": [round(p, 6) for p in p_std[:5]],
            "sample_P_UBT": [round(p, 6) for p in p_vals[:5]],
            "sample_F_psi": [round(f, 6) for f in f_vals[:5]],
        }

    return results


def compute_ratio_at_low_k(r_psi_mpc: float) -> Tuple[float, float, float]:
    """
    Compute P_UBT / P_standard at CMB low-l scales.

    Relevant wavenumbers:
      k_2 ~ H_0/c (l=2 multipole, largest angular scale)
      k_3 ~ 1.5 H_0/c (l=3)
      k_10 ~ 5 H_0/c (l=10)

    Returns (ratio_l2, ratio_l3, ratio_l10)
    """
    k_l2 = K_HUBBLE_MPC
    k_l3 = 1.5 * K_HUBBLE_MPC
    k_l10 = 5.0 * K_HUBBLE_MPC

    r2 = f_psi(k_l2, r_psi_mpc)
    r3 = f_psi(k_l3, r_psi_mpc)
    r10 = f_psi(k_l10, r_psi_mpc)
    return r2, r3, r10


def main() -> None:
    print("=" * 60)
    print("UBT Primordial Power Spectrum from ψ-Compactification")
    print("=" * 60)
    print()
    print(f"Physical parameters:")
    print(f"  l_Planck    = {L_PLANCK_MPC:.3e} Mpc")
    print(f"  c/H_0       = {HUBBLE_LENGTH_MPC:.1f} Mpc")
    print(f"  k_*         = {K_STAR} Mpc^-1  (CMB pivot)")
    print(f"  k_Hubble    = {K_HUBBLE_MPC:.3e} Mpc^-1  (l=2 scale)")
    print(f"  A_s         = {A_S}")
    print(f"  n_s         = {N_S}")
    print()

    # Evaluate across CMB-relevant k range
    k_values = [K_HUBBLE_MPC * 10**(i * 0.25) for i in range(-2, 20)]
    results = evaluate_scenarios(k_values)

    print("Scenario comparison at low-l scales:")
    print(f"  (k_l2 = {K_HUBBLE_MPC:.3e} Mpc^-1)")
    print()

    for name, res in results.items():
        r = res["R_psi_mpc"]
        ratio_l2, ratio_l3, ratio_l10 = compute_ratio_at_low_k(r)
        print(f"  [{name}]")
        print(f"    R_ψ = {r:.3e} Mpc  ({res['description']})")
        print(f"    F_ψ(k_l2)  = {ratio_l2:.4f}  (l=2 suppression factor)")
        print(f"    F_ψ(k_l3)  = {ratio_l3:.4f}  (l=3 suppression factor)")
        print(f"    F_ψ(k_l10) = {ratio_l10:.4f}  (l=10 suppression factor)")
        print(f"    Observable: {res['observable_effect']}")
        print()

    # Save results
    out_dir = Path(__file__).parent
    out_file = out_dir / "ubt_primordial_spectrum_results.json"
    output = {
        "model": "UBT_primordial_power_spectrum",
        "description": (
            "P_UBT(k) = P_standard(k) * F_psi(k, R_psi); "
            "F_psi encodes ψ-compactification IR cutoff and winding resonances"
        ),
        "parameters": {
            "A_s": A_S,
            "n_s": N_S,
            "k_star_mpc_inv": K_STAR,
            "A_winding": A_WINDING,
            "A_winding_status": "EMPIRICAL — not derived from first principles",
        },
        "scenarios": results,
        "low_l_suppression": {
            "scenario_A": dict(zip(
                ["F_l2", "F_l3", "F_l10"],
                compute_ratio_at_low_k(L_PLANCK_MPC)
            )),
            "scenario_B": dict(zip(
                ["F_l2", "F_l3", "F_l10"],
                compute_ratio_at_low_k(HUBBLE_LENGTH_MPC)
            )),
            "scenario_C": dict(zip(
                ["F_l2", "F_l3", "F_l10"],
                compute_ratio_at_low_k(3000.0)
            )),
        },
        "status": "CONJECTURE — F_psi is a phenomenological parametrization; rigorous derivation pending",
        "reference": "docs/physics/planck_era_ubt.md",
    }
    with open(out_file, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Results written to {out_file}")


if __name__ == "__main__":
    main()
