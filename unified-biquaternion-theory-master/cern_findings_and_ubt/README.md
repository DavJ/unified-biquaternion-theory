# CERN Findings and UBT Analysis

This directory contains comprehensive documentation and analysis tools for testing Unified Biquaternion Theory (UBT) predictions against recent CERN/LHC experimental results from 2023-2025.

## Main Documents

### Quick Start
- **[CERN_ANALYSIS_QUICKSTART.md](CERN_ANALYSIS_QUICKSTART.md)** - Entry point for understanding latest CERN findings and UBT explanations

### Comprehensive Analysis
- **[CERN_DATA_UBT_ANALYSIS.md](CERN_DATA_UBT_ANALYSIS.md)** - Complete analysis with first-principles derivations
  - 7 BSM phenomena covered
  - 40+ mathematical equations
  - Experimental comparisons
  - Testable predictions

### Implementation
- **[IMPLEMENTATION_SUMMARY_CERN.md](IMPLEMENTATION_SUMMARY_CERN.md)** - Summary of work completed

## Analysis Tools

### Python Script
- **[analyze_cern_ubt_signatures.py](analyze_cern_ubt_signatures.py)** - UBT signature analysis toolkit
  - Mass quantization checker
  - Semi-visible jet calculator
  - SUEP multiplicity predictor
  - Event classification

### Documentation
- **[CERN_ANALYSIS_README.md](CERN_ANALYSIS_README.md)** - Tool documentation and usage guide

## LaTeX Appendix

For inclusion in the main UBT document, see:
- **[../consolidation_project/appendix_CERN_BSM_predictions.tex](../consolidation_project/appendix_CERN_BSM_predictions.tex)**

This LaTeX appendix contains:
- Summary of UBT predictions for all major CERN BSM searches
- Key equations and derivations
- References to experimental results
- Testable predictions and falsification criteria

## Key UBT Predictions

1. **Quantized Mass Spectrum**: M_n = n × m_e (unique to UBT)
2. **Semi-Visible Jets**: Visible fraction f = 1/(1 + e^(Δm/T)) ≈ 0.3-0.7
3. **SUEP**: Track multiplicity N ~ E/Λ_dark
4. **Hidden Valley**: Long-lived particles from ψ-winding
5. **Extra Dimensions**: Fine KK spacing ΔM ~ 0.5 MeV (not TeV)

## Usage

### Quick Start
```bash
# Read the quick start guide
cat CERN_ANALYSIS_QUICKSTART.md

# Run the Python analysis demonstration
python3 analyze_cern_ubt_signatures.py
```

### Detailed Analysis
```python
from analyze_cern_ubt_signatures import UBTSignatureAnalyzer

analyzer = UBTSignatureAnalyzer()

# Check mass quantization
masses = [500, 1000, 2000]  # MeV
uncertainties = [5, 10, 20]  # MeV
results = analyzer.check_mass_quantization(masses, uncertainties)
```

## References

Complete experimental and theoretical references are available in:
- **[../SCIENTIFIC_DATA_SOURCES_BIBLIOGRAPHY.md](../SCIENTIFIC_DATA_SOURCES_BIBLIOGRAPHY.md)** - Section 7: LHC and BSM Searches

## Author

David Jaroš

## Last Updated

November 5, 2025
