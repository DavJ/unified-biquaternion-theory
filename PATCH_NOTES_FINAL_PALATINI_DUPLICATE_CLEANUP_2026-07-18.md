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

# Final Palatini duplicate cleanup

Scope: repository hygiene only.

- Removes the misspelled duplicate
  `canonical/gr_closure/gap_10t_paladini_torsion_dynamics.tex`.
- Removes the matching obsolete PDF if present.
- Keeps the canonical correctly named source
  `canonical/gr_closure/gap_10t_palatini_torsion_dynamics.tex`.
- Makes no changes to equations, claim levels, tests, or physics.

The uploaded baseline already contains the restored
`compute_goodness_of_fit(..., mask=None)` behavior; no further theta-fit source
change is included here.
