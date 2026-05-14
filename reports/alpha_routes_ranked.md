<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# alpha_routes_ranked.md — All Alpha Routes Ranked

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T3_ALPHA — Fine Structure Constant  
**Purpose**: Rank all known UBT derivation routes to α by strength, honestly.
Kill weak routes explicitly.  Identify the primary route and the single missing lemma.  
**Sources**: `canonical/alpha/alpha_derivation_routes.md`,
`canonical/alpha/prime_137_status.md`, `ALPHA_STRUCTURAL_ORIGINS.md`,
`reports/failed_routes_graveyard.md`

---

## Ranking Criteria

Each route is scored on five criteria (0–3 each, max 15):

| Criterion | 3 | 2 | 1 | 0 |
|-----------|---|---|---|---|
| Foundation depth | [L0] algebra alone | [L1] proved theorem | [MC] conjecture | [COND] circular |
| Independence from α | No α input at all | No α; 1 other experiment | Uses related exp. | Uses α directly |
| Gap clarity | Gap precisely stated; 1 missing lemma | Gap stated; 2+ lemmas | Gap vague | Unknown |
| Corroborations | 2+ independent checks | 1 independent check | Numerical coincidence | None |
| Path to completion | < 4 weeks if gap solved | < 3 months | > 3 months | No path |

---

## Route Rankings

### Rank 1 — A_PRIME: V_eff Prime Attractor

**Claim**: α⁻¹_bare = 137 (integer) from winding-mode spectrum V_eff minimum

**Score**: 14/15

| Criterion | Score | Notes |
|-----------|-------|-------|
| Foundation depth | 3 | N_eff = 12 is [L0]; V_eff structure forced by algebra |
| Independence from α | 3 | No α input; B derived from action (pending gap) |
| Gap clarity | 3 | One gap: G137-B — derive B = B_phenom from S[Θ] |
| Corroborations | 3 | V_eff attractor + modular μ(Γ₀(137))/3 + Hecke lepton masses |
| Path to completion | 2 | Modular bootstrap approach; 4-week time-box |

**Status**: PRIMARY ROUTE — see `canonical/alpha/PRIMARY_ROUTE.md`

**What is proved**: n*(B_phenom) = 137, N_eff = 12, prime stability  
**What is open**: B = B_phenom from S[Θ] (Gap G137-B)  
**Kill condition**: Would be killed if N_eff = 12 derivation fails (extremely unlikely — it is [L0])

---

### Rank 2 — A1: Gauge Normalization (Conditional)

**Claim**: α = e²/(4π) from canonical kinetic-term normalization of A_μ

**Score**: 7/15

| Criterion | Score | Notes |
|-----------|-------|-------|
| Foundation depth | 2 | U(1) identification is [L0]; rest requires symmetry breaking |
| Independence from α | 2 | No α input; but requires sin²θ_W from algebra (OPEN) |
| Gap clarity | 2 | Gap EW-1 clearly stated; but EW-1 itself has sub-gaps |
| Corroborations | 0 | No independent check of Weinberg angle from algebra |
| Path to completion | 1 | Gap EW-1 resisted algebraic approaches; unclear path |

