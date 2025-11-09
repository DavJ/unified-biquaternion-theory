# UBT v19 — Equation Check Scope (Symbolic Audit Plan)
_Date: 2025-11-06_0731_

This file defines the **scope** for a full SymPy verification pass we will run after the v20 edits land.

## Targets
- `appendix_ALPHA_one_loop_biquat.tex`: β‑function, B(R_ψ, N_eff, 𝓡)
- `appendix_E2_fermion_masses.tex`: no α upstream in mass textures
- `appendix_G_internal_color_symmetry.tex`: algebra identities (commutators, f^{abc})

## Tests to run
1. **β‑function extraction**: verify that the stated integral reduces to the printed B formula (symbolic to numeric evaluation).  
2. **Mode count**: confirm that N_eff=12 follows from stated d.o.f. counting.  
3. **Acyclicity**: static check that `m_e` definitions do not reference α in any upstream assumption.  
4. **SU(3) algebra**: programmatically check commutator table for the inserted λᵢ.

## Outputs
- `alpha_B_check.log` with the numeric breakdown  
- `acyclicity_scan.txt` listing any references that would imply cycles
