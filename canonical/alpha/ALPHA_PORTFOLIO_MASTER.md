<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# ALPHA_PORTFOLIO_MASTER.md — T3_ALPHA Alpha Program Portfolio Master

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T3_ALPHA — Fine Structure Constant  
**Purpose**: Single authoritative file governing the alpha program as a
disciplined competing-route portfolio.  
**Status-note (2026-05-10)**: Portfolio planning artifact only.
The single authoritative alpha status file is
`canonical/alpha/ALPHA_MASTER_STATUS.md`.  
**Supersedes**: Root-level `ALPHA_PORTFOLIO_STATUS.md` (2026-04-29).  
**Truth anchor**: `STATUS_OF_UBT.md §T3_ALPHA`

> **Governance rule**: No route may be listed as ACTIVE in any document
> unless it is listed as Tier A or Tier B here.  STATUS_OF_UBT.md governs
> if any conflict arises.

---

## Objective

Derive α⁻¹_bare = 137 (integer) from UBT without fitting any parameter.

**Acceptance criteria**:
1. No number is fitted to reproduce α or 137.
2. Every numerical input is derived from another UBT sector or from S[Θ].
3. Every step is reproducible from a cited proof file.

**Full derivation** (137.036) requires solving Gap G137-B first.

---

## Portfolio Governance Principles

| Principle | Statement |
|-----------|-----------|
| P1 | At most 2 routes per Tier A at any time |
| P2 | Kill weak routes by evidence, not by exhaustion |
| P3 | Promote strong routes by results, not by preference |
| P4 | No route gets permanent privilege or immunity from kill |
| P5 | Tier C routes are monitored but receive zero effort allocation |
| P6 | Monthly reallocation is mandatory — see §Monthly Reallocation |

---

## Current Portfolio Summary

| Tier | Route | Status | Go/No-Go Gate |
|------|-------|--------|---------------|
| **A** | modular_hecke | **ACTIVE** | 2026-05-27 |
| ~~A~~ | ~~electroweak_weinberg~~ | **PARKED** | See note |
| B | theta_spectral | ACTIVE — PARTIAL | No hard gate |
| B | gut_rg | ACTIVE — RELAY | Unlocks when Tier A delivers |
| C | unsupported_numerology | REJECTED | — |
| C | arbitrary_137_patterns | REJECTED | — |

> **Note on electroweak_weinberg**: This route was previously listed as Tier A
> ACTIVE in root-level `ALPHA_PORTFOLIO_STATUS.md`.  That listing is superseded.
> Per `STATUS_OF_UBT.md §Deprecated Claims` and `canonical/gauge/GAUGE_MASTER_STATUS.md §6`,
> the Weinberg angle derivation is a **pure-algebra DEAD END**: the biquaternion algebra cannot
> fix the ratio g'/g.  The route is PARKED; EW-1b (EW1+RG) remains conditional,
> pending first-principles closure in T2_GAUGE.  Active priority: ZERO.

---

## Route Scorecard

| Route | Foundation depth | Independence from α | Gap clarity | Corroborations | Path to completion | Total |
|-------|-----------------|---------------------|-------------|---------------|-------------------|-------|
| **A_PRIME (modular_hecke)** | 3/3 | 3/3 | 3/3 | 3/3 | 2/3 | **14/15** |
| theta_spectral | 2/3 | 3/3 | 2/3 | 1/3 | 1/3 | 9/15 |
| gut_rg | 2/3 | 2/3 | 1/3 | 1/3 | 1/3 | 7/15 |
| electroweak_weinberg | 2/3 | 1/3 | 1/3 | 1/3 | 1/3 | 6/15 |
| A1: gauge_normalization | 2/3 | 1/3 | 1/3 | 1/3 | 1/3 | 6/15 |

---

## Tier A — Primary Routes (max 2 active)

*Criteria for Tier A*: structurally grounded in the biquaternion algebra,
contains at least one proved sub-result, has a clearly stated single
blocking gap, and the gap has a tractable attack path.

---

### modular_hecke — V_eff Prime Attractor + Modular Bootstrap

**Full name**: V_eff prime attractor + modular bootstrap on Kac-Moody level  
**Status**: **ACTIVE**  
**Claim target**: Derive α⁻¹_bare = 137 (integer) from winding-mode spectrum
without fitting any parameter.

**Foundation (proved, no free parameters)**:

| Result | Level | Source |
|--------|-------|--------|
| N_eff = 12 candidate (mode counting) | OPEN/[MC] | `canonical/n_eff/step2_AUDIT.tex` |
| B₀ = 8π (one-loop) | [L1] | `canonical/n_eff/step2_vacuum_polarization.tex` |
| V_eff(n) = n² − B·n·ln n structure | [L1] given B | `canonical/alpha/alpha_best_route.tex` |
| n* = 137 for B_phenom ≈ 46.298 | [L1][COND: G137-B] | `canonical/alpha/alpha_best_route.tex` |
| 137 is prime-stable attractor | [L0]+[STD] | Number theory |
| μ(Γ₀(137))/3 ≈ 46.00 (0.64% from B_phenom) | [L2] | `canonical/alpha/prime_137_status.md` |

