<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# PRIORITIES_2026.md — UBT Strategic Research Priorities

> **DEPRECATED / SUPERSEDED STATUS: This document contains pre-audit alpha claims. Current alpha status is given by STATUS_OF_UBT.md and canonical/alpha/ALPHA_MASTER_STATUS.md.**
> Audit references: `canonical/alpha/gamma_entropy_alpha_refinement_status.tex`, `reports/gamma_entropy_alpha_interpolation_audit.md`.


**Author**: Ing. David Jaroš  
**Generated**: 2026-04-27  
**Basis**: Full repository audit — DERIVATION_INDEX.md, canonical/, research_tracks/, experiments/, docs/

> **Purpose**: Define the highest-value next research priorities.  
> Convert UBT from a broad framework into a focused high-impact program.  
> Be brutally honest. Prefer depth over breadth.

---

## Section 1 — Executive Summary

### 1.1 Current Maturity Level

**Overall: Strong Partial — publication-ready in two sectors, open in three.**

UBT is a structurally coherent unified field theory with a locked axiom system and a
substantial body of proved results at the [L0]–[L1] level.  It is **not** a loose
collection of speculative claims.  The repository contains genuine mathematical
theorems with zero free parameters in several sectors.

**Maturity by sector:**

| Sector | Maturity | Publication-readiness |
|--------|----------|----------------------|
| Biquaternion algebra foundations | Strong | Ready |
| GR recovery (Steps 1–5, Schwarzschild, Regge-Wheeler) | Strong Partial | Near-ready |
| SM gauge structure SU(3)×SU(2)_L×U(1)_Y | Strong Partial | Near-ready |
| QM/GR/stat-mech unification from single field eq. | Strong Partial | Near-ready |
| Fine structure constant α | Open | Not yet (B_base gap) |
| Lepton mass spectrum | Open | Not yet |
| Higgs/Yukawa sector | Candidate | Not yet (λ gap ×11) |
| Mirror sector | Candidate | Not yet |
| CMB/coding fingerprints | Experimental | Speculative |

### 1.2 Main Strengths

1. **SM gauge group proved from first principles** — SU(3) via involutions (two independent routes), SU(2)_L from left automorphisms, U(1)_Y from right action, U(1)_EM from ψ-cycle phase; all with zero free parameters at [L0].
2. **GR recovery is essentially complete** — Schwarzschild metric, linearized gravity, Regge-Wheeler (odd-parity graviton), and Steps 1–5 of the Einstein chain all proved [L1].  Off-shell compact M⁴ and Zerilli (even-parity) remain open.
3. **QM emergence is rigorous** — Born rule, Dirac equation (massless), Schrödinger projection, and QM/GR/statistical mechanics as three projections of one field equation all proved with no extra postulates.
4. **N_eff = 12 and B₀ = 8π derived with zero free parameters** — strongest numerical scaffold for the α derivation.
5. **Disciplined housekeeping** — speculative content is isolated; DERIVATION_INDEX.md faithfully labels proved vs. open; dead ends are documented.

### 1.3 Main Bottlenecks

1. **B_base coefficient (α derivation)** — B_base = N_eff^{3/2} = 41.57 is partially proved but k=1 (Kac-Moody level) remains a motivated conjecture; 27+ approaches exhausted; correction factor R≈1.114 is an Open Hard Problem.
2. **Lepton mass ratios** — KK mismatch theorem *proves* the torus winding formula cannot reproduce the factor-207 mass jump; no mechanism found yet.
3. **Higgs/Yukawa λ gap ×11** — radiative Hosotani is partially proved but the quartic coupling is off by an order of magnitude.
4. **Weinberg angle** — confirmed Dead End from ℂ⊗ℍ algebra alone.
5. **No arXiv preprint yet** — the work is not visible to the community; reproducibility and priority remain unestablished.

### 1.4 Strategic Direction Recommendation

