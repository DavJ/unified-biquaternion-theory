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

# UBT differential patch — GR submission: prior-art honesty pass

**Patch date:** 2026-07-26
**Base commit marker:** `cb1ca2a6a5cc2cf09e28f6acb853a081481de6ef`

## Changes

1. "Relation to standard tetrad geometry" replaced by a three-part
   "Relation to prior work": (a) standard machinery not claimed as new
   (Cartan, Utiyama-Kibble, Ashtekar); (b) convergent programmes
   (Einstein 1945, Moffat NGT, Chamseddine, Hestenes STA,
   Lasenby-Doran-Gull GTG, teleparallel gravity, Ogievetskii-Polubarinov,
   de Haas 2014 and the 2025 gravitational-rotor construction); (c) an
   explicit delimitation of what IS claimed as new, restricted to the
   machine-verified theorems, with an explicit statement of how the
   metric mechanism differs from the rotor adjoint action of de Haas 2025
   and an explicit no-priority-claim sentence.
2. Bibliography extended from 5 to 17 references.
3. The torsion-dynamics section now includes a paragraph on the
   linearized D-composite status (symbol identity, off-resonance
   flatness, six-dimensional exponential sector, open questions), so the
   delimitation references only results the paper actually presents.
4. Ledger table extended with the three D-composite rows; GAP-10T-DYN
   remaining-work wording updated.

## Rationale

The previous five-reference related-work section was the paper's weakest
point against referee scrutiny; the November 2025 de Haas rotor paper is
the closest active prior art and must be engaged, not ignored. All new
claims remain restricted to verified theorems.

## Validation

- pdflatex (two passes): zero errors; PDF regenerated in docs/pdfs/.
