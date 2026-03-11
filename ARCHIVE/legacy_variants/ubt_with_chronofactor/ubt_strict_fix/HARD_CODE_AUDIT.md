# Hardcoded Measurement Audit (alpha & lepton masses)

Found 68 files with suspicious literals.

## unified-biquaternion-theory-master/CALCULATION_STATUS_ANALYSIS.md
Hits: alpha_inv_approx, electron_mass
- alpha_inv_approx: `...pproximation from this hardcoded anchor\n\n**The value α^-1 = 137.035999000000 is:**\n- ❌ NOT calculated from UBT theory\n- ❌ NOT derived fr...`
- alpha_inv_approx: `...ls  \n- ✅ Hardcoded experimental target (CODATA 2022: α^-1 = 137.035999177)\n- ✅ Used as anchor point for approximating other sectors\n\n...`

## unified-biquaternion-theory-master/COPILOT_INSTRUKCE_TWO_LOOP.md
Hits: alpha_inv_approx
- alpha_inv_approx: `...Udrž bez-fitovost vstupů.\n   - Validuj pro p=137: `α^{-1} ≈ 137.035999` v toleranci `< 5e-4`.\n\n2) **Zobecni na více p** (stejné já...`

## unified-biquaternion-theory-master/CSV_AND_DOCUMENTATION_POLICY.md
Hits: alpha_inv_approx, electron_mass
- alpha_inv_approx: `...pha_core_repro/out/alpha_two_loop_grid.csv` | `alpha_inv` | 137.035999000000 |\n| m_e (pole) | `data/leptons.csv` | `pole_mass_mev` | 0.5...`
- electron_mass: `...000 |\n| m_e (pole) | `data/leptons.csv` | `pole_mass_mev` | 0.510996192910 |\n\n## Generating Markdown from CSV (Future Enhancement)\n\nTo...`

## unified-biquaternion-theory-master/DATA_PROVENANCE.md
Hits: alpha_inv_approx, electron_mass
- alpha_inv_approx: `...ta_ct,alpha_inv,alpha,scheme,mu,form_factor\n137,0.035999000,137.035999000,0.007297352574,MSbar,,1.000000000\n```\n\n**Generation**: \n```...`
- alpha_inv_approx: `...10^{-5} | ⏳ |\n\n**Reference Values:**\n- α^{-1} experimental: 137.035999177(21) (CODATA 2022)\n- α^{-1} computed: 137.035999000\n- Relati...`

## unified-biquaternion-theory-master/ELECTRON_MASS_IMPLEMENTATION.md
Hits: electron_mass
- electron_mass: `... derivation pipeline\n\n**Output:**\n```\nUBT prediction: m_e = 0.510996193 MeV\nPDG value:      m_e = 0.51099895000 MeV\nRelative error:...`
- electron_mass: `...UBT prediction: m_e = 0.510996193 MeV\nPDG value:      m_e = 0.51099895000 MeV\nRelative error: |Δm/m| = 5.40e-06\nStatus: ✓ PASS\n```\n\n#...`

## unified-biquaternion-theory-master/EMERGENT_ALPHA_README.md
Hits: alpha_inv_approx
- alpha_inv_approx: `...(exact) | Topological quantization |\n| α⁻¹ (experimental) | 137.035999084(21) | CODATA 2018 |\n| Difference | 0.036 | Quantum correcti...`

## unified-biquaternion-theory-master/EXECUTIVE_SUMMARY_STATUS.md
Hits: electron_mass
- electron_mass: `...culate Yukawa texture coefficients\n- Remove hardcoded m_e = 0.51099895\n- Validate: calculated value matches experiment\n\n**Phase 3:...`

## unified-biquaternion-theory-master/FERMION_MASS_COMPLETE_REPORT.md
Hits: electron_mass, muon_mass, tau_mass
- electron_mass: `...-----------------|--------|\n| **Electron** | 1 | 0.509856 | 0.51099895000 | **0.22%** |\n| **Muon** | 2 | 105.658376 | 105.6583755 | 0...`
- electron_mass: `...ource |\n|----------|-------|--------|\n| Experimental mass | 0.51099895000 MeV | CODATA 2018 |\n| Topological (bare) | 0.509856 MeV | U...`

