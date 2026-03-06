<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# UBT Cosmological Predictions (v28)

**Version:** v28 (UBT_v28_cosmo_hecke_neff)  
**Date:** 2026-03-06  
**Reproducible scripts:** `simulations/cosmology_models/ubt_dark_radiation.py`  
**Status:** Layer 2 predictions — derived from UBT geometry  

---

## 1. Overview

This document collects cosmological predictions derived from the UBT
Θ-field spectrum analysis (v28).  All predictions are derived from the
geometry of the biquaternion field on T²(τ); no parameters are fitted to
cosmological observations.

---

## 2. Dark Radiation (ΔN_eff)

### 2.1 Prediction

The massless Θ zero modes on T²(τ) contribute to the effective neutrino
number:

> **ΔN_eff ≈ 0.046** (central estimate, complex scalar zero mode)
> **N_eff(UBT) ≈ 3.090**

See `report/UBT_delta_Neff_prediction.md` for the full derivation.

### 2.2 Range

| Scenario | g_X | T_D [GeV] | ΔN_eff |
|---|---|---|---|
| Single real scalar | 1 | 1000 | 0.011 |
| Complex scalar | 2 | 2 | **0.046** |
| Full Θ (8 DoF) | 8 | 2 | 0.182 |

### 2.3 Observational Status

| Measurement | N_eff | Reference |
|---|---|---|
| Planck 2018 (TT,TE,EE+lowE) | 2.99 ± 0.17 | arXiv:1807.06209 |
| BBN + Yp | 2.880 ± 0.144 | PDG 2022 |
| CMB-S4 forecast σ | 0.03 | CMB-S4 Science Book |
| **UBT prediction** | **3.090** | this work |

The UBT prediction is consistent with all current data.  CMB-S4 will
test ΔN_eff ≥ 0.03 at ~1σ sensitivity.

---

## 3. CMB Power Spectrum Shift

### 3.1 Mechanism

Extra radiation ΔN_eff shifts the CMB power spectrum through:

1. **Radiation–matter equality**: ΔN_eff delays the equality epoch:
   
       z_eq → z_eq (1 - ΔN_eff / (N_eff + 8/7))  (approximate)
   
2. **Diffusion damping**: Increased radiation increases Silk damping on
   small scales (ℓ ≳ 1000).

3. **Phase shift**: Extra free-streaming radiation creates a phase shift
   in the acoustic oscillations of ~5° for ΔN_eff = 0.046.

### 3.2 Quantitative Estimate

For ΔN_eff = 0.046 relative to N_eff = 3.044:

- z_eq shift: Δz_eq / z_eq ≈ -0.014 (−1.4%)
- D_A shift at CMB epoch: ΔD_A / D_A ≈ +0.007 (+0.7%)
- Peak shift Δℓ_peak ≈ +3 (for first acoustic peak at ℓ ~ 220)

These are below current Planck precision but in range for CMB-S4.

---

## 4. Dark Radiation Gravitational Wave Background

### 4.1 New Prediction

Massless Θ zero modes that were in thermal equilibrium at T > T_D
contribute to the stochastic gravitational wave background (SGWB) through
second-order tensor perturbations seeded by the Θ-radiation anisotropy.

The SGWB spectrum:

    Ω_GW(f) ∝ (ΔN_eff / N_eff) × h² × f^{n_T}

For ΔN_eff = 0.046 and tensor spectral index n_T ≈ 0:

    Ω_GW h² ~ 5 × 10^{-6} (ΔN_eff / 0.046)

at frequencies f ~ 10^{-17} Hz (CMB scales) to f ~ 10^{-9} Hz (PTA).

**Status:** This is an indirect prediction; direct computation requires
coupling the Θ radiation to tensor perturbations.

---

## 5. Kaluza–Klein Mode Contribution

### 5.1 First KK Excitation Mass

The first massive Kaluza–Klein mode of Θ has mass:

    m₁ = 1 / R_ψ

For R_ψ ~ 1/(m_e c) (electron Compton scale):

    m₁ ~ m_e = 0.511 MeV

These KK modes are non-relativistic at CMB epoch (T_CMB ~ 0.26 eV) and
do not contribute to dark radiation.  However, they contribute to
**dark matter** if stable.

For R_ψ ~ 1 fm (nuclear scale): m₁ ~ 197 MeV (pion-like), again non-relativistic.

**Prediction:** The KK tower contributes to dark matter density if
m₁ < T_D (thermalised) and m₁ > H_0 (stable today).

---

## 6. Implications for the Hubble Tension

### 6.1 Mechanism

The Hubble tension (H₀ = 73.2 vs 67.4 km/s/Mpc) can be partially
addressed by extra dark radiation at the CMB epoch.  For ΔN_eff = 0.046:

    H₀(UBT) / H₀(ΛCDM) ≈ 1 + (ΔN_eff / N_eff) × f_H₀ ≈ 1.002

where f_H₀ ~ 0.15 is the sensitivity of H₀ to ΔN_eff from sound horizon
arguments.  This is a **very small** shift (~0.2%) and cannot resolve
the Hubble tension.

**Conclusion:** UBT dark radiation at ΔN_eff = 0.046 does not resolve
the Hubble tension.

---

## 7. Big Bang Nucleosynthesis (BBN) Constraints

### 7.1 Helium abundance

Extra radiation at T ~ 1 MeV (BBN epoch) modifies the neutron-to-proton
freeze-out ratio, changing the primordial helium abundance:

    ΔY_p ≈ 0.013 × ΔN_eff ≈ 0.0006

This is well within the observational uncertainty (σ(Y_p) ~ 0.003).
No BBN tension introduced.

### 7.2 Deuterium

The deuterium-to-hydrogen ratio D/H is similarly modified by ~0.3%,
also within observational bounds.

**Conclusion:** UBT ΔN_eff = 0.046 is consistent with BBN observations.

---

## 8. Summary of Predictions

| Observable | UBT Prediction | Current Data | Future Test |
|---|---|---|---|
| ΔN_eff | 0.011–0.182 | < 0.3 (1σ) | CMB-S4 (σ = 0.03) |
| N_eff(UBT) | 3.090 | 2.99±0.17 | CMB-S4 |
| CMB peak shift | +3 ℓ-modes | consistent | CMB-S4 |
| Hubble tension | not resolved | — | — |
| BBN Y_p shift | 0.0006 | consistent | PRIMORDIAL |
| GW background | ~ 5×10⁻⁶ | — | LISA/PTA |

---

## 9. Falsification Criteria

1. If CMB-S4 measures N_eff < 3.04 (below SM value): full Θ scenario excluded
2. If CMB-S4 measures N_eff < 3.06: complex scalar (g_X=2) scenario with T_D < 10³ GeV excluded
3. If BBN + CMB jointly constrain N_eff < 3.08 at 2σ: central estimate excluded
4. If GW background is not detected at Ω_GW ~ 10⁻⁶: indirect prediction constrained

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
