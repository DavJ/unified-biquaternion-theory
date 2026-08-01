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

# Final Palatini duplicate and theta-fit mask fixes

Exact baseline: `unified-biquaternion-theory-master(11).zip`.

## Changes

1. Remove the misspelled duplicate source:
   `canonical/gr_closure/gap_10t_paladini_torsion_dynamics.tex`.
   Active sources already use the corrected `palatini` spelling.
2. Restore `compute_goodness_of_fit(y_true, y_pred, mask=None)`.
   When `mask` is supplied, metrics are computed only on selected bins.
   Omitting `mask` preserves the previous two-argument behavior and return shape.

No tests, physical claims, equations, or Planck mappings were changed.
