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

# Apply: final Palatini duplicate cleanup

This is a root overlay for the current UBT repository snapshot. It adds no
mathematical source changes. It only carries the explicit deletion list needed
to remove the misspelled historical duplicate that an ordinary ZIP overwrite
cannot delete.

From the repository root:

```bash
unzip -o UBT_FINAL_PALATINI_DUPLICATE_CLEANUP_EXACT_ROOT_OVERLAY_2026-07-18.zip
while IFS= read -r path; do
  [ -n "$path" ] && rm -f -- "$path"
done < DELETE_PATHS_FINAL_PALATINI_DUPLICATE_CLEANUP_2026-07-18.txt

pytest -q \
  tests/test_release_polish_palatini_refs.py \
  tests/test_theta_fit_tau.py
```
