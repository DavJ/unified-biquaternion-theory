# Release checklist — v10.2.1

**Purpose:** technical and audit patch for the v10.2.0 covariant-tetrad
milestone. This release must not introduce a new GR architecture or claim new
fundamental gap closure.

## Scientific content

- [x] Covariant-tetrad architecture frozen for v10.x.
- [x] Architecture-before-repair rule added to human and AI instructions.
- [x] Standard Cartan/tetrad geometry distinguished from UBT-specific results.
- [x] One-sided no-go assumptions restated explicitly.
- [x] Two-sided derivative described as a minimal demonstrated route, not a
      uniqueness theorem.
- [x] Fiber route archived as mathematically consistent but weakly selective.
- [x] v10.2.1 preserves the pre-v10.3 ledger; the new conditional subclosures belong to the subsequent mathematical release.

## PDF build

The repository-wide local audit on 2026-07-16 found:

- standalone active TeX roots attempted: **327**;
- PDFs produced: **219**;
- failed roots logged: **108**;
- timed-out roots: **0**.

The failures are retained under `reports/latex_build/` and did not interrupt
later roots.

### Release-critical PDFs

- [x] `canonical/UBT_canonical_main.tex`
- [x] `papers/UBT_GR_Submission.tex`
- [x] `canonical/gr_closure/covariant_tetrad_rank_theorem.tex`
- [x] `canonical/gr_closure/gap_10omega_connection_elimination.tex`
- [x] `canonical/gr_closure/gap_10i_integrability_selection.tex`
- [x] `docs/textbook/covariant_tetrad_student_paper.tex`

All six compiled successfully after the final source edits and were copied to
`docs/pdfs/`. Selected rendered pages were visually inspected for clipping,
missing glyphs, and broken layout.

## Tests

- [x] LaTeX batch compiler unit tests.
- [x] Architecture-freeze/workflow regression tests.
- [x] Covariant tetrad, GAP-10Ω, and GAP-10I tests.
- [x] Claims/status consistency tests.
- [x] Historical fiber guard test remains skipped as intended.

A repository-wide pytest invocation reaches unrelated pre-existing failures and
long-running suites; v10.2.1 is gated by the targeted tests for files changed in
this patch, not by retroactively repairing every research track.

## Metadata and release

- [x] `.zenodo.json` version and description updated to `v10.2.1`.
- [x] `CITATION.cff` version and release date updated.
- [x] `CHANGELOG.md` and patch notes updated.
- [ ] Create GitHub tag/release `v10.2.1` only after merging this patch.
- [ ] Verify Zenodo imports the exact GitHub release archive.
- [ ] Do not modify the historical `v10.2.0` tag or release.


## Subsequent v10.3.0 development note

After the v10.2.1 technical gate, the frozen architecture acquired four new
mathematical subclosure notes: minimal Palatini torsion elimination,
Lorentz/psi symmetry propagation, prescribed-coefficient augmented holonomy,
and the conditional Palatini/Lovelock Einstein--Lambda endpoint. These belong
to v10.3.0 and do not alter the historical scope of v10.2.1.
