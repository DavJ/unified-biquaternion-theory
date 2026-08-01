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
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Self-Dual Torus Condition Verdict

**Task**: `derive_or_reject_self_dual_torus_condition`  
**Date**: 2026-05-09  
**Companion file**: `research_tracks/alpha_spectral/self_dual_torus_derivation.tex`

---

## Verdict

> **CONDITIONAL**
>
> From the current UBT action sector and spectral one-loop free energy,
> the square torus condition `R_t = R_psi` is derived as a **shape stationary
> point** and shown locally stable, but the action does **not** fix the overall
> scale modulus `sqrt(R_t R_psi)`. Therefore `tau = i` is not unconditionally
> selected without an extra scale-fixing input.

---

## Requirement-by-requirement outcome

| Requirement | Outcome | Notes |
|---|---|---|
| Start from `S[Theta]` | **PROVED** | Uses canonical biquaternionic action and isolates the `(t_E, psi)` kinetic sector. |
| Isolate `t_E` and `psi` kinetic terms | **PROVED** | Quadratic sector written with independent coefficients `K_t`, `K_psi`. |
| Allow independent radii `R_t`, `R_psi` | **PROVED** | Toroidal compactification with no equality assumption. |
| Derive effective free energy `F(R_t, R_psi)` | **PROVED** | One-loop spectral free energy from mode eigenvalues `lambda_{m,n}`. |
| Check stationarity gives `R_t = R_psi` | **CONDITIONAL** | At isotropic normalization (`K_t = K_psi`) and symmetric mode measure: `R_t = R_psi` is stationary. |
| Check stability of square torus | **CONDITIONAL** | Second variation in shape variable is nonnegative and generically positive, giving local shape stability. |
| Determine if UBT fully selects square torus | **NO-GO (current level)** | Scale modulus remains unfixed in this sector, so full dynamical selection is not yet proved. |

---

## Exact obstruction

### O1 — Missing scale-fixing equation

The derived free energy constrains the shape ratio `rho = R_t / R_psi`, but not
an isolated finite value of `s = sqrt(R_t R_psi)` in the kinetic-plus-mass
sector alone. Without an independent equation for `s` (fixed area constraint,
additional potential, renormalisation condition, or boundary principle),
`R_t = R_psi` is not a complete dynamical prediction.

---

## What is proved now

- The derivation starts from `S[Theta]` and does not assume `tau = i`.
- Independent radii are carried explicitly through mode decomposition.
- The one-loop spectral free energy is obtained explicitly.
- For isotropic compact-cycle normalization and symmetric spectrum,
  `rho = 1` (`R_t = R_psi`) is a stationary point.
- The square point is locally stable in the shape mode.

## What remains conditional

- Whether UBT field equations enforce isotropic compact-cycle normalization in
  the relevant sector.
- Whether additional UBT terms fix the scale modulus and thereby promote
  shape stability to full radius selection.

---

## Hard-rule compliance

- No fitting used. ✓
- No assumption `tau=i` used. ✓
- No use of `alpha`, `p=137`, `eta(i)`, or `B_required`. ✓
- Verdict class from mandatory set: **CONDITIONAL**. ✓
