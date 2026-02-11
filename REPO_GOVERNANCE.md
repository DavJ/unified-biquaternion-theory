# UBT Repository Governance

**Version**: 1.0  
**Date**: 2026-01-10  
**Purpose**: Define clear rules for canonical vs. speculative content classification and organization

---

## Overview

This document establishes governance rules for the Unified Biquaternion Theory (UBT) repository to ensure scientific integrity, proper content classification, and reproducible research practices. It defines what belongs in `canonical/`, what belongs in `speculative_extensions/`, and how to maintain clear boundaries between empirically validated and hypothetical content.

---

## Core Principles

1. **Scientific Integrity**: Separate validated derivations from speculative hypotheses
2. **Reproducibility**: All empirical claims must be verifiable and reproducible
3. **Transparency**: Clear labeling of rigor level for all content
4. **No Post-Hoc Fitting**: Pre-register predictions before data analysis
5. **Cross-Reference Discipline**: Speculative content must link to canonical definitions without redefining them

---

## Content Classification System

### 🟢 Canonical Content (`canonical/`)

**What Belongs Here:**
- Rigorous mathematical definitions (Θ-field, biquaternions, metric, stress-energy tensor)
- Proven derivations (GR equivalence, SM gauge group emergence)
- Symbol dictionary (authoritative definitions of all mathematical symbols)
- Core field equations with complete proofs
- Validated predictions with complete derivation chains

**Criteria for Canonical Status:**
- Mathematical proof complete and verified
- Consistent with established physics in appropriate limits
- No free parameters or post-hoc fitting (or transparently documented if fitted)
- Peer-reviewed or independently verified (preferred but not required)

**Examples:**
- `canonical/fields/theta_field.tex` - Biquaternion field Θ(q,T_B) definition
- `canonical/geometry/metric.tex` - Metric tensor g_μν derivation
- `canonical/CANONICAL_DEFINITIONS.md` - Symbol dictionary

**Modification Rules:**
- Changes require justification and documentation
- Backwards-incompatible changes trigger version increment
- Original content preserved in version history
- All files include version headers

### 🔵 Speculative Extensions (`speculative_extensions/`)

**What Belongs Here:**
- Hypotheses without quantitative predictions
- Exploratory mathematical frameworks
- Interpretations and philosophical implications
- Unverified mappings or applications
- Content requiring extensive future work for validation

**Criteria for Speculative Classification:**
- Qualitative framework only, OR
- No numerical predictions, OR
- Testability unclear or distant future, OR
- Requires assumptions beyond core UBT

**Examples:**
- `speculative_extensions/complex_consciousness/` - Consciousness modeling (psychons, CTCs)
- `speculative_extensions/appendices/appendix_P2_multiverse_projection.tex` - Multiverse interpretation
- `speculative_extensions/appendices/appendix_J_rotating_spacetime_ctc.tex` - Closed timelike curves

**Warning Requirements:**
- Must include `\SpeculativeContentWarning` in LaTeX documents
- Must have clear disclaimer in markdown files
- Must reference canonical definitions without redefining
- Must state what is assumed vs. derived

### 🟡 Semi-Empirical Content (Intermediate Status)

**What This Means:**
- Framework rigorous but details incomplete
- Prediction matches experiment but derivation has gaps
- Mostly derived with some fitted components

**Examples:**
- Fine-structure constant derivation (baseline geometric, renormalization in progress)
- Electron mass prediction (topology proven, quantum corrections being calculated)

**Documentation Requirements:**
- Explicit statement of what's validated vs. what's fitted
- Clear description of remaining gaps
- Roadmap to complete derivation
- Transparent parameter documentation in `FITTED_PARAMETERS.md`

### 🔴 Empirical/Validation Content (`forensic_fingerprint/`, `tools/planck_validation/`)

**What Belongs Here:**
- Pre-registered statistical tests
- Data analysis protocols
- Validation pipelines against observational data
- Reproducible computational implementations

**Critical Requirements:**
- **Pre-registration**: Hypotheses, parameters, and methods fixed before examining data
- **No post-hoc fitting**: Parameters locked in protocol documents before analysis
- **Provenance**: All datasets documented with SHA-256 hashes
- **Reproducibility**: Fixed random seeds, version-controlled code
- **Transparency**: Both positive and null results reported

**Examples:**
- `forensic_fingerprint/PROTOCOL.md` - Three pre-registered statistical tests
- `tools/planck_validation/` - Planck 2018 parameter mapping implementation
- `tools/data_provenance/` - Dataset verification tools

