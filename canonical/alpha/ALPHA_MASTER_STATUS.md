<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# ALPHA_MASTER_STATUS.md — T3_ALPHA Canonical Master Status

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T3_ALPHA — Fine Structure Constant  
**Purpose**: Single authoritative file consolidating all alpha-program status.
Supersedes and summarises: `reports/alpha_routes_ranked.md`, `reports/alpha_no_fit_progress.md`,
`reports/alpha_missing_lemma.md`, `canonical/alpha/prime_137_status.md`,
`reports/ew_mixing_status.md` (alpha perspective), `canonical/alpha/ew_mixing_gap_map.md`
(alpha routes only).  
**Truth anchor**: `STATUS_OF_UBT.md §T3_ALPHA`  
**Single canonical reference for chain status**: `canonical/alpha/alpha_gap_closure_matrix.tex`

---

## Objective

Derive α⁻¹_bare = 137 (integer) from UBT without fitting any parameter.  
Full derivation (137.036) requires solving Gap G137-B first.

## Canonical alpha position (authoritative wording)

UBT currently provides a conditional structural route to the bare integer alpha
inverse alpha_bare^{-1} = 137 through a prime winding-mode attractor,
conditional on deriving the effective coupling B ≈ 46.284–46.298 from the UBT
action. This unresolved step is Gap G137-B. The physical correction from 137
to 137.036 is not yet derived from first principles.

**Acceptance criteria**:
1. No number is fitted to reproduce α or 137.
2. Every numerical input is derived from another UBT sector or from S[Θ].
3. Every step is reproducible from a cited proof file.

---

## Current Overall Status

| Item | Verdict |
|------|---------|
| α derivation: overall | **NOT DERIVED** — B-gap open |
| α⁻¹_bare = 137 (integer) | **CONDITIONAL ONLY** — no first-principles closure |
| α⁻¹ = 137.036 (full precision) | **NOT ACHIEVED** — requires Gap G137-B resolution |
| Active routes | 1 (A_PRIME) |
| Parked routes | 2 (A1, A2 — conditional on dead-end Weinberg angle) |
| Killed routes | 2 (A3, A4 — definitively failed) |

### Status sync (2026-05-10 — winding NO-GO update)

- Prime-stability set: **derived**
- B-gap: **open** (fully open after winding NO-GO)
- **Constant winding correction ΔB_wind ≈ 18.5: NO-GO**
  - Derived expression: ΔB_wind(n) = N_eff·n/(12π²) (n-dependent)
  - Produces n²·ln n term in V_eff, not a constant B shift
  - B_best ≈ 43.6 is **OBSOLETE HEURISTIC** — retracted
- Current strongest safe coefficient: **B₀ = 8π ≈ 25.133** (CONDITIONAL on KK matching)
- eta(i) route: **rejected as first-principles B-modifier**; allowed only as numerical observation / partition-normalization clue
- Hecke path-integral route: **current no-go** (until O1–O3 or determinant-to-B insertion is solved)
- Alpha: **not derived**
- Canonical wording source: `reports/alpha_current_verdict.md`
- B-gap summary: `reports/alpha_B_gap_after_winding_no_go.md`

### N_eff audit sync (2026-05-10)

- New critical audit: `canonical/n_eff/step2_AUDIT.tex`
- Current audited position:
  - `N_phases = 3` is proved
  - `N_helicity = 2` and explicit `N_charge = 2` are not yet proved as
    independent one-loop multipliers in the audited scalar-action path
  - loop-safe audited value: `N_eff = 3` (provisional audit result)
- Consequence: T3 alpha route is downgraded to **CONDITIONAL-WEAK** until
  the multiplicity audit and `B0 -> B` bridge are formally closed.
- Bridge file added: `canonical/alpha/B_identification_proof.tex`

### Self-dual torus sync (2026-05-09)

- `tau=i` / `R_t=R_psi`: **CONDITIONAL** only
- Shape stationary point: yes
- Local shape stability: yes (under stated assumptions)
- Scale modulus fixed: **no** (remains open)

