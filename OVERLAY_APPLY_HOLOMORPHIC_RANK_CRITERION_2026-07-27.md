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

# Apply instructions

Extract the overlay at the repository root, preserving paths and replacing
existing files. Then delete every path listed in
`DELETE_PATHS_HOLOMORPHIC_RANK_CRITERION_2026-07-27.txt`.

Validation commands:

```bash
python tools/verify_canonical_relation_dirac_lift.py
pytest -q tests/test_canonical_relation_dirac_lift.py \
          tests/test_canonical_dirac_track_hygiene.py
```

The historical spinor-current implementation must remain only under
`research_tracks/history/legacy_spinor_current_tetrad_2026-07-26/`.
