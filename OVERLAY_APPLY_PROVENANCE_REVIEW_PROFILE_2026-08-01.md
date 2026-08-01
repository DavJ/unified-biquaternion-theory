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

# Apply: orthogonal provenance review profiles

From the repository root:

```bash
unzip -o ~/Downloads/UBT_PROVENANCE_REVIEW_PROFILE_2026-08-01.zip
bash APPLY_PROVENANCE_REVIEW_PROFILE_2026-08-01.sh
```

The apply script verifies the static overlay, checks ordinary provenance markers,
regenerates the inventory, verifies the independent review registry, and checks
the main integrity anchor.  Then run the full audit:

```bash
bash VERIFY_PROVENANCE_REVIEW_PROFILE_2026-08-01.sh
```

The verification script runs the focused tests, checks all curated PDFs, and
rechecks the main checksum anchor.

The overlay does not replace A/B/C/D and does not alter the signed Tier-A set.
