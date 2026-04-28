<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# EW Mixing Status Report

**File**: `reports/ew_mixing_status.md`  
**Purpose**: High-level status of the electroweak mixing problem in UBT.
Companion to the technical derivation document.  
**Date**: 2026-04-28  
**Priority**: CRITICAL  
**Companion file**: `canonical/alpha/weinberg_angle_derivation.md`  
**Sources**: `canonical/alpha/alpha_derivation_routes.md`,
`reports/alpha_no_fit_audit.md`,
`research_tracks/T3_ALPHA/alpha_progress_log.md`,
`canonical/interactions/sm_gauge.tex`

---

## Problem Statement

**Derive $g'/g = \tan\theta_W$ from UBT first principles.  No numerical fitting.**

This is the **conversion of the α problem**: instead of deriving α directly via the
prime-attractor/Kac-Moody route (blocked after 27+ approaches), the strategy is to
derive the Weinberg angle $\theta_W$ algebraically and obtain α via:
$$\alpha = \frac{g^2\sin^2\theta_W}{4\pi}$$

**Acceptance criterion**: No parameter is chosen to reproduce $\sin^2\theta_W \approx 0.231$.

---

## 1. What Is Already Known

### Proved (zero free parameters)

| Claim | Level | Source |
|-------|-------|--------|
| $A_\mu = \sin\theta_W W^3_\mu + \cos\theta_W B_\mu$ (photon field) | [L1] | Standard EW algebra |
| $e = g\sin\theta_W = g'\cos\theta_W$ | [L1] | `canonical/alpha/gauge_normalization_attempt.tex §3` |
| $\alpha = g^2\sin^2\theta_W/(4\pi)$ | [L1] | Follows from above |
| SU(2)_L from left-unitary action on ℂ⊗ℍ | [L0] | `canonical/interactions/sm_gauge.tex` |
| U(1)_Y from right scalar phase action on ℂ⊗ℍ | [L0] | `canonical/interactions/sm_gauge.tex` |
| Generator norms equal in fundamental: Tr(τ²) = Tr(Y²) = 1/2 | [L0] | EW1 computation |

### Semi-empirical (not derived from UBT)

| Claim | Experimental value | Source |
|-------|-------------------|--------|
| $\sin^2\theta_W(M_Z)$ | 0.23122 | PDG 2024 |
| $g(M_Z)$ | 0.6527 | PDG 2024 |
| $g'(M_Z)$ | 0.3497 | PDG 2024 |
| $M_{\mathrm{GUT}}$ | $\sim 2\times10^{16}$ GeV (SU(5)) | Experimental running |

### Excluded near-miss

| Attempt | UBT prediction | Experimental value | Status |
|---------|---------------|-------------------|--------|
| $g = g'$ (equal norms in doublet rep) | $\sin^2\theta_W = 1/2$ | 0.231 | **EXCLUDED** |

The $g = g'$ result is the algebraically simplest outcome of the UBT kinetic term
in the doublet representation and is recorded as a confirmed near-miss.

---

## 2. Three Workstream Status

### EW1 — Pure UBT Algebra Route

**Objective**: Fix $g'/g$ from the generator normalizations of SU(2)_L and U(1)_Y
within ℂ⊗ℍ, accounting for the full fermion representation content.

**Current status**: OPEN — not yet attempted.

| Task | Description | Status |
|------|-------------|--------|
| EW1.A | Derive fermion Y assignments from ψ-winding modes | ❌ OPEN |
| EW1.B | Compute Tr_all_reps(Y²) and Tr_all_reps(T₃²) | ❌ OPEN |
| EW1.C | Derive g'/g from the generator ratio | ❌ OPEN (depends on EW1.A,B) |

**Potential outcome**: If UBT ψ-winding modes give the same fermion representation
content as the SM, the SU(5) relation $g'^2/g^2 = 3/5$ would follow naturally
(Georgi-Glashow result from representation theory without full GUT embedding).

