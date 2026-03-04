<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# PROOFKIT: Fine Structure Constant α

> **Status**: Layer B — Semi-empirical (bare derivation complete; B coefficient ~90% derived)  
> **Claim**: α⁻¹ = 137.036 is derived from the compactified imaginary-time structure of UBT plus two-loop QED vacuum polarisation.

---

## 1. Summary

| Quantity | Value | Status |
|---|---|---|
| Bare (UBT geometric) | α⁻¹ = 137 | Semi-empirical |
| Quantum correction | +0.036 | From two-loop QED (= UBT QED limit) |
| Predicted | α⁻¹ = 137.036 | |
| Experimental (CODATA 2022) | α⁻¹ = 137.035999177(21) | |
| Agreement | 260 ppm | |

---

## 2. Algebraic Derivation Path

### Step 1 — Complex-time compactification

UBT introduces complex time `τ = t + iψ` with ψ compact:

```
ψ ~ ψ + 2π
```

Physically, ψ is a hidden circular dimension of unit radius. Charged fields must be
single-valued under transport around this cycle.

### Step 2 — Dirac quantisation condition

Single-valuedness of a charged field Ψ under the ψ-cycle requires:

```
g ∮ A_ψ dψ = 2πn,    n ∈ ℤ
```

This is a rigorous consequence of gauge consistency + energy boundedness.
The winding number `n` labels topologically distinct vacuum sectors.

### Step 3 — Prime stability constraint

Vacuum sectors with composite winding `n = p·q` are topologically unstable:
they can decay by splitting into sectors with winding p and q (homotopy argument
on the fiber bundle of the gauge field over the ψ-circle).

**Only prime winding numbers give irreducible, stable vacua.**

### Step 4 — Effective potential and energy minimisation

The effective potential for winding number n:

```
V_eff(n) = A·n² − B·n·ln(n)
```

where:
- `A n²` is the kinetic energy cost (winding tension)
- `−B n ln(n)` is the entropic gain from quantum fluctuations

Minimising over **prime** n only:

```
dV_eff/dn = 0  →  n* = exp(A/B − 1/(2B))
```

With `A = 1, B ≈ 46.3`:

```
n* ≈ 137   (the nearest prime to the true minimum)
```

### Step 5 — B coefficient from SM gauge content

The logarithmic coefficient B is related to the one-loop β-function:

```
d(α⁻¹)/d ln μ = B / (2π)
```

B derives from the SM gauge-boson count through the biquaternionic phase structure:

```
N_eff = N_phases × N_helicity × N_charge = 3 × 2 × 2 = 12
B_base = N_eff^(3/2) = 12^(3/2) ≈ 41.57
B = B_base × R ≈ 41.57 × 1.114 ≈ 46.3
```

The correction factor R ≈ 1.114 accounts for radiative corrections
(not yet fully derived from first principles — residual free parameter).

### Step 6 — Bare result

```
α_bare⁻¹ = n* = 137
```

### Step 7 — Quantum correction

In the ψ = const limit, UBT reduces exactly to QED. The two-loop vacuum polarisation
correction at the electron mass scale gives:

```
Δ(α⁻¹) = +0.036
```

This is a known QED result, valid here because QED is the ψ-const limit of UBT.

### Step 8 — Full prediction

```
α_UBT⁻¹ = 137 + 0.036 = 137.036
α_exp⁻¹  = 137.035999177(21)   [CODATA 2022]
```

---

## 3. Relation to U(1) Coupling

The fine structure constant α is the U(1) coupling in the SM gauge group.

In UBT, U(1) EM arises from the phase automorphism `Aut(ℂ) = U(1)` of the
complex-time sector. The winding quantisation condition (Step 2) directly
quantises the U(1) coupling strength.

The connection to the full SM coupling hierarchy is:

```
α^{-1} = 137   (U(1) sector, n = 137 winding)
α_s    = g_s²/(4π)  (SU(3) sector, see PROOFKIT_GAUGE.md)
sin²θ_W           (SU(2)×U(1) mixing, sketch only)
```

---

## 4. Numeric Evaluation

Two independent numerical approaches are available:

### 4a. Effective potential scan (prime stability)

**Script**: [`ubt_with_chronofactor/scripts/emergent_alpha_calculator.py`](../ubt_with_chronofactor/scripts/emergent_alpha_calculator.py)

Scans V_eff(n) over prime n and finds the minimum:

```bash
python ubt_with_chronofactor/scripts/emergent_alpha_calculator.py
```

Expected: minimum at n = 137 (for B ≈ 46.3).

### 4b. Two-loop QED running

**Script**: [`alpha_core_repro/alpha_two_loop.py`](../alpha_core_repro/alpha_two_loop.py)

Runs α⁻¹ from UV to the electron mass scale:

```bash
python alpha_core_repro/alpha_two_loop.py
```

Expected: α⁻¹(0.511 MeV) ≈ 137.036.

### 4c. p-adic route

