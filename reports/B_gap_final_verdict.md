<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# B_gap_final_verdict.md — B(p) = (p+1)/3: Derivation or Ansatz?

**Task**: close_or_kill_B_coefficient_gap / construct_or_kill_hecke_equivariant_winding_path_integral  
**Author**: Ing. David Jaroš  
**Date**: 2026-05-09 (updated from 2026-05-08; incorporates Hecke path-integral no-go result)  
**Priority**: CRITICAL  
**Gap ID**: G137-B  
**Companion LaTeX**: `research_tracks/alpha_spectral/b_coefficient_gap_resolution.tex`,
`research_tracks/alpha_spectral/hecke_equivariant_path_integral.tex`  
**Hecke route report**: `reports/hecke_path_integral_no_go_or_success.md`  
**Hard rules**: No use of observed α; no fitting B to 137.

---

## Executive Summary

> **VERDICT: CONDITIONAL**
>
> $B(p) = (p+1)/3$ **cannot currently be derived** from the UBT action $S[\Theta]$.
> It must remain a **phenomenological/modular ansatz** until the Hecke-trace or
> non-perturbative mechanism is identified.  All intermediate results are stated
> with explicit proof-status labels.

---

## 1. What Is $B(p)$ and Why It Matters

The UBT effective potential for winding modes on the compact imaginary-time
circle is:

$$V_{\mathrm{eff}}(n) = n^2 - B\,n\ln n$$

The minimum occurs at $n^* = n^*(B)$ satisfying $2n^* = B(\ln n^* + 1)$.
For the prime attractor to land at $n^* = p$, the required value is:

$$B_{\mathrm{phenom}}(p) = \frac{2p}{\ln p + 1}$$

The prime-stability formula proposes:

$$B(p) = \frac{p+1}{3}$$

At $p = 137$: $B(137) = 138/3 = 46.000$, versus $B_{\mathrm{phenom}}(137) \approx 46.298$ (error 0.64%).

---

## 2. Four Routes Examined

### Route 1 — One-Loop RG from KK Spectrum

| Item | Result | Status |
|------|--------|--------|
| $n^2$ term from KK compactification | $V_\mathrm{tree} = n^2$ | **PROVED** |
| $n^2\ln n$ shape from one-loop $d{=}1$ | $\delta V \propto n^2\ln n$ | **PROVED** |
| Regulator independence of $\ln n$ coeff | UV-finite at one loop | **PROVED** |
| Gauge invariance ($n$ is $\mathrm{U}(1)_\psi$ charge) | SM-gauge-invariant | **PROVED** |
| Constant $B$ (not $n$-dependent) | $B(n) = n/(2\pi)$ naive | **HEURISTIC** |
| $B \approx 21.8$ (one-loop, $n=137$) | $137/(2\pi)$ | **HEURISTIC** |

**Conclusion**: One-loop KK gives $B \approx 21.8$, a factor $\approx 2.1$ below the target.
The shape of $V_{\mathrm{eff}}$ is rigorous; the coefficient is not.

---

### Route 2 — KK+Winding at Self-Dual Radius

| Item | Result | Status |
|------|--------|--------|
| T-duality degeneracy at $R_\psi = 1$ | Factor 2 in loop sum | **HEURISTIC** |
| $B_{\mathrm{KK+wind}} = 2 \times 21.8$ | $\approx 43.6$ | **HEURISTIC** |
| Self-dual radius $R_\psi = 1$ derived | Not derived from UBT moduli | **OPEN** |
| $\Delta B = 46 - 43.6 = 2.4$ explained | Not explained | **OPEN** |

**Candidate sources of $\Delta B \approx 2.4$**:

- Two-loop: $\delta B \lesssim 1.4$ (order-of-magnitude; diagrams not computed)
- Gauge-boson loops: $\delta B \lesssim 1$ (estimate)
- Non-perturbative threshold: unknown magnitude
- **None individually or jointly close the gap with rigor**

**Conclusion**: KK+winding gives $B \approx 43.6$. Missing factor $\approx 1.054$ unexplained.

---

### Route 3 — Modular Index $\mu(\Gamma_0(p))/3$

