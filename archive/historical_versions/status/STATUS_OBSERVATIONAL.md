<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Observational Tests and Predictions — Unified Biquaternion Theory

This document consolidates the current status of observational tests, CMB analysis, modified gravity predictions, and experimental proposals for the Unified Biquaternion Theory (UBT).

---

## 1. Overview

UBT makes a hierarchy of observational predictions spanning vastly different feasibility scales:

| Domain | Prediction | Feasibility |
|---|---|---|
| CMB power spectrum | Jacobi cluster k=134–143; BB peak k=139 | **Feasible now** (Planck data available) |
| CMB asymmetry | A_asym = 0.070 ± 0.015 | **Feasible now** |
| Hubble tension | Smooth H(z) interpolation at z~0.5–2 | **Feasible now** |
| Modified Schwarzschild | δ_UBT ~ 10⁻²⁰ (neutron stars) | Far future |
| BEC decoherence | Γ_UBT ~ 10⁻²⁹ Hz | Far future |
| GW multiverse | δ_φ ~ 10⁻⁶⁰ | Not foreseeable |
| Precision spectroscopy | Δν_UBT ~ 10⁻⁴ Hz | Not foreseeable |

---

## 2. CMB Power Spectrum Analysis

### 2.1 UBT Predictions for CMB

The biquaternion field Θ(q, τ) over complex time τ = t + iψ admits a decomposition:

```
Θ = Θ_S + Θ_V + i(Θ̃_S + Θ̃_V)
```

Solutions in the dispersive sector take the form:

```
Θ̃_S(θ, τ) = Σ_n c_n θ₃(n·θ, exp(-D·τ))
```

where θ₃(z, q) = Σ_{n=-∞}^{∞} q^{n²} exp(2πinz) is the Jacobi theta function, evaluated via a Feynman path integral on a toroidal configuration space.

**Three concrete UBT predictions for the CMB power spectrum:**

1. **TT Channel (dispersive sector Θ̃_S):** Broad Jacobi cluster at multipoles k = 134–143
2. **BB Channel (biquaternion sector Θ_V):** Sharp resonance at k = 139
3. **Phase-lock:** Non-random phase lock between TT(k=137) and BB(k=139); cross-channel coherence Γ(137, 139) ≈ 1

### 2.2 Spectral Fingerprint Analysis Tools

#### `jacobi_cluster_fit.py` (435 lines)

Fits the Jacobi theta function θ₃(z, q) to the k = 134–143 cluster in the CMB TT channel.

- Model: `P(k) ∝ |θ₃(k/k₀, q)|²` where `q = exp(-D·τ)`
- Outputs: fitted parameters (k₀, D, τ, amplitude), χ², physical interpretation

#### `cross_channel_phase_coherence.py` (520 lines)

Cross-channel phase coherence analyzer (TT vs BB channels).

- Statistic: `Γ(k₁, k₂) = |⟨exp(i(φ_TT - φ_BB))⟩|`
- Monte Carlo permutation testing
- Tests whether channels originate from a unified biquaternion field

#### `demo_ubt_cmb_analysis.py` (270 lines)

End-to-end workflow with synthetic data demonstrating the full analysis pipeline.

### 2.3 Observational Status

From Planck PR3 SMICA analysis:

| Channel | Signal | Significance |
|---|---|---|
| TT | Broad cluster k = 134–143 | p ≈ 0 (> 3.3σ) |
| BB | Sharp peak at k = 139 | p < 0.009 |

The twin-prime paper (`twin_prime_spectral_stability.tex`) contains a new section, "Dispersive Evolution in Complex Time," documenting the theoretical derivation leading to these predictions.

### 2.4 Court-Grade CMB Comb Test Results

A court-grade forensic fingerprint analysis was run on publicly available CMB data to test for a periodic comb signal predicted by UBT.

| Dataset | p-value | Δℓ | Verdict |
|---|---|---|---|
| Planck PR3 | 9.19×10⁻¹ | 16 | **NULL result** |
| WMAP | 1.00×10⁻⁴ | 255 | **CANDIDATE signal** |
| Combined | — | — | No confirmed CMB fingerprint |

**Files generated:**
- `forensic_fingerprint/reports/CMB_COMB_REPORT_2026-01-12.md` (624 lines)
- `forensic_fingerprint/tools/run_court_grade_cmb_comb.py`
- One-command pipeline: `bash forensic_fingerprint/tools/run_court_grade_cmb_comb.sh`

### 2.5 Technical Fix: CMB Units Mismatch Resolution

#### Problem

The CMB comb test was producing catastrophic χ²/dof ~ 10¹³ due to a units mismatch between Planck observation files and the UBT model files.

- **Planck observation format:** `Dl` format — columns `l  Dl  -dDl  +dDl`
- **Model format:** multi-column `Dl` format with different normalization conventions
- Units were not being detected robustly

#### Solution: Two-Stage Detection

1. **Header-based:** Scan comment lines for keywords `"Dl"`, `"D_l"`, `"D(l)"`, `"Cl"`, `"C_l"`, `"C(l)"`
2. **Magnitude fallback:** `median > 1000 → Dl`; otherwise `Cl`

