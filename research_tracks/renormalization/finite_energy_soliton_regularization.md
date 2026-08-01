<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Finite-Energy Soliton Regularization (Research Track)

Status label used in code:

> **regularized finite-energy soliton model; full RG derivation open.**

## Implemented formula

In `src/ubt/solitons/regularization.py`:

- energy density scaffold

\[
\rho(r) = \frac{A}{r_\text{eff}(r)^2}
\]

with configurable effective radius:

- hard cutoff: \(r_\text{eff}=\max(r,\epsilon)\)
- lorentzian: \(r_\text{eff}=\sqrt{r^2+\epsilon^2}\)
- gaussian-inspired: \(r_\text{eff}=\sqrt{r^2+2\epsilon^2}\)

and total energy integrated numerically:

\[
E(R) = 4\pi\int_0^R r^2 \rho(r)\,dr
\]

## What diverged before

Without regularization, direct terms proportional to \(1/r^2\) are singular at \(r=0\). This causes unstable or divergent behavior in naive pointwise evaluation and motivates controlled cutoff handling.

## How cutoff is introduced

A positive `cutoff_length` is exposed in `SolitonRegularizationConfig` and applied before division by radius.
No branch in the scaffold divides directly by raw `r` at the origin.

## Physical vs numerical interpretation of cutoff

Current status: **numerical scaffold with optional physical scale interpretation**.

- default cutoff uses Planck length as an optional scale anchor,
- the code does not claim this identifies the true physical regulator,
- interpretation remains model-dependent until derivation from UBT action is closed.

## Open problem

Derive renormalization-group flow and regulator/scheme dependence from the UBT action rather than imposing a numerical cutoff prescription.