The index of the congruence subgroup $\Gamma_0(p)$ in $\mathrm{SL}(2,\mathbb{Z})$
is $\mu(\Gamma_0(p)) = p+1$ (Diamond & Shurman, Thm 3.1.1).  The normalised
hyperbolic area of $X_0(p)$ is $(p+1)/3 = B(p)$.

| Quantity | Value at $p=137$ | Error vs $B_{\mathrm{phenom}}$ |
|----------|-----------------|-------------------------------|
| $\mu(\Gamma_0(137))/3$ | 46.000 | −0.64% |
| $+\, \nu_2/4$ (elliptic correction) | 46.500 | +0.44% |
| Chowla–Selberg $B_{\mathrm{CS}}$ | 46.281 | −0.04% |
| $B_{\mathrm{phenom}}$ | 46.298 | 0 |

**Properties of the modular route**:
- ✅ Gauge-invariant: $\mu(\Gamma_0(p))$ is an arithmetic invariant, independent of SM gauge fields
- ✅ Regulator-independent: topological invariant, unaffected by UV scheme
- ❌ **Not derived from $S[\Theta]$**: No known mechanism connecting the UBT action to $\mu(\Gamma_0(n^*))$

**Missing step**: A first-principles computation of $\int \mathcal{D}\Theta\, e^{iS[\Theta]}$
in the winding sector at level $n=p$ that returns $\mu(\Gamma_0(p)) = p+1$ as
the loop coefficient.

**Candidate mechanisms** (none yet realised):
1. Hecke-operator trace: $\mathrm{Tr}(T_p) = p+1$ on $\mathbb{P}^1(\mathbb{F}_p)$
2. Winding-sector coset enumeration: $\mu(\Gamma_0(p))$ coset reps as winding vacua
3. Spectral geometry at $\tau = i$: Chowla–Selberg formula coupling Hecke structure to spectral determinant

**Conclusion**: Modular route gives the correct $B$ but is not derived from $S[\Theta]$.
Status: **MOTIVATED COINCIDENCE [MC]**, not a derivation.

---

### Route 4 — Fixed-Point Bootstrap

Substituting $B = (p+1)/3$ into the prime-attractor equation gives the system:

$$6n = (n+1)(\ln n + 1)$$

| $n$ | $(n+1)(\ln n+1) - 6n$ | Sign |
|-----|-----------------------|------|
| 137 | $-5.2$ | − (undershoots) |
| 139 | $-3.2$ | − (undershoots) |
| ~141 | $\approx 0$ | root (not prime) |
| 150 | $+7.2$ | + (overshoots) |

The system has no exact prime solution.  $p=137$ and $p=139$ are the nearest
primes to the root $n_{\mathrm{root}} \approx 141$, consistent with the
observed 0.64% discrepancy.

**Conclusion**: The ansatz is self-consistent near $n=137$.  The bootstrap
confirms consistency but does not constitute a derivation of $B(p) = (p+1)/3$.

---

## 3. Master Gap Table

| Claim | Status | Reference |
|-------|--------|-----------|
| $V_\mathrm{eff}$ shape ($n^2 - Bn\ln n$) | **PROVED** | `rg_nlogn/full_rg_derivation.tex` |
| Gauge invariance | **PROVED** | same |
| Regulator independence | **PROVED** | same |
| $B \approx 21.8$ one-loop | **HEURISTIC** | self-dual radius assumed |
| $B \approx 43.6$ KK+winding | **HEURISTIC** | T-duality assumed |
| $B = 46$ exact | **OPEN** | Gap G137-B |
| $|\Gamma_0(p)\backslash\mathrm{SL}(2,\mathbb{Z})| = p+1$ (arithmetic) | **PROVED** | Diamond & Shurman Thm 3.1.1 |
| $\mathrm{vol}(X_0(p))/\pi = (p+1)/3$ (arithmetic) | **PROVED** | `hecke_equivariant_path_integral.tex` Cor. 2.3 |
| $\mathcal{H}_p$ arithmetically closed under $\Gamma_0(p)$ | **PROVED** (arithmetic) | same, Lem. 6.1 |
| $S[\Theta]$ modular-invariant under $\mathrm{SL}(2,\mathbb{Z})$ | **OPEN** (Obstruction O1) | same, Prop. 5.1 |
| $\mathrm{SL}(2,\mathbb{Z})$ action on winding modes derived | **OPEN** (Obstruction O2) | same, Prop. 6.2 |
| $p+1$ equal-action saddles from $Z_p$ | **OPEN** (Obstruction O3) | same, Prop. 7.2 |
| $B(p) = (p+1)/3$ derived from $S[\Theta]$ via Hecke route | **CONDITIONAL — NO-GO** (O1–O3 unresolved) | `hecke_path_integral_no_go_or_success.md` |
| Modular coincidence $\mu(\Gamma_0(p))/3$ | **OBSERVATION** | `reports/gamma0_137_invariants.md` |
| Self-consistency bootstrap | **COND** | sec. 4 of companion LaTeX |

