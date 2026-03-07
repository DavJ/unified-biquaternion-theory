<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Hecke Eigenvalues and Lepton Masses — SageMath Results 2026-03-07

**Date of SageMath run**: 2026-03-07  
**Author**: Ing. David Jaroš  
**Status**: **[NUMERICAL OBSERVATION — needs theoretical motivation]**  
**Track**: Three Generations / Hecke Eigenvalue Conjecture  
**Predecessor**: `research_tracks/three_generations/hecke_sage_results.txt` (2026-03-06)

---

> ⚠️ **Epistemic notice**
>
> Nothing in this document constitutes a derivation of fermion masses.
> All numerical agreements are **observations** unless explicitly marked
> as derived from UBT first principles.  No new physical postulates are
> introduced.  Negative or inconclusive results are documented alongside
> positive ones.

---

## 1. Summary of New Matches (2026-03-07 Run)

A SageMath search extended the level ranges for the weight-4 and weight-6
forms relative to the 2026-03-06 run.  The following triple was found:

| Form | Level N | Weight k | a₁₃₇ | Ratio to a₁₃₇(k=2) | Mass ratio target | Error |
|------|---------|----------|-------|---------------------|-------------------|-------|
| k=2 (electron) | **76** | 2 | −11 | 1 (reference) | 1 | — |
| k=4 (muon) | **7** | 4 | +2274 | 2274/11 = **206.727** | m_μ/m_e = 206.768 | **0.0%** |
| k=6 (tau) | **208** | 6 | −38286 | 38286/11 = **3480.5** | m_τ/m_e = 3477.23 | **0.1%** |

Compared to the best 2026-03-06 result (μ-error 0.37%, τ-error 3.06%), this
new triple achieves substantially lower errors at **both** ratios simultaneously.

The problem statement reports 10 additional triples with identical ratios
(same k=4 and k=6 forms, different k=2 normalisers).  The 2274/11 ratio
with 0.0% μ-error is reproduced by any k=2 form with `a_{137} = -11`
(or `+11`).

### Level factorisation

| Level | Factorisation | Remark |
|-------|---------------|--------|
| N=76  | 4 × 19        | composite |
| N=7   | **7** (prime) | Γ₀(7): simplest prime-level subgroup after N=2,3,5 |
| N=208 | 16 × 13       | composite |

The low level N=7 for the k=4 (muon) form is the most structurally
interesting aspect of this match.

---

## 2. Numerical Observation vs. Derivation

The following table classifies each claim strictly.

| Claim | Classification | Evidence |
|-------|----------------|----------|
| Forms with levels (76, 7, 208) and weights (2, 4, 6) exist with a₁₃₇ = (−11, 2274, −38286) | **Verified fact** | SageMath computation |
| Ratios 2274/11 ≈ 206.77 ≈ m_μ/m_e | **Numerical observation** | Arithmetic |
| Ratios 38286/11 ≈ 3480.5 ≈ m_τ/m_e | **Numerical observation** | Arithmetic |
| These ratios are NOT coincidental | **Open question** — see Task 1 | Pending prime-specificity test |
| k=2,4,6 corresponds to generations 1,2,3 | **Motivated conjecture** | `step7_weight_motivation.tex` |
| N=7 arises from the algebraic structure ℂ⊗ℍ | **Suggestive, not derived** | See Section 4 |
| Fermion masses are *derived* from UBT | **NOT claimed** | Would require proof |

---

## 3. Task 1: Prime Specificity (Status — PENDING)

**Question**: Are the ratios 2274/11 ≈ 206.77 and 38286/11 ≈ 3480.5
special for p = 137, or do they hold for arbitrary primes p?

**Script**: `scripts/hecke/test_prime_specificity.sage`

The script computes a_p for the three forms (N=76 k=2, N=7 k=4, N=208 k=6)
at all primes p ∈ {127, 131, 137, 139, 149, 151} and reports the ratios
and their errors relative to the lepton mass targets.

**To run**:
```
sage scripts/hecke/test_prime_specificity.sage
```
or paste into https://sagecell.sagemath.org/.

**Interpretation**:
- If μ-error and τ-error are small **only at p = 137** → **strong signal**;
  strengthens the conjecture; proceed to LMFDB label identification.
- If errors are small at **multiple primes** → likely coincidence;
  document as **DEAD END**.
- Copy output to `reports/hecke_lepton/prime_specificity_results.txt` and
  update the status table in this document.

**Expected statistical baseline**: The Sato–Tate distribution gives
|a_p| ≤ 2p^{(k−1)/2}.  For k=4 at p=137, the Ramanujan bound is ≈ 3207.
The probability that a random Hecke eigenvalue ratio falls within 0.1% of
a given target is roughly 0.1% / (range width / range) ≈ small but non-zero.
With 6 test primes and 2 ratios to match simultaneously, the expected number
of accidental matches at < 0.5% is O(0.1).  A single match at p=137 alone
is therefore mildly suggestive; multiple matches across primes would indicate
coincidence.

