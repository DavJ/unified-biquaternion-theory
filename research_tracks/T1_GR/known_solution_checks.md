<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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


# T1_GR — Known Solution Checks

**Track**: T1_GR — General Relativity Recovery  
**Purpose**: Record every explicit known-solution verification in the T1_GR chain,
with numerical results, status flags, and honest accounting of what is and is not
verified.  
**Date**: 2026-04-28  
**Sources**: `GR_theorem_result.tex §Appendix B`, `tools/verify_schwarzschild_theta.py`,
`canonical/geometry/biquaternionic_vacuum_solutions.tex §3`,
`canonical/gr_closure/GR_chain_summary.tex §Gravitational Sector`

---

## Summary

| Check | Result | Status |
|-------|--------|--------|
| Schwarzschild spatial metric $g_{ij}$ | $\Psi(r)^4\delta_{ij}$, error $< 10^{-15}$ | ✅ VERIFIED |
| Schwarzschild off-diagonal $g_{i0}$ | Numerically zero | ✅ VERIFIED |
| ODE consistency $f'^2 + g'^2 = \Psi^4$ | Exact analytical identity + numerical | ✅ VERIFIED |
| Schwarzschild temporal $g_{tt}$ | Requires complex-time structure | ⚠️ NEEDS FULL $\tau$ |
| ASD Ricci-flat sector | Holonomy $\subset \mathrm{SU}(2)_-$, $C^+=0$, ASD Ricci-flat | ✅ PROVED |
| Twistor space description | Penrose nonlinear graviton theorem applies | ✅ PROVED |
| Regge-Wheeler equation (odd-parity graviton) | Derived from linearised UBT | ✅ PROVED |
| Zerilli equation (even-parity graviton) | Not yet derived | ❌ OPEN [GAP-Z] |

---

## Check 1: Schwarzschild Metric from $\Theta_0$

### Setup

**Ansatz**:
$$\Theta_0 = e^{i\Phi(r)}\bigl[f(r)\,\mathbf{1} + g(r)\,\boldsymbol{e}_r\bigr],$$
with $M = 1$ (geometrised units), $g(r) = r\Psi(r)^2$,
$f'(r) = \Psi(r)\sqrt{2M/r}$, $\Phi(r) = (1-M/2r)/(1+M/2r)$.

**Expected result** (Schwarzschild in isotropic coordinates):
$$g_{tt} = -\Phi(r)^2, \qquad
g_{ij} = \Psi(r)^4\,\delta_{ij}, \qquad
\Psi(r) = 1 + \frac{M}{2r}.$$

**Script**: `tools/verify_schwarzschild_theta.py`

---

### ODE Consistency Condition

The ansatz functions must satisfy $f'^2 + g'^2 = \Psi^4$.

**Analytical proof**: $f' = \Psi\sqrt{2M/r}$, $g' = 1 - M^2/(4r^2)$.  Direct
computation gives:
$$f'^2 + g'^2 = \Psi^2 \cdot \frac{2M}{r} + \left(1 - \frac{M^2}{4r^2}\right)^2
= \Psi^4. \quad \checkmark$$

**Numerical verification**:

| $r/M$ | $f'$ | $g'$ | $f'^2+g'^2$ | $\Psi^4$ | Error |
|--------|------|------|------------|----------|-------|
| 2.0 | 1.250000 | 0.937500 | 2.441406 | 2.441406 | 0.00 |
| 5.0 | 0.695701 | 0.990000 | 1.464100 | 1.464100 | $1.5\times10^{-16}$ |
| 10.0 | 0.469574 | 0.997500 | 1.215506 | 1.215506 | $1.8\times10^{-16}$ |
| 100.0 | 0.142128 | 0.999975 | 1.020151 | 1.020151 | $4.3\times10^{-16}$ |

**Status**: ✅ VERIFIED — exact analytical identity, confirmed to floating-point precision.

---

### Spatial Metric Components

**Computed vs.\ expected** $g_{ij} = \Psi(r)^4\,\delta_{ij}$:

| $r/M$ | $\Psi^4$ (expected) | $g_{xx}$ | $g_{yy}$ | $g_{zz}$ | $\max|g_\mathrm{off}|$ | Status |
|--------|---------------------|----------|----------|----------|----------------------|--------|
| 2.0 | 2.441406 | 2.441406 | 2.441406 | 2.441406 | $5.6\times10^{-17}$ | ✅ OK |
| 5.0 | 1.464100 | 1.464100 | 1.464100 | 1.464100 | $1.9\times10^{-16}$ | ✅ OK |
| 10.0 | 1.215506 | 1.215506 | 1.215506 | 1.215506 | $2.8\times10^{-17}$ | ✅ OK |
| 50.0 | 1.040604 | 1.040604 | 1.040604 | 1.040604 | $7.3\times10^{-17}$ | ✅ OK |
| 100.0 | 1.020151 | 1.020151 | 1.020151 | 1.020151 | $2.7\times10^{-16}$ | ✅ OK |

**Relative error**: $< 10^{-15}$ across all tested radii.  
**Off-diagonal components**: numerically zero (as expected for spherical symmetry).

**Status**: ✅ VERIFIED — all spatial components agree to floating-point precision.

---

### Temporal Component

The static real-quaternion ansatz $\Theta_0$ has $\partial_t\Theta_0 = 0$ (time-independent),
so the metric formula gives $g_{tt} = 0$ for this ansatz alone.