### Deprecated / rejected claim register (2026-05-10, updated)

- Rejected as derived first-principles n log n coefficient:
  `B = 12^(3/2)*(2 eta(i))^(1/4)`.
- This expression may be cited only as numerical observation / partition-normalization clue.
- **Constant winding correction ΔB_wind ≈ 18.5: NO-GO.**
  The derived winding term is ΔB_wind(n) = N_eff·n/(12π²) (n-dependent; produces n²·ln n).
- **B_best ≈ 43.6: OBSOLETE HEURISTIC.** Do not cite as an estimate. Route withdrawn.

---

## Route Ranking

### PRIMARY — A_PRIME: V_eff Prime Attractor (Conditional)

**Claim**: α⁻¹_bare = 137 (integer) from winding-mode spectrum V_eff minimum  
**Score**: 10/15  
**Status**: **PRIMARY BUT CONDITIONAL-WEAK**

| Criterion | Score | Notes |
|-----------|-------|-------|
| Foundation depth | 3/3 | N_eff = 12 is [L0]; V_eff structure forced by algebra |
| Independence from α | 2/3 | No α input; $B=(p+1)/3$ used only as a conditional modular ansatz |
| Gap clarity | 2/3 | Gap G137-B remains open; no first-principles derivation of B from S[Θ] |
| Corroborations | 3/3 | V_eff attractor + modular μ(Γ₀(137))/3 + Hecke lepton masses |
| Path to completion | 0/3 | eta(i) and Hecke path-integral first-principles routes rejected/no-go |

**What is proved** (no fitting, zero free parameters):

| Claim | Level | Source |
|-------|-------|--------|
| N_eff = 12 from ℂ⊗ℍ algebra alone | OPEN / [MC] (under critical audit) | `canonical/n_eff/step2_AUDIT.tex` |
| V_eff(n) = n² − B·n·ln n structure | [L1] | `canonical/alpha/alpha_best_route.tex` |
| n*(B_phenom) = 137 for B_phenom ≈ 46.298 | [L1] (given B) | `canonical/alpha/alpha_best_route.tex` |
| 137 is prime — consistent with V_eff stability | [L0]+[STD] | Number theory |
| B₀ = 8π from S_kin[Θ] (one-loop) | [L1] | `canonical/t_munu/` |
| ΔB_wind ≈ 18.5 (constant) | **NO-GO** | `reports/t_dual_winding_verdict.md` |
| B_best ≈ 43.6 | **OBSOLETE HEURISTIC** | Withdrawn after winding NO-GO |

**What is open** (Gap G137-B, updated after winding NO-GO):  
- Derive B_phenom ≈ 46.298 from UBT action S[Θ] without using α as input.
- B₀ = 8π (proved, one-loop) gives n* ≈ 65, not 137.
- The constant winding correction ΔB_wind ≈ 18.5 is **NO-GO** (correction is n-dependent).
- B_best ≈ 43.6 is **OBSOLETE HEURISTIC**: do not use.
- The strongest safe coefficient is B₀ = 8π (CONDITIONAL on KK matching).
- Missing mechanism: must bridge B₀ = 8π → B ≈ 46 without fitting.
- The relation $B=(p+1)/3$ is currently a conditional modular ansatz, not a first-principles derivation.
- Source: `reports/alpha_missing_lemma.md`, `reports/alpha_B_gap_after_winding_no_go.md`

**Corroborations** (not proofs, supporting evidence):

| Signal | Value | Significance |
|--------|-------|--------------|
| μ(Γ₀(137))/3 | ≈ 46.00 (0.64% from B_phenom) | Independent structural signal |
| Hecke eigenvalue → lepton mass ratios | 0.02–0.1% accuracy | Independent of V_eff |
| P¹(𝔽₁₃₇) cardinality = μ(Γ₀(137)) | Exact identity | Number-theoretic self-consistency |

**Kill condition**: A_PRIME is killed if audited multiplicity closure cannot recover
a first-principles path compatible with the alpha objective.

---

### PARKED — A1: Gauge Normalization

