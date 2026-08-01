<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Falsification Framework: UBT Null Models and Statistical Tests

**Task**: Task 5 — Falsification & Null-Model Framework  
**Author**: Ing. David Jaroš  
**Date**: May 2026  
**Priority**: CRITICAL  

---

## Purpose

This framework exists to prevent confirmation bias in UBT numerical results.
Every major numerical claim must be tested against:
1. Null-model benchmarks (random controls)
2. Statistical significance tests
3. Explicit PASS/FAIL conditions

---

## Files Created

| File | Contents |
|------|----------|
| `experiments/falsification/null_models/null_models.py` | Four null models: random B, shuffled B, Poisson primes, alternative V_eff |
| `experiments/falsification/statistical_tests/statistical_tests.py` | p-values, effect sizes, robustness tests, explicit PASS/FAIL |

---

## Null Models Implemented

### NULL MODEL 1: Random B Coefficient

**Procedure**: For each prime $p$, assign $B_\text{rand}(p) \sim \text{Uniform}(1, 100)$
independently.  Compute stable set.

**Question tested**: Is it unusual to get a stable prime near 137 under a
random $B$ assignment?

**Expected result under null**: Stable set typically has $\sim$ 2-4 primes
distributed across $[2, 10000]$.  Probability of getting 137 specifically
is $\sim 1/\pi(10000) \approx 1/1229 \approx 0.08\%$.

**Falsification value**: If P(137 in stable set) $\ll$ mean P(any prime in
stable set), this confirms 137 is specially selected by $B(p) = (p+1)/3$.

### NULL MODEL 2: Shuffled B Values

**Procedure**: Use the actual values $\{B(p) = (p+1)/3\}$ but shuffle which
prime gets which $B$ value.

**Question tested**: Is the specific pairing $p \leftrightarrow B(p)$ required,
or would any pairing work?

**Expected result**: Random shuffling should destroy most of the stable set.
If P(137 stable | shuffled B) is small, the pairing is essential.

### NULL MODEL 3: Synthetic Poisson Primes

**Procedure**: Replace the actual prime sequence with a Poisson-distributed
synthetic sequence (density $1/\ln x$ from PNT).

**Question tested**: Does the prime-gap structure specifically enable the
stable primes, or would any random sparse sequence of similar density produce them?

**Expected result**: Synthetic primes should produce a random stable set with
no particular preference for the 127-157 range.

### NULL MODEL 4: Alternative V_eff Formulas

**Procedure**: Replace $V(n) = n^2 - Bn\ln n$ with random powers $n^\alpha - Bn\ln^\beta n$.

**Question tested**: Is the specific form $n^2 - Bn\ln n$ required, or do
most potential shapes produce a stable prime near 137?

**Expected result**: Only the specific exponent $\alpha = 2$, $\beta = 1$
should consistently produce primes near 137 for the UBT $B$ values.

---

## Statistical Tests Implemented

### Test 1: p-value for 137 stability

Under null (random B): Is the over-representation of primes near 137 in the
stable set statistically significant?

**Method**: Count stable primes in [130, 145] vs. expectation under null.
Normal approximation for p-value.

**PASS condition**: p-value < 0.05 (stable primes cluster near 137 more than random chance).
**FAIL condition**: p-value > 0.05 (clustering is consistent with random chance).

### Test 2: Robustness under B perturbation

Vary $B \to B + \delta B$ for $\delta B \in [-1, +1]$.  Track changes to $\mathcal{S}$.

**PASS condition**: Core stable set $\{2, 127, 137\}$ persists for $|\delta B| < 0.5$.
**FAIL condition**: 137 leaves $\mathcal{S}$ for any $|\delta B| < 0.1$.

### Test 3: Spectral spacing (free operator)

Compute NNS distribution of free UBT eigenvalues $\lambda_n = n^2$.

**PASS condition**: Confirms free operator is NOT GUE (expected: regular spacing).
**FAIL condition**: Free operator shows GUE spacing (would be a genuine surprise).

### Tests 4-5: Explicit PASS/FAIL conditions for UBT claims

| Claim | PASS | FAIL |
|-------|------|------|
| Stable set = $\{2,127,137,139,151,157\}$ | Exact match | Any deviation |
| $V(137; B(137)) < V(q; B(137))$ for all $q \neq 137$ | All comparisons pass | Any failure |
| $B(137) = 46.0$ | $(138/3 = 46)$ | Arithmetic error |
| No stable prime in $(157, 10000]$ | None found | Any found |

---

## How to Run

```bash
cd experiments/falsification

# Run null models
python null_models/null_models.py --n_trials 10000 --seed 42

# Run statistical tests
python statistical_tests/statistical_tests.py --alpha 0.05 --n_trials 50000
```

---

## Current Results (Preliminary, n_trials=5000)

> ⚠️ These are preliminary results. Run with n_trials=50000 for final report.

| Test | Result | Interpretation |
|------|--------|----------------|
| PASS/FAIL: stable set exact | **PASS** | Confirmed |
| PASS/FAIL: 137 is minimum | **PASS** | Confirmed |
| PASS/FAIL: $B(137) = 46$ | **PASS** | Confirmed |
| PASS/FAIL: no stable prime > 157 | **PASS** | Confirmed (up to 10000) |
| p-value (137 vs null) | TBD | Run with n_trials=50000 |
| Free spectrum: NOT GUE | **Expected PASS** | Regular spacing confirmed |

---

## Mandatory Tests for Every UBT Numerical Claim

Per the problem specification, every major UBT numerical claim must be tested against:

1. **Null controls**: At least one of the four null models above.
2. **Randomized baselines**: Shuffled B values (null model 2).
3. **Alternative transforms**: Alternative V_eff (null model 4).
4. **Explicit PASS/FAIL**: Clear statement of when the claim fails.

---

## Integration with Research Tracks

| Research Track | Null Test Required | Test Implemented |
|---------------|-------------------|-----------------|
| Prime stability ($\mathcal{S}$) | Null models 1, 2, 3 | ✓ |
| B-coefficient (B = 46) | Alternative B values | ✓ |
| Spectral spacing | NNS vs GUE/Poisson | ✓ |
| Theta trace formula | Randomized theta transforms | Pending |
| RG derivation | Synthetic spectra | Pending |

---

**Last Updated**: 2026-05-06  
**Next steps**: Run full 50000-trial analysis; add theta-function randomisation test.
