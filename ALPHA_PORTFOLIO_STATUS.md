<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# ALPHA_PORTFOLIO_STATUS.md — Alpha Research: Competing-Route Portfolio

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T3_ALPHA — Fine Structure Constant  
**Purpose**: Maintain a disciplined small portfolio of competing derivation routes
for α.  No route receives permanent privilege.  Routes are promoted or killed by
evidence, not by prior investment.

**Companion files**: `route_scores.md`, `monthly_reallocation.md`

---

## Portfolio Governance Principles

| Principle | Statement |
|-----------|-----------|
| P1 | Do not prematurely commit to one route |
| P2 | Maintain at most 2 routes per tier at any time |
| P3 | Kill weak routes by evidence, not by exhaustion |
| P4 | Promote strong routes by results, not by preference |
| P5 | No route gets permanent privilege or immunity from kill |
| P6 | Tier C routes are monitored but receive zero effort allocation |

---

## Tier A — Primary Routes (max 2 active)

*Criteria for Tier A*: structurally grounded in the biquaternion algebra,
contains at least one proved sub-result, has a clearly stated single blocking
gap, and the gap has a tractable attack path.

---

### A1 — modular_hecke

**Full name**: Modular bootstrap + Hecke structure of the partition function  
**Status**: **ACTIVE** — modular bootstrap NOT YET ATTEMPTED (as of 2026-04-29)  
**Claim target**: Derive B_base = N_eff^{3/2} (or equivalently k_KM = 1) from
crossing symmetry constraints on Ẑ(τ) = ϑ₃³(τ).  If successful, α⁻¹_bare = 137
follows from the proved prime-attractor chain.

**Foundation** (proved, no free parameters):

| Result | Level | Source |
|--------|-------|--------|
| N_eff = 12 from ℂ⊗ℍ | [L0] | `canonical/n_eff/step3_N_eff_result.tex` |
| B₀ = 8π (one-loop) | [L1] | `canonical/n_eff/step2_vacuum_polarization.tex` |
| Ẑ(τ) = ϑ₃³(τ), modular weight 3/2 | [L0] | `research_tracks/T3_ALPHA/`, gap G8 computed |
| V_eff(n) = n² − B ln n structure | [L1] given B | `canonical/appendices/appendix_alpha_geometry.tex §3` |
| n* = 137 is prime-stable attractor | [L1] given B_phenom | `canonical/appendices/appendix_alpha_geometry.tex §4` |
| μ(Γ₀(137))/3 ≈ 46.00 (independent signal) | Structural | `canonical/alpha/prime_137_status.md` |

**Single blocking gap**: Gap G3-k — prove k_KM = 1 from crossing symmetry of the
biquaternion CFT on T².

**Attack path**:
1. Apply modular bootstrap crossing symmetry to the 4-point function on T².
2. Check whether consistency forces k_KM = 1 as the only admissible level.
3. Alternatively: evaluate the one-loop heat kernel of ∇†∇ on T³ × S¹_ψ via
   ζ-function regularisation; if the result closes to B_base = N_eff^{3/2},
   Gap G3-k is resolved without Kac-Moody level machinery.

**Time-box**: 4 weeks from 2026-04-29 → **go/no-go gate: 2026-05-27**

**Kill condition**: Modular bootstrap produces no k_KM = 1 constraint, AND the
heat-kernel path also fails within the time-box.

---

### A2 — electroweak_weinberg

**Full name**: Weinberg angle derivation via electroweak symmetry breaking in UBT  
**Status**: **ACTIVE — CONDITIONAL** (blocked by Gap EW-1; may be unblocked via GUT)  
**Claim target**: Fix sin²θ_W from UBT algebra or GUT embedding, giving
α = g² sin²θ_W / (4π) without fitting any parameter.

**Foundation** (proved):

| Result | Level | Source |
|--------|-------|--------|
| Covariant derivative D_μ with SM gauge groups | [L0] | `canonical/interactions/` |
| Electric charge e = g sinθ_W = g' cosθ_W | Clean algebra | `canonical/alpha/gauge_normalization_attempt.tex` |
| α = e²/(4π) given e | Clean algebra | Standard |
| sin²θ_W(SU(5) GUT) = 3/8 algebraic result | External Lie theory | Not yet embedded in UBT |

**Blocking gaps**:

