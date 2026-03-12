# Candidate Fingerprint: WMAP 9yr CMB TT Comb

## Status: CANDIDATE (Not Replicated)

⚠️ **This is a statistical candidate that has NOT been replicated in independent data.**

## Prediction

UBT Variant C (Explicit Frame Synchronization) predicts periodic comb structure in CMB temperature power spectrum residuals.

## WMAP 9yr TT Test Result

| Parameter | Value |
|-----------|-------|
| **Dataset** | WMAP 9yr TT |
| **Multipole Range** | ℓ = 30 to 800 (771 multipoles) |
| **Best-Fit Period** | Δℓ = 255 |
| **Amplitude** | A = 0.3448 |
| **P-value** | **1.00e-04** |
| **Significance** | **CANDIDATE** |

**Interpretation**: Statistical candidate signal at Δℓ = 255 with p = 1e-4 (exactly at MC floor for 10k samples).

## Critical Problem: NOT Replicated in Planck

### Planck PR3 TT Test Result

| Parameter | Value |
|-----------|-------|
| **Dataset** | Planck PR3 TT |
| **Multipole Range** | ℓ = 30 to 1500 (1471 multipoles) |
| **Best-Fit Period** | Δℓ = 16 (NOT 255) |
| **Amplitude** | A = 0.0539 |
| **P-value** | **9.19e-01** |
| **Significance** | **NULL** |

**Interpretation**: No evidence for periodic comb structure in Planck. Best-fit period is completely different and not statistically significant.

## Combined Verdict

**FAIL** - Criteria not satisfied:
1. Planck p-value < 0.01 → ❌ FAIL (p = 0.919)
2. WMAP p-value < 0.05 → ✅ PASS (p = 1e-4)
3. Same period in Planck and WMAP → ❌ FAIL (Planck: Δℓ = 16, WMAP: Δℓ = 255)
4. Consistent phase (within π/2) → ❌ FAIL (different periods → N/A)

**Conclusion**: WMAP candidate is NOT replicated in Planck PR3.

## Possible Explanations

1. **WMAP statistical fluctuation**: At p = 1e-4, ~0.01% chance of false positive. With 6 candidate periods tested, effective rate is ~0.06%.

2. **Different systematics**: WMAP and Planck have different beam characteristics, foreground subtraction, calibration procedures, and sensitivity levels.

3. **ℓ-range differences**: WMAP tested ℓ = 30-800, Planck ℓ = 30-1500. Planck has better S/N at low-ℓ.

4. **Coincidental period**: Δℓ = 255 is a large period. Random fluctuations could align by chance.

**Most likely**: WMAP candidate is a statistical fluctuation or systematic artifact. Planck's null result (with higher sensitivity) is definitive.

## Classification Rationale

This remains in `candidate/` rather than `null_results/` because:
- WMAP shows p = 1e-4 signal (statistically significant in isolation)
- However, **NON-REPLICATION is a critical failure**
- Kept as candidate to document the attempted replication
- Prevents future re-discovery of same statistical fluctuation

**For scientific purposes: This prediction is effectively NULL due to non-replication.**

## Implications

- ❌ **Do NOT pursue** large-scale CMB TT comb searches
- ✅ **DO pursue** phase-sensitive observables, polarization, near-field tests
- ✅ **Theory refinement** needed for Variant C's CMB prediction

## References

- Full report: `FINGERPRINTS/null_results/combined_verdict.md`
- Forensic protocol: `FORENSICS/protocols/`
- Pre-registration: `FORENSICS/protocols/FORENSIC_VERDICT_CRITERIA.md`

## Provenance

- Test date: 2026-01-12
- Protocol: Court-grade with SHA-256 manifests
- Replication status: **NOT replicated** (Planck NULL)
- Classification: CANDIDATE (effectively NULL due to non-replication)

---

**Recommendation**: Treat as NULL for publication purposes. Non-replication is a critical failure in the scientific method.
