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

# Provenance release gate and macOS portability — 2026-08-01

This patch targets the signed 2026-08-01 repository snapshot.

It closes four narrow release-path issues:

1. `PROVENANCE_TIERS.yaml` is now treated as a strict YAML document. Duplicate
   mapping keys fail tests instead of silently overwriting an earlier value.
2. `.github/workflows/latex_build.yml` requires the human Tier-A sign-off before
   compilation and publishes or commits curated PDFs only after successful
   provenance and PDF-metadata verification.
3. Checksum verification uses `tools/verify_sha256sums.py`, avoiding the
   GNU-only `sha256sum` dependency on macOS.
4. `SHA256SUMS.txt` is regenerated after the author's signed tier-map change.

The scientific content, equations, claim levels, GAP statuses, and PDF bodies
are unchanged by this patch.
