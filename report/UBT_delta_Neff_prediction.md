<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# UBT ΔN_eff Prediction — Dark Radiation from Θ Zero Modes

**Version:** v28 (UBT_v28_cosmo_hecke_neff)  
**Date:** 2026-03-06  
**Reproducible script:** `simulations/cosmology_models/ubt_dark_radiation.py`  
**Notebook:** `notebooks/neff_estimation.ipynb`  
**Status:** Layer 2 prediction — derived from geometry, no curve fitting  

---

## 1. Executive Summary

The UBT Θ-field zero modes on T²(τ) are massless relativistic bosons
in the early universe.  Depending on their decoupling temperature T_D,
they contribute:

| Scenario | g_X | T_D [GeV] | ΔN_eff |
|---|---|---|---|
| Single real scalar (conservative) | 1 | 1000 | 0.011 |
| Complex scalar (1 complex DoF) | 2 | 2 | **0.046** |
| Full Θ field (all zero modes) | 8 | 2 | 0.182 |

**Central estimate** (complex scalar, T_D ~ 2 GeV):

> **ΔN_eff ≈ 0.046**  (exceeds CMB-S4 detection threshold of 0.03)

---

## 2. Standard Formula

The total radiation energy density is:

    ρ_rad = ρ_γ [1 + (7/8)(4/11)^{4/3} N_eff]

For a new bosonic species X with g_X DoF decoupled at T_D, the
contribution to ΔN_eff is:

    ΔN_eff = (8/7) × (11/4)^{4/3} × (g_X / 2) × (T_X / T_γ)^4

where the temperature ratio (entropy conservation):

    T_X / T_γ = [g_{*S}(T_0) / g_{*S}(T_D)]^{1/3}

with g_{*S}(T_0) = 2 (photons only after e+e- annihilation).

---

## 3. UBT Setup

### 3.1 Identifying the Relativistic Modes

From `report/theta_spectrum_analysis.md`:

- The UBT Θ field has **8 real DoF** (biquaternion components)
- On T²(τ) each component has one exactly massless zero mode
- Total massless Θ DoF = **8**

For the purposes of ΔN_eff we consider three nested scenarios:

1. **Conservative** (g_X = 1): only the single real zero mode of the
   scalar part of Θ is relativistic
2. **Moderate** (g_X = 2): a single complex zero mode (particle +
   antiparticle-like degree of freedom)
3. **Full** (g_X = 8): all 8 real DoF of Θ are light and thermalised
   before T_D

### 3.2 Decoupling Temperature

The Θ zero modes couple to the SM via the biquaternionic coupling κ.
In the imaginary-time sector, this coupling is gravitationally suppressed
at low energies.  We parameterise T_D and present results for the full
range.

**Expected T_D:**

- If coupling is gravitational-strength: T_D ~ M_Pl × (κ²) → T_D >> T_EW
- If coupling is sub-gravitational: T_D can be as low as a few GeV

---

## 4. Numerical Results

All computed with `simulations/cosmology_models/ubt_dark_radiation.py`:

### 4.1 Scan over T_D

| T_D [GeV] | g*S | ΔN(1 real) | ΔN(complex) | ΔN(full Θ, 8 DoF) |
|---|---|---|---|---|
| 1.00×10⁴ | 110.75 | 0.0104 | 0.0209 | 0.0834 |
| 1.00×10³ | 106.75 | 0.0110 | 0.0219 | 0.0876 |
| 1.00×10² | 106.75 | 0.0110 | 0.0219 | 0.0876 |
| 2.00 | 61.75 | 0.0227 | 0.0455 | 0.1818 |
| 5.00×10⁻¹ | 17.25 | 0.1245 | 0.2489 | 0.9957 |
| 1.50×10⁻¹ | 17.25 | 0.1245 | 0.2489 | 0.9957 |

### 4.2 Best-Estimate Scenario

**T_D = 2 GeV** (after charm threshold, before QCD confinement),  
**g*S = 61.75**:

- ΔN_eff (single real) = 0.0227
- ΔN_eff (complex) = **0.0455**
- ΔN_eff (full Θ) = 0.1818

**N_eff(UBT) = N_eff(SM) + ΔN_eff(complex) = 3.044 + 0.046 = 3.090**

---

## 5. Comparison with Observations

| Source | N_eff | Reference |
|---|---|---|
| SM theory | 3.044 | Cielo et al. 2023 |
| Planck 2018 (base) | 2.99 ± 0.17 | arXiv:1807.06209 |
| CMB-S4 forecast | σ(N_eff) ~ 0.03 | CMB-S4 Science Book |
| UBT central estimate | 3.090 ± (model unc.) | this work |

The UBT prediction of **N_eff ≈ 3.09** (for complex zero mode, T_D ~ 2 GeV)
lies within the Planck 1σ band and would be **detectable** with CMB-S4
(ΔN_eff = 0.046 > σ_CMB-S4 = 0.03).

---

## 6. Derivation Outline (No Curve Fitting)

All quantities are derived from the torus geometry:

1. **g_X = 8** from counting real DoF of a biquaternion (4 complex × 2 real)
2. **T_X/T_γ** from entropy conservation (Kolb & Turner 1990, eq. 3.74)
3. **g*S(T_D)** from the SM particle content (PDG 2022 Table 22)
4. **ΔN_eff formula** from the standard radiation energy budget

No free parameters are fitted to the N_eff observation.

---

## 7. Open Questions

1. What is T_D exactly?  A first-principles coupling calculation (in the
   imaginary-time sector of UBT) is needed.
2. Is the entire biquaternion Θ field thermalised, or only sub-sectors?
3. Does the imaginary time phase ψ contribute an additional thermal bath?
4. Can the CMB angular power spectrum distinguish UBT dark radiation from
   a simple massless scalar?

---

## 8. Falsification

**Falsifiable prediction:** If CMB-S4 measures N_eff < 3.05, the
g_X = 2 scenario with T_D < 10³ GeV is **excluded**.  The full Θ scenario
(g_X = 8) requires N_eff < 3.14 to be excluded at 2σ.

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
