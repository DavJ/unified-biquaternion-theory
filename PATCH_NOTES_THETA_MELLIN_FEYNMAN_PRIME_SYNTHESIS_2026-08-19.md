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

# Patch notes — theta / Mellin / Feynman / prime synthesis

**Date:** 2026-08-19  
**Scope:** documentation + reproducible bridge mathematics. No canonical UBT claim is promoted by this patch.

## Motivation

Preserve the 2026-08-19 research thread in a form useful both as a student reference and as an auditable research map. Classical mathematics is retained when it is needed to understand UBT, while labels distinguish standard results, controlled bridge statements, and UBT-open claims.

## Added

- `docs/textbook/chapters/05_theta_mellin_feynman_big_picture.tex`
  - theta-template Gram kernel and non-orthogonality;
  - matched-filter interpretation;
  - Fourier/Laplace/Mellin spectral triangle;
  - Mellin as Fourier in logarithmic coordinates;
  - time-twisted quadratic zeta family
    \(Z_\Theta(s;t)=\sum_{n\ge1}e^{i\pi t n^2}n^{-2s}\);
  - ordinary \(\zeta(2s)\) as the \(t=0\) slice in the working UBT time convention;
  - \(t=1\) eta-function slice;
  - rational-time Hurwitz-zeta decomposition;
  - quadratic Gauss sums and CRT factorization;
  - exact free-particle-on-\(S^1\) theta-mode ↔ Feynman-winding bridge;
  - Euler-factor pole lattices, vertical Fourier log-frequencies, von Mangoldt prime-power comb, and PNT/explicit-formula context;
  - `GAP-THETA-PROP`, `GAP-THETA-PRIME-1`, and `GAP-THETA-PRIME-2`.
- `research_tracks/theta_spectral/theta_mellin_feynman_prime_synthesis_2026-08-19.md`
  - consolidated research note preserving the full thread, caveats, blocked routes, and next mechanisms to test.
- `research_tracks/theta_spectral/theta_zeta_probe.py`
  - numerical checks for Mellin/theta/zeta identity;
  - time-twisted special slices and rational Hurwitz decomposition;
  - noncollision sanity check for prime-power log frequencies;
  - exact Gauss-sum CRT checks;
  - Gram conditioning/ridge check;
  - deterministic noisy matched-filter recovery demonstration.

## Updated

- `docs/textbook/main.tex`
  - includes the new theta/Mellin/Feynman chapter before the alpha chapter;
  - title changed to `Student Text and Engineer's Guide`.
- `docs/textbook/frontmatter/preface.tex`
  - states the textbook policy: retain classical foundations, derive them didactically, then connect them explicitly to UBT bridges/claims/gaps.
- `docs/textbook/CONTRIBUTING.md`
  - codifies the same three-layer policy and preservation of useful negative results.
- `research_tracks/theta_spectral/trace_formula_connections.tex`
  - cross-links the older primitive-orbit prime route with the new rational-revival/Gauss route and keeps them logically distinct.

## Important convention note

An earlier RH scratch thread used the positive heat coordinate \(y=-\psi\) and wrote the theta parameter as \(t-i\psi=t+iy\). The new textbook chapter uses a positive damping coordinate directly in \(e^{-\pi\psi n^2}\). The two are related by the relabelling \(y=-\psi\); the sign convention must be fixed before attaching a physical direction to UBT imaginary time.

## Validation

- `python tools/apply_provenance_headers.py --check` — PASS.
- `python research_tracks/theta_spectral/theta_zeta_probe.py` — PASS.
- New textbook chapter compiled standalone with `pdflatex` — PASS.
- Updated `trace_formula_connections.tex` compiled standalone with `pdflatex` — PASS.
- Full `docs/textbook/main.tex` build remains blocked by a **pre-existing repository issue**: `chapters/01_overview.tex` inputs missing `../../consolidation_project/ubt_2_main.tex`. This patch does not alter that unrelated dependency.