---

## Cross-Referencing Rules

### Rule 1: Symbol Consistency
**All documents MUST use symbols as defined in `canonical/CANONICAL_DEFINITIONS.md`**

- ✅ **DO**: `\tau` for complex time (isotropic limit), `T_B` for biquaternion time (canonical)
- ❌ **DON'T**: Redefine `\tau` to mean something different in appendices

### Rule 2: Definition References
**Speculative documents MUST link to canonical definitions**

- ✅ **DO**: "Using the Θ-field as defined in `canonical/fields/theta_field.tex`..."
- ❌ **DON'T**: Introduce new definitions of Θ without explicit justification

### Rule 3: No Redefinition
**Speculative content MUST NOT redefine canonical symbols**

If a speculative extension needs additional structure:
- Introduce new symbols (e.g., Θ_ext for extended field)
- Explicitly state relationship to canonical definition
- Document in speculative appendix, not canonical directory

### Rule 4: Derivation Chains
**All claims must trace back to canonical definitions**

- Empirical predictions → canonical equations → mathematical foundations
- If chain is incomplete, document in semi-empirical or speculative category
- No orphaned claims without derivation path

---

## "No-Fit / No Post-Hoc" Policy for Predictions

### Pre-Registration Requirements

**For any claimed prediction against observational data:**

1. **Protocol First**: Document the mapping/formula BEFORE analyzing data
2. **Parameters Locked**: All tunable parameters fixed in advance
3. **Thresholds Fixed**: Success/failure criteria stated before results
4. **Version Control**: Protocol committed to repository with timestamp
5. **Public Archive**: Protocol archived (Zenodo/OSF) for third-party verification

### Prohibited Practices

❌ **Post-hoc parameter tuning**: Adjusting parameters after seeing data  
❌ **Cherry-picking**: Selecting favorable datasets and hiding unfavorable ones  
❌ **P-hacking**: Running multiple analyses and reporting only significant results  
❌ **Moving goalposts**: Changing success criteria after seeing results  
❌ **Selective reporting**: Publishing positive results while suppressing null results

### Enforcement

- All validation code in `tools/planck_validation/` uses **locked constants** (no runtime parameters)
- Tests in `tests/test_planck_validation_mapping.py` enforce exact numerical outputs
- CI/CD pipeline fails if predictions change without protocol update
- Protocol version increments documented in `forensic_fingerprint/PROTOCOL.md`

### Example: Grid Denominator Lock

**Correct (Protocol v1.0):**
```python
# forensic_fingerprint/grid_255/config.py
GRID_DENOMINATOR = 255  # LOCKED - Protocol v1.0 - DO NOT CHANGE
```

**Incorrect:**
```python
# ❌ BAD: Runtime parameter allows post-hoc tuning
GRID_DENOMINATOR = int(sys.argv[1])  # Allows 255, 256, 257, etc.
```

---

## Where to Put New Work

### Decision Tree

**New Content → Ask:**

1. **Is it a core definition or proven derivation?**
   - YES → `canonical/` (with version header and proof)
   - NO → Continue

2. **Does it make quantitative predictions?**
   - YES → Continue to #3
   - NO → `speculative_extensions/` (with disclaimer)

3. **Are predictions testable with current data?**
   - YES → Continue to #4
   - NO → `speculative_extensions/` (theoretical framework)

4. **Is the derivation complete and fit-free?**
   - YES → `canonical/` or main repository (with validation)
   - PARTIAL → Semi-empirical (document gaps in `FITTED_PARAMETERS.md`)
   - NO → `speculative_extensions/` (mark as hypothesis)

5. **Does it involve data analysis or validation?**
   - YES → `forensic_fingerprint/` or `tools/` (with pre-registration protocol)
   - NO → Follow classification from steps 1-4

### Quick Reference Table

| Content Type | Location | Requirements |
|-------------|----------|--------------|
| Core definitions | `canonical/` | Proof, version header, no redefinition |
| Proven derivations | `canonical/` or main | Complete derivation chain, verification |
| Semi-empirical predictions | Main repository | Document gaps, roadmap, transparency |
| Speculative hypotheses | `speculative_extensions/` | Disclaimer, link to canonical, state assumptions |
| Data validation | `forensic_fingerprint/` or `tools/` | Pre-registration, locked parameters, provenance |
| Consciousness/CTC content | `speculative_extensions/complex_consciousness/` | Strong disclaimer, ethical guidelines |

---

## Directory Structure Summary

