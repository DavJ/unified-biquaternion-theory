# Lepton Ratios Forensic Audit — Inventory

**Date**: 2026-02-28  
**Audit scope**: Reproduce or refute the claims of Appendix W:
- `m_μ/m_e ≈ 207.3`
- `m_τ/m_μ ≈ 16.9`

---

## Files Searched

Keywords searched: `Appendix W`, `m_mu/m_e`, `m_tau/m_mu`, `207`, `16.9`, `E_{0,1}`, `E_{0,2}`,
`eigenmode`, `torus`, `radius`, `R`, `scale`, `Lambda`.

---

## Files Found and Claims

### 1. `consolidation_project/appendix_W2_lepton_spectrum.tex`

**Primary source** for the lepton-ratio claims.

| Section | Claim |
|---------|-------|
| W.1 | Electron arises as the first non-trivial Dirac eigenmode on compact torus T²(τ) |
| W.2 | Dirac operator eigenspectrum: `E_{n,m} = (1/R) √[(n+δ)² + (m+δ')²]` |
| W.3 | Electron identified with mode (0,1): `m_e = E_{0,1} ≈ 1/R` with `δ=½` |
| W.4 | Muon identified with (0,2), tau with (1,0) or (1,1) |
| W.5 | Claims `E_{0,2}/E_{0,1} ≈ 207.3` and `E_{1,0}/E_{0,2} ≈ 16.9` |
| W.T | Table lists eigenvalue `√((0+½)²+2²)` for (0,2) and says ratio-to-E_{0,1} ≈ 207.3 |

**Critical observation**: The table entry for (0,2) gives the correct *eigenvalue* formula
`√((0+½)²+2²) = √4.25 ≈ 2.062`, but then asserts the *ratio* to E_{0,1} is ≈ 207.3.
These two statements are mutually inconsistent: `√4.25 / √1.25 ≈ 1.844`, not 207.3.

---

### 2. `consolidation_project/appendix_V2_emergent_alpha.tex`

Claims the torus modulus `τ = iy_*` is dynamically fixed by minimising a one-loop Casimir
effective potential at scale `μ₀ ~ M_Z`.  
Provides the formula `α(M_Z)⁻¹ = 4πN/y_*` with `N=10`.  
The modulus value `y_*` is referenced by Appendix W ("For τ = τ_* determined in Appendix V …"),
but the eigenvalue formula in Appendix W **does not include `y_*`** explicitly.

---

### 3. `consolidation_project/appendix_G6_neutrino_mass_biquaternionic_time.tex`

Uses `R` (torus radius) and Majorana scale `M_R = (ℏc)/R_eff`.  
Does not independently predict `m_μ/m_e` or `m_τ/m_μ`.

---

### 4. `consolidation_project/appendix_K5_Lambda_QCD.tex`

Uses `μ = R⁻¹` as a matching scale for QCD running coupling.  
Does not predict lepton mass ratios.

---

### 5. `consolidation_project/appendix_FORMAL_constants_normalization.tex`

Defines normalisation conventions; references `R`, `Λ`, `ℏc`.  
No independent lepton-ratio claim.

---

## Summary

The **only** source for the 207.3 and 16.9 claims is `appendix_W2_lepton_spectrum.tex`.  
The eigenvalue formula given there is `E_{n,m} = (1/R)√[(n+δ)²+(m+δ')²]`.  
Evaluating this formula **directly** gives:

| Mode (n,m) | δ | δ' | E·R     | E_{n,m}/E_{0,1} |
|------------|---|----|---------|-----------------|
| (0,1)      | ½ | 0  | 1.11803 | 1.000           |
| (0,2)      | ½ | 0  | 2.06155 | 1.844           |
| (1,0)      | ½ | 0  | 1.50000 | 1.342           |
| (1,1)      | ½ | 0  | 1.80278 | 1.612           |

None of these ratios reproduce 207.3 or 16.9.  
See `reproduction.md` and `missing_step.md` for detailed analysis.