---

## 4. Verdict by Requirement

| Requirement from task | Finding |
|-----------------------|---------|
| RG derivation consistency | ✅ Shape proved; ❌ coefficient not derived |
| KK+winding estimate $B \approx 43.6$ | ✅ Heuristic; T-duality assumed |
| Missing factor $43.6 \to 46$ | ❌ Unknown; two-loop insufficient ($\Delta B \lesssim 1.4$) |
| Modular index route $\mu(\Gamma_0(p))/3$ | ✅ Numerically correct; ❌ not in $S[\Theta]$ |
| Modular index entering effective action | ❌ No mechanism identified |
| Gauge invariance of $B$ | ✅ $n$ is $\mathrm{U}(1)_\psi$ charge; modular index is arithmetic |
| Regulator dependence | ✅ $\ln n$ coefficient is UV-finite |
| No use of observed $\alpha$ | ✅ Confirmed — no experimental input |

---

## 5. Final Verdict

$$\boxed{B(p) = \frac{p+1}{3} \quad \text{is a CONDITIONAL modular ansatz.}}$$

It is supported by:
- Three structural coincidences (modular index, Chowla–Selberg, bootstrap consistency)
- Strong numerical accuracy (0.04% with Chowla–Selberg value)
- Gauge invariance and regulator independence (of the modular quantity)

It is **not** supported by:
- Any derivation from $S[\Theta]$
- A perturbative calculation (best perturbative value: 43.6, error 5.8%)
- Any identification of a UBT mechanism that produces $\mu(\Gamma_0(n^*))$

---

## 6. Hecke Path-Integral Route: No-Go Result

The priority Hecke-trace attempt (task
`construct_or_kill_hecke_equivariant_winding_path_integral`, 2026-05-09)
has been completed.  Full details are in
`reports/hecke_path_integral_no_go_or_success.md` and the companion LaTeX
`research_tracks/alpha_spectral/hecke_equivariant_path_integral.tex`.

**Verdict: CONSTRUCTION INCOMPLETE — NO-GO at current level.**

Three obstructions block the derivation:

| Label | Obstruction | Severity |
|-------|-------------|----------|
| O1 | $S[\Theta]$ not proved modular-invariant under $\mathrm{SL}(2,\mathbb{Z})$ | **Critical** |
| O2 | $\mathrm{SL}(2,\mathbb{Z})$ action on winding modes $\Theta_n$ not derived | **Critical** |
| O3 | Equal-action of $p+1$ candidate saddles cannot be established (depends on O1) | **Blocking** |

What is exact (arithmetic, unconditional):

- $|\Gamma_0(p)\backslash\mathrm{SL}(2,\mathbb{Z})| = p+1$
- Bijection with $\mathbb{P}^1(\mathbb{F}_p)$
- $\mathrm{vol}(\mathrm{SL}(2,\mathbb{Z})\backslash\mathbb{H}) = \pi/3$
- $B(p) = \mathrm{vol}(X_0(p))/\pi = (p+1)/3$ as an exact geometric identity
  (given $\mathrm{vol}(\mathrm{SL}(2,\mathbb{Z})\backslash\mathbb{H})=\pi/3$, which is a classical result of hyperbolic geometry)

What is NOT derived:

- Any physics mechanism connecting $S[\Theta]$ to the coset count $p+1$
- Equal-action of the $p+1$ candidate saddles
- Multiplication of the $n\ln n$ coefficient by $p+1$

