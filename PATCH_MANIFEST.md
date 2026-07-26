# Patch manifest — canonical relation generalized-Dirac consolidation

Root-relative overlay based on repository version `(34)`.

## Active files added or changed

- `canonical/geometry/biquaternion_dirac_lift.tex`
- `canonical/THEORY/architecture/geometry/biquaternion_dirac_lift.tex`
- `canonical/geometry/biquaternion_tetrad.tex`
- `canonical/THEORY/architecture/geometry/biquaternion_tetrad.tex`
- `canonical/UBT_canonical_main.tex`
- `canonical/bridges/GR_chain_bridge.tex`
- `research_tracks/canonical_relation_generalized_dirac/README.md`
- `research_tracks/canonical_relation_generalized_dirac/PROOF_STATUS.md`
- `research_tracks/canonical_relation_generalized_dirac/canonical_relation_dirac_proof.tex`
- `tools/verify_canonical_relation_dirac_lift.py`
- `tests/test_canonical_relation_dirac_lift.py`
- `STATUS_OF_UBT.md`
- `WHAT_IS_PROVED.md`
- `ROADMAP.md`
- `CHANGELOG.md`
- `reviews/dual_sector_cl5_prior_art.md`
- `PATCH_NOTES_CANONICAL_RELATION_GENERALIZED_DIRAC_2026-07-27.md`

## Historical moves

The former spinor-current tetrad branch was moved to:

- `research_tracks/history/legacy_spinor_current_tetrad_2026-07-26/`

The path `research_tracks/dual_sector_clifford5/README.md` now redirects to the
active and historical locations.

## Validation

```bash
python tools/verify_canonical_relation_dirac_lift.py
pytest -q tests/test_canonical_relation_dirac_lift.py
```
