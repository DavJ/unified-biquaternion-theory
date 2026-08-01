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

# Patch notes — self-contained UBT/Theta introduction

**Date:** 2026-07-20  
**Base:** repository version `(17)` with the GAP-10I torsionful local-representer update  
**Claim impact:** none; this is an exposition and publication-readiness patch

## Motivation

The canonical GR manuscript entered directly into the covariant-tetrad
construction. A reader unfamiliar with the repository was not told clearly
what Unified Biquaternion Theory is, what the field `Theta(q,tau)` denotes, or
how the single-field postulate connects to the tetrad and metric.

## Changes

- Expanded the opening of the abstract with a one-sentence definition of UBT
  and its canonical field.
- Added a new first section, **“Introduction: UBT and the role of Theta”**.
- Defined
  `Theta : M x C_tau -> B = C tensor H`, with `tau = t + i psi`.
- Displayed the four-complex/eight-real-component biquaternion decomposition.
- Explained the distinct roles of the commuting complex unit and quaternion
  units, and why the algebra supports Lorentz-spin and left/right actions.
- Clarified that `Theta` is the name of the UBT master field and is not, by
  definition, a Jacobi theta function.
- Explained that “one fundamental field” is an architectural postulate, not a
  claim that all matter, gauge, or gravitational dynamics have already been
  derived.
- Made the gravitational construction explicit as

  `Theta -> D_mu Theta -> E_mu -> (g_mu nu, omega, R)`.

- Delimited the manuscript to the local classical GR bridge and retained the
  honest statement that Einstein dynamics, action-level torsion selection,
  and wider UBT sectors remain open.

## Files

- `papers/UBT_GR_Submission.tex`
- `docs/pdfs/UBT_GR_Submission.pdf`
- `CHANGELOG.md`

## Validation

- `latexmk -pdf -interaction=nonstopmode -halt-on-error` completed successfully.
- The rebuilt manuscript has 16 A4 pages.
- Pages 1–4, including the complete new introduction and the transition to the
  proof-status boxes, were rendered and visually inspected.
- No clipping, overlap, broken glyphs, or new introduction-section overflow was
  found.
- Twenty focused repository tests passed, covering the paired/torsionful GAP-10I
  results, remaining GR subclosures, LaTeX audit, and publication workflow.
- Existing long-path/table overfull warnings later in the manuscript are
  unchanged in character and are unrelated to this introduction patch.