**Impact on Gap G137-B**: Gap is not closed.  The Hecke route is
the most promising known route and it fails at O1.

**Required next lemma**: Prove that the biquaternionic Dirac–Laplace
operator $\nabla^\dagger\nabla$ on the complex-time torus
$\mathbb{C}/(\mathbb{Z}+\mathbb{Z}\tau)$ is a modular-covariant operator
of definite weight, with the measure $d^4x\,d\psi$ (four real spacetime
directions plus the imaginary-time circle $S^1_\psi$) transforming
covariantly under $\tau \to (a\tau+b)/(c\tau+d)$.  An $\eta$-function
regularisation argument (analogous to Polchinski Ch. 7) might resolve O1.

---

## 7. UBT Prime-Stability Framework — Status Statement

> **UBT has a finite prime-stability framework containing alpha-relevant
> primes.**
> The prime-stability analysis with $B(p) = (p+1)/3$ yields the stable
> prime set $S = \{2, 127, 137, 139, 151, 157\}$; the prime 137 is
> stable within this set.
>
> **The remaining gap is deriving $B(p) = (p+1)/3$ from $S[\Theta]$.**
>
> The Hecke-equivariant path-integral route, the most structured known
> approach, is blocked by Obstruction O1 (modular invariance of
> $S[\Theta]$).  **The modular coefficient remains a conditional ansatz.**
>
> Alpha is not solved.  The integer-137 result is structurally motivated
> and internally consistent, but its derivation is incomplete pending
> resolution of Gap G137-B.

---

## 8. Recommended Next Steps

The Hecke-trace mechanism has been attempted and produced a NO-GO.
The recommended programme is:

1. **Resolve O1** (4–8 week time-box): Attempt to prove $\mathrm{SL}(2,\mathbb{Z})$
   invariance of $S[\Theta]$ using $\eta$-function or heat-kernel methods on
   the complex-time torus.  If successful, O2 and O3 resolve consequentially.

2. **If O1 is not resolved**:
   - Publish the prime-stability and integer-137 results as
     **CONDITIONAL** on Gap G137-B.
   - State $B(p) = (p+1)/3$ explicitly as a conditional modular ansatz
     with full supporting evidence.
   - Redirect resources to T1\_GR and T2\_GAUGE tracks.

3. **Check equal action numerically for small $p$**:
   For $p = 2, 3, 5$ compute the classical action $S[\bar\Theta_a]$ for
   each of the $p+1$ coset representatives and verify or falsify equal
   action at leading order.  A counter-example would rule out the route
   without requiring the full modular proof.

**Falsification conditions**:

| Condition | What it falsifies |
|-----------|------------------|
| Two-loop: $B_\mathrm{2-loop} < 44$ | RG perturbative origin |
| $R_\psi \neq 1$ from moduli | Self-dual radius assumption |
| $B(p)$ non-monotone in $p$ | The formula $B=(p+1)/3$ |
| $S[\Theta]$ modular symmetry proved absent | Entire Hecke route |
| Equal action fails at $p=2$ (numerical check) | Saddle-degeneracy mechanism |

---

## 9. References

| Document | Role |
|----------|------|
| `research_tracks/rg_nlogn/full_rg_derivation.tex` | Full RG derivation |
| `research_tracks/rg_nlogn/b_coefficient_analysis.md` | $B$ sensitivity analysis |
| `research_tracks/T3_ALPHA/chowla_selberg_b_derivation.tex` | Chowla–Selberg route |
| `reports/gamma0_137_invariants.md` | Modular curve $X_0(137)$ analysis |
| `reports/alpha_missing_lemma.md` | Precise statement of Gap G137-B |
| `canonical/alpha/best_candidate_derivation.tex` | Derivation chain for $\alpha^{-1}=137$ |
| `research_tracks/alpha_spectral/b_coefficient_gap_resolution.tex` | Synthesis of all B-coefficient routes |
| `research_tracks/alpha_spectral/hecke_equivariant_path_integral.tex` | Hecke route full proofs and obstructions |
| `reports/hecke_path_integral_no_go_or_success.md` | Hecke route verdict (NO-GO) |