**Single blocking gap**: G137-B — derive B_phenom ≈ 46.298 from S[Θ] without
using α as input.  B₀ = 8π (proved) gives n* ≈ 65; missing factor ≈ 1.84.
`B_Ram` is **OBS only, not derived from S[Theta]**. `lambda_exact` and
`lambda_frac` are **OBS only, no derivation currently known**.

**Attack path**:
1. Apply modular bootstrap crossing symmetry to the 4-point function on T².
2. Check if consistency forces k_KM = 1 as the only admissible Kac-Moody level.
3. Alternative: evaluate the one-loop heat kernel of ∇†∇ on T³ × S¹_ψ via
   ζ-function regularisation; if result closes to B_base = N_eff^{3/2}, gap resolves.

**Time-box**: 4 weeks from 2026-04-29 → **go/no-go gate: 2026-05-27**

**Kill condition**: Modular bootstrap produces no k_KM = 1 constraint AND
the heat-kernel path also fails within the time-box.

**If successful**: Write T3_ALPHA paper; claim α⁻¹_bare = 137 at [L1]; submit
as companion note to T1_GR.  
**If not solved** (70–80% probability): Publish conditional integer-137 note
with Gap G137-B explicitly stated; downgrade T3_ALPHA to STRUCTURAL EVIDENCE
status; redirect effort fully to T2_GAUGE.

**Sources**:
- `canonical/alpha/alpha_best_route.tex` — V_eff derivation chain
- `reports/alpha_missing_lemma.md` — exact formulation of G137-B
- `canonical/alpha/prime_137_status.md` — modular corroborations
- `reports/prime_137_structural_audit.md` — structural audit

---

## Tier B — Secondary Routes (max 2 active)

*Criteria for Tier B*: structurally coherent but has multiple blocking gaps,
requires an intermediate result not yet achieved in Tier A, or the attack
path exceeds one month.

---

### theta_spectral — Spectral Geometry / NCG

**Full name**: Spectral geometry / NCG spectral triple of the biquaternion field Θ  
**Status**: ACTIVE — PARTIAL RESULTS  
**Claim target**: Derive B_base from Seeley-DeWitt heat-kernel coefficients
of the Dirac operator on the ℂ⊗ℍ spectral triple.

**Foundation**:

| Result | Level |
|--------|-------|
| ℂ⊗ℍ ≅ M₂(ℂ) — 8 real dimensions | [L0] |
| NCG spectral triple structure defined | [L0] |
| 1⊕3⊕3̄⊕1 decomposition under SU(2) | [L0] |
| B_base/N_gen² ≈ 4.619 ≈ 3π/2 numerical signal | [L2] partial |

**Blocking gap**: det(S'') not computed; no closed-form heat kernel on
Im(ℍ) torus with full UBT field content.

**Promotion condition to Tier A**: Closed-form heat-kernel gives B_base = N_eff^{3/2}
independently, with no free parameters.

---

### gut_rg — GUT RGE Running

**Full name**: GUT-scale prediction + RGE running to IR α  
**Status**: ACTIVE — RELAY ROUTE (cannot deliver α independently; requires Tier A input)  
**Claim target**: Given a UBT-algebraic prediction of α(μ_GUT), run RGE
to obtain α(m_Z) or α(0) using SM beta functions.

**Foundation**:

| Result | Level |
|--------|-------|
| One-loop QED running α(μ₂) from α(μ₁) | [L1] — `canonical/interactions/qed.tex` |
| RGE formula α⁻¹(0) = α⁻¹_bare + (1/3π) ln(Λ/m_e) | [L1] |

**Blocking gaps**:
- Requires UV-scale α prediction from Tier A.
- μ_UV cannot be set without m_e (circular gap).
- α_GUT is a free parameter unless GUT embedding fixes it.

**Role**: Validation relay.  When Tier A delivers α(μ_GUT), this route
verifies that RGE running is consistent with observed α(0).

---

## Parked Routes

| Route | Blocker | Revival condition |
|-------|--------|-------------------|
| electroweak_weinberg | [DEAD for pure algebra; OPEN/COND for EW-1b]: algebra cannot fix g'/g in pure algebra | Only if EW-1b is unblocked via GUT/RG closure in T2_GAUGE |
| gauge_normalization (A1) | Conditional on EW-1 pure-algebra dead end; EW-1b conditional | Same |
| symmetry_breaking_projection (A2) | Conditional on EW-1 + EW-2 | Same |

