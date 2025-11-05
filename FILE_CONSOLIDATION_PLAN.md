# File Consolidation Plan

**Goal:** Reduce 79+ markdown files to ~40 by consolidating redundant documentation

## Files to Remove (Information Preserved Elsewhere)

### Alpha Derivation Files (Keep: FITTED_PARAMETERS.md, consolidation appendices)
- [ ] ALPHA_DERIVATION_IMPLEMENTATION.md → Info in FITTED_PARAMETERS.md
- [ ] ALPHA_HARMONIZATION_GUIDE.md → Info in FITTED_PARAMETERS.md
- [ ] ALPHA_IMPACT_ON_UBT_EVALUATION.md → Info in evaluations
- [ ] ALPHA_PADIC_README.md → Info in scripts/DATA_ANALYSIS_README.md
- [ ] QUICKSTART_EMERGENT_ALPHA.md → Info in OVERVIEW.md
- [ ] COMMENT_RESPONSE_ALPHA_RIGOR.md → Obsolete (addressed)
- [ ] SYMBOL_B_USAGE_CLARIFICATION.md → Info in FITTED_PARAMETERS.md
**Keep:** ALPHA_SYMBOLIC_B_DERIVATION.md (technical details), B_CONSTANT_DERIVATION_SUMMARY.md (historical context), EMERGENT_ALPHA_README.md (links to code)

### Evaluation/Rating Files (Keep latest comprehensive ones)
- [ ] ALPHA_IMPACT_ON_UBT_EVALUATION.md → Covered in comprehensive evaluations
- [ ] UBT_RATING_NOV4_2025.md → Superseded by UBT_UPDATED_SCIENTIFIC_RATING_2025.md
- [ ] REEVALUATION_SUMMARY.md → Info in UBT_REEVALUATION_2025.md
- [ ] EVALUATION_EXECUTIVE_SUMMARY.md → Can merge into README or keep as quick ref
**Keep:** UBT_COMPREHENSIVE_EVALUATION_REPORT.md, UBT_REEVALUATION_2025.md, UBT_UPDATED_SCIENTIFIC_RATING_2025.md, UBT_SCIENTIFIC_RATING_2025.md (baseline)

### Summary/Completion Reports (Merge into CHANGELOG)
- [ ] TASK_COMPLETION_SUMMARY.md → Add to CHANGELOG
- [ ] TASK_COMPLETION_EMAIL_AND_GUIDES.md → Obsolete
- [ ] PRIORITY_1_COMPLETION_SUMMARY.md → Add to CHANGELOG
- [ ] FERMION_MASS_ACHIEVEMENT_SUMMARY.md → Add to CHANGELOG
- [ ] FERMION_MASS_COMPLETE_REPORT.md → Keep (technical details)
- [ ] FINAL_IMPROVEMENTS_REPORT.md → Add to CHANGELOG
- [ ] FINAL_SUMMARY.md → Add to CHANGELOG
- [ ] NEUTRINO_DERIVATION_VERIFICATION.md → Keep (technical)
- [ ] QUANTUM_GRAVITY_IMPLEMENTATION_SUMMARY.md → Add to CHANGELOG

### Version-Specific Files (Archive or consolidate)
- [ ] UBT_V8_COMPLETION_SUMMARY.md → Add to CHANGELOG
- [ ] UBT_V9_IMPLEMENTATION_SUMMARY.md → Add to CHANGELOG
- [ ] UBT_V10_IMPLEMENTATION_SUMMARY.md → Add to CHANGELOG
- [ ] UBT_V8_REEVALUATION_AND_TOE_COMPARISON.md → Superseded by newer evals

### Issue Resolution Files (Consolidate)
- [ ] ISSUES_ADDRESSED.md → Merge with CHANGELOG
- [ ] ISSUE_RESOLUTION_SUMMARY.md → Merge with CHANGELOG
- [ ] UBT_CONCERNS_FIXES.md → Merge with CHANGELOG
- [ ] CHANGES_ADDRESSING_EVALUATION.md → Merge with CHANGELOG
- [ ] UBT_IMPROVEMENTS_SUMMARY.md → Keep or merge

### Checklists (Keep or consolidate)
- [ ] IMPLEMENTATION_VERIFICATION_CHECKLIST.md → Useful, keep
- [ ] REPOSITORY_RELEASE_CHECKLIST.md → Useful, keep
- [ ] verification_checklist.md → Duplicate? Consolidate