**Conversion formula:**
```
Cl = Dl × 2π / [l(l+1)]
```

**Early detection:** Sigma validation (σ > 0, ratio checks) catches mismatch before fitting.

#### Verification

- All 8 unit tests passing after the fix
- Synthetic Planck-format files tested end-to-end
- χ²/dof is now in a reasonable range

**Files modified:**
- `forensic_fingerprint/loaders/planck.py`
- `RUNBOOK_REAL_DATA.md`
- `test_units_fix.py`

---

## 3. Modified Gravity Prediction

### 3.1 Overview

This is the first quantitative testable prediction from UBT in the gravitational sector. The derivation follows the standard effective-field-theory approach applied to the biquaternionic loop expansion.

### 3.2 Modified Schwarzschild Metric

```
ds²_UBT = -(1 - 2GM/r + δ_UBT(r)) dt²
        + (1 - 2GM/r + δ_r(r))⁻¹ dr²
        + r² dΩ²
```

**Correction term:**

```
δ_UBT(r) = α_UBT · (GM/r)² · (ℓ_P/r)²
          = 26.3 · (GM)² · ℓ_P² / r⁴
```

where:

```
α_UBT = 8π²/3 ≈ 26.3
```

derived from biquaternionic one-loop corrections with enhancement factor:

```
α_UBT = 8π² · (N_internal / 3) ≈ 8π²/3,   N_internal = 1
```

### 3.3 Derivation Path

1. **One-loop effective action:**
   ```
   S_eff[G] = S_Einstein[G] + S_1-loop[G]
   ```

2. **Heat kernel expansion:**
   ```
   Tr[e^{-t∇†∇}] ~ (4πt)^{-2} ∫ d⁴x √g [1 + tR/6 + ...]
   ```

3. **Renormalization counterterms** are computed from the divergent part of the heat kernel.

4. **Schwarzschild vacuum** (R = 0):
   ```
   R_μνλσ R^μνλσ = 48(GM)² / r⁶
   ```

5. **Metric correction:**
   ```
   δg_tt = -c₃ · (GM)² · ℓ_P² / r⁴
   ```
   where c₃ arises from biquaternionic loop integrals.

### 3.4 Numerical Estimates

| System | Radius | δ_UBT | Status |
|---|---|---|---|
| Earth surface | 6.4 × 10⁶ m | ~ 10⁻⁸⁰ | Unmeasurable |
| Sun surface | 7 × 10⁸ m | ~ 10⁻⁷⁵ | Unmeasurable |
| Neutron star | 10 km | ~ 10⁻²⁰ | Potentially future detectors |
| Black hole | 100 km | ~ 10⁻²³ | Future detectors |

**Gap to LIGO/Virgo sensitivity:** ~ 10⁴⁴–10⁴⁶ orders of magnitude.

### 3.5 Honest Assessment

The effect is unobservable with current or any foreseeable technology. However, the derivation demonstrates that the biquaternionic framework produces finite, well-defined quantitative predictions consistent with the known structure of quantum corrections to GR. This validates the internal consistency of the theoretical machinery.

---

## 4. Hubble Tension: Metric Latency Proposal

### 4.1 Background

The Hubble tension is a > 5σ discrepancy between:

- **CMB (early universe):** H₀ ≈ 67.4 km/s/Mpc
- **Local measurements:** H₀ ≈ 73.0 km/s/Mpc

UBT offers a speculative mechanism: effective metric or time-parameter latency that causes the inferred Hubble constant to differ systematically between early- and late-universe probes.

**Source file:** `speculative_extensions/appendices/appendix_HT_hubble_tension_metric_latency.tex` (553 lines, 34 equations)

### 4.2 Mathematical Framework

**Minimal extension** (covariant, diffeomorphism-invariant):

```
dτ = dt (1 + ε f(z)),   f(z) = β z
```

**Derived effective Hubble parameter:**

```
H_eff = H / (1 + ε f(z))
```

**Required parameter:** `εβ ≈ 8 × 10⁻⁴` (ε ~ 0.08%, small but plausible)

### 4.3 Validation Tests

| Test | Result | Notes |
|---|---|---|
| GR Consistency | ✓ PASS | Covariance preserved |
| ΛCDM Background | ✓ PASS | Expansion history unchanged |
| BAO Measurements | ✓ PASS | Corrections ~0.02%, below 1% precision |
| CMB Acoustic Peaks | ⚠️ REQUIRES NUMERICAL VERIFICATION | Potential cancellation in θ_A ratio |
| Cosmic Chronometers | ✓ LIKELY PASS | — |
| Structure Growth | ✓ PASS | Corrections ~0.2%, within constraints |

### 4.4 Possible Physical Interpretations

1. **Effective metric averaging (backreaction):** Challenges noted; not straightforward
2. **Measurement protocol dependence:** Most plausible interpretation
3. **Higher-order GR corrections:** Possible
4. **Quantum gravity effects:** Effectively ruled out (requires ψ >> Planck scale)