---

## Killed Routes (Tier C — Zero Effort)

| Route | Status | Failure evidence | Archive |
|-------|--------|-----------------|---------|
| A3: theta_modular_direct | [DEAD] | Exhaustive search — no modular invariant = 137.036 | `reports/failed_routes_graveyard.md` |
| A4: layer2_coding | [DEAD] | Proved impossible: coding fixes spectrum, not coupling magnitude | `reports/failed_routes_graveyard.md` |
| unsupported_numerology | REJECTED | No structural derivation path | Documented in this file |
| arbitrary_137_patterns | REJECTED | Rediscovery of existing [L1] result; not a new derivation | Documented in this file |

---

## What Is Already Achieved (Zero-Parameter Chain)

These results are locked-in and form the foundation all Tier A/B routes build on.

| Result | Level | Source |
|--------|-------|--------|
| N_eff = 12 candidate (mode counting) | **OPEN/[MC]** | `canonical/n_eff/step2_AUDIT.tex` |
| B₀ = 8π one-loop | **[L1]** | `canonical/n_eff/step2_vacuum_polarization.tex` |
| V_eff(n) = n² − B·n·ln n | **[L1] given B** | `canonical/appendices/appendix_alpha_geometry.tex §3` |
| 2n* = B(ln n* + 1) stationarity | **[L1] given B** | `canonical/alpha/veff_corrected_statement.tex` |
| Prime stability of n* = 137 | **[L1]** | Same §4 |
| Dirac charge quantisation | **[L0]** | `canonical/qed_phi_const/appendix_alpha_geometry.tex §1` |

---

## What Is NOT Being Pursued

| Route | Reason | Level |
|-------|--------|-------|
| Weinberg angle sin²θ_W from algebra | [DEAD for pure algebra; OPEN/COND for EW-1b] — algebra cannot fix g'/g in pure algebra | Pure-algebra DEAD END; EW-1b conditional |
| Route A3 (modular direct) | [DEAD] — exhaustive search failed | DEAD END |
| Route A4 (coding constraint) | [DEAD] — proved impossible | DEAD END |
| δ = 0.036 correction without α | [COND] — uses α as input (circular) | CIRCULAR |
| R_ψ calibration from m_e | [SE] — breaks unit-free derivation | SEMI-EMPIRICAL |
| New speculative routes | Forbidden during cleanup window | — |

---

## Monthly Reallocation

**Review date**: Last day of each month  
**Decision criteria**:

| Trigger | Action |
|---------|--------|
| Tier A route hits go/no-go gate and succeeds | Promote to paper draft; declare T3_ALPHA resolved |
| Tier A route hits go/no-go gate and fails | Kill route; promote strongest Tier B to Tier A |
| Tier B route produces B_base independently | Promote to Tier A immediately |
| Tier B route produces no result in 8 weeks | Kill and archive |

**Next reallocation review**: 2026-05-27 (coincides with modular_hecke gate)

**Effort allocation (current)**:
- modular_hecke (Tier A): 100% of T3_ALPHA effort
- theta_spectral (Tier B): 0% active effort (passive monitoring)
- gut_rg (Tier B): 0% active effort (waiting for Tier A)

---

## Evidence Corroboration Register

These are supporting signals, not independent derivations.
They must not be inflated to proof-level claims.

| Signal | Value | Significance | Level |
|--------|-------|--------------|-------|
| μ(Γ₀(137))/3 | ≈ 46.00 (0.64% from B_phenom) | Independent structural signal for B_phenom | [L2] |
| P¹(𝔽₁₃₇) cardinality = μ(Γ₀(137)) | Exact identity | Number-theoretic self-consistency | [L0]+[STD] |
| Hecke eigenvalue → lepton mass ratios | 0.02–0.1% accuracy | Independent of V_eff | [L2] |

---

## Source Files

| Purpose | File |
|---------|------|
| Route detail and scoring | `canonical/alpha/ALPHA_MASTER_STATUS.md` |
| Primary route derivation chain | `canonical/alpha/alpha_best_route.tex` |
| Gap G137-B exact statement | `reports/alpha_missing_lemma.md` |
| Failed routes archive | `reports/failed_routes_graveyard.md` |
| No-fit audit | `reports/alpha_no_fit_audit.md` |
| Structural corroborations | `canonical/alpha/prime_137_status.md` |
| Full route ranking | `reports/alpha_routes_ranked.md` |

---

## Version History

| Date | Change |
|------|--------|
| 2026-04-29 | Created — supersedes `ALPHA_PORTFOLIO_STATUS.md` at root; corrects Weinberg status from ACTIVE to PARKED |


Cross-references: `canonical/alpha/gamma_entropy_alpha_refinement_status.tex`, `reports/gamma_entropy_alpha_interpolation_audit.md`.
