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

# History overlay validation — 2026-07-17

## Baseline

Validated against the user-supplied repository snapshot
`unified-biquaternion-theory-master(8).zip`.

## Content review

- The 2013 independent biquaternionic electromagnetic notation is recorded
  without a historical-priority claim.
- Handwritten candidate metric calculations from 2013–2015 are explicitly
  identified as pre-AI work.
- AICON Seattle 2025, the Fokker–Planck insight, NDC London 2026, the transition
  toward agentic development, and Chinese-developed models from 16 July 2026
  are retained.
- The decisive scientific and architectural choices remain assigned to David
  Jaroš; AI is described as an assisting and auditing tool.
- Early claims about superluminal longitudinal propagation and a
  biquaternionic-coordinate invisibility machine remain historical hypotheses.
  The text records the relevant constraints from standard Lorentz causality,
  transverse source-free vacuum waves, and transformation-optics cloaking.

## Automated checks

```text
pytest -q tests/test_history_of_ubt.py
4 passed
```

A repository-wide test collection was also attempted. It could not be used as a
release gate in this container because `tests/test_physics_properties.py`
requires the optional `hypothesis` package, which is not installed. A second
run excluding that module exceeded the execution window and exposed unrelated
pre-existing failures before timeout. The history-specific regression suite is
fully passing.

## Scope result

No canonical mathematics, claim ledger, GR closure file, gauge/QM file, paper,
or generated PDF is modified by this overlay.
