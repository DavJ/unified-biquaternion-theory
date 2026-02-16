# UBT Mathematical Engine Lock Status

**Document ID**: Final Deliverable Summary  
**Date**: February 16, 2026  
**Task**: `ubt_engine_lock_phase`

---

## Executive Summary

The Unified Biquaternion Theory (UBT) mathematical engine has been audited and locked. This document provides a one-page summary of what is **derived from Layer-0 axioms** vs what remains **phenomenological calibration** or **heuristic selection**.

---

## Engine Status

### ✅ Operator Uniqueness: **YES**

**Status**: `operator_unique = YES`

**Verdict**: The Dirac-like operator $\mathcal{D} = i \gamma^\mu \nabla_\mu$ is **uniquely determined** by Layer-0 axioms up to gauge/unitary equivalence.

**Minimal axioms required**:
1. Bundle structure: $\Theta \in \Gamma(P \times_{G_{\text{tot}}} (\mathcal{B} \otimes S \otimes V_G))$
2. Metric compatibility: $\nabla_\mu g_{\alpha\beta} = 0$
3. Torsion-free: $\Omega_\nu{}^\mu{}_\rho - \Omega_\rho{}^\mu{}_\nu = 0$
4. Clifford algebra: $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}$
5. Gauge covariance: $\nabla_\mu (U \Theta) = U (\nabla_\mu \Theta)$

**No additional axioms needed**. Alternative operators ruled out by minimal coupling principle.

**Reference**: `ubt/operators/dirac_like_operator.tex`, Section 8 (Operator Status: LOCKED)

---

### ⚠️ Quantization Derived: **PARTIAL**

**Status**: `quantization_derived = PARTIAL`

**What IS derived** (topologically protected):
- ✅ Phase winding: $n_\psi \in \mathbb{Z}$ from $\pi_1(U(1)) = \mathbb{Z}$
- ✅ Gauge holonomy: $n_{\text{hol}} \in \mathbb{Z}$ from Dirac quantization
- ✅ Chern class: $c_1 \in \mathbb{Z}$ from bundle topology

**What is NOT derived** (heuristic/calibrated):
- ❌ Prime restriction: $n_\psi \in \{2, 3, 5, 7, ...\}$ — **NOT topologically required**
- ❌ Specific value: $n_\psi = 137$ — **Empirical calibration**, not unique minimum
- ❌ RS(255,201) error-correcting codes — **Engineering optimization**, not fundamental

**Explicit theorem**: Theorem 4.1 in `ubt/quantization/winding_quantization.tex` proves prime restriction is **NOT derivable** from current axioms.

**Honest communication**:
- ❌ Avoid: "UBT predicts α⁻¹ = 137 from pure geometry"
- ✅ Use: "UBT derives $n_\psi \in \mathbb{Z}$; we calibrate $n=137$ to match observed α⁻¹"

**Reference**: `ubt/quantization/winding_quantization.tex`, Section 7 (Quantization Status: LOCKED)

---

### ✅ RG Flow Clean: **YES**

**Status**: `rg_clean = YES`

**Audit result**: All numeric insertions traced and classified.

**Parameter classification**:

| Parameter | Origin | Status |
|-----------|--------|--------|
| $\kappa_0, D_\psi, \Lambda_{\text{RG}}$ | Fitted to observations | **FREE** (3 parameters) |
| $\kappa(z), \Delta H_0/H_0, \mu_\psi$ | Computed from fits | **DERIVED** |
| $\alpha^{-1}(m_Z), M_{\text{Pl}}, H_0$ | Measured | **FIXED** |
| $n_\psi = 137$ | Calibrated to α⁻¹(m_e) | **PHENOMENOLOGICAL** |

**Symbolic β-functions** (no hard-coded numerics):
```
β_κ_ψ = (n_ψ² / 16π² R_ψ²) κ_ψ²
β_g_i = -(b_i g_i³ / 16π²) + β_g_i^ψ
```

**All appearances of 137** trace to phenomenological calibration $n_\psi = 137$, not independent numeric insertions.

**No symbolic numerology**. All numbers either:
1. Measured (α⁻¹, M_Pl, H_0)
2. Computed from measured (137² = 18769)
3. Derived from theory (β-function coefficients b_i)

**Reference**: `ubt/phenomenology/rg_flow_and_scales.tex`, Section 6 (RG Flow Status: LOCKED)

---

## What Remains Assumed (Not Derived)

### Layer-0 Assumptions

1. **Boundary conditions**: Closed manifold vs asymptotic flatness (Assumption 5.1 in Deliverable A)
2. **Test function $f$**: Specific form (e.g., $f(x) = e^{-x}$ vs $f(x) = \Theta(1-x)$) (Assumption 5.2 in Deliverable A)
3. **UV cutoff Λ**: Planck scale or earlier (not uniquely fixed)
4. **Compactification radius $R_\psi$**: Phase sector size (constrained by fits, not derived)

### Layer-2 Heuristics

1. **Prime-gating**: Restriction to prime winding numbers (Theorem 4.1: NOT derived)
2. **n = 137**: Specific winding number (calibrated, not predicted)
3. **RS(255,201)**: Error-correcting code structure (engineering, not fundamental)
4. **16 OFDM channels**: Signal processing choice (not uniquely determined)
5. **256-state grid**: Computational discretization (convergence parameter)
6. **Window functions**: Signal processing (standard practice, not physics)

---

## Falsification Criteria