| Gap | Statement | Severity |
|-----|-----------|----------|
| EW-1 | g'/g not constrained by Aut(ℂ⊗ℍ); U(1)_Y normalisation is free | HIGH |
| EW-2 | Θ₀ VEV as SU(2) doublet not derived from S[Θ] | MEDIUM |
| GUT-UBT | No natural embedding of ℂ⊗ℍ (dim 8) into SU(5) (dim 24) | MEDIUM |

**Known dead end — excluded**: Setting g = g' at EW scale gives sin²θ_W = 1/2,
hence α ≈ 1/97.  This is **definitively excluded** by experiment.  Do not revisit.

**Attack path (most promising)**:
Investigate whether ℂ⊗ℍ embeds algebraically into an exceptional Lie algebra
(E₆, E₇, E₈, or G₂) whose maximal subgroup contains SU(3) × SU(2) × U(1) and
fixes the ratio g'/g.  This would give sin²θ_W(GUT) as a Lie-algebraic prediction
with no free parameters.

**Time-box**: 6 weeks from 2026-04-29 → **go/no-go gate: 2026-06-10**

**Kill condition**: No embedding fixes g'/g by clean algebra after 6-week attack;
route is demoted to Tier B.

---

## Tier B — Secondary Routes (max 2 active)

*Criteria for Tier B*: structurally coherent but either has multiple blocking
gaps, requires an intermediate result not yet achieved in Tier A, or the attack
path is longer than one month.

---

### B1 — theta_spectral

**Full name**: Spectral geometry / NCG spectral triple of the biquaternion field Θ  
**Status**: **ACTIVE — PARTIAL RESULTS**  
**Claim target**: Derive B_base from the Seeley-DeWitt heat-kernel coefficients
of the Dirac operator on the ℂ⊗ℍ spectral triple.

**Foundation**:

| Result | Level |
|--------|-------|
| ℂ⊗ℍ ≅ M₂(ℂ) — 8 real dimensions | [L0] |
| NCG spectral triple structure defined | [L0] |
| 1⊕3⊕3̄⊕1 decomposition under SU(2) | [L0] |
| B_base/N_gen² ≈ 4.619 ≈ 3π/2 numerical signal | [MC] partial |

**Blocking gaps**: det(S'') not computed; no closed-form heat kernel on
Im(ℍ) torus with full UBT field content.

**Dependency**: Benefits from A1 resolution.  If modular bootstrap confirms
k_KM = 1, the spectral triple approach gains a consistency anchor.

**Promotion condition to Tier A**: Closed-form heat-kernel computation gives
B_base = N_eff^{3/2} independently, with no free parameters.

---

### B2 — gut_rg

**Full name**: GUT-scale prediction + RGE running to IR α  
**Status**: **ACTIVE — RELAY ROUTE** (cannot deliver α independently; requires Tier A input)  
**Claim target**: Given a UBT-algebraic prediction of α(μ_GUT) from electroweak
embedding, run RGE to obtain α(m_Z) or α(0) using SM beta functions.

**Foundation**:

| Result | Level |
|--------|-------|
| One-loop QED running α(μ₂) from α(μ₁) | [L1] — `canonical/interactions/qed.tex` |
| QED two-loop correction structure | [L1] — `experiments/alpha_core_repro/alpha_two_loop.py` |
| RGE formula α⁻¹(0) = α⁻¹_bare + (1/3π) ln(Λ/m_e) | [L1] | 

**Blocking gaps**:
- Requires UV-scale α prediction from A2 (electroweak_weinberg) or equivalent.
- μ_UV cannot be set without m_e (Gap A10 — circular).
- α_GUT itself is a free parameter unless GUT embedding fixes it.

**Role**: Validation relay.  When A2 (electroweak_weinberg) delivers α(μ_GUT),
this route verifies that RGE running is consistent with observed α(0).

**Promotion condition to Tier A**: A2 provides a clean UV-scale α prediction;
this route then becomes the bridge to observable α.

---

## Tier C — Rejected / Monitored Routes (zero effort allocation)

*Criteria for Tier C*: No structural derivation path.  Numerical coincidences
without algebraic origin.  Circular use of α or m_e as inputs.  These routes
are listed for completeness and to prevent re-investment.

---

### C1 — unsupported_numerology

**Definition**: Any route that produces a number close to 137.036 (or 137) by
combining UBT-unrelated constants, adjusting combinations post-hoc, or relying
on a coincidence without a derivation chain traceable to S[Θ] or ℂ⊗ℍ axioms.

