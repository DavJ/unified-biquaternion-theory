<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Gauge/QM Honest-Status Patch Validation

**Date:** 2026-07-17  
**Patch:** `UBT_GAUGE_QM_HONEST_STATUS_ROOT_OVERLAY_2026-07-17.zip`  
**Base:** repository after the v10.3.0 GR-subclosures overlay and the reviewed
History-of-UBT overlay

## Scope

This patch changes only the claim status and explanatory documentation of the
legacy gauge and quantum-emergence branches. It does not alter the frozen
covariant-tetrad GR architecture or any GR theorem.

## Patch-specific regression result

```text
30 passed
```

Command:

```bash
pytest -q tests/test_claims_consistency.py \
  tests/test_involutions_triplet_space.py \
  tests/test_architecture_freeze_and_latex_workflow.py \
  tests/test_remaining_gr_subclosures.py
```

The claims scan now recursively includes `canonical/gauge/` and
`canonical/qm_emergence/`.

## TeX validation

| Document | Result | Pages |
|---|---:|---:|
| `canonical/qm_emergence/step7_born_rule.tex` | compiled, rendered, visually checked | 2 |
| `docs/notes/symmetry_from_automorphisms.tex` | compiled, rendered, visually checked | 11 |
| `canonical/su3_derivation/su3_from_involutions.tex` | compiled through a temporary wrapper, rendered, visually checked | 15 |

No LaTeX compilation errors occurred. The temporary SU(3) wrapper deliberately
did not load the parent bibliography, so its pre-existing external
representation-theory citation remained unresolved in that wrapper only.

The retracted Born document was reformatted so that its final status table no
longer extends beyond the page. The SU(3) status table was also constrained to
the width of its status box.

## Verbatim legacy-gauge deprecation header

> **DEPRECATED AS A STATUS SOURCE (2026-07-17).** The legacy labels in this
> file, including `SU(3): PROVED` and `SU(2)_L: PROVED`, are superseded by
> `CLAIMS_MATRIX.md`, where the Standard-Model gauge chain is
> `DERIVED_WITH_ASSUMPTIONS`. The July 2026 gauge audit established that the
> involutions select a complex rank-three carrier, while the unitary/Yang--Mills
> dynamics on that carrier is still an introduced structure (`GAP-SU3-DYN`).
> This file is retained for historical traceability and must not override the
> current claim ledger. See `reviews/gauge_qm_honest_status_audit_2026-07-17.md`.

## Verbatim Born-rule retraction header

> **RETRACTED (2026-07-17).** The previous argument conflated the
> Fokker--Planck equation for a probability density `P` with a diffusion
> equation for the amplitude `Theta`. For example,
> `Theta = exp(ikx-Dk^2T)` solves amplitude diffusion, while its squared norm
> decays as `exp(-2Dk^2T)`. The file is retained to preserve the correct
> norm-decay computation and the audit trail. It is superseded by the OPEN
> Born-rule/unitarity status in `CLAIMS_MATRIX.md`.

## Verbatim SU(3) scope statement

> The involution construction selects a complex rank-three carrier
> `V_c ≅ C^3` [proved]. Once a unitary structure on that carrier is postulated,
> its traceless unitary transformations have Lie algebra `su(3)` and the
> standard fundamental/adjoint representation theory follows. The selection of
> the unitary/Yang--Mills dynamics from the canonical UBT action remains open as
> `GAP-SU3-DYN`.

## Full-suite note

A full repository `pytest -q` run was attempted. It is not claimed as clean:
the first isolated blocker, `test_validate_manifest_from_different_cwd`, also
fails on the unmodified pre-patch base, and the longer run contains additional
unrelated legacy failures. This patch neither introduces nor repairs those
pre-existing repository-wide issues. The complete patch-specific and GR
regression suite listed above passes.
