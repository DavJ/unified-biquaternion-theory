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


# Phase 2 — Heat-kernel / zeta route for \(B_\mathrm{eff}\)

## Setup

Use quadratic fluctuation operator around winding background \(\Theta_n\):

\[
\mathcal D_n = -\nabla^\dagger\nabla + \mathcal M_n^2 + \mathcal U_n,
\]

and one-loop effective action

\[
\Gamma_{1\text{-loop}}(n)=\frac12\log\det\mathcal D_n
= -\frac12\zeta'_{\mathcal D_n}(0).
\]

Heat-kernel form:

\[
\Gamma_{1\text{-loop}}(n)= -\frac12\int_0^\infty \frac{ds}{s}\,\mathrm{Tr}\,e^{-s\mathcal D_n}.
\]

## Isolation of \(n\log n\)

Writing \(\mathcal M_n^2\sim n^2\) from winding scale, logarithmic terms can appear as

\[
\Gamma_{1\text{-loop}}(n)\supset -\frac12\,\mathcal C\,n\log n,
\]

only after summing over an \(n\)-dependent set of modes / quanta (4D RG-style accumulation), not from a strict fixed-level single-mode determinant.

Thus a symbolic split is

\[
B_\mathrm{eff}=B_0+\Delta B_{\mathrm{heat}},\qquad B_0=8\pi.
\]

## What can be derived non-circularly here

- \(B_0=8\pi\): available from canonical one-loop counting.
- Existence of logarithmic structure from determinant/zeta: yes.
- A unique constant \(\Delta B_{\mathrm{heat}}\approx 21.151\) from UBT primitives only: **not closed**.

## Failure analysis for closure criterion

The route remains open because candidate \(\Delta B_{\mathrm{heat}}\) terms depend on one or more of:
- renormalization scheme and finite-part prescription,
- unresolved spectral measure normalization,
- higher-loop/mixed curvature-gauge contributions not fixed in canonical alpha chain,
- model-dependent occupancy assumptions converting \(\log n\to n\log n\).

These are currently not uniquely fixed by canonical \(S[\Theta]\) data alone.

## Phase-2 verdict

\[
\boxed{B_\mathrm{eff}=8\pi+\Delta B_{\mathrm{heat}}\ \text{(symbolic only)},\quad
\Delta B_{\mathrm{heat}}\ \text{not uniquely derived}.}
\]

**Status:** route informative but **not closed** for the required numeric target without extra assumptions.
