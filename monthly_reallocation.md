<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# monthly_reallocation.md — Alpha Portfolio: Monthly Reallocation Protocol

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T3_ALPHA — Fine Structure Constant  
**Purpose**: Define the rules, criteria, and calendar for monthly portfolio
reallocation.  Ensures no route receives permanent privilege, and effort is
reallocated by evidence rather than inertia.  
**Companion**: `ALPHA_PORTFOLIO_STATUS.md`, `route_scores.md`

---

## Reallocation Principles

| Rule | Statement |
|------|-----------|
| R1 | **Kill weak routes by evidence.** A route failing a time-box gate or scoring below threshold is killed immediately. |
| R2 | **Promote strong routes by results.** A route producing a new proved sub-result moves up by one tier. |
| R3 | **No route gets permanent privilege.** Even the highest-scoring route is re-evaluated at each monthly review. |
| R4 | **Portfolio size is bounded.** Maximum 2 active routes per Tier A, maximum 2 per Tier B. |
| R5 | **Effort tracks tier.** Tier A routes receive the majority of research time; Tier B receive minority support; Tier C receive zero. |
| R6 | **No new routes without scoring.** Any new proposed route must complete the scoring procedure (`route_scores.md`) before being admitted. |

---

## Effort Allocation Guidelines

| Tier | Effort share | Rationale |
|------|-------------|-----------|
| A | ~70–80 % | Highest-probability completion; time-boxed gates |
| B | ~20–30 % | Background development; monitor for promotion |
| C | 0 % | Rejected; monitoring only (prevent re-investment) |

Within Tier A, effort is split proportionally to score gap from the kill threshold.
Example: if A1 scores 14/15 and A2 scores 9/15, A1 receives approximately 60%
of the Tier A allocation and A2 receives approximately 40%.

---

## Reallocation Triggers

Reallocation is triggered by any of the following events:

| Event type | Trigger | Action required |
|-----------|---------|----------------|
| **Time-box gate reached** | A Tier A route reaches its go/no-go date | Evaluate gate outcome; kill or continue |
| **New proved result** | Any route achieves a new [L0] or [L1] sub-result | Re-score the route; consider promotion |
| **Route fails** | A derivation step is proved impossible | Kill the route; move to archive |
| **Score drop** | Monthly review finds no progress; score decreases | Demote or kill |
| **New route proposed** | A new derivation path is identified | Score it; admit to lowest qualifying tier or reject |
| **Monthly review** | End of each calendar month | Mandatory full review regardless of other triggers |

---

## Monthly Review Procedure

The monthly review must complete the following steps in order.

### Step 1: Progress Audit

For each active Tier A and Tier B route, answer:

1. Has any new sub-result been proved (at any level: [L0], [L1], [MC])?
2. Has the single blocking gap narrowed?
3. Has any new corroboration been computed?

Record answers in the **Evidence Log** section below.

---

### Step 2: Re-score Each Route

Apply the five criteria from `route_scores.md` to each route using current state.
Do not carry forward scores from the previous month without re-evaluation.

Record the new score in the Score History table in `route_scores.md`.

---

### Step 3: Apply Promotion/Kill Rules

| Condition | Action |
|-----------|--------|
| Tier A route scores ≥ 11 AND gap narrowed | **Continue** — maintain Tier A |
| Tier A route scores ≥ 11 AND gap NOT narrowed in 30 days | **Warning** — one more month before demotion |
| Tier A route scores 8–10 | **Demote to Tier B** unless the blocking gap was independently closed |
| Tier A route scores < 8 | **Kill** — move to archive; update `ALPHA_PORTFOLIO_STATUS.md` |
| Tier A route reaches time-box gate with no result | **Kill** — no extension without new evidence |
| Tier B route scores ≥ 11 AND Tier A has a free slot | **Promote to Tier A** |
| Tier B route scores ≥ 11 AND Tier A is full | **Replace lowest Tier A route** if the incoming score is ≥ 2 points higher |
| Tier B route scores < 6 | **Kill** — move to archive |
| Tier C route scores ≥ 6 | **Re-admit to Tier B** (this requires presenting a concrete gap-closure path) |

---

### Step 4: Adjust Effort Allocation

Based on updated scores and tier assignments, recalculate effort shares per the
guidelines in the Effort Allocation section above.  Update the next-month work plan.

---

### Step 5: Update Portfolio Documents

After reallocation decisions are final:

1. Update `ALPHA_PORTFOLIO_STATUS.md` — revise route statuses, time-box gates, and kill conditions.
2. Update `route_scores.md` — add current month to Score History table.
3. Update this file — add a row to the Reallocation Log section below.
4. Archive killed routes in `reports/failed_routes_graveyard.md`.