The Lorentzian $g_{tt} = -\Phi(r)^2$ is recovered only when the **full
complex-time structure** $\tau = t + i\psi$ is used.  Specifically:
$$\partial_\psi\Theta_0 = i\alpha(r)\Theta_0 \quad\Longrightarrow\quad
g_{tt} = -\mathrm{Re}[\mathrm{Tr}(\partial_\psi\Theta_0\cdot\partial_\psi\Theta_0^\dagger)]
= -\Phi(r)^2.$$

This is an **expected feature** of the static ansatz, not an error.  The
complex-time structure is AXIOM-B, from which the Lorentzian signature $g_{00} < 0$
follows as a theorem (Step 3).

**Status**: ⚠️ REQUIRES FULL $\tau$ STRUCTURE — analytically understood; numerical
verification requires the complex-time UBT solver (planned as future work).

---

### Reproduction Instructions

```bash
# Prerequisites
pip install numpy

# Run from repository root
python tools/verify_schwarzschild_theta.py

# Optional arguments
python tools/verify_schwarzschild_theta.py --mass 2.0 --r_values 3,6,12
```

The script exits with code 0 if all spatial components agree within tolerance
$10^{-8}$ (default), and code 1 otherwise.

---

## Check 2: ASD Condition and Twistor Space

**Source**: `canonical/gr_closure/GR_chain_summary.tex §Gravitational Sector [v57]`,
`research_tracks/research/asd_condition_ubt.tex §5`

**Result**: For $\Theta \in \mathrm{SU}(2)_- \subset \mathbb{C}\otimes\mathbb{H}$
smooth with $|\Theta| = 1$:

1. **Holonomy**: The holonomy of $g_{\mu\nu}[\Theta]$ lies in
   $\mathrm{Sp}(1) \cong \mathrm{SU}(2)_-$.
2. **ASD Weyl condition**: The anti-self-dual Weyl tensor condition $C^+ = 0$ holds.
3. **ASD Ricci-flat**: Combined with $\nabla^\dagger\nabla\Theta = 0$
   (giving $R_{\mu\nu} = 0$ via the GR chain), the metric is ASD Ricci-flat.
4. **Twistor space**: By the Penrose nonlinear graviton theorem, $g_{\mu\nu}[\Theta]$
   admits a curved twistor space description.

**Note**: Schwarzschild (Petrov type D) lies outside the $\mathrm{SU}(2)_-$ sector.
This is consistent: Schwarzschild has a non-zero self-dual Weyl tensor.

**Status**: ✅ PROVED [L1]

---

## Check 3: Regge-Wheeler Equation (Odd-Parity Graviton)

**Source**: Linearised GR chain (see `GR_theorem_result.tex §Extended Result 3`)

**Setup**: Linearise the UBT field equation around flat background:
$$\Theta = \Theta_0 + \epsilon\,\delta\Theta.$$

**Result**: The linearised UBT equation reproduces the linearised Einstein equations.
For odd-parity (axial) perturbations of the Schwarzschild background decomposed into
angular modes $(\ell, m, \omega)$, the master perturbation equation is the
Regge-Wheeler equation:
$$\left[\frac{\mathrm{d}^2}{\mathrm{d}r_*^2} + \omega^2 - V_{\mathrm{RW}}(r)\right]\Psi_{\mathrm{RW}} = 0,$$
where $r_* = r + 2M\ln|r/2M - 1|$ is the tortoise coordinate and
$$V_{\mathrm{RW}}(r) = \left(1 - \frac{2M}{r}\right)
\left[\frac{\ell(\ell+1)}{r^2} - \frac{6M}{r^3}\right]$$
is the Regge-Wheeler potential (for spin-2 gravitational perturbations).

**No additional input** beyond the UBT metric chain is required.

**Status**: ✅ PROVED [L1]

---

## Check 4: Zerilli Equation (Even-Parity Graviton) — OPEN

**Status**: ❌ OPEN [GAP-Z, L2]

**What is missing**: The even-parity (polar) perturbation equation:
$$\left[\frac{\mathrm{d}^2}{\mathrm{d}r_*^2} + \omega^2 - V_{\mathrm{Z}}(r)\right]\Psi_{\mathrm{Z}} = 0,$$
where $V_{\mathrm{Z}}$ is the Zerilli potential (different from $V_{\mathrm{RW}}$).

**Why it is hard**: Even-parity modes couple scalar and tensor sectors in the
UBT framework; Chandrasekhar's two-potential transformation has not been
implemented for the even-parity $\Theta$ sector.

**Impact on main theorem**: None.  The proved Regge-Wheeler result is sufficient
for the main GR recovery claim.

See `proof_gap_list.md §GAP-Z` for a detailed obstruction map.

---

## Honest Accounting Summary

| Component | Analytical | Numerical | Status |
|-----------|-----------|-----------|--------|
| Metric formula (Steps 1–3) | ✅ | — | Proved |
| Levi-Civita + curvature (Step 4) | ✅ | — | Standard GR |
| Einstein equations (Step 5) | ✅ | — | Proved |
| Schwarzschild $g_{ij}$ (spatial) | ✅ (exact) | ✅ (error $<10^{-15}$) | Verified |
| Schwarzschild $g_{i0}$ (off-diagonal) | ✅ (symmetry) | ✅ (zero) | Verified |
| Schwarzschild $g_{tt}$ (temporal) | ✅ (complex $\tau$) | ⚠️ (needs $\tau$ solver) | Analytically known |
| ODE consistency $f'^2+g'^2=\Psi^4$ | ✅ (algebraic) | ✅ (FP precision) | Verified |
| ASD Weyl condition | ✅ | — | Proved |
| Twistor space | ✅ (Penrose theorem) | — | Proved |
| Regge-Wheeler (odd-parity) | ✅ | — | Proved |
| Zerilli (even-parity) | ❌ | ❌ | Open [GAP-Z] |
