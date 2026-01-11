# CMB Forensic Fingerprint - Court-Grade Audit Report

**Date**: 2026-01-11 15:21:13 UTC
**Protocol Version**: v2.0 (Court-Grade)
**Variant**: C
**Random Seed**: 42

## Overview

This report consolidates results from multiple audit modes:

1. **Baseline**: Standard TT analysis with diagonal/covariance uncertainties
2. **Polarization**: Independent tests on EE/TE channels (if available)
3. **Ablation**: Tests across multiple ℓ-ranges to detect localized artifacts
4. **Synthetic Null**: ΛCDM false positive rate validation

---

## Baseline Results

### Planck TT

- **ℓ range**: 30 to 100
- **Whitening**: diagonal
- **Best period**: Δℓ = 16
- **Amplitude**: A = 0.082934
- **Phase**: φ = 0.005116 rad
- **P-value**: 1.000000e+00
- **Significance**: **NULL**

---

## Ablation Results

### Planck TT

**Summary**: 2/5 valid ranges

**Period counts across ranges**:

- Δℓ = 16: 2 range(s)

**Phase consistency**: Max diff = 0.000 rad ✓ (within π/2)

**Per-range results**:

| Range | ℓ min | ℓ max | Best Period | P-value | Status |
|-------|-------|-------|-------------|---------|--------|
| low | 30 | 250 | 16 | 1.0000e+00 | OK |
| mid | 251 | 800 | - | - | SKIPPED |
| high | 801 | 1500 | - | - | SKIPPED |
| full_low | 30 | 800 | 16 | 1.0000e+00 | OK |
| full_high | 200 | 1500 | - | - | SKIPPED |

---

## Interpretation Guidelines

### Signal Robustness Indicators

A **robust** candidate signal should exhibit:

1. **Baseline**: p < 0.01 in primary TT channel
2. **Whitening**: Signal persists with full covariance whitening
3. **Polarization**: Appears in EE/TE with consistent phase
4. **Ablation**: Appears in ≥2 independent ℓ-ranges
5. **Synthetic Null**: Δℓ=255 appears in <1% of ΛCDM realizations

### Potential Artifacts

Signal **disappears** after whitening → likely covariance artifact
Signal **absent** in polarization → likely TT-specific systematic
Signal **restricted** to one ℓ-range → likely localized artifact
Signal **frequent** in ΛCDM null → likely generic statistical fluctuation

---

**End of Audit Report**