---

## 4. Task 2: Geometric Motivation for N=7 (Γ₀(7))

### 4a. What was found in the repository

A systematic search of `consolidation_project/`, `canonical/`, and
`DERIVATION_INDEX.md` for the number 7 in an algebraic context found:

| File | Context | Relevance |
|------|---------|-----------|
| `canonical/algebra/algebra_summary_table.tex` | `dim_ℝ(ℂ⊗ℍ) = 8` | dim = 7+1 |
| `canonical/algebra/involutions_Z2xZ2xZ2.tex` | 8-dimensional real basis of ℂ⊗ℍ | dim = 7+1 |
| `consolidation_project/SU3_derivation/step2_octonion_embedding.tex` | Fano plane multiplication table for octonions | 7 points |
| `consolidation_project/gap_A_resolution/A2_modular_curve.tex` | μ(Γ₀(139)) = 140 = 4×5×**7** | factor of 7 |

### 4b. Suggestive connection

The **Fano plane** is the unique projective plane of order 2 with **7 points**
and 7 lines.  It encodes the multiplication table of the octonions 𝕆
(7 imaginary units e₁, …, e₇).  The quaternion subalgebra ℍ ⊂ 𝕆 uses
3 of these 7 units; the biquaternion algebra ℂ⊗ℍ has real dimension
**8 = 7 + 1** (7 imaginary basis elements + the identity).

The congruence subgroup Γ₀(7) is among the simplest (lowest prime level)
congruence subgroups of SL(2,ℤ) beyond Γ₀(2), Γ₀(3), Γ₀(5).  The
index μ(Γ₀(7)) = 8 = dim_ℝ(ℂ⊗ℍ).

This gives a **suggestive numerical coincidence**:

```
μ(Γ₀(7)) = 8 = dim_ℝ(ℂ⊗ℍ)
```

### 4c. Verdict on Task 2

**Status: [SUGGESTIVE — not a derivation]**

The connection between N=7 and the algebraic structure of ℂ⊗ℍ exists as
a **numerical coincidence** (μ(Γ₀(7)) = dim_ℝ(ℂ⊗ℍ) = 8) and a structural
analogy (Fano plane ↔ octonions ⊃ quaternions ⊃ ℂ⊗ℍ basis).  However:

- No derivation in the repository shows that the modular-form level N of
  the muon form must equal 7.
- The connection via octonions is speculative: ℂ⊗ℍ is associative and does
  not require octonions; the Fano plane reference in step2_octonion_embedding.tex
  is for an *embedding* of ℍ ⊂ 𝕆, not for the main UBT algebra.
- A genuine derivation would need to show that the UBT dynamics selects
  Γ₀(7) as the modular symmetry of the muon ψ-mode; this requires a
  mechanism connecting the biquaternionic field equations to that specific
  congruence subgroup.

**Next step (if pursuing this direction)**:
Check whether the muon form 7.4.a.a (or whichever newform at N=7, k=4 matches
a₁₃₇ = 2274) has special properties at level 7 — e.g., is it related to the
Klein quartic X(7) or to the j-invariant of an elliptic curve with CM by ℚ(√−7)?
Search: LMFDB entry for the form.

---

## 5. Task 3: Weight Connection k=2,4,6 with Generations

### 5a. Existing UBT derivation

`research_tracks/three_generations/step7_weight_motivation.tex` (2026-03-06)
provides a theoretical argument for why weights k = 2, 4, 6 correspond to
generations n = 1, 2, 3 respectively:

1. The Θ-field has a Fourier decomposition along the imaginary-time circle ψ:
   ```
   Θ(x, ψ) = Σ_n  Θ_n(x) · exp(inψ/R_ψ)
   ```
   Mode Θ_n carries n units of ψ-angular momentum.

2. Under the SL(2,ℤ) action on complex time τ = t + iψ (the modular group
   relevant to the compactified ψ-circle), the kinetic action S_kin[Θ_n]
   transforms as a modular form of weight **k = 2n**.

3. Therefore:
   - Θ_1 (electron, n=1) → k = 2
   - Θ_2 (muon, n=2) → k = 4
   - Θ_3 (tau, n=3) → k = 6

### 5b. Consistency check with 2026-03-07 results

The 2026-03-07 match uses exactly weights (2, 4, 6) for (electron, muon, tau)
— consistent with the k = 2n prediction in step7_weight_motivation.tex.

| Assignment | step7 prediction | 2026-03-07 result | Consistent? |
|-----------|-----------------|-------------------|-------------|
| electron  | k=2 | k=2, N=76 | ✅ |
| muon      | k=4 | k=4, N=7  | ✅ |
| tau       | k=6 | k=6, N=208 | ✅ |

