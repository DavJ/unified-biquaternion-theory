<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Canonical generalized-Dirac proof hardening

**Date:** 2026-07-27  
**Baseline:** `unified-biquaternion-theory-master(35).zip`

## Purpose

Continue only the canonical UBT chain

\[
\Theta \to E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta
\to \{g_{\mu\nu},\Gamma_\mu\}
\]

and prevent the archived spinor-current tetrad from reappearing as an active
alternative metric mechanism.

## Exact results added

1. **Carrier typing:** `Psi = vec(Theta) in C^4` is explicitly a column
   representation of the same biquaternionic field, not a new fundamental
   field. Similarity changes of `vec` leave the Clifford relation and metric
   invariant.
2. **Principal-symbol factorisation:**
   \[
   \sigma_4(\xi)^2=g^{\mu\nu}\xi_\mu\xi_\nu I_4,
   \qquad
   \det\sigma_4(\xi)=\bigl(g^{\mu\nu}\xi_\mu\xi_\nu\bigr)^2.
   \]
   Hence the generalized-Dirac lift has exactly the canonical UBT metric null
   cone and introduces no second causal structure.
3. **Fifth-channel factorisation:** for
   `Gamma_psi^2 = epsilon I`,
   \[
   \sigma_5^2=
   \bigl(g^{\mu\nu}\xi_\mu\xi_\nu+\varepsilon\xi_\psi^2\bigr)I_4.
   \]
4. **Conditional psi-normal theorem:** if `D_psi Psi` is an independent
   first-jet slot and the equation is linear in it with invertible
   `Gamma_psi`, it is solved uniquely. Therefore the pointwise equation does
   not restrict the four spacetime tetrad slots and preserves the proved
   `E -> g` rank ten.

All verifier checks use exact SymPy algebra. No floating-point tolerance is
used.

## Honest boundary

The psi-normal result is conditional. Canonical UBT also assumes holomorphy in
`tau=t+i psi`, which relates the real-time and psi derivatives. Compatibility
of the normal-form argument with that strict Cauchy-Riemann constraint remains
the decisive on-shell rank theorem.

## Historical cleanup

The following duplicate active files were removed; their contents already
exist in the dated history directory:

- `research_tracks/dual_sector_clifford5/dual_sector_cl5_rank_status.md`
- `tools/verify_dual_sector_cl5_rank.py`
- `tests/test_dual_sector_cl5_rank.py`

The redirect README remains active, while the calculations remain at
`research_tracks/history/legacy_spinor_current_tetrad_2026-07-26/`.

## Build and validation

- Exact verifier: PASS.
- Targeted pytest selection: 20 passed.
- Standalone proof PDF: 4 pages, compiled and render-checked.
- `canonical/UBT_canonical_main.tex` progressed past the previous literal
  Unicode `Theta` failure after correcting `canonical/fields/theta_field.tex`,
  but the full build still stops later on an unrelated legacy Unicode checkmark
  in `canonical/fields/biquaternion_time.tex`.
