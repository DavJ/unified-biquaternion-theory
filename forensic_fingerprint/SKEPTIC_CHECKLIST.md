# Skeptical Counter-Argument Checklist

**Document Purpose**: Court-grade documentation of systematic error controls and counter-arguments for the CMB comb test.

**Status**: Living document, updated with each test refinement  
**Last Updated**: 2026-01-11  
**Protocol Version**: v1.0

---

## Overview

This checklist documents potential systematic errors, confounds, and counter-arguments that could invalidate or weaken claims from the CMB comb fingerprint test. For each counter-argument, we document:

1. **The skeptical argument** (strongest form)
2. **How we addressed it** (implementation details)
3. **Residual risk** (what remains uncontrolled)
4. **Status** (✓ ADDRESSED / ⚠ PARTIAL / ✗ OPEN)

This is a **living document**. New counter-arguments are added as they are identified, and status is updated as controls are implemented.

---

## 1. Look-Elsewhere Effect (Multiple Testing)

### Skeptical Argument

> **"You searched through multiple candidate periods. One of them will appear significant by chance even if there's no signal. Your p-value doesn't account for the family-wise error rate."**

### How We Addressed It

**Implementation**: Monte Carlo max-statistic method (pre-registered)

- **Candidate periods**: Fixed set [8, 16, 32, 64, 128, 255] (LOCKED before analysis)
- **Null distribution**: For each MC trial, compute Δχ² for ALL candidate periods and record max
- **P-value**: Fraction of trials where max(Δχ²_null) ≥ max(Δχ²_obs)
- **Effect**: P-value includes penalty for testing multiple periods

**Code**: `forensic_fingerprint/cmb_comb/cmb_comb.py::monte_carlo_null_distribution()`

**Validation**: Synthetic null tests (ΛCDM with no periodic structure) should produce uniform p-values.

### Residual Risk

- **Period selection bias**: The candidate set includes 255 (predicted by RS theory). If we chose this post-hoc, it would be circular.
  - **Mitigation**: Period 255 was pre-registered in UBT theory papers before data analysis began (see `PROTOCOL.md`).
  
- **Trials factor**: We test 6 periods, so naive Bonferroni would be p_corrected = 6 × p_raw. Max-statistic is less conservative but valid.

### Status

✓ **ADDRESSED** — Max-statistic method implemented and validated.

---

## 2. Data Units Mismatch (C_ℓ vs D_ℓ)

### Skeptical Argument

> **"Your residuals might have units mismatch. If the observation is in D_ℓ = ℓ(ℓ+1)C_ℓ/2π but the model is in C_ℓ, or vice versa, you'll get spurious structure."**

### How We Addressed It

**Implementation**: χ²/dof sanity check

- **Check**: After computing residuals, we compute χ²/dof = Σ(r²) / (N - k)
- **Expected**: For correct units and good model fit, χ²/dof ≈ 1.0
- **Warning threshold**: If χ²/dof > 10 or < 0.1, emit warning

**Code**: `forensic_fingerprint/cmb_comb/cmb_comb.py::compute_residuals()`

**Validation**: Test with known-good data (same file for obs and model → residuals = 0 → χ² = 0).

### Residual Risk

- **Manual inspection required**: Automated check can't definitively prove units are correct, only flag gross errors.
- **Model quality**: High χ²/dof could also mean poor model fit (not just units), so interpretation requires judgment.

### Status

✓ **ADDRESSED** — Automated check implemented. Court-grade runs require χ²/dof review.

---

## 3. Covariance Matrix Errors

### Skeptical Argument

> **"Your covariance matrix might be wrong (numerical errors, wrong binning, etc.). If Cov is invalid, whitening produces garbage and p-values are meaningless."**

### How We Addressed It

**Implementation**: Covariance validation suite

- **Symmetry check**: Verify C = C^T (tolerance 1e-10)
- **Positive definiteness**: Compute eigenvalues, verify all λ ≥ 0
- **Condition number**: Compute κ = λ_max / λ_min, warn if κ > 1e10
- **Regularization**: Apply ridge jitter (λI) if needed for numerical stability
- **Calibration test**: Generate N(0, Cov) samples, whiten them, verify variance ≈ 1 and correlations ≈ 0

**Code**:
- `forensic_fingerprint/cmb_comb/cmb_comb.py::validate_covariance()`
- `forensic_fingerprint/cmb_comb/cmb_comb.py::calibrate_whitening()`
- `forensic_fingerprint/whitening.py::build_whitener()`

