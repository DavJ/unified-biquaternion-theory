<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# veff_extremum_audit.md — V_eff(n) Extremum Derivative Check

**Author**: Ing. David Jaroš  
**Date**: 2026-05-02  
**Track**: T3_ALPHA  
**Priority**: CRITICAL  
**Mode**: prove_or_break  
**Purpose**: Step-by-step derivative check for every V_eff variant found in the
repository, following the Alpha Critical Fix task specification.

---

## STEP 1 — All V_eff Variants Found in the Repository

Systematic search (grep for `V_eff`, `Veff`, `n\^2`, `B ln`, `B\,n\ln`) across
all `.tex`, `.md`, `.py`, `.sage` files produced the following distinct formulas
with an alpha-derivation role.

### V1 — Primary Canonical Form ✓

```
V_eff(n) = n² − B·n·ln n
```

**Sources**:
- `canonical/alpha/alpha_equation_matrix.tex` §2 (Thm. [L1])
- `canonical/alpha/alpha_best_route.tex` §6
- `canonical/alpha/neff_32_alpha_route.tex` §G5
- `canonical/alpha/veff_corrected_statement.tex` (2026-05-02)
- `canonical/alpha/veff_corrected.tex` (2026-05-02)
- `canonical/appendices/appendix_alpha_geometry.tex` §3 (corrected 2026-05-02)
- `ALPHA_PROGRESS_REPORT.md` §2.3 (corrected 2026-05-02)
- `docs/papers/papers/generated/ubt_action_and_alpha.tex` eq.(V_eff)

**Origin of A=1 coefficient**: KK winding energy $\hbar^2 n^2 / (2mR_\psi^2)$
in natural units ($\hbar=1$, $2m=1$, $R_\psi=1$). Unit choice, not a free parameter.

**Status**: PROVED [L1] (functional form); B is open.

### V2 — Legacy Code Variant

```python
def V_eff(n, A=1.0, B=20.3):
    return A * n**2 - B * n * np.log(n)
```

**Source**: `ARCHIVE/archive_legacy/tex/emergent_alpha_calculations.tex` §code block

**Note**: Same functional form as V1. **B=20.3 is misleading**: the script
restricts the prime search to p ∈ [100, 200], creating a false appearance that
B=20.3 selects p=137. The **global** prime minimiser for B=20.3 is p=47, not 137.
This must **not** be cited as evidence for the prime attractor.

### V3 — Non-Hermitian Mass Term (unrelated to α)

```
V_eff = (m² + iγ)·Tr[Θ†Θ],   γ ∈ ℝ
```

**Source**: `canonical/symmetry/step3_breaking_catalogue.tex` eq.(cat:V_eff)

This describes PT-symmetric open-system dynamics. **No role in the α derivation.**

### V4 — Erroneous Form (missing n factor)

```
V(n) = n² − B·ln n
```

This form appears **nowhere explicitly** in the repository as an intended formula,
but it is the **only form consistent with the stationarity claim n\* = √(B/2)**
that appeared in older documents. For B ≈ 46.3, √(B/2) ≈ 4.8, not 137.
This variant was a transcription error in:

- `canonical/appendices/appendix_alpha_geometry.tex` §3 (pre-2026-05-02) — **FIXED**
- `ALPHA_PROGRESS_REPORT.md` §2.3 header, §9 entry A7 (pre-2026-05-02) — **FIXED**

### V5 — Graviton Potential (unrelated to α)

Regge-Wheeler/Zerilli potential in `research_tracks/research/graviton_schwarzschild.tex`.
No connection to the fine-structure constant route.

---

## STEP 2 — Derivative Check (No Assumptions)

### 2.1 V1: V(n) = n² − B·n·ln n

```
d/dn [n²]         = 2n
d/dn [B·n·ln n]   = B·(ln n + n·(1/n))
                  = B·(ln n + 1)

dV/dn = 2n − B·(ln n + 1)
```

**Stationarity: dV/dn = 0**

```
2n* = B·(ln n* + 1)
```

This is a **transcendental equation** — no elementary closed form exists.

**Second derivative:**

```
d²V/dn² = 2 − B/n
```

