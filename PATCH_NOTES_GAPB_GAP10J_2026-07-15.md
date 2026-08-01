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

# GAP-B conditional closure + GAP-10J operationalization — 15 July 2026

## 1. GAP-B: CLOSED CONDITIONALLY (new result)

**NEW `canonical/gr_closure/linearised_fiber_closure.tex`** — the perturbation
bridge δ(∇†∇Θ)→δG_μν is DERIVED, not assumed: linearising the exact pure-Θ
vacuum equation ∇_ν(G^{μν}E_μ)=0 around a regular fiber-free stationary vacuum
background gives, via (i) Ḡ=0 from the local closure theorem (open condition ⇒
holds on a neighbourhood), (ii) the linearised contracted Bianchi identity
∇_νδG^{μν}=0, and (iii) the Gauss step ∇_νĒ_μ = B̄_{μν} (purely normal), the
normal equation δG^{μν}B̄_{μν}=0; fiber-free injectivity yields δG_{μν}=0.
RW/Zerilli then follow by the standard harmonic decomposition.
**Single remaining condition:** existence of a fiber-free stationary pure-Θ
representation of the Schwarzschild exterior — i.e., GAP-B is subsumed by
GAP-10R/GAP-U2Θ and carries no independent logical weight.
Compiles standalone: 0 errors.

Propagated to: paper abstract, Key Claims item 6, Open Problems (new GAP-B
paragraph in the gap box), Zerilli box, status tables ([L1 cond. (GAP-B→GAP-10R)]),
CLAIMS.yaml, CLAIMS_MATRIX.md. Paper compiles: 0 errors, 0 undefined citations.

## 2. GAP-10J: operationalized (no status change)

**NEW `tools/fiber_free_check.py`** — general fiber-freeness checker for any
finite-Fourier two-jet (tangents, ten second profiles, pairing H): computes
regularity, Lorentzian signature, and the closure rank. Self-tests reproduce
both closure-paper theorems numerically: explicit construction rank 10/10;
single ψ-section rank exactly 4/10. ALL SELF-TESTS PASS.

**NEW `research_tracks/gap_10j/gap_10j_status.md`** — finding: the canonical
kernel θ₃(τ) is spatially constant (not regular), so GAP-10J is not yet a
well-posed computation; definition-of-done specified; the checker makes it
mechanical once the family is written down.

## Status changes
- GAP-B: OPEN → CLOSED CONDITIONALLY (on GAP-10R representer).
- No other status values changed.
