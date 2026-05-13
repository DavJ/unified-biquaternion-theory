<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Publication Canonicals and Release Hygiene

Purpose: keep one canonical manuscript per track in papers/ and archive prior release variants in papers/old_releases/.

## Canonical Manuscripts (active)

- GR track canonical manuscript: `papers/UBT_GR_Submission.tex`
- Gauge track canonical manuscript: `papers/UBT_Gauge_Submission.tex`

## Archived Releases (historical)

- `papers/old_releases/UBT_GR_RC1_v2.tex`
- `papers/old_releases/UBT_GR_RC1_v2.pdf` (submitted to OSF)
- `papers/old_releases/UBT_GR_RC2.tex`
- `papers/old_releases/UBT_GR_Submission_v2.tex`

## Operating Rules

1. Keep exactly one active manuscript filename per track in papers/ root.
2. New iteration before submission: edit the canonical file in place, do not create a new root filename.
3. If a frozen snapshot is needed for external deposit, copy it to papers/old_releases/ with date or RC suffix.
4. Update references in `STATUS_OF_UBT.md`, `WHAT_IS_PROVED.md`, `CLAIMS_MATRIX.md`, and `README.md` in the same commit.
5. If external platforms (OSF/Zenodo/arXiv) receive a non-canonical file, record it in this document.