**Status**: PARKED — conditional on Gap EW-1 (Weinberg angle — **DEAD END**)  
**Score**: 7/15

**Blocker**: Requires sin²θ_W from algebra (Gap EW-1).  Gap EW-1 = DEAD END.  
**Revival condition**: Only if Gap EW-1 is somehow closed in T2_GAUGE track.  
**Active priority**: ZERO.

---

### PARKED — A2: Symmetry-Breaking Projection

**Status**: PARKED — same blocker as A1 (EW-1 + EW-2)  
**Score**: 7/15

**Blocker**: EW-1 (DEAD END) and EW-2 (OPEN).  
**Active priority**: ZERO.

---

### KILLED — A3: Theta/Modular Route

**Status**: **DEFINITIVELY FAILED**  
**Score**: 3/15

**Failure**: Exhaustive search over modular invariants, Hecke eigenvalues, j-invariants,
and eta functions found no expression equal to α⁻¹ = 137.036.  
**Archive**: `reports/failed_routes_graveyard.md`  
**Active priority**: ZERO — closed permanently.

---

### KILLED — A4: Layer 2 Coding Constraint

**Status**: **DEFINITIVELY FAILED**  
**Score**: 2/15

**Failure**: Proved impossible — coding constraints fix charge spectrum (integer or
half-integer multiples of a unit charge), not the magnitude of the unit charge.
α = e²/(4π) requires coupling magnitude, which depends on UV cutoff and renormalization
scheme — neither determined by coding constraints.  
**Archive**: `reports/failed_routes_graveyard.md`  
**Active priority**: ZERO — closed permanently.

---

### SUPPORTING (Not a Bare-α Route) — A5: One-Loop QED Running

**Status**: SUPPORTING RESULT only  
**Score**: 8/15

**Value**: Validates QED sector of UBT; reproduces SM one-loop running α(μ₂) from α(μ₁).  
**Limitation**: Uses α as input; cannot determine bare α from first principles.  
**Source**: `canonical/interactions/qed.tex`

---

## Summary Ranking Table

| Rank | Route | Score | Status | Claim |
|------|-------|-------|--------|-------|
| 1 | **A_PRIME**: V_eff prime attractor | **10/15** | **PRIMARY BUT CONDITIONAL** | α⁻¹_bare = 137 (integer), conditional on G137-B |
| 2 | A5: One-loop running | 8/15 | SUPPORTING (not bare-α) | α(μ₂) from α(μ₁) |
| 3 | A1: Gauge normalization | 7/15 | PARKED (EW-1 dead end) | α after θ_W fixed |
| 4 | A2: Symmetry-breaking projection | 7/15 | PARKED (EW-1+EW-2) | α after SSB |
| 5 | A3: Theta/modular | 3/15 | **KILLED** | Failed |
| 6 | A4: Layer 2 coding | 2/15 | **KILLED** | Failed (proved impossible) |

---

## Next 30-Day Attack Plan (Updated 2026-05-10)

### Deliverables created (2026-05-10)

All three deliverables for the go/no-go gate are now ready:

| File | Path | Status |
|------|------|--------|
| Path A: modular bootstrap attempt | `research_tracks/T3_ALPHA/modular_bootstrap_attempt.tex` | ✅ Created |
| Path B: ζ-function regularisation | `research_tracks/T3_ALPHA/zeta_regularisation_B.tex` | ✅ Created |
| Path C: conditional companion note | `research_tracks/T3_ALPHA/conditional_alpha_note_draft.tex` | ✅ Created |

### Current gap status (2026-05-10)

**Path A result**: Crossing symmetry on T² is set up; the Virasoro block
decomposition is the next step.  Even if k_KM = 1 is confirmed, the result
gives B_base ≈ 41.6, not 46.3.  A further mechanism is needed (open).

**Path B result**: ζ-function regularisation on T³ × S¹_ψ gives B_ζ ≈ 41.6
at leading order — same as Path A.  The 10% discrepancy to B_phenom ≈ 46.3
has no identified mechanism from one-loop zeta regularisation.

