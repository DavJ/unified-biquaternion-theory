# GR subclosures validation — 2026-07-16

This report records the validation gate for the frozen covariant-tetrad
v10.3.0 candidate. It does not upgrade conditional results to unconditional
UBT derivations.

## Exact symbolic verifiers

All passed:

- `tools/verify_covariant_tetrad_rank.py`
  - central anticommutator on the Lorentz slice;
  - tetrad-to-metric rank 10, kernel 6;
  - explicit reachability of every symmetric metric variation.
- `tools/verify_gap_10omega_connection.py`
  - Minkowski Cartesian connection;
  - nonzero flat polar-frame connection;
  - torsion-free connection uniqueness rank 24/24;
  - exact contorsion reconstruction.
- `tools/verify_gap_10i_integrability.py`
  - affine Minkowski representer;
  - one-sided invertible flatness obstruction;
  - exact two-sided curvature identity.
- `tools/verify_remaining_gr_subclosures.py`
  - Cartan torsion map rank 24/24;
  - intrinsic Lorentz-slice involution;
  - psi Lorentz-gauge metric invariance;
  - augmented-curvature/compatibility identity.

## Targeted regression tests

The targeted architecture, workflow, claims, status, metric, symbol,
connection, integrability, and GR-regression suite passed. One historical
fiber test remains skipped by design.

## LaTeX gate

Nine roots were compiled in isolated directories with strict failure handling:

1. `canonical/gr_closure/gap_10t_paladini_torsion_dynamics.tex`
2. `canonical/gr_closure/gap_10l_psi_symmetry_propagation.tex`
3. `canonical/gr_closure/gap_10i_augmented_holonomy.tex`
4. `canonical/gr_closure/gap_10d_low_energy_uniqueness.tex`
5. `canonical/THEORY/canonical/canonical_action.tex`
6. `canonical/appendices/appendix_metric_review.tex`
7. `papers/UBT_GR_Submission.tex`
8. `docs/textbook/covariant_tetrad_student_paper.tex`
9. `canonical/UBT_canonical_main.tex`

Result: **9 attempted, 9 PDFs produced, 0 failures, 0 timeouts**.
The new PDFs and the revised GR/student PDFs were rendered and visually checked
for clipping, broken glyphs, and overlapping content.

## Explicit non-results

This validation does not prove:

- that the fundamental canonical UBT action is Hilbert--Palatini or satisfies
  the Lovelock hypotheses;
- the exact UBT spin current or the numerical values of `kappa` and `Lambda`;
- well-posedness of the final nonlinear self-consistent curved PDE;
- a global regular curved solution for arbitrary GR geometry;
- the original-master perturbation bridge (`GAP-B-MASTER`);
- canonical on-shell Schwarzschild lapse/tetrad selection (`GAP-U2Theta`).
