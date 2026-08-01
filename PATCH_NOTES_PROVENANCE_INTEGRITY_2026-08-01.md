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

# Provenance and integrity hardening — 2026-08-01

This patch closes three repository-hygiene defects found by an independent audit.
It does not modify UBT equations, claim levels, or physical conclusions.

## Changes

1. `tools/forensic_fingerprint/layer2/predictors.py` no longer embeds CODATA
   comparison literals. It loads `alpha_inverse` and `electron_mass_MeV` from
   the provenance-tracked `data/reference_constants/codata_reference.json`.
   The uppercase `DATA/` mirror is kept byte-identical.
2. The alpha hard-code guard now matches both CODATA 2018 and CODATA 2022 style
   values. Existing intentional comparison occurrences are declared as exact
   repository-relative exemptions rather than passing accidentally.
3. Directory exclusions in the guard are evaluated relative to the repository.
   A checkout under a parent named `data` can no longer cause the entire scan to
   be skipped.
4. `SHA256SUMS.txt` is regenerated and protected by a pytest integrity check.
   `tools/regenerate_sha256sums.py` provides the canonical refresh command.

## Validation

```bash
pytest -q tests/test_no_hardcoded_constants.py \
  tests/test_layer2_predictors_placeholder_vs_ubt.py \
  tests/test_sha256sums_integrity.py
python tools/regenerate_sha256sums.py
sha256sum -c SHA256SUMS.txt
```
