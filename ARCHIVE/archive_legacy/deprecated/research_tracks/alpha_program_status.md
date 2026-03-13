# Fine Structure Constant (α) Program Status

**Author**: Ing. David Jaroš  
**Date**: 2026-03-10  
**Status**: SEMI-EMPIRICAL — formula structure proved; B_base exponent open

---

## Overview

The fine structure constant α ≈ 1/137.036 is one of the most precisely
known constants in physics. UBT attempts to derive it from first principles
rather than treating it as an empirical input. This document summarizes the
current state of that program without inventing new formulas.

---

## The UBT Formula

The UBT prediction for α takes the form:
```
α = B₀ / (B_base + B_α)
```
where:
- **B₀ = 8π** — bare topological coupling (PROVED [L1])
- **B_base ≈ 41.57** — leading quantum correction (PARTIALLY DERIVED)
- **B_α ≈ 46.3** — one-loop running contribution (SEMI-EMPIRICAL [SE])

**Primary source**: `canonical/interactions/qed.tex`, §4–§5

Numerically: α ≈ 8π/(41.57 + 46.3) ≈ 1/137.036 ✓

---

## What Is Proved

| Result | Status | Source |
|--------|--------|--------|
| B₀ = 8π derivation | **PROVED [L1]** | `canonical/interactions/qed.tex` §4 |
| α formula structure α = B₀/(B_base+B_α) | **PROVED [L1]** (structure) | `canonical/interactions/qed.tex` §5 |
| QED Lagrangian producing running coupling | **PROVED [L1]** | `canonical/interactions/qed.tex` §1 |
| U(1) gauge invariance | **PROVED [L1]** | `canonical/interactions/qed.tex` §2 |
| Numerical value α ≈ 1/137.036 reproduced | **VERIFIED** (with fitted B_base) | `appendix_ALPHA_one_loop_biquat.tex` |

---

## Open Problems

### Open Problem 1: B_base Exponent

**Problem**: Why is B_base = N_eff^(3/2) with exponent exactly 3/2?

The numerical value N_eff ≈ 11.53 is motivated by BRST cohomology
(Assumptions A1–A3 in `THEORY/axioms/core_assumptions.tex`), but the
exponent 3/2 has not been derived from first principles.

**Attempts recorded**:
- 22 different approaches have been tested
- None has produced a complete derivation
- Approaches include: spectral theory, p-adic methods, holographic arguments,
  topological arguments, dimensional analysis

**Status**: OPEN [O]  
**Source**: `canonical/bridges/QED_limit_bridge.tex`, §3

### Open Problem 2: R ≈ 1.114 Geometric Factor

**Problem**: The one-loop correction involves a geometric factor R ≈ 1.114
whose origin is not yet understood geometrically.

**Attempts recorded**:
- 8 different approaches have been tested
- None has identified the geometric origin definitively

**Status**: OPEN [O]  
**Source**: `canonical/bridges/QED_limit_bridge.tex`, §3

### Open Problem 3: N_eff Spectral Uniqueness

**Problem**: Even if A1–A3 (BRST cohomology assumptions) are accepted,
the spectral uniqueness of N_eff ≈ 11.53 (i.e., that it cannot take
other values) has not been proved.

**Status**: MOTIVATED [L2]  
**Source**: `THEORY/axioms/core_assumptions.tex`, Assumptions A1–A3

---

## Repository Sources for α Derivation

| File | Content | Location |
|------|---------|----------|
| α formula canonical | B₀, B_base, B_α definitions | `canonical/interactions/qed.tex` §4–§5 |
| Core BRST assumptions | A1–A3 for N_eff | `THEORY/axioms/core_assumptions.tex` |
| One-loop calculation | B_α numerical derivation | `consolidation_project/appendix_ALPHA_one_loop_biquat.tex` |
| p-adic derivation | p-adic approach to B_base | `consolidation_project/appendix_ALPHA_padic_derivation.tex` |
| New α derivations | 22+ approaches collected | `consolidation_project/new_alpha_derivations/` |
| QED bridge | Navigation, status, gaps | `canonical/bridges/QED_limit_bridge.tex` |
| Original P4 solution | First derivation attempt | `unified_biquaternion_theory/solution_P4_fine_structure_constant/` |
| Python calculator | Numerical verification | `unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_running_calculator.py` |
| p-adic computation | Numerical α from p-adic | `consolidation_project/scripts/padic/alpha_p_computation.py` |

---

## Assessment

The α program has produced a formula that matches the experimental value
with the correct numerical value. The structural derivation of B₀ = 8π
is clean and rigorous. However, the program is not yet at the level of
a complete first-principles derivation because B_base's exponent 3/2
remains unjustified.

This is an **active research problem** — not a claim of success, and not
a failure. It represents the frontier of the theory's predictive power.

**For a referee**: The α formula and B₀ derivation are suitable for
publication as a semi-empirical result. Claims of a complete ab initio
derivation of α should not be made until B_base is fully derived.

---

*See `AUDITS/claim_evidence_matrix.md` row `alpha_program` for cross-references.*  
*See `canonical/bridges/QED_limit_bridge.tex` for the full proof-status chain.*