**Validation**: Calibration test runs automatically if `--whiten full` is used.

### Residual Risk

- **Covariance source uncertainty**: We rely on Planck/WMAP published covariance matrices. Errors in the published data propagate to our results.
- **Regularization impact**: Ridge regularization (jitter) can slightly alter results. We document jitter parameter for reproducibility.

### Status

✓ **ADDRESSED** — Full validation suite implemented. Regularization documented.

---

## 4. Independent Replication (Planck vs WMAP)

### Skeptical Argument

> **"Planck alone could show a fluke. You need independent confirmation from WMAP (or other datasets) to rule out Planck-specific systematics."**

### How We Addressed It

**Implementation**: Two-dataset protocol (pre-registered)

- **Primary**: Planck PR3 TT spectrum (ℓ = 30-1500)
- **Replication**: WMAP 9yr TT spectrum (ℓ = 30-800)
- **PASS criteria** (all required):
  1. Planck p < 0.01
  2. WMAP p < 0.05 (weaker threshold due to lower sensitivity)
  3. Same best-fit period in both datasets
  4. Consistent phase (within π/2)

**Code**: `forensic_fingerprint/run_real_data_cmb_comb.py::generate_combined_verdict()`

**Validation**: If signal is Planck-specific systematic, WMAP will show null → FAIL verdict.

### Residual Risk

- **Common-mode systematics**: If both Planck and WMAP have the same systematic error (e.g., both mismodel foregrounds the same way), replication doesn't help.
  - **Mitigation**: Planck and WMAP use different instruments, scan strategies, and foreground removal methods, so common-mode systematics are unlikely for high-frequency periodic structure.

- **WMAP sensitivity**: WMAP has lower sensitivity than Planck. A weak real signal might pass in Planck but fail in WMAP due to noise alone.

### Status

✓ **ADDRESSED** — Two-dataset protocol implemented. WMAP threshold relaxed appropriately.

---

## 5. False Positive Rate Calibration (ΛCDM Null Control)

### Skeptical Argument

> **"Even with all your controls, your pipeline might have a bug that produces false positives. You need to test on synthetic ΛCDM data (no signal) and measure the actual false positive rate."**

### How We Addressed It

**Implementation**: Synthetic ΛCDM control tests

- **Synthetic data generation**:
  - Generate C_ℓ from best-fit ΛCDM model (using CAMB/CLASS)
  - Add Gaussian noise with realistic covariance
  - Run full CMB comb pipeline
  
- **Expected behavior**: p-values should be uniformly distributed U(0,1) under null

- **Test**: Run 100+ synthetic realizations, plot p-value distribution
  - **PASS**: p-values follow uniform distribution (KS test p > 0.05)
  - **FAIL**: p-values show excess at low values → pipeline bug

**Code**: 
- `forensic_fingerprint/synthetic/lcdm.py::generate_synthetic_lcdm_spectrum()`
- `forensic_fingerprint/run_synthetic_lcdm_control.py`

**Validation**: See `forensic_fingerprint/stress_tests/test_4_lcdm_null.py` for automated test.

### Residual Risk

- **Synthetic vs real differences**: Synthetic data might not capture all properties of real data (e.g., non-Gaussianity, foreground residuals).
  - **Mitigation**: Use published Planck covariance (includes non-Gaussian effects) for synthetic noise.

### Status

✓ **ADDRESSED** — Synthetic ΛCDM control implemented and tested.

---

## 6. ℓ-Range Dependence (Cherry-Picking Windows)

### Skeptical Argument

> **"You chose ℓ = 30-1500 for Planck. Maybe the signal only appears in a specific ℓ-window and disappears in others. This could indicate a systematic rather than a real signal."**

### How We Addressed It

**Implementation**: Ablation tests (ℓ-range robustness)

- **Predefined ℓ-windows**:
  - Full range: 30-1500 (Planck), 30-800 (WMAP)
  - Low-ℓ only: 30-500
  - Mid-ℓ only: 200-1000
  - High-ℓ only: 800-1500 (Planck only)
  - Sliding windows: 30-800, 100-900, 200-1000, etc.

- **Robustness check**: Signal should persist across multiple independent ℓ-windows
  - If signal appears only in one window → likely systematic
  - If signal appears in all windows → robust

**Code**: `forensic_fingerprint/ablation.py`

**Validation**: Real periodic signal should be detectable in multiple ℓ-ranges. Systematics typically affect specific ℓ-ranges.

### Residual Risk

