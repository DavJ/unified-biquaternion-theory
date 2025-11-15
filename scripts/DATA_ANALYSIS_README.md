# UBT Data Analysis Scripts

This directory contains Python scripts for analyzing experimental data relevant to UBT (Unified Biquaternion Theory) predictions.

## Available Scripts

### 1. `analyze_dark_matter_limits.py`
Analyzes dark matter direct detection experimental limits and compares them with UBT p-adic dark matter predictions.

**UBT Prediction Being Tested:**
- Cross-section: σ_SI = σ₀ × (m_DM / 100 GeV)^(-2)
- Reference: σ₀ = (3.5 ± 1.2) × 10^(-47) cm²
- Source: Appendix W (testable predictions)

**Data Sources:**
- XENON1T (2018) - PRL 121, 111302
- LUX-ZEPLIN (2022) - PRL 131, 041002
- PandaX-4T (2021) - PRL 127, 261802

**Usage:**
```bash
python3 analyze_dark_matter_limits.py
```

**Output:**
- Plot: `ubt_dark_matter_limits.png`
- Console: Testability analysis table

### 2. `analyze_cmb_power_spectrum.py`
Analyzes Cosmic Microwave Background power spectrum data and tests UBT multiverse projection prediction.

**UBT Prediction Being Tested:**
- CMB suppression: C_ℓ^UBT = C_ℓ^ΛCDM × [1 - A_MV × exp(-ℓ / ℓ_decohere)]
- Multiverse amplitude: A_MV = 0.08 ± 0.03
- Decoherence scale: ℓ_decohere = 35 ± 10
- Source: Appendix W (testable predictions)

**Data Sources:**
- Planck 2018 power spectrum (simulated in demo)
- Real data available at: https://pla.esac.esa.int/

**Usage:**
```bash
python3 analyze_cmb_power_spectrum.py
```

**Output:**
- Plot: `ubt_cmb_analysis.png`
- Console: Statistical analysis and χ² comparison

## Installation Requirements

```bash
# Install required Python packages
pip install numpy scipy matplotlib

# Optional for real data analysis:
pip install healpy  # For CMB map analysis
pip install astropy # For cosmological calculations
```

## Data Availability

All scripts demonstrate analysis methods using:
- **Published experimental limits** (publicly available)
- **Simulated data** (for demonstration purposes)

For **production analysis with real data:**

### Gravitational Waves
- LIGO/Virgo GWOSC: https://gwosc.org/
- Install: `pip install gwpy pycbc`

### Gamma-Ray Bursts
- Fermi-LAT Data: https://fermi.gsfc.nasa.gov/ssc/data/
- Install Fermi Science Tools

### Dark Matter
- HEPData repository: https://hepdata.net/
- Experiment websites: XENON, LZ, PandaX

### CMB
- Planck Legacy Archive: https://pla.esac.esa.int/
- Install: `pip install healpy camb`

### Atomic Physics
- NIST Database: https://www.nist.gov/pml/atomic-spectra-database
- CODATA constants: https://physics.nist.gov/cuu/Constants/

## Script Structure

Each script follows this pattern:

1. **Load/Generate Data**: Real or simulated experimental data
2. **Calculate UBT Prediction**: Apply formula from Appendix W
3. **Compare**: Overlay prediction with observations
4. **Statistical Analysis**: χ², significance testing
5. **Visualize**: Generate publication-quality plots
6. **Report**: Console output with interpretation

## Notes and Limitations

### Simulated Data
The current scripts use **simulated data** for demonstration. For scientific publication:
- Download real experimental data
- Use proper likelihood codes
- Account for all systematic uncertainties
- Include full covariance matrices

### Approximate Values
Some experimental limits are digitized from published plots. For precise analysis:
- Use HEPData numerical tables
- Contact experimental collaborations
- Cite original publications

### Statistical Rigor
Production analysis requires:
- Proper treatment of cosmic variance (CMB)
- Systematic error propagation (all experiments)
- Blinding procedures for unbiased analysis
- Peer review of analysis code

## Future Scripts (Planned)

### 3. `analyze_gravitational_waves.py`
Coherent stacking of LIGO/Virgo events to search for phase modulation.

### 4. `analyze_grb_time_delays.py`
Fermi-LAT gamma-ray burst time-of-flight analysis for quantum gravity effects.

### 5. `analyze_lamb_shift.py`
Compilation of precision atomic spectroscopy measurements.

## References

Complete references are available in:
- `../UBT_DATA_ANALYSIS_SCIENTIFIC_SUPPORT.md` - Full data analysis report
- `../consolidation_project/appendix_W_testable_predictions.tex` - UBT predictions
- `../consolidation_project/references.bib` - Bibliography

## Contributing

To add new analysis scripts:
1. Follow the existing script structure
2. Include comprehensive documentation
3. Cite all data sources properly
4. Test with both simulated and real data
5. Add entry to this README

## Contact

For questions about UBT predictions:
- See main repository: https://github.com/DavJ/unified-biquaternion-theory
- Read: `UBT_READING_GUIDE.md`
- Review: `TESTABILITY_AND_FALSIFICATION.md`

## License

These analysis scripts are part of the UBT repository and follow the same license (CC BY-NC-ND 4.0 from v0.4 onwards).
Data sources have their own licenses - consult original publications and data repositories.

---

**Last Updated:** November 2, 2025  
**Status:** Demonstration scripts with simulated data  
**Next Step:** Implement analysis with real experimental data
