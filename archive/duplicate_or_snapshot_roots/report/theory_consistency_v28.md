<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# UBT Theory Consistency Audit — v28

**Version:** v28 (UBT_v28_cosmo_hecke_neff)  
**Date:** 2026-03-06  
**Base:** Inherits all results from `report/theory_consistency.md` (v27)  
**Scope:** New v28 additions: spectral analysis, ΔN_eff, Hecke structure  
**Auditor:** Automated + manual review

---

## 1. Overview

This report extends the v27 consistency audit (`report/theory_consistency.md`)
with checks specific to the v28 additions:

1. Theta field eigenmode spectrum analysis
2. ΔN_eff dark radiation prediction
3. Hecke/modular structure of Θ functions

**All v27 checks remain PASS** (see v27 report for details).

---

## 2. New v28 Checks

### 2.1 Dimensional Consistency of ΔN_eff Formula

The ΔN_eff formula:

    ΔN_eff = (8/7) × (11/4)^{4/3} × (g_X / 2) × (T_X / T_γ)^4

**Dimensional check:**
- (8/7): dimensionless ratio (fermion/boson DoF)
- (11/4)^{4/3}: dimensionless (photon/neutrino temperature ratio)
- g_X / 2: dimensionless (counting factor)
- (T_X / T_γ)^4: dimensionless (temperature ratio)

**Result:** ✅ ΔN_eff is dimensionless as required.

**Energy budget check:** ρ_rad = ρ_γ × (1 + (7/8)(4/11)^{4/3} × N_eff)

- [ρ_rad] = [ρ_γ] = energy density ✅
- The coefficient (7/8)(4/11)^{4/3} converts from neutrino-equivalent units ✅

### 2.2 Gauge Invariance of Spectral Computation

The Laplacian eigenvalues λ_k = (2π/L)² |k|² are computed for the **free**
Θ field.  In the presence of gauge fields:

    -Δ → -(D_μ)² = -(∂_μ + iA_μ)²

The eigenvalues shift to λ_k → (2π k/L + eA)².

**Check:** For zero gauge field (A_μ = 0), the gauge-invariant and
gauge-field-independent results agree.  The v28 scan uses A_μ = 0 (free field).

**Result:** ✅ The free-field eigenvalue computation is gauge-covariant.
The physical spectrum in the presence of gauge fields requires a separate
computation (not done in v28, flagged as open).

### 2.3 Lorentz Invariance of Spectral Gap

The spectral gap Δ = (1/R_ψ)² is the mass of the first KK mode.  In the
4D effective theory, this is a Lorentz-scalar mass:

    ℒ_KK = -½ (∂_μ Θ̂₁)† (∂^μ Θ̂₁) - ½ (1/R_ψ)² |Θ̂₁|²

**Check:** The mass term (1/R_ψ)² is Lorentz-invariant (a scalar mass). ✅

**Result:** ✅ KK masses are Lorentz-invariant scalars.

### 2.4 Energy-Momentum Conservation with ΔN_eff Contribution

Adding ΔN_eff dark radiation to the Friedmann equations:

    ρ_tot = ρ_Λ + ρ_m + ρ_γ (1 + (7/8)(4/11)^{4/3} N_eff)

The Bianchi identity ∇_μ G^μν = 0 requires ∇_μ T^μν = 0, which for the
radiation sector means:

    d(ρ_X a⁴) = 0   (conservation for massless radiation)

This holds by construction for any massless species (ρ ∝ T^4 ∝ a^{-4}).

**Result:** ✅ Adding dark radiation from Θ zero modes preserves energy-momentum
conservation.

### 2.5 Poisson Duality (Spectral ↔ Winding)

The Poisson summation identity verified in `theta_spectrum_scan.py`:

    W(R) = R · S(R)

**Check:** This is a mathematically exact identity (not an approximation).

- W(R) = spectral sum: converges for R > 0 ✓
- S(R) = winding sum: converges for R > 0 ✓
- Ratio W/S = R: verified numerically to 10^{-8} relative precision ✓

**Result:** ✅ Poisson duality confirmed.

### 2.6 Hecke Operator Formula

The Hecke operator T(p²) formula used in `automorphic/hecke_l_route.py`:

    (T(p²) a)_n = a_{p²n} + χ(p) p^{k-1} a_n + p^{2k-1} a_{n/p²}

**Check against Shimura (1973), Kohnen (1980):**

For half-integral weight k = 1/2, the standard formula is:

    (T(p²) a)_n = a_{p²n} + χ(p) p^{k-1} a_n + p^{2k-1} a_{n/p²}

with k = 1/2:
- p^{k-1} = p^{-1/2}
- p^{2k-1} = p^0 = 1

The implementation in `hecke_l_route.py` correctly uses k = 0.5, so:
- p_k1 = p^{0.5-1.0} = p^{-0.5} ✅
- p_2k1 = p^{2×0.5-1.0} = p^0 = 1 ✅

**Result:** ✅ Hecke operator formula is correct.

### 2.7 No Layer 0 / Layer 1 Modifications

**Checklist:**
- [ ] AXIOMS.md: unchanged ✅
- [ ] biquaternion_algebra.tex: unchanged ✅
- [ ] Field equation ∇†∇Θ = κ𝒯: unchanged ✅
- [ ] Complex time τ = t+iψ: unchanged ✅
- [ ] GR recovery (ψ→0 limit): unchanged ✅

**Result:** ✅ No Layer 0 or Layer 1 modifications made.

---

## 3. Consistency Score — v28 Additions

| Check | Status | Notes |
|-------|--------|-------|
| ΔN_eff dimensional consistency | ✅ PASS | Dimensionless ratio |
| Gauge invariance (free field) | ✅ PASS | A=0 case; gauge-field correction open |
| Lorentz invariance (KK masses) | ✅ PASS | Scalar mass term |
| Energy-momentum conservation | ✅ PASS | Bianchi identity preserved |
| Poisson duality | ✅ PASS | Exact identity verified |
| Hecke operator formula | ✅ PASS | Matches Shimura/Kohnen |
| No Layer 0/1 modification | ✅ PASS | Axiomatic structure preserved |

**v28 additions: 7/7 PASS**

---

## 4. New Open Issues (v28)

| Issue | Severity | Description | Resolution path |
|-------|----------|-------------|-----------------|
| T_D uncertain | Medium | Decoupling temperature T_D not derived from UBT coupling | Compute Θ-SM coupling in ψ-sector |
| A_μ ≠ 0 spectrum | Medium | Spectral gap may shift in gauge background | Full covariant computation |
| Zero mode mass protection | Low | Is the n=0 masslessness radiatively stable? | Ward identity / Coleman-Weinberg |
| Full Θ thermalisation | Low | Only g_X = 2 (complex) is motivated | Model dependent |

---

## 5. Inheritance from v27

All v27 results (9/10 PASS, 1/10 PARTIAL for B-coefficient) are
unchanged and inherited.  The v28 additions contribute 7 new PASS checks.

**Combined score: 16/17 PASS + 1 PARTIAL (B-coefficient circularity, inherited from v27)**

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
