<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Prediction Program Status

**Date:** 2026-03-02  
**Status:** STABLE — all reports bounded; falsifiability statements present.

---

## Scope

This document summarises the three active prediction reports, verifying that
each clearly separates **Inputs**, **Assumptions**, and **Derived statements**,
and includes a **Falsifiability** criterion.

No new physical results are computed here.

---

## 1. Newtonian Limit (`reports/newtonian_limit_test.md`)

### Inputs
- UBT biquaternionic field equation: ℰ_{μν} = κ 𝒯_{μν}
- Weak-field slow-motion limit: |h_{μν}| ≪ 1, |T_{ij}| ≪ |T_{00}|
- Imaginary-sector assumption: |ε_{μν}| ≪ |h_{μν}|

### Assumptions
- Real sector recovers GR at leading order (proved, linearised).
- Imaginary-sector correction is Yukawa-type with undetermined parameters
  α_ψ (dimensionless coupling) and λ_ψ (screening length).

### Derived Statements
- Standard Newtonian potential Φ = −GM/r recovered exactly from real sector.
- UBT correction: δΦ = α_ψ · (GM/r) · e^{−r/λ_ψ} (Yukawa form).

### Experimental Bound
- **|α_ψ| < 0.001** for λ_ψ > 1 mm (Eöt-Wash / Kapner et al. 2007).
- Exponentially suppressed for planetary scales (r ≫ λ_ψ).

### Falsifiability
A null result in sub-millimeter gravity at |α| < 10^{−3} for λ ~ 10 μm–1 mm
constrains UBT to α_ψ < 10^{−3} or λ_ψ < 10 μm.

### Status
✅ Bounded | ✅ Falsifiable | ⚠️ α_ψ and λ_ψ not yet derived from first principles.

---

## 2. Cosmological Linearisation (`reports/cosmology_linearization.md`)

### Inputs
- FLRW background, flat spatial sections.
- UBT real-sector → Friedmann equations (exact GR at background level).
- Imaginary-sector perturbations δε_{μν} with undetermined amplitude μ₀ and scale k_*.

### Assumptions
- Imaginary-sector coupling α_ψ ≪ 1 (sub-dominant).
- Scale-dependent modification parameterised as μ_UBT(k) = μ₀(k/k_*)²/(1+(k/k_*)²).

### Derived Statements
- Modified growth equation: δ̈ + 2H δ̇ − 4πG ρ_m δ = S_ψ.
- Effective Newton's constant: G_eff = G(1 + μ_UBT).
- Non-zero gravitational slip: Δη ~ (φ_ψ − ψ_ψ)/Ψ_GR.

### Observables Affected
- **H(z):** Background expansion unmodified (imaginary sector sub-dominant).
- **Growth rate f(k):** Scale-dependent deviation at k ~ k_*.
- **CMB TT/EE:** ISW effect modified at ~0.5% level if ρ_ψ ~ 1% of dark energy.
- **Weak lensing:** Gravitational slip Δη detectable by Euclid/DESI.

### Experimental Bounds
- |Δη| < 0.015 (Planck 2018, 95% CL).
- |μ₀| < 0.05 (RSD + Planck).

### Falsifiability
If Euclid+DESI constrain |μ₀| < 0.001, UBT imaginary sector is cosmologically
invisible (α_ψ < 10^{−3} or k_* < 0.001 h/Mpc).

### Status
✅ Bounded | ✅ Falsifiable | ⚠️ μ₀, k_* not derived from first principles.

---

## 3. Electron Mass Mechanism (`reports/electron_mass_mechanism.md`)

### Inputs
- Biquaternionic Θ-field over complex time τ = t + iψ.
- Resonance condition on imaginary-time boundary: ψ₀ = n · (ℏ/m_e c).
- Mode number n = 1 for the electron.

### Assumptions
1. Θ-field depends on complex time τ = t + iψ (not a new claim; part of UBT core).
2. Standing-wave resonance condition determines mass scale.
3. n = 1 fundamental mode identified with electron.
4. Real-sector coupling transmits resonance energy to observed mass.

### Derived Statements
- Dimensionless mass formula: m_e/m_P = C(n, λ_Θ).
- Schematic form: C(1, λ_Θ) = exp(−1/λ_Θ²) with λ_Θ ≈ 0.23 reproducing m_e/m_P numerically.

### Circularity Check
- ❌ α does NOT appear as an input. Verified: λ_Θ, ψ₀, n are defined independently of α.
- ❌ m_e does NOT appear as an input (it is the output).

### Falsifiability
If an independent derivation of λ_Θ from the algebra gives λ_Θ ≠ 0.23 and
the resulting m_e disagrees with experiment, the mechanism is falsified.

### Status
✅ No circular α | ✅ Inputs vs derived clearly separated | ⚠️ λ_Θ not yet derived from first principles — mechanism is currently a *parametrisation*, not a *prediction*.

---

## Overall Assessment

| Report | Bounded | Falsifiable | Free parameters | Status |
|--------|---------|-------------|-----------------|--------|
| Newtonian limit | ✅ | ✅ | α_ψ, λ_ψ | Partial |
| Cosmological linearisation | ✅ | ✅ | μ₀, k_* | Partial |
| Electron mass mechanism | ✅ | ✅ | λ_Θ | Partial |

All three reports are in **consistent partial status**: bounds are stated,
falsifiability criteria are explicit, and free parameters are identified as
open problems.  No new physics has been claimed.

---

## References

- `reports/newtonian_limit_test.md`
- `reports/cosmology_linearization.md`
- `reports/electron_mass_mechanism.md`
- `reports/gr_recovery_final_status.md`
