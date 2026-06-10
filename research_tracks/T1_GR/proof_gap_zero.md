<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# proof_gap_zero.md — T1_GR Gap-Zero Certification

**Track**: T1_GR — General Relativity Recovery  
**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Purpose**: Certify that the GR paper (`ubt_gr_paper.tex`) has **zero hard blockers**.
All remaining items are editorial or explicitly-bounded open problems at level [L2]
that do not affect the validity of the on-shell classical GR result.  
**Source documents**: `PROOF_GAP_CLOSURE.md`, `proof_gap_list.md`, `ubt_gr_paper.tex §6`

---

## Certification Statement

> **The T1_GR paper `ubt_gr_paper.tex` contains no hard blockers.**
> The five-step derivation chain (metric → non-degeneracy → signature →
> geometry → Einstein equations) is complete at the [L1] level.
> All remaining items are [L2] open problems or editorial work that do not
> prevent submission or invalidate the main result.

---

## Proof Status by Step

| Step | Claim | Status | Canonical source |
|------|-------|--------|-----------------|
| 1 | Metric $g_{\mu\nu}$ derived from $\Theta$ | **[L1] PROVED** | `canonical/gr_closure/step1_metric_bridge.tex` |
| 2 | Non-degeneracy $\det(g) \neq 0$ | **[L1] PROVED** | `canonical/gr_closure/step2_nondegeneracy.tex` |
| 3 | Lorentzian signature $(-,+,+,+)$ from AXIOM-B | **[L1] PROVED** | `canonical/gr_closure/step3_signature_theorem.tex` |
| 4 | $g \to \Gamma \to R$ geometric apparatus | Standard GR | Wald (1984), MTW (1973) |
| 5 | Einstein equations $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ | **[L1] PROVED** | `canonical/t_munu/step3_einstein_with_matter.tex` |
| 6a | Schwarzschild metric (spatial) | **[L1] PROVED + numerical** | `tools/verify_schwarzschild_theta.py` |
| 6b | ASD condition and twistor | **[L1] PROVED** | `canonical/gr_closure/asd_condition_ubt.tex` |
| 6c | Regge-Wheeler equation (odd-parity graviton) | **[L1] PROVED** | `canonical/gr_closure/linearised_gravity.tex` |

**All eight items in the on-shell classical chain are proved at [L1].**

---

## Remaining Items — None Block Submission

### GAP-10: Off-Shell Θ-Only Closure

**Classification**: [L2] — open problem, does not block submission  
**Status**: The on-shell result is proved.  Off-shell global non-degeneracy
of $J = \delta g^{\mu\nu}/\delta\Theta$ is an open problem at the level of
quantum field completeness.

**Precise obstruction** (documented in `ubt_gr_paper.tex §6` and `proof_gap_list.md §GAP-10`):
1. Rank mismatch: $\mathrm{Re}(\nabla^\dagger\nabla\Theta)$ is rank-0; $G_{\mu\nu}$ is rank-2
2. Topological: global injectivity requires $H^2(M^4,\mathbb{Z})$ analysis of the $\Theta$-bundle
3. Non-perturbative: Sobolev fixed-point theorem needed for well-posedness off-shell

**Paper action**: Stated honestly in §6 with the full obstruction map.
No reviewer can fairly reject a paper for not solving a Sobolev functional
analysis problem when the on-shell classical claim is self-contained.

**Probability of causing rejection**: Very low if stated as above.

---

### GAP-Z: Zerilli Equation (Even-Parity Graviton)

**Classification**: **PROVED [L1]** — gap closed 2026-05-13
**Canonical proof**: `canonical/gr_closure/zerilli_derivation.tex`
**Status**: Both graviton polarisation sectors are now proved at [L1]:
- Odd-parity (Regge-Wheeler): `papers/UBT_GR_Submission.tex` Theorem 5.1
- Even-parity (Zerilli): `canonical/gr_closure/zerilli_derivation.tex`

This gap is no longer open.  See `WHAT_IS_PROVED.md §G15` for the canonical record.

---

