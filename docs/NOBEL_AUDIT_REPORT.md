# PHASE 0 — VERIFICATION AUDIT REPORT
**Unified Biquaternion Theory (UBT)**  
**Mode: Verification + Extraction (No New Physics)**  
**Date: 2026-03-03**

---

## SCOPE

This report audits three existing UBT claims for reproducibility, parameter freedom, and falsifiability:

- **Claim A**: Hubble tension resolution (~8%)
- **Claim B**: Fine-structure constant derivation (α⁻¹ ≈ 137.036)
- **Claim C**: SU(3) coupling relation predictions (g₃ : g₂ : g₁)

---

## CLAIM A — HUBBLE TENSION RESOLUTION (~8%)

### Location in Repository

| File | Description |
|------|-------------|
| `ubt_with_chronofactor/papers/nobel_assault/T1_hubble_tension_derivation.tex` | Primary derivation paper |
| `speculative_extensions/appendices/appendix_HT_hubble_tension_metric_latency.tex` | Extended analysis (~550 lines) |
| `HUBBLE_LATENCY/` | Supplemental calibration scripts |
| `ubt_with_chronofactor/papers/nobel_assault/nobel_assault_status.md` | Status summary |
| `HUBBLE_TENSION_IMPLEMENTATION_SUMMARY.md` | Implementation overview |

### Input Assumptions

1. **Imaginary time compactification**: ψ is compactified with period 2πR_ψ (natural in UBT).
2. **Information channel structure**: N = 16 channels from GF(2⁸) → GF(2⁴) dimensional reduction.
3. **Frame structure**: F = 256 ticks per effective frame (from GF(2⁸) field capacity).
4. **Overhead model**: O = b + (N−1)·k·(2−η), where b ≈ 2 (frame transition), k = 1 (per-channel cost), η ∈ [0.80, 0.95] (efficiency factor).

### Key Derivation

Effective time dilation from information-theoretic latency:

```
δ = O/F ≈ 19/256 ≈ 0.074

H₀^late / H₀^early = 1/(1 − δ) ≈ 1.080

ΔH₀/H₀ ≈ 8.0 ± 1.0%
```

Observed tension (Riess et al. 2021, Planck 2018):  
H₀^Planck ≈ 67.4 ± 0.5 km/s/Mpc, H₀^SH0ES ≈ 73.0 ± 1.0 km/s/Mpc → ~8.3% discrepancy.

### Free Parameters

| Parameter | Value | Status |
|-----------|-------|--------|
| N (channels) | 16 | **Derived** from GF(2⁸)→GF(2⁴) |
| F (frame size) | 256 | **Derived** from GF(2⁸) field |
| b (frame transition) | 2 | **Estimated** (information theory) |
| k (per-channel cost) | 1 | **Estimated** (minimal) |
| η (efficiency) | 0.875 ± 0.075 | **Estimated** (not uniquely derived) |

**Effective free parameter count**: ~1 (efficiency η), constrained within [0.80, 0.95].

### Mathematical Status

**HEURISTIC / PARTIAL**

- Metric emergence from biquaternionic field: formally stated.
- Hubble ratio formula H_late/H_early = 1/(1−δ): rigorously derived from effective time dilation.
- Overhead model O = b + (N−1)k(2−η): physically motivated but not uniquely derived from UBT axioms.
- Channel count N = 16 from GF(2⁸)/GF(2⁴): claimed as structural but dimensional reduction steps not fully proven.

### Numerical Reproducibility

**YES** — The key formula δ = O/F with O ≈ 19, F = 256 gives δ ≈ 0.074 and ΔH₀/H₀ ≈ 8.0%. This is numerically reproducible given the parameter values. Python calibration script available in `HUBBLE_LATENCY/calibration/calibrate_hubble_latency.py`.

### Uses Fitting?

**NO** — Numerical values N, F are claimed as structural (not fitted to H₀ data). The efficiency η is estimated but not tuned post-hoc to match observation. However, the agreement should be regarded as approximate confirmation rather than zero-parameter prediction because η is not uniquely fixed by first principles.

### Falsifiable?

**YES**

