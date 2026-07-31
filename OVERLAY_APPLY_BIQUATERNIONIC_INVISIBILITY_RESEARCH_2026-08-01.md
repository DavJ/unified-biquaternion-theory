# Apply note — biquaternionic invisibility research track

This overlay is repository-root relative and records a speculative research
program. It does not modify Axiom C or promote an invisibility claim to
canonical status.

## Changes

- restores explicit terminology for the full ordered biquaternionic geometric
  tensor while preserving the central GR metric definition;
- creates a current invisibility/null-geometry research program;
- rebases historical ST-1--ST-5 documents against the July 2026 architecture;
- adds exact algebra checks for a metric-null but biquaternionically active
  witness and for the determinant of a purely imaginary 4D metric;
- updates the claim matrix, history, map, and speculative index.

## Verify

```bash
python tools/verify_biquaternionic_metric_nullity.py
pytest -q tests/test_biquaternionic_metric_nullity.py
```
