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

# Validation report: final Palatini duplicate and theta-fit mask fixes

## Targeted validation

Command:

```bash
pytest -o addopts='' \
  tests/test_release_polish_palatini_refs.py \
  tests/test_theta_fit_tau.py
```

Result:

```text
12 passed, 1 skipped in 0.27s
```

Additional direct check confirmed that:

- two-argument `compute_goodness_of_fit` retains the prior `rmse`/`r2` result shape;
- a supplied Boolean mask excludes unselected bins and returns residual statistics;
- the misspelled active TeX source is absent after applying the deletion list.

## Full-suite note

A clean-container full-suite run was attempted after installing the repository-declared
`hypothesis` development dependency. This exact uploaded snapshot still reproduced
pre-existing failures unrelated to these two edits, including data-provenance validation,
a forensic-fingerprint import-path collection error, and two Planck aggregate-prediction
tests. A monolithic non-fail-fast run also exceeded the execution window. Therefore this
report does not claim a fully green historical suite in this environment.