**Shift from exploration to consolidation and publication.**

The theory has enough proved results to support at least two or three strong papers
that would establish UBT in the literature.  The highest-value use of the next 12
months is:

1. Write and submit the three publication-ready papers (gauge structure, GR, QM).
2. Focus the α effort on a *single* new algebraic route rather than repeating the
   exhausted B_base approaches.
3. Freeze the Hecke bridge exploration at its current numerical result and await
   LMFDB verification.
4. Stop maintaining the CMB fingerprint track as a core research priority.

**One flagship path is clearly strongest**: the SM gauge structure paper —
`SU(3)×SU(2)_L×U(1)_Y from Biquaternion Algebra` — is the highest credibility move
available right now.

---

## Section 2 — Ranked Research Priorities (1–10)

---

### Priority 1 — Write and Submit the SM Gauge Structure Paper

**Title**: *Emergence of SU(3)×SU(2)_L×U(1)_Y from Biquaternion Algebra ℂ⊗ℍ*

**Why it matters**  
This is the result most likely to survive peer review intact.  All three gauge factors
are algebraically derived from ℂ⊗ℍ with zero free parameters:
- SU(3) from ℤ₂×ℤ₂ involutions on ℂ⊗ℍ (Theorems G.A–G.D, two independent proofs)
- SU(2)_L from left automorphisms; U(1)_Y from right action; U(1)_EM from ψ-cycle phase
- Eight Gell-Mann generators verified numerically; color confinement structural argument

No other published framework derives the *full* SM gauge group from a single algebra
without introducing the gauge group as an external input.

**Expected scientific impact**: High.  This is a publishable theorem in mathematical
physics, independent of whether the rest of UBT is correct.

**Difficulty**: Low (proofs exist; requires writing and internal consistency check).

**Time to meaningful result**: 6–8 weeks to draft; 3–4 months to submission.

**Dependencies**: None.  Stand-alone result.

**Credibility gain if solved**: Very high.  Establishes UBT as a serious mathematical
program in the literature.

---

### Priority 2 — Write and Submit the GR Recovery Paper

**Title**: *General Relativity as a Real-Projected Limit of Unified Biquaternion Theory*

**Why it matters**  
Steps 1–5 of the GR chain (Θ→g→Γ→R→Einstein) are proved [L1].  Linearized GR,
Schwarzschild metric (spatial + temporal), and odd-parity graviton (Regge-Wheeler)
are all proved.  The Lorentzian signature emerges from AXIOM B without choice.
The story is logically complete enough for a focused paper.

**Expected scientific impact**: High.  GR recovery from a unified field theory with
explicit Schwarzschild and graviton results is directly comparable to published
work in string theory and loop quantum gravity.

**Difficulty**: Low-Medium.  Proofs exist; writing + Zerilli limitation must be stated
clearly.

**Time to meaningful result**: 8–10 weeks to draft.

**Dependencies**: Priority 1 can be done in parallel.

**Credibility gain if solved**: High.  Gravitational physics community will recognize
the Regge-Wheeler result.

---

### Priority 3 — Write and Submit the QM Emergence Paper

**Title**: *Quantum Mechanics, General Relativity, and Statistical Mechanics as
Projections of a Single Biquaternionic Field Equation*

**Why it matters**  
The FPE ↔ Euler-Lagrange equivalence is proved in all sectors (U(1), SU(2), SU(3)).
The Born rule is proved without postulate.  The massless Dirac equation is proved.
QM/GR/stat-mech as three projections (Re, Im, full) of ∂_TΘ = D∇²Θ is a strong
and precise unification statement.

**Expected scientific impact**: Medium-High.  The Born rule derivation alone is noteworthy.

**Difficulty**: Low-Medium.  Gap S1 (diffusion coefficient ℏ/2m) is partially closed
by dimensional analysis; this limitation must be stated explicitly.

**Time to meaningful result**: 6–8 weeks to draft.

