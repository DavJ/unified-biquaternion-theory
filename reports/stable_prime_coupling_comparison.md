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


# Stable-Prime to Coupling Comparison (Non-Fit)

**Task**: `map_stable_prime_sectors_to_coupling_constants` — Target 2  
**Author**: Ing. David Jaroš  
**Date**: 2026-05-10  
**Mode**: hypothesis_test_no_numerology  
**Hard rule**: No reinterpretation of constants to force matches.  Distances are computed
mechanically from the coupling inventory (`reports/coupling_inventory.md`).

---

## 1. Stable Prime Set

$$\mathcal{S} = \{2,\; 127,\; 137,\; 139,\; 151,\; 157\}$$

These are the six primes satisfying the UBT prime-stability condition
$V(q; B(p)) > V(p; B(p))$ for all primes $q \neq p$, where $B(p) = (p+1)/3$.

## 2. Coupling Reference Values

Taken directly from `reports/coupling_inventory.md`.  All values are
experimentally established.  No prime has been used to derive or adjust any entry.

| Label | Coupling | Scale | α^{-1} value |
|-------|---------|-------|--------------|
| EM0 | α_em | μ → 0 | 137.036 |
| EM_e | α_em | m_e = 0.511 MeV | 137.036 |
| EM_μ | α_em | m_μ = 105.66 MeV | ≈ 136.0 |
| EM_τ | α_em | m_τ = 1777 MeV | ≈ 133.5 |
| EM_Z | α_em | M_Z = 91.19 GeV | 127.9 |
| W2 | α₂ (SU(2)) | M_Z | ≈ 29.6 |
| W1 | α₁ (U(1) GUT) | M_Z | ≈ 58.7 |
| S3 | α₃ (SU(3)) | M_Z | ≈ 8.47 |

---

## 3. Distance Table: Each Prime vs Each Coupling

For each stable prime $p \in \mathcal{S}$ and each coupling inverse $C_i$:

$$d(p, C_i) = |p - C_i|, \qquad \delta(p, C_i) = \frac{|p - C_i|}{C_i} \times 100\%$$

### 3.1 Prime p = 2

| Coupling | C_i | |p − C_i| | δ (%) | Match? |
|---------|-----|---------|--------|-------|
| EM0 | 137.036 | 135.036 | 98.5% | NO |
| EM_Z | 127.9 | 125.9 | 98.4% | NO |
| α₂^{-1} | 29.6 | 27.6 | 93.2% | NO |
| α₁^{-1} | 58.7 | 56.7 | 96.6% | NO |
| α₃^{-1} | 8.47 | 6.47 | 76.4% | NO |

**p = 2**: No match to any known coupling inverse.  The prime 2 is a structural
element of the theory (the unique even prime; lowest prime-stable element) and
does not correspond to a large inverse coupling.

### 3.2 Prime p = 127

| Coupling | C_i | |p − C_i| | δ (%) | Match? |
|---------|-----|---------|--------|-------|
| EM0 | 137.036 | 10.036 | 7.32% | NO |
| EM_e | 137.036 | 10.036 | 7.32% | NO |
| EM_μ | ≈ 136.0 | ≈ 9.0 | ≈ 6.6% | NO |
| EM_τ | ≈ 133.5 | ≈ 6.5 | ≈ 4.9% | NO |
| **EM_Z** | **127.9** | **0.9** | **0.70%** | **WEAK MATCH** |
| α₂^{-1} | 29.6 | 97.4 | 329% | NO |
| α₁^{-1} | 58.7 | 68.3 | 116% | NO |
| α₃^{-1} | 8.47 | 118.5 | 1400% | NO |

**p = 127**: Weak match to α_em^{-1}(M_Z) = 127.9 with a distance of 0.9 (0.70%).
No match to any other coupling.

### 3.3 Prime p = 137

| Coupling | C_i | |p − C_i| | δ (%) | Match? |
|---------|-----|---------|--------|-------|
| **EM0** | **137.036** | **0.036** | **0.026%** | **STRONG MATCH** |
| EM_e | 137.036 | 0.036 | 0.026% | STRONG MATCH |
| EM_μ | ≈ 136.0 | ≈ 1.0 | ≈ 0.7% | WEAK MATCH |
| EM_τ | ≈ 133.5 | ≈ 3.5 | ≈ 2.6% | NO |
| EM_Z | 127.9 | 9.1 | 7.1% | NO |
| α₂^{-1} | 29.6 | 107.4 | 363% | NO |
| α₁^{-1} | 58.7 | 78.3 | 133% | NO |
| α₃^{-1} | 8.47 | 128.5 | 1518% | NO |

**p = 137**: Strong match to α_em^{-1}(0) = 137.036 with distance 0.036 (0.026%).
Weak proximity to α_em^{-1}(m_μ).  No match to any other coupling.

### 3.4 Prime p = 139

| Coupling | C_i | |p − C_i| | δ (%) | Match? |
|---------|-----|---------|--------|-------|
| EM0 | 137.036 | 1.964 | 1.43% | MARGINAL |
| EM_e | 137.036 | 1.964 | 1.43% | MARGINAL |
| EM_μ | ≈ 136.0 | ≈ 3.0 | ≈ 2.2% | NO |
| EM_τ | ≈ 133.5 | ≈ 5.5 | ≈ 4.1% | NO |
| EM_Z | 127.9 | 11.1 | 8.7% | NO |
| α₂^{-1} | 29.6 | 109.4 | 370% | NO |
| α₁^{-1} | 58.7 | 80.3 | 137% | NO |
| α₃^{-1} | 8.47 | 130.5 | 1541% | NO |