### 4.5 Status

**VIABLE BUT CONSTRAINED.** Parameter window `εβ ~ (5–10) × 10⁻⁴` (narrow but plausible). No compelling physical mechanism has been identified yet to derive ε from first principles within UBT.

### 4.6 Key Prediction and Falsification

**Key prediction:** High-precision H(z) measurements at z ~ 0.5–2 should reveal smooth interpolation between early- and late-universe values with no discontinuity.

**Falsification criteria:**
- CMB acoustic peak positions inconsistent with `εβ ~ 10⁻³`
- BAO measurements showing a discontinuity in the distance-redshift relation
- Cosmic chronometers rejecting the smooth interpolation ansatz

---

## 5. Other Experimental Proposals (Transition Criterion Tests)

These proposals target the UBT transition criterion `ℑ(∇_μ Θ† Θ) = 0`, which governs the boundary between quantum and classical behavior in the biquaternionic framework.

### 5.1 Experiment 1: Ultra-Cold Atom Interferometry

- **System:** BEC (⁸⁷Rb or ²³Na), T < 100 nK, N ~ 10⁵ atoms
- **Observable:** Excess decoherence rate `Γ_UBT = α_branch · N · m / ℏ`
- **Estimate:** `α_branch ~ 10⁻⁴⁰`; `Γ_UBT ~ 10⁻²⁹ Hz` (coherence time ~ 10²¹ years)
- **Enhanced scenario:** Gravitational cat states, M ~ 1 μg, Δx ~ 1 μm → coherence time ~ 300 years
- **Conclusion:** CHALLENGING; conceivable only in the far future

### 5.2 Experiment 2: Gravitational Wave Multiverse Signatures

- **Method:** Cross-correlation of GW events from binary mergers
- **Expected signature:** `S_multiverse(f) ~ ε² · N_branches · f⁻³` with ε ~ 10⁻⁶⁰
- **Estimate:** `δ_φ ~ 10⁻⁶⁰`, too small for individual events or any foreseeable correlation analysis
- **Conclusion:** Not feasible with any foreseeable technology

### 5.3 Experiment 3: Precision Spectroscopy

- **UBT predicts corrections** to atomic transitions arising from imaginary-time geometry
- **Estimate:**
  ```
  Δν_UBT ≈ α_transition × (m_e c²) × (R_e / R_Bohr)² ~ 10⁻⁴ Hz
  ```
- **Context:** Natural linewidth ~ 10⁸ Hz; ratio `Δν_UBT / Δν_natural ~ 10⁻¹²`
- **Conclusion:** 12 orders of magnitude below current experimental precision

### 5.4 Experiment 4: CMB Anomaly Analysis (**HIGH PRIORITY — FEASIBLE**)

- **Data:** Planck 2018 (publicly available now)
- **Method:** MCMC analysis with UBT-specific spectral templates
- **UBT prediction:** `A_asym = 0.070 ± 0.015` (power spectrum suppression at low-ℓ)
- **Current observation:** `A_asym = 0.072 ± 0.020` (consistent within 1σ)
- **Falsification:** If `A_MV < 0.05` → rules out simplest UBT models
- **Timeline:** ~18 months from start
- **Estimated cost:** ~$100k
- **Probability of detection:** 10–20%

---

## 6. Observational Priority Summary

| Experiment | UBT Prediction | Gap to Feasibility | Priority |
|---|---|---|---|
| CMB anomaly analysis | A_asym = 0.070 | **Feasible now** | **HIGH** |
| Hubble tension H(z) | Smooth interpolation z~0.5–2 | **Feasible now** | **HIGH** |
| CMB spectral fingerprint | Jacobi cluster k=134–143 | **Feasible now** | **HIGH** |
| Modified gravity (neutron star) | δ_UBT ~ 10⁻²⁰ | Future detectors | Medium (long-term) |
| Modified gravity (BH) | δ_UBT ~ 10⁻²³ | Future detectors | Medium (long-term) |
| BEC interferometry | Γ ~ 10⁻²⁹ Hz | ~10⁻²¹× current sensitivity | Low |
| Spectroscopy | Δν ~ 10⁻⁴ Hz | ~10⁻¹²× current precision | Very Low |
| GW multiverse | δ_φ ~ 10⁻⁶⁰ | ~10⁻³⁸× current sensitivity | Very Low |

### Immediate Next Steps

1. **CMB asymmetry MCMC:** Run MCMC on Planck 2018 data using UBT templates; check A_asym against prediction 0.070 ± 0.015.
2. **CMB comb follow-up:** Investigate WMAP CANDIDATE signal (Δℓ = 255, p = 1×10⁻⁴); cross-check with Planck at same Δℓ.
3. **Hubble tension H(z):** Compile existing cosmic chronometer data at z ~ 0.5–2; fit smooth interpolation model; test εβ ~ 8×10⁻⁴.
4. **CMB acoustic peaks:** Perform full numerical verification of the εβ ~ 10⁻³ constraint from the Hubble tension metric latency model.