**Examples already documented and rejected**:

| Expression | Value | Reason for rejection |
|-----------|-------|----------------------|
| j(i) / 1000 | 1.728 | Unrelated modular invariant; no UBT connection |
| e^π (Gelfond constant) | 23.14 | No UBT derivation |
| 16π³ | 4961 | No UBT derivation |
| Hecke T₁₃₇ eigenvalue of Δ | Large integer ≠ 137.036 | No match |
| Dynkin index (adjoint rep) | k = 6 ≠ 1 | Wrong level |
| Dynkin index (fundamental rep) | k = 3/2 ≠ 1 (integer required) | Wrong level |
| g = g' at EW scale → α ≈ 1/97 | Excluded by experiment | |

**Rule**: Any new proposed expression must pass the no-fit audit
(`reports/alpha_no_fit_audit.md`) before it can enter Tier B.

---

### C2 — arbitrary_137_patterns

**Definition**: Any route that observes the integer 137 appearing in some
UBT-adjacent context and asserts this is a new derivation of α, without:
(a) connecting it to the prime-attractor chain already established in [L1], or
(b) providing an independent derivation from S[Θ].

**Already documented as non-independent occurrences of 137**:

| Signal | Source | Why it is not a new derivation |
|--------|--------|--------------------------------|
| 137 as prime-stable V_eff minimum | `canonical/appendices/appendix_alpha_geometry.tex §4` | Already the [L1] primary result |
| Γ₀(137) modular curve | `canonical/alpha/prime_137_status.md` | Structural corroboration, not new derivation |
| P¹(𝔽₁₃₇) cardinality | Same as above | Same corroboration |
| τ(137) Ramanujan τ-function | `alpha_routes_scorecard.md §A3` | Large integer; no match to 137.036 |

**Rule**: Rediscovering that 137 is special does not constitute a derivation of α.
A derivation must produce 137.036 (or at minimum 137 as a zero-parameter result
from B_base) from a fresh derivation path not already counted in the [L1] chain.

---

## Current Portfolio Summary

| Tier | Route | Status | Time-box gate |
|------|-------|--------|---------------|
| A | modular_hecke | ACTIVE | 2026-05-27 |
| A | electroweak_weinberg | ACTIVE — CONDITIONAL | 2026-06-10 |
| B | theta_spectral | ACTIVE — PARTIAL | No hard gate |
| B | gut_rg | ACTIVE — RELAY | Unlocks when A2 delivers |
| C | unsupported_numerology | REJECTED | — |
| C | arbitrary_137_patterns | REJECTED | — |

---

## What Is Already Achieved (Zero-Parameter Chain)

These results are locked-in and are the foundation all Tier A/B routes build on.

| Result | Status | Source |
|--------|--------|--------|
| N_eff = 12 from ℂ⊗ℍ | **PROVED [L0]** | `canonical/n_eff/` |
| B₀ = 8π one-loop | **PROVED [L1]** | `canonical/n_eff/step2_vacuum_polarization.tex` |
| V_eff(n) = n² − B ln n | **PROVED [L1] given B** | `canonical/appendices/appendix_alpha_geometry.tex §3` |
| n* = √(B/2) stationarity | **PROVED [L1] given B** | Same §4 |
| Prime stability of n* = 137 | **PROVED [L1]** | Same §4 |
| Dirac charge quantisation | **PROVED [L0]** | Same §1 |
| Modular weight of Ẑ(τ) = 3/2 | **COMPUTED [L0]** | T3_ALPHA gap G8 |

---

## References

| File | Content |
|------|---------|
| `route_scores.md` | Scoring matrix for all portfolio routes |
| `monthly_reallocation.md` | Reallocation rules and decision calendar |
| `alpha_routes_scorecard.md` | Detailed step-by-step scorecard (A1–A5) |
| `ALPHA_MASTER_STATUS.md` (canonical/alpha/) | Previous single-route status document |
| `ALPHA_PROGRESS_REPORT.md` | 27+ exhausted approach inventory |
| `ALPHA_FINAL_OFFENSIVE.md` | Last-pass offensive analysis |
| `reports/alpha_no_fit_audit.md` | No-fit audit of all routes |
| `canonical/alpha/alpha_best_route.tex` | Prime-attractor derivation chain |
| `reports/alpha_missing_lemma.md` | Exact statement of Gap G3-k / G137-B |