**Dependencies**: Priority 1–2 can run in parallel.

**Credibility gain if solved**: Medium-High.  Quantum foundations community is an
accessible target audience.

---

### Priority 4 — Close the B_base Gap via a Genuinely New Route

**What**: Derive B_base = N_eff^{3/2} = 41.57 rigorously — specifically, fix the
Kac-Moody level k = 1 (Gap G3-k) from S[Θ] without circular reference to n*.

**Why it matters**  
If B_base is proved, then N_eff=12, B₀=8π, and B_base are all zero-parameter results,
making α⁻¹=137 a *first geometric derivation of the fine structure constant* — one of
the most significant results in theoretical physics.

**Honest assessment of current state**:  
27+ approaches have been tried and documented; the most recent positive result is
k=1 as a *motivated conjecture* from CS-term absence (H2 approach).  The two-loop
correction R≈1.114 (ΔB=3π/2 candidate) is a motivated conjecture only.  The approach
has been exhaustive.  Repeating variants of exhausted routes is not productive.

**Recommended strategy**:  
Stop exhaustive search on known approaches.  Identify *one* new route that has not
been tried:
- Modular bootstrap: compute the partition function Ẑ(τ) = ϑ₃³(τ) modular weight 3/2
  and derive k from the crossing symmetry constraint directly.
- Verlinde formula approach on the ψ-circle CFT.
- Formal Witten-type argument from the WZW-model at the self-dual point.

**Expected scientific impact**: Transformative if closed.  Historic if α is derived
from first principles with zero parameters.

**Difficulty**: Very High.  27 approaches have failed; this is an Open Hard Problem.

**Time to meaningful result**: 3–6 months for a focused new approach.

**Dependencies**: Requires Priority 1–3 to be submitted first so the community can
evaluate the underlying framework.

**Credibility gain if solved**: Maximum.

---

### Priority 5 — Complete the Zerilli Even-Parity Graviton Derivation

**What**: Derive the Zerilli master equation from UBT perturbation theory.  The
odd-parity (Regge-Wheeler) is proved; the even-parity off-diagonal spin-connection
term (+20M/r³ gap) is the remaining piece.

**Why it matters**  
Completing both parities would give the *full* graviton spectrum in a Schwarzschild
background from UBT — a strong quantitative result for the GR paper and follow-up.

**Difficulty**: Medium-High.  The structure is set up (§8.2 of
`graviton_schwarzschild.tex`); the off-diagonal V₀₁ spin-connection computation is
the explicit missing step.

**Time to meaningful result**: 4–6 weeks once focused.

**Dependencies**: Can be done in parallel with Priority 2 writing.

**Credibility gain if solved**: High for the GR paper.

---

### Priority 6 — Complete the Hecke/Lepton Non-CM Form Search

**What**: Search the LMFDB database for non-CM weight-6 modular forms at levels
N ∈ [50, 500] that match the Hecke eigenvalue pattern (a₁₃₇ = 81400 ± 10%).

**Why it matters**  
The numerical result is already striking: p=137 is the unique global hit in [50,300]
for Set A; p=139 for Set B (mirror sector); 47 other primes fail.  Finding the
corresponding non-CM form would establish the Hecke bridge algebraically and provide
a path to three-generation mass ratios without free parameters.

**Difficulty**: Medium.  Requires LMFDB API access or SageMath computation;
infrastructure exists (nonCM_search_results.json, step6_nonCM_search.tex).

**Time to meaningful result**: 2–4 weeks once computational access is arranged.

**Dependencies**: Independent of Priorities 1–5.

**Credibility gain if solved**: High.  Connection to automorphic forms would attract
number theory community attention.

---

### Priority 7 — Resolve the R_ψ Two-Scale Discrepancy

**What**: Derive the factor ~10.4 between R_ψ^α (α-sector) and R_ψ^EW (Higgs VEV
sector) from renormalization group running between electroweak scale and the α-scale.

