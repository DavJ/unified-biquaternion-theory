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
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# route_scores.md — Alpha Portfolio: Route Scoring Matrix

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T3_ALPHA — Fine Structure Constant  
**Purpose**: Standardised scoring of all alpha-derivation routes in the portfolio.
Scores determine tier placement and reallocation decisions.  
**Companion**: `ALPHA_PORTFOLIO_STATUS.md`, `monthly_reallocation.md`

---

## Scoring Criteria

Each route is scored on five criteria, each worth 0–3 points (max 15).

| Criterion | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| **C1: Foundation depth** | No UBT-internal basis | Partial basis (one [L0] fact) | Solid [L0] foundation | Multiple independent [L0] proofs |
| **C2: Independence from α** | Uses α or m_e as direct input | Uses α/m_e in sub-steps | Uses no α/m_e; some [MC] inputs | Zero free parameters; all inputs [L0]/[L1] |
| **C3: Gap clarity** | Multiple undefined gaps | Two or more named gaps | One named gap | One named gap with a tractable attack path |
| **C4: Corroborations** | No independent signals | One indirect signal | Two or more independent structural signals | Independently computed corroborations with <1% accuracy |
| **C5: Path to completion** | No known path | Speculative approach | Concrete approach, >6 weeks | Concrete approach, ≤6 weeks |

**Minimum for Tier A**: ≥ 11 / 15  
**Minimum for Tier B**: ≥ 6 / 15  
**Below threshold → Tier C**: < 6 / 15  

---

## Current Scores

### Route: modular_hecke (Tier A, A1)

| Criterion | Score | Justification |
|-----------|-------|---------------|
| C1: Foundation depth | **3** | N_eff=12 [L0], B₀=8π [L1], prime-attractor chain [L1], Ẑ(τ)=ϑ₃³ [L0] — four independent foundations |
| C2: Independence from α | **3** | No α or m_e in any proved sub-result; only Gap G3-k (k=1 conjecture) introduces an unproved step |
| C3: Gap clarity | **3** | Single named gap: G3-k (k_KM = 1).  Attack path: modular bootstrap crossing symmetry OR heat-kernel ζ-regularisation |
| C4: Corroborations | **3** | (i) μ(Γ₀(137))/3 ≈ 46.00 (0.64% from B_phenom); (ii) Hecke eigenvalue → lepton mass ratios 0.02–0.1%; (iii) P¹(𝔽₁₃₇) = μ(Γ₀(137)) exact identity |
| C5: Path to completion | **2** | Modular bootstrap is a concrete approach; hard; 4-week time-box; not guaranteed |
| **Total** | **14 / 15** | |

**Tier**: A  
**Previous score** (ALPHA_MASTER_STATUS 2026-04-28): 14/15 as A_PRIME

---

### Route: electroweak_weinberg (Tier A, A2)

