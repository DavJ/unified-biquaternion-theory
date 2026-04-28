<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# alpha_no_fit_progress.md — α Derivation: No-Fit Progress Report

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T3_ALPHA — Weinberg-Angle Program  
**Purpose**: Concise, honest progress report on deriving α without numerical
fitting. Documents what is proved, what is blocked, and current attack priorities.  
**Companion files**: `canonical/alpha/ew_mixing_gap_map.md`,
`reports/ew_mixing_status.md`, `research_tracks/T3_ALPHA/alpha_status_report.md`

---

## Executive Summary

| Item | Status |
|------|--------|
| α⁻¹ = 137 from V_eff attractor (bare value) | PROVED [L1] given B_base |
| B₀ = 8π one-loop coefficient | PROVED [L1] |
| N_eff = 12 from ℂ⊗ℍ mode counting | PROVED [L0] |
| Equal coupling near-miss: sin²θ_W = 1/2 (excluded) | CONFIRMED [L0] |
| A5 icosahedral candidate: sin²θ_W = (5−√5)/10 ≈ 0.276 | NEW — SUGGESTIVE, unanchored |
| tan θ_W = g'/g from UBT first principles | BLOCKED — Gap EW-1 |
| Fully closed first-principles derivation of α | NOT ACHIEVED |

**Strategy update**: The direct α derivation remains blocked at B_base (27+
approaches exhausted). The reframing as the Weinberg-angle program has produced
one new lead: the icosahedral A5 discrete symmetry group gives sin²θ =
(5−√5)/10 ≈ 0.276 from projection geometry of Platonic axes. This is the
closest clean algebraic expression to sin²θ_W(M_Z) ≈ 0.231 found to date.

---

## Proved Results (Unchanged)

### N_eff = 12 [L0]

The count of charged modes contributing to one-loop vacuum polarization:

```
N_eff = N_phases × N_helicity × N_charge = 3 × 2 × 2 = 12
```

where N_phases = dim_ℝ(Im ℍ) = 3 (from the quaternion imaginary basis).

**Source**: `canonical/n_eff/`, `canonical/appendices/appendix_alpha_geometry.tex §2`

### B₀ = 8π [L1]

```
B₀ = 2π N_eff / 3 = 2π × 12 / 3 = 8π ≈ 25.133
```

**Source**: `canonical/n_eff/step2_vacuum_polarization.tex`

### Prime attractor α⁻¹ = 137 (bare) [L1, given B_base]

V_eff minimum at n* = 137 given B_base = N_eff^{3/2} = 12^{3/2} ≈ 41.57.

**Source**: `canonical/appendices/appendix_alpha_geometry.tex §3`

### Equal-norm excluded [L0]

The simplest UBT kinetic-term result (equal SU(2)_L and U(1)_Y norms) gives
sin²θ_W = 1/2, excluded at 7σ by experiment.

**Source**: `reports/ew_mixing_status.md §1`

---

## New Lead: A5 Icosahedral Prediction

**New result from the polyhedral scan** (`report/polyhedral_weinberg_scan.md`):

The icosahedral symmetry group A5 produces a parameter-free algebraic prediction
from the angle between its 5-fold (C₅) and 2-fold (C₂) rotation axes:

```
sin²θ = 1/(φ+2) = (5−√5)/10 ≈ 0.2764
```

where φ = (1+√5)/2 is the golden ratio.

**Status**: SUGGESTIVE — requires physical justification.

**Why it is not yet a derivation**:
1. No UBT-internal reason identified for why A5 acts on the EW mixing sector.
2. The axis identification T₃ ↔ C₅, Y ↔ C₂ is not derived.
3. The prediction (5−√5)/10 ≈ 0.276 is 19.5% above sin²θ_W(M_Z) = 0.231 and
   26% below sin²θ_W(M_GUT) = 0.375. It would require matching at an
   intermediate scale whose value is not predicted.

**What would validate this lead**:
- Show that A5 is a discrete symmetry subgroup of Aut(ℂ⊗ℍ) acting on the EW mixing plane.
- Derive the axis identification from the UBT covariant derivative structure.
- Compute the scale at which sin²θ_W(μ) = (5−√5)/10 and check consistency.

---

## Route Status Update

