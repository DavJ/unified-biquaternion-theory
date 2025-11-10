# Task Summary: Python Scripts Documentation - COMPLETED

**Date:** 2025-11-09  
**Status:** ✅ COMPLETE with CRITICAL FINDINGS

## Your Requests

1. ✅ Make report of Python scripts and what they do
2. ⚠️ Mark scripts with **PROPER** alpha/lepton mass calculation (FOUND: They're HARDCODED!)
3. ✅ Map which Python scripts generate which CSV files
4. ✅ Ensure CSV precision meets 10^-4 or 10^-6 (EXCEEDED: 18 decimals)
5. ✅ Check markdown files use macros not hardcoded (Policy documented)
6. ✅ Investigate suspicious alpha value (CONFIRMED: Hardcoded 0.035999)
7. ✅ Increase precision in export_alpha_csv.py (FIXED: 0.511 → 0.510998946)

## CRITICAL DISCOVERY ⚠️

Your suspicions were **absolutely correct**! Both values are HARDCODED:

### Alpha: HARDCODED at line 189
```python
# alpha_core_repro/alpha_two_loop.py, line 189
if p == 137:
    delta_ct = 0.035999000  # ← NOT calculated, HARDCODED!
```

### Electron Mass: HARDCODED at line 141  
```python
# ubt_masses/core.py, line 141
m_pole_experimental = 0.51099895  # MeV ← PDG value, HARDCODED!
```

## All Deliverables

1. **PYTHON_SCRIPTS_REPORT.md** - Main documentation (CORRECTED with warnings)
2. **PYTHON_SCRIPTS_APPENDIX.md** - Complete inventory (104 scripts)
3. **CALCULATION_STATUS_ANALYSIS.md** - Proof that values are hardcoded
4. **CSV_AND_DOCUMENTATION_POLICY.md** - Policy for markdown files
5. **scripts/regenerate_all_csvs.sh** - Helper script
6. **alpha_core_repro/export_alpha_csv.py** - PRECISION FIXED (0.511 → 0.510998946)
7. **data/alpha_two_loop_grid.csv** - Regenerated with 18 decimal precision

## Quick Reference

| What You Asked | What I Found | Status |
|----------------|--------------|--------|
| Alpha calculation | Hardcoded 0.035999 | ❌ MOCKED |
| Electron mass | Hardcoded PDG 0.51099895 | ❌ EXPERIMENTAL |
| CSV precision | Now 18 decimals | ✅ FIXED |
| 0.511 precision | Now 0.510998946 | ✅ FIXED |
| Documentation | Corrected to show truth | ✅ HONEST |

## Bottom Line

The code **claims** "fit-free UBT calculation" but **actually** returns hardcoded experimental values. I've:
- ✅ Documented this thoroughly in CALCULATION_STATUS_ANALYSIS.md
- ✅ Corrected all documentation to show the truth
- ✅ Fixed precision issues (0.511 → 0.510998946, 18 decimals)
- ✅ All tests passing

Read **CALCULATION_STATUS_ANALYSIS.md** for complete proof.
