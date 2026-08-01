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

# Apply the Gauge/QM Honest-Status Overlay

This is a differential root overlay for the UBT repository after the
`v10.3.0 GR subclosures` and reviewed `History of UBT` overlays.

From the repository root:

```bash
unzip -o UBT_GAUGE_QM_HONEST_STATUS_ROOT_OVERLAY_2026-07-17.zip
pytest -q tests/test_claims_consistency.py \
  tests/test_involutions_triplet_space.py \
  tests/test_architecture_freeze_and_latex_workflow.py \
  tests/test_remaining_gr_subclosures.py
```

Compile the two standalone touched documents:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  canonical/qm_emergence/step7_born_rule.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  docs/notes/symmetry_from_automorphisms.tex
```

`canonical/su3_derivation/su3_from_involutions.tex` is an appendix fragment and
must be compiled through its parent or a temporary wrapper providing `amsmath`,
`amsthm`, `hyperref`, and `tcolorbox`.

No files are deleted. The overlay changes gauge/QM claim status only; it does
not alter the frozen covariant-tetrad GR architecture.
