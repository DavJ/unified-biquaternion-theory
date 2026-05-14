<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# alpha_route_scoreboard.md — Alpha Route Scoreboard (3-Route System)

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T2_ALPHA — Fine Structure Constant  
**Purpose**: Machine-readable scoreboard for the three active alpha routes.
Updated every cycle. Determines route priority and kill decisions.

---

## Scoring Criteria (15 points total per route)

| Criterion | Max | Definition |
|-----------|-----|-----------|
| Foundation depth | 3 | How deep is the proved foundation? 3 = [L0] algebraic, 2 = [L1] functional, 1 = speculative |
| α-independence | 3 | Does the route avoid using α as input? 3 = completely, 2 = partially, 1 = α used implicitly |
| Gap clarity | 3 | Are the blockers precisely stated? 3 = exact gap with equation, 2 = qualitative, 1 = vague |
| Corroborations | 3 | Independent signals supporting the route? 3 = two+, 2 = one, 1 = none |
| Path to completion | 3 | Realistic path to closing blockers? 3 = clear strategy, 2 = plausible, 1 = speculative |

---

## Current Scores (2026-04-29)

### Route A — Modular-Hecke

**Name**: modular_hecke_route  
**Target**: Derive B = μ(Γ₀(137))/3 from S[Θ]; provide independent route to n* = 137  
**Score**: **9/15**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| Foundation depth | 2 | Winding-mode action [L1]; heat kernel proved; but Kac-Moody level uncomputed |
| α-independence | 3 | No α input; Hecke structure independent of α |
| Gap clarity | 2 | Gap A-1 (Kac-Moody level) is precisely stated; Gap A-2 (Hecke L-function connection) is qualitative |
| Corroborations | 2 | μ(Γ₀(137))/3 ≈ 46.00 ≈ B_phenom (0.64%); one independent signal |
| Path to completion | 2 | Compute WZW level from boundary term — clear strategy; Hecke L-function computation — plausible |

**Status**: ACTIVE — 4-week time-box starting 2026-04-29  
**Kill condition**: If Kac-Moody level k ≠ 1 OR if L(1, f₁₃₇) does not match B_phenom/π within 1%

---

### Route B — V_eff Spectral (PRIMARY)

**Name**: theta_spectral_v_eff_route  
**Target**: Close Gap G137-B: derive B_phenom ≈ 46.298 from S[Θ] without fitting  
**Score**: **14/15**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| Foundation depth | 3 | N_eff=12 is OPEN/[MC] (critical audit); V_eff route is conditional from S[Theta]; B₀=8π remains audit-context only |
| α-independence | 3 | No α input; all ingredients from biquaternion algebra |
| Gap clarity | 3 | Gap G137-B exactly stated: derive B = B_phenom ≈ 46.298; missing factor ≈ 1.84 quantified |
| Corroborations | 3 | μ(Γ₀(137))/3 + Hecke lepton masses + P¹(𝔽₁₃₇) cardinality |
| Path to completion | 2 | Two-loop heat kernel + Kac-Moody correction — plausible; higher-loop may be needed |

**Status**: PRIMARY — maximum priority; 4-week modular bootstrap attack  
**Kill condition**: If N_eff = 12 candidate fails critical audit (OPEN/[MC])  
**Promotion condition**: Gap G137-B closed ⟹ write T3_ALPHA paper; claim α⁻¹_bare = 137 at [L1]

---

### Route C — EW/GUT Bridge

**Name**: electroweak_or_gut_bridge  
**Target**: GUT embedding of ℂ⊗ℍ → SU(5) → sin²θ_W(GUT) = 3/8 → α(M_Z) → α(0)  
**Score**: **6/15**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| Foundation depth | 2 | SU(3)×SU(2)×U(1) from ℂ⊗ℍ is [L0]; but GUT embedding is unproved |
| α-independence | 1 | Requires gauge coupling g as input (not yet derived from UBT) |
| Gap clarity | 2 | Gap C-1 (GUT embedding) qualitatively stated; Gap G-strong (derive g) not yet formulated precisely |
| Corroborations | 1 | Standard SU(5) GUT prediction sin²θ_W = 3/8 (not UBT-specific) |
| Path to completion | 0 | Two unresolved gaps of high difficulty; no clear strategy for either |

**Status**: ACTIVE (CONDITIONAL) — watch only; requires both Gap C-1 and Gap G-strong  
**Demotion trigger**: If neither Gap C-1 nor Gap G-strong shows progress by 2026-05-13  
**Kill condition**: If Aut(ℂ⊗ℍ) is proved non-embeddable in SU(5)

---

## Route Comparison Table

| Route | Score | Status | Blockers | Priority |
|-------|-------|--------|---------|---------|
| B (V_eff) | **14/15** | **PRIMARY** | Gap G137-B | Highest |
| A (Hecke) | 9/15 | ACTIVE | A-1, A-2 | Second |
| C (GUT) | 6/15 | CONDITIONAL | C-1, G-strong | Watch only |

---

## Killed Routes (for reference)

| Route | Score at kill | Reason |
|-------|--------------|--------|
| A3 (Theta/Modular direct) | 3/15 | Exhaustive search: no modular invariant = 137.036 |
| A4 (Layer 2 coding) | 2/15 | Proved impossible: coding fixes spectrum, not coupling magnitude |
| A1 (Gauge normalization) | 7/15 | Parked: EW-1 pure-algebra route is dead end; EW-1b remains conditional |
| A2 (Symmetry breaking) | 7/15 | Parked: requires Gaps EW-1 + EW-2 (both blocked) |

---

## Decision Rules

| Condition | Action |
|-----------|--------|
| Route score falls below 5 in two consecutive cycles | Demote to PARKED |
| Route score falls below 3 | KILL |
| Route proves main claim | PROMOTE to FLAGSHIP; write paper |
| Route produces zero math progress in 2 cycles | Demote to PARKED |
| New route proposed | Must KILL or PARK another first |

---

## Next Cycle Targets (2026-05-06)

| Route | Target |
|-------|--------|
| B | Compute two-loop heat-kernel correction on S¹_ψ × M⁴; evaluate Kac-Moody level from WZW boundary term |
| A | Compute WZW boundary term contribution; evaluate L(1, f₁₃₇) numerically |
| C | Determine if Aut(ℂ⊗ℍ) → SU(5) embedding exists; if no progress, park |

---

## References

- `canonical/alpha/alpha_equation_matrix.tex` — full equation chains for all routes
- `canonical/alpha/alpha_best_route.tex` — Route B primary derivation
- `canonical/alpha/ALPHA_MASTER_STATUS.md` — master status document
- `reports/alpha_missing_lemma.md` — Gap G137-B exact formulation
- `reports/alpha_hidden_fit_audit.md` — hidden-fit audit


Cross-references: `canonical/alpha/gamma_entropy_alpha_refinement_status.tex`, `reports/gamma_entropy_alpha_interpolation_audit.md`.