**Why it matters**  
Until this is resolved, both the α derivation and the Higgs/Yukawa sector remain
semi-empirical.  The discrepancy is fully characterized algebraically (§8.4 of
hosotani_higgs.tex); what is missing is a physical explanation of the factor 10.4.

**Difficulty**: High.  Requires two-loop RG running computation bridging two distinct
physical scales.

**Time to meaningful result**: 2–4 months.

**Dependencies**: Depends on closing the λ Hosotani gap; can run in parallel with B_base effort.

**Credibility gain if solved**: Medium-High.  Closes the largest open semi-empirical gap in the Higgs sector.

---

### Priority 8 — Fermionic Statistics: Spin Eigenvalue from KK Soliton

**What**: Complete the spin eigenvalue computation from the Noether angular-momentum
operator for odd-winding KK modes (the Grassmannian measure is already proved [L1]).

**Why it matters**  
Closing this gap would prove spin-statistics from first principles in UBT — a strong
result for the QM paper.

**Difficulty**: Medium.  Angular-momentum operator structure is known; Noether charge
computation on a soliton state is technical but tractable.

**Time to meaningful result**: 3–5 weeks.

**Dependencies**: Can be included in Priority 3 paper.

**Credibility gain if solved**: Medium.

---

### Priority 9 — Establish a Clear Falsifiability Prediction for the Mirror Sector

**What**: Derive a quantitative, unique prediction of the mirror sector (p=139 vacuum)
that is distinguishable from ΛCDM and from dark matter candidates at other mass scales.
Specifically: compute the mirror matter mass spectrum and gravitational lensing
signature.

**Why it matters**  
The mirror sector is currently a motivated conjecture.  A specific falsifiable prediction
would transform it into a scientific hypothesis.  The Foot-Volkas mirror dark matter
precedent exists; UBT can make a sharper prediction via the twin-prime vacuum structure.

**Difficulty**: High.  Requires completing the mirror sector Higgs mechanism and
coupling structure.

**Time to meaningful result**: 3–6 months.

**Dependencies**: Depends on Priority 7 (R_ψ) and partially on Higgs sector.

**Credibility gain if solved**: High for the experimental physics community.

---

### Priority 10 — Archive and Freeze the CMB Coding Fingerprint Track

**What**: Write a single definitive document summarizing the L2S (Hamming) and L2T
(Gray) fingerprint hypotheses, the current statistical evidence, and the requirements
for a falsifiable test.  Then freeze further development of this track until the
theoretical foundation (B_base, generation structure) is proved.

**Why it matters**  
The coding fingerprint track currently consumes research energy without strengthening
the core theory.  The positive CMB detection result (p < 0.01 syndrome-zero fraction)
is intriguing but:
- It is not a first-principles UBT prediction
- The detection significance is not yet peer-reviewed
- Continued expansion of the track risks the appearance of post-hoc fitting

A frozen reference document preserves the result for future evaluation without
diluting the core program.

**Difficulty**: Low (document writing).

**Time to meaningful result**: 2–3 weeks.

**Dependencies**: None.

**Credibility gain**: Medium (negative credibility is avoided by not over-claiming).

---

## Section 3 — Flagship Result Candidates

> Ranked by strategic value: **one best path is identified explicitly**.

---

### 🏆 Flagship #1 (RECOMMENDED NOW): SU(3)×SU(2)_L×U(1)_Y Derivation

**Candidate**: SM gauge structure from ℂ⊗ℍ — publication of the proved theorem.

| Criterion | Assessment |
|-----------|-----------|
| Chance of success (paper accepted) | **High** (70–80%) — proofs exist; referee could challenge notation or completeness of confinement claim, but core theorem is rigorous |
| Impact if true | **Very High** — first algebraic derivation of full SM gauge group from a single algebra |
| Reviewer interest | **High** — mathematical physics, gauge theory communities |
| Risk of failure | **Low** — confinement remains Clay Prize; this is clearly stated as a gap; other results stand independently |
| Recommendation | **Publish NOW** (Q2–Q3 2026) |

