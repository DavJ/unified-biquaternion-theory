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

# Apply the GR Theta-Hessian principal-symbol overlay

From the repository root:

```bash
unzip -o UBT_GR_THETA_HESSIAN_PRINCIPAL_SYMBOL_2026-08-01.zip
bash APPLY_GR_THETA_HESSIAN_PRINCIPAL_SYMBOL_2026-08-01.sh
```

The script is idempotent. It verifies the overlay manifest, source provenance,
the new symbolic theorem, existing GR regressions, curated PDF provenance,
the current provenance inventory, and the repository checksum anchor.

No Tier-A file is modified by this overlay.
