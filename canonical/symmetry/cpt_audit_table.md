<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->

# CPT Audit Table — UBT Action Terms

© 2026 Ing. David Jaroš — CC BY-NC-ND 4.0

This table audits every term in the UBT Lagrangian density

$$\mathcal{L}_{\rm UBT} = \mathcal{L}_{\rm grav} + \mathcal{L}_{\rm kin} + \mathcal{L}_{\rm gauge} + \mathcal{L}_{\rm pot} + \mathcal{L}_{\rm weak} + \mathcal{L}_{\rm mix}$$

against the discrete symmetries $C$, $P$, $T_{\rm UBT}$, $CP$, and $CPT$ defined in
`discrete_symmetries.tex` and `step1_CPT_definitions.tex`.

**Key**: ✓ = invariant, ✗ = violated, ~ = invariant with caveats/gap, ? = open/unknown.

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✓ | Term is invariant under the transformation |
| ✗ | Term explicitly breaks the symmetry |
| ~ | Invariant in the real sector; gap in biquaternionic sector (see notes) |
| ? | Status unresolved; open problem |
| (spont.) | Symmetry broken spontaneously by vacuum, not by the term itself |

---

## Main Audit Table

| Sector | Term | C | P | T | CP | CPT | Status | Note |
|--------|------|---|---|---|-----|-----|--------|------|
| Gravity | $\frac{1}{2\kappa}R$ | ✓ | ✓ | ~ | ✓ | ~ | Canonical (proved) | $T$ invariant in real limit; full $\psi$-sector gap (Gap S2 in step2) |
| Kinetic | $\mathrm{Tr}[(D_\mu\Theta)^\dagger(D^\mu\Theta)]$ | ✓ | ✓ | ✓ | ✓ | ✓ | Proved | Real-sector proof complete; see step2 §3 |
| Kinetic ($\psi$) | $\int d\psi\,\mathrm{Tr}[(\partial_\psi\Theta)^\dagger(\partial_\psi\Theta)]$ | ✓ | ✓ | ✓ | ✓ | ✓ | Candidate | $T_{\rm UBT}$: $\psi\to-\psi$ leaves $|\partial_\psi\Theta|^2$ invariant |
| Gauge | $-\frac{1}{4}F^a_{\mu\nu}F^{a\,\mu\nu}$ | ✓ | ✓ | ✓ | ✓ | ✓ | Proved (standard YM) | Standard result; $F_{\mu\nu}F^{\mu\nu}$ is $C$-, $P$-, $T$-even |
| Potential | $-m^2\,\mathrm{Tr}(\Theta^\dagger\Theta)$ | ✓ | ✓ | ✓ | ✓ | ✓ | Proved | Mass term; $P_1 P_2$-invariant |
| Potential | $-\lambda(\mathrm{Tr}(\Theta^\dagger\Theta))^2$ | ✓ | ✓ | ✓ | ✓ | ✓ | Proved | Quartic; same argument as mass term |
| Potential | $-\mu^2(\Theta^\dagger\Theta - v^2\mathbf{1})$ | ✓ | ✓ | ✓ | ✓ | ✓ | Proved | SSB: vacuum $\Theta_0$ may break $P$ spontaneously |
| Weak (chiral) | $\mathrm{Tr}[\Theta_L^\dagger W_\mu \partial^\mu \Theta_L]$ | ✗ | ✗ | ✓ | ✗ | ✓ | Explicit $C$ and $P$ breaking | Parity and charge-conjugation violated; $CPT$ compatible (real-time limit); see `chirality_and_parity_breaking.tex` |
| Weak (chiral) | $\bar\Theta_L \gamma^\mu (\partial_\mu + igW_\mu)\Theta_L$ | ✗ | ✗ | ✓ | ✗ | ✓ | Explicit $C$ and $P$ breaking | Standard left-chiral fermion coupling; $C$ broken by absence of right-handed sector |
| CP-odd (gauge) | $\theta_{\rm eff}\,F^a_{\mu\nu}\tilde F^{a\,\mu\nu}$ | ✓ | ✗ | ✗ | ✗ | ✓ | Candidate $CP$ and $T$ breaking | $C$-even, $P$-odd, $T$-odd → $CP$-odd; strong-$CP$ problem: why $|\bar\theta|<10^{-10}$? |
| CP-odd (Yukawa) | $y_{\rm CP}\,\Theta_L^\dagger H \Theta_R + \mathrm{h.c.}$ with $y_{\rm CP}\in\mathbb{C}$ | ~ | ✓ | ~ | ✗ | ✓ | Candidate $CP$ breaking | Complex phase in $y_{\rm CP}$ violates $CP$; $CPT$ preserved by hermiticity |
| CP-odd ($\psi$ phase) | $\delta_\psi\,\mathrm{Im}\bigl[\mathrm{Tr}(\Theta^\dagger\partial_\psi\Theta)\bigr]$ | ✗ | ✓ | ✓ | ✗ | ✓ | Conjecture | $C$ odd ($\psi\to-\psi$ under $C$); $CP$ odd if $\delta_\psi\neq0$; speculative |
| Vacuum phase | $\Theta_0 = v\,e^{i\delta}$ (VEV with phase $\delta\neq0,\pi$) | (spont.) | (spont.) | (spont.) | (spont.) | ✓ | Spontaneous $CP$ breaking conjecture | Vacuum phase misalignment; $CPT$ of action still preserved |
| Effective diffusion | $\partial_\tau\Theta = D\nabla^2\Theta - V\Theta$ | ✓ | ✓ | ✗ | ✓ | ✗ | **Effective only** | NOT fundamental; apparent $T$ and $CPT$ breaking is an artefact of coarse-graining; see `effective_vs_fundamental_breaking.tex` |
| Mixed gauge-grav | $\xi\,R\,\mathrm{Tr}(\Theta^\dagger\Theta)$ (non-minimal coupling) | ✓ | ✓ | ~ | ✓ | ~ | Candidate | Same $T$ gap as gravitational sector |

