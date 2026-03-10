# Fine Structure Constant α — Derivation Status

**Author**: Ing. David Jaroš  
**Date**: 2025  
**Status**: SEMI-EMPIRICAL — formula structure proved; B_base exponent open

---

## Overview

The fine structure constant α ≈ 1/137.036 is one of the most precisely
measured constants in physics. The Unified Biquaternion Theory (UBT) attempts
to derive it from first principles rather than treating it as an empirical
input. This document gives the current derivation status accurately and without
overstating the results.

---

## The UBT Derivation Chain

The UBT derivation of α proceeds through the following stages:

### Stage 1: Topological coupling B₀ = 8π (PROVED [L1])

The bare topological coupling is:
```
B₀ = 8π
```
This is derived from the kinetic action S_kin[Θ] by integrating the
biquaternionic field over the compact imaginary-time circle.

- **Status**: PROVED [L1] — zero free parameters
- **Source**: `canonical/interactions/qed.tex`, §4;
  `consolidation_project/N_eff_derivation/step2_vacuum_polarization.tex`

### Stage 2: Formula structure α = B₀ / (B_base + B_α) (PROVED [L1], structure only)

The UBT prediction takes the form:
```
α = B₀ / (B_base + B_α)
```
where:
- **B₀ = 8π** — topological coupling (PROVED)
- **B_base ≈ 41.57** — leading quantum correction (PARTIALLY DERIVED)
- **B_α ≈ 46.3** — one-loop running contribution (SEMI-EMPIRICAL)

The structural form of this formula is proved. The numerical values of
B_base and B_α are not independently derived.

- **Source**: `canonical/interactions/qed.tex`, §5

### Stage 3: Running coupling formula (PROVED structure; SEMI-EMPIRICAL numerics)

The running coupling takes the form:
```
1/α(μ) = 1/α(μ₀) + (B_α / 2π) ln(μ/μ₀)
```
The structural derivation from N_eff = 12 is proved. The precise coefficient
B_α ≈ 46.3 depends on the open B_base value.

- **Status**: Structural form PROVED [L1]; B_α numerical value SEMI-EMPIRICAL [SE]
- **Source**: `STATUS_ALPHA.md`, §7

### Stage 4: B_base = N_eff^(3/2) = 41.57 (OPEN HARD PROBLEM)

The formula `B_base = N_eff^(3/2)` with N_eff = 12 gives B_base ≈ 41.57.
The factor:
- Factor 3 = dim_ℝ(Im H) is an algebraic fact [L0]
- Factor 2 from Gaussian integration is proved [L1]

**The exponent 3/2 has not been derived from first principles.**

- **Status**: OPEN [O]
- **Source**: `canonical/bridges/QED_limit_bridge.tex`, §3

---

## Summary Table

| Derivation step | Status | Source |
|-----------------|--------|--------|
| B₀ = 8π | **PROVED [L1]** | `qed.tex` §4 |
| Formula structure α = B₀/(B_base+B_α) | **PROVED [L1]** (structure) | `qed.tex` §5 |
| QED Lagrangian producing running coupling | **PROVED [L1]** | `qed.tex` §1 |
| U(1) gauge invariance | **PROVED [L1]** | `qed.tex` §2 |
| B_α ≈ 46.3 numerical value | **SEMI-EMPIRICAL [SE]** | `STATUS_ALPHA.md` §7 |
| B_base exponent 3/2 | **OPEN [O]** | `QED_limit_bridge.tex` §3 |
| R ≈ 1.114 geometric correction | **OPEN [O]** | `PROOFKIT_ALPHA.md` §5 |
| Numerical reproduction α ≈ 1/137.036 | **VERIFIED** (with fitted B_base) | `appendix_ALPHA_one_loop_biquat.tex` |

---

## Open Problems

### Open Problem 1: B_base Exponent (3/2)

The formula `B_base = N_eff^(3/2)` is a motivated conjecture.
22 approaches have been tested (spectral theory, p-adic methods,
holographic arguments, topological arguments, dimensional analysis)
and none has produced a complete derivation.

A promising direction involves Kac–Moody algebras at level k = 1, motivated
by the relation `k · dim(g) = N_eff`. However, the direct computation of
the Kac–Moody level from the UBT action S[Θ] is an open gap (Gap G3-k).

**Status**: OPEN [O]

### Open Problem 2: Geometric Factor R ≈ 1.114

The one-loop correction involves a factor R ≈ 1.114 bridging
`B_base = 41.57 → B_α ≈ 46.3`. Its geometric origin is unknown.
Eight approaches have been tested. All have reached dead ends.

**Status**: OPEN [O]

### Open Problem 3: N_eff Spectral Uniqueness

Even if the BRST cohomology assumptions A1–A3 are accepted, the spectral
uniqueness of N_eff ≈ 11.53 has not been proved — it is possible in principle
that other values could arise.

**Status**: MOTIVATED [L2]

---

## What Conclusions Are Warranted

- The α formula and B₀ derivation are suitable for publication as a
  semi-empirical result with a clear statement that B_base is fitted.
- **Claims of a complete ab initio derivation of α must not be made**
  until the B_base exponent is fully derived.
- The numerical match α ≈ 1/137.036 is not coincidental — the formula
  structure is principled — but is not yet a first-principles prediction.

---

## Repository Sources

| File | Content |
|------|---------|
| `canonical/interactions/qed.tex` | Canonical QED and α formula |
| `THEORY/axioms/core_assumptions.tex` | BRST assumptions A1–A3 for N_eff |
| `consolidation_project/appendix_ALPHA_one_loop_biquat.tex` | One-loop B_α calculation |
| `consolidation_project/appendix_ALPHA_padic_derivation.tex` | p-adic approach to B_base |
| `consolidation_project/new_alpha_derivations/` | 22+ approaches collected |
| `canonical/bridges/QED_limit_bridge.tex` | Navigation, status, gaps |
| `STATUS_ALPHA.md` | Full α derivation chain and gap list |
| `DERIVATION_INDEX.md` | Row-by-row derivation status |
| `unified_biquaternion_theory/solution_P4_fine_structure_constant/` | First derivation attempt |
| `consolidation_project/scripts/padic/alpha_p_computation.py` | Numerical α from p-adic |

---

*Cross-reference: `research/alpha_program_status.md` (earlier status document).*  
*Cross-reference: `AUDITS/claim_evidence_matrix.md` row `alpha_program`.*  
*Cross-reference: `canonical/bridges/QED_limit_bridge.tex` for full proof-status chain.*
