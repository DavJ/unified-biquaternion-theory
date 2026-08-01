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

# UBT differential patch — canonical action audit for GAP-10T-DYN and GAP-10D

**Patch date:** 2026-07-26
**Base archive commit marker:** `c9cf57384dc9bc0609614a6f9bcf14281407d2ac`

Root-relative overlay. Extract from the repository root so `canonical/`,
`tools/`, and `tests/` merge with the existing tree.

## Scope

Implements the canonical-action audit task for GAP-10T-DYN and GAP-10D.
No new independent fields are introduced. No closure is claimed by importing
the Hilbert–Palatini action; the import is classified as an import.

## Results

1. **Dependency classification** of every working-action object into
   derived / low-energy assumption / standard import / undefined
   (audit TeX, item table).
2. **Exact tree-level spin current derived** for the pure-pair
   representative `A = Omega, B = -Omega^ddagger`:
   `tau^mu(M) = <M Theta + Theta M^ddagger, D^mu Theta>`.
   Verified for both canonical pairings (ddagger Hilbert–Schmidt and
   sharp scalar-part).
3. **Slice lemma [L0]:** with `D Theta` in the Lorentz slice, the current
   couples only to the anti-Hermitian part of `Theta`.
4. **Pointwise rigidity [L0]:** for the standard nondegenerate tetrad the
   joint kernel over all four slots is exactly anti-Hermitian part zero.
5. **Flat affine no-go [L1] (`GAP-10T-FLAT-NOGO`):** on every affine
   representer the current vanishes at most at one point; its gradient is a
   `Theta0`-independent nonzero constant (`±2 N0` ddagger, `±N0` sharp).
   With the proved invertible Cartan map, the minimal Hilbert–Palatini +
   kinetic branch forces nonzero torsion there, so the flat inertial
   torsion-free solution is not a solution of the minimal branch. This is
   the exact flat-space counterpart of the curved Gaussian-patch scaling
   obstruction (`K ~ 1/rho` kinematic vs `tau ~ rho` sourced).
6. **No curvature from `S_Theta` at tree level:** the kinetic density is
   polynomial degree two in `Omega` with no derivatives of `Omega`; every
   curvature term originates in the imported `S_HP`.
7. **Coefficient audit:** neither sign nor magnitude of `1/4 kappa` nor
   `Lambda` is fixed by `N0` or the `Theta` vacuum; spectral tooling reaches
   only flat tori. Recorded as the named induced-Palatini lemma in GAP-10D.

## Verdicts (CLAIMS.yaml aligned)

- `GAP-10T-SPIN`: CLOSED CONDITIONALLY [L1] (pairing class + pure pair).
- `GAP-10T-FLAT-NOGO`: CLOSED AS NO-GO [L1].
- `GAP-10T-DYN`: NARROWED — remaining lemma named (non-minimal torsion
  term, canonically selected pairing/projection annihilating the affine
  current, or torsion-free relative bimodule completion, derived from
  `S[Theta]`).
- `GAP-10D`: NARROWED — remaining lemma named (induced-Palatini
  coefficient derivation, e.g. curved heat-kernel `a2` of `D^dagger D`).
- "Essentially closed" is not used anywhere.

## Files

- `canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex` (new)
- `tools/verify_canonical_spin_current.py` (new)
- `tests/test_canonical_spin_current.py` (new)
- `CLAIMS.yaml` (edited: evidence + four assumption-ledger lines)
- `CLAIMS_MATRIX.md` (edited: GR row notes + source list)
- `PATCH_NOTES_GAP10TDYN_10D_ACTION_AUDIT_2026-07-26.md` (this file)
- `PATCH_FILELIST_GAP10TDYN_10D_ACTION_AUDIT_2026-07-26.txt`

## Validation

- `python tools/verify_canonical_spin_current.py` — 13/13 exact checks PASS.
- `pytest tests/test_canonical_spin_current.py tests/test_claims_consistency.py`
  — 7 passed (5 new + 2 claims-consistency).
- Full suite `pytest tests/` — green (passed/skipped only), including
  `tests/test_physics_properties.py` with `hypothesis` installed.
- `pdflatex` on the audit TeX — compiles cleanly, 3 pages.

## Explicit non-claims

This patch does not close GAP-10T-DYN or GAP-10D, does not derive `S_HP`,
and does not decide whether the composite scheme reproduces
Einstein–Hilbert. The curved-patch scaling no-go remains a separate result
with its own overlay; this patch neither depends on it nor supersedes it.