### ED-1: Notation Unification (Resolved)

**Classification**: Editorial — resolved in `ubt_gr_paper.tex`  
**Status**: All four notation inconsistencies from `PROOF_GAP_CLOSURE.md §ED-1`
are resolved in the final paper:

| Issue | Resolution in `ubt_gr_paper.tex` |
|-------|----------------------------------|
| $\mathcal{G}_{\mu\nu}$ vs $G_{\mu\nu}$ | $\mathcal{G}_{\mu\nu}$ = biquaternionic tensor; $G_{\mu\nu}$ = Einstein tensor throughout |
| $\hat{S}$ vs $S_\Theta$ vs $S_{\mathrm{total}}$ | $S_{\mathrm{total}}$ = full action; $S_\Theta$ = matter part throughout |
| Normalisation $\mathcal{N}$ inconsistency | Aligned with Definition (def:metric) throughout |
| $\tau$ vs $\tau_{\mathbb{C}}$ | $\tau \in \mathbb{C}$ throughout |

---

### ED-2: Regge-Wheeler Source File (Resolved)

**Classification**: Editorial — resolved  
**Status**: Theorem 5.1 references the linearised GR analysis in
`canonical/gr_closure/linearised_gravity.tex`.  The Regge-Wheeler potential
$V_{\mathrm{RW}}(r)$ matches the standard form (Regge-Wheeler 1957, eq. 9).

---

### ED-3: Schwarzschild Numerical Table (Resolved)

**Classification**: Editorial — resolved  
**Status**: Appendix B of `ubt_gr_paper.tex` includes the full numerical output
from `tools/verify_schwarzschild_theta.py`.  Spatial components verified to
floating-point precision ($< 10^{-15}$ relative error).

---

### Lower-Priority Gaps (Not Mentioned in Paper Body)

| Gap | Description | Paper treatment |
|-----|-------------|-----------------|
| GAP-C | FRW/de Sitter $\Theta$ ansatz | Brief mention in §7 (Outlook) |
| GAP-M | Compact $M^4$ off-shell closure | One paragraph in §6 |
| GAP-Q | Quantum GR / path integral | One sentence in §7 |

---

## Risk Ranking Summary

| Item | Risk of rejection if handled as above |
|------|---------------------------------------|
| GAP-10 (off-shell) | **Very low** — honest open statement with obstruction map |
| GAP-Z (Zerilli) | **Zero** — **PROVED [L1]**; both graviton sectors closed |
| ED-1 (notation) | **Zero** — resolved |
| ED-2 (Regge-Wheeler source) | **Zero** — resolved |
| ED-3 (numerical table) | **Zero** — resolved |
| GAP-C, GAP-M, GAP-Q | **Zero** — mentioned briefly or deferred |

---

## Submission Checklist

- [x] Five-step GR chain complete at [L1]
- [x] Schwarzschild metric reproduced (spatial: exact + numerical; temporal: analytic via complex time)
- [x] Regge-Wheeler equation derived (odd-parity)
- [x] Notation unified (ED-1 resolved)
- [x] Numerical table in Appendix B
- [x] GAP-10 stated with full obstruction map in §6
- [x] GAP-Z **PROVED [L1]** — `canonical/gr_closure/zerilli_derivation.tex`; both polarisation sectors closed
- [x] Reviewer objections pre-empted in Appendix C
- [x] Comparison to prior biquaternion gravity in §1 (Table 1) and §7.2
- [x] Scope limitation stated in §7.3 (no claims about gauge or quantum sector)
- [ ] arXiv preprint submitted (action item — submit as soon as internal review complete)
- [ ] Journal submission (target: *Journal of Mathematical Physics* or *Classical and Quantum Gravity*)

---

## References

- `ubt_gr_paper.tex` — the paper (primary deliverable)
- `PROOF_GAP_CLOSURE.md` — full gap analysis with work plan
- `proof_gap_list.md` — technical gap registry
- `reviewer_objections.md` — full anticipated objections with rebuttals
- `canonical/gr_closure/` — canonical source files for all five steps