**Blocker**: Fermion hypercharge assignments from ψ-winding are not yet derived.

---

### EW2 — GUT Embedding Route

**Objective**: Test whether ℂ⊗ℍ embeds into SU(5), SO(10), or an internal UBT
GUT structure, giving the boundary condition $\sin^2\theta_W(\mathrm{GUT}) = 3/8$.

**Current status**: OPEN — fresh, high-priority attack.

| Task | Description | Status |
|------|-------------|--------|
| EW2.A | Test SU(5) embedding of the SM gauge algebra in ℂ⊗ℍ | ❌ OPEN |
| EW2.B | Test SO(10) embedding via 16-dim spinor | ❌ OPEN |
| EW2.C | Investigate internal UBT GUT (complexification route) | ❌ OPEN |
| EW2.D | RG flow from GUT scale to EW scale | ❌ OPEN (depends on EW2.A–C) |

**Best-case result if EW2.A succeeds**:

$$\sin^2\theta_W(\mathrm{GUT}) = \frac{3}{8} \quad\longrightarrow\quad
\sin^2\theta_W(M_Z) \approx 0.231 \quad\longrightarrow\quad
\alpha \approx \frac{1}{137}$$

This would be a 3-parameter prediction (M_GUT, g(M_GUT), α(M_Z)) from the
UBT algebraic structure — comparable in depth to the original SU(5) prediction
by Georgi and Glashow (1974).

**Algebraic key**: SU(5) gives $\sin^2\theta_W = 3/8$ solely from the
hypercharge-generator embedding:
$$Y_{\mathrm{SU5}} = \mathrm{diag}(-\tfrac{1}{3},-\tfrac{1}{3},-\tfrac{1}{3},\tfrac{1}{2},\tfrac{1}{2})$$
The UBT question is: does ℂ⊗ℍ naturally produce this generator?

---

### EW3 — Geometric Projection Route

**Objective**: Interpret $\theta_W$ as a geometric projection angle in the
internal symmetry fiber of the $\Theta$-bundle, derivable from the Killing metric
of $\mathfrak{g}_{EW}$ induced by $\mathrm{Tr}[(D_\mu\Theta)^\dagger D^\mu\Theta]$.

**Current status**: OPEN — EW3.A (induced inner product computation) is the
most tractable entry point.

| Task | Description | Status |
|------|-------------|--------|
| EW3.A | Compute Killing metric on $\mathfrak{g}_{EW}$ from UBT kinetic term | ❌ OPEN |
| EW3.B | Derive $\cos\theta_W = \langle Q,Y\rangle/(\|Q\|\|Y\|)$ | ❌ OPEN (depends on EW3.A) |
| EW3.C | Geometric bundle interpretation | ❌ OPEN |

**Note**: EW3 is the most speculative route but requires only a computation on
known objects. If the induced Killing metric differs from the equal-norm result
(which gave $\theta_W = \pi/4$), EW3 could constrain $\theta_W$ to a different value.

---

## 3. Parallel Tracks: EW vs. Modular Bootstrap

Both the EW conversion and the modular bootstrap (k=1) tracks are running in parallel.

| Track | Goal | Status | Deadline |
|-------|------|--------|----------|
| EW2.A (GUT embedding) | $\sin^2\theta_W = 3/8$ GUT boundary | OPEN — start now | No hard deadline |
| Modular bootstrap M1–M4 | $k = 1 \Rightarrow$ α⁻¹ = 137 | IN PROGRESS — M1 active | 2026-05-26 |
| EW1.A (fermion reps) | $g'/g$ from ψ-winding | OPEN | No hard deadline |

**Resource allocation**: Given the global_rules (no new tracks for 30 days, optimize
for completed outputs), the T3_ALPHA 15% allocation covers both sub-tracks.
EW2.A should receive most of that allocation given its high breakthrough probability.

