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

# Canonical and GR derivation audit

<!-- BILINGUAL-UNIT: audit.scope -->
## Scope

This patch audits the theorem-critical algebra used by the canonical layer and
`papers/UBT_GR_Submission.tex`. The source language of this paired note and the
paired paper correction is English. Automated structural and status parity
must pass; human semantic-equivalence review is required before merge.

<!-- BILINGUAL-UNIT: audit.result -->
## Result

The central metric/rank, connection/contortion, local integrability,
split-jet, principal-symbol, and conditional induced-Einstein-coefficient
checks pass within their recorded assumptions. The legacy promotion of a
spatial Schwarzschild identity to a complete canonical single-Theta solution
fails and remains `SUPERSEDED_INVALID_DERIVATION`.

A separate composition of the already established split-jet right inverse,
nonpropagating auxiliary action, and conditional Einstein-Hilbert infrared
effective branch closes the scoped recovery question as
`GR-RECOVERY: CLOSED CONDITIONALLY`. Consequently
`GAP-U2Theta: CLOSED CONDITIONALLY FOR GR RECOVERY` and
`GAP-B-MASTER: CLOSED CONDITIONALLY FOR EFFECTIVE GR PERTURBATIONS` without
restoring the invalid historical ansatz.

The invalid promotion has been removed from the published canonical Pages set
and superseded by a machine-readable status record and paired paper correction.
The historical source is retained for traceability.

<!-- BILINGUAL-UNIT: audit.fixes -->
## Fixes

- Added an independent SageMath audit of exact metric rank, exact
  contortion-to-torsion rank, exact Schwarzschild counter-witnesses, and the
  heat-trace coefficient.
- Repaired the heat-trace verifier by mapping the infinite integration range
  to a stable finite interval.
- Bounded the legacy NumPy verifier to the spatial identity it actually checks
  and added a canonical Lorentz-slice guard.
- Added regression tests and a machine-readable verification ledger.
- Added paired English/Czech correction documents with identical equations,
  claim statuses, and limitations.
- Added a paired GR-recovery completion theorem and a scoped recovery ledger.

<!-- BILINGUAL-UNIT: audit.assumptions -->
## Assumptions and limitations

The computer-algebra checks establish only the encoded finite-dimensional
identities and conditional quadrature. Conditional GR recovery assumes a
finite positive renormalized Einstein-Hilbert coefficient, the proved local
split-jet construction on regular non-null patches, a Levi-Civita physical
connection, and suppression of higher-derivative terms at the infrared order
claimed. The result does not derive the complete microscopic Theta-only metric
selector, the constrained quantum measure, a first-principles numerical value
of Newton's constant, UV psi stability, or global/null-patch continuation.

<!-- BILINGUAL-UNIT: audit.remaining -->
## Remaining fundamental questions

- `UBT-FUND-GR-ACTION: OPEN`: derive the complete effective selector from a
  finalized microscopic Theta-only action.
- `UBT-UV-G-PREDICTION: OPEN`: derive the composite Hessian, mode count,
  coupling, cutoff identification, and constrained measure needed to predict
  Newton's constant rather than recover GR with a renormalized coefficient.
- `UBT-FUND-GLOBAL: OPEN`: prove global and null/horizon-patch continuation.
- `LEAN-PENDING`: no current Lean source formalizes the audited GR claims.
- Human semantic-equivalence review of the English/Czech pair is required
  before merge.
