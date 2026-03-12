# Consolidation Project — Clean/Core vs. Speculative Split
**Updated:** 2025-08-09

This consolidation refactors the project into two clearly separated layers:

- **CORE (publishable):** mathematically consistent UBT content (biquaternion GR, EM, QED, SM embeddings) that does **not** rely on prime-based heuristics or consciousness interpretations.
- **SPECULATIVE (research notes):** hypotheses and work-in-progress ideas (ψ–consciousness link, psychons, p‑adic/prime discretizations, CTCs, rotating metrics beyond standard energy conditions, "parameter‑free" mass schemes).

The goal is to address reviewer feedback (incl. Gemini) without discarding promising ideas. The main article and appendices for submission must reference ONLY the CORE set. Speculative items live in a separate notes track.

## Directory Guide
- `appendix_A_biquaternion_gravity_consolidated.tex` — **CORE**
- `appendix_C_electromagnetism_gauge_consolidated.tex` — **CORE (canonical path)**
- `appendix_D_qed_consolidated.tex` — **CORE**
- `appendix_E_SM_QCD_embedding.tex` — **CORE (partial; mark sections needing proof)**

- `appendix_F_psychons_theta.tex` — **SPECULATIVE**
- `appendix_G_dark_matter_unified_padic.tex` — **SPECULATIVE**
- `appendix_H_alpha_padic_combined.tex` — **SPECULATIVE**
- `appendix_J_rotating_spacetime_ctc.tex` — **SPECULATIVE**
- `appendix_K_fundamental_constants_consolidated.tex` — **SPECULATIVE**

See `MANIFEST_CORE.txt` and `MANIFEST_SPECULATIVE.txt` for full lists.

## Canonical EM/QED Derivation
Use the chain documented in `EM_QED_CANONICAL_PATH.md`. Alternative derivations should be relegated to `notes/` with explicit status.

## Fine-Structure Constant (α) Policy
The mainline does **not** assert an ab‑initio derivation of α. We treat α as an empirical parameter (with standard QED running). Prime/p‑adic or entropic models are documented in `SPECULATIVE_NOTES.md` and excluded from claims in the main text. See `alpha_statement.md`.

## Consciousness & ψ
Interpretations connecting ψ to consciousness are moved to `SPECULATIVE_NOTES.md`. The CORE text may mention ψ as a generic phase coordinate with information‑theoretic meaning **without** ontological claims.

## Submission Build
- `make core` — builds only CORE appendices into `pdf/ubt_core.pdf`
- `make all` — builds full set (clearly watermarking SPECULATIVE sections).

## Reviewer-facing Summary
See `REVIEWER_SUMMARY.md` for a 2‑page narrative aligning the project with mainstream standards (assumptions, theorem/lemma structure, limits matching GR/QED, falsifiable predictions).

