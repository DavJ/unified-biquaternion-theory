<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Chirality and Parity Status (Weak-Sector Track)

Status label used in code:

> **chirality algebra scaffold for future weak-sector derivation.**

## What is implemented

Module: `src/ubt/algebra/chirality.py`

- standard Pauli matrices,
- \(\gamma^5\) construction from gamma matrices,
- chiral projectors \(P_L=(1-\gamma^5)/2\), \(P_R=(1+\gamma^5)/2\),
- parity operator scaffold (`P = gamma^0`) and parity-conjugation utility,
- explicit CPT placeholder interface that raises `NotImplementedError`.

## What is standard Clifford algebra

- Pauli identities,
- Clifford anticommutation relations,
- pseudoscalar \(\gamma^5\) algebra,
- projector idempotence and orthogonality,
- parity conjugation behavior for \(\gamma^\mu\).

## What is UBT-specific here

- integration point with existing UBT biquaternion gamma-matrix construction in `tools/dirac_from_biquaternion.py`,
- status discipline explicitly preventing weak-sector overclaims.

## Open weak-sector gaps

- derivation of explicit \(SU(2)_L\) coupling from UBT geometry,
- hypercharge assignment derivation,
- anomaly-cancellation derivation,
- fermion-generation closure,
- W/Z mass mechanism derivation,
- CPT theorem proof from UBT action/symmetry structure.