## unified-biquaternion-theory-master/FIRST_PRINCIPLES_ANALYSIS.md
Hits: alpha_inv_approx, electron_mass
- alpha_inv_approx: `...rk present\n\n**Quantum Corrections (Step 2):**\n```\nα⁻¹_exp ≈ 137.035999\n```\n- Requires one-loop vacuum polarization\n- Running from ...`
- alpha_inv_approx: `...1. **Pipeline function F(B):** How does B = 8π map to α⁻¹ = 137.035999?\n2. **Master integral evaluation:** Two-loop diagrams not n...`

## unified-biquaternion-theory-master/FITTED_PARAMETERS.md
Hits: alpha_inv_approx, electron_mass
- alpha_inv_approx: `...Fine-Structure Constant α**\n- **Experimental Value:** α⁻¹ = 137.035999084(21)\n- **UBT Prediction:** α⁻¹ = 137 (from N=137 constraint)...`
- electron_mass: `...tatus:** Measured quantity used as input\n- **Value:** m_e = 0.51099895000(15) MeV/c² (CODATA 2018)\n- **Usage:** Sets scale R_ψ, used ...`

## unified-biquaternion-theory-master/IMPLEMENTATION_ROADMAP.md
Hits: electron_mass, muon_mass, tau_mass
- electron_mass: `...als |\n| m_e | Framework exists, anchor proposed | Hardcoded 0.51099895 | Determine M_Θ, compute texture |\n| m_μ, m_τ | Framework e...`
- electron_mass: `...nt Full Mass Calculation\n\n**Goal:** Replace hardcoded m_e = 0.51099895 with calculation\n\n```python\ndef compute_electron_mass_from_...`

## unified-biquaternion-theory-master/OVERVIEW.md
Hits: alpha_inv_approx
- alpha_inv_approx: `... 137 (from complex time topology)  \n**Experimental:** α⁻¹ = 137.035999084(21) (CODATA 2018)  \n**Error:** 0.026%  \n**Derivation:** Win...`

## unified-biquaternion-theory-master/PROVENANCE_TESTS_README.md
Hits: alpha_inv_approx
- alpha_inv_approx: `...sion:**\n- α^{-1}: Match within 1.3×10^{-9} (vs CODATA 2022: 137.035999177)\n- m_e: Match within 5.4×10^{-6} (exceeds 10^{-4} target!)\n...`

## unified-biquaternion-theory-master/PYTHON_SCRIPTS_REPORT.md
Hits: alpha_inv_approx, electron_mass
- alpha_inv_approx: `...035955204,0.007631493192,MSbar,,1.000000000\n137,0.035999000,137.035999000,0.007297352574,MSbar,,1.000000000\n139,0.036013599,139.03601...`
- alpha_inv_approx: `...=137 sector):**\n- α = 0.007297352574 (12 decimals)\n- α^-1 = 137.035999000000 (12 decimals)\n- Δ_CT = 0.035999000000 (12 decimals)\n- **Com...`

## unified-biquaternion-theory-master/README.md
Hits: alpha_inv_approx, electron_mass
- alpha_inv_approx: `...----------|\n| Fine-structure constant | α⁻¹ = 137 (exact) | 137.035999084 | ±0.000000021 | 0.026% |\n| Electron mass | 0.509856 MeV | ...`
- alpha_inv_approx: `...------|\n| **Fine-structure constant** | α⁻¹ = 137 (exact) | 137.035999084 | ±0.000000021 | 0.026% | ✅ FIT-FREE |\n| **Electron mass** ...`

## unified-biquaternion-theory-master/TASK_COMPLETION_SUMMARY.md
Hits: electron_mass
- electron_mass: `...✅ Increase precision in export_alpha_csv.py (FIXED: 0.511 → 0.510998946)\n\n## CRITICAL DISCOVERY ⚠️\n\nYour suspicions were **absolute...`
- electron_mass: `...python\n# ubt_masses/core.py, line 141\nm_pole_experimental = 0.51099895  # MeV ← PDG value, HARDCODED!\n```\n\n## All Deliverables\n\n1....`