**p = 139**: Marginal proximity to α_em^{-1}(0) at 1.43% but well outside
experimental precision.  The observed value α_em^{-1}(0) = 137.036 is known to
better than 1 ppm; 139 is thus 2 units away from the physical value.
No match to any other coupling.

### 3.5 Prime p = 151

| Coupling | C_i | |p − C_i| | δ (%) | Match? |
|---------|-----|---------|--------|-------|
| EM0 | 137.036 | 13.964 | 10.2% | NO |
| EM_Z | 127.9 | 23.1 | 18.1% | NO |
| α₂^{-1} | 29.6 | 121.4 | 410% | NO |
| α₁^{-1} | 58.7 | 92.3 | 157% | NO |
| α₃^{-1} | 8.47 | 142.5 | 1683% | NO |

**p = 151**: No match to any known Standard Model coupling inverse.

### 3.6 Prime p = 157

| Coupling | C_i | |p − C_i| | δ (%) | Match? |
|---------|-----|---------|--------|-------|
| EM0 | 137.036 | 19.964 | 14.6% | NO |
| EM_Z | 127.9 | 29.1 | 22.7% | NO |
| α₂^{-1} | 29.6 | 127.4 | 430% | NO |
| α₁^{-1} | 58.7 | 98.3 | 167% | NO |
| α₃^{-1} | 8.47 | 148.5 | 1754% | NO |

**p = 157**: No match to any known Standard Model coupling inverse.

---

## 4. Summary Table

| Prime | Closest coupling | Distance | δ (%) | Classification |
|-------|-----------------|----------|--------|---------------|
| 2 | α₃^{-1}(M_Z) = 8.47 | 6.47 | 76% | NON-MATCH |
| 127 | α_em^{-1}(M_Z) = 127.9 | **0.9** | **0.70%** | WEAK MATCH |
| 137 | α_em^{-1}(0) = 137.036 | **0.036** | **0.026%** | STRONG MATCH |
| 139 | α_em^{-1}(0) = 137.036 | 1.964 | 1.43% | MARGINAL |
| 151 | α₁^{-1}(M_Z) ≈ 58.7 | 92.3 | 157% | NON-MATCH |
| 157 | α₁^{-1}(M_Z) ≈ 58.7 | 98.3 | 167% | NON-MATCH |

---

## 5. Classification of Matches

### 5.1 Strong matches

| Prime | Coupling | Distance | Verdict |
|-------|---------|----------|--------|
| p = 137 | α_em^{-1}(0) = 137.036 | 0.036 | **HYPOTHESIS: electromagnetic coupling at Thomson limit** |
| p = 127 | α_em^{-1}(M_Z) = 127.9 | 0.9 | **HYPOTHESIS: electromagnetic coupling at M_Z** |

Both 127 and 137 fall within the running range of the *same* electromagnetic
coupling.  The scale difference spans ≈ 11 orders of magnitude in energy
(m_e → M_Z) and α_em^{-1} changes continuously from 137.036 to 127.9.
See `reports/rg_prime_checkpoint_verdict.md` for the RG analysis.

### 5.2 Non-matches

| Prime | Observation |
|-------|------------|
| p = 2 | Not near any coupling inverse; structural role |
| p = 139 | Within 1.43% of α_em^{-1}(0) but physically distinct (139 ≠ 137.036) |
| p = 151 | No correspondence within 10% to any SM coupling |
| p = 157 | No correspondence within 10% to any SM coupling |

### 5.3 Absent primes

The following Standard Model inverse couplings have **no corresponding stable prime**:

| Coupling | α^{-1} value | Nearest stable prime | Distance |
|---------|------------|---------------------|---------|
| α₂^{-1}(M_Z) ≈ 29.6 | 29.6 | 2 (distance 27.6) or 127 (distance 97.4) | none close |
| α₁^{-1}(M_Z) ≈ 58.7 | 58.7 | none | none close |
| α₃^{-1}(M_Z) ≈ 8.47 | 8.47 | 2 (distance 6.47) | none close |

---

## 6. Hard-Rule Compliance Check

| Rule | Status |
|------|-------|
| No prime assumed to correspond to known coupling | ✓ |
| No prime used to fit or derive coupling value | ✓ |
| Distances computed from coupling inventory before comparison | ✓ |
| No reinterpretation to force matches on 139, 151, 157 | ✓ |
| Matches flagged as hypotheses only | ✓ |

---

## 7. Preliminary Interpretation

- **127 and 137** both sit within the physical running range of α_em^{-1}.
  Their proximity to the low-energy and M_Z values of α_em^{-1} is the only
  numerically significant observation in this data set.
- **139** is close to α_em^{-1}(0) at 1.43% but at a distance of nearly 2 units;
  the physical value is not 139.
- **151, 157** have no proximity to any known SM coupling.
- **2** is a structural prime with no large-α^{-1} interpretation.

The data support at most: *137 and 127 are approximate checkpoints on the
electromagnetic RG trajectory.*  No statement can be made about 139, 151, or 157
without further theoretical input.

---

**Deliverable**: `reports/stable_prime_coupling_comparison.md`  
**Basis for**: `reports/rg_prime_checkpoint_verdict.md`, `reports/stable_prime_coupling_master_verdict.md`
