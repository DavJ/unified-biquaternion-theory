<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->

# Orthogonal review profiles

`PROVENANCE_TIERS.yaml` remains the stable A/B/C/D release classification.
Those tiers are intentionally not replaced by a combined `AB` tier, because a
single label could be misread as complete human and machine verification of an
entire document.

`PROVENANCE_REVIEW.yaml` records three independent axes for selected files:

- **machine verification**: how much is checked by named scripts or tests;
- **human review**: which part was actually examined and understood by a
  person;
- **editorial approval**: whether a named person consciously approved
  publication and accepts editorial responsibility.

The most common high-value UBT profile is expected to be:

```yaml
machine_verification: comprehensive_for_named_claims
human_review: selected_claims
editorial_approval: approved
```

This means that every listed claim has strong reproducible checks, the author
has reviewed and understood the explicitly named principal claims, and the
file is consciously approved for publication.  It does **not** claim a manual
line-by-line recomputation of every displayed formula.

## Source block

A source listed in the registry carries a second structured comment block:

```text
UBT-REVIEW-PROFILE-BEGIN
schema: ubt-review-profile/v1
machine_verification: comprehensive_for_named_claims
human_review: selected_claims
editorial_approval: approved
registry: PROVENANCE_REVIEW.yaml
UBT-REVIEW-PROFILE-END
```

This block is independent of the existing `UBT-AI-PROVENANCE` marker.  The
registry is the source of truth; `tools/verify_provenance_review.py` checks the
registry, source block, evidence paths, dates and approval fields.

## Publication notice

Curated LaTeX sources may use:

```tex
\UBTReviewProfile
  {comprehensive for named claims}
  {selected principal claims}
  {author approved}
```

The visible PDF notice and PDF metadata then expose all three axes.  A document
without this macro keeps the legacy tier-only notice unchanged.

## Interpretation limits

Machine tests establish only the statements encoded by those tests.  Human
review applies only to the scope named in the registry.  Editorial approval is
not a claim that every equation was independently recomputed.  Claim maturity
(`speculative`, `candidate`, `conditional`, `proved`) remains a separate
scientific classification.
