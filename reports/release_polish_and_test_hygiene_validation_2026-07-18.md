# Validation report: release polish and test hygiene

Baseline: `unified-biquaternion-theory-master (2)(3).zip`
Date: 2026-07-18

## Scope

The overlay cumulatively includes the approved Palatini/reference polish and the
following two test-hygiene fixes only:

- pytest-compatible class-scoped Minkowski tetrad fixture;
- restored no-fitting wording in the two unimplemented Planck mapping stubs.

## Patch-specific verification

- 20/20 selected regression tests passed.
- The six Minkowski tetrad tests passed with
  `PytestRemovedIn10Warning` promoted to an error.
- Both TBD Planck stubs retain `NotImplementedError` and the exact phrase
  `NO additional tunable parameters`.
- 4/4 exact GR verifier scripts passed.

## LaTeX and PDF verification

Five affected standalone roots compiled successfully with strict audit:

1. `papers/UBT_GR_Submission.tex`
2. `canonical/gr_closure/gap_10t_palatini_torsion_dynamics.tex`
3. `canonical/gr_closure/gap_10i_augmented_holonomy.tex`
4. `canonical/gr_closure/gap_10l_psi_symmetry_propagation.tex`
5. `canonical/gr_closure/gap_10omega_connection_elimination.tex`

Result: 5 success, 0 failed, 0 timeout.

The five PDFs were regenerated, rendered, and visually inspected. No clipping,
overlap, malformed glyphs, or broken references were observed.

## Full-suite accounting

A full-suite run in the supplied container did not become globally green after
these two fixes. It reproduces older, unrelated failures in data-provenance,
legacy forensic/Planck loader shims, and additional Planck utility expectations;
a monolithic run also exceeds the execution window. These failures are outside
the requested two-change scope and were not modified or hidden. The cumulative
overlay therefore reports the patch-specific suite separately and makes no claim
that every historical repository test is green in this container.

## Intentional deletions

- `canonical/gr_closure/gap_10t_paladini_torsion_dynamics.tex`
- `docs/pdfs/gap_10t_paladini_torsion_dynamics.pdf`
