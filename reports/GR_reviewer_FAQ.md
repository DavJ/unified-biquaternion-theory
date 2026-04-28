<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# GR_reviewer_FAQ.md — Frequently Asked Questions for Reviewers

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T1_GR — General Relativity Recovery  
**Purpose**: Concise Q&A for external readers and peer reviewers encountering
UBT for the first time.  Complementary to `GR_hostile_review.md` (technical
attacks) and `GR_reviewer_objections_and_answers.md` (detailed rebuttals).  
**Paper**: `papers/UBT_GR_Submission.tex`

---

## Quick-Start Questions

### Q1. What exactly does this paper claim?

The paper proves that standard General Relativity — including the metric tensor,
Lorentzian signature, Einstein field equations, Schwarzschild solution, and the
Regge-Wheeler equation for gravitational perturbations — all follow from a single
biquaternionic field **Θ(q,τ)** defined over complex time **τ = t + iψ**.

The key novelty: **the metric is derived**, not postulated.  Prior biquaternion
gravity papers (Adler 1995, Finkelstein 1962) assume or impose the metric.  UBT
derives it via the bilinear formula
g_μν = Re[Tr(∂_μΘ · ∂_νΘ†)] / 𝒩.

### Q2. What is biquaternion algebra (ℂ⊗ℍ)?

It is the algebra of complex quaternions: quaternions with complex (instead of
real) coefficients.  It is isomorphic to Mat(2,ℂ) and to the spacetime Clifford
algebra Cl₁,₃(ℝ).  This is an 8-real-dimensional algebra.  No exotic mathematics
is involved; the isomorphism ℂ⊗ℍ ≅ Cl₁,₃(ℝ) is a classical result (Porteous 1995).

### Q3. What does it mean that the metric is "derived"?

In standard GR, the metric g_μν is a postulated dynamical field, and the
signature (−,+,+,+) is separately assumed.

In UBT, the metric g_μν is computed from the fundamental field Θ via a trace
formula.  Lorentzian signature follows as a theorem from a single axiom
(AXIOM-B: ∂_τ lies in the timelike sector of Cl₁,₃(ℝ)).  The metric is
not a separate input.

### Q4. What are the three axioms?

| Axiom | Content |
|-------|---------|
| **AXIOM-A** | The algebraic structure is 𝔹 = ℂ⊗ℍ ≅ Cl₁,₃(ℝ) |
| **AXIOM-B** | Physical time is τ = t+iψ with ∂_τ timelike in Cl₁,₃ |
| **AXIOM-F** | The fundamental field Θ satisfies ∇†∇Θ = κ𝒯 |

These three replace the larger set of inputs of standard GR
(metric, signature, action, matter content, coordinate system).

### Q5. What is Newton's constant G in this framework?

Newton's constant G enters as an overall normalisation of the
Einstein-Hilbert action coefficient (16πG)⁻¹.  It is an input parameter
setting the Planck scale.  **This paper does not derive G from UBT** — that
is explicitly stated as out of scope.  G plays the same role here as in
standard GR.

---

## Questions About the Proof

### Q6. Is the derivation circular? Does AXIOM-B secretly assume the signature?

No.  AXIOM-B states that ∂_τ lies in the timelike sector of the
abstract Clifford algebra Cl₁,₃(ℝ).  This is one scalar inequality
(⟨∂_τ,∂_τ⟩_η < 0) in the algebraic structure, not an assumption about
the spacetime signature of g_μν.

The four eigenvalues of g_μν(x) are then shown to follow from the algebraic
structure of 𝔹, giving (−,+,+,+) as a theorem (Theorem 3.3, Appendix A).
See §3.3 and `reports/GR_hostile_review.md §H1–H2` for full details.

### Q7. Is the Schwarzschild ansatz reverse-engineered from the known answer?

No.  The ansatz Θ₀ = e^{iΦ(r)}[f(r)𝟏 + g(r)e_r] is derived as the most
general spherically symmetric, time-independent, asymptotically flat admissible
field configuration in 𝒜_UBT.  This uniqueness is proved.  The Schwarzschild
metric is then computed from Θ₀ without knowing the answer in advance.
Spatial components are verified numerically to < 10⁻¹⁵ as an independent check.

### Q8. Is the off-shell Θ→g map injective? What if many Θ give the same metric?

The off-shell global injectivity of Θ → g[Θ] is **not** claimed and is not
proved.  This is GAP-10, explicitly stated in §6 with a full obstruction map.
The paper proves the **on-shell** statement: for every admissible on-shell Θ
satisfying the Euler-Lagrange equation, the induced metric g[Θ] satisfies the
Einstein equations.  GAP-10 is an [L2] open problem that does not affect the
classical GR result.

### Q9. Why is the even-parity (Zerilli) graviton equation missing?

Deriving Zerilli requires handling the coupling between scalar and tensor
perturbation modes in the even-parity sector, which in turn requires
Chandrasekhar's two-potential transformation.  This has not yet been
implemented in the UBT even-parity Θ sector.  GAP-Z is explicitly stated
in §5 and §6.  It does not affect the main result (Steps 1–5 and Schwarzschild).
See `reports/GR_final_gap_checklist.md §GAP-Z` for the closing strategy.

---

## Questions About Scope and Claims

### Q10. Does this paper claim to quantise gravity?

No.  The paper establishes the **classical GR sector** of UBT.  Path-integral
quantisation (GAP-Q) is a long-term open problem, explicitly out of scope.

### Q11. Does this paper derive the Standard Model or fine structure constant?

No.  Those are separate tracks (T2_GAUGE, T3_ALPHA) treated in companion papers.
This paper is exclusively about the GR recovery.

### Q12. How does UBT relate to prior biquaternion gravity work?

The critical difference is the metric formula.  Prior biquaternion gravity
papers (Adler 1995, Finkelstein 1962, De Leo 1996) all postulate or impose
the metric.  UBT derives it via a bilinear trace formula.  Table 1 in §1 of
the paper provides an explicit comparison.

### Q13. What happens in the flat-space limit?

When Θ = const, the trace formula gives g_μν = η_μν (Minkowski metric).
UBT contains flat spacetime as a special case.

### Q14. Is there an arXiv version I can cite?

The paper is in final pre-submission state.  Submission to arXiv (gr-qc or
math-ph) is planned within days.  In the meantime, the commit history of
this public repository establishes the priority date.

---

## Questions About Open Problems

### Q15. What would it take to close GAP-10?

Prove that the kernel of the variation map J = δg^μν/δΘ consists only of
gauge directions (pure phase rotations or diffeomorphisms) for all Θ in the
full off-shell field space.  This requires either a global cohomology argument
(show H¹(M⁴, ker J) = 0) or a Sobolev fixed-point theorem.  Estimated effort:
4–8 weeks of specialist work.

### Q16. What would it take to close GAP-Z?

Implement Chandrasekhar's two-potential transformation in the UBT even-parity
sector.  Start from the even-parity linearised UBT field equation and show it
reduces to the Zerilli equation.  Estimated effort: 2–4 weeks.

---

## Navigation

| Question type | Go here |
|--------------|---------|
| Full claim-to-proof traceability | `reports/GR_claim_to_proof_matrix.md` |
| Technical hostile reviewer attacks | `reports/GR_hostile_review.md` |
| Detailed objection rebuttals | `reports/GR_reviewer_objections_and_answers.md` |
| Gap analysis | `reports/GR_final_gap_checklist.md` |
| The paper itself | `papers/UBT_GR_Submission.tex` |
| What is proved across all tracks | `WHAT_IS_PROVED.md` |
| Repository status | `STATUS.md` |
