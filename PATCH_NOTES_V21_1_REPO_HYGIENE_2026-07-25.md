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

# UBT v21.1 repository-hygiene patch notes

Date: 2026-07-25

## Scope

This patch follows an independent audit of the SU(3) triqubit update and the
surrounding repository.  It does not change the verified SU(3) Fock
construction, the GEM compact-mode equations, or any canonical gravitational
equation.  It fixes active-code packaging, provenance validation, and two
status-wording drifts.

## Functional corrections

1. **Forensic fingerprint root detox**
   - Replaced active shims into the archived `ubt_with_chronofactor` package
     with root-level implementations.
   - Restored complete `cmb_comb`, Planck/WMAP loader, covariance, Grid-255,
     invariance, ablation, synthetic-control, and real-data-runner code.
   - The preserved sources under `ARCHIVE/` remain unchanged.

2. **Manifest validation now fails closed**
   - `files: []`, missing `files`, malformed entries, missing hashes, missing
     files, size mismatches, and digest mismatches return `False`.
   - Relative paths are resolved from an explicitly supplied base directory or
     from the repository root discovered from the manifest location, not from
     the caller's current directory.
   - The legacy real-data fallback may explicitly retry bare filenames relative
     to the observation-file directory and prints a warning when doing so.

3. **Remaining active runtime shims removed**
   - Restored local implementations for spectral utilities, `ubt_core`, alpha
     reproduction, `ubt_masses`, and flavour/RGE helpers used by the suite.
   - A repository scan finds no active `import_module("ubt_with_chronofactor…")`
     or `import_module("ubt_no_chronofactor…")` outside `ARCHIVE/`.

## Status-language alignment

- Route A4 now says the prime-attractor mechanism is `[L1 cond.] on G137-B`,
  not an unconditional existing L1 result.
- `research_tracks/T2_GAUGE/su3_proof_status.md` now matches
  `CLAIMS.yaml: three_generations = DERIVED_WITH_ASSUMPTIONS`.  The dimension
  count `dim_R(Im H)=3` remains exact; the physical generation identification
  and canonical dynamical selection remain assumptions/open.

## Validation

- 60/60 SU(3) triqubit tests passed.
- SU(3) algebra residual: `1.755e-16`.
- Both SU(3) verifiers passed.
- GEM compact-mode verifier passed with the stated action/dynamics limitations.
- 617 collectable repository tests were run in three groups and passed or were
  skipped by their existing markers.
- `tests/test_physics_properties.py` could not be collected because the optional
  `hypothesis` dependency is not installed and cannot be fetched in the current
  offline environment.
- Python `compileall` passed for all modified packages.

## Known pre-existing status-tool issue

The standalone broad alpha-overclaim scanner still reports older active files
outside this patch's scope.  This patch does not claim that the complete alpha
status corpus is clean; it fixes the specific Route A4 wording identified by
the audit.