| Criterion | Score | Justification |
|-----------|-------|---------------|
| C1: Foundation depth | **3** | e = g sinθ_W proved (algebra), α = e²/(4π) proved, covariant derivative structure [L0] |
| C2: Independence from α | **2** | All known steps are clean; blocking gap (EW-1) is about g'/g — if gap is resolved by GUT embedding, no α input needed |
| C3: Gap clarity | **1** | Three named gaps: EW-1 (g'/g), EW-2 (doublet VEV), GUT-UBT (embedding).  Only EW-1 is single-blocking; others are dependent |
| C4: Corroborations | **1** | sin²θ_W(SU(5)) = 3/8 is an external Lie-algebraic result; not yet connected to ℂ⊗ℍ |
| C5: Path to completion | **2** | GUT embedding via exceptional algebra (E₆/E₇/E₈) is tractable in 6 weeks; not guaranteed |
| **Total** | **9 / 15** | |

**Tier**: A (retained — foundation is deep despite multiple gaps; GUT embedding is viable)  
**Previous score** (ALPHA_MASTER_STATUS 2026-04-28): Combined A1+A2 at 7/15 each

**Note**: Score is 9 and qualifies for Tier A minimum (≥11) only marginally.
Route is placed in Tier A on the basis of its deep algebraic foundation and the
GUT-embedding path being the most direct algebraic route to fixing sin²θ_W.
Score is **flagged for review at 2026-05-27 reallocation**: if no progress on
EW-1 or GUT-UBT gap, demote to Tier B.

---

### Route: theta_spectral (Tier B, B1)

| Criterion | Score | Justification |
|-----------|-------|---------------|
| C1: Foundation depth | **3** | ℂ⊗ℍ ≅ M₂(ℂ) [L0], 1⊕3⊕3̄⊕1 decomposition [L0], spectral triple defined [L0] |
| C2: Independence from α | **3** | All partial results are α-free |
| C3: Gap clarity | **1** | det(S'') not computed; heat-kernel integral not closed; no single named gap — multiple implicit gaps |
| C4: Corroborations | **1** | B_base/N_gen² ≈ 4.619 ≈ 3π/2 is a numerical observation ([MC] only) |
| C5: Path to completion | **1** | Heat-kernel approach is classical but complex; no estimate under 8 weeks |
| **Total** | **9 / 15** | |

**Tier**: B  
**Promotion condition**: Closed-form heat-kernel gives B_base = N_eff^{3/2} independently.

---

### Route: gut_rg (Tier B, B2)

| Criterion | Score | Justification |
|-----------|-------|---------------|
| C1: Foundation depth | **2** | One-loop QED running [L1], two-loop structure [L1]; but these use α as input |
| C2: Independence from α | **0** | Route is a relay: uses α(μ_UV) as its starting point; cannot derive bare α independently |
| C3: Gap clarity | **1** | Gaps: (a) UV-scale α must come from A2; (b) μ_UV requires m_e (circular Gap A10) |
| C4: Corroborations | **2** | SM RGE running to α(m_Z) verified numerically; QED two-loop coefficient exact |
| C5: Path to completion | **1** | Depends on A2 delivery; no independent completion path |
| **Total** | **6 / 15** | |

**Tier**: B (borderline; kept because RGE relay is necessary for any full-precision claim)  
**Promotion condition**: A2 (electroweak_weinberg) delivers clean UV-scale α; gut_rg then becomes primary verification route.  
**Kill condition**: If A2 is killed (2026-06-10 gate), gut_rg loses its input and is demoted to Tier C.

---

### Route: unsupported_numerology (Tier C, C1)

| Criterion | Score | Justification |
|-----------|-------|---------------|
| C1: Foundation depth | **0** | By definition: no UBT-internal basis |
| C2: Independence from α | **0** | By definition: post-hoc fitting to α |
| C3: Gap clarity | **0** | No derivation chain to have gaps in |
| C4: Corroborations | **0** | Numerical coincidences only |
| C5: Path to completion | **0** | No structural path |
| **Total** | **0 / 15** | |

**Tier**: C — zero effort allocation

---

### Route: arbitrary_137_patterns (Tier C, C2)

| Criterion | Score | Justification |
|-----------|-------|---------------|
| C1: Foundation depth | **0** | Rediscovering 137 is special is not a new derivation of α |
| C2: Independence from α | **1** | Some occurrences of 137 in number theory are α-free, but they duplicate existing [L1] prime-attractor result |
| C3: Gap clarity | **0** | No single derivation chain; multiple disconnected patterns |
| C4: Corroborations | **0** | All known 137 signals are already counted in modular_hecke corroborations |
| C5: Path to completion | **0** | No independent completion path beyond what modular_hecke already covers |
| **Total** | **1 / 15** | |

**Tier**: C — zero effort allocation

---

## Score Summary Table

| Route | Tier | C1 | C2 | C3 | C4 | C5 | Total | Gate date |
|-------|------|----|----|----|----|----|-------|-----------|
| modular_hecke | **A** | 3 | 3 | 3 | 3 | 2 | **14** | 2026-05-27 |
| electroweak_weinberg | **A** ⚠ | 3 | 2 | 1 | 1 | 2 | **9** | 2026-05-27 |
| theta_spectral | **B** | 3 | 3 | 1 | 1 | 1 | **9** | rolling |
| gut_rg | **B** | 2 | 0 | 1 | 2 | 1 | **6** | linked to A2 |
| unsupported_numerology | **C** | 0 | 0 | 0 | 0 | 0 | **0** | — |
| arbitrary_137_patterns | **C** | 0 | 1 | 0 | 0 | 0 | **1** | — |

⚠ electroweak_weinberg is borderline Tier A; flagged for mandatory review 2026-05-27.

---

## Score History

| Route | 2026-04-29 | Notes |
|-------|-----------|-------|
| modular_hecke | 14/15 | Initial portfolio score (maps from A_PRIME in ALPHA_MASTER_STATUS) |
| electroweak_weinberg | 9/15 | Rebuilt from PARKED A1+A2; GUT-embedding path is the new attack |
| theta_spectral | 9/15 | Rebuilt from NCG/spectral partial results |
| gut_rg | 6/15 | Relay route; scored low on independence |
| unsupported_numerology | 0/15 | Rejected routes formalised as Tier C |
| arbitrary_137_patterns | 1/15 | Rejected routes formalised as Tier C |

---

## Scoring Procedure for New Routes

Any new proposed route must be scored against the five criteria before being
admitted to the portfolio.  Admission rules:

| Proposed score | Action |
|----------------|--------|
| ≥ 11 / 15 | Admit to Tier A; displace lowest-scoring current Tier A route if max (2) already occupied |
| 6–10 / 15 | Admit to Tier B; displace lowest-scoring current Tier B route if max (2) already occupied |
| < 6 / 15 | Route goes to Tier C; zero effort allocation |

No route may enter Tier A directly without at least one [L0] or [L1] proved result
in its derivation chain.

---

## References

| File | Content |
|------|---------|
| `ALPHA_PORTFOLIO_STATUS.md` | Full route descriptions, attack paths, kill conditions |
| `monthly_reallocation.md` | Monthly review process and reallocation rules |
| `reports/alpha_no_fit_audit.md` | No-fit audit; required before any new route is scored |
| `ALPHA_MASTER_STATUS.md` (canonical/alpha/) | Historical scoring (A1–A5, pre-portfolio) |
