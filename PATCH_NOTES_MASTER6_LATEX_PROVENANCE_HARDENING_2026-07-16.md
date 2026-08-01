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

# Master(6) LaTeX provenance hardening — 2026-07-16

## Scope

This technical patch preserves the exact source-commit provenance of generated
PDFs and LaTeX audit reports.

## Change

The long-running `latex_build.yml` workflow no longer rebases its generated
commit onto a newer `master` head.  Before committing generated reports and
curated PDFs, it fetches `origin/master` and compares it with `GITHUB_SHA`.

- If the branch is unchanged, the generated files are committed normally.
- If a human or another process advanced `master`, all workflow artifacts and
  failure logs remain available from the Actions run, but the workflow refuses
  to attach stale PDFs to the newer source commit.  The newer push starts its
  own fresh workflow run.

This changes no scientific source, claim, equation, or PDF content.
