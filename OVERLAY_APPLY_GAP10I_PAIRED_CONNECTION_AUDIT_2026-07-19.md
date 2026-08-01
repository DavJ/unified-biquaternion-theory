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

# UBT GAP-10I paired-connection audit overlay

> **Superseded scope note (19 July 2026):** the concurrent-vector no-go below is valid only for the torsion-free (`K=0`) generated-tetrad branch. The later `GAP-10I-TORSION-LOCAL` theorem constructs a local composite-contortion representer for every smooth Lorentzian tetrad, so a relative pair is not required for local kinematics.

Date: 2026-07-19
Base archive: `unified-biquaternion-theory-master(16).zip`
Base SHA-256: `64c021a3c928d81c468b930e7b78781746504d0ddcd700467a467c1742ad9462`

Apply by extracting this ZIP into the repository root and allowing replacement of existing files.
No files are deleted by this overlay.

## Scientific status

- Closes `GAP-10I-PAIR-KIN` at L1: Lorentz-slice and metric compatibility reduce the left/right pair to one spin connection, modulo a cancelling common central term.
- Closes `GAP-10I-PAIR-GR` as an L1 **torsion-free** no-go: the `K=0` pure paired branch implies a concurrent/homothetic vector and excludes the non-flat Schwarzschild vacuum exterior with nonzero mass.
- The later torsionful-local overlay supersedes the earlier claim that a relative pair is required.  Full `GAP-10D` nevertheless remains open/narrowed because canonical torsion/current selection and Einstein dynamics are not derived.

## Validation

Focused repository tests: 15 passed.
Symbolic verifier: all implemented checks passed.
All updated LaTeX targets compiled; rebuilt PDFs are included.
The unrestricted legacy suite has pre-existing failures; its first failure (`test_validate_manifest_from_different_cwd`) reproduces unchanged on the supplied base archive.

## Files

Modified: 34
Added: 5
Deleted: 0
