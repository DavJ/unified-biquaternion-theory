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

# Apply: final Palatini duplicate + theta-fit mask fixes

Apply from the repository root:

```bash
unzip -o UBT_FINAL_PALATINI_THETA_FIT_FIXES_EXACT_ROOT_OVERLAY_2026-07-18.zip
while IFS= read -r path; do
  [ -n "$path" ] && rm -f -- "$path"
done < DELETE_PATHS_FINAL_PALATINI_THETA_FIT_2026-07-18.txt
sha256sum -c OVERLAY_MANIFEST_FINAL_PALATINI_THETA_FIT_2026-07-18.sha256
```

Targeted regression check:

```bash
pytest -o addopts='' \
  tests/test_release_polish_palatini_refs.py \
  tests/test_theta_fit_tau.py
```