- Prediction: δ(z) = constant (redshift-independent). Falsified if H(z) measurements show δ(z) varies by >10% across 0.1 < z < 1100.
- Standard sirens: H₀^GW = H₀^EM within 5%. Falsified by LISA/Einstein Telescope data showing >5% discrepancy.
- CMB phase comb: No periodic modulation at ℓ ~ 256. Falsified by detection of comb at >5σ.

---

## CLAIM B — FINE-STRUCTURE CONSTANT DERIVATION (α⁻¹ ≈ 137.036)

### Location in Repository

| File | Description |
|------|-------------|
| `original_release_of_ubt/solution_P4_fine_structure_constant/alpha_constant_derivation.tex` | Primary derivation |
| `original_release_of_ubt/solution_P4_fine_structure_constant/alpha_constant_derivation_precise.tex` | One-loop correction detail |
| `ubt_with_chronofactor/papers/nobel_assault/T3_alpha_from_spectrum.tex` | Spectral invariant approach |
| `consolidation_project/appendix_V2_emergent_alpha.tex` | Consolidated derivation |
| `alpha_core_repro/alpha_two_loop.py` | Numerical validation |
| `original_release_of_ubt/validation/validate_alpha_constant.py` | Validation script |

### Input Assumptions

1. **Spectral action principle**: Gauge couplings arise from Tr[f(D²/Λ²)] (standard in noncommutative geometry / Connes).
2. **Winding quantization**: ψ-periodicity requires integer winding n_ψ ∈ ℤ (natural in UBT).
3. **Anomaly cancellation**: Standard Model chiral anomaly structure (Σ Q³ = 0).
4. **Prime restriction (selection principle)**: Only prime winding numbers are topologically stable (spectral entropy = 0 for primes).
5. **Energetic selection**: S(n) ≈ A·n² − B·n·ln(n) is minimized for n = 137 among primes.

### Key Derivation

Step 1: Topological quantization yields α₀⁻¹ = n_ψ (integer).  
Step 2: Prime-gated stability + energy minimization selects n_ψ = 137.  
Step 3: QED 1-loop vacuum polarization (derived, not fitted) yields δ_QED ≈ 0.036.  
Step 4: α⁻¹ = n_ψ + δ_QED = 137 + 0.036 = 137.036.

Experimental: α⁻¹ = 137.035999... (CODATA 2018). Agreement: <0.001%.

### Free Parameters

| Parameter | Value | Status |
|-----------|-------|--------|
| n_ψ (winding number) | 137 | **Selected** by prime-gated stability (not externally fitted) |
| δ_QED (loop correction) | 0.036 | **Derived** from QED 1-loop running |
| A, B (action coefficients) | implicit | **Not uniquely derived** from UBT axioms |

**Effective free parameter count**: 0 if prime-gating selection is accepted; 1 if n_ψ = 137 is treated as empirical calibration.

### Mathematical Status

**PARTIAL**

- Topological quantization n_ψ ∈ ℤ: **rigorous** (follows from periodicity of ψ).
- Spectral action framework (Connes): **rigorous** (established literature).
- Prime restriction: **heuristic** — entropy argument physically motivated but not rigorously derived from spectral structure.
- Selection of n_ψ = 137 as unique prime minimum: **heuristic** — verified numerically for S(n) = A·n² − B·n·ln(n) but A, B not derived from first principles.
- QED 1-loop correction δ_QED ≈ 0.036: **rigorous** (standard QFT calculation).

### Numerical Reproducibility

**YES** — Scripts in `alpha_core_repro/alpha_two_loop.py` and `original_release_of_ubt/validation/validate_alpha_constant.py` reproduce the two-loop running. The bare value n_ψ = 137 is asserted, not computed from axioms; however, the QED running is fully reproducible.

### Uses Fitting?

**BORDERLINE** — n_ψ = 137 is selected by a principle (prime stability + energy minimization), not directly fitted to α_exp. However, the action parameters A, B are not derived, and the selection mechanism relies on an unproven prime-gating conjecture. The claim "0 free parameters" holds only if the full selection principle is accepted.

### Falsifiable?

**YES**

- Bare coupling: α_bare⁻¹ = 137 (exact integer). Falsified if QED corrections shift bare value away from integer.
- Running of α: Must follow standard QED running below M_Z. Falsified by >5σ deviation.
- Integer winding: Imaginary-time winding n_ψ = 137. Falsified by any future quantum gravity probe measuring n_ψ ≠ 137.

