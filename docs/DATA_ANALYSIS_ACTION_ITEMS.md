<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Issues Identified in Data Analysis - Action Items

## Critical Issues Requiring Resolution

### 1. Lamb Shift Prediction Numerical Inconsistency (RESOLVED ✅)

**Location:** `consolidation_project/appendix_W_testable_predictions.tex`, Prediction 4.1

**Problem:**
The UBT prediction for Lamb shift correction had numerical inconsistency:
- Stated correction: "~10 kHz" for hydrogen n=2 (INCORRECT)
- Formula: ΔE_Lamb^UBT = ΔE_Lamb^QED + δ_ψ × (α⁵ m_e c²) / n³
- With δ_ψ = 2.3 × 10⁻⁶

**Analysis:**
```
Standard Lamb shift (n=2): 1057.8446 MHz
α⁵ m_e c² / 8 ≈ 320 MHz (corrected calculation)
UBT correction: 2.3 × 10⁻⁶ × 320 MHz ≈ 0.7 kHz (≈ 1 kHz)

Fractional shift: 1 kHz / 1057.8 MHz ≈ 9 × 10⁻⁷ (0.0009%)
```

**Resolution:**
- ✅ The formula is **correct** as stated
- ✅ The numerical estimate "~10 kHz" was **incorrect**
- ✅ **Corrected to "~1 kHz"** (matches formula calculation)
- ✅ Added explanatory note with calculation details
- ✅ Updated timeline: 2-5 years → 5-10 years (more realistic for 1 kHz precision)

**Impact:**
- Correction is ~1 kHz: **Below current measurement precision** (~MHz level)
- Requires ~1000× improvement in spectroscopy precision
- Still testable with next-generation optical frequency combs (5-10 year timeline)
- No conflict with existing experiments (UBT is consistent with all data)

**Actions Completed:**
1. ✅ **Created**: Comprehensive explanation in `LAMB_SHIFT_EXPLANATION.md`
2. ✅ **Updated**: `consolidation_project/appendix_W_testable_predictions.tex`
3. ✅ **Updated**: `UBT_DATA_ANALYSIS_SCIENTIFIC_SUPPORT.md`
4. ✅ **Updated**: `UBT_VS_OTHER_THEORIES_COMPARISON.md`
5. ✅ **Verified**: No other files contain the incorrect value

**Status:** ✅ **RESOLVED** - Numerical error corrected throughout documentation

**Date Resolved:** November 2, 2025

---

## Minor Improvements

### 2. Data Source Specificity (LOW PRIORITY)

**Location:** `scripts/analyze_dark_matter_limits.py`, lines 57-58

**Issue:** Experimental limits are approximate (digitized from plots)

**Improvement:**
- Add direct links to HEPData entries
- Use exact numerical tables when available
- Document digitization procedure

**Actions:**
- ⏳ Add HEPData URLs to script comments
- ⏳ Create function to download HEPData directly (if API available)

**Status:** 🟢 Minor - current approximation adequate for demonstration

### 3. Author Attribution (LOW PRIORITY)

**Location:** Script headers

**Issue:** Generic "UBT Research Team" used

**Improvement:**
- Use specific author names or "David Jaroš (UBT Developer)" + contributors
- Add contact email or GitHub username

**Actions:**
- ⏳ Update script headers with proper attribution
- ⏳ Add CONTRIBUTORS file if multiple authors

**Status:** 🟢 Minor - generic attribution acceptable for team work

### 4. Random Seed Documentation (LOW PRIORITY)

**Location:** `scripts/analyze_cmb_power_spectrum.py`, line 102

**Issue:** Random seed 42 used without explanation

**Note:** This is actually good practice! Seed 42 is widely used in scientific computing for reproducibility (and as a Hitchhiker's Guide reference).

**Actions:**
- ✅ **Optional**: Add comment explaining seed choice
- ✅ Already reproducible as-is

**Status:** 🟢 Good practice already implemented

---

## Resolved Issues

### ✅ Data Availability
- **Status:** RESOLVED
- All data sources verified as publicly accessible
- Complete bibliography provided
- Download instructions included

### ✅ Analysis Tool Functionality
- **Status:** RESOLVED
- Both scripts tested and working
- Output plots generated successfully
- Documentation complete

### ✅ Scientific Integrity
- **Status:** RESOLVED
- Honest assessment provided
- Limitations acknowledged
- Both supportive and contradictory evidence included

---

## Action Timeline

**Week 1 (Current):**
- ✅ Document all data sources
- ✅ Create working analysis scripts
- ✅ Identify Lamb shift issue
- ✅ Create this action items document

**Week 2-3:**
- ✅ Review Lamb shift derivation in theory documents
- ✅ Determine correct numerical values (formula correct, stated value wrong)
- ✅ Update Appendix W with corrected values
- ✅ Create comprehensive explanation document (LAMB_SHIFT_EXPLANATION.md)

**Month 1-2:**
- ⏳ Implement real data downloads (not simulated)
- ⏳ Add HEPData direct access
- ⏳ Re-run analysis with corrected predictions

**Month 3-6:**
- ⏳ Publish analysis scripts on GitHub
- ⏳ Contact experimental collaborations
- ⏳ Submit analysis to peer review

---

## Priority Levels

✅ **Resolved**: Issue has been addressed  
🟡 **Important**: Should be addressed soon  
🟢 **Minor**: Nice to have, low impact

---

**Document Created:** November 2, 2025  
**Last Updated:** November 2, 2025 (Lamb shift correction completed)  
**Next Review:** After data source improvements (Month 1-2)