---

## Notes

### N1 — Gravitational $T$ gap
The full biquaternionic metric $\mathcal{G}_{\mu\nu}[\Theta(q,\tau)]$ depends on
$\tau = t+i\psi$.  Under $T_{\rm UBT}$: $\tau\to-\tau=-t-i\psi$.  If
$\mathcal{G}$ is even in $\tau$, the Ricci scalar $R$ is $T$-invariant.
An explicit mode-expansion calculation is needed to confirm this for
$\psi\neq0$.  In the real limit $\psi\to0$, $T$-invariance is guaranteed
by the standard CPT theorem.  **Priority: LOW.**

### N2 — Chiral coupling and CPT
The left-chiral coupling $\mathcal{L}_{\rm weak}\sim\Theta_L^\dagger W\Theta_L$
explicitly breaks both $C$ and $P$ (and hence $CP$), but is CPT-compatible by
construction in the real-time limit: the composition $CPT$ maps $\Theta_L$
through $T$ (time-reverse) → $P$ (parity, exchanging left/right) → $C$
(charge-conjugation, restoring the original chirality), reproducing the original
term.  Full equivalence to the standard CPT theorem remains open pending the
antiunitary-$T$ inner product in the biquaternionic sector.
See `chirality_and_parity_breaking.tex`.

### N3 — $\theta_{\rm eff}$ and CP violation
The term $\theta_{\rm eff}F\tilde F$ is $C$-**even**, $P$-odd, and $T$-odd,
hence $CP$-**odd** (consistent with the table row above: C ✓, P ✗, T ✗, CP ✗,
CPT ✓).  A non-zero $\theta_{\rm eff}$ (the QCD $\theta$ angle) violates $P$
and $T$ individually and breaks $CP$.  The strong-CP problem — why
$\theta_{\rm eff}\approx0$ experimentally — is an open problem in UBT.
See `open_problems.md`, item OP-S5.

> **Correction from earlier draft**: an earlier version of this note incorrectly
> stated that $F\tilde F$ is $C$-odd and $P$-odd and hence $CP$-even.
> The correct classification is $C$-even (see `discrete_symmetries.tex`,
> field transformation table), $P$-odd, $T$-odd, $CP$-odd.

### N4 — Effective diffusion sector
The diffusion equation $\partial_\tau\Theta = D\nabla^2\Theta - V\Theta$ is an
**effective**, not fundamental, equation.  Its apparent violation of $T$ and
$CPT$ is an artefact of coarse-graining (integrating out short-scale
$\Theta$ modes).  The fundamental action from which it is derived is
$CPT$-invariant.  **This must not be cited as a prediction of fundamental
CPT violation.**

---

## Summary: Symmetry Status by Sector

| Sector | $C$ | $P$ | $T$ | $CP$ | $CPT$ |
|--------|-----|-----|-----|------|-------|
| Gravitational | ✓ | ✓ | ~(gap) | ✓ | ~(gap) |
| Kinetic | ✓ | ✓ | ✓ | ✓ | ✓ |
| Gauge (YM) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Potential (symmetric) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Weak (chiral) | **✗** | **✗** | ✓ | **✗** | ✓ |
| $\theta_{\rm eff}F\tilde F$ (if present) | ✓ | **✗** | **✗** | **✗** | ✓ |
| Complex Yukawa phase | ~ | ✓ | ~ | **✗** | ✓ |
| Effective diffusion | ✓ | ✓ | **✗** | ✓ | **✗** (effective) |

**Bottom line**: The UBT fundamental action preserves $CPT$ in the real-time limit (full biquaternionic equivalence to the standard CPT theorem remains open).
Parity $P$ is explicitly broken by left-chiral couplings.
Both $C$ and $CP$ are broken in the minimal weak chiral sector; $CP$ invariance would require a compensating conjugate sector.
$T$-asymmetry in the diffusion sector is not fundamental.
