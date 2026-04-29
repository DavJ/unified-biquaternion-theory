<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# alpha_hidden_fit_audit.md — Hidden-Fit Audit for Alpha Derivation

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Track**: T2_ALPHA — Fine Structure Constant  
**Purpose**: Trace every constant factor and every assumed input in the
three active alpha routes. Identify hidden assumptions. Downgrade any weak
claims to honest conditional status.

---

## Audit Standard

A derivation is **fit-free** if and only if:

| Criterion | Requirement |
|-----------|------------|
| F1 | No constant in the derivation is chosen to reproduce α or 137 |
| F2 | Every numerical input is independently derived from UBT algebra or cited external theorem |
| F3 | Every claimed equality is proved (not "numerically close") or explicitly conditional |
| F4 | Every assumption is listed; none is hidden inside notation |

Anything that violates F1–F4 is a **hidden fit** and must be downgraded.

---

## Shared Foundation Audit

### N_eff = 12

| Input | Value | Source | Hidden fit? |
|-------|-------|--------|-------------|
| dim_ℝ(ℂ⊗ℍ) | 8 | Definition of biquaternion algebra | ✅ No |
| dim_ℝ(Im ℍ) | 3 | Definition of quaternion imaginary part | ✅ No |
| Phase modes | 1 | U(1) phase of ℂ factor | ✅ No |
| **N_eff = 12** | 8+3+1 | Algebraic counting | ✅ No — exact identity |

**Verdict**: N_eff = 12 is **completely fit-free**. No hidden assumption.

---

### V_eff(n) = n² − B·n·ln(n)

| Input | Value | Source | Hidden fit? |
|-------|-------|--------|-------------|
| One-loop structure n²·(logarithm) | Standard one-loop | Coleman-Weinberg / heat kernel on S¹ | ✅ No — standard QFT |
| Exponent 3/2 in one-loop | 3/2 | Heat kernel on Im ℍ ≅ ℝ³ [L0] | ✅ No — exact derivation |
| Overall form n² − B·n·ln(n) | Functional form | One-loop effective potential | ✅ No — standard |
| **B is free** | ? | Not yet derived from S[Θ] | ⚠️ B is the unknown — not yet a hidden fit, but not yet a derivation |

**Verdict**: The V_eff form is fit-free; the value of B remains open (Gap G137-B). No parameter is fitted to α; B is an unknown to be derived.

---

### B₀ = 8π

| Input | Value | Source | Hidden fit? |
|-------|-------|--------|-------------|
| N_eff = 12 | 12 | Algebraic [L0] | ✅ No |
| One-loop kinetic integral | 2π/N_eff × 48 = 8π | Gaussian integral on S¹_ψ | ✅ No |
| **B₀ = 8π** | ≈ 25.13 | Closed-form computation | ✅ No — exact |

**Verdict**: B₀ = 8π is **completely fit-free**. No hidden assumption.

---

## Route A Audit — Modular-Hecke

### Step A3: Kac-Moody level k

| Claim | Assumed value | Derived or assumed? | Fit risk |
|-------|--------------|---------------------|---------|
| k = 1 from WZW boundary | k = 1 | **Not yet derived** — Gap A-1 | ⚠️ POTENTIAL HIDDEN FIT if k is chosen to give correct answer |

**Required action**: Compute k from first principles. If k = 1 is assumed to match B_phenom, this is a hidden fit. The WZW boundary computation must precede any claim.

### Step A4: Hecke L-function match

| Claim | Value | Derived or assumed? | Fit risk |
|-------|-------|---------------------|---------|
| B = μ(Γ₀(137))/3 | 46.00 | Mathematical fact — μ(Γ₀(137)) = 138 is exact | ✅ No hidden fit in the computation |
| Identification of B_phenom with μ(Γ₀(n*))/3 | — | **Not proved** — only 0.64% numerical match | ⚠️ POTENTIAL HIDDEN FIT: the identification is currently a numerical coincidence, not a theorem |

**Required action**: Either prove the identification from S[Θ] dynamics, or label it as "numerical coincidence / supporting evidence" only.

**Route A hidden fit assessment**: No confirmed hidden fit, but two unproved steps that carry hidden-fit risk if treated as equalities rather than as open questions. Route A is honest as long as these are labeled OPEN.

---

## Route B Audit — V_eff Spectral (PRIMARY)

### Gap G137-B: B_phenom ≈ 46.298

| Claim | Value | Derived or assumed? | Fit risk |
|-------|-------|---------------------|---------|
| B_phenom ≈ 46.298 used in n*(B) = 137 | 46.298 | **Taken from experiment (α⁻¹ = 137)** | 🔴 CONFIRMED HIDDEN FIT in the conditional claim |
| n*(B₀) ≈ 65 (proved, no fitting) | 65 | Computed from B₀ = 8π | ✅ No hidden fit |

**Explanation of the hidden fit**: The claim "n*(B_phenom) = 137 where B_phenom = 46.298" currently uses B_phenom derived by inverting the V_eff equation: B_phenom = solution of n*(B) = 137. This is circular at the level of a complete derivation. The claim is honestly labeled CONDITIONAL on Gap G137-B in all current documents. **This is not a hidden fit in the claim — it is an explicit condition stated in the document.** The risk arises only if B_phenom is claimed as "derived" without closing Gap G137-B.

