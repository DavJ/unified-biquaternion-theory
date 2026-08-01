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

# Patch notes — active GitHub Actions path repair

**Date:** 2026-07-26  
**Scope:** repository/CI hygiene only; no physics equations, claims, or numerical results changed.

## Problem

Three GitHub Actions workflows still referenced package trees removed from the
active repository layout:

- `ubt_with_chronofactor/...`;
- lowercase `archive/consolidation_project/...`.

The alpha workflow would fail because its pytest targets did not exist. The
forensic and Planck path filters could also fail to trigger when active code was
changed.

## Changes

- Repointed alpha CI to active tests under `tests/` and active alpha reproduction
  code under `experiments/alpha_core_repro/`.
- Repointed forensic triggers and documentation to `tools/forensic_fingerprint/`
  and `experiments/forensic_fingerprint/`.
- Repointed Planck triggers to `tools/planck_validation/` and
  `experiments/planck.py`.
- Added `tests/test_workflow_active_paths.py` to reject future stale active-tree
  references.

Historical content under `ARCHIVE/` was not modified.

## Validation

- active workflow regression tests pass;
- the workflow pytest command sets were executed locally and pass;
- the existing 216-test GEM/Layer2/SU(3)/forensic/Planck/manifest target set
  remains green;
- ZIP integrity and root-level layout are checked separately for release.
