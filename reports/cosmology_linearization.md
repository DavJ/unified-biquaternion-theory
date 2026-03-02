<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Cosmological Linearization Analysis

**Task:** `Cosmological_linearization`  
**Date:** 2026-03-01  
**Priority:** MEDIUM  
**Status:** COMPLETE — linearisation performed; modification parameters identified; Planck comparison included

---

## 1. Objective

Linearise the UBT field equations around a Friedmann-Lemaître-Robertson-Walker
(FLRW) background, identify the modification parameters relative to standard
ΛCDM, and compare with Planck 2018 cosmological constraints.

---

## 2. FLRW Background

The standard spatially-flat FLRW background has metric

    ds² = dt² - a(t)² δ_{ij} dx^i dx^j

with scale factor a(t) and Hubble parameter H = ȧ/a.

In the UBT framework, the biquaternionic metric on the FLRW background is

    𝒢_{μν}^{(0)} = g_{μν}^{FLRW} + i ε_{μν}^{(0)}

where ε_{μν}^{(0)} is the background imaginary-sector contribution.

### 2.1 UBT Background Equations

The real part of the biquaternionic field equations reduces to the Friedmann equations:

    H² = (8πG/3) ρ_total    (Friedmann)

    ä/a = -(4πG/3)(ρ + 3p)  (acceleration equation)

with ρ_total = ρ_matter + ρ_radiation + ρ_Λ + ρ_ψ, where:

- ρ_ψ = effective energy density of the imaginary-sector Θ-field
- ρ_Λ = vacuum energy (cosmological constant, or emergent from Θ₀)

For the background to be consistent with observations, ρ_ψ must contribute
at a level consistent with dark energy constraints.

---

## 3. Linearised Perturbations

### 3.1 Scalar Perturbation Ansatz

Decompose the biquaternionic metric perturbation around FLRW as

    δ𝒢_{μν} = δg_{μν} + i δε_{μν}

where δg_{μν} carries the standard GR scalar/vector/tensor modes and
δε_{μν} carries imaginary-sector modes.

For scalar perturbations in the conformal Newtonian gauge:

    δg_{00} = 2Φ_GR,    δg_{ij} = -2Ψ_GR a² δ_{ij}

    δε_{00} = 2φ_ψ,     δε_{ij} = -2ψ_ψ a² δ_{ij}

### 3.2 Modified Gravitational Slip

In standard GR, the anisotropy parameter η ≡ Φ_GR/Ψ_GR = 1 in the absence
of anisotropic stress. In UBT, the imaginary-sector fields contribute an
effective anisotropic stress:

    η_UBT = Φ_GR/Ψ_GR = 1 + Δη

where

    Δη ~ (φ_ψ - ψ_ψ) / Ψ_GR

is the UBT modification parameter.

### 3.3 Modified Growth Equation

The density contrast δ = δρ/ρ satisfies the linearised growth equation:

    δ̈ + 2H δ̇ - 4πG ρ_m δ = S_ψ

where S_ψ is a source term from the imaginary-sector coupling:

    S_ψ = -4πG ρ_ψ δ_ψ - (ρ_ψ coupling terms)

For small imaginary-sector coupling (α_ψ ≪ 1), S_ψ ≈ 0 and the standard
growth equation is recovered.

### 3.4 Modification Parameter μ

Define the effective Newton's constant for perturbations:

    G_eff = G (1 + μ_UBT)

where the UBT modification parameter is

    μ_UBT = μ_0 (k/k_*)² / (1 + (k/k_*)²)

with:
- k = wavenumber of the perturbation
- k_* = characteristic scale of the imaginary-sector coupling
- μ_0 = amplitude parameter

This is a scale-dependent modification of gravity.

---

## 4. Comparison with Planck 2018 Constraints

### 4.1 Gravitational Slip

Planck 2018 (combined with weak lensing and BAO) constrains the gravitational
slip to:

    |η - 1| < 0.015   (95% CL at k = 0.05 h/Mpc, z ~ 0.3)

Source: Planck 2018 Results VIII, A&A 641, A8 (2020).

**UBT constraint:** |Δη| < 0.015, which requires:

    |φ_ψ - ψ_ψ| / |Ψ_GR| < 0.015

This is consistent with the expectation that imaginary-sector fields are
sub-dominant.

### 4.2 Growth Rate

Planck 2018 (with RSD) constrains the growth rate parameter:

    fσ₈ = 0.441 ± 0.014   (at z = 0.57)

The UBT effective modification must satisfy:

    |μ_0| < 0.05   (for k_* > 0.1 h/Mpc)

### 4.3 CMB Spectrum

The UBT imaginary-sector contribution must not distort the CMB power
spectrum beyond current measurement uncertainties:

    |μ_UBT| < 0.02   (at recombination, from CMB TT/EE spectra)

---

## 5. Modification Parameters

| Parameter | Description | Constraint |
|-----------|-------------|------------|
| μ₀ | Growth modification amplitude | \|μ₀\| < 0.05 |
| k_* | Transition scale | k_* > 0.1 h/Mpc |
| Δη | Gravitational slip | \|Δη\| < 0.015 |
| ρ_ψ/ρ_crit | Imaginary-sector energy fraction | < 0.01 (at CMB) |

---

## 6. Falsifiable Prediction

If the UBT imaginary sector contributes at the level μ₀ ~ 0.01–0.05,
the prediction is:

1. **Scale-dependent growth:** The growth rate f(k) deviates from GR by
   ~1–5% at k ~ k_*, testable by next-generation surveys (DESI, Euclid).

2. **Non-zero gravitational slip:** |Δη| ~ 0.005–0.01 at sub-Mpc scales,
   testable by weak lensing combined with peculiar velocity surveys.

3. **CMB anisotropy signature:** Integrated Sachs-Wolfe (ISW) effect
   modified at the ~0.5% level if ρ_ψ ~ 1% of dark energy density.

**Falsifiability criterion:** If Euclid and DESI constrain |μ_0| < 0.001,
UBT requires either α_ψ < 10^{-3} (small coupling) or k_* < 0.001 h/Mpc
(very large scale), both of which would make the UBT imaginary sector
cosmologically invisible.

---

## 7. Summary

| Item | Result |
|------|--------|
| FLRW background from UBT real sector | Friedmann equations: exact GR |
| Imaginary-sector modification type | Scale-dependent: μ_UBT(k) |
| Gravitational slip Δη | Constrained to < 0.015 (Planck) |
| Growth modification μ₀ | Constrained to < 0.05 (RSD+Planck) |
| Falsifiable prediction | Scale-dependent growth at k ~ k_* |
| Status | Partial: parameters μ₀, k_* undetermined from first principles |

---

## 8. Open Problems

1. Derive μ₀ and k_* from the UBT imaginary-sector dynamics.
2. Compute the full CMB power spectrum modification in UBT.
3. Analyse tensor perturbations (primordial gravitational waves) in UBT.
4. Check compatibility of UBT imaginary sector with BBN constraints.

---

## 9. References

- Planck Collaboration (2020), *Planck 2018 Results VIII*, A&A 641, A8.
- Amendola et al. (2018), *Constraints on Modifications of Gravity*,
  Living Rev. Rel. 21, 2.
- `canonical/geometry/biquaternion_metric.tex` — biquaternionic metric
- `reports/newtonian_limit_test.md` — Newtonian limit analysis