- **Scale-dependent signals**: If the signal is genuinely scale-dependent (e.g., Variant D hierarchical synchronization), ablation could be misleading.
  - **Mitigation**: Document ℓ-dependence and compare to theoretical predictions.

### Status

✓ **ADDRESSED** — Ablation framework implemented. Results aggregated in markdown reports.

---

## 7. Polarization Cross-Check (TT vs TE/EE)

### Skeptical Argument

> **"You only tested TT (temperature-temperature). If the signal doesn't appear in TE (temperature-E-mode) or EE (E-mode-E-mode) polarization, it could be foreground contamination or instrumental systematic rather than a real CMB effect."**

### How We Addressed It

**Implementation**: TE/EE pipeline extension

- **Loaders extended**: Planck and WMAP loaders now support TE and EE spectra
- **CLI option**: `--spectrum TT|TE|EE` (default: TT)
- **Expectation**:
  - Variant C predicts periodic structure in all spectra (TT, TE, EE) because it's a geometric effect in spacetime, not specific to temperature fluctuations.
  - If signal appears in TT but not TE/EE → likely foreground or systematic

**Code**:
- `forensic_fingerprint/loaders/planck.py::load_planck_data()` (TE/EE support)
- `forensic_fingerprint/loaders/wmap.py::load_wmap_data()` (TE/EE support)

**Validation**: Run comb test on TT, TE, and EE separately. Consistent signal across all three → strong evidence for real effect.

### Residual Risk

- **TE/EE sensitivity**: Polarization spectra have lower signal-to-noise than TT. A real but weak signal might not reach significance in TE/EE.
  - **Mitigation**: Use combined TT+TE+EE analysis for maximum sensitivity (future work).

- **Data availability**: Some datasets may not have published TE/EE covariance matrices.

### Status

⚠ **PARTIAL** — Loaders extended for TE/EE (CLI `--spectrum` flag added). Full validation pending.

---

## 8. Phase Coherence (Planck vs WMAP)

### Skeptical Argument

> **"Even if both Planck and WMAP show the same period, if the phases are inconsistent, it could be two independent noise fluctuations at the same frequency, not a real signal."**

### How We Addressed It

**Implementation**: Phase consistency check

- **PASS criterion**: |φ_Planck - φ_WMAP| < π/2 (allowing for phase wrapping)
  - Phases should be consistent if signal is real and datasets overlap in ℓ-range
  
- **Documented in verdict**: Combined verdict report includes phase comparison

**Code**: `forensic_fingerprint/run_real_data_cmb_comb.py::generate_combined_verdict()`

**Validation**: Synthetic signal tests show phase recovery is robust when S/N > 3.

### Residual Risk

- **ℓ-range differences**: Planck (30-1500) and WMAP (30-800) have different ranges. Phase could legitimately differ if signal is scale-dependent.
  - **Mitigation**: Report phase for overlapping ℓ-range (30-800) separately.

- **Phase degeneracy**: Phase is periodic (mod 2π), so we allow wrapping in comparison.

### Status

✓ **ADDRESSED** — Phase check implemented in PASS/FAIL criteria.

---

## 9. Whitening Mode Consistency (Diagonal vs Full Covariance)

### Skeptical Argument

> **"You tested with diagonal whitening (ignoring correlations). If you use full covariance whitening, the signal might disappear, suggesting it was an artifact of not accounting for error correlations."**

### How We Addressed It

**Implementation**: Multiple whitening modes

- **Modes available**:
  - `none`: No whitening (raw residuals) — for debugging only
  - `diag`: Diagonal whitening (r / σ) — candidate-grade
  - `full`: Full covariance Cholesky whitening — court-grade
  
- **Comparison**: Run analysis with both `diag` and `full` modes
  - If signal persists in both → robust
  - If signal disappears in `full` → likely correlation artifact

- **Regularization**: Full covariance mode includes automatic ridge regularization for numerical stability (documented in metadata)

**Code**:
- `forensic_fingerprint/run_real_data_cmb_comb.py` (CLI flags: `--whiten diag|full`)
- `forensic_fingerprint/whitening.py::build_whitener()`

**Validation**: Whitening calibration test verifies that full mode produces unit variance and zero correlations.

### Residual Risk

- **Regularization dependence**: Ridge jitter (default 1e-12) can affect results if covariance is ill-conditioned. We document jitter parameter for reproducibility.

### Status

✓ **ADDRESSED** — Multiple whitening modes implemented. Calibration test validates full covariance mode.

---

## 10. Prior Specification Bias

