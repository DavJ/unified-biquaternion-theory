# Apply GR submission/status synchronization overlay — 1 August 2026

Apply this ZIP at the repository root. The archive is repository-relative and
contains no wrapper directory.

## Purpose

This is a status and release-hygiene synchronization only. It does not change
the GR architecture, promote the noncanonical profile branch, or promote the
speculative invisibility track.

## Corrections

- synchronizes the abstract and front proof-status boxes of
  `papers/UBT_GR_Submission.tex` with the theorems already present later in the
  paper:
  - split-jet local right inverse;
  - algebraic/nonpropagating auxiliary jet variables;
  - no-go for dynamical selection by the surjective pure constraint;
  - conditional induced Einstein–Lambda infrared branch;
- restores the explicit strict-holomorphy boundary, general
  constrained-rank projection criterion, `F_z` condition, and rank-budget
  no-go in the active generalized-Dirac proof status;
- removes three accidentally reintroduced active copies of the historical
  dual-sector/current-tetrad track while preserving their dated history copies;
- regenerates `docs/pdfs/UBT_GR_Submission.pdf` from the synchronized TeX and
  makes the two status boxes breakable so no text overlaps the page footer.

## Metric interpretation retained

For the current `sharp` construction, the symmetric channel is always central:
its coefficient may be complex, `gamma_mu_nu = g_mu_nu + i h_mu_nu`, but it is
not genuinely quaternion-valued. Quaternion-vector information is carried by
the antisymmetric `Sigma_mu_nu` channel. Exact classical GR remains the real
Lorentzian branch. The profile realization of the complex channel remains
noncanonical.

## Apply deletions

After extracting the ZIP at repository root, run:

```bash
bash APPLY_GR_SUBMISSION_SYNC_2026-08-01.sh
```

The script only removes the paths listed in
`DELETE_PATHS_GR_SUBMISSION_SYNC_2026-08-01.txt` and is idempotent.

## Verification performed

- `papers/UBT_GR_Submission.tex` compiles successfully with `latexmk`;
- the generated 21-page PDF was rendered and visually checked, including the
  split status boxes and gap ledger;
- the targeted canonical-Dirac, GR, complex-metric, and invisibility regression
  suite passes, with one pre-existing skip for missing `CURRENT_STATUS.md`;
- complete suite collection in the audit container still requires the optional
  `hypothesis` package, which is already declared in `requirements.txt` and in
  the `dev` extras of `pyproject.toml`.
