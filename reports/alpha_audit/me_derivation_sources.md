# Electron Mass (m_e) Derivation Sources

## Search Results

Searched for electron mass references across Python, Markdown, and LaTeX files.

### Keyword: `m_e.*=`

Found 371 occurrences

#### File: `validate_alpha_renormalization.py`

Line 91: `print("  The UBT prediction α⁻¹(m_e) = 137.107 achieves ~0.05% precision,")`

#### File: `tests/test_electron_mass.py`

Line 44: `M_E_POLE_REF = 0.51099895  # MeV, electron pole mass`

Line 158: `f"  Computed: m_e = {m_pole:.9f} MeV\n"`

Line 159: `f"  Reference: m_e = {M_E_POLE_REF:.9f} MeV\n"`

#### File: `tests/test_electron_mass_precision.py`

Line 23: `M_E_REF = 0.51099895  # MeV`

#### File: `tests/test_no_circularity.py`

Line 136: `# ∂m_exp/∂(anything in theory) = 0  (experimental data is external)`

Line 251: `Explicit numerical test: ∂M_theory/∂m_exp = 0 at tree level.`

Line 265: `m_exp_original = np.array([0.01, 0.1, 1.0])`

#### File: `cern_findings_and_ubt/analyze_cern_ubt_signatures.py`

Line 22: `M_ELECTRON = 0.511  # MeV/c²`

Line 245: `ax1.set_title('UBT Mass Quantization: M = n × m_e', fontsize=14, fontweight='bold')`

Line 267: `ax2.set_ylabel('Residual: M_measured - n×m_e (MeV)', fontsize=12)`

---

### Keyword: `electron.*mass.*=`

Found 86 occurrences

#### File: `tests/test_docs_use_generated_csv.py`

Line 103: `electron_mass = electron_rows[0]["pole_mass_mev"]`

Line 104: `assert electron_mass != "NOT_IMPLEMENTED", (`

#### File: `ubt_masses/core.py`

Line 114: `Electron MSbar mass m̄_e in MeV at μ = m̄_e`

#### File: `ubt_masses/export_leptons_csv.py`

Line 52: `print(f"Warning: Could not compute electron mass: {e}", file=sys.stderr)`

#### File: `scripts/alpha_circularity_audit.py`

Line 111: `r'electron.*mass.*=',`

#### File: `scripts/validate_electron_mass.py`

Line 54: `print(f"  Electron pole mass (PDG, for comparison): m_e = {m_e_pole_pdg:.9f} MeV")`

---

### Keyword: `mass.*electron`

Found 185 occurrences

#### File: `tests/test_layer2_predictors_placeholder_vs_ubt.py`

Line 33: `assert 'electron_mass' in predictions, "Should predict electron_mass"`

Line 37: `assert isinstance(predictions['electron_mass'], (int, float)), "electron_mass should be numeric"`

#### File: `tests/test_docs_use_generated_csv.py`

Line 103: `electron_mass = electron_rows[0]["pole_mass_mev"]`

Line 109: `mass_val = float(electron_mass)`

#### File: `ubt_masses/core.py`

Line 102: `def ubt_mass_operator_electron_msbar(alpha_mu: float | None = None) -> float:`

Line 104: `UBT mass operator for electron in MSbar scheme.`

Line 122: `# UBT Mass Operator - Electron MSbar Mass`

#### File: `cern_findings_and_ubt/analyze_cern_ubt_signatures.py`

Line 63: `masses = n * M_ELECTRON`

Line 100: `n_best = np.round(mass / M_ELECTRON)`

Line 198: `mass = n * M_ELECTRON * hopf_suppression`

#### File: `scripts/alpha_circularity_audit.py`

Line 112: `r'mass.*electron',`

---

### Keyword: `hopfion.*mass`

Found 64 occurrences

#### File: `scripts/alpha_circularity_audit.py`

Line 113: `r'hopfion.*mass',`

#### File: `SPECULATIVE_VS_EMPIRICAL.md`

Line 269: `| **Hopfion fermion mass** | 🟡 SEMI-EMPIRICAL | Layer B | Topology solid, coefficients fitted |`

Line 395: `> "🟡 SEMI-EMPIRICAL: UBT predicts m_e = 0.510 MeV from hopfion topology (0.22% error). The topologic`

#### File: `RESEARCH_PRIORITIES.md`

Line 63: `2. Hopfion mass formula coefficients (A, p, B) - **Layer B refinement**`

#### File: `CURRENT_STATUS.md`

Line 113: `**Hopfion Mass Baseline:** m_e = 0.509856 MeV ✅`

Line 421: `**Baseline Hopfion Mass** ✅ COMPLETE`

#### File: `ELECTRON_MASS_REFINEMENT_ANALYSIS.md`

Line 156: `3. Add to bare Hopfion mass`

---

### Keyword: `0\.51.*MeV`

Found 302 occurrences

#### File: `validate_alpha_renormalization.py`

Line 80: `print(f"✓ Two-loop running: α⁻¹(0.511 MeV) = {alpha_inv_me:.9f}")`

#### File: `tests/test_alpha_provenance.py`

Line 37: `mu = 0.511  # MeV`

#### File: `tests/test_electron_mass.py`

Line 44: `M_E_POLE_REF = 0.51099895  # MeV, electron pole mass`

Line 54: `mu = 0.511  # MeV, approximate electron mass scale`

Line 104: `m_msbar_input = 0.510  # MeV`

#### File: `tests/test_electron_mass_precision.py`

Line 23: `M_E_REF = 0.51099895  # MeV`

#### File: `ubt_masses/core.py`

Line 132: `# 1. The UBT topological mass formula suggests m_e ≈ 0.510 MeV (bare)`

Line 133: `# 2. This is ~0.2% lower than experimental PDG value of 0.51099895 MeV`

Line 152: `# The UBT derivation should give m_e ≈ 0.510 MeV from Hopfion topology`

---

## Key Files for m_e Derivation

- `ELECTRON_MASS_REFINEMENT_ANALYSIS.md`
- `scripts/validate_electron_mass.py`
- `tests/test_electron_mass.py`
- `tests/test_electron_mass_precision.py`
- `ubt_masses/core.py`
- `ubt_masses/export_leptons_csv.py`

## Known Relevant Files (from search)

- ✓ `TOOLS/simulations/validate_electron_mass.py` (exists)
  - Contains 8 mathematical expressions
- ✓ `TOOLS/simulations/ubt_complete_fermion_derivation.py` (exists)
  - Contains 37 mathematical expressions
- ✓ `TOOLS/simulations/fit_flavour_minimal.py` (exists)
  - Contains 16 mathematical expressions
- ✓ `appendix_E_m0_derivation_strict.tex` (exists)
  - Contains 61 mathematical expressions
- ✓ `original_release_of_ubt/solution_P4_fine_structure_constant/alpha_constant_derivation.tex` (exists)
  - Contains 4 mathematical expressions