**Path C**: Conditional companion note is ready for submission at go/no-go
gate (2026-05-27) regardless of Paths A and B outcome.

### Week 1–4: Modular Bootstrap on Gap G137-B

**Target**: Derive B = μ(Γ₀(n*))/3 from S[Θ] evaluated at n* = 137.

**Approach**:
1. Compute S[Θ] for the winding-mode ansatz at n = 137.
2. Evaluate the Kac-Moody level k from the WZW boundary term.
3. Check if k = 1 follows from the boundary structure of S[Θ].
4. Alternatively: evaluate one-loop correction beyond B₀ = 8π using
   heat-kernel on S¹_ψ × M⁴.

**Resources**:
- `reports/alpha_missing_lemma.md` — exact formulation of G137-B
- `canonical/t_munu/` — B₀ = 8π derivation (starting point)
- `canonical/alpha/alpha_best_route.tex` — V_eff derivation chain
- `reports/prime_137_structural_audit.md` — corroborations

**Go/no-go at Week 4 (2026-05-27)**:
- **If solved** → write T3_ALPHA paper; claim α⁻¹_bare = 137 at [L1]; submit as
  companion note to T1_GR.
- **If not solved** (70–80% probability) → publish conditional integer-137 note
  (`research_tracks/T3_ALPHA/conditional_alpha_note_draft.tex`) with Gap G137-B
  explicitly stated; downgrade T3_ALPHA from flagship to STRUCTURAL EVIDENCE
  status; redirect effort fully to T2_GAUGE.

---

## What Is Not Being Pursued

| Route | Reason |
|-------|--------|
| Weinberg angle derivation | DEAD END — algebra cannot fix g'/g |
| Route A3 (modular direct) | KILLED — exhaustive search failed |
| Route A4 (coding) | KILLED — proved impossible |
| eta(i) insertion as derived B-modifier | REJECTED — not first-principles derivation of n log n coefficient |
| δ = 0.036 correction without α | CIRCULAR — uses α as input |
| R_ψ calibration from m_e | SEMI-EMPIRICAL — breaks unit-free derivation |
| Constant winding correction ΔB_wind ≈ 18.5 | **NO-GO** — derived correction is n-dependent; B_best ≈ 43.6 is OBSOLETE HEURISTIC |
| New speculative routes | FORBIDDEN — no new branches in cleanup window |

---

## Source Files

| Purpose | File |
|---------|------|
| Full route ranking with scores | `reports/alpha_routes_ranked.md` |
| Primary route detail | `canonical/alpha/PRIMARY_ROUTE.md` |
| Gap G137-B exact statement | `reports/alpha_missing_lemma.md` |
| Prime 137 structural roles | `canonical/alpha/prime_137_status.md` |
| Failed routes archive | `reports/failed_routes_graveyard.md` |
| V_eff derivation chain | `canonical/alpha/alpha_best_route.tex` |
| No-fit audit | `reports/alpha_no_fit_audit.md` |
| No-fit progress | `reports/alpha_no_fit_progress.md` |

---

## Nová strategie po revizi 2026-05-10

### Identifikovaný kořenový problém

$V_\mathrm{eff}(n) = n^2 - B \cdot n \ln n$ selektuje $n^*=137$ pouze pro
$B \approx 46.28$.  $B$ není odvozeno → selekce je quasi-arbitrary (volný parametr).

Přesněji:
- $V_\mathrm{CW}(n) = n^2 - N_\mathrm{eff}\ln(2\sinh(\pi n))$ bez volného $B$
  dává minimum u $n^*\approx 19$ pro $N_\mathrm{eff}=12$.
- Pro $n^*=137$ by bylo potřeba $N_\mathrm{eff}\approx 87.2$ (gap faktor $7.27$).
- Kombinace $V_\mathrm{CW} + V_\mathrm{modulární}$ s přirozeným $C$ nestačí.

### Tři nové přístupy (seřazeno dle priority)

