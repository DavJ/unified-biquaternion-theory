# UBT CERN Data Analysis Tools

This directory contains tools for analyzing CERN/LHC data for signatures predicted by Unified Biquaternion Theory (UBT).

## Files

### `analyze_cern_ubt_signatures.py`

Python script for analyzing particle physics data for UBT-specific signatures.

**Features:**
- Mass quantization check (M = n × m_e)
- Semi-visible jet fraction calculations
- SUEP (Soft Unclustered Energy Patterns) multiplicity predictions
- Dark photon mass spectrum
- Event classification and analysis

**Requirements:**
```bash
pip install numpy scipy matplotlib
```

**Usage:**
```bash
python3 analyze_cern_ubt_signatures.py
```

**Example Output:**
```
UBT Signature Analysis for CERN/LHC Data
========================================

Example 1: Mass Quantization Check
----------------------------------
Number of consistent masses: 7
Chi-squared: 0.01
P-value: 1.0000

Example 2: Semi-Visible Jet Predictions
---------------------------------------
Δm = 0 MeV → Visible fraction: 0.500
Δm = 100 MeV → Visible fraction: 0.475
...
```

**Integration with Real Data:**

To use with actual LHC data:

1. Download data from CERN Open Data Portal: http://opendata.cern.ch/
2. Extract invariant masses or track information
3. Import the `UBTSignatureAnalyzer` class:

```python
from analyze_cern_ubt_signatures import UBTSignatureAnalyzer

analyzer = UBTSignatureAnalyzer()

# Your measured masses from LHC data
masses = np.array([...])  # in MeV
uncertainties = np.array([...])  # in MeV

# Check for UBT quantization
results = analyzer.check_mass_quantization(masses, uncertainties)

if results['p_value'] > 0.05:
    print("Consistent with UBT mass quantization!")
else:
    print("Not consistent with UBT")
```

## Related Documentation

- **CERN_DATA_UBT_ANALYSIS.md** - Comprehensive analysis of recent CERN findings and UBT explanations
- **SCIENTIFIC_DATA_SOURCES_BIBLIOGRAPHY.md** - References and data sources
- **TESTABILITY_AND_FALSIFICATION.md** - Falsification criteria for UBT

## UBT Predictions Summary

### 1. Quantized Mass Spectrum
**Prediction:** All BSM particles should have masses M_n = n × m_e (to first order)  
**Test:** Search for resonances at exact multiples of electron mass  
**Distinctive:** Different from all other BSM theories

### 2. Semi-Visible Jets
**Prediction:** Visible fraction f_vis = 1/(1 + exp(Δm/T_dark))  
**Test:** Measure visible energy fraction in SVJ events  
**Typical Value:** f_vis ~ 0.3 - 0.7 for Δm ~ 0.5-1 GeV

### 3. SUEP Multiplicity
**Prediction:** N_tracks ~ (E_collision / Λ_dark)  
**Test:** Track multiplicity vs collision energy should be linear  
**Typical Value:** Λ_dark ~ 1 GeV → N ~ 1000 for E ~ 1 TeV

### 4. Dark Photon Spectrum
**Prediction:** M_γ'(n) = n × m_e × [correction factors]  
**Test:** Search for narrow resonances at specific masses  
**Range:** From MeV (n ~ 10) to TeV (n ~ 10⁶)

## Contributing

If you develop additional analysis tools or apply these to real LHC data:

1. Add your scripts to this directory
2. Update this README
3. Document your methods and results
4. Cite the data sources used

## Contact

For questions about UBT predictions or analysis methods, see the main repository documentation.

**Last Updated:** November 5, 2025