---

### Flagship #2 (RECOMMENDED NOW): GR Recovery Paper

**Candidate**: GR recovery chain + Schwarzschild + Regge-Wheeler from UBT.

| Criterion | Assessment |
|-----------|-----------|
| Chance of success | **High** (65–75%) — results are technically solid; reviewers will ask about Zerilli |
| Impact if true | **High** — explicit GR solutions from a unified framework |
| Reviewer interest | **High** — gravitational physics community |
| Risk of failure | **Low** — Zerilli gap can be stated honestly without invalidating other results |
| Recommendation | **Publish NOW** (Q2–Q3 2026), with Zerilli as stated open problem |

---

### Flagship #3 (RECOMMENDED SOON): Fine Structure Constant Derivation

**Candidate**: α⁻¹ = 137 from ℂ⊗ℍ with zero free parameters.

| Criterion | Assessment |
|-----------|-----------|
| Chance of success | **Medium** (30–40%) — N_eff=12 and B₀=8π are proved; B_base k=1 is a motivated conjecture; R≈1.114 is open hard |
| Impact if true | **Transformative** — historic result; would immediately attract broad attention |
| Reviewer interest | **Very High** — but also highest skepticism |
| Risk of failure | **Medium** — current state is semi-empirical; submitting prematurely risks rejection and reputation damage |
| Recommendation | **NOT YET** — close B_base gap first; then submit as highest-priority standalone paper |

---

### Flagship #4 (LATER): Lepton Mass Spectrum Derivation

**Candidate**: Derive e/μ/τ mass ratios from Hecke eigenvalues at p=137.

| Criterion | Assessment |
|-----------|-----------|
| Chance of success | **Low-Medium** (20–30%) — numerical signal is remarkable; algebraic connection not yet established; non-CM form not found |
| Impact if true | **Very High** — particle mass prediction is the holy grail |
| Reviewer interest | **Very High** |
| Risk of failure | **High** — Hecke connection is a conjecture; instanton approach (Option C) has failed; no mechanism reproduces ratio 207 |
| Recommendation | **LATER** (pending Hecke non-CM form search, Priority 6) |

---

### Flagship #5 (LATER): CPT / Symmetry Completion

**Candidate**: Derive CPT and full parity structure from UBT ψ-parity mechanism.

| Criterion | Assessment |
|-----------|-----------|
| Chance of success | **Medium** (40%) — ψ-parity as γ⁵ is proved; chirality selection is conditional (Gap C1) |
| Impact if true | **Medium** — important for SM completeness |
| Reviewer interest | **Medium** |
| Risk of failure | **Medium** — Gap C1 (no W_R in S[Θ]) is an assumption |
| Recommendation | **LATER** (after gauge structure paper establishes the framework) |

---

### Flagship #6 (LATER): SU(3) Gauge / 3-Qubit Equivalence Theorem

**Candidate**: Formalize the one-hot triqubit ↔ SU(3) color mapping.

| Criterion | Assessment |
|-----------|-----------|
| Chance of success | **Medium-High** (50%) — Lie algebra homomorphism verified (51 tests); separate from mainline |
| Impact if true | **Medium** — interesting for quantum information community |
| Reviewer interest | **Medium** |
| Risk of failure | **Low** — already a valid mathematical result; question is physical interpretation |
| Recommendation | **LATER** — low priority relative to main papers; include as appendix in SM paper |

---

### Flagship #7 (SPECULATIVE): Strong CMB Fingerprint Reproducible Result

**Candidate**: Publish the L2S Hamming (8,4,4) CMB positive detection.

