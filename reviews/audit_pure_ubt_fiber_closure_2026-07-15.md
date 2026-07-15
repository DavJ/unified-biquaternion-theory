# Independent Audit: `canonical/gr_closure/pure_ubt_fiber_closure.tex`

| Field | Value |
|---|---|
| **Audit date** | 2026-07-15 |
| **Auditor** | Claude (Anthropic), independent verification session directed by the author |
| **Document version** | as of repo snapshot 2026-07-15 (post GAP-10 safe merge) |
| **Method** | Line-by-line proof reading; independent recomputation of key algebraic steps; Fourier-support analysis of the explicit jet construction |
| **Verdict** | **Central mathematics VERIFIED.** Closure ledger statuses are accurate and honest. Two scope caveats noted below (both already acknowledged in the document itself). |

---

## Verified items

**V1 — Scalar-part proposition.** Sc and Tr of a faithful 2×2 representation map
to ℂ, not 𝔹. Trivially correct; the raw-tensor/metric-channel distinction is a
genuine repair of older wording.

**V2 — Zero-mode uniqueness (Haar projection).** Translation invariance +
linearity + normalization on trigonometric polynomials forces the circle
average. Standard Fourier argument; proof correct as written.

**V3 — Local-normalization obstruction.** 𝒩(x) = |H(∂₀Θ,∂₀Θ)| forces g₀₀ = −1
on a timelike branch. Correct; this justifies the constant-𝒩₀ axiom and is
consistent with the AXIOMS.md convention.

**V4 — Exact first variation and full Euler–Lagrange equation.** The formula
δg = (2/𝒩₀)⟨E₍μ, ∂ν₎δΘ⟩ and the resulting
𝓕_Θ + (1/κ𝒩₀)∇_ν(𝓔^{μν}E_μ) = 0 verified, given pairing compatibility and the
stated boundary conditions.

**V5 — Vanishing of the tangential part (Gauss-formula step).** Independently
recomputed: from g = ⟨E,E⟩/𝒩₀ one has ⟨∂_μ∂_νΘ, E_λ⟩ = 𝒩₀ Γ_{λ,μν}
(Christoffel of the first kind), hence ⟨∇_νE_μ, E_λ⟩ = 𝒩₀(Γ_{λ,νμ} − Γ_{λ,νμ}) = 0
and B_{μν} := ∇_νE_μ is purely normal. The reduction of the E–L equation to the
normal closure equation 𝓔^{μν}B_{μν} = 0 (given 𝓕_Θ = 0 and Bianchi/Noether) is
therefore exact, not approximate.

**V6 — Single-section rank no-go.** dim𝔹 = 8, tangent span 4 ⇒ normal space ≤ 4
⇒ rank 𝒦 ≤ 4 < 10. Correct rank–nullity; this quantitatively confirms the
July 2026 external audit's dimensional concern and honestly DISPROVES the
single-section closure route.

**V7 — Explicit fiber-free holomorphic jet (existence).** The construction with
φ_m(τ) = exp(mτ/R_ψ) was checked in detail:
(a) periodicity in ψ holds for integer m; holomorphy in τ holds;
(b) conj(φ_a)φ_b has ψ-average zero for a ≠ b — pairwise disjoint Fourier
supports ⇒ the stated orthogonalities hold after fiber averaging;
(c) f'' is not proportional to f' for a two-frequency profile (distinct
frequencies scale differently under d/dτ) ⇒ P_⊥f'' ≠ 0, and likewise for each
P_⊥g_i';
(d) the ten normal vectors carry pairwise disjoint (direction × frequency)
supports ⇒ linear independence.
The existence theorem is correct as written.

**V8 — Finite-mode genericity.** Polynomial-minor argument valid; the explicit
construction witnesses a nonzero minor, so the complement lies in a proper
algebraic set. Correct, with scope honestly limited by the document's own
remark (no infinite-dimensional density claim).

**V9 — Closure ledger.** Every row checked against the body of the document.
Statuses (PROVED / DISPROVED / PROVED CONDITIONALLY / OPEN) accurately reflect
what is proved. No overclaim found.

---

## Caveats (both already acknowledged in the document; recorded here for the
status surfaces)

**C1 — Kinematic vs. dynamical fiber-freeness.** The genericity theorem is a
statement about jet spaces, not about solutions. Existence of *stationary*
fiber-free configurations (i.e., that the dynamically selected solution family
intersects the fiber-free locus) is exactly GAP-10J and remains open. The
vacuum closure theorem is therefore of the form "fiber-free stationary ⇒
Einstein", with the antecedent's non-vacuity at solution level still to be
established.

**C2 — Realization of specific geometries.** Pointwise Gram representability
does not give integrable on-shell representation of a prescribed metric field
(GAP-10R, open). In particular, the closure theorem does not yet by itself
re-derive the Schwarzschild exterior within the pure-Θ framework; the temporal
sector remains governed by the GAP-U2Θ split.

---

## Cross-consistency notes fixed in this patch

1. `research_tracks/gap_u2/gap_u2_lapse_mechanism.md` referenced a nonexistent
   file `derive_connection_equation.tex`; the reference is replaced by an
   explicit open-task note.
2. Gap naming: the paper's remaining bare "GAP-U2" mentions are aligned with
   the CLAIMS.yaml taxonomy (GAP-U2Θ for the Θ-dynamics question); see patch
   notes.

*Prepared with Claude's assistance under the author's direction; all
verification computations are reproducible from the descriptions above.*
