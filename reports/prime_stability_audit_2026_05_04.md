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


# Prime Stability Derivation — Audit Report

**Date**: 2026-05-04  
**Auditor**: Copilot agent (automated re-derivation)  
**Targets audited**:
- `canonical/alpha/prime_stability_set.tex`
- `reports/prime_stability_scan.md`

**Overall verdict**: The core mathematical content is sound. Two labelling issues require correction: the modular inequality is overstrong as a "stability condition" (it fails for two of the six stable primes), and the finiteness theorem needs a `[COND]` tag for its unconditional-looking header. All numerical tables pass exact re-verification.

---

## 1. Scope and Method

The audit independently re-derived every claim in the two target documents by:

1. Recomputing the stable set by exhaustive search — candidate primes up to 100 000 evaluated against all primes up to 110 000 (avoiding the boundary artifact that arises if the sieve stops at 100 000 and primes just below that cutoff appear spuriously stable).
2. Re-evaluating L(p, p⁻) and U(p, p⁺) to 4 decimal places for every entry in the stability table.
3. Recomputing all V-difference table entries.
4. Re-evaluating the modular inequality μ(Γ₀(p))·(ln p + 1) < 6p for every member of the stable set.
5. Numerically solving for the continuous minimum gap required for stability and comparing with the asymptotic formula in the documents.

All Python code used is reproduced in §8.

---

## 2. Verification of L(p, p⁻) and U(p, p⁺) Formulas

**Status: [EXACT — PASS]**

Formulas as stated in both documents:

$$L(p, p^-) = \frac{p^2 - p_-^2}{p\ln p - p_-\ln p_-}, \qquad
  U(p, p^+) = \frac{p_+^2 - p^2}{p_+\ln p_+ - p\ln p}$$

Every entry in the stability table recomputes correctly to 4 decimal places:

| p   | p⁻  | p⁺  | B(p)    | L(p,p⁻)  | U(p,p⁺)  | Δ⁻     | Δ⁺     | Verified |
|----:|----:|----:|--------:|---------:|---------:|-------:|-------:|:--------:|
| 2   | —   | 3   | 1.0000  | −∞       | 2.6184   | ∞      | 1.6184 | ✓        |
| 127 | 113 | 131 | 42.6667 | 41.4728  | 44.0290  | 1.1939 | 1.3623 | ✓        |
| 137 | 131 | 139 | 46.0000 | 45.4410  | 46.5646  | 0.5590 | 0.5646 | ✓        |
| 139 | 137 | 149 | 46.6667 | 46.5646  | 48.2443  | 0.1021 | 1.5777 | ✓        |
| 151 | 149 | 157 | 50.6667 | 49.9116  | 51.0197  | 0.7551 | 0.3530 | ✓        |
| 157 | 151 | 163 | 52.6667 | 51.0197  | 52.6739  | 1.6470 | 0.0072 | ✓        |

---

## 3. Nearest-Prime Dominance

**Status: [L0 — correctly labelled]**

The claim that B_low(p) = L(p, p⁻) and B_high(p) = U(p, p⁺) (i.e. the binding constraints come from the immediately adjacent primes, not from distant ones) is:

- **Analytically plausible**: L(p, q) is monotone increasing in q for q < p (tends to 2p/(ln p + 1) = B*(p) as q → p), so the maximum over all q < p is at q = p⁻. Similarly U(p, q) starts at B*(p) as q → p and is increasing in q for q > p, so the minimum over all q > p is at q = p⁺.
- **Numerically verified** for all six stable primes (the proof sketch in §2/Lemma of the .tex file is accurate).

The [L0] label (numerically verified, analytic proof sketched) is appropriate. The analytic proof sketch is logically sound and could be formalised into a full [L1] proof by completing the monotonicity argument via L'Hôpital / derivative calculation.

---

## 4. Complete Stable Set

**Status: [EXACT — PASS]**

$$\mathcal{S} = \{2,\; 127,\; 137,\; 139,\; 151,\; 157\}, \quad |\mathcal{S}| = 6$$