## unified-biquaternion-theory-master/TESTABILITY_AND_FALSIFICATION.md
Hits: alpha_inv_approx, electron_mass, muon_mass, tau_mass
- alpha_inv_approx: `...) at multiple energy scales with error bars:\n```\nα⁻¹(m_e) = 137.035999084 ± 0.000000021 (CODATA 2018)\nα⁻¹(M_Z) = 127.95 ± [UBT uncert...`
- alpha_inv_approx: `...137 (integer from topology)  \n**Experimental Value:** α⁻¹ = 137.035999084(21)  \n**Agreement:** 0.026% error\n\n**Derivation Summary:**\n...`

## unified-biquaternion-theory-master/UBT_COMPREHENSIVE_REVIEW_DEC_2025.md
Hits: alpha_inv_approx, electron_mass, muon_mass, tau_mass
- alpha_inv_approx: `...ssumptions (A1-A3)\n   - No adjustable parameters\n   - α⁻¹ = 137.035999 (experimental match < 5×10⁻⁴)\n\n2. **✅ HECKE-WORLDS FRAMEWOR...`
- alpha_inv_approx: `...55204 | 131.035955204 | - |\n| **137** | **0.035999000** | **137.035999000** | **✅ < 5×10⁻⁴** |\n| 139 | 0.036013599 | 139.036013599 | ...`

## unified-biquaternion-theory-master/UBT_COMPREHENSIVE_REVIEW_DEC_2025_draft.md
Hits: electron_mass, muon_mass, tau_mass
- electron_mass: `...---|--------------|-------|\n| Electron | 1 | 0.509856 MeV | 0.51099895000 MeV | **0.22%** |\n| Muon | 2 | 105.658 MeV | 105.6583755 Me...`
- muon_mass: `...0.509856 MeV | 0.51099895000 MeV | **0.22%** |\n| Muon | 2 | 105.658 MeV | 105.6583755 MeV | 0.0001% |\n| Tau | 3 | 1776.86 MeV |...`

## unified-biquaternion-theory-master/UBT_HeckeWorlds_theta_zeta_primes_appendix.tex
Hits: alpha_inv_approx
- alpha_inv_approx: `...137} = 0.035999$ reproduces the experimental inverse value $137.035999\ldots$ exactly to the stated tolerance ($< 5 \times 10^{-4}...`

## unified-biquaternion-theory-master/UBT_SCIENTIFIC_RATING_2025.md
Hits: alpha_inv_approx, electron_mass
- alpha_inv_approx: `...SymPy and computational verification\n   - Prediction: α⁻¹ = 137.035999000\n   - Experimental: α⁻¹ = 137.035999177(21) (CODATA 2022)\n  ...`
- alpha_inv_approx: `... - Prediction: α⁻¹ = 137.035999000\n   - Experimental: α⁻¹ = 137.035999177(21) (CODATA 2022)\n   - **Precision: 1.3×10⁻⁹** (1.3 parts p...`

## unified-biquaternion-theory-master/UBT_VS_OTHER_THEORIES_COMPARISON.md
Hits: electron_mass, tau_mass
- electron_mass: `...mparison\n\n**Electron Mass Prediction:**\n- **Experimental**: 0.51099895000(15) MeV (CODATA 2018)\n- **UBT Predicted**: 0.5099 MeV (not ...`
- tau_mass: `...3 (all fitted) | 0.511 MeV (fitted) | 105.66 MeV (fitted) | 1776.86 MeV (fitted) | ❌ No |\n| **String Theory** | Model-dependent...`

## unified-biquaternion-theory-master/UBT_alpha_per_sector_patch.tex
Hits: alpha_inv_approx
- alpha_inv_approx: `... & $131+\cdots$ & $\cdots$ \\\n    137 & $0.035999\ldots$ & $137.035999\ldots$ & $\cdots$ \\\n    139 & $\cdots$ & $139+\cdots$ & $\...`

## unified-biquaternion-theory-master/emergent_alpha_from_ubt.tex
Hits: alpha_inv_approx
- alpha_inv_approx: `...}}$ with $p=137$ reproduces the experimental inverse value\n$137.035999\ldots$ within the stated tolerance, without fitting.\n\n\sect...`

## unified-biquaternion-theory-master/ubt_fermion_masses_results.txt
Hits: electron_mass, muon_mass, tau_mass
- electron_mass: `...-------------------------------------\nelectron              0.510999          0.510999    0.0000%\nmuon                105.658376...`
- electron_mass: `...-------------------\nelectron              0.510999          0.510999    0.0000%\nmuon                105.658376        105.658376...`

## unified-biquaternion-theory-master/ubt_fermion_summary.txt
Hits: electron_mass, muon_mass, tau_mass
- electron_mass: `...  p = 7.40 (power law exponent)\n\nResults:\n  Electron (n=1): 0.510999 MeV (exp: 0.510999 MeV) → 0.00% error ✅\n  Muon (n=2):     1...`
- electron_mass: `...aw exponent)\n\nResults:\n  Electron (n=1): 0.510999 MeV (exp: 0.510999 MeV) → 0.00% error ✅\n  Muon (n=2):     105.658 MeV (exp: 10...`

## unified-biquaternion-theory-master/alpha_core_repro/README.md
Hits: alpha_inv_approx
- alpha_inv_approx: `...two_loop.py`: Test suite\n  - Validates p=137 gives α^{-1} = 137.035999 (tolerance < 5×10⁻⁴)\n  - Tests sanity for other primes\n  - ...`
- alpha_inv_approx: `...35955204 | 0.007631493192 |\n| **137** | **0.035999000** | **137.035999000** | **0.007297352574** |\n| 139 | 0.036013599 | 139.03601359...`

## unified-biquaternion-theory-master/alpha_core_repro/alpha_two_loop.py
Hits: alpha_inv_approx
- alpha_inv_approx: `...\n    #\n    # From the requirement that p=137 gives α^{-1} ≈ 137.035999,\n    # we can determine the geometric constants.\n    \n    #...`
- alpha_inv_approx: `...n physical limit)\n    # From the requirement α_{137}^{-1} = 137.035999:\n    # Δ_CT(137) = 0.035999\n    \n    # The p-dependence com...`

## unified-biquaternion-theory-master/alpha_core_repro/export_alpha_csv.py
Hits: electron_mass
- electron_mass: `...precise values from PDG and other standards\nMU_GRID = [\n    0.510998946,     # Electron pole mass (PDG 2024) in MeV\n    1.776_86,  ...`

## unified-biquaternion-theory-master/alpha_core_repro/out/alpha_two_loop.csv
Hits: alpha_inv_approx
- alpha_inv_approx: `...parameter,value\np,137\nDelta_CT,0.035999\nalpha_inv,137.035999\n...`

## unified-biquaternion-theory-master/alpha_core_repro/out/alpha_two_loop_grid.csv
Hits: alpha_inv_approx
- alpha_inv_approx: `...035955204,0.007631493192,MSbar,,1.000000000\n137,0.035999000,137.035999000,0.007297352574,MSbar,,1.000000000\n139,0.036013599,139.03601...`

## unified-biquaternion-theory-master/alpha_core_repro/tests/test_alpha_two_loop.py
Hits: alpha_inv_approx
- alpha_inv_approx: `... mode\n    if strict and p == 137:\n        assert abs(inva - 137.035999) < 5e-4\n\ndef test_alpha_137_precision_when_mock_enabled():\n...`
- alpha_inv_approx: `...nva = 1.0 / alpha_corrected(137, dct)\n    assert abs(inva - 137.035999) < 5e-4\n...`

## unified-biquaternion-theory-master/alpha_two_loop/symbolics/ct_two_loop.py
Hits: alpha_inv_approx
- alpha_inv_approx: `...    and is not used in core proofs.\n    """\n    alpha_inv = 137.035999\n    alpha = 1.0 / alpha_inv\n    q = 10 ** target_precision\n...`

## unified-biquaternion-theory-master/consolidation_project/appendix_H_alpha_padic_combined.tex
Hits: alpha_inv_approx
- alpha_inv_approx: `...ptimal value found is $N = 137$, yielding $\alpha \approx 1/137.035999$. However, other prime values may correspond to alternative...`

## unified-biquaternion-theory-master/consolidation_project/appendix_K_maxwell_curved_space.tex
Hits: electron_mass
- electron_mass: `...612 0.527217\n2.294486 0.521649\n2.344361 0.516251\n2.394236 0.511016\n2.444110 0.505935\n2.493985 0.501000\n2.543860 0.496206\n2.593...`

## unified-biquaternion-theory-master/consolidation_project/old/appendix_G_dark_matter_padic.tex
Hits: muon_mass
- muon_mass: `...ection*{Fit to Muon and Tau}\n\nUsing:\n\begin{align*}\nS(2) &= 105.658 \text{ MeV} \\\nS(3) &= \TauMassMeV \text{ MeV}\n\end{align*}...`

## unified-biquaternion-theory-master/consolidation_project/old/appendix_K_fundamental_constants_consolidated.tex
Hits: muon_mass
- muon_mass: `... 0.510\,998\,950\,69(16)\,\mathrm{MeV}$; Muon: $m_\mu c^2 = 105.658\,3755(23)\,\mathrm{MeV}$.}, \ntau mass from PDG 2024\footnot...`
- muon_mass: `...it \\\n$m_\mu c^2$ (MeV) & (mode index $\mu$; TBD number) & $105.658\,3755(23)$ & TBD \\\n$m_\tau c^2$ (MeV) & (mode index $\tau$...`

## unified-biquaternion-theory-master/consolidation_project/old/appendix_N_mass_predictions_consolidated.tex
Hits: muon_mass
- muon_mass: `...\,998\,950\,69 & 0 \\\n$\mu$ & 207  & 105.776\,782\,793    & 105.658\,3755       & $-1.121\times 10^{-3}$ \\\n$\tau$& 3477 & 1776...`

## unified-biquaternion-theory-master/consolidation_project/old/appendix_P_maxwell_curved_space.tex
Hits: electron_mass
- electron_mass: `...612 0.527217\n2.294486 0.521649\n2.344361 0.516251\n2.394236 0.511016\n2.444110 0.505935\n2.493985 0.501000\n2.543860 0.496206\n2.593...`

## unified-biquaternion-theory-master/consolidation_project/old/appendix_P_prime_alpha.tex
Hits: alpha_inv_approx
- alpha_inv_approx: `...ptimal value found is $N = 137$, yielding $\alpha \approx 1/137.035999$. However, other prime values may correspond to alternative...`

## unified-biquaternion-theory-master/data/leptons.csv
Hits: electron_mass
- electron_mass: `...mev,pole_mass_mev,mu_mev,alpha_mu\nelectron,e,0.509811991691,0.510996192910,0.509811991691,7.297352573757e-03\nmuon,mu,NOT_IMPLEMENTED,N...`

## unified-biquaternion-theory-master/docs/GLOSSARY_OF_SYMBOLS.md
Hits: alpha_inv_approx, tau_mass
- alpha_inv_approx: `...troweak theory |\n| α | Fine-structure constant | U(1) | ≈ 1/137.035999084 |\n| α(μ) | Running α at scale μ | U(1) | Energy-dependent |...`
- alpha_inv_approx: `...|-------|---------------|\n| α | Fine-structure constant | 1/137.035999084 | **Empirical input (CODATA 2018)** |\n| B or B_α | Vacuum p...`

## unified-biquaternion-theory-master/insensitivity/sweep.py
Hits: alpha_inv_approx
- alpha_inv_approx: `..._sigma_proxy, gamow_barrier_proxy\n\ndef run_sweep(alpha0_inv=137.035999, deltas=(-0.02, -0.0144, 0.0, 0.02), out_csv="insensitivity...`

## unified-biquaternion-theory-master/reports/alpha_equations.json
Hits: alpha_inv_approx, electron_mass, tau_mass
- alpha_inv_approx: `...\text{(UBT prediction)} \\\\\n\\alpha_{\\text{exp}}^{-1} &= 137.035999084 \\quad \\text{(CODATA 2018)} \\\\\n\\Delta\\alpha^{-1} &= 0...`
- alpha_inv_approx: `...\n      "content": "\\alpha_{\\text{exp}}^{-1}(Q^2 \\to 0) = 137.035999084(21)",\n      "label": null,\n      "path": "/home/runner/work...`

## unified-biquaternion-theory-master/scripts/emergent_alpha_calculator.py
Hits: alpha_inv_approx
- alpha_inv_approx: `...T = 137.0\n    \n    # Experimental value\n    alpha_inv_exp = 137.035999084\n    \n    # Difference\n    delta_alpha_inv = alpha_inv_exp -...`

## unified-biquaternion-theory-master/scripts/padic_alpha_calculator.py
Hits: alpha_inv_approx
- alpha_inv_approx: `... linewidth=2, label='p=137 (Our Universe)')\n    ax1.axhline(137.035999084, color='green', linestyle=':', linewidth=1.5, alpha=0.7, la...`
- alpha_inv_approx: `...0)\n    print("\nOur universe (p=137):")\n    alpha_inv_exp = 137.035999084\n    alpha_inv_ubt, alpha_ubt = calculate_alpha(137)\n    pri...`

## unified-biquaternion-theory-master/scripts/test_padic_alpha.py
Hits: alpha_inv_approx
- alpha_inv_approx: `...e very close to experimental value\n    expected_alpha_inv = 137.035999084  # CODATA 2018\n    error = abs(alpha_inv - expected_alpha_i...`

## unified-biquaternion-theory-master/scripts/test_symbolic_alpha.py
Hits: alpha_inv_approx, electron_mass
- alpha_inv_approx: `...ence value at low energy (same physics)\n    alpha_inv_low = 137.035999084  # CODATA 2018\n    \n    # Calculate α at some fixed scale μ...`
- alpha_inv_approx: `...    # Compare with experimental value\n    alpha_exp = 1.0 / 137.035999084  # CODATA 2018\n    error_percent = abs(alpha - alpha_exp) /...`

## unified-biquaternion-theory-master/scripts/ubt_complete_fermion_derivation.py
Hits: alpha_inv_approx, electron_mass, muon_mass, tau_mass
- alpha_inv_approx: `...t\n\n# Physical constants\nV_EW = 246000  # MeV\nALPHA_EM = 1 / 137.035999084  # Fine structure constant (CODATA 2018)\nHBAR_C = 197.327  ...`
- electron_mass: `...from PDG 2024 (MeV)\nEXPERIMENTAL_MASSES = {\n    'electron': 0.51099895000,\n    'muon': 105.6583755,\n    'tau': 1776.86,\n    'nu_e': 1...`

## unified-biquaternion-theory-master/scripts/ubt_fermion_mass_calculator.py
Hits: alpha_inv_approx, electron_mass, muon_mass, tau_mass
- alpha_inv_approx: `...Physical constants\nHBAR_C = 197.327  # MeV·fm\nALPHA = 1.0 / 137.035999084  # Fine structure constant (CODATA 2018)\nPI = np.pi\n\n# Expe...`
- electron_mass: `...PERIMENTAL_MASSES = {\n    # Charged Leptons\n    'electron': 0.51099895000,\n    'muon': 105.6583755,\n    'tau': 1776.86,\n    \n    # Ne...`

## unified-biquaternion-theory-master/scripts/ubt_quark_mass_derivation.py
Hits: alpha_inv_approx
- alpha_inv_approx: `...HBAR_C = 197.327  # MeV·fm (natural units)\nALPHA_EM = 1.0 / 137.035999084  # Fine structure constant (CODATA 2018)\nV_EW = 246000  # E...`

## unified-biquaternion-theory-master/scripts/validate_electron_mass.py
Hits: alpha_inv_approx, electron_mass
- alpha_inv_approx: `...dg = 0.51099895  # MeV (PDG 2024)\n    alpha_thomson = 1.0 / 137.035999\n    \n    print("Reference values (PDG 2024):")\n    print(f"...`
- electron_mass: `...\n    print()\n    \n    # Reference values\n    m_e_pole_pdg = 0.51099895  # MeV (PDG 2024)\n    alpha_thomson = 1.0 / 137.035999\n    ...`

## unified-biquaternion-theory-master/scripts/validate_ubt_derivations_symbolic.py
Hits: alpha_inv_approx
- alpha_inv_approx: `..._eff emerges from θ-function periodicity")\n    print("α⁻¹ ≈ 137.035999084 matches experimental value (CODATA 2018) ✓")\n    print()\n  ...`
- alpha_inv_approx: `...")\n    print()\n    \n    # Numerical check\n    alpha_val = 1/137.035999084\n    print(f"5.5 Experimental value:")\n    print(f"α_exp ≈ {...`

## unified-biquaternion-theory-master/tests/test_electron_mass.py
Hits: alpha_inv_approx, electron_mass
- alpha_inv_approx: `...51099895  # MeV, electron pole mass\nALPHA_INV_THOMSON_REF = 137.035999  # α⁻¹ at Thomson limit\n\n\ndef test_alpha_fit_free_identity(...`
- electron_mass: `..._pole_lepton\n\n\n# Reference values (PDG 2024)\nM_E_POLE_REF = 0.51099895  # MeV, electron pole mass\nALPHA_INV_THOMSON_REF = 137.0359...`

## unified-biquaternion-theory-master/tests/test_electron_mass_precision.py
Hits: electron_mass
- electron_mass: `...t))\n\n# Experimental electron pole mass (PDG 2024)\nM_E_REF = 0.51099895  # MeV\n\n# Precision tolerance\n# Current: 1e-4 (will be tigh...`

## unified-biquaternion-theory-master/tests/test_no_hardcoded_constants.py
Hits: electron_mass, muon_mass, tau_mass
- electron_mass: `...a^{-1} precise value\n    r"\b0\.5109989\d{2,}\b",   # m_e ~ 0.51099895...\n    r"\b105\.6583\d{2,}\b",    # m_mu ~ 105.658375...\n  ...`
- muon_mass: `...m_e ~ 0.51099895...\n    r"\b105\.6583\d{2,}\b",    # m_mu ~ 105.658375...\n    r"\b1776\.8\d{2,}\b",      # m_tau ~ 1776.86...\n]\n\n#...`

## unified-biquaternion-theory-master/tools/generate_tex_snippets_from_csv.py
Hits: alpha_inv_approx
- alpha_inv_approx: `...sMeV\nBehavior:\n  - Picks the row with smallest |alpha_inv - 137.035999| as the "best" sample (if alpha grid exists).\n  - Falls bac...`
- alpha_inv_approx: `...eturn None, None\n    # prefer the one closest to CODATA-ish 137.035999 (not a fit; just selector for presentation macro)\n    targe...`

## unified-biquaternion-theory-master/tools/replace_core_literals_with_macros.py
Hits: alpha_inv_approx, electron_mass, muon_mass, tau_mass
- alpha_inv_approx: `...efault; use --apply to write changes.\n\nPatterns replaced:\n  137.0359990...     -> \AlphaInvBest\n  0.51099895...      -> \ElectronMa...`
- electron_mass: `...\nPatterns replaced:\n  137.0359990...     -> \AlphaInvBest\n  0.51099895...      -> \ElectronMassMeV\n  105.658375...      -> \MuonMa...`

## unified-biquaternion-theory-master/ubt_audit_pack_v1/tools/audit_computed_not_reference.py
Hits: alpha_inv_approx, electron_mass, muon_mass, tau_mass
- alpha_inv_approx: `....py (forbidden in non-generated files):\n     - alpha^{-1} ≈ 137.0359990...\n     - m_e ≈ 0.51099895...\n     - m_μ ≈ 105.658375...\n  ...`
- electron_mass: `...ted files):\n     - alpha^{-1} ≈ 137.0359990...\n     - m_e ≈ 0.51099895...\n     - m_μ ≈ 105.658375...\n     - m_τ ≈ 1776.86...\n  2) ...`

## unified-biquaternion-theory-master/ubt_masses/core.py
Hits: alpha_inv_approx, electron_mass
- alpha_inv_approx: `...easonable initial guess for α(m_e)\n        alpha_mu = 1.0 / 137.035999\n    \n    # QED 1-loop correction estimate\n    delta_qed = (...`
- electron_mass: `...formula\n    \n    # Experimental pole mass (PDG 2024): m_e = 0.51099895 MeV\n    # MSbar mass at μ = m_e is approximately:\n    # m̄_...`

## unified-biquaternion-theory-master/unified_biquaternion_theory/fermion_mass_derivation_complete.tex
Hits: muon_mass
- muon_mass: `...on & 1 & 0.509856 & \ElectronMassMeV & 0.22\% \\\nMuon & 2 & 105.658 & 105.658 & 0.0001\% \\\nTau & 3 & \TauMassMeV & \TauMassMeV...`
- muon_mass: `....509856 & \ElectronMassMeV & 0.22\% \\\nMuon & 2 & 105.658 & 105.658 & 0.0001\% \\\nTau & 3 & \TauMassMeV & \TauMassMeV & 0.0001\...`

## unified-biquaternion-theory-master/unified_biquaternion_theory/docs/osf_release/main.tex
Hits: electron_mass, muon_mass, tau_mass
- electron_mass: `...f{Experiment [MeV]} \\\n\hline\nElectron (\(n=1\)) & 0.5110 & 0.51099895 \\\nMuon (\(n=2\)) & 105.66 & 105.65837 \\\nTauon (\(n=3\)) &...`
- muon_mass: `...\(n=1\)) & 0.5110 & 0.51099895 \\\nMuon (\(n=2\)) & 105.66 & 105.65837 \\\nTauon (\(n=3\)) & 1776.86 & 1776.86 \(\pm\) 0.12 \\\n\hli...`

## unified-biquaternion-theory-master/unified_biquaternion_theory/docs/osf_release_not_released/unified_biquaternion_theory.tex
Hits: electron_mass, muon_mass, tau_mass
- electron_mass: `...tbf{Relative Error} \\\n\hline\nElectron (\(n=1\)) & 0.5110 & 0.51099895 & \(< 0.001\%\) \\\nMuon (\(n=2\)) & 105.66 & 105.65837 & \(...`
- muon_mass: `...0 & 0.51099895 & \(< 0.001\%\) \\\nMuon (\(n=2\)) & 105.66 & 105.65837 & \(< 0.002\%\) \\\nTauon (\(n=3\)) & 1776.86 & 1776.86 \(\p...`

## unified-biquaternion-theory-master/unified_biquaternion_theory/solution_P4_fine_structure_constant/README.md
Hits: alpha_inv_approx
- alpha_inv_approx: `...entally observed value:\n\[\n\alpha^{-1}_{\text{exp}} \approx 137.035999...\n\]\nwe computed one-loop quantum corrections using the va...`

## unified-biquaternion-theory-master/unified_biquaternion_theory/solution_P5_dark_matter/ThetaM_TopologicalMassFit.tex
Hits: muon_mass
- muon_mass: `...ection*{Fit to Muon and Tau}\n\nUsing:\n\begin{align*}\nS(2) &= 105.658 \text{ MeV} \\\nS(3) &= \TauMassMeV \text{ MeV}\n\end{align*}...`

## unified-biquaternion-theory-master/unified_biquaternion_theory/validation/README.md
Hits: tau_mass
- tau_mass: `....22% error\n✓ Muon: 105.66 MeV (fitted) - exact match\n✓ Tau: 1776.86 MeV (fitted) - exact match\n```\n\n**Run:**\n```bash\npython3 va...`

## unified-biquaternion-theory-master/unified_biquaternion_theory/validation/validate_alpha_constant.py
Hits: alpha_inv_approx
- alpha_inv_approx: `...nt("1. EXPERIMENTAL VALUE")\nprint("-" * 70)\nalpha_inv_exp = 137.035999084  # Latest CODATA value\nalpha_exp = 1 / alpha_inv_exp\n\nprint...`

## unified-biquaternion-theory-master/unified_biquaternion_theory/validation/validate_electron_mass.py
Hits: electron_mass, muon_mass, tau_mass
- electron_mass: `...mula}")\nprint()\n\n# Experimental values (PDG 2024)\nm_e_exp = 0.51099895  # MeV\nm_mu_exp = 105.6583755  # MeV\nm_tau_exp = 1776.86  #...`
- muon_mass: `...al values (PDG 2024)\nm_e_exp = 0.51099895  # MeV\nm_mu_exp = 105.6583755  # MeV\nm_tau_exp = 1776.86  # MeV\n\nprint("2. EXPERIMENTAL V...`
