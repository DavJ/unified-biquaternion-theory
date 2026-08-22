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
passes; human semantic-equivalence review is required before merge.

<!-- BILINGUAL-UNIT: audit.result -->
## Result

The central metric/rank, connection/contortion, local integrability,
split-jet, principal-symbol, and conditional induced-Einstein-coefficient
checks pass within their recorded assumptions. The legacy promotion of a
spatial Schwarzschild identity to a complete canonical single-Theta solution
fails. The authoritative status remains `GAP-U2Theta: OPEN`.

The invalid promotion has been removed from the published canonical Pages
set and superseded by a machine-readable status record and a paired paper
correction. The historical source is retained for traceability and requires a
separate bilingual archival migration before it can be rewritten or removed.

<!-- BILINGUAL-UNIT: audit.fixes -->
## Fixes

- Added an independent SageMath audit of exact metric rank, exact
  contortion-to-torsion rank, exact Schwarzschild counter-witnesses, and the
  heat-trace coefficient.
- Repaired the heat-trace verifier by mapping the infinite integration range
  to a stable finite interval.
- Bounded the legacy NumPy verifier to the spatial identity it actually
  checks and added a canonical Lorentz-slice guard.
- Added regression tests and a machine-readable verification ledger.
- Added paired English/Czech correction documents with identical equations,
  claim statuses, and limitations.

<!-- BILINGUAL-UNIT: audit.assumptions -->
## Assumptions and limitations

The computer-algebra checks establish only the encoded finite-dimensional
identities and conditional quadrature. They do not prove action selection,
PDE well-posedness, global continuation, a preferred imaginary-time section,
or the physical truth of UBT. The induced Einstein coefficient remains
conditional on the stated Laplace-type Hessian, measure, cutoff, mode count,
and regulator assumptions.

<!-- BILINGUAL-UNIT: audit.remaining -->
## Remaining gaps

- `GAP-U2Theta: OPEN`: canonical on-shell generation of the complete
  Schwarzschild tetrad and lapse.
- `LEAN-PENDING`: no current Lean source formalizes the audited GR claims.
- Human semantic-equivalence review of the English/Czech pair is required
  before merge.
