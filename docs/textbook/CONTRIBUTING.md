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

# Contributing to the UBT Textbook

## Purpose

The textbook is a working learning/reference text, not merely a compressed publication summary. It should preserve enough derivation and context that a reader can reconstruct why a mathematical tool is relevant to UBT.

## Content policy

1. **Keep classical mathematics when it is structurally useful.** Label it as classical/standard; do not omit it merely because it is not novel.
2. **Derive before claiming.** Give rigorous derivations or precise references for standard identities, then state exactly how UBT uses them.
3. **Separate layers visibly:** classical foundation → controlled UBT bridge → UBT-specific theorem/claim/open gap.
4. **Never promote by association.** A standard identity used in a UBT argument is not itself a UBT theorem.
5. **Preserve negative results and objections.** A blocked route belongs in the research record if it clarifies what a future derivation must supply.
6. **Keep canonical claim files conservative.** Expansive synthesis, alternative representations, and exploratory connections belong here or in `research_tracks/` until their UBT-specific bridge is closed.
7. **Never `\input` live textbook content from `ARCHIVE/**`.** Historical material may be quoted or discussed with an explicit historical label, but it is not a source of record.
8. Reuse active canonical source with `\input{../../...}` only when the target is include-safe and exact claim text must stay synchronized; otherwise cite the canonical path and write a self-contained textbook derivation.
9. Status wording comes from Tier-A ledgers before Tier-B derivation files if the two differ.
10. Include a build/reproduction check for new mathematics when practical.
11. Preserve the exact AI-provenance nomenclature from `AI_PROVENANCE.md` / `PROVENANCE_TIERS.yaml`; agents may apply headers but may not assign or elevate tiers on their own.

## Style

Start from the object being manipulated, derive the relevant transform or identity, explain the interpretation, and finish by naming the exact UBT file/claim/gap to which it connects. The intended reader should not need to know in advance which pieces are Riemann, Jacobi, Poisson, Feynman, or UBT-specific.
