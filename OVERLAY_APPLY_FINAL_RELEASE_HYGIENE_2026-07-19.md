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

# Apply final release hygiene overlay

Run from the repository root:

```bash
unzip -o UBT_FINAL_RELEASE_HYGIENE_EXACT_ROOT_OVERLAY_2026-07-19.zip

while IFS= read -r path; do
  [ -n "$path" ] && rm -f -- "$path"
done < DELETE_PATHS_FINAL_RELEASE_HYGIENE_2026-07-19.txt

sha256sum -c OVERLAY_MANIFEST_FINAL_RELEASE_HYGIENE_2026-07-19.sha256
```

The explicit deletion step is required because ZIP extraction cannot remove an
already existing file.
