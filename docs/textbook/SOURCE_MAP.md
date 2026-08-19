<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# UBT textbook source map

**Purpose:** prevent the student textbook from silently learning active claims from
`ARCHIVE/**`.  Historical files remain useful for provenance and comparison, but they
are not sources of record.

## Rule

1. The textbook is Tier `C_working` and may contain self-contained pedagogical
   derivations of classical mathematics.
2. Active UBT status is taken from Tier-A status/claim ledgers first
   (`STATUS.md`, `WHAT_IS_PROVED.md`, `CLAIMS.yaml`, `DERIVATION_INDEX.md`).
3. Mathematical definitions and machine-verified derivation components may be cited
   from `canonical/**` (Tier `B_machine_verified`), but their status wording must not
   override the Tier-A ledgers.
4. `ARCHIVE/**` (Tier `D_historical`) may be discussed explicitly as historical
   material, but it must not be `\input` into the live textbook.
5. When an old route conflicts with the current architecture, the textbook states
   the conflict and teaches the current route.

## Migration of the former archive-backed chapters

| Textbook chapter | Former archive dependency | Live replacement / authority | Action |
|---|---|---|---|
| `chapters/01_overview.tex` | `consolidation_project/ubt_2_main.tex` | `STATUS.md`, `WHAT_IS_PROVED.md`, `papers/UBT_GR_Submission.tex` | Rewritten as a status-aware overview; obsolete projection language removed. |
| `chapters/03_lorentz_in_HC.tex` | `consolidation_project/appendix_P6_lorentz_in_HC.tex` | classical `Herm(2,C)`/`SL(2,C)` construction + `canonical/algebra/biquaternion_algebra.tex` + current Lorentz-slice convention in the GR track | Rewritten self-contained, with proof of determinant invariance and an explicit map to biquaternion notation. |
| `chapters/04_ct_scheme.tex` | `consolidation_project/alpha_two_loop/tex/ct_scheme_definition.tex` | standard Ward--Takahashi identities + `canonical/THEORY/complex_time_canonical_choice.tex` + Tier-A alpha status | Rewritten as pedagogy and status, not as a proof that the archived two-loop route closes alpha. |
| `chapters/05_alpha_derivation.tex` | `R_UBT_extraction.tex`, `appendix_CT_two_loop_baseline.tex`, `geometric_inputs_proof.tex` | `STATUS.md`, `WHAT_IS_PROVED.md`, `canonical/alpha/ALPHA_MASTER_STATUS.md`, current alpha sub-results | Rewritten to expose the conditional chain and the two distinct `N_eff` counts; `fit-free` overclaim removed. |
| `chapters/06_tests_and_repro.tex` | prose path to archived alpha tests | active `tests/`, `tools/`, `research_tracks/` | Updated to active paths and the real CI artifact name. |

## Superseded statement that must not return

The archived consolidated manuscript described a real metric as an
"observer-restricted Hermitian projection".  The current covariant-tetrad branch uses
instead the central anticommutator

`1/2 (E_mu^sharp E_nu + E_nu^sharp E_mu) = g_munu 1`

on the real Lorentz slice.  The live textbook therefore does **not** teach a projection
as necessary for the minimal local metric construction.

## Alpha wording guardrail

The live textbook must not say simply "fit-free alpha derivation".  The safe current
summary is:

- the prime-stability/`n=137` structure has conditional/structural results;
- the required effective coefficient `B` is not derived from the UBT action;
- the loop-safe and twist-sector `N_eff` counts are not yet identified with each other;
- physical `alpha^{-1}=137.036...` is not derived from first principles.

This wording is subordinate to the current Tier-A status ledgers if those files change.