| Criterion | Assessment |
|-----------|-----------|
| Chance of success | **Low** (15–25%) — statistical signal exists; but (a) not a UBT first-principles prediction; (b) no algebraic proof; (c) high risk of data-fitting criticism |
| Impact if true | **High** — would be extraordinary |
| Reviewer interest | **High skepticism** |
| Risk of failure | **Very High** — risk of damaging the credibility of the rest of UBT |
| Recommendation | **DO NOT publish as UBT flagship** until algebraic grounding exists; maintain as research track only |

---

### Flagship #8 (NOT RECOMMENDED): Layer 2 Hamming/Gray Coding Paper

**Candidate**: Publish the coding-theory interpretation of UBT phase structure.

| Criterion | Assessment |
|-----------|-----------|
| Chance of success | **Very Low** (10%) for physics journal; would need quantum-information framing |
| Impact if true | **Low-Medium** |
| Reviewer interest | **Low** in physics; possibly medium in quantum information |
| Risk of failure | **Very High** — perception of numerology |
| Recommendation | **DO NOT publish as UBT flagship** |

---

## Section 4 — Open Hard Problems

> Honest inventory of the hardest unresolved issues.

### OHP-1: α derivation without fitting

**Status**: Open Hard Problem (27+ approaches exhausted)  
**Core gap**: k=1 (Kac-Moody level) not derived from S[Θ] independently of n*=137.  
**Core gap**: R≈1.114 two-loop correction — best candidate ΔB=3π/2 is a motivated conjecture with no algebraic proof.  
**Honest assessment**: The theory predicts α⁻¹=137 *given* B_base; but B_base is partially proved with one unresolved conjecture inside. The result is semi-empirical, not zero-parameter.

### OHP-2: Lepton/quark generation structure

**Status**: Open Hard Problem  
**Core gap**: KK mismatch theorem *proves* that the torus Dirac spectrum cannot reproduce the μ/e ratio of 207 from any real modulus. Options A, B (dead ends); Option C (instantons) calibrated to muon gives tau off by ×6.  
**Core gap**: Three generations have two algebraic candidates ({i,j,k} and ψ-winding) but whether they are the same mechanism is open [L2].  
**Honest assessment**: No predictive derivation of lepton mass ratios exists.

### OHP-3: Weinberg angle sin²θ_W

**Status**: Pure-algebra Dead End (ℂ⊗ℍ alone); EW-1b (EW1+RG) remains conditional  
**Assessment**: The mixing ratio g/g' between SU(2)_L and U(1)_Y is not fixed by pure algebra; it requires additional dynamical input. UBT derives the gauge *group* but not the *coupling ratios* from pure algebra alone. A conditional EW-1b (EW1+RG) branch is still tracked and should be labeled conditional in all papers.

### OHP-4: Renormalization / scale behavior beyond one loop

**Status**: Open  
**Core gap**: The two-loop β-function on T³×S¹ is computed but does not close the R factor or the Hosotani λ gap (factor ×11).  No systematic renormalization group treatment of UBT exists.

### OHP-5: Rigorous Standard Model closure

**Status**: Strong Partial  
**Core gaps**: Chirality selection (Gap C1 conditional); quark mass spectrum (not started); CKM matrix (not started); top quark Yukawa (not started).  
**Honest assessment**: The SM gauge *structure* is proved; the SM *dynamics* (mass spectrum, mixing angles) is almost entirely open.

### OHP-6: Unique experimental prediction distinguishable from ΛCDM+SM

**Status**: Weak  
**Candidates currently in the theory**:  
- δα/α ~ 10⁻²¹ at two loops in a cosmological φ-background (unmeasurable)  
- Mirror matter dark matter (mass/cross-section not yet computed)  
- Hubble tension latency (model parameter δ≈0.08 fitted)  
**Assessment**: No concrete, falsifiable, *parameter-free* prediction of a deviation from ΛCDM+SM exists yet.  This is the most significant scientific weakness of the program.