| Přístup | Soubor | Stav | Výsledek |
|---------|--------|------|---------|
| A: Self-konzistentní pevný bod | `research_tracks/T3_ALPHA/self_consistency_fixed_point.tex` | HOTOVO [MC] | $n^*(B(p))=p$: $p=137$ přibližně ($0.56\%$); není unikátní (twin-prime okno $\{137,139\}$) |
| B: Hecke eigenvalue → α | `research_tracks/T3_ALPHA/hecke_alpha_connection.tex` | HOTOVO [MC] | Přímý výpočet: $a_{131}=-9$, $a_{137}=-11$, $a_{139}=-3$; shoda unikátní pro $p=137$ |
| C: Exaktní $V_\mathrm{CW}$ bez $B$ | `research_tracks/T3_ALPHA/vcw_exact_minimum.tex` | HOTOVO [L1/OPEN] | Minimum u $n^*=19$ ($N_\mathrm{eff}=12$); faktor $7.27$ zbývá; žádná přirozená kombinace nedá $n^*=137$ |

### Podrobné výsledky

**Přístup A — self-konzistence**:
- Nejbližší fixed point (základní $B_\mathrm{mod}$): $p=139$, $|\delta|=0.636$.
- $p=137$: $|\delta|=1.011$ (základní), $|\delta_r|=0.770$ (refinovaná s $\nu_2/4$).
- Algebraická podmínka $(5p-1)/(p+1)=\ln p$ se kříží mezi $p=137$ a $p=139$ ($p_0\approx 138.5$).
- Selekce twin-prime okna $\{137,139\}$ — ne unikátně $p=137$.
- Potřeba doplňujícího mechanismu (Hecke nebo odvození $B$ z $S[\Theta]$).

**Přístup B — Hecke**:
- $|a_{137}(N=76, k=2)| = 11 = g(X_0(137))$: numericky pravdivé.
- Přímý výpočet z Weierstrassova modelu $[0,-1,0,-21,-31]$:
  $a_{131}=-9$, $a_{137}=-11$, $a_{139}=-3$.
- Primes s $g=11$ v $[50,300]$: $\{131, 137, 139\}$; shoda $|a_p|=11$ je unikátní pro $p=137$.
- Kill condition pro přístup B: nesplněna. $p=137$ je unikátní v $\{131,137,139\}$.
- Lepton mass ratios potvrzeny: $R_\mu=2274/11=206.73$ (exp 206.77, 0.02\%),
  $R_\tau=38286/11=3480.55$ (exp 3477.23, 0.10\%) — silný [MC] signál.
- Struktura Hecke $\to \alpha$ path-integral: no-go status (viz `reports/hecke_path_integral_no_go_or_success.md`).

**Přístup C — $V_\mathrm{CW}$**:
- $V_\mathrm{CW}$ minimum ($N_\mathrm{eff}=12$): $n^*=19$ (prvočíslo). [L1]
- $N_\mathrm{eff}$ potřebné pro $n^*=137$: $87.2$ (gap $7.27$). [L0]
- Modulární korekce $C$ potřebná: $354.9$ (přirozené $C_\mathrm{nat}\approx 12.6$; poměr $28\times$). [L0]
- $V_\mathrm{combined}$ minimum s $C=354.9$: $n^*=79$ — nedosáhne $137$.
- Přístup C sám nedokáže uzavřít gap.

### Aktuální nejpřesnější predikce α

Predikce $\alpha^{-1}=137$ zůstává podmíněná: Route A\_PRIME je živá ale [CONDITIONAL-WEAK].
Žádný z přístupů A, B, C sám neuzavírá gap G137-B.
Lepton mass Hecke signál (přístup B) je nejsilnější numerický signál — ale bez UBT derivace forem.

### Kill conditions (aktualizováno 2026-05-10)