---

## 4. Expected Outputs and Publication Plan

### If EW2.A (SU(5) embedding) succeeds

**Paper title candidate**: *Weinberg Angle from Biquaternion Algebra: SU(5) Boundary
Condition from ℂ⊗ℍ*

**Claim hierarchy**:
1. [L0] ℂ⊗ℍ ≅ Mat(2,ℂ) — algebraic foundation
2. [L0] SU(2)_L and U(1)_Y embedded in Aut(ℂ⊗ℍ)
3. [L1] SU(5) embedding of the SM subgroup gives $\sin^2\theta_W(\text{GUT}) = 3/8$ (new)
4. [L1] RG flow to M_Z gives $\sin^2\theta_W(M_Z) \approx 0.231$ (using one-loop SM RG)
5. [L1] $\alpha = g^2\sin^2\theta_W/(4\pi)$ follows

**Stated as semi-empirical**: $M_{\mathrm{GUT}}$ from phenomenological running (unless derived from R_ψ).

**Target journal**: Physical Review D (Letters) or Physics Letters B.

### If EW2.A fails (no SU(5) embedding)

- Continue EW1 (fermion representation route) and EW3 (geometric projection).
- Fallback: state that $\theta_W$ is currently the primary open problem in the EW
  sector of UBT, with three attack routes documented.

---

## 5. Impact on Existing Results

### No impact on T1_GR (GR Recovery)

The GR derivation chain (Theorems 3.1–3.5, `UBT_GR_PAPER.md`) is independent
of $\theta_W$ and is unaffected by the EW conversion.

### No impact on T2_GAUGE (SM Gauge Structure)

The proved gauge results (Theorems G.A–G.D, SU(3), three generations, confinement)
are independent of $\theta_W$ and remain valid.

### Replaces T3_ALPHA B_base strategy

The EW conversion **supersedes** the k=1 Kac-Moody approach as the primary T3_ALPHA
strategy.  The modular bootstrap continues in parallel as a 4-week time-boxed effort.

---

## 6. Gap Registry (EW Sector)

| Gap ID | Description | Workstream | Priority |
|--------|-------------|-----------|----------|
| EW-1 | $\tan\theta_W = g'/g$ from UBT algebra | EW1/EW2/EW3 | **CRITICAL** |
| EW-2 | $\Theta_0$ VEV as SU(2)_L doublet | EW2.C | HIGH |
| GUT-UBT | SU(5) or SO(10) embedding of ℂ⊗ℍ | EW2.A/EW2.B | HIGH |
| EW-g | SU(2)_L coupling $g$ from canonical kinetic normalisation | EW1.C | MEDIUM |
| RG-UBT | GUT scale $M_{\mathrm{GUT}}$ from ψ-circle radius | EW2.D | MEDIUM |

---

## 7. Summary Table

| Item | Value | Status |
|------|-------|--------|
| $e = g\sin\theta_W$ | Identity | [L1] Proved |
| $\alpha = g^2\sin^2\theta_W/(4\pi)$ | Identity | [L1] Proved |
| SU(2)_L in ℂ⊗ℍ | Left-unitary action | [L0] Proved |
| U(1)_Y in ℂ⊗ℍ | Right-phase action | [L0] Proved |
| $\tan\theta_W = g'/g$ (value) | **GAP EW-1** | ❌ OPEN |
| EW1.A — fermion Y from ψ-modes | — | ❌ OPEN (fresh) |
| EW2.A — SU(5) embedding | — | ❌ OPEN (fresh, recommended first) |
| EW3.A — induced Killing metric | — | ❌ OPEN (tractable) |
| $\sin^2\theta_W = 1/2$ (equal norms) | **EXCLUDED** by experiment | Tested near-miss |
| $\sin^2\theta_W = 3/8$ (GUT, if EW2 succeeds) | 0.375 → 0.231 after RG | [MC] MOTIVATED |