### OHP-7: Proof completeness gaps in GR

**Status**: Open [L2]  
**Core gaps**: Zerilli even-parity graviton; off-shell rank on compact M⁴; metric uniqueness outside A_UBT admissible class.

### OHP-8: Gravitational constant G not fixed by algebra

**Status**: Open Hard Problem  
**Assessment**: G requires a UV cutoff λ_UV not determined by ℂ⊗ℍ alone.  The 8π structure is algebraically derived (dim_ℝ(ℍ)=4); the numerical value of G is not.

---

## Section 5 — 90-Day Practical Roadmap

### Month 1 (May 2026) — Write the SM Gauge Paper

**Goal**: Draft ready for internal review.

Tasks:
- [ ] Write `docs/papers/sm_gauge_paper_draft.tex` from canonical/su3_derivation/ + canonical/interactions/
- [ ] Include all four results: SU(3) (involutions), SU(3) (superposition), SU(2)_L, U(1)_Y
- [ ] State confinement gap explicitly (Clay Millennium Problem; distinct from UBT derivation)
- [ ] State Weinberg angle limitation explicitly
- [ ] Internal consistency check: verify all theorems reference canonical sources
- [ ] Add numerical verification section (tools/verify_su3_superposition.py)
- [ ] Target journal: *Journal of Mathematical Physics* or *Letters in Mathematical Physics*

Milestone: Submittable draft by end of Month 1.

---

### Month 2 (June 2026) — Submit SM Paper + Draft GR Paper

**Goal**: SM paper submitted; GR paper draft ready.

Tasks:
- [ ] Revise SM paper from internal review; submit to arXiv (hep-th or math-ph)
- [ ] Write `docs/papers/gr_recovery_paper_draft.tex` from canonical/gr_closure/ + research_tracks/research/
- [ ] Include: Steps 1–5, Schwarzschild, linearized GR, Regge-Wheeler
- [ ] State Zerilli gap; attempt Priority 5 (off-diagonal V₀₁ computation) in parallel
- [ ] If Zerilli gap closes during this month, include in paper
- [ ] Run non-CM Hecke form search (Priority 6) using LMFDB API — 2 weeks part-time

Milestone: SM paper on arXiv; GR paper draft complete; Hecke search result obtained.

---

### Month 3 (July 2026) — Submit GR Paper + Begin α Focus + Freeze Coding Track

**Goal**: GR paper submitted; new α approach initiated; CMB track frozen.

Tasks:
- [ ] Revise GR paper; submit to arXiv
- [ ] Write `docs/papers/qm_emergence_paper_draft.tex` (Born rule + Dirac + QM/GR/stat-mech)
- [ ] Identify *one new algebraic route* for B_base: modular bootstrap or Verlinde formula on ψ-circle CFT
- [ ] Document and freeze the coding fingerprint track: write `research_tracks/fingerprints/FREEZE_REPORT.md`
- [ ] Do **not** start new coding/CMB experiments until core papers are submitted

Milestone: Two papers on arXiv (SM gauge + GR); QM draft ready; α new route initiated.

---

### Beyond Month 3

Priorities in order:
1. Submit QM emergence paper (Month 4)
2. Continue B_base new route
3. Complete Zerilli derivation if not done in Month 2
4. Begin mirror sector falsifiability analysis (Priority 9)
5. Respond to referee comments on SM and GR papers

---

## Section 6 — Stop-Doing List

> Activities that currently dilute progress.  Stop immediately.

### STOP-1: Exhausted B_base approaches

**Action**: Do not attempt new variants of the 27 documented dead ends.  
Specific routes confirmed dead: KK sum, zeta function, Hausdorff approach (without new structure), NCG spectral triple, instanton action, two-loop β-function coefficient, Weyl anomaly, Dynkin index, Cartan-Killing metric, canonical norm normalization, two-scale R_ψ substitution, heat kernel on flat T³.  
**Instead**: One genuinely new angle only (modular bootstrap or Verlinde).