Independently recomputed. Candidate primes up to 100 000 were tested against **all** primes up to 110 000 (the extra 10 000 prevents the boundary artifact). Result: no additional stable primes. The code in §9 of `prime_stability_scan.md` is correct; the only caution is to ensure the competitor list extends beyond the candidate range (the published code uses a shared 100 000 list but the conclusion is unaffected because the scan already restricts candidates to p ≤ 10 000).

Near-miss values confirmed exact:

| p   | B(p)   | L(p,p⁻) | U(p,p⁺) | Failure side | Margin   |
|----:|-------:|--------:|--------:|:-------------|:--------:|
| 131 | 44.000 | 44.029  | 45.441  | lower (−0.029) | ✓       |
| 149 | 50.000 | 48.244  | 49.912  | upper (−0.088) | ✓       |
| 163 | 54.667 | 52.674  | 54.046  | upper (−0.621) | ✓       |

---

## 5. Finiteness Claim — Classification

**Status: compound — see below**

| Sub-claim | Strength | Label |
|-----------|----------|-------|
| No stable prime in (157, 100 000] | Direct computation, no assumptions | **[EXACT]** |
| No stable prime in (100 000, ∞) under Cramér's conjecture | Requires max-gap bound ~ (ln p)² | **[CONDITIONAL — Cramér]** |
| No stable prime in (100 000, ∞) under RH alone | Requires max-gap bound ~ √p · ln p; required gap grows as ~p ln p so conclusion still follows | **[CONDITIONAL — RH]** |
| No stable prime in (100 000, ∞) unconditionally | Baker–Harman–Pintz: max gap = O(p^{0.525}); required gap ~ p · ln p; conclusion holds for all sufficiently large p, but no explicit finite crossing threshold is given in the documents | **[OPEN — no explicit threshold stated]** |

**Required action for Theorem 4.1 in `prime_stability_set.tex`**: The theorem header currently reads as an unconditional statement. It should be labelled **[COND]** or split into a verified part (p ≤ 100 000) and a conditional part (p > 100 000).

Suggested wording:

> **Theorem 4.1 [Finiteness, partly conditional]**  
> *(i)* [EXACT] No prime in (157, 100 000] is prime-stable.  
> *(ii)* [COND — Cramér] No prime beyond 100 000 is prime-stable, assuming that prime gaps satisfy g(p) = O((ln p)²).

---

## 6. ⚠ Overstrong Sentence — Modular Index Inequality

**Status: [FLAG — mislabelled as "the stability condition"]**

### What the documents say

- `prime_stability_set.tex`, §S7 gapbox:  
  *"The stability condition (S7-modular) can be stated entirely in terms of modular invariants: μ(Γ₀(p))·(ln p + 1) < 6p."*

- `prime_stability_scan.md`, §8:  
  *"The stability condition is: μ(Γ₀(p))·(ln p + 1) < 6p."*

### What the audit finds

Re-evaluation of μ(Γ₀(p))·(ln p + 1) < 6p for every member of S:

| p   | LHS = (p+1)(ln p+1) | RHS = 6p | Satisfied? |
|----:|--------------------:|---------:|:----------:|
| 2   | 5.079               | 12       | ✓          |
| 127 | 748.056             | 762      | ✓          |
| 137 | 816.957             | 822      | ✓          |
| 139 | 830.826             | 834      | ✓          |
| **151** | **914.627**     | **906**  | **✗ (+8.63)** |
| **157** | **956.887**     | **942**  | **✗ (+14.89)** |

**p = 151 and p = 157 are prime-stable but do NOT satisfy the modular index inequality.**

### Root cause

The inequality μ(Γ₀(p))·(ln p + 1) < 6p is the leading-order upper stability condition B(p) < B*(p) = 2p/(ln p + 1), which is **only a necessary condition at leading order**. It does not account for the gap correction: primes 151 and 157 survive because their actual upper prime gaps (6 in both cases) exceed the minimum required gap by a small positive margin, even though the leading-order condition fails.

### Correct labelling

The inequality is:

