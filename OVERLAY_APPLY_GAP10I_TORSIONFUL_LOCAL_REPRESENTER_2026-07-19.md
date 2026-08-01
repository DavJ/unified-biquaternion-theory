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

# UBT GAP-10I torsionful local-representer overlay

Date: 2026-07-19  
Base archive: `unified-biquaternion-theory-master(17).zip`  
Base SHA-256: `469707a6eb92208a309606c56e87262a28871528217f6ae1c4d0eaaaa6c30ab5`

Apply by extracting the overlay ZIP into the repository root and allowing
replacement of existing files.  No files are deleted.

## Scientific status

- Corrects the pure-pair no-go to the torsion-free (`K=0`) branch.
- Closes `GAP-10I-TORSION-LOCAL` locally at L1 by an explicit composite
  metric-compatible contortion.
- Does not add independent `A`, `B`, or propagating torsion fields at the
  kinematic construction level.
- Does not close canonical action selection, physical torsion constraints,
  global continuation, Einstein dynamics, or on-shell Schwarzschild/Kerr/FRW
  selection.

## Validation

- 35 targeted architecture, claim-consistency, GR-closure, and publication tests passed.
- Both exact GAP-10I symbolic verifiers passed.
- 12 affected standalone LaTeX roots compiled successfully; the new theorem,
  canonical paper, GR paper, and student paper PDFs were rebuilt and visually
  checked.
- The unrestricted suite retains a pre-existing first failure in
  `test_validate_manifest_from_different_cwd`; the same first failure was
  reproduced on the untouched `(17)` baseline.

See `PATCH_NOTES_GAP10I_TORSIONFUL_LOCAL_REPRESENTER_2026-07-19.md` and the
overlay SHA-256 manifest for exact file hashes.

## Files

Modified: 46  
Added: 7  
Deleted: 0