**Status**: CONDITIONAL — blocked by Gap EW-1 (tan θ_W = g'/g from algebra)  
**Killed as standalone alpha route**: Subsumed in T2_GAUGE track (EW mixing paper)  
**Revival condition**: Close Gap EW-1 in T2_GAUGE, then α follows automatically

---

### Rank 3 — A2: Symmetry-Breaking Projection (Conditional)

**Claim**: α from fixing Weinberg angle θ_W via SSB structure SU(2)_L × U(1)_Y → U(1)_EM

**Score**: 7/15

| Criterion | Score | Notes |
|-----------|-------|-------|
| Foundation depth | 2 | SSB pattern is [MC] not [L0] |
| Independence from α | 2 | No α input; but Higgs doublet structure [OPEN] |
| Gap clarity | 2 | Gap EW-1 (same as A1) + Gap EW-2 (VEV as doublet) |
| Corroborations | 0 | No independent check |
| Path to completion | 1 | Two gaps, neither with clear path |

**Status**: CONDITIONAL — same blocker as A1 (Gap EW-1); also blocked by Gap EW-2  
**Killed as standalone route**: Depends on same resolution as A1

---

### Rank 4 — A3: Theta/Modular Route (FAILED)

**Claim**: α⁻¹ = 137.036 from modular invariants of complex time τ ∈ ℍ

**Score**: 3/15

| Criterion | Score | Notes |
|-----------|-------|-------|
| Foundation depth | 1 | Modular structure of τ is [L0]; connection to α is [MC] |
| Independence from α | 2 | No α input |
| Gap clarity | 0 | No gap — the route simply does not work |
| Corroborations | 0 | Exhaustive search found no modular invariant = 137.036 |
| Path to completion | 0 | No completion path identified |

**Status**: **DEFINITIVELY FAILED**

**Failure summary**: Exhaustive search over modular invariants, Hecke eigenvalues,
j-invariants, and eta functions produced no expression equal to α⁻¹ = 137.036.
The integer 137 as a structural feature is captured by Route A_PRIME (V_eff);
the modular route adds no independent content beyond this.

**Final verdict**: KILLED.  No further effort should be spent on this route.

---

### Rank 5 — A4: Layer 2 Coding Constraint (FAILED)

**Claim**: α from Hamming (8,4,4) code or Gray transport constraints on U(1) phase

**Score**: 2/15

| Criterion | Score | Notes |
|-----------|-------|-------|
| Foundation depth | 1 | Coding structure is real; physical interpretation is [MC] |
| Independence from α | 2 | No α input |
| Gap clarity | 0 | Route is not just gapped — it is proved to fail |
| Corroborations | 0 | No independent check |
| Path to completion | 0 | Proved impossible: coding fixes quantization, not magnitude |

**Status**: **DEFINITIVELY FAILED**

**Failure summary**: Coding constraints select admissible charge spectra (integer
or half-integer multiples of a unit charge) but cannot fix the magnitude of the
unit charge.  The coupling strength α = e²/(4π) requires the magnitude of e in
physical units, which depends on the UV cutoff and renormalization scheme — neither
of which is determined by the coding layer.

**Proved impossibility**: The scan (layer2_coding_alpha_scan.py) confirmed that
no combination of L2S/L2T coding constraints produces a numerical output equal to α.

**Final verdict**: KILLED.  No further effort should be spent on this route.

---

### Rank 6 — A5: One-Loop QED Running from UBT (Partial result only)

**Claim**: α(μ₂) = α(μ₁) · [renormalization group factor] from UBT QED sector

**Score**: 8/15

| Criterion | Score | Notes |
|-----------|-------|-------|
| Foundation depth | 2 | QED from φ=const sector is [L1] |
| Independence from α | 1 | Uses α(μ₁) as input; reproduces running but not bare value |
| Gap clarity | 3 | Not a gap — this is a partial result, not a route to bare α |
| Corroborations | 1 | Reproduces SM one-loop RGE correctly |
| Path to completion | 1 | Cannot become a bare-α route without Route A_PRIME |

**Status**: SUPPORTING RESULT — not a standalone alpha route  
**Value**: Validates the QED sector of UBT; does not determine α from first principles.  
**Interpretation**: Given α⁻¹(M_Z) ≈ 128 from experiment, UBT recovers this via
standard QED running from α⁻¹_bare = 137.  This is not a new derivation.

---

## Summary Ranking Table

| Rank | Route | Score | Status | Claim |
|------|-------|-------|--------|-------|
| 1 | **A_PRIME**: V_eff prime attractor | **14/15** | **PRIMARY** | α⁻¹_bare = 137 (integer), gap G137-B |
| 2 | A1: Gauge normalization | 7/15 | CONDITIONAL (EW-1) | α after θ_W fixed |
| 3 | A2: Symmetry-breaking projection | 7/15 | CONDITIONAL (EW-1+EW-2) | α after SSB |
| 4 | A5: One-loop running | 8/15 | SUPPORTING (not a bare-α route) | α(μ₂) from α(μ₁) |
| 5 | A3: Theta/modular | 3/15 | **KILLED** | Failed: no modular invariant = 137.036 |
| 6 | A4: Layer 2 coding | 2/15 | **KILLED** | Failed: coding ≠ coupling magnitude |

---

## Killed Routes Registry

Routes closed forever, with reason:

| Route | Reason for killing | Evidence |
|-------|-------------------|----------|
| A3 Theta/modular | Exhaustive search: no modular invariant produces 137.036 | `alpha_derivation_routes.md §Route A3` |
| A4 Layer 2 coding | Proved: coding fixes spectrum, not coupling strength | `alpha_derivation_routes.md §Route A4`, `layer2_coding_alpha_scan.py` |

---

## What Must Happen Next

1. **4-week time-box on Gap G137-B** (modular bootstrap: derive B = μ(Γ₀(n*))/3 from S[Θ]).
2. If G137-B is solved: publish T3_ALPHA paper with clean integer-137 result.
3. If G137-B is not solved in 4 weeks: publish conditional integer-137 claim
   as a companion note to T1_GR (honest statement of gap).
4. Pursue Gap EW-1 within T2_GAUGE track; if solved, A1/A2 automatically give α.

---

## References

- `canonical/alpha/PRIMARY_ROUTE.md` — the selected primary route
- `canonical/alpha/alpha_derivation_routes.md` — detailed route survey
- `canonical/alpha/prime_137_status.md` — prime 137 structural roles
- `reports/alpha_missing_lemma.md` — Gap G137-B exact statement
- `reports/failed_routes_graveyard.md` — archive of all tried and failed approaches
- `ALPHA_STRUCTURAL_ORIGINS.md` — N_eff and exponent origin
