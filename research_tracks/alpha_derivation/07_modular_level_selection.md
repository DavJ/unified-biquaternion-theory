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


# Phase 7 — Modular-level selection from canonical \(S[\Theta]\)

## Objective

Test the non-circular chain

\[
S[\Theta]\ \Rightarrow\ V_{\mathrm{mod}}(N)\ \Rightarrow\ N_*\ \Rightarrow\ B_{\mathrm{eff}}
=\frac{\mu(\Gamma_0(N_*))}{3}+\delta_{\mathrm{mod}}
\]

without inserting any phenomenological level by hand.

## Step A — From canonical action to modular kinematics

Use canonical biquaternion action with compact phase coordinate \(\psi\sim\psi+2\pi\):

\[
S[\Theta]=\int d^4x\,d\psi\;\mathrm{Re}\,\mathrm{Tr}\!\left[(\nabla^\dagger\Theta)^*(\nabla^\dagger\Theta)-V(\Theta)\right].
\]

For a two-cycle compact sector \((\psi,\chi)\in T^2\), large diffeomorphisms act by
\(\mathrm{SL}(2,\mathbb Z)\) on cycle basis. Hence modular structure is not imposed externally; it is the mapping-class symmetry of the toroidal compact sector.

## Step B — Why \(\Gamma_0(N)\) can appear

If winding/holonomy data selects a congruence class where one cycle is preserved modulo level \(N\), allowed large diffeomorphisms must satisfy

\[
\begin{pmatrix}a&b\\ c&d\end{pmatrix}
\binom{1}{0}\equiv \binom{*}{0}\pmod N
\;\Longrightarrow\; c\equiv 0\pmod N,
\]

which is exactly \(\Gamma_0(N)\subset \mathrm{SL}(2,\mathbb Z)\).

So \(\Gamma_0(N)\) can emerge from boundary-condition preservation, not by assumption.

## Step C — Modular effective potential definition

Define a level-resolved modular free energy

\[
V_{\mathrm{mod}}(N)\equiv -\log Z_N,\qquad
Z_N=\int_{\mathcal F_N}\mathcal D\Theta\;e^{-S_{\mathrm{eff}}[\Theta;\tau]},
\]

with \(\mathcal F_N\) a fundamental region for \(\Gamma_0(N)\).

At this point canonical UBT fixes existence of a level-resolved partition sum, but does not yet fix the sign/normalization structure of finite modular terms that control level preference.

## Step D — Stationary-level test (non-fitted)

A parameter-free scan over canonical proxy families for \(V_{\mathrm{mod}}(N)\) was implemented in:

- `research_tracks/alpha_derivation/tools/modular_level_scan.py`

and report:

- `research_tracks/alpha_derivation/reports/modular_level_selection_status.md`

Result: tested parameter-free families produce non-unique, model-dependent minimizers (some interior, some boundary/window-dependent), not a unique dynamically selected attractor level.

## Step E — Consequence for \(B_{\mathrm{eff}}\)

Because no canonically forced interior \(N_*\) is selected, the expression

\[
\frac{\mu(\Gamma_0(N_*))}{3}
\]

cannot be evaluated as a derived prediction in this phase. Any specific level choice would be external insertion.

## Step F — Residual correction \(\delta_{\mathrm{mod}}\)

\(\delta_{\mathrm{mod}}\) receives eta/cusp/finite-size contributions, but canonical equations do not uniquely determine:

1. finite renormalized modular counterterm prescription,
2. sign of anomaly contribution in the effective potential,
3. measure normalization needed to convert modular degeneracy to a unique additive coefficient.

Therefore \(\delta_{\mathrm{mod}}\) is only symbolic here and not fixed numerically.

## Exact missing theorem (route-failure point)

The route fails at the missing theorem:

> **Theorem T\(_{\mathrm{mod\_select}}\)**: Starting only from canonical \(S[\Theta]\) with compact toroidal boundary conditions, there exists a unique renormalization-scheme-independent modular effective potential \(V_{\mathrm{mod}}(N)\) whose interior stationary point \(N_*\) is unique, and whose finite modular residue \(\delta_{\mathrm{mod}}\) is fixed.

This theorem is currently not proved in canonical UBT.

## Phase-7 verdict

**Rejected as closed first-principles derivation at current state.**

Reason: \(\Gamma_0(N)\) emergence is structurally plausible, but dynamic level selection and residual-fixing theorem are missing; therefore any specific \(N\) would be hand insertion.
