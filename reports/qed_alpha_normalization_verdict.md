<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# qed_alpha_normalization_verdict.md

**Task**: `fix_or_reject_U1_coupling_normalization` — Target 5  
**Priority**: CRITICAL  
**Mode**: physics-first, no numerology  
**Date**: 2026-05-10

---

## Final classification

$$\boxed{\textbf{FREE\_NORMALIZATION}}$$

The current UBT formulation **does not fix** the numerical value of the fine
structure constant α from first principles.

---

## Derivation chain status

| Step | Element | Status |
|---|---|---|
| 0 | Canonical action S[Θ] | DERIVED |
| 1 | U(1) identification in biquaternion algebra | DERIVED |
| 2 | Generator normalization Tr(T²) = 1/2 | DERIVED |
| 3 | Unit charge q_Θ = 1 | DERIVED |
| 4 | Integer charge quantization (unit flux convention) | CONDITIONAL |
| 5 | Parent coupling e₅ | **NO-GO** |
| 6 | Compact radius R_ψ | **NO-GO** |
| 7 | 4D coupling e₄² = e₅²/(2π R_ψ) | CONDITIONAL (blocked by 5,6) |
| 8 | α = e₄²/(4π) | **NO-GO** (blocked by 5,6) |

---

## Key findings from each target

### Target 1 — U(1) generator normalization: CONDITIONAL
- The U(1)_EM generator is identified as the right-phase action in
  Mat(2,ℂ), giving `T_EM = (1/2)I₂`.
- Trace normalization `Tr(T_EM²) = 1/2` is algebraically derived.
- Unit charge `q_Θ = 1` follows from the right-phase action period.
- The physical electron charge `e = g sin θ_W` is conditional on the
  Weinberg angle, which is not derived from the algebra alone.
- **Verdict: CONDITIONAL** (generator derived; absolute coupling conditional).

### Target 2 — R_ψ scale fixing: NO-GO
- The spectral free energy fixes the shape modulus `R_t/R_ψ = 1`
  (conditionally, under isotropic normalization).
- The scale modulus `√(R_t R_ψ)` is a flat direction in all examined
  potentials — no equation from S[Θ] fixes it.
- T-duality and modular covariance do not fix the absolute volume.
- **Verdict: NO-GO** (absolute R_ψ is free).

### Target 3 — Parent coupling e₅: NO-GO
- e₅ can always be absorbed by field rescaling `𝒜_M = e₅ A_M`, making
  the action e₅-independent.
- No topological condition (Chern class, holonomy, flux quantization)
  fixes e₅ independently of an unconstrained flux modulus.
- **Verdict: NO-GO** (e₅ is a pure normalization convention).

### Target 4 — Charge quantization: CONDITIONAL
- Single-valuedness of Θ on S¹_ψ forces integer charges in units of q_Θ = 1,
  given the standard flux normalization Φ₀ = 2π.
- Quark fractional charges (2/3, −1/3) require SM hypercharge assignments
  not derived from the biquaternion algebra.
- **Verdict: CONDITIONAL** (integer quantization follows from topology;
  fractional charges are external input).

---

## Free parameters remaining

| Parameter | Status |
|---|---|
| e₅ (5D parent coupling) | Free — field rescaling removes it |
| R_ψ (compact radius) | Free — scale modulus is flat |
| θ_W (Weinberg angle) | Free — not fixed by algebra |
| Y (hypercharge assignments) | Free — SM input |

Minimum inputs needed to fix α: the product `e₅²/(2π R_ψ)` (equivalently, e₄
directly), plus the Weinberg angle.

---

## Post-derivation consistency check only

After deriving the RG direction (α⁻¹ decreasing with μ), comparison with
known checkpoints:

- α⁻¹(m_e) ≈ 137.036 — consistent with RG trajectory direction.
- α⁻¹(M_Z) ≈ 127.9 — consistent with RG trajectory direction.

These are **OBSERVED CONSISTENCY** only, not derivation.

---

## Mandatory final sentence

> **"Alpha remains a free normalization in the current UBT formulation."**

---

## Next possible route if α remains free

The most direct path to fixing α would require **either**:

1. A gravitational-electromagnetic unification condition that relates
   `e₅²` to the 5D gravitational coupling `G₅` and a fundamental length scale.
2. A dynamical potential for the compact moduli that breaks the
   `R_ψ → λ R_ψ` moduli symmetry and selects a specific vacuum value of R_ψ.
3. A topological quantization condition (e.g., from a compact internal
   manifold with quantized flux) that independently fixes the product
   `e₅²/(2π R_ψ)` without measured input.

None of these routes is currently available in the canonical UBT formulation.