- **Přístup A je zabit pokud**: přesná podmínka $(5p-1)/(p+1)=\ln p$ nemá žádné blízké prvočíselné řešení — **NEVZNIKÁ**, podmínka je blízko pro $\{137,139\}$.
- **Přístup A je degradován pokud**: twin-prime degenerace $\{137,139\}$ nelze prolomit dalšími UBT mechanismy.
- **Přístup B je zabit pokud**: $a_{131}(N=76,k=2) = -11$ nebo $a_{139}(N=76,k=2)=-11$ (shoda pak není specifická pro $p=137$). Kill condition **NESPLNĚNA**: $a_{139}=-3$ [L0]; přímý výpočet z Weierstrassova modelu $[0,-1,0,-21,-31]$. Status přístupu B: **[MC/confirmed — twin-prime test passed]**.
- **Přístup C je zabit**: Přístup C nemůže dát $n^*=137$ s přirozenými konstantami. **KILL CONDITIONS SPLNĚNY** pro přístup C jako samostatnou cestu.

### Doporučená priorita (po 2026-05-10)

1. LMFDB/Sage ověření: $a_{131}(N=76,k=2)$ a $a_{139}(N=76,k=2)$ — rozhodne o přístupu B
   (`reports/hecke_eigenvalue_twin_prime_test.md`, aktuálně [OPEN]).
2. Derivace $B_\mathrm{mod}(p)=(p+1)/3$ z $S[\Theta]$ — uzavření gap G137-B pro přístup A.
3. Kac-Moody level $k\approx 7$ hypotéza — mohla by dát $N_\mathrm{eff}^\mathrm{eff}\approx 84$ pro přístup C.

---

## Selekční kritéria p=137 (aktualizace 2026-05-11, Copilot Instrukce v6)

Mezi prvočísly s $g(X_0(p))=11$ (tj. $\{131,137,139\}$) jsou aktuálně:

1. **Kronecker filtr**: $\nu_2(p)>0 \Leftrightarrow p\equiv1\pmod4$.
   - Arithmeticky [L0], v klastru $g=11$ vybírá jednoznačně $p=137$.
   - Fyzikální most $C\leftrightarrow w_p$ (charge-conjugation $\to$ Atkin-Lehner):
     prověřen v `research_tracks/T3_ALPHA/charge_conjugation_wp_bridge.tex`.
     **Verdikt C (NO-GO pro přímou derivaci)**: přímá identifikace $\tau_C = w_p$
     selhává (fixed-point count je konstantní, nezávisí na $p$).
     Modularní cesta (přes Eulerovu charakteristiku $X_0(p)$) je [OPEN],
     závisí na uzavření Gap G137-B.

2. **Self-konzistence**: $f(p)=\frac{5p-1}{p+1}-\ln p$.
   - $f(137)=+0.036541$, $f(139)=+0.022669$.
   - Obě hodnoty jsou kladné, proto znaménkový test sám o sobě
     137 od 139 neodděluje (selection FAIL pro tuto verzi testu).

3. **Residuum vs QED**:
   - Pozorování: $f(137)\approx\Delta\alpha^{-1}_{\mathrm{exp}}$ (1.5% rozdíl; post-check).
   - Jednosmyčkový leptonic model s $\Lambda=M_{\mathrm{Pl}}$ dává
     $\sum\Delta_{\mathrm{QED}}=0.114595$, což je od $f(137)$ vzdálené
     o 68.1% $\Rightarrow$ [NC] pro tuto identifikaci.

4. **Hecke prime-specificity**:
   - $a_{137}(N=76,k=2)=-11$ je známé.
   - $a_{131}=-9$, $a_{139}=-3$: přímý výpočet [L0] z Weierstrassova modelu $[0,-1,0,-21,-31]$.
   - $|a_{137}|=g=11$ je unikátní v $\{131,137,139\}$ $\Rightarrow$ **[MC/confirmed]**.

**Aktuální souhrn (2026-05-11)**:
- Hecke prime-specificity: **[MC/confirmed]** — kill condition nesplněna ($a_{139}=-3 \neq \pm11$).
- Kronecker filtr: arithmeticky [L0]; fyzikální most [NO-GO pro přímou cestu], [OPEN] pro modularní.
- Selekce $p=137$ celkově: **[MC] — strengthened po Hecke ověření**, fyzikální základ [OPEN].