### What Would Falsify UBT?

1. **Operator inconsistency**: If $I_{\text{spec}} \neq S[\Theta]/\hbar \times O(1)$ from quantum gravity observations
2. **Fractional winding**: Detection of $n_\psi \notin \mathbb{Z}$ (violates Theorem 2.1)
3. **Wrong Hubble evolution**: If $H(z) \neq H_0(1 + 0.08(1+z)^{-1})$ from JWST/Euclid
4. **Charge quantization violation**: Observation of charges not multiples of $e/3$
5. **Fine-tuning crisis**: If required κ ~ 10¹⁰ to fit data

---

## Testable Predictions

### Near-Term (JWST, Euclid, 2025–2030)

**Hubble redshift evolution**:
```
H(z) = H₀ · [1 + 0.08 · (1+z)⁻¹]
dH/dz|_{z=1} ≈ -0.04 H₀
```

**Test**: Measure $dH/dz$ independently of absolute $H_0$ calibration.

### Long-Term (Quantum Gravity, >2040)

**Spectral invariant**:
```
I_spec[Θ] = Tr[f(D²/Λ²)] should match S[Θ]/ℏ up to O(1) factors
```

**Test**: If primordial gravitational waves reveal spectrum of $\mathcal{D}^2$, compute $I_{\text{spec}}$ independently.

---

## Summary Table

| Component | Derived? | Status | Reference |
|-----------|----------|--------|-----------|
| **Dirac operator $\mathcal{D}$** | ✅ YES | Unique up to gauge | Deliverable A, §8 |
| **Spectral invariant $I_{\text{spec}}$** | ✅ YES | Gauge-invariant | Deliverable A, §5 |
| **Winding $n_\psi \in \mathbb{Z}$** | ✅ YES | Topological | Deliverable B, §2 |
| **Prime restriction** | ❌ NO | Heuristic | Deliverable B, §4, Theorem 4.1 |
| **Value $n = 137$** | ❌ NO | Calibrated | Deliverable B, §5 |
| **β-functions** | ✅ YES | Derived (1-loop) | Deliverable C, §3 |
| **Hubble tension formula** | ✅ YES | From latency | Deliverable C, §4 |
| **Layer-2 prime-gating** | ❌ NO | Engineering | Deliverable D, §3 |
| **RS(255,201) codes** | ❌ NO | Optimization | Deliverable D, §3 |

---

## Communication Guidelines

### ✅ Acceptable Claims

- "UBT uniquely derives the Dirac operator from bundle structure"
- "Topological quantization yields integer winding numbers $n_\psi \in \mathbb{Z}$"
- "RG flow predicts Hubble tension $\Delta H_0/H_0 = \kappa R_\psi \Lambda_{\text{RG}}/M_{\text{Pl}}$"
- "Layer-2 provides numerical estimators with quantified errors"
- "n = 137 is calibrated to match $\alpha^{-1}(m_e)$, not predicted a priori"

### ❌ False Claims to Avoid

- "UBT predicts α⁻¹ = 137 with no free parameters"
- "Prime-gating emerges from fundamental symmetries"
- "RS codes are ontologically required by quantum geometry"
- "Layer-2 produces fundamental constants"

---

## Integration with Existing Documentation

**Core theoretical documents**:
1. `FORMAL_INVARIANT_EXTRACTION_LAYER0.tex` — Rigorous invariant extraction
2. `LAYER0_INVARIANT_EXTRACTION_README.md` — Executive summary
3. `ubt/operators/dirac_like_operator.tex` — Operator construction (Deliverable A)
4. `ubt/quantization/winding_quantization.tex` — Quantization conditions (Deliverable B)
5. `ubt/phenomenology/rg_flow_and_scales.tex` — RG flow (Deliverable C)
6. `forensic_fingerprint/layer2_demote_heuristics.md` — Layer-2 classification (Deliverable D)

**Cross-references**:
- Operator uniqueness: Deliverable A, Theorem 3.1
- Prime restriction status: Deliverable B, Theorem 4.1
- Parameter budget: Deliverable C, Table 6.2
- Layer-2 estimator equations: Deliverable D, §2.1

---

## Conclusion

**Engine status**: ✅ **LOCKED**

The UBT mathematical engine is now formally locked with:
1. ✅ **Operator uniqueness proven** (5 axioms, no missing structure)
2. ⚠️ **Quantization partially derived** (integers YES, primes NO, n=137 NO)
3. ✅ **RG flow clean** (symbolic β-functions, classified parameters)
4. ✅ **Layer-2 demoted** (explicit estimator, no fundamental constant production)

**Hard constraints satisfied**:
- ✅ No aesthetic arguments
- ✅ No symbolic justification
- ✅ No primes unless derived (explicitly marked as NOT derived)
- ✅ Every physical claim references an equation

**Acceptance criteria**:
- ✅ D is proven unique (Theorem 3.1, Deliverable A)
- ✅ Missing axioms: NONE (all needed axioms listed)
- ✅ Quantization: integers DERIVED, primes NOT DERIVED (Theorem 4.1, Deliverable B)
- ✅ RG: no unexplained numerics (Table 6.1, Deliverable C)
- ✅ Layer-2: explicit estimator I_est ≈ I + δ (§2.1, Deliverable D)

---

**Document Version**: 1.0  
**Last Updated**: February 16, 2026  
**Maintainer**: UBT Theory Development  
**License**: CC BY-NC-ND 4.0 (theory content)
