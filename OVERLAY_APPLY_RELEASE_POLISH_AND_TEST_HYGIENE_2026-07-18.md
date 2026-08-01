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

# Apply: release polish and test hygiene overlay

Apply from the repository root:

```bash
unzip -o UBT_RELEASE_POLISH_AND_TEST_HYGIENE_EXACT_ROOT_OVERLAY_2026-07-18.zip

while IFS= read -r path; do
  [ -n "$path" ] && rm -f -- "$path"
done < DELETE_PATHS_RELEASE_POLISH_AND_TEST_HYGIENE_2026-07-18.txt
```

Verify the overlay payload:

```bash
sha256sum -c OVERLAY_MANIFEST_RELEASE_POLISH_AND_TEST_HYGIENE_2026-07-18.sha256
```

Run the patch-specific regression set:

```bash
pytest -q \
  tests/test_release_polish_palatini_refs.py \
  tests/test_architecture_freeze_and_latex_workflow.py \
  tests/test_remaining_gr_subclosures.py \
  tests/test_biquaternion.py::TestBiquaternionTetradMinkowski \
  tests/test_planck_validation_mapping.py::TestMappingTBD::test_tbd_error_messages_mention_no_fitting \
  -W error::pytest.PytestRemovedIn10Warning
```
