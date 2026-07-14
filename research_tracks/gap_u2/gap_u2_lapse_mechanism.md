# GAP-U2: Mechanism Identified — the Schwarzschild Lapse as a Covariantly Harmonic U(1)_ψ Potential

**Status: OPEN — mechanism identified; closure reduces to GAP-U1 (bilinear normalization).** Date: 2026-07-15. Verified symbolically (SymPy, exact); script: `tools/verify_gap_u2_lapse.py`.

## Result 1 (No-go for the phase ansatz, flat operator)

For the ψ-extended phase ansatz Θ(r,ψ) = e^{iΦ(r)ψ}[f(r)·1 + g(r)·e_r] with the Theorem-4.1 functions (Ψ = 1+M/2r, g = rΨ², f' = Ψ√(2M/r), Φ = (1−M/2r)/(1+M/2r)), the flat vacuum equation (±∂_ψ² + ∇²)Θ = 0 fails at orders ψ¹ and ψ² for both sign conventions; the ψ² coefficient is proportional to M^{5/2}(M−2r)·Φ'² and vanishes only at r = M/2. Additionally, on compact ψ ∈ S¹, single-valuedness of e^{iΦ(r)ψ} requires Φ(r)·R_ψ ∈ ℤ, impossible for continuous non-constant Φ. **Conclusion: the relation ∂_ψΘ = iΦ(r)Θ with non-constant Φ is not realizable as a field phase in the flat theory — neither dynamically nor topologically.**

## Result 2 (Connection mechanism)

Let the ψ-sector enter through the U(1)_ψ connection already present in UBT (the U(1) of the ψ-phase / right action; cf. Q ∈ ℤ from U(1)_EM holonomy on S¹_ψ): D_ψΘ = ∂_ψΘ + iqA_ψ(r)Θ. For static single-valued Θ (∂_ψΘ = 0), D_ψΘ = iqA_ψΘ reproduces the required structure with Φ := qA_ψ, with no multivalued phase — the topological obstruction of Result 1 does not arise.

## Result 3 (Exact derivation of Φ — the central result)

The vacuum field equation for A_ψ(r) on the UBT-induced spatial metric g_ij = Ψ⁴δ_ij is the covariant Laplace equation (1/√g)∂_i(√g g^{ij}∂_j A_ψ) = 0, which in the radial sector reads ∂_r(r²Ψ² A_ψ') = 0. Since r²Ψ² = (r + M/2)² exactly, the general solution is A_ψ = D − C/(r + M/2). With boundary condition A_ψ(∞) = 1 and C = M: A_ψ(r) = 1 − M/(r + M/2) ≡ (1 − M/2r)/(1 + M/2r) = Φ(r) — an exact identity, verified symbolically. Equivalently: covariant_Laplace[Φ] = 0 exactly on g_ij = Ψ⁴δ_ij. **Conclusion: the Schwarzschild lapse is the unique covariantly harmonic U(1)_ψ potential on the UBT-induced spatial geometry with unit boundary value and charge M. The relation D_ψΘ₀ = iΦΘ₀ is thereby mechanistically derived, not imposed.**

## Remaining step (why GAP-U2 stays OPEN)

g_tt = −|D_ψΘ₀|²/𝒩 = −q²A_ψ²|Θ₀|²/𝒩 equals −Φ² iff q²|Θ₀|²/𝒩 = 1. Since |Θ₀|² = f² + g² is not constant, closure requires the precise specification of the bilinear ⟨·,·⟩ and normalization 𝒩 — i.e., GAP-U1. GAP-U2 closure is hereby reduced to GAP-U1.

## GR interpretation (credibility note)

A harmonic lapse on spatial slices is a known structure (isotropic coordinates / maximal-slicing-type conditions in GR). The UBT-specific content is the *reason*: the harmonicity is the vacuum Maxwell equation of the ψ-sector connection on the induced geometry.