At n*: `d²V/dn² = 2 − B/n* > 0  ⟺  n* > B/2`

For B ≈ 46.3 and n* = 137: 137 > 23.15 ✓ → confirmed **minimum**.

### 2.2 V4 (erroneous): V(n) = n² − B·ln n

```
d/dn [n²]       = 2n
d/dn [B·ln n]   = B/n

dV/dn = 2n − B/n
```

**Stationarity: dV/dn = 0**

```
2n² = B  ⟹  n* = √(B/2)
```

This **does** have a closed form: `n* = √(B/2)`.

For B = 46.298: n* = √(23.149) ≈ **4.81** — **nowhere near 137**.

---

## STEP 3 — Required B Values and Consistency Table

### Summary Table (all forms)

| V_eff form | dV/dn | Stationarity | n\* (continuous) | B required for n\*=137 |
|------------|-------|-------------|-----------------|------------------------|
| V1: `n² − B·n·ln n` | `2n − B(ln n + 1)` | `2n* = B(ln n*+1)` (transcendental) | 137.0 for B≈46.284 | `B = 274/(ln 137+1) ≈ 46.284` |
| V4: `n² − B·ln n` | `2n − B/n` | `n* = √(B/2)` (closed form) | ≈4.8 for B≈46.3 | `B = 2×137² = 37,538` |

### Numerical n\*(B) for V1

| B value | n\*_continuous | Prime minimiser | Classification |
|---------|---------------|-----------------|----------------|
| B₀ = 8π ≈ 25.133 | 65.0 | 67 | PROVED [L1] |
| B_base = N_eff^{3/2} ≈ 41.569 | 120.4 | 127 | CONJECTURAL [MC] |
| μ(Γ₀(137))/3 = 46.000 | 136.0 | 137 | EXACT MATH (index formula) |
| B_required = 46.284 | 137.000 | **137** | Exact constraint |
| B_phenom ≈ 46.298 | 137.05 | **137** | PHENOMENOLOGICAL |

---

## STEP 4 — First-Principles Reconstruction of V_eff

### Energy term (KK spectrum)

Classical KK winding energy on S¹_ψ:

```
E_n = ℏ²n²/(2mR_ψ²) = n²  (natural units, A=1)
```

**Source**: Standard Kaluza-Klein, `canonical/appendices/appendix_alpha_geometry.tex` §2.

### Entropy/degeneracy term

The one-loop Coleman-Weinberg (CW) effective potential from the functional
determinant of (−∇†∇) on the biquaternion field Θ:

```
S_CW(n) = −½ ln det(−∇†∇)|_n  ≈  (N_eff/2)·n·ln n  (large n)
```

**Why n·ln n, not ln n:**

- The heat kernel on S¹_ψ at winding number n contributes `ln(n/Λ)` per mode
  in the UV-regulated functional determinant.
- There are n distinct winding sub-sectors at level n (from the mode sum).
- Each of the N_eff = 12 charged modes contributes `n·ln(n/Λ)`.
- Summing and absorbing Λ into the renormalization scheme gives `B·n·ln n`
  with B = N_eff/2 × (numerical factor from the heat-kernel integral).

The form `ln n` (without the factor n) would arise from a winding-independent
functional determinant — inconsistent with the KK mode structure.

**Resulting V_eff:**

```
V_eff(n) = E_n − S_CW(n) = n² − B·n·ln n
```

Functional form: **DERIVED** from the one-loop CW calculation.
Coefficient B: **OPEN** (Gap G137-B).

### Entropy functional form classification

| Entropy form | Physical interpretation | Correct? |
|-------------|------------------------|----------|
| `ln n` | Winding-independent degeneracy | ✗ Inconsistent with KK mode sum |
| `n·ln n` | KK winding-mode degeneracy on S¹_ψ | ✓ **Correct** |
| `n·ln·n` (SUGRA) | Used in black hole entropy; unrelated here | ✗ Different context |

---

## STEP 5 — Coefficient B: Origin Classification

