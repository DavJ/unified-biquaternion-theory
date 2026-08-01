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

# Apply: signed provenance release gate — 2026-08-01

Unpack the overlay directly in the repository root, then run:

```bash
bash APPLY_PROVENANCE_RELEASE_GATE_2026-08-01.sh
```

On macOS, PDF verification also requires Poppler:

```bash
brew install poppler
```

The apply script is idempotent. It verifies the overlay manifest, rechecks the
signed Tier-A map, regenerates the repository checksum anchor, and runs the
focused provenance/release regression tests.
