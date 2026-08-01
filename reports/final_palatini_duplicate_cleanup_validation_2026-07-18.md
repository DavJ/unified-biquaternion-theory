<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Validation report: final Palatini duplicate cleanup

Baseline inspection found both the misspelled and corrected Palatini source
files. Active references already point to the corrected spelling. The old name
appears only in deletion instructions, patch/validation history, and the
regression test that asserts its absence.

After applying the deletion list on a fresh copy:

- misspelled TeX source: absent;
- misspelled PDF: absent;
- corrected TeX source: present;
- corrected PDF: present;
- `tests/test_release_polish_palatini_refs.py`: passed;
- `tests/test_theta_fit_tau.py`: passed with its expected skip.

Focused result: `12 passed, 1 skipped`.

A full-suite probe still encounters the pre-existing unrelated failure
`tests/test_data_provenance.py::test_validate_manifest_from_different_cwd`.
This cleanup does not alter that subsystem.