---

## CLAIM C — SU(3) COUPLING RELATION PREDICTIONS

### Location in Repository

| File | Description |
|------|-------------|
| `Appendix_G_Emergent_SU3.tex` | SU(3) from quaternionic phase structure |
| `SM_GAUGE_GROUP_RIGOROUS_DERIVATION.md` | Formal derivation of SM gauge group from Aut(B⁴) |
| `canonical/interactions/sm_gauge.tex` | SM gauge interactions in UBT |
| `consolidation_project/appendix_C_electromagnetism_gauge_consolidated.tex` | EM/gauge derivation |
| `ubt_rge.py` | RGE runner for coupling evolution |

### Input Assumptions

1. **Biquaternion algebra**: ℬ = ℂ ⊗ ℍ ≅ Mat(2,ℂ), with Aut(ℬ) ⊃ SU(3)×SU(2)×U(1).
2. **Phase structure**: Three quaternionic axes (i, j, k) ↔ three color charges (R, G, B).
3. **Spectral action normalization**: Coupling constants arise from Seeley-DeWitt coefficients.
4. **RGE running**: SM renormalization group equations used to evolve couplings from high scale.

### Mathematical Status

**PARTIAL / HEURISTIC**

- SU(3) emergence from 3 quaternionic phase axes: **plausible structural correspondence**, not proven gauge group isomorphism.
- SU(2)_L × U(1)_Y from complex structure: **argued** but not uniquely derived.
- Explicit coupling ratio prediction g₃:g₂:g₁ at a common scale: **not computed** in existing documents. The documents establish that the gauge group is contained in Aut(B⁴) but do not produce explicit numerical predictions for coupling ratios without additional assumptions (e.g., GUT-scale unification).

### Numerical Reproducibility

**PARTIAL** — `ubt_rge.py` provides RGE evolution machinery, but coupling unification prediction requires specifying an input scale and initial values, which are not uniquely determined by UBT axioms in the current documents. The RGE runner uses SM experimental inputs as placeholders.

### Uses Fitting?

**YES (IMPLICIT)** — Current implementation in `ubt_rge.py` uses experimental SM fermion masses and coupling constants as inputs, not UBT-derived predictions.

### Falsifiable?

**IN PRINCIPLE YES, BUT CLAIM IS INCOMPLETE** — A falsifiable prediction requires explicit g₃:g₂:g₁ ratios at a specified energy scale derived from UBT alone. These are not yet extracted. The SM group emergence is structural but coupling normalization remains undetermined.

---

## SUMMARY TABLE

| | Claim A (Hubble) | Claim B (α) | Claim C (Gauge) |
|---|---|---|---|
| **Mathematical status** | Heuristic/Partial | Partial | Heuristic/Partial |
| **Numerical reproducibility** | Yes | Yes (partial) | Partial |
| **Uses fitting?** | No (1 estimate) | Borderline | Yes (implicit) |
| **Falsifiable?** | Yes | Yes | In principle |
| **Key gap** | η not uniquely derived | Prime selection heuristic | Coupling ratios not extracted |

---

## GLOBAL ASSESSMENT

### Success Condition Evaluation

**Condition A**: "A numerical prediction matches known anomaly without tuning."  
→ **Partially met**: Hubble tension prediction ΔH₀/H₀ ≈ 8.0 ± 1.0% matches observed ~8.3% with ~1 estimated parameter (η). The agreement is real but not zero-parameter.

**Condition B**: "A new testable deviation from ΛCDM or SM is identified."  
→ **Met**: The UBT Hubble latency predicts redshift-independent δ(z), distinguishable from all dynamical Hubble tension models. This is a novel, testable signature.

**Condition C**: "A coupling relation emerges naturally and differs from GUT expectations."  
→ **Not yet met**: The structural derivation of SM gauge group from Aut(B⁴) is present, but explicit coupling ratio predictions have not been extracted and compared to GUT expectations.

### Recommendation

> **Do not escalate Claim C** until coupling ratio predictions are explicitly computed from UBT axioms without SM experimental inputs.  
> **Proceed with Claim A** (Hubble) and **Claim B** (α) as the strongest candidates, with honest labeling of heuristic elements.

---

*Audit performed under Global Rules: no axiom modification, extraction and verification only.*
