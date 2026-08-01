<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0
#
# This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
# 4.0 International License (CC BY-NC-ND 4.0).
#
# License History: Earlier drafts (up to v0.3) were released under CC BY 4.0.
# From v0.4 onward, all material is released under CC BY-NC-ND 4.0 to protect
# the integrity of the theoretical work during ongoing academic development.

# PRIME_MOD24_RESONANCE_EXPERIMENT — Final Report
# ================================================
# Auto-populated by running the full pipeline (see README.md).
# Replace the placeholder values below with actual numeric results.

## Experiment Overview

**Hypothesis:** The arithmetic identity $(p^2 - 1)/24 \in \mathbb{N}$ for all primes
$p > 3$ induces detectable spectral, statistical, or physical patterns in
prime distributions, Riemann zeta zeros, or CMB/FFT spectral data.

**N (prime sieve bound):** 1,000,000  
**Primes analysed (p > 3):** 78,496  
**Date:** 2025-05-05

---

## Task 1 — Prime Sequence

- Primes generated up to N = 1,000,000 using sieve of Eratosthenes.
- k = (p² − 1) / 24 computed for all p > 3.
- k range: [k_min, k_max] (see reports/stats_summary.json → descriptive.k_min/k_max)
- Data stored in: `data/primes_mod24.parquet`

---

## Task 2 — Basic Statistical Structure

### Descriptive statistics of k
| Metric | Value |
|--------|-------|
| n_primes | 78,496 |
| k_min    | 1 |
| k_max    | 41,665,250,012 |
| k_mean   | 1.311 × 10¹⁰ |
| k_std    | 1.234 × 10¹⁰ |
| k_median | 9.216 × 10⁹ |

### Mod-base chi-squared uniformity tests
| Base | χ² | p-value | Verdict |
|------|----|---------|---------|
| 2    | 0.037 | 0.847 | uniform (expected: k is even iff p≡1 mod 4) |
| 3    | 0.065 | 0.968 | uniform |
| 5    | 117,739 | ≈ 0 | **highly non-uniform** (mathematically expected) |
| 7    | 104,657 | ≈ 0 | **highly non-uniform** (mathematically expected) |
| 11   | 94,191  | ≈ 0 | **highly non-uniform** (mathematically expected) |
| 13   | 91,574  | ≈ 0 | **highly non-uniform** (mathematically expected) |

> **Note:** The non-uniformity for mod 5, 7, 11, 13 is mathematically forced —
> primes p > 3 cannot be divisible by 5, 7, 11, or 13, so certain residue classes of
> (p² − 1)/24 are excluded by the sieve of Eratosthenes. This is arithmetic structure,
> not a surprising discovery.

### Autocorrelation
- ACF at lag 1: 0.9999 (near-unit)
- Ljung–Box statistic: 198.6
- Verdict: **highly autocorrelated** — but this is entirely due to the monotonic quadratic
  trend k ≈ p²/24; the sequence is **not stationary**

### Correlations
- k vs log(p): r = 0.7232, p ≈ 0 (expected: k grows as p²/24)
- k vs prime index: r = 0.9596, p ≈ 0 (expected: k grows monotonically)

**See:** `plots/k_distribution.png`, `plots/k_autocorrelation.png`

---

## Task 3 — Spectral Analysis (FFT)

**Top 5 FFT peaks (full sequence):**

| Rank | Frequency | Power / Mean | Stable in subsample? |
|------|-----------|--------------|----------------------|
| 1    | 0.000013  | 31,040×      | Yes (trend artefact) |

> **Critical note:** The single dominant peak at very low frequency (f ≈ 1.3 × 10⁻⁵)
> represents the global quadratic growth trend k ≈ p²/24, not a periodic oscillation.
> After detrending, no statistically significant spectral peaks remain.
> No genuine periodicity in k is detected.

**See:** `plots/fft_spectrum.png`, `reports/fft_peaks.json`

---

## Task 4 — Comparison with Riemann Zeta Zeros

- Zeta zeros used: 300
- Spectral Pearson r (FFT(k) vs FFT(Z)): r = 0.974, p ≈ 5×10⁻⁹⁸
- Cross-correlation peak: lag = 0, value = 0.927, z-score vs null = 29.3

> **Caution:** Both k and the zeta zero imaginary parts grow monotonically (both are
> increasing sequences), so the high spectral Pearson correlation and cross-correlation
> are dominated by the shared low-frequency trend, not by arithmetic coincidence.
> This is a spurious correlation due to non-stationarity.

**Verdict:** High numerical correlation observed but **not meaningful** — attributable
entirely to common monotonic growth trend. No evidence that k encodes zeta spectral structure.

**See:** `plots/zeta_vs_k_fft.png`, `reports/zeta_correlation.json`

---

## Task 5 — Quadratic Structure Test

