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

# Apply: CODATA provenance and checksum integrity overlay

Baseline: repository snapshot `(43)` with the already-applied
`GR_STATUS_PDF_HYGIENE_2026-08-01` overlay.

Unpack this archive directly into the repository root, overwriting matching
files, then run:

```bash
bash APPLY_PROVENANCE_INTEGRITY_2026-08-01.sh
```

The script checks the mirrored CODATA JSON files, runs the focused provenance
and checksum tests, and verifies the release-level `SHA256SUMS.txt` anchor.

This overlay changes repository hygiene only. It does not change physical
claims, equations, gap status, or the generated GR submission PDF.