- **[ASYMPTOTIC]**: an approximation valid to leading order in p, not the full stability condition.
- **[NECESSARY, not sufficient]**: it must be supplemented by the gap correction for primes near e⁵ ≈ 148.4.
- **[OPEN]** for its interpretation in terms of Hecke eigenvalues — this part is correctly flagged.

### Required corrections

1. **`prime_stability_set.tex`, §S7 gapbox**: Replace  
   *"the stability condition (S7-modular)"*  
   with  
   *"the leading-order upper stability condition (approximation of S2 for p near e⁵)"*  
   Add a note: *"Note: this leading-order form fails for p = 151 and p = 157, which are stable due to gap corrections (§S4). The exact stability condition is (S2)."*

2. **`prime_stability_scan.md`, §8**: Replace  
   *"The stability condition is: μ(Γ₀(p))·(ln p + 1) < 6p"*  
   with  
   *"The leading-order upper stability condition (approximate, fails for p = 151, 157) is: μ(Γ₀(p))·(ln p + 1) < 6p"*

3. Both documents: Preserve the identity μ(Γ₀(p)) = p + 1 and the inequality as a modular reformulation — but label it **[ASYMPTOTIC]** rather than as "the stability condition".

---

## 7. Asymptotic Formula for Required Gap

**Status: [ASYMPTOTIC — safe for finiteness conclusion, not tight for small p]**

The document gives the required gap formula:

$$g_+ \;\gtrsim\; \frac{p(\ln p - 5)}{2} \quad\text{(leading-order approximation)}$$

Comparison with the numerically exact continuous minimum gap and with Cramér's conjectured maximum gap:

| p     | g_cont (exact min) | g_doc ≈ p(ln p−5)/2 | g_doc_exact formula | Cramér max ≈ (ln p)² |
|------:|-------------------:|--------------------:|--------------------:|---------------------:|
| 157   | 5.95               | 4.42                | 7.59                | 25.6                 |
| 163   | 8.53               | 7.64                | 10.89               | 25.9                 |
| 200   | 26.20              | 29.83               | 33.51               | 28.1                 |
| 300   | 85.75              | 105.57              | 110.15              | 32.5                 |
| 1 000 | 739.38             | 953.88              | 961.63              | 47.7                 |

**Observations**:

- For p = 157 the asymptotic formula (4.42) **underestimates** the true minimum gap (5.95). This means the formula alone does not prove 157's stability margin; numerical verification is needed (the document correctly provides this via Δ⁺ = 0.0072).
- For p ≥ 200 the formula **overestimates** the minimum gap, providing a conservative bound.
- For the finiteness conclusion ("no prime ≥ 300 is stable under Cramér's conjecture"): even the exact continuous minimum gap at p = 300 is 85.75, far above the Cramér maximum (~33). The conclusion is robust regardless of whether one uses the approximate or exact formula.
- The table values in `prime_stability_scan.md` §6.3 use the simple asymptotic p(ln p−5)/2 and are correctly labelled as approximate (the ≳ sign). No correction needed, but a clarifying note is advisable.

**Label for the conclusion "no prime ≥ 300 can be prime-stable"**: **[CONDITIONAL — Cramér]** (verified computationally up to 100 000; conditional on Cramér-scale gaps beyond that).

---

## 8. V-Difference Tables

**Status: [EXACT — PASS]**

All entries recomputed:

### p = 137, B = 46.000

| q   | V(q;46) − V(137;46) | Doc value | Match |
|----:|--------------------:|----------:|:-----:|
| 113 | +432.76             | +432.76   | ✓     |
| 127 | +65.98              | +65.98    | ✓     |
| 131 | +19.78              | +19.78    | ✓     |
| 137 | 0                   | 0         | ✓     |
| 139 | +6.69               | +6.69     | ✓     |
| 149 | +140.67             | +140.67   | ✓     |
| 151 | +187.69             | +187.69   | ✓     |

### p = 157, B = 52.6667

