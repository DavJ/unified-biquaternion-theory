<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# UBT Θ-Field Eigenmode Spectrum Analysis

**Version:** v28 (UBT_v28_cosmo_hecke_neff)  
**Date:** 2026-03-06  
**Reproducible script:** `simulations/theta_eigenmodes/theta_spectrum_scan.py`  
**Status:** Layer 2 extension — preserves all Layer 0/1 axioms  

---

## 1. Executive Summary

The UBT field Θ(q, τ) on a compact torus T²(R_t × R_ψ) possesses an
exactly massless **zero mode** at Kaluza–Klein level n = 0.  Each of the
8 real degrees of freedom of the biquaternion Θ field contributes one
massless mode.  These zero modes are candidates for **dark radiation**
contributing to ΔN_eff.

**Key findings:**
| Quantity | Value | Derivation |
|---|---|---|
| Zero mode degeneracy (1D ψ-circle) | 1 | k = 0, λ = 0 |
| Zero mode degeneracy (T²) | 1 | (k₁,k₂) = (0,0), λ = 0 |
| Massless Θ zero-mode DoF | **8** | one per real biquaternion component |
| Spectral gap (1D, normalised) | 1.000 | λ₁ = (2π/L)² |
| Poisson duality | PASS | W/S = R ✓ |

---

## 2. Theoretical Framework

### 2.1 Compact Imaginary Time

In UBT the complex time τ = t + iψ renders the imaginary direction ψ
compact:

    ψ ~ ψ + 2π R_ψ

The compactification radius R_ψ is a free parameter of UBT.

### 2.2 Fourier Mode Expansion

The UBT field expands as a Kaluza–Klein tower on the ψ-circle:

    Θ(x, t, ψ) = Σ_{n∈Z}  Θ̂_n(x,t) · exp(i n ψ / R_ψ)

The 4D effective mass of KK mode n is:

    m_n = |n| / R_ψ

The **n = 0 mode is exactly massless** by translation invariance in ψ.

### 2.3 Operator: Laplacian on T^d

For the scalar Laplacian on a d-dimensional torus T^d(L) the eigenvalues
are:

    λ_k = (2π / L)² |k|²,   k ∈ Z^d

The spectrum for d = 1 (ψ-circle) and d = 2 (T² with R_t = R_ψ) is given
in Section 3.

### 2.4 Mode Classification

| Class | Condition | Physical interpretation |
|-------|-----------|------------------------|
| Zero mode | λ = 0 | Massless; dark radiation candidate |
| KK tower | λ = (n/R_ψ)² | Massive for finite R_ψ |
| Spectral gap | λ₁ = (1/R_ψ)² | First massive mode |

---

## 3. Numerical Results

Computed with `simulations/theta_eigenmodes/theta_spectrum_scan.py`
(R_ψ = 1 in normalised units, mode cutoff |k| ≤ 8).

### 3.1 1D ψ-Circle Spectrum

| Level | λ | Degeneracy | Type |
|-------|---|------------|------|
| 0 | 0.000000 | 1 | **ZERO** |
| 1 | 1.000000 | 2 | massive |
| 2 | 4.000000 | 2 | massive |
| 3 | 9.000000 | 2 | massive |
| 4 | 16.000000 | 2 | massive |

Spectral gap: Δ₁ = 1.0 (normalised)

### 3.2 2D T² Spectrum

| Level | λ | Degeneracy |
|-------|---|------------|
| 0 | 0.000000 | 1 |
| 1 | 1.000000 | 4 |
| 2 | 2.000000 | 4 |
| 3 | 4.000000 | 4 |
| 4 | 5.000000 | 8 |

Spectral gap: Δ₂ = 1.0 (normalised)

### 3.3 Poisson Duality Verification

The Poisson summation relation `W(R) = R · S(R)` is verified numerically:

- Spectral sum S = 1.08643481  
- Winding sum W = 1.08643481  
- Ratio W/S = 1.00000000 = R ✓

This confirms the internal consistency of the toroidal quantisation.

---

## 4. Physical Interpretation

### 4.1 Massless Θ Zero Modes

The biquaternion field Θ has **8 real components** (4 complex).  Each real
component has a zero mode on T².  Therefore:

> **The UBT torus geometry predicts 8 massless scalar degrees of freedom
> from Θ zero modes.**

For R_ψ ≠ 0 and finite, the KK tower has a **mass gap** m₁ = 1/R_ψ,
separating the massless zero mode from the massive KK excitations.

### 4.2 Dark Radiation Signature

The zero modes remain ultra-relativistic at early-universe temperatures
as long as T >> m₁ = 1/R_ψ.  If they decouple from the SM thermal
bath before BBN, they contribute to **dark radiation** as measured by
ΔN_eff.  See `report/UBT_delta_Neff_prediction.md` for the quantitative
estimate.

### 4.3 Connection to Spectral α Search

The spectral gap Δ₁ = (1/R_ψ)² controls the scale of the first massive
mode.  The ratio

    α_spectral ≡ λ₀ / λ₁ = 0 / 1 = 0   (zero mode is massless)

does not directly yield α.  The non-trivial spectral content for the
α-search lives in the Hecke eigenvalue spectrum of the modular forms
associated to the Θ field; see `report/hecke_modular_structure.md`.

---

## 5. Mode Degeneracy Classification

| Mode | λ (normalised) | DoF (per Θ component) | Total (8 Θ DoF) |
|------|----------------|----------------------|-----------------|
| Zero mode | 0 | 1 | **8** |
| KK level 1 | 1 (= Δ) | 2 | 16 |
| KK level 2 | 4 | 2 | 16 |
| KK level 3 | 9 | 2 | 16 |

Total massless DoF from Θ zero modes: **8** (exactly one per real DoF).

---

## 6. Open Questions

1. **Mass protection**: Is the zero mode protected by a symmetry beyond
   translation invariance in ψ (e.g., a shift symmetry for Θ)?  If so,
   the masslessness is stable against quantum corrections.

2. **Non-flat torus**: Does introducing imaginary curvature in the T²
   (complex modular parameter τ = iR_ψ/R_t → general τ ∈ ℍ) generate
   a small mass for the zero mode?

3. **Coupling strength**: What is the coupling of the Θ zero mode to SM
   particles?  This determines whether they thermalise at T > T_D.

---

## 7. Conclusion

The eigenmode analysis of the UBT Θ field on T²(τ) reveals:

- **Exactly 8 massless zero modes** (one per real biquaternion DoF)
- **Mass gap** Δ = 1/R_ψ separates the zero mode from KK excitations
- **Poisson duality** is verified: the spectral and winding sums are dual

These massless modes are the primary candidates for the dark radiation
contribution ΔN_eff discussed in the companion report.

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