---

## Reallocation Calendar

| Review date | Type | Focus |
|-------------|------|-------|
| **2026-05-27** | Time-box gate + monthly review | Go/no-go on modular_hecke (4-week time-box). Re-evaluate electroweak_weinberg (borderline Tier A). Full portfolio re-score. |
| **2026-06-10** | Time-box gate | Go/no-go on electroweak_weinberg (6-week time-box from 2026-04-29). |
| **2026-06-30** | Monthly review | Full re-score; effort reallocation for Q3 2026. |
| **2026-07-31** | Monthly review | Full re-score; assess theta_spectral promotion readiness. |
| **2026-08-31** | Monthly review | Full re-score. |
| **2026-09-30** | Monthly review | Full re-score. T3_ALPHA annual assessment. |

---

## Kill Protocol

When a route is killed:

1. Update its status in `ALPHA_PORTFOLIO_STATUS.md` to `KILLED — [reason]`.
2. Move its detailed documentation to `reports/failed_routes_graveyard.md` with:
   - The kill date
   - The specific evidence or failure that triggered the kill
   - A summary of all proved sub-results that survive the kill (to be preserved)
3. Do NOT delete any previously proved sub-results.  The prime-attractor chain [L1],
   for example, survives regardless of what happens to modular_hecke's time-box.
4. Update `route_scores.md` Score History with the final score and status.
5. Update this file's Reallocation Log with the kill record.

---

## Promotion Protocol

When a route is promoted from Tier B to Tier A:

1. Check that Tier A has a free slot (max 2).  If not, determine which current
   Tier A route has the lower score; replace it if the incoming score is ≥ 2 points
   higher, otherwise queue the promotion for next month.
2. Update `ALPHA_PORTFOLIO_STATUS.md` — change tier, update attack path and time-box.
3. Assign a new time-box gate (maximum 6 weeks from promotion date).
4. Update `route_scores.md` with promotion date.
5. Adjust effort allocation immediately (do not wait for next monthly review).

---

## Evidence Log

*(Append a new block after each monthly review.)*

---

### 2026-04-29 — Initial Portfolio Setup

| Route | New results since last review | Gap change |
|-------|------------------------------|-----------|
| modular_hecke | Initial setup. Modular bootstrap identified as single untested direction. | G3-k: status unchanged (OPEN — not yet attempted) |
| electroweak_weinberg | GUT-embedding path (E₆/E₇/E₈) formalised as primary attack. | EW-1: OPEN; GUT-UBT: OPEN |
| theta_spectral | NCG spectral triple structure in place. B_base/N_gen² ≈ 3π/2 signal noted. | det(S'') open |
| gut_rg | One-loop and two-loop QED running confirmed. | Waiting on A2 input |

**Reallocation actions taken**:
- Portfolio rebuilt from scratch with competing-route structure.
- modular_hecke: Tier A (replaces A_PRIME single-route designation).
- electroweak_weinberg: Tier A conditional (replaces PARKED A1+A2).
- theta_spectral: Tier B (replaces NCG partial results from DERIVATION_INDEX).
- gut_rg: Tier B relay (replaces BLOCKED A4 relay route).
- Previous "KILLED" designations for A3 and A4 in ALPHA_MASTER_STATUS replaced
  by Tier C to prevent re-investment of identical approaches, while preserving
  the distinction between "no derivation path exists" (C) and "modular bootstrap
  is genuinely untested" (A1 — modular_hecke is the untested direction, not A3).

**Effort allocation for 2026-05**:

| Tier | Route | Effort share |
|------|-------|-------------|
| A | modular_hecke | ~50 % |
| A | electroweak_weinberg (GUT-embedding sub-attack) | ~25 % |
| B | theta_spectral | ~15 % |
| B | gut_rg | ~10 % |
| C | unsupported_numerology | 0 % |
| C | arbitrary_137_patterns | 0 % |

---

## Reallocation Log

*(Append one row per reallocation event.)*

| Date | Event | Route(s) affected | Decision | Outcome |
|------|-------|-------------------|----------|---------|
| 2026-04-29 | Initial setup | All | Portfolio initialised with 4 routes across A/B/C tiers | See Evidence Log above |

---

## References

| File | Content |
|------|---------|
| `ALPHA_PORTFOLIO_STATUS.md` | Full route descriptions, attack paths, kill conditions |
| `route_scores.md` | Scoring criteria and current scores |
| `reports/failed_routes_graveyard.md` | Archive of killed routes |
| `reports/alpha_no_fit_audit.md` | No-fit audit; required before any new route is scored |
| `ALPHA_PROGRESS_REPORT.md` | 27+ exhausted approach inventory; reference for C-tier routes |