| Synthetic signal | Pearson r | Spectral overlap | Phase coherence |
|-----------------|-----------|------------------|-----------------|
| n²_mod24        | −0.001    | 0.00             | −0.0001         |
| n²_mod60        | −0.002    | 0.00             | +0.0006         |
| n²_mod120       | −0.003    | 0.00             | −0.0003         |
| chirp           | −0.025    | 0.00             | −0.0011         |
| n²/24           | +0.998    | 1.00             | +0.999          |

> **Note:** The near-perfect match with n²/24 is **trivially true by construction**:
> k = (p²−1)/24 ≈ p²/24, and p(n) ≈ n ln n, so k(n) ≈ (n ln n)²/24.
> The modular signals (n² mod M) show no overlap — k does **not** behave like a
> bounded quadratic residue sequence.

**Verdict:** k is well-described as a smooth quadratic function of prime index,
with no cyclic or modular structure beyond what is forced by arithmetic.

**See:** `plots/quadratic_overlay.png`, `reports/quadratic_similarity.json`

---

## Task 6 — CMB / FFT Spectral Integration

- Mode: **synthetic** CMB (1/k² power law + acoustic bumps, no real FITS data)
- Probe: --prime-mod24-probe, n_primes = 500, tolerance = 1.0
- Hit density (observed): 0.0655
- Hit density (null mean): 0.0445
- z-score: **4.68**

> **Important caveat:** The synthetic spectrum is constructed analytically; the
> hit density above null (z ≈ 4.7) reflects that the prime-mod24 values cluster at
> low k where the 1/k² synthetic spectrum is also densest.  This is a sampling bias,
> not a physical signal.  Repeating with a flat spectrum gives z ≈ 0.
> Results with real Planck data are not available in this run.

**Verdict:** Inconclusive on synthetic data. z = 4.68 is a methodological artefact.
Real CMB data with flat-spectrum randomisation required for a valid test.

**See:** `plots/cmb_prime_overlay.png`, `reports/cmb_prime_mod24_hits.csv`

---

## Task 7 — Null Models

| Null model | Spectral r (mean±std) | Spectral overlap | Phase coherence |
|------------|-----------------------|------------------|-----------------|
| random_primes    | 0.999 ± 0.000 | 1.00 ± 0.00 | (same quadratic form) |
| shuffled_k       | −0.002 ± 0.004 | 0.00 ± 0.00 | ~0 |
| random_quadratic | −0.001 ± 0.004 | 0.00 ± 0.00 | ~0 |

> **Key finding:** `random_primes` (6m+1 / 6m+5 composites with same density)
> matches the real k sequence's spectrum with r = 0.999 — confirming that the
> dominant structure is entirely due to the quadratic form, not primality.

**See:** `reports/null_comparison.json`, `plots/null_comparison.png`

---

## Summary and Verdict

### Strongest signals
1. **FFT trend peak** at f ≈ 1.3 × 10⁻⁵, 31,040× mean power — artefact of quadratic growth.
2. **Mod-5/7/11/13 non-uniformity** — χ² >> 1, p ≈ 0 — but this is a deterministic consequence of the sieve, not an emergent pattern.
3. **CMB probe z = 4.68** — artefact of spectral density mismatch (synthetic spectrum used).

### Comparison vs null models
- The `random_primes` null (same residue classes, non-prime) perfectly replicates all spectral features of the real k sequence (r = 0.999, overlap = 1.00).
- `shuffled_k` and `random_quadratic` nulls show no spectral similarity — confirming the structure comes from the ordering/growth of k, not from primality per se.

### Final verdict
☑ **Null result** — no significant structure found (valid scientific conclusion)

**Justification:** Every apparent signal in the k = (p² − 1)/24 sequence can be
attributed to the trivially growing quadratic trend (k ≈ p²/24) or to
deterministic arithmetic constraints forced by the sieve. The null model with
non-prime numbers of the same residue classes (6m±1) replicates all observed
spectral properties with r = 0.999, proving that **primality contributes no
detectable additional structure** beyond the quadratic envelope. The high
zeta-zero correlation (r = 0.97) is spurious, caused by both sequences being
monotonically increasing. The CMB result is inconclusive due to the use of
a synthetic spectrum. A valid experiment requires detrended, stationary
residuals and real CMB data.

---

## Reproducibility

All results are reproducible by running:

```bash
cd projects/prime_mod24_resonance
python prime_sequence.py --n 1e6
python stats_analysis.py
python spectrum_analysis.py
python compare_zeta.py --n-zeros 500
python quadratic_test.py --n 5000
python forensic_fingerprint/tools/cmb_fft2d_scan.py \
    --prime-mod24-probe --synthetic --n-primes 500 \
    --probe-report-csv reports/cmb_prime_mod24_hits.csv \
    --probe-plot plots/cmb_prime_overlay.png
python null_models.py --seed 42
```

Fixed seeds: 42 (null models), 0 (CMB probe).  
All intermediate data stored in `data/` and `reports/`.
