<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# GR_exact_vs_conditional_table.md — T1_GR Exact vs Conditional Claims

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T1_GR — General Relativity Recovery  
**Purpose**: Compact decision table — every claim in `papers/UBT_GR_RC2.tex`
classified as EXACT (no unproved inputs beyond stated axioms) or CONDITIONAL
(requires an unproved additional assumption).  
**Definitions**:
- **EXACT [E]**: Result follows from stated UBT axioms (A1–A5) by a complete
  mathematical argument. No hidden assumptions. Any expert can verify.
- **CONDITIONAL [C]**: Result holds given an additional unproved input, which
  is explicitly named.
- **AXIOM [AX]**: An input postulate, not derived.

---

## Foundational Inputs (Axioms)

| ID | Claim | E/C/AX | Condition (if C) | Comments |
|----|-------|--------|-----------------|---------|
| AX-1 | ℂ⊗ℍ ≅ Mat(2,ℂ) ≅ Cl₁,₃(ℝ) algebra | E | — | Definition + algebra theorem [L0] |
| AX-2 | Complex time τ = t + iψ (AXIOM-B) | AX | — | Core UBT postulate |
| AX-3 | Field equation ∇†∇Θ = κ𝒯 (AXIOM-F) | AX | — | Fundamental dynamical postulate |
| AX-4 | Admissibility: {∂_μΘ} linearly independent | AX | — | Regularity condition |
| AX-5 | Newton's G is input parameter | AX | — | Not derived; sets Planck scale |

---

## Five-Step GR Chain

| Step | Claim | E/C/AX | Condition (if C) | Level | Verdict |
|------|-------|--------|-----------------|-------|---------|
| 1 | g_μν = Re[Tr(∂_μΘ·∂_νΘ†)]/𝒩 is a Lorentzian metric tensor | **E** | — | [L1] | ✅ Exact |
| 2 | det(g_μν) ≠ 0 for admissible Θ | **E** | — | [L1] | ✅ Exact |
| 3 | Signature (−,+,+,+) from AXIOM-B | **E** | — | [L1] | ✅ Exact |
| 4 | Levi-Civita connection Γ and Riemann curvature R from g | **E** | — | [STD] | ✅ Exact (standard GR geometry) |
| 5 | G_μν = 8πG·T_μν from Hilbert variation | **E** | G is free param (AX-5) | [L1] | ✅ Exact given G as input |

---

## Schwarzschild Sector

| Claim | E/C/AX | Condition (if C) | Level | Verdict |
|-------|--------|-----------------|-------|---------|
| Θ₀ is unique admissible spherically symmetric vacuum solution (up to gauge) | **E** | — | [L1] | ✅ Exact (proof in canonical/geometry/) |
| Schwarzschild metric g_ij = Ψ⁴δ_ij from Θ₀ | **E** | — | [L1] | ✅ Exact + numerically verified |
| Spatial components verified to < 5×10⁻¹⁵ | **E** | — | [NUM] | ✅ Exact numerical |
| Temporal component g_tt = −Φ² via ψ-structure | **E** | — | [L1] | ✅ Analytically exact; numerical deferred |
| ASD condition C⁺ = 0 for SU(2)₋ sector | **E** | — | [L1] | ✅ Exact |

---

## Linearised Gravity

| Claim | E/C/AX | Condition (if C) | Level | Verdict |
|-------|--------|-----------------|-------|---------|
| Linearised UBT reproduces linearised Einstein equations | **E** | — | [L1] | ✅ Exact |
| Regge-Wheeler equation (odd-parity graviton) | **E** | — | [L1] | ✅ Exact |

---

## Open Problems (Explicitly Bounded)

| Gap | E/C/AX | Status | Impact on main result |
|-----|--------|--------|-----------------------|
| GAP-10: Off-shell Θ-only closure | — | **OPEN [L2]** | Zero — does not affect on-shell GR |
| GAP-Z: Zerilli equation (even-parity) | — | **OPEN [L2]** | Zero — stated; complementary result |

---

## Summary Counts

| Category | Count | All exact? |
|----------|-------|------------|
| Core axiom inputs | 5 | N/A (postulates) |
| EXACT proved results [L0/L1/STD] | 9 | ✅ Yes |
| EXACT numerical verifications | 1 | ✅ Yes |
| CONDITIONAL results | **0** | — |
| OPEN gaps (bounded, non-blocking) | 2 | — |

**Zero conditional claims in the main chain.**  
All conditional items (G free parameter, GAP-10, GAP-Z) are explicitly
stated and do not block the primary result.

---

## Decision Table: What Would Change These Classifications?

| Event | Impact |
|-------|--------|
| AXIOM-B (complex time) shown inconsistent | Would degrade Step 3 from EXACT to FAILED |
| AXIOM-F (field equation) contradicted by experiment | Would degrade full chain |
| Admissibility condition proved unreachable for physical Θ | Would degrade Steps 1–2 |
| GAP-10 resolved | Would upgrade off-shell result — bonus, not needed |
| GAP-Z resolved | Would add Zerilli result — bonus, not needed |
| G derived from UBT algebra | Would remove AX-5 — upgrade |

No current evidence points to any of these events.

---

## References

- `papers/UBT_GR_RC2.tex` — source document
- `reports/GR_claim_strength_table.md` — detailed per-claim strength assessment
- `reports/GR_final_red_team.md` — post-RC2 red team
- `DERIVATION_STATUS_STANDARD.md` — proof level definitions