### Route A1: Algebra Normalization

**Current state**: The UBT kinetic term Tr[(D_μΘ)†(D^μΘ)] has equal SU(2)_L
and U(1)_Y normalization by construction → sin²θ_W = 1/2 (excluded).

**Path forward**: Identify a mechanism that breaks the equal-norm symmetry. Two
candidates:
- (i) The SU(2)_L Casimir differs from the U(1)_Y charge normalization when
  the broken phase is considered (Higgs-mechanism normalization shift).
- (ii) Embedding in a GUT group via McKay changes the relative normalization.

**Status**: BLOCKED at Gap EW-1.

### Route A2: Symmetry-Breaking Projection

**Current state**: The electroweak breaking pattern SU(2)_L × U(1)_Y → U(1)_EM
is identified. The Θ₀ VEV as doublet is a candidate but not proved.

**Status**: BLOCKED at Gap EW-2 (doublet identification).

### Route A3: Theta/Modular

**Status**: FAILED — no modular invariant produces α⁻¹ = 137.036.

### Route A4: Coding (L2 Hamming)

**Status**: FAILED — coding fixes charge spectrum, not coupling magnitude.

### Route A5 (new): Polyhedral / A5 Icosahedral

**Current state**: Clean algebraic prediction (5−√5)/10 from A5 axis geometry.
Physical identification not yet established.

**Status**: CANDIDATE — needs investigation of A5 ⊂ Aut(ℂ⊗ℍ).

---

## Blocking Gap: EW-1

All routes to sin²θ_W (and hence α) converge on the same blocker:

> **Gap EW-1**: Derive the ratio tan θ_W = g'/g from UBT first principles.
> The relative normalization of the SU(2)_L and U(1)_Y kinetic terms is
> a free parameter in the current formulation.

Full obstruction map: `canonical/alpha/ew_mixing_gap_map.md`

---

## Prioritized Next Attacks

| Priority | Attack | Description |
|----------|--------|-------------|
| 1 | **A5 ⊂ Aut(ℂ⊗ℍ) check** | Is A5 (icosahedral group) a discrete symmetry of the UBT algebra? If yes, the (5−√5)/10 prediction becomes anchored. |
| 2 | **UBT kinetic term symmetry breaking** | Does the complex-time structure τ = t+iψ break the U(1)×U(1) norm symmetry of the kinetic term? If yes, the ratio g'/g could be fixed dynamically. |
| 3 | **E₇ non-SU(5) breaking chain** | Complete the E₇ → SM breaking analysis via all maximal subgroup chains; determine if any gives sin²θ_W consistent with 0.231 without the SU(5) subalgebra. |
| 4 | **ψ-winding hypercharge derivation** | Derive the U(1)_Y hypercharge quantum numbers from the ψ-circle winding representation theory; this would fix the Y normalization (Gap EW-3). |

---

## What Has NOT Been Attempted

| Approach | Reason not tried | Worth trying? |
|----------|----------------|---------------|
| Non-perturbative fixed-point for g'/g | Requires functional RG in UBT (not yet set up) | Yes, long-term |
| A5 as symmetry of S[Θ] | New lead from polyhedral scan | **Yes, next priority** |
| E₇ non-SU(5) breaking | E₇ breaking chains not fully computed | Yes |
| Complex-time normalization effect | Effect of ψ rotation on kinetic-term normalization | Yes |

---

## Timeline Assessment

- **sin²θ_W derived from first principles**: 6–18 months if A5 lead is valid;
  blocked indefinitely otherwise.
- **α derived from sin²θ_W + UBT g calculation**: Depends on sin²θ_W derivation.
- **Current fallback**: Document Gap EW-1 precisely (this document) and focus
  on T1_GR flagship first (per meta-control allocation).

---

## References

- `canonical/alpha/ew_mixing_gap_map.md` — full gap analysis
- `canonical/alpha/weinberg_angle_routes.md` — routes survey
- `canonical/alpha/alpha_derivation_routes.md` — routes A1–A4
- `report/polyhedral_weinberg_scan.md` — polyhedral scan (new)
- `reports/alpha_no_fit_audit.md` — previous audit
- `research_tracks/T3_ALPHA/alpha_status_report.md` — historical status