### STOP-2: CMB fingerprint expansion

**Action**: No new CMB fingerprint experiments, no new coding track branches, no Reed-Solomon physics claims until the SM + GR + QM papers are published.  
**Instead**: Freeze in a single reference document.

### STOP-3: Duplicate derivations with minor variation

**Action**: Stop generating new `.tex` files that are minor variants of existing dead ends (e.g., b_base_* variants, r_factor_* variants).  The DERIVATION_INDEX.md documents 27+ dead ends clearly; new files in the same direction add noise.  
**Instead**: Maintain the index; write a new dead end entry if a new approach fails; do not create stub files.

### STOP-4: Weinberg angle derivation from ℂ⊗ℍ alone

**Action**: Accept the Dead End finding and state it explicitly in every relevant paper.  Stop attempting to fix sin²θ_W from algebra.  
**Instead**: Include as an explicit limitation; note that UBT derives gauge *structure* but coupling *ratios* require additional dynamical input.

### STOP-5: Unsynced notation proliferation

**Action**: All new documents must use canonical symbols from `canonical/CANONICAL_DEFINITIONS.md`.  Do not introduce new symbols for standard objects (no T_B, no metric-v2 notation, no ψ as wave function).  
**Instead**: Single notation pass through all new paper drafts before submission.

### STOP-6: Universe-as-atom / simulation / consciousness claims in physics documents

**Action**: Do not include consciousness (psychon), Reed-Solomon cosmology, or digital-universe claims in any arXiv submission or physics paper.  
**Instead**: These remain isolated in `speculative_extensions/`; reference them only as speculative appendices if at all.

### STOP-7: Premature priority-claim language in public documents

**Action**: Replace phrases like "first derivation", "Nobel-level result", "proves quantum mechanics" in any document intended for public or arXiv submission.  
**Instead**: State results precisely: "We derive SU(3)×SU(2)_L×U(1)_Y algebraically from ℂ⊗ℍ with zero free parameters."  Let the result speak.

### STOP-8: Maintaining too many parallel research fronts

**Action**: Freeze or archive: automorphic forms bridge, p-adic universe branching, CTC stability, Theta Resonator, consciousness modeling, quantization grid, Hubble latency MCMC until core papers are accepted.  
**Instead**: Depth on Priorities 1–5 only.

---

## Near-Breakthrough Alert

> **If current repo already contains a near-breakthrough result, identify it explicitly.**

**YES. The near-breakthrough result is already proved and is sitting unpublished.**

**Result**: *Derivation of SU(3)×SU(2)_L×U(1)_Y from the biquaternion algebra ℂ⊗ℍ with zero free parameters.*

Specifically:
- SU(3) derived via two independent routes (involutions, Theorems G.A–G.D; quantum superposition over {I,J,K})
- SU(2)_L from left automorphisms; U(1)_Y from right action
- U(1)_EM from ψ-cycle phase topology
- Eight Gell-Mann generators verified numerically
- Color confinement structural argument (free quarks algebraically inadmissible)
- All proved at [L0] with zero free parameters

This is a genuine mathematical theorem, not a numerical observation.  It is stronger than
most published work on gauge symmetry emergence from algebra.  The only reason it has
not had impact is that it has not been submitted to a journal.

**The highest-priority action for the entire program is to write and submit this paper.**

---

*Last updated: 2026-05-13*  
*Compiled from: DERIVATION_INDEX.md, canonical/README.md, canonical/AXIOMS.md,  
canonical/CANONICAL_DEFINITIONS.md, research_tracks/README.md, docs/RESEARCH_PRIORITIES.md,  
docs/STATUS_ALPHA.md, canonical/geometry/**, canonical/interactions/**, canonical/su3_derivation/**,  
experiments/**, docs/reports/hecke_lepton/**.*
