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

# Textbook consolidation and derivation-verification policy — 2026-08-19

## Scope

This patch changes repository/documentation workflow only. It does not promote
or alter any scientific UBT claim tier.

## Textbook

- `docs/textbook/main.tex` is the single primary textbook root.
- Standalone student papers are explicitly supplements rather than competing
  textbooks.
- The book is grouped into four parts: foundations/geometry, complex-time and
  spectral structure, phenomenology/verification/applications, and appendices.
- The build contract now emits stable PDFs under `build/textbook/public/` and
  `make -C docs/textbook publish` copies the curated set to `docs/pdfs/`.
- `.github/workflows/textbook.yml` runs on relevant pushes/PRs as well as manual
  dispatch and uploads the stable PDF set.
- The primary student edition is Czech. New student-facing prose should be
  Czech; an English edition should be parallel rather than mixed into Czech
  chapters. Existing inherited English prose is a migration debt and is not a
  template for new text.

## Derivation verification

New policy: `docs/DERIVATION_VERIFICATION_POLICY.md`.

- Lean is the preferred formal verifier for theorem-critical exact mathematics.
- A generated `.lean` file is not a proof unless Lean actually checks it.
- Missing formalization is recorded explicitly as `LEAN-PENDING`.
- Paper-critical results should normally have two independent verification
  channels, preferably Lean plus an independent CAS/numerical implementation.
- Supported cross-check tools include SymPy, Maxima, NumPy/SciPy, GNU Octave,
  MATLAB, and Mathcad; open/scriptable tools are preferred for public CI.
- Every active paper is in scope. New/materially modified papers must record
  tool/version, artifact, assumptions, scope, limitations, result, and Lean
  status in the same patch; older active papers form a migration queue.
- Machine checks never automatically promote a UBT proof/claim tier.

The policy is wired into `AGENTS.md`, `.github/copilot-instructions.md`,
`docs/UBT_COPILOT_INSTRUCTIONS.md`, `docs/copilot/01_COPILOT_INSTRUCTIONS.md`,
and `CONTRIBUTING.md`.

## Verification performed in this environment

- provenance header check: PASS;
- SHA-256 manifest verification: PASS (99 entries);
- strict textbook LaTeX audit: 3/3 roots PASS;
- stable textbook PDF build: PASS;
- PDF render inspection: PASS for the main book and both supplements.

Available local math tools during this patch:

- SymPy 1.14.0;
- NumPy 2.3.5.

Not installed in this runtime:

- Lean/Lake;
- Maxima;
- GNU Octave;
- MATLAB.

No claim of Lean verification is made by this patch.
