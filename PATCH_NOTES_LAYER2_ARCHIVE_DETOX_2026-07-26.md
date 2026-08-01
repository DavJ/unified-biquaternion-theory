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

# Layer2 archive-detox and test-visibility repair

**Date:** 2026-07-26  
**Scope:** repository hygiene only; no canonical physics claim changes

## Problem found

The active files

- `tools/forensic_fingerprint/tools/layer2_rigidity_experiment.py`
- `tools/forensic_fingerprint/tools/layer2_fingerprint_sweep_v2.py`

were still runtime shims into `ARCHIVE/archive_legacy/.../ubt_with_chronofactor`.
This was hidden because `tests/conftest.py` unconditionally skipped every test
whose node id contained `layer2` or `predictor`, regardless of whether an
optional dependency was actually missing.

A separate helper in
`experiments/constants_derivation/derive_fine_structure.py` also attempted the
removed `ubt_with_chronofactor.alpha_core_repro` namespace before silently
falling back.

## Repair

1. Restored self-contained active Layer2 configuration, metric, reporting, and
   sweep helpers under `tools/forensic_fingerprint/layer2/`.
2. Replaced both active CLI shims with active-tree implementations.
3. Made the `ubt` Layer2 mapping fail explicitly as **not implemented**; the
   placeholder mapping remains available only for framework tests.
4. Rewired the alpha helper to `experiments/alpha_core_repro`.
5. Removed the unconditional Layer2/predictor skip hook.
6. Made CLI test working directories repository-relative.
7. Repacked the delivered ZIP with repository files at archive root, without an
   extra `unified-biquaternion-theory-master/` directory.

## Validation

- Four formerly hidden Layer2 test modules: **21 passed**.
- Broader targeted suite covering Layer2, GEM compact modes, forensic
  fingerprint, Planck validation, manifests, alpha/electron pipelines, claim
  consistency, and repository sanity: **154 passed, 1 skipped**.
- `python -m compileall` on changed Python areas: **PASS**.
- Direct `--help` smoke tests for both Layer2 CLIs: **PASS**.
- `python tools/verify_gem_compact_modes.py`: **PASS**, with its existing
  explicit non-claims preserved.
- `experiments/constants_derivation/derive_fine_structure.py`: **PASS** using
  the active alpha package.

## Boundaries

- No GAP status, UBT equation, SU(3) result, GEM claim, or GR-endgame theorem was
  changed.
- The full suite still cannot collect `tests/test_physics_properties.py` in this
  environment because the optional `hypothesis` package is not installed.
- The newest exact symbolic GR tests are computationally heavy in this
  environment and were not re-certified as part of this hygiene-only patch.