**Verdict**: Route B's primary claim is **not a hidden fit** because the condition (B = B_phenom assumed) is explicitly stated. However, it must remain labeled CONDITIONAL until Gap G137-B is closed.

**Action**: Do not promote n*(B_phenom) = 137 to PROVED until B_phenom is independently derived.

### Corroborations (supporting, not proofs)

| Corroboration | Exact or numerical? | Hidden fit risk? |
|---------------|--------------------|--------------------|
| μ(Γ₀(137))/3 ≈ 46.00 | Exact math; 0.64% numerical agreement | Low — agreement not used as proof |
| Hecke eigenvalue → lepton mass ratios 0.02–0.1% | Numerical | Low — labeled as corroboration |
| P¹(𝔽₁₃₇) cardinality = μ(Γ₀(137)) | Exact identity | ✅ No risk — exact theorem |

**Verdict**: Corroborations are correctly labeled as supporting evidence, not proofs. No hidden fits.

---

## Route C Audit — EW/GUT Bridge

### Step C1: GUT embedding

| Claim | Assumed | Source | Fit risk |
|-------|---------|--------|---------|
| SU(5) ⊃ ℂ⊗ℍ | Not proved — Gap C-1 | — | ⚠️ If assumed without proof, this is a hidden structural fit |

### Step C2: sin²θ_W(GUT) = 3/8

| Claim | Value | Source | Fit risk |
|-------|-------|--------|---------|
| sin²θ_W = 3/8 at GUT scale | 3/8 = 0.375 | Standard SU(5) normalization | ✅ No fit — exact result for SU(5) |

### Step C3: RG running

| Claim | Value | Source | Fit risk |
|-------|-------|--------|---------|
| SM β-functions | Standard | Standard Model | ✅ No fit — external input (SM) |
| SM particle content | 3 generations + Higgs | Standard | ✅ No fit |

### Step C4: α extraction

| Claim | Value | Source | Fit risk |
|-------|-------|--------|---------|
| e = g sin θ_W | Identity | Standard EW | ✅ No fit |
| α(M_Z) ≈ 1/128 | Numerical | RG running from GUT scale | ✅ No fit (given GUT embedding) |
| **α(0) ≈ 1/137** | 1/137.036 | QED running | ✅ No fit (given above) |

**Route C hidden fit assessment**: No confirmed hidden fit in the standard GUT machinery (Steps C2–C4). The critical gap is Step C1 (GUT embedding): if the SU(5) embedding is assumed without proof from UBT algebra, it is a structural assumption, not a fit for α. However, accepting the SM + GUT framework as input weakens the claim that α is derived from UBT; it becomes "α derived from GUT + UBT algebra."

**Verdict**: Route C's derivation of α is fit-free in the GUT sector but requires an unproved GUT embedding. Honest status: CONDITIONAL on Gap C-1 and Gap G-strong.

---

## Summary: Hidden Fit Inventory

| Route | Hidden fits found | Explicit conditions | Honest status |
|-------|------------------|--------------------|-|
| Shared foundation | **None** | None needed | ✅ Fit-free |
| Route A | Potential (Gap A-1, A-2) | Must remain OPEN | OPEN — no fit if gaps labeled honestly |
| Route B | B_phenom circular at face value | Explicitly CONDITIONAL on G137-B | ✅ Honest |
| Route C | GUT embedding assumed | CONDITIONAL on C-1 + G-strong | ✅ Honest if labeled |

**No currently confirmed hidden fits in the published claim set.**  
All known circular dependencies are explicitly labeled as open gaps or conditional claims.

---

## Mandatory Downgrade Actions

| Claim | Current label | Required label |
|-------|--------------|----------------|
| "n*(B_phenom) = 137 is proved" | CONDITIONAL in docs | ✅ Already CONDITIONAL — no action needed |
| "B = μ(Γ₀(137))/3" (Route A) | Open claim | Must remain OPEN or CORROBORATION until proved |
| "GUT embedding of ℂ⊗ℍ exists" | Gap C-1 | Must remain GAP — do not use as a premise |
| "Kac-Moody level k = 1" | Uncomputed | Must be computed before use in Route A |

---

## Constants Requiring Tracing at Next Stage

When Gap G137-B is attacked, the following constants must be traced:

| Constant | Expected source | Status |
|----------|----------------|--------|
| B_phenom ≈ 46.298 | S[Θ] two-loop + Kac-Moody | Gap G137-B — OPEN |
| Missing factor 1.84 = B_phenom / B₀ | Higher-loop correction | OPEN |
| μ(Γ₀(137)) = 138 | Exact group-index formula | ✅ Derived (external theorem) |
| Kac-Moody level k | WZW boundary term | Gap A-1 — OPEN |
| L(1, f₁₃₇) | Hecke L-function | Gap A-2 — OPEN |

---

## References

- `canonical/alpha/alpha_equation_matrix.tex` — route equation chains
- `canonical/alpha/alpha_route_scoreboard.md` — route scores
- `canonical/alpha/ALPHA_MASTER_STATUS.md` — master status
- `reports/alpha_no_fit_audit.md` — prior audit (complement to this document)
- `reports/alpha_missing_lemma.md` — Gap G137-B exact statement
