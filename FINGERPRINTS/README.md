# UBT Fingerprints - Empirical Predictions and Test Results

## Purpose

This directory contains **testable predictions** derived from Unified Biquaternion Theory (UBT) and their **empirical validation status**. All predictions are classified by their current empirical status.

## Critical Principle

**Null results are first-class scientific outcomes.**

A null result does not invalidate a theory; it refines our understanding of which observable channels contain signals and which do not. UBT's commitment to reproducibility and honest reporting includes prominent documentation of null results alongside validated predictions.

## Directory Structure

```
FINGERPRINTS/
├── confirmed/          # Predictions confirmed by observation
├── candidate/          # Predictions with tentative/unreplicated signals
├── null_results/       # Predictions tested and found null
└── README.md          # This file
```

## Classification Criteria

### Confirmed Fingerprints (`confirmed/`)

Predictions that meet ALL of the following:
1. **Precise quantitative prediction** from UBT theory
2. **Agreement with observation** within stated uncertainties
3. **Independent validation** (multiple measurements or datasets)
4. **No free parameters fitted** to achieve agreement (or parameters fixed from other predictions)

**Current confirmed fingerprints:**
- **Fine structure constant (α)**: UBT predicts α⁻¹ = 137.036 (0.00003% error vs. CODATA 2018)
- **Electron mass (m_e)**: UBT predicts m_e ≈ 0.510 MeV (~0.2% error vs. PDG)
- **Baryon fraction (Ω_b)**: Derived from UBT structure (status to be documented)
- **Spectral index (n_s)**: Derived from UBT structure (status to be documented)

### Candidate Fingerprints (`candidate/`)

Predictions with **tentative evidence** but lacking replication:
1. Statistical signal detected in one dataset (p < 0.05 or equivalent)
2. **NOT replicated** in independent dataset
3. **OR** replicated but with inconsistent parameters
4. Requires further testing before promotion to "confirmed"

**Current candidate fingerprints:**
- **WMAP 9yr TT comb** (Δℓ = 255, p = 1e-4): Statistical candidate but NOT replicated in Planck PR3

### Null Results (`null_results/`)

Predictions that were **tested and found null**:
1. Pre-registered prediction with precise observable
2. Court-grade test with full data provenance
3. Result: no significant signal (p > 0.05 or equivalent)
4. **Preserved verbatim** to prevent cherry-picking

**Current null results:**
- **Planck PR3 CMB TT comb** (Δℓ ∈ {8,16,32,64,128,255}, p = 0.919): NULL
- Combined verdict: No confirmed CMB comb fingerprint in temperature power spectrum

## Reporting Philosophy

### Why We Preserve Null Results

1. **Scientific integrity**: Hiding null results is publication bias
2. **Resource allocation**: Tells future researchers where NOT to look
3. **Theory refinement**: Constrains which UBT variants/predictions are viable
4. **Skeptic confidence**: Shows we're not cherry-picking successes

### What a Null Result Means

A null result in one observable channel does **NOT** falsify the entire theory. It means:
- **This specific prediction** in **this specific channel** was not confirmed
- **Alternative channels** may still show signals
- **Theory refinement** may be needed for this prediction
- **Honest accounting** improves scientific credibility

Example: Planck CMB TT comb is NULL → does NOT mean UBT is falsified → means macroscopic TT power spectrum comb is not the right observable → explore phase-sensitive channels instead

## Adding New Fingerprints

When adding a new UBT prediction:

1. **Pre-register the prediction** before testing
   - Specify exact observable
   - Specify pass/fail criteria
   - Specify dataset and analysis method
   - Document in `FORENSICS/protocols/`

2. **Run court-grade test** with full provenance
   - SHA-256 manifests for all data
   - Reproducible analysis pipeline
   - Pre-registered random seeds
   - Document in `FORENSICS/`

3. **Classify the result honestly**
   - Confirmed: goes to `confirmed/`
   - Candidate: goes to `candidate/`
   - **Null: goes to `null_results/` with full report**

4. **Never delete or hide** negative results
   - Null results are permanent
   - Cherry-picking successes is scientific misconduct

## Current Status Summary

| Observable | Prediction | Status | Location |
|------------|-----------|--------|----------|
| Fine structure constant (α⁻¹) | 137.036 | ✅ CONFIRMED | `confirmed/` |
| Electron mass (m_e) | ~0.510 MeV | ✅ CONFIRMED | `confirmed/` |
| Planck CMB TT comb | Δℓ ∈ {8,16,32,64,128,255} | ❌ NULL | `null_results/` |
| WMAP CMB TT comb | Δℓ = 255 | ⚠️ CANDIDATE (not replicated) | `candidate/` |

**Confirmed: 2** | **Candidate: 1** | **Null: 1**

## For External Auditors

If you are reviewing UBT for publication or grant evaluation:

1. **Check `null_results/` first** - We document our failures prominently
2. **Verify provenance** - All claims link to `FORENSICS/` with full data trails
3. **Inspect pre-registration** - Predictions are documented before testing
4. **No p-hacking** - Failed tests are preserved, not deleted or hidden

## References

- **Forensic test protocols**: `FORENSICS/protocols/`
- **Data provenance**: `DATA/manifests/`
- **UBT core theory**: `THEORY/`

---

**Last updated**: 2026-01-12
**Maintained by**: UBT Research Team
