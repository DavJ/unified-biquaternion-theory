<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Publication Canonicals and Release Hygiene

Purpose: keep one canonical manuscript per track in papers/ and archive prior release variants in papers/old_releases/.

This file defines the long-term publication hygiene policy for multiple papers.

## Canonical Manuscripts (active)

- GR track canonical manuscript: `papers/UBT_GR_Submission.tex`
- Gauge track canonical manuscript: `papers/UBT_Gauge_Submission.tex`

## Scalable Naming Standard

- Canonical manuscript per track:
	- `UBT_<Track>_Submission.tex`
- Optional support files:
	- `UBT_<Track>_Abstract.md`
	- `UBT_<Track>_Flagship.bib`
	- `UBT_<Track>_Figures/`
- Archived snapshots:
	- `papers/old_releases/UBT_<Track>_<Tag>.tex`
	- `papers/old_releases/UBT_<Track>_<Tag>.pdf`
	- where `<Tag>` can be `RC1_v2`, `pre_arxiv_2026-05-13`, `osf_upload_2026-05-13`, etc.

## Directory Roles

- `papers/`:
	- only canonical active manuscripts and shared publication controls
- `papers/old_releases/`:
	- immutable historical snapshots and externally uploaded file variants
- `papers/PUBLICATION_INDEX.md`:
	- one-row-per-track index of canonical file, status, and primary target venue
- `papers/DEPOSITION_LOG.md`:
	- append-only external upload log (OSF, arXiv, Zenodo)

## Noncanonical root-level legacy drafts

The following root-level files are retained only for backward file-history
compatibility and are **superseded** by `papers/UBT_GR_Submission.tex`:

- `papers/UBT_GR_Flagship.tex`
- `papers/UBT_GR_RC2_final.tex`

They contain historical claim language that is not the current audited status
and must not be submitted, cited as the current result, or used to prepare a
release. A future repository-cleanup commit may move them to
`papers/old_releases/`; until then, the canonical registry above controls.

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

## Release Lifecycle (per track)

1. Draft in canonical file.
2. Freeze snapshot for external upload into `papers/old_releases/`.
3. Record upload in `papers/DEPOSITION_LOG.md` with file name and date.
4. Keep canonical file as the single source for ongoing edits.
5. If canonical target changes, update `papers/PUBLICATION_INDEX.md` first.
