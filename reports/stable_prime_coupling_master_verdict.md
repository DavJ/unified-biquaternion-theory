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


# Stable-Prime Coupling Master Verdict

**Task**: `map_stable_prime_sectors_to_coupling_constants` — Target 5  
**Author**: Ing. David Jaroš  
**Date**: 2026-05-10  
**Mode**: hypothesis_test_no_numerology  
**Status**: Final verdict

**Constituent reports**:
- `reports/coupling_inventory.md` — Target 1
- `reports/stable_prime_coupling_comparison.md` — Target 2
- `research_tracks/coupling_spectrum/rg_prime_checkpoints.tex` + `reports/rg_prime_checkpoint_verdict.md` — Target 3
- `research_tracks/coupling_spectrum/multi_coupling_projection_hypothesis.tex` — Target 4

---

## 1. Stable Prime Set

$$\mathcal{S} = \{2,\; 127,\; 137,\; 139,\; 151,\; 157\}$$

Derived from the UBT prime-stability condition.  No physical input used in derivation.

---

## 2. Per-Prime Coupling Verdict

| Prime | Closest SM coupling inverse | Distance | δ (%) | RG role | Verdict |
|-------|---------------------------|----------|--------|---------|--------|
| 2 | — | — | — | None identified | STRUCTURAL ELEMENT |
| 127 | α_em^{-1}(M_Z) = 127.9 | 0.9 | 0.70% | Approx. RG endpoint at M_Z | OBSERVED_CONSISTENCY |
| 137 | α_em^{-1}(0) = 137.036 | 0.036 | 0.026% | Approx. RG endpoint at low E | OBSERVED_CONSISTENCY |
| 139 | α_em^{-1}(0) = 137.036 | 1.964 | 1.43% | No RG checkpoint | NO_EVIDENCE |
| 151 | None within 10% | > 13 | > 10% | No RG checkpoint | NO_EVIDENCE |
| 157 | None within 10% | > 19 | > 14% | No RG checkpoint | NO_EVIDENCE |

---

## 3. Evaluation by Verdict Option

### OBSERVED_CONSISTENCY ✓ (partial)

The stable prime set *includes* both known electromagnetic RG checkpoints:
- p = 137 is near α_em^{-1}(0) = 137.036 (distance 0.036, 0.026%)
- p = 127 is near α_em^{-1}(M_Z) = 127.9 (distance 0.9, 0.70%)

Both lie inside the physical running window of α_em^{-1}.  This is an
**observed consistency**, not a derivation.  The stable primes do not derive
the electromagnetic coupling; they are numerically proximate to known checkpoints.

**Applies to**: p ∈ {127, 137}

### PLAUSIBLE_RG_STRUCTURE ✓ (partial, for electromagnetic pair only)

The RG trajectory of α_em^{-1} runs continuously from ~137.036 at μ → 0 to
~127.9 at μ = M_Z.  The stable-prime set contains approximate values at both
endpoints (137 and 127 respectively).  The separation in the stable-prime set
(Δp = 10) is close to the physical running (Δα^{-1} = 9.136).

This constitutes a **plausible RG structure** for the electromagnetic pair only:
the prime-stability condition accidentally (or non-accidentally) selects primes
near both endpoints of the known electromagnetic running.

**Applies to**: {127, 137} as a pair  
**Condition**: This interpretation requires a UBT mechanism that explains *why*
the prime-stability condition singles out primes near the endpoints of α_em^{-1}.
No such mechanism is currently derived.

### MULTI_COUPLING_CANDIDATE ✗ (not supported)

The three primes {139, 151, 157} have no correspondence to any known SM coupling:
- α₂^{-1}(M_Z) ≈ 29.6 — distant
- α₁^{-1}(M_Z) ≈ 58.7 — distant
- α₃^{-1}(M_Z) ≈ 8.47 — distant

No coupling projection mechanism from S[Θ] is currently derived.  The
multi-coupling projection hypothesis (Target 4) is speculative and incomplete.

**Does not apply.**

### NO_EVIDENCE (partial, for {2, 139, 151, 157})

Four of the six stable primes have no identified SM coupling correspondence:
- p = 2: structural element, no large inverse coupling interpretation
- p = 139: within 1.43% of α_em^{-1}(0) but the physical value is 137.036, not 139
- p = 151: no SM coupling within 10%
- p = 157: no SM coupling within 10%

**Applies to**: p ∈ {2, 139, 151, 157}

---

## 4. Synthesis

The verdict is a combination:

| Category | Applies to | Status |
|----------|-----------|-------|
| OBSERVED_CONSISTENCY | {127, 137} | ✓ Both near α_em^{-1} endpoints |
| PLAUSIBLE_RG_STRUCTURE | {127, 137} as pair | ✓ Conditional (mechanism not derived) |
| MULTI_COUPLING_CANDIDATE | — | ✗ No evidence for {139, 151, 157} |
| NO_EVIDENCE | {2, 139, 151, 157} | ✓ |

**Primary verdict**:

> OBSERVED_CONSISTENCY + PLAUSIBLE_RG_STRUCTURE (for electromagnetic pair)  
> NO_EVIDENCE (for remaining primes)

---

## 5. What Would Change This Verdict?

| Condition | Would upgrade to |
|-----------|-----------------|
| Derivation of α_em^{-1}(0) = 137.036 from S[Θ] without primes | DERIVATION |
| Derivation of α_em^{-1}(M_Z) = 127.9 from S[Θ] and running | DERIVATION |
| UBT mechanism producing effective coupling inverses near {139, 151, 157} | MULTI_COUPLING_CANDIDATE |
| Demonstration that the proximity is a mathematical coincidence with probability > 0.05 | Weakens to NO_EVIDENCE |

---

## 6. Hard-Rule Compliance

| Rule | Status |
|------|-------|
| No prime assumed to correspond to known coupling | ✓ |
| No prime used to fit or derive coupling | ✓ |
| No reinterpretation to force matches | ✓ |
| 139, 151, 157 assessed as NO_EVIDENCE | ✓ |
| Offsets explicitly stated | ✓ |
| Verdict matches available evidence | ✓ |

---

## 7. Mandatory Final Sentence

**Stable primes do not currently map to Standard Model couplings beyond alpha-like coincidences.**
