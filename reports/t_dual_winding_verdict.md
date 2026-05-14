<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# T-dual winding correction verdict

**Task**: `prove_or_reject_T_dual_winding_correction`  
**Priority**: critical  
**Companion file**: `research_tracks/rg_B46/t_dual_winding_derivation.tex`

---

## Final verdict

> **NO-GO**
>
> The claim that a **constant** winding correction is derived from current UBT
> structure does not pass. What is derivable without fitted input is an
> **n-dependent** winding contribution in the compact tower analysis.

---

## Requirement-by-requirement outcome

| Requirement | Outcome | Notes |
|---|---|---|
| Derive `R_psi = 1` from UBT moduli | **CONDITIONAL** | Current derivation fixes shape stationarity (`R_t = R_psi`) under assumptions, but does not fix overall compact scale. |
| Prove T-duality symmetry of compact `psi` sector | **CONDITIONAL** | Spectral Gaussian momentum-winding lattice is duality-invariant under `R_psi ↔ 1/R_psi`, but full-action modular compensation remains open. |
| Compute winding contribution without fixed special integer | **PROVED** | `ΔB_wind(n) = N_eff n /(12 π^2)` from momentum/winding doubling in non-fitted tower expression. |
| Decide constant vs n-dependent | **PROVED** | Derived correction is linear in `n`, therefore not a universal constant. |
| Check effect on coefficient of `n log n` | **NO-GO (constant-shift interpretation)** | Substitution gives an additional `n^2 log n` structure, not a universal shift of a constant coefficient multiplying `n log n`. |

---

## Key derived formulas (no fitting)

- Momentum sector:
  - `B_mom(n) = N_eff n /(12 π^2)`
- Momentum + winding symmetric sector:
  - `B_mom+wind(n) = N_eff n /(6 π^2)`
- Winding increment:
  - `ΔB_wind(n) = N_eff n /(12 π^2)`

These formulas use no fitted target and no fixed special integer input.

---

## Interpretation of the old constant-number usage

A constant numerical increment can only appear after choosing a specific
evaluation level. That is a **post-evaluation bookkeeping value**, not a
universal UBT-derived constant.

So the old usage must be downgraded to:

- **HEURISTIC** as a chosen-level numeric summary,
- **not** a first-principles derived constant correction.

---

## Hard-rule compliance

- No fitting used. ✓
- No forbidden fixed special integer input used. ✓
- No forbidden target coefficient input used. ✓
- Verdict class from mandatory set: **NO-GO**. ✓
