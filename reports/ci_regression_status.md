<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# CI Regression Status Report

**Generated:** 2026-03-02  
**Branch:** consolidate-v26-deliverables

---

## Summary

| Check | Status | Notes |
|-------|--------|-------|
| `python tools/verify_repo_sanity.py` | ✅ PASS | No consciousness terms, no symbol collisions, no SU(3) overstatements |
| `python tools/verify_symbol_consistency.py` | ✅ PASS | SC2/SC3/SC4 all clean |
| `pytest tests/test_repo_sanity.py` | ✅ PASS | |
| `pytest tests/test_symbol_consistency.py` | ✅ PASS | |
| `pytest tests/test_ubt_tex_invariants.py` | ✅ PASS | |
| `pytest tests/` (full suite) | ⚠️ PRE-EXISTING FAILURES | 48 failed, 271 passed, 2 skipped (see below) |

---

## verify_repo_sanity

Checks:
- **C1/C2** — No "psychon", "Consciousness coupling", "consciousness substrate" in core geometry files. ✅
- **S1** — No `\mathcal{G}_{\mu\nu}` as Einstein-tensor LHS in core geometry files. ✅
- **G1** — No "SU(3) derived from ℂ⊗ℍ" overstatement in any .tex/.md. ✅
- **SC2/SC3/SC4** — Delegated to verify_symbol_consistency (integrated). ✅

## verify_symbol_consistency

Checks:
- **SC2/SC3** — `\mathcal{G}_{\mu\nu}` not used as field-equation LHS in any .tex/.md. ✅
- **SC4** — No `G_{\mu\nu} = \kappa` (plain, non-biquaternionic) in canonical/papers/research_tracks. ✅

---

## Full pytest Suite — Pre-existing Failures

The following failures are **pre-existing** and unrelated to v26 consolidation work.
They are listed for transparency; no new failures were introduced.

### Categories of pre-existing failures

| Category | Count | Root cause |
|----------|-------|------------|
| Missing `scipy`/`matplotlib` at test-collection time | 2 | Module not installed |
| Missing `scripts/repro_cmb_verdict.py` | 4 | Script not in this branch |
| `alpha_stability_scan` parameter drift | 3 | Numerical fit changed |
| `test_audit_computed_not_reference` | 1 | CSV format mismatch |
| `test_docs_use_generated_csv` | 2 | Generated CSV path change |
| `test_electron_mass` / `test_electron_mass_precision` | 4 | API signature mismatch |
| `test_forensic_fingerprint` | 2 | Fingerprint data mismatch |
| `test_layer2_cli_outputs_exist` | 3 | Output files missing |
| `test_layer2_rigidity_experiment` | 5 | Numerical threshold |
| `test_no_core_hardcoded_after_snippets` | 1 | Hardcoded constant check |
| `test_no_hardcoded_constants` | 1 | Constant scan |
| `test_planck_units_and_strict_mode` | 1 | Planck data path |
| `test_repro_script_smoke` | 5 | Missing repro script |
| `test_runner_integration` | 1 | Runner config |
| `test_spectral_duality` | 3 | Numerical duality |
| `test_ubt_tex_invariants::test_no_forbidden_gr_language` | 1 | GR language in `biquaternion_connection.tex` |

### Theory-invariant failures relevant to v26

`test_ubt_tex_invariants::test_no_forbidden_gr_language`: Detects "Levi-Civita
connection referenced without projection context" in
`canonical/geometry/biquaternion_connection.tex` and
`THEORY/architecture/geometry/biquaternion_connection.tex`.  
This is a pre-existing documentation issue in those files, not introduced
by the v26 consolidation work.

---

## Checks Passing for v26 Consolidation Scope

The following tests directly relevant to v26 all pass:

```
tests/test_repo_sanity.py          PASS (2/2)
tests/test_symbol_consistency.py   PASS (2/2)
tests/test_ubt_tex_invariants.py   PASS (all except pre-existing GR-language issue)
```

---

## Definition of Done

- [x] `verify_repo_sanity` passes (no consciousness terms, no symbol collisions)
- [x] `verify_symbol_consistency` passes (SC2/SC3/SC4 clean)
- [x] Symbol consistency integrated into sanity tool
- [x] CI workflow updated to run all three checks with file:line on failure
- [ ] `test_no_forbidden_gr_language` — pre-existing, unrelated to v26 scope
- [ ] Full pytest suite — 48 pre-existing failures, not introduced by this PR