| B symbol | Value | Origin | Classification |
|----------|-------|--------|----------------|
| B₀ = 8π | 25.133 | One-loop vacuum polarisation, N_eff=12 on S¹_ψ | **DERIVED** [L1] |
| B_base = N_eff^{3/2} | 41.569 | Conditional on Kac-Moody level k=1 (Gap G3-k) | **CONJECTURAL** [MC] |
| μ(Γ₀(137))/3 | 46.000 | Exact group index formula; 0.64% from B_phenom | **EXACT MATH** [L0]; identification with B is **OPEN** |
| B_required | 46.284 | Back-solved from 2n\*=B(ln n\*+1) at n\*=137 | **EXACT CONSTRAINT**; circular if used as input |
| B_phenom | ≈46.298 | Back-solved from requiring n\*=137 | **PHENOMENOLOGICAL** (circular) |
| R-factor = B_phenom/B_base | ≈1.1134 | No derivation | **UNKNOWN/OPEN** (Gap G137-B) |

### What each contribution would need to produce B ≈ 46.284

To go from B₀ = 8π ≈ 25.13 to B_required ≈ 46.284:

- Missing factor: 46.284 / 25.133 ≈ **1.841**
- This factor must come from: higher-loop corrections, Kac-Moody structure,
  modular form special values, or spectral density of the θ-function

Candidates explored (all **rejected or unresolved**):

| Approach | Result | Status |
|----------|--------|--------|
| One-loop only (B₀ = 8π) | n\* ≈ 65, not 137 | Proved but insufficient |
| B_base = N_eff^{3/2} (k=1 KM) | n\* ≈ 120 | Conjectural; still short |
| Two-loop β-function | All dead-ended | DEAD END |
| Seeley-DeWitt curvature | Vanishes in UV | DEAD END |
| Instanton corrections | Require negative action | IMPOSSIBLE |
| μ(Γ₀(137))/3 = 46.00 | 0.64% from target | Supporting signal only |
| R = 1 + α(N_eff+π+1/4) ≈ 1.1123 | 0.15% error; uses α | CIRCULAR |

**Open Gap G137-B**: derive R ≈ 1.113 from S[Θ] without α as input.

---

## STEP 6 — Decision

### Is V_eff consistent?

**Yes.** The correct form V1 (`n² − B·n·ln n`) is:
- Derived from first principles
- Mathematically consistent
- The unique form compatible with the one-loop CW calculation on S¹_ψ

### Does the 137 extremum claim hold?

**Yes, conditionally.** For B ∈ [46.00, 46.50], the prime minimiser of V1 is p=137.
The stationarity condition is correct. The mathematics is internally consistent.

### Is B ≈ 46.3 derived or phenomenological?

**Phenomenological.** B_phenom is obtained by inverting the stationarity
condition with n\*=137 as input. This is circular by construction.
The nearest derived value is B₀ = 8π ≈ 25.13, which gives n\* ≈ 65.
The conjectural value B_base = N_eff^{3/2} ≈ 41.57 gives n\* ≈ 120.
Neither reaches 137 without an additional factor R ≈ 1.113 (Gap G137-B).

### Action

- Keep the alpha route (V1 is mathematically correct)
- Classify B as phenomenological and mark as target for derivation (Gap G137-B)
- Do **not** promote n\*(B_phenom) = 137 to PROVED until Gap G137-B is closed

---

## References

| File | Role |
|------|------|
| `canonical/alpha/veff_corrected.tex` | First-principles V_eff derivation |
| `canonical/alpha/veff_corrected_statement.tex` | Formal theorem list for corrected statements |
| `canonical/alpha/alpha_equation_matrix.tex` | Three-route equation chain |
| `canonical/alpha/alpha_best_route.tex` | Full derivation chain overview |
| `canonical/appendices/appendix_alpha_geometry.tex` | Corrected canonical appendix |
| `ALPHA_PROGRESS_REPORT.md` | Progress and strategy report (corrected) |
| `reports/alpha_veff_sanity_audit.md` | Prior comprehensive sanity audit |
| `reports/alpha_consistency_verdict.md` | Alpha route consistency verdict |
| `reports/alpha_hidden_fit_audit.md` | Prior hidden-fit analysis |
| `reports/alpha_missing_lemma.md` | Formal statement of Gap G137-B |
