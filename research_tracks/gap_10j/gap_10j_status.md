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

# GAP-10J: Status and Operationalization (2026-07-15)

**Finding.** The canonical Jacobi kernel in the repository is the theta
*constant* θ₃(τ) = Σₙ exp(iπn²τ) (see `canonical/appendices/appendix_theta_spectrum.tex`),
a function of τ alone. A spatially constant field has E_i = ∂_iΘ = 0, hence a
degenerate tangent Gram — it is not even *regular*, so the fiber-free question
does not apply to the bare kernel. **GAP-10J is therefore not yet a well-posed
computation:** the "dynamically selected Jacobi sector" must first be pinned
down as an explicit x-dependent family Θ(x,ψ) (kernel × spatial modulation,
boundary conditions, and the selection principle).

**Operationalization.** `tools/fiber_free_check.py` provides a general checker:
given the finite-Fourier two-jet of ANY concrete ansatz (four tangent profiles,
ten second-derivative profiles, and the pairing matrix H), it computes the
tangent Gram (regularity + Lorentzian signature) and the rank of the ten
projected normal vectors B_μν. Self-tests reproduce both closure-paper
theorems numerically: the explicit holomorphic construction has rank 10/10
(fiber-free), a single ψ-section has rank exactly 4/10 (the theorem bound).

**Definition of done for GAP-10J:** (1) write the canonical Jacobi family as an
explicit two-jet at a representative point; (2) run the checker; (3) rank 10 →
GAP-10J closed at that configuration class; rank < 10 → documented obstruction
and the family must be enriched (more independent fiber modes) or the selection
principle revisited.

**Status: OPEN — now mechanically checkable once the family is specified.**