### Publication Guides (Czech) - Move to docs/ subfolder
- [ ] PUBLIKACE_RYCHLY_START_CZ.md → Move to docs/
- [ ] OSF_PUBLIKACE_NAVOD_CZ.md → Move to docs/
- [ ] ZENODO_PUBLIKACE_NAVOD_CZ.md → Move to docs/
- [ ] ANALYZA_VEDECKYCH_DAT_CZ.md → Move to docs/
- [ ] LAMB_SHIFT_PROBLEM_A_UBT_SROVNANI_CZ.md → Move to docs/
- [ ] UBT_LEPSI_NEZ_SM_STRING_SROVNANI_CZ.md → Move to docs/

### Data Analysis Files (Keep but maybe consolidate)
- [ ] DATA_ANALYSIS_ACTION_ITEMS.md → Merge into DATA_ANALYSIS_PROJECT_SUMMARY.md?
**Keep:** DATA_ANALYSIS_PROJECT_SUMMARY.md, UBT_DATA_ANALYSIS_SCIENTIFIC_SUPPORT.md, SCIENTIFIC_DATA_SOURCES_BIBLIOGRAPHY.md

### Specialized Technical Files (Keep)
- [x] AHARONOV_TSVF_ANALYSIS.md - Unique content
- [x] EXPERIMENTAL_TESTS_TRANSITION_CRITERION.md - Important
- [x] HOLOGRAPHIC_COMPUTATIONAL_METHODS.md - Technical details
- [x] HOLOGRAPHIC_EXTENSION_GUIDE.md - Technical guide
- [x] HYPERSPACE_WAVES_INTEGRATION_ASSESSMENT.md - Important decision doc
- [x] LAMB_SHIFT_EXPLANATION.md - Unique content
- [x] MATHEMATICAL_FOUNDATIONS_COMPLETION.md - Status tracking
- [x] MATHEMATICAL_FOUNDATIONS_TODO.md - Active TODO list
- [x] MATHEMATICAL_REVIEW_REPORT.md - Important review
- [x] MODIFIED_GRAVITY_PREDICTION.md - Active research
- [x] SM_GAUGE_GROUP_RIGOROUS_DERIVATION.md - Key derivation
- [x] SM_GEOMETRIC_EMERGENCE_DRAFT.md - Research draft
- [x] THETA_FIELD_DEFINITION.md - Technical definition
- [x] TRANSITION_CRITERION_COMPLEX_BIQUATERNIONIC.md - Important criterion
- [x] UBT_HARDENING_COMPLETE_REPORT.md - Important milestone
- [x] UBT_ORIGINALITY_REPORT.md - Important for priority

### Keep Core Documentation (New Comprehensive Docs)
- [x] OVERVIEW.md - Essential starting point
- [x] ROADMAP.md - Essential planning
- [x] FITTED_PARAMETERS.md - Essential transparency
- [x] LITERATURE_COMPARISON.md - Essential academic context
- [x] PEER_REVIEW_ROADMAP.md - Essential for publication
- [x] SPECULATIVE_VS_EMPIRICAL.md - Essential categorization
- [x] TESTABILITY_AND_FALSIFICATION.md - Essential scientific rigor
- [x] CONTRIBUTING.md - Essential for community
- [x] CODE_OF_CONDUCT.md - Essential for community

### Keep Essential Existing Docs
- [x] README.md - Main entry point
- [x] LICENSE.md - Legal requirement
- [x] PRIORITY.md - Author priority claim
- [x] RESEARCH_PRIORITIES.md - Active priorities
- [x] CHANGELOG.md - Version history
- [x] UBT_READING_GUIDE.md - Navigation guide
- [x] CONSCIOUSNESS_CLAIMS_ETHICS.md - Important ethics
- [x] UBT_SCIENTIFIC_STATUS_AND_DEVELOPMENT.md - Status doc
- [x] REMAINING_CHALLENGES_DETAILED_STATUS.md - Current challenges
- [x] UBT_VS_OTHER_THEORIES_COMPARISON.md - Important comparison
- [x] UBT_DEVELOPMENT_SUMMARY_NOV2025.md - Recent summary

## Action Plan

1. **Create docs/czech/** subdirectory
2. **Move Czech docs** to docs/czech/
3. **Update CHANGELOG.md** with info from completion reports
4. **Remove redundant files** listed above
5. **Update cross-references** in remaining files
6. **Test all links** to ensure no broken references

## Expected Result

- **Before:** 79 markdown files
- **After:** ~40-45 markdown files
- **Reduction:** ~40-45% fewer files
- **Benefit:** Easier navigation, less duplication, clearer structure