```
unified-biquaternion-theory/
├── canonical/                    # 🟢 Canonical definitions (single source of truth)
│   ├── CANONICAL_DEFINITIONS.md # Master symbol dictionary
│   ├── fields/                   # Field definitions (Θ, T_B, metric, etc.)
│   ├── geometry/                 # Geometric structures (curvature, GR equivalence)
│   ├── interactions/             # SM gauge structure (QED, QCD, Yukawa)
│   └── appendices/               # Canonical appendices
│
├── speculative_extensions/       # 🔵 Speculative/hypothetical content
│   ├── README.md                # Strong disclaimers
│   ├── complex_consciousness/   # Consciousness modeling (highly speculative)
│   └── appendices/              # Speculative appendices (psychons, CTCs, multiverse)
│
├── forensic_fingerprint/         # 🔴 Pre-registered empirical tests
│   ├── PROTOCOL.md              # Locked protocol (no post-hoc changes)
│   ├── cmb_comb/                # CMB comb signature test
│   ├── grid_255/                # Grid quantization test
│   └── invariance/              # Cross-dataset invariance test
│
├── tools/                        # Computational implementations
│   ├── planck_validation/       # Planck 2018 mapping (locked parameters)
│   └── data_provenance/         # Dataset hashing and verification
│
├── tests/                        # Pytest validation suite
│   ├── test_forensic_fingerprint.py
│   └── test_planck_validation_mapping.py
│
├── unified_biquaternion_theory/ # Original UBT documents (historical, read-only)
├── consolidation_project/       # Consolidated UBT documents
└── data/                         # Data ingestion scaffolding (no large files committed)
```

---

## Compliance and Enforcement

### For Contributors

**Before adding new content:**
1. Read this document
2. Classify your content using the decision tree
3. Follow directory and documentation requirements
4. Include appropriate disclaimers/version headers
5. Submit PR with justification for classification

### For Reviewers

**PR review checklist:**
- [ ] Content properly classified (canonical vs. speculative)?
- [ ] Symbols consistent with `canonical/CANONICAL_DEFINITIONS.md`?
- [ ] Cross-references to canonical definitions present?
- [ ] Appropriate disclaimers/version headers included?
- [ ] No post-hoc fitting in empirical validation code?
- [ ] Pre-registration protocol followed for data analysis?

### For Maintainers

**Quarterly audit:**
- [ ] Review all new content for proper classification
- [ ] Check for symbol redefinitions or conflicts
- [ ] Verify empirical validation code hasn't introduced tunable parameters
- [ ] Update this document if new categories needed
- [ ] Document classification changes in `CHANGELOG.md`

---

## Relationship to Existing Documents

This governance document supersedes and consolidates rules from:
- `canonical/README.md` - Canonical content rules
- `speculative_extensions/README.md` - Speculative content disclaimers  
- `SPECULATIVE_VS_EMPIRICAL.md` - Classification system
- `CONTRIBUTING.md` - Contribution guidelines

**In case of conflict:**
1. `REPO_GOVERNANCE.md` (this document) is authoritative
2. Specific directory READMEs provide additional detail
3. Older documents preserved for historical context

---

## Updates and Versioning

**This document follows semantic versioning:**
- **Major version (X.0)**: Fundamental changes to classification system
- **Minor version (1.X)**: New categories or significant rule additions
- **Patch (1.0.X)**: Clarifications and minor corrections

**Version History:**
- **v1.0** (2026-01-10): Initial governance document

**Review Schedule:** Quarterly  
**Next Review:** 2026-04-10  
**Responsibility:** Repository maintainers

---

## Questions and Exceptions

**For questions about classification:**
1. Check this document's decision tree
2. Review `SPECULATIVE_VS_EMPIRICAL.md` for examples
3. Open GitHub issue with `governance` label
4. Maintainers will provide guidance

**For exceptional cases:**
- Open issue before creating content
- Explain why existing categories don't fit
- Propose new category or classification
- Wait for maintainer approval

---

## Summary

**Key Takeaways:**
1. **Canonical** = proven, rigorous, single source of truth
2. **Speculative** = hypothetical, disclaimer required, link to canonical
3. **No post-hoc fitting** = pre-register before analyzing data
4. **Symbol consistency** = use canonical definitions, never redefine
5. **Transparency** = document gaps, fitted parameters, assumptions

**Goal:** Enable fair scientific evaluation of UBT by clearly separating validated content from speculation.

---

**Document Status:** Active governance policy  
**Compliance:** Required for all new contributions  
**Authority:** Repository maintainers  
**Contact:** GitHub issues with `governance` label