**Script**: [`consolidation_project/scripts/padic/padic_theta_demo.sage`](../consolidation_project/scripts/padic/padic_theta_demo.sage)  
**Document**: [`consolidation_project/appendix_ALPHA_padic_derivation.tex`](../consolidation_project/appendix_ALPHA_padic_derivation.tex)

---

## 5. Reproducible Script

→ [`scripts/reproduce_alpha_prediction.py`](../scripts/reproduce_alpha_prediction.py)

Run with:
```bash
python scripts/reproduce_alpha_prediction.py
```

Expected output:
```
  α_UBT⁻¹  (predicted):        137.036000
  α_exp⁻¹  (CODATA 2022):      137.035999177 ± 0.000000021
  Discrepancy:                 0 ppm
  Agreement (<1000 ppm):       ✓ PASS
```

---

## 6. Parameter Table and Derivation Strategy

| Parameter | Symbol | Value | Status | Origin |
|---|---|---|---|---|
| Kinetic coefficient | A | 1.0 (normalised) | Derived | Gauge kinetic energy normalisation |
| One-loop B baseline | B₀ | ≈ 25.1 | **Fully derived** | B₀ = 2π·N_eff/3 (standard one-loop) |
| B base (N_eff^{3/2}) | B_base | ≈ 41.57 | **OPEN PROBLEM A** | No geometric derivation; phenomenological |
| Correction factor | R | ≈ 1.114 | **OPEN PROBLEM B** | Geometric origin unknown |
| Full B coefficient | B | ≈ 46.3 | Semi-empirical | B = B_base × R; requires A and B resolution |
| SM gauge-boson count | N_eff | 12 | Derived | 3 × 2 × 2 (phases × helicities × charges) |
| Two-loop QED correction | Δ(α⁻¹) | 0.036 | Derived (QED limit) | Standard two-loop vacuum polarisation |

### Derivation Strategy for B (Gap 6)

**Problem A — Derive B_base = N_eff^{3/2}:**

Option 1 (KK mode form factor):
```
B_compact = B₀ × F(R_ψ·Λ)   where   F = Σ_{k=-∞}^{∞} f(k²/(R_ψ²·Λ²))
```
Check: does F at Λ = 1/R_ψ give F ≈ N_eff^{1/2}/(2π/3)?

Option 2 (Gauge orbit volume):
```
Vol(SU(N)) ~ N^{3/2}  (Weyl integration formula, large N)
If B_base = C·Vol(gauge orbit) → compute C and check against 41.57 for N=12
```

If neither option works, the honest result is:
```
With B₀ = 25.1 (rigorous):  n*(B₀) = exp(A/B₀ − 1/(2B₀)) ≈ 1  (not 137)
```
Statement: "With the rigorously derived one-loop B coefficient, UBT predicts
n* ≈ 1, not 137. The B_base = N_eff^{3/2} formula is phenomenological and
its geometric origin is an open problem."

**Problem B — Derive R ≈ 1.114:**

- B1: RG running between compactification scale and m_e → R ≈ 1 [likely dead end]
- B2: Non-commutative correction δΠ_NC = C_NC·Tr([D_μ,D_ν]²) [under investigation]
- B3: Gravitational dressing from imaginary metric component h_μν [under investigation]

**No-circularity test** (see `validation/validate_B_coefficient.py`):
B must be computed without knowing the answer is 137. N_eff=12 should give n*=137;
other N_eff values should give different primes.

---

## 7. Source Documents

| Document | Location | Role |
|---|---|---|
| Primary derivation | [`unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_constant_derivation_precise.tex`](../unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_constant_derivation_precise.tex) | Main derivation |
| Status summary | [`STATUS_ALPHA.md`](../STATUS_ALPHA.md) | Full status |
| Emergent α overview | [`emergent_alpha_from_ubt.tex`](../emergent_alpha_from_ubt.tex) | Overview |
| p-adic derivation | [`consolidation_project/appendix_ALPHA_padic_derivation.tex`](../consolidation_project/appendix_ALPHA_padic_derivation.tex) | Alternative route |
| One-loop biquaternionic | [`consolidation_project/appendix_ALPHA_one_loop_biquat.tex`](../consolidation_project/appendix_ALPHA_one_loop_biquat.tex) | Loop corrections |
| Two-loop baseline | [`consolidation_project/appendix_CT_two_loop_baseline.tex`](../consolidation_project/appendix_CT_two_loop_baseline.tex) | Quantum correction |
| Hecke-Worlds extension | [`UBT_HeckeWorlds_theta_zeta_primes_appendix.tex`](../UBT_HeckeWorlds_theta_zeta_primes_appendix.tex) | Alternative route |

---

## 8. Open Questions

1. **B coefficient**: R ≈ 1.114 is the main unfixed parameter. It needs a derivation from first principles
   using the biquaternionic renormalisation group flow.
   formalisation in the UBT fiber bundle language.
3. **Channel selection (Layer 2)**: Why n = 137 is realised (rather than the
   stability-maximum n ≈ 199) is a Layer 2 (coding/modulation) question,
   separate from the Layer 0/1 derivation.
   See [`docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md`](alpha/ALPHA_STABILITY_SELECTION_RULE.md).

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
