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

# GR covariant-profile and central-complex-metric overlay

Apply this ZIP at repository root.  Paths are repository-relative and the ZIP
contains no wrapper directory.

This is cumulative against `unified-biquaternion-theory-master (3)(2).zip`; it
includes the preceding free-fiber hardening changes.

## What it adds

- proves the sharp-symmetrised product is central for arbitrary
  biquaternions, with a generally complex coefficient
  `gamma_mu_nu = g_mu_nu + i h_mu_nu`;
- proves that quaternion-vector information belongs to the antisymmetric
  bivector `Sigma_mu_nu`, not to a noncentral symmetric metric;
- replaces the fixed ambient profile frame by a flat, pairing-compatible
  ambient connection `mathbb D_mu`;
- derives the curved Levi-Civita connection as the tangential projection of
  that flat ambient transport;
- shows free rank and the local vacuum closure are invariant under ambient
  profile-frame changes and do not reintroduce the concurrent-vector no-go;
- keeps the branch noncanonical: the ambient derivative must still be
  distinguished from the old pointwise spin-lift `D_mu`, and action origin and
  profile-mode control remain open.

## Verification

```bash
python tools/verify_covariant_profile_geometry.py
pytest -q \
  tests/test_covariant_profile_geometry.py \
  tests/test_covariant_tetrad_geometry.py \
  tests/test_free_fiber_completion.py \
  tests/test_gap_10i_integrability.py \
  tests/test_gap_10i_paired_connection.py \
  tests/test_gap_10i_torsionful_local_representer.py \
  tests/test_gap_10omega_connection.py \
  tests/test_gr_closure_regressions.py \
  tests/test_gr_endgame_completion.py \
  tests/test_gr_minimal_one_connection_no_go.py \
  tests/test_gr_status_consistency.py \
  tests/test_gradient_composite_flatness.py \
  tests/test_metric_lock.py \
  tests/test_pure_ubt_fiber_closure.py \
  tests/test_remaining_gr_subclosures.py \
  tests/test_two_mode_hermitian_metric_correction.py
```

Expected result for the listed suite: all tests pass, with one pre-existing
skip.

The two TeX notes compile to the PDFs included under `docs/pdfs/`.