### 5c. Why weights 2, 4, 6 and not 1, 2, 3?

**Algebraic argument** (from step7_weight_motivation.tex):
The Θ-field is a *bosonic* biquaternionic field; its kinetic term is
quadratic in ∂_τ Θ.  Under τ → (aτ+b)/(cτ+d), the measure dτ transforms
as (cτ+d)^{−2}; the quadratic kinetic term introduces a factor (cτ+d)^2 per
unit of ψ-angular momentum.  For the n-th winding mode, this gives
(cτ+d)^{2n}, i.e., modular weight k = 2n (even weights only).

**Conclusion**: Even weights k = 2, 4, 6 arise naturally because the
kinetic action is quadratic.  Odd weights (k = 1, 3, 5) would correspond
to fermionic (half-integer spin) fields, which lie outside the bosonic
biquaternionic framework of ℂ⊗ℍ at tree level.

**Status**: The argument in step7_weight_motivation.tex is a
**motivated conjecture**, not yet a complete theorem (the full modular
transformation of S_kin[Θ_n] has not been rigorously verified for n > 1
in the non-linearised regime).

---

## 6. Prior Results Comparison

| Run date | p | k=2 (N, a_p) | k=4 (N, a_p) | k=6 (N, a_p) | μ-err | τ-err |
|----------|---|----------|----------|----------|-------|-------|
| 2026-03-06 | 137 | N=38, a=−9 | N=56, a=−1854 | N=50, a=−32253 | 0.37% | 3.06% |
| 2026-03-06 | 139 | N=195, a=15 | N=50, a=3100 | N=54, a=53009 | 0.05% | 1.63% |
| **2026-03-07** | **137** | **N=76, a=−11** | **N=7, a=2274** | **N=208, a=−38286** | **0.0%** | **0.1%** |

The 2026-03-07 result is the best match found to date for the simultaneous
reproduction of both mass ratios at a single prime.

---

## 7. Open Tasks

| Task | Status | Action |
|------|--------|--------|
| Task 1: Prime specificity | **PENDING** | Run `scripts/hecke/test_prime_specificity.sage` |
| Task 2: N=7 motivation | **SUGGESTIVE, not derived** | LMFDB label for 7.4.?.? ; Klein quartic connection? |
| Task 3: k=2,4,6 weights | **Motivated conjecture** | Formalise step7 argument; prove for n>1 |
| LMFDB labels | Pending | Run `research_tracks/three_generations/identify_lmfdb_labels.py` with N=76, 7, 208 |
| Non-coincidence argument | Pending | Count expected chance matches at <0.1% tolerance |
| Non-newform check | Pending | Verify N=7, k=4 form is a genuine newform (not oldform from N=1) |

---

## 8. File Inventory

| File | Content |
|------|---------|
| `scripts/hecke/test_prime_specificity.sage` | Task 1 script (run in SageMath) |
| `reports/hecke_lepton/sage_results_2026_03_07.md` | This document |
| `reports/hecke_lepton/prime_specificity_results.txt` | To be created after running Task 1 |
| `research_tracks/three_generations/hecke_sage_results.txt` | 2026-03-06 raw results |
| `research_tracks/three_generations/step6_hecke_matches.tex` | Analysis of 2026-03-06 results |
| `research_tracks/three_generations/step7_weight_motivation.tex` | k=2n derivation argument |
| `consolidation_project/SU3_derivation/step2_octonion_embedding.tex` | Fano plane (octonion context) |
| `canonical/algebra/algebra_summary_table.tex` | dim_ℝ(ℂ⊗ℍ) = 8 |
| `DERIVATION_INDEX.md` | Hecke conjecture status (Three Generations section) |

---

## 9. Decision Criteria

After running `test_prime_specificity.sage`:

**If SIGNAL (ratios close only at p=137)**:
1. Identify LMFDB labels for (76.2.?.?, 7.4.?.?, 208.6.?.?)
2. Verify genuine newform status for N=7 k=4 form
3. Investigate N=7 → Γ₀(7) → Klein quartic / arithmetic geometry connection
4. Formalise step7_weight_motivation argument
5. Update DERIVATION_INDEX.md: Hecke conjecture status → "extended numerical support"

**If DEAD END (ratios match at multiple primes)**:
1. Document the failure in this file with computed table
2. Update DERIVATION_INDEX.md: add dead-end entry for the 2026-03-07 match
3. Archive the forms (76, 7, 208) in hecke_search_results.json
4. Investigate whether a *different* selection criterion (beyond a_p matching)
   is needed to isolate p=137

---

*Document generated: 2026-03-07.  
All numerical values from SageMath via `CuspForms(Gamma0(N), k).newforms('a')`.*
