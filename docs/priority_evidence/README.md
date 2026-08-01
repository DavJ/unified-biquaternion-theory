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

# Priority evidence

Priority claims in UBT are mechanism-specific. This folder separates three
questions that must not be conflated:

1. **What historical artifact exists?** — fixed by an archive/page SHA-256.
2. **What date is externally represented in that artifact?** — an embedded post
   date or a dated site-backup label.
3. **What proposition does it actually support?** — listed under `supports`;
   stronger later theorems are listed under `does_not_support`.

The complete legacy archive should be deposited separately in an immutable
repository (for example Zenodo) and its DOI added to the evidence JSON. The
main UBT repository intentionally retains only hashes and selected equation
assets, avoiding a 170 MB historical dump and unrelated personal material.
