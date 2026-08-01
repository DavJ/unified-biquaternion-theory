<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# UBT GR Endgame Overlay — 26 July 2026

Apply this ZIP directly at the root of `unified-biquaternion-theory` version
(29).  Paths are root-relative; the archive contains no wrapper directory.

## Result

- `GAP-10T-JET-AUX: CLOSED [L1]` — the split-jet action is algebraic,
  nonpropagating, and has zero on-shell backreaction on non-null patches.
- `GAP-10T-JET-CONSTRAINT-SELECTION: CLOSED AS NO-GO [L1]` — the pure
  surjective constraint cannot choose a tetrad from Theta.
- `GAP-10D-UNDERDETERMINATION: CLOSED AS NO-GO [L1]` — the current kinematic
  axioms cannot determine the Newton coefficient.
- `GAP-10D-A2-FORM` and `GAP-10D-SPECTRAL-IR: CLOSED CONDITIONALLY [L1]` — a
  specified gauge-fixed Hessian gives the exact proper-time/KK induced
  Einstein coefficient and a complete local Einstein--Lambda IR branch.

The recovery of GR as a renormalized effective theory is separated from the
stronger open goal of predicting the numerical value of Newton's constant
from the fundamental constrained UBT measure.

## Validation

- exact verifier: `tools/verify_gr_endgame_completion.py`;
- targeted GR/claim/publication tests pass;
- all four affected PDF roots compile and were visually rendered;
- the optional full property-test module still requires `hypothesis` in the
  execution environment.

See `PATCH_NOTES_GR_ENDGAME_2026-07-26.md` for the proof boundary.
