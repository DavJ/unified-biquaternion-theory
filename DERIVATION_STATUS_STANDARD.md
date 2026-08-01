<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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


# DERIVATION_STATUS_STANDARD.md — Canonical Proof Level System

**Author**: Ing. David Jaroš  
**Date**: 2026-05-13  
**Purpose**: Single authoritative definition of every proof / evidence label
used in UBT documents.  Every claim in every active file must carry exactly
one label from this system.  
**Truth anchor**: `STATUS_OF_UBT.md`

> **Governance rule**: No alternative labelling scheme is permitted in active
> documents.  Historic files that use different labels are marked SUPERSEDED.

---

## Canonical Derivation Levels

| Level | Short name | Meaning |
|-------|-----------|---------|
| **[L0]** | Exact algebraic | Exact derivation from the definition of ℂ⊗ℍ alone. No empirical input. No axioms beyond the algebra. Reproducible by any reader given the definitions. |
| **[L1]** | Proved theorem | Derivation from stated UBT axioms (AXIOM-B, AXIOM-F, admissibility condition) plus standard mathematics. May include one explicitly named assumption or closure condition. Every step is traceable to a canonical source file. |
| **[L2]** | Numerical / structural | Numerical evidence, structural consistency, or strong structural signal. Not a formal proof. Must cite a reproducible script or explicit structural argument. |
| **[L3]** | Conjectural route | Plausible derivation path identified. No proof yet. All assumptions stated. Testable in principle. |
| **[L4]** | Speculative idea | Exploratory concept. No derivation, may lack a testable prediction. |
| **[DEAD]** | Failed route | Investigated route that has been proved impossible or has failed exhaustive search. Archive citation required. Revival requires new evidence not present at time of closure. |
| **[OPEN]** | Unresolved problem | Problem with no accepted derivation. Not a failed attempt — the route has not yet been tried or is known to be hard. |
| **[AX]** | Axiom / postulate | A stated assumption. Not derived, not expected to be derived at this stage. Clearly marked as an input to the theory. |
| **[STD]** | Standard result | A result from established mathematics or physics, not novel. Citation required. |
| **[NUM]** | Numerically verified | A statement verified by a reproducible computational script. Must cite the script. |
| **[MC]** | Motivated conjecture | A statement that has a strong physical or structural motivation but no formal proof. Distinct from [L3] in that the motivation is explicit and detailed. |
| **[SE]** | Semi-empirical | A result that uses at least one empirical number as input. Stated explicitly to prevent circularity. |
| **[COND]** | Conditional | A result that is correct only if another unproved statement holds. The dependency must be named. |

---

## Usage Rules

1. **One label per claim.** Do not attach two labels to the same claim.
   Exception: compound labels are allowed where both apply, e.g. [L1]+[NUM]
   means a proved result that is also numerically confirmed.

2. **Hype labels are forbidden.** The following words **must not** be used
   as proof-status labels in active documents:

   | Forbidden word | Replacement |
   |---------------|-------------|
   | breakthrough | Use [L1] or [L2] with honest description |
   | nearly solved | Use [L3] with explicit blocker |
   | revolutionary | Not a proof level; remove entirely |
   | solved | Replace with [L0], [L1], or [L2] as appropriate |
   | proven (informal) | Replace with [L1] PROVED + source citation |

3. **Scope creep guard.** A claim may not be promoted from [L3] to [L1]
   without a source file containing the proof.

4. **Dead routes stay dead.** A route labelled [DEAD] may only be reopened
   if a materially new argument — not present at closure — is identified.
   The reopening requires an explicit note in `reports/contradictions_resolved.md`.

5. **Axioms are not proofs.** A claim labelled [AX] does not become [L1]
   simply by being embedded in a longer derivation.  If a claim depends on
   an axiom, the axiom dependency must be stated.

6. **Conditional results.** Any claim labelled [COND] must name the unproved
   prerequisite.  Example: "[L1] conditional on Gap G137-B".

---

## Level Hierarchy for Paper Claims

When writing a paper or formal document, use this hierarchy to decide how
to state a claim:

```
Provable without fitting → [L0] or [L1]        → state as theorem
Numerical confirmation   → [L1]+[NUM]           → state as theorem + verified
Conditional result       → [L1][COND: gap-name] → state with explicit assumption
Open problem             → [OPEN] or [L2]        → state as open problem
Dead end                 → [DEAD]                → state as dead end explicitly
```

---

## Applied Examples

| Example claim | Correct level | Why |
|--------------|--------------|-----|
| ℂ⊗ℍ ≅ Mat(2,ℂ) | [L0] | Pure algebra from definitions |
| g_μν derived from Θ (Theorem 3.1) | [L1] | Requires AXIOM-B + AXIOM-F |
| Lorentzian signature from AXIOM-B | [L1] | Requires complex-time axiom |
| Schwarzschild metric to 10⁻¹⁵ error | [L1]+[NUM] | Proved analytically, confirmed numerically |
| α⁻¹_bare = 137 (integer) given B_phenom | [L1][COND: G137-B] | Proved given B; B not yet derived |
| N_eff = 12 is a motivated mode-counting candidate, currently OPEN/[MC]. | OPEN/[MC] | `canonical/n_eff/step2_AUDIT.tex` |
| Weinberg angle sin²θ_W from UBT | [DEAD for pure algebra; OPEN/COND for EW-1b] | No-go for pure algebra: algebra cannot fix g'/g; EW-1b branch remains conditional |
| Fermion mass hierarchy | [OPEN] | Hard; known obstruction (KK mismatch) |
| Zerilli equation (GAP-Z) | PROVED [L1] | Canonical proof in `canonical/gr_closure/zerilli_derivation.tex` and GR paper. Both graviton polarisation sectors are now closed at [L1]. |
| Dark sector p-adic extension | [L3] | Route identified; not attempted |
| Consciousness / psychons | [L4] | Speculative; frozen in speculative_extensions/ |

---

## Source Files Applying This Standard

| Track | Master status file |
|-------|--------------------|
| T1_GR | `reports/GR_REVIEW_MASTER.md`, `reports/GR_claim_to_proof_matrix.md` |
| T2_GAUGE | `canonical/gauge/GAUGE_MASTER_STATUS.md` |
| T3_ALPHA | `canonical/alpha/ALPHA_PORTFOLIO_MASTER.md` |
| Cross-track | `CLAIMS_MATRIX.md` |

---

## Version History

| Date | Change |
|------|--------|
| 2026-04-29 | Initial creation — replaces ad-hoc labelling across all active documents |