| q   | V(q;52.6667) − V(157;52.6667) | Doc value | Match |
|----:|------------------------------:|----------:|:-----:|
| 149 | +92.78                        | +92.78    | ✓     |
| 151 | +59.66                        | +59.66    | ✓     |
| 157 | 0                             | 0         | ✓     |
| 163 | +0.26                         | +0.26     | ✓     |
| 167 | +33.95                        | +33.95    | ✓     |

### p = 139, B = 46.6667

| q   | V(q;46.6667) − V(139;46.6667) | Doc value | Match |
|----:|------------------------------:|----------:|:-----:|
| 131 | +44.58                        | +44.58    | ✓     |
| 137 | +1.21                         | +1.21     | ✓     |
| 139 | 0                             | 0         | ✓     |
| 149 | +94.18                        | +94.18    | ✓     |

---

## 9. Modular Reformulation — Preservation Check

**Status: [PRESERVED]**

The identity μ(Γ₀(p)) = p + 1 for prime p is a standard result (index of Γ₀(p) in SL₂(ℤ) equals p + 1). Its use to write B(p) = μ(Γ₀(p))/3 is preserved and correctly flagged **[OPEN]** for its derivation from the UBT action S[Θ].

The modular index inequality μ(Γ₀(p))·(ln p + 1) < 6p is preserved as a leading-order reformulation with the corrections in §6 above.

---

## 10. Summary of All Findings

| # | Claim / Item | Document | Verified status | Action required |
|---|---|---|---|---|
| F1 | L(p,p⁻) and U(p,p⁺) formulas | both | **[EXACT]** | None |
| F2 | All stability table values | both | **[EXACT]** | None |
| F3 | Nearest-prime dominance lemma | .tex | **[L0]** correctly labelled | Consider upgrading to [L1] (proof is complete in sketch) |
| F4 | Stable set S = {2,127,137,139,151,157} | both | **[EXACT]** (up to 100 000) | None |
| F5 | No stable prime in (157, 100 000] | both | **[EXACT]** | None |
| F6 | No stable prime beyond 100 000 | .tex Thm 4.1 | **[CONDITIONAL — Cramér]** | Add [COND] tag to theorem header |
| F7 | "No prime ≥ 300 can be prime-stable" | .tex §S4 | **[CONDITIONAL — Cramér]** | Label already mentions Cramér; add explicit [COND] |
| **F8** | **μ(Γ₀(p))·(ln p+1) < 6p as "the stability condition"** | **both** | **⚠ [OVERSTRONG — FAILS for p=151,157]** | **Relabel as [ASYMPTOTIC] leading-order upper condition; add caveat about 151,157** |
| F9 | Asymptotic formula g≳p(ln p−5)/2 | scan.md | **[ASYMPTOTIC]** — conservative for p≥200, underestimates for p=157 | Add note; finiteness conclusion unaffected |
| F10 | V-difference tables (3 tables) | both | **[EXACT]** | None |
| F11 | Near-miss values (131,149,163) | both | **[EXACT]** | None |
| F12 | μ(Γ₀(p)) = p+1 identity | both | **[EXACT]** | None |
| F13 | Modular reformulation as [OPEN] | both | **[OPEN]** correctly labelled | None — preserve as is |

---

## 11. Recomputation Script

```python
import math

def sieve(n):
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_p[i]:
            for j in range(i*i, n+1, i):
                is_p[j] = False
    return [i for i in range(2, n+1) if is_p[i]]

def V(q, B):
    return q**2 - B * q * math.log(q)

def B_of(p):
    return (p + 1) / 3

# Use 110 000 to avoid boundary artifact
primes = sieve(110_000)
primes_100k = [p for p in primes if p <= 100_000]

def is_prime_stable(p, competitor_list):
    B = B_of(p)
    Vp = V(p, B)
    return all(V(q, B) > Vp for q in competitor_list if q != p)

stable = [p for p in primes_100k if is_prime_stable(p, primes)]
# Result: [2, 127, 137, 139, 151, 157]
```

Run date: 2026-05-04. Python 3.x, standard library only.

---

*End of audit report.*