### Skeptical Argument

> **"You pre-registered candidate periods including 255. If 255 was chosen after looking at the data, this invalidates the p-value."**

### How We Addressed It

**Documentation**: Pre-registration timeline

- **Theory development**: Reed-Solomon (255, 223) code structure documented in UBT papers (2023-2024) BEFORE any CMB analysis
  - Period 255 = 2^8 - 1 (Galois field GF(256) generator)
  - Predicted from first principles, not from data
  
- **Protocol registration**: `forensic_fingerprint/PROTOCOL.md` committed to git with timestamp BEFORE real data analysis
  - Git commit history shows periods [8, 16, 32, 64, 128, 255] were locked before results

- **Audit trail**: All analysis code and data provenance tracked with SHA-256 hashes

**Mitigation**: Even if a skeptic doesn't believe the pre-registration, the max-statistic method provides valid p-values as long as the candidate set is fixed before computing p-values.

### Status

✓ **ADDRESSED** — Pre-registration documented. Git history provides audit trail.

---

## 11. Confirmation Bias in Interpretation

### Skeptical Argument

> **"You might interpret ambiguous results favorably because you want the theory to work. Even automated tests can be unconsciously biased by choice of parameters."**

### How We Addressed It

**Implementation**: Blinded analysis and pre-registered criteria

- **Automated PASS/FAIL**: Decision logic is coded in `generate_combined_verdict()` based on pre-registered thresholds
  - No manual judgment required
  
- **Skeptic checklist**: This document itself is a guard against confirmation bias
  - We document counter-arguments even if they don't currently apply
  
- **Open data and code**: Full pipeline is public, allowing independent replication

**Culture**: We actively encourage skepticism and independent verification.

### Status

✓ **ADDRESSED** — Automated decision logic. Open science practices.

---

## Summary Table

| # | Counter-Argument | Status | Key Mitigation |
|---|-----------------|--------|----------------|
| 1 | Look-elsewhere effect | ✓ ADDRESSED | Max-statistic MC |
| 2 | Units mismatch | ✓ ADDRESSED | χ²/dof check |
| 3 | Covariance errors | ✓ ADDRESSED | Validation + calibration |
| 4 | Needs replication | ✓ ADDRESSED | Planck + WMAP protocol |
| 5 | False positive rate | ✓ ADDRESSED | ΛCDM null control |
| 6 | ℓ-range cherry-picking | ✓ ADDRESSED | Ablation tests |
| 7 | TT-only (no TE/EE) | ⚠ PARTIAL | Loaders ready, validation pending |
| 8 | Phase incoherence | ✓ ADDRESSED | Phase consistency check |
| 9 | Whitening mode dependence | ✓ ADDRESSED | Diagonal vs full comparison |
| 10 | Prior specification bias | ✓ ADDRESSED | Pre-registration + git audit |
| 11 | Confirmation bias | ✓ ADDRESSED | Automated decisions + open science |

---

## How to Use This Checklist

### For Developers

When implementing new analysis features:
1. **Before coding**: Review this checklist. Does your feature address or introduce any of these issues?
2. **During development**: Add tests that explicitly check for the counter-arguments (e.g., synthetic null tests for false positive rate)
3. **After coding**: Update this checklist with implementation details

### For Reviewers

When reviewing results:
1. **Check status column**: Are all critical issues ADDRESSED?
2. **Review residual risks**: Are they acceptable for the claim being made?
3. **Inspect implementation**: Do the code and tests actually do what this document claims?

### For Skeptics

This checklist is for YOU. We want your strongest counter-arguments because they make the science stronger.

If you have a counter-argument not listed here:
1. Open a GitHub issue describing it
2. We'll add it to this checklist and update the status as we address it

---

## Versioning

This document follows semantic versioning:
- **Major version**: Change to PASS/FAIL criteria or pre-registered protocol
- **Minor version**: New counter-argument added or status update
- **Patch version**: Clarifications or typo fixes

**Current version**: 1.0.0 (2026-01-11)

---

## References

- Protocol: `forensic_fingerprint/PROTOCOL.md`
- Verdict criteria: `forensic_fingerprint/FORENSIC_VERDICT_CRITERIA.md`
- Implementation details: See `forensic_fingerprint/IMPLEMENTATION_SUMMARY_COURT_GRADE.md`
- Stress tests: `forensic_fingerprint/stress_tests/`
- Theory background: `unified_biquaternion_theory/ubt_main_article.tex`

---

**End of Skeptical Counter-Argument Checklist**
