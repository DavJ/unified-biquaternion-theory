<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Neutrino/CKM archive exploration (H1)

## Sources read (archive, read-only)

- `ARCHIVE/archive_legacy/consolidation_project/appendix_QA2_quarks_CKM.tex`
- `ARCHIVE/archive_legacy/ARCHIVE/legacy_variants/ubt_with_chronofactor/scripts/ubt_neutrino_mass_derivation.py`

## (a) What was attempted

1. **CKM in archival appendix QA2**
   - Discrete torus-mode assignment for quark generations.
   - CKM from overlap integrals of mode functions on `T^2` with holonomy textures.
   - Multiple baseline tables auto-inserted with placeholder-style numerical attempts.

2. **Neutrino archival script**
   - Type-I see-saw toy model with phenomenological constants.
   - Ad-hoc assumptions for complex-time Majorana scale and Yukawa hierarchy.

## (b) Why it appears archived / what failed

- CKM appendix contains many baseline blocks and placeholders, with no clean first-principles closure.
- Numerical outputs in QA2 visibly deviate from PDG CKM structure in inserted comparison tables.
- Neutrino script is largely phenomenological (external constants and tunable assumptions), not a closed derivation from canonical UBT action.
- Both artifacts are exploratory and not aligned with current canonical proof-status standards.

## (c) Reusable basis for Hecke-style restart

Potential reusable elements:
- Keep **discrete-mode** mindset (integer mode indices, finite holonomy classes).
- Replace broad placeholder scans with a **small explicit map** from arithmetic invariants to observables.

Candidate direction (still speculative):
- Test whether CKM hierarchy can be encoded through prime-indexed arithmetic ratios
  (analogous to Hecke-ratio logic used in lepton-mass candidate notes), but with strict
  no-fit constraints and immediate NO-GO criteria when degeneracy appears.

Current verdict: **NO-GO for direct reuse**, but **narrow reusable idea** exists: discrete/arithmetic indexing framework.

## Status Summary

- **Hlavní výsledek**: Archivní CKM/neutrino linie byla zmapována; přímé převzetí je nevhodné.
- **Klasifikace**: [NO-GO for direct reuse] + [OPEN exploratory seed].
- **Dopad na teorii**: Brání recyklaci slabých placeholder modelů; zužuje další práci na přísně auditovatelný diskrétní rámec.
- **Příští krok**: Navrhnout minimální CKM testbed s jedním explicitním aritmetickým pravidlem a předem daným NO-GO kritériem.
- **Alpha je odvozena**: NE (unconditional)
