# Next Steps: Turning Numerical Support into a Proof

**Track:** CORE — Three Generations  
**Date:** 2026-03-06  
**Author:** David Jaroš  
**Status:** Following up on matches found in `step6_hecke_matches.tex`

---

## Current State

SageMath found matching Hecke eigenvalue triples at both p=137 and p=139
(see `step6_hecke_matches.tex`, raw data in `hecke_sage_results.txt`).
These are **numerical support** for Conjecture 2.1, not a proof.

Best match overall: p=139, Match #2 — levels (195, 50, 54), μ-error 0.05%, τ-error 1.63%.
Best match at UBT prime: p=137 — levels (38, 56, 50), μ-error 0.37%, τ-error 3.06%.

---

## What Is Needed for a Proof

### 1. Identify Exact LMFDB Labels

Each matching newform must be identified by its canonical LMFDB label
of the form `N.k.chi.id` (e.g., `38.2.a.a`).

**How to do it:**
- Query `https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/` with
  weight and level filters.
- For each level N and weight k, retrieve all newforms and compute a_p.
- Alternatively, use `search_hecke_lmfdb_api.py` with network access.

**Forms to identify:**

| p   | k | N   | a_p    | LMFDB label (TBD)        |
|-----|---|-----|--------|--------------------------|
| 137 | 2 | 38  | -9     | 38.2.?.?                 |
| 137 | 4 | 56  | -1854  | 56.4.?.?                 |
| 137 | 6 | 50  | -32253 | 50.6.?.?                 |
| 139 | 2 | 195 | 15     | 195.2.?.?                |
| 139 | 4 | 50  | 3100   | 50.4.?.?                 |
| 139 | 6 | 54  | 53009  | 54.6.?.?                 |

**Note:** Multiple newforms may exist at the same level and weight.
The LMFDB label disambiguates them. The SageMath output should specify
which eigenspace (labelled by `a`, `b`, `c`, ...) each form belongs to.

---

### 2. Verify Genuine Newform Status (Not Oldforms)

An oldform is a newform of lower level embedded at a higher level by
the map f(z) → f(dz). Oldforms do not count — Conjecture 2.1 requires
genuine newforms.

**How to check:**
- A newform at level N is a genuine newform if its LMFDB entry has
  `is_self_dual = True` and `atkin_lehner_eigenvals` is non-empty.
- Equivalently: if f has conductor N (level of its associated L-function),
  it is a newform.
- In SageMath: `CuspForms(N, k).newforms('a')` returns only newforms
  by construction.

**Action:** Confirm that the SageMath output already filtered for
newforms (i.e., that `run_hecke_sage.py` used `.newforms('a')` and
not `.basis()`). This should be verified by inspecting the script.

---

### 3. Extend the p=139 Search Systematically

The current p=139 results used "priority levels" — a subset of levels
chosen heuristically. A systematic search should cover:

- **Weight 2:** all levels N ≤ 300 (not just those in priority list)
- **Weight 4:** all levels N ≤ 200
- **Weight 6:** all levels N ≤ 100 (non-CM only — CM forms are excluded
  by the structural argument in step5)

Estimate: ~2 hours SageMath runtime for N ≤ 200 across all three weights.

**Specific question:** Does a p=139 triple with τ-error < 1% exist?
The current best τ-error is 1.39% (Match #1) and 1.63% (Match #2).
Reducing this further would strengthen the case for p=139.

---

### 4. Check for Algebraic Relationship Between Levels and Prime

The levels found (38, 56, 50 for p=137; 195, 50, 54 for p=139) show
no obvious relation to p. A deeper search should check:

- Are any of these levels **conductor of an elliptic curve with CM
  by Q(√(-p))**? (Complex multiplication by the prime.)
- Does the Atkin–Lehner eigenvalue at N equal ±1 (sign in the
  functional equation of L(s,f))?
- Is there a **Shimura correspondence** between the k=2 form at N₀
  and the k=6 form at N₂ that passes through the k=4 form at N₁?
  (The Shimura lift maps weight-k forms to weight-2k forms; this
  could explain the weight pattern 2→4→6.)

---

### 5. Non-coincidence Argument

With thousands of (k=2, k=4, k=6) triples at levels N ≤ 200, some
near-matches within 5% are expected by chance.

**Estimate:** The number of k=6 non-CM newforms at N ≤ 100 is roughly
500–1000. For each, the probability that |a_139/a_195| ∈ [206.7 ± 5%]
(a window of width ~20 out of a Sato–Tate range of ~900) is about 2%.
Expected chance matches: ~0.02 × 1000 = 20. The observed matches are
within this expected noise.

**Consequence:** The mere existence of a match is not surprising.
What would be surprising (and strong evidence for the conjecture) is:
- The matching levels having algebraic relationships to p (see §4).
- The match persisting when stricter tolerance (< 0.1%) is required
  for *both* ratios simultaneously.
- The same newforms appearing from an independent theoretical prediction.

---

### 6. Tau Ratio Improvement

The τ-ratio errors (1.39%–3.06%) are substantially larger than the
μ-ratio errors (0.05%–0.37%). Possible explanations:

- The tau identification may require a different weight assignment
  (e.g., k=8 instead of k=6 for f₂).
- The τ mass itself has larger experimental uncertainty (~0.02%) than
  the μ mass (~0.00001%), but this only accounts for a tiny fraction
  of the 1.4–3% discrepancy.
- The Conjecture may require a correction term (e.g., Atkin–Lehner
  twist of f₂ changes the sign of a_p without changing |a_p|, but
  a twist by a Dirichlet character χ changes a_p to χ(p)a_p).

**Action:** Test twisted forms f₂ ⊗ χ for small characters χ.

---

## Priority Order

1. **[HIGH]** Run `search_hecke_lmfdb_api.py` with network access →
   get LMFDB labels for all matching forms → verify newform status.

2. **[HIGH]** Extend p=139 systematic search (all N ≤ 300 for k=2,
   all N ≤ 200 for k=4, all N ≤ 100 for k=6 non-CM) →
   find if τ-error < 1% match exists.

3. **[MEDIUM]** Check Shimura correspondence between matching forms →
   algebraic explanation for why weights (2,4,6) arise.

4. **[MEDIUM]** Non-coincidence argument → count expected chance matches
   and compare to observed.

5. **[LOW]** Twin-prime {137, 139} theoretical mechanism → only if
   independent theoretical motivation is found.

---

## Milestone

> **Proof milestone:** Conjecture 2.1 is proved when an LMFDB-labelled
> triple of genuine newforms is identified whose Hecke eigenvalue ratios
> at p=137 match the lepton mass ratios within experimental precision,
> and a non-coincidence argument rules out chance.

Current status: **Numerically Supported** (first milestone reached).
Next milestone: **LMFDB labels identified** (requires network access).
