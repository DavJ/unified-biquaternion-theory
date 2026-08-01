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


# ALPHA_DERIVATION_STATUS

## Scope

Task: derive or falsify a first-principles route to

\[
B_\mathrm{eff}\in[46.284,46.298]
\]

for

\[
V_\mathrm{eff}(n)=n^2-B_\mathrm{eff}n\log n,
\qquad
2n=B_\mathrm{eff}(\log n+1).
\]

Hard rule used: no derivation step may use forbidden fitted inputs.

## Best candidate derivation identified

**Best structural candidate:** modular-index bridge

\[
B_\mathrm{eff}\stackrel{?}{=}\frac{\mu(\Gamma_0(N_*))}{3}+\delta_{\mathrm{mod}}
\]

with dynamic \(N_*\) required from UBT action rather than inserted.

Why best: it is the only currently known UBT-adjacent structure naturally in the numerical neighborhood of the required coefficient.

## Is it first-principles right now?

**No.**

Current blockers:
1. No closed derivation of a modular effective potential \(V_{\mathrm{mod}}(N)\) from canonical \(S[\Theta]\) that uniquely selects \(N_*\).
2. Residual correction \(\delta_{\mathrm{mod}}\) not fixed by canonical equations.
3. Heat-kernel/spectral-density routes recover baseline structure and log behavior, but not the missing constant shift \(\Delta B\approx 21.151\) without additional assumptions.

## Exact assumptions used in this work

- Canonical UBT action and Theta/operator definitions are taken from canonical files.
- Baseline one-loop coefficient accepted as \(B_0=8\pi\).
- Winding potential structure \(n^2-Bn\log n\) treated as canonical alpha-route form.
- No fitted insertion was used to *derive* candidate constants in Phases 1–5.

## Exact equations used

- Action: \(S[\Theta]=\int d^4x\sqrt{-g}\,\mathcal L_{\mathrm{UBT}}\).
- Biquaternionic kinetic operator: \(\nabla^\dagger\nabla\).
- One-loop determinant: \(\Gamma_{1\text{-loop}}=\frac12\log\det\mathcal D_n=-\frac12\zeta'_{\mathcal D_n}(0)\).
- Stationary condition: \(2n=B(\log n+1)\).
- Baseline coefficient: \(B_0=2\pi N_{\mathrm{eff}}/3=8\pi\).

## Free parameters / unresolved choices

- Renormalization finite-part prescription in heat-kernel route.
- Spectral occupancy rule needed to make coefficient unique in entropy/spectral route.
- Dynamic modular-level selection \(N_*\) and modular residual \(\delta_{\mathrm{mod}}\).

## Numerical status

- Derived baseline from canonical chain: \(B_0\approx25.132741\).
- Missing shift to target band: \(\Delta B\approx21.151\).
- No non-fitted route in this task produced a closed value in \([46.284,46.298]\).

## Gap-closure assessment

Gap G137-B is **not closed** under hard criteria.

Smallest remaining mathematical gap:

> A unique, first-principles derivation from canonical \(S[\Theta]\) of a constant correction \(\Delta B\) that is scheme-independent and does not require externally fixing attractor index input.

## Final declaration

**PARTIAL:**

"A promising candidate exists, but Gap G137-B remains open because the required constant shift to \(B_\mathrm{eff}\) is not yet derivable uniquely from canonical UBT action data without external attractor-level insertion."
