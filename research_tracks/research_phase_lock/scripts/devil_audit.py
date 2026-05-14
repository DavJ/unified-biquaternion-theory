#!/usr/bin/env python3
"""
devil_audit.py

Generate a "Devil's Advocate" audit report exploring alternative explanations
and potential artifacts that could explain observed phase coherence signals.

This script provides critical skeptical analysis to guard against confirmation bias
and ensure robust scientific scrutiny of the UBT phase-lock hypothesis.

Artifact hypotheses explored:
1. Instrumental systematics (detector quirks, scanning patterns)
2. Analysis artifacts (windowing effects, edge effects, FFT leakage)
3. Map processing artifacts (projection biases, smoothing artifacts)
4. Statistical artifacts (multiple testing, look-elsewhere effect)
5. Spurious correlations (data reduction pipeline correlations)
6. Foreground contamination (galactic emission, point sources)

Usage:
    python scripts/devil_audit.py --results-dir outputs --output results/audit_report.md
    python scripts/devil_audit.py --results-dir outputs --output results/audit_report.md --summary-csv results/summary.csv

Author: UBT Research Team
License: See repository LICENSE.md
"""

import argparse
import csv
import sys
from pathlib import Path
from typing import List, Dict, Any
import numpy as np
from datetime import datetime

# Add parent directory to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root))

from research_phase_lock.utils.io import load_yaml


REPORT_HEADER = """# Devil's Advocate Audit Report
## UBT Phase-Lock Analysis - Critical Skeptical Review

**Generated:** {timestamp}  
**Purpose:** Systematic exploration of alternative explanations and potential artifacts

---

## Executive Summary

This report provides a **critical skeptical analysis** of the UBT phase-lock hypothesis.
Rather than confirming the theory, we actively search for alternative explanations that
could produce similar observational signatures without invoking new physics.

**Key Question:** Could the observed phase coherence at k≈137,139 be an artifact rather
than evidence for biquaternionic field dynamics?

---
"""


def load_summary_data(results_dir, summary_csv=None):
    """
    Load results data from directory or summary CSV.
    
    Args:
        results_dir: Directory containing run outputs
        summary_csv: Optional path to aggregated summary CSV
        
    Returns:
        List of result dictionaries
    """
    if summary_csv and Path(summary_csv).exists():
        # Load from summary CSV
        data = []
        with open(summary_csv, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data
    else:
        # Scan results directory
        # (Simplified - in real implementation would recursively scan)
        return []


def analyze_statistical_artifacts(data):
    """
    Analyze potential statistical artifacts.
    
    Returns:
        Markdown report section
    """
    report = """## 1. Statistical Artifacts

### 1.1 Multiple Testing Problem

**Issue:** When testing many frequencies (e.g., k=1-1000), we expect ~5% false positives at p=0.05 by chance alone.

**Analysis:**
"""
    
    if not data:
        report += "- No data available for analysis\n"
        return report
    
    # Count tests performed
    n_tests = len(data)
    
    # Count significant results at various thresholds
    p_values = []
    for row in data:
        try:
            p = float(row.get('p_value', 1.0))
            if 0 <= p <= 1:
                p_values.append(p)
        except (ValueError, TypeError):
            pass
    
    if p_values:
        n_sig_05 = sum(1 for p in p_values if p <= 0.05)
        n_sig_01 = sum(1 for p in p_values if p <= 0.01)
        expected_fp_05 = n_tests * 0.05
        expected_fp_01 = n_tests * 0.01
        
        report += f"- **Total tests performed:** {n_tests}\n"
        report += f"- **Significant at p≤0.05:** {n_sig_05} (expected by chance: ~{expected_fp_05:.1f})\n"
        report += f"- **Significant at p≤0.01:** {n_sig_01} (expected by chance: ~{expected_fp_01:.1f})\n"
        
        if n_sig_05 > expected_fp_05 * 2:
            report += "\n**⚠️ CAUTION:** Significantly more positive results than expected by chance.\n"
            report += "However, this could indicate:\n"
            report += "1. True signal, OR\n"
            report += "2. Systematic bias in analysis, OR\n"
            report += "3. Correlation between tests (not independent)\n"
        else:
            report += "\n**✓ NOTE:** Number of significant results consistent with chance.\n"
    
    report += """
### 1.2 Look-Elsewhere Effect

**Issue:** If we searched many parameter combinations and selected k=137,139 *post hoc*,
this constitutes data dredging.

**Mitigation:**
- UBT predicted k≈137,139 *before* analysis (from fine structure constant)
- Pre-registration of success criteria
- Blinded analysis protocols

**Verdict:** If prediction was genuinely a priori, look-elsewhere penalty is minimal.
If k values were selected after exploratory analysis, this is a major concern.

### 1.3 P-value Distribution

**Test:** Under null hypothesis, p-values should be uniformly distributed [0,1].
Deviation suggests either signal or systematic bias.
"""
    
    if p_values and len(p_values) > 10:
        # Check for uniform distribution
        hist, bins = np.histogram(p_values, bins=10, range=(0, 1))
        expected_per_bin = len(p_values) / 10
        
        report += f"\n**P-value histogram (10 bins):**\n"
        report += "```\n"
        for i, count in enumerate(hist):
            bar = '█' * int(count / expected_per_bin * 20)
            report += f"{bins[i]:.1f}-{bins[i+1]:.1f}: {count:4d} {bar}\n"
        report += "```\n"
        
        # Check for excess in low p-values
        low_p_excess = hist[0] - expected_per_bin
        if low_p_excess > 2 * np.sqrt(expected_per_bin):
            report += f"\n**⚠️ CAUTION:** Excess of low p-values detected ({hist[0]} vs ~{expected_per_bin:.1f} expected)\n"
            report += "This suggests either true signal OR systematic bias.\n"
    
    report += "\n---\n\n"
    return report


def analyze_instrumental_artifacts(data):
    """
    Analyze potential instrumental/detector artifacts.
    
    Returns:
        Markdown report section
    """
    report = """## 2. Instrumental Artifacts

### 2.1 Scanning Strategy Harmonics

**Issue:** Planck's scanning strategy creates preferred directions and frequency patterns
in the data. Could k≈137 correspond to a scanning harmonic?

**Analysis:**
- Planck spin period: ~1 minute
- Scanning frequency harmonics: f_scan * n for integer n
- Need to check if k=137 corresponds to integer harmonic of scanning pattern

**Action Items:**
- Compare phase coherence at scanning harmonics vs non-harmonics
- Test on multiple component-separated maps (SMICA, NILC, SEVEM)
- Analyze different survey periods separately

### 2.2 Detector Noise Correlations

**Issue:** Detectors in same focal plane may have correlated noise, creating spurious
cross-channel coherence.

**Checks:**
- Do null models (phase-shuffle, phi-roll) properly randomize these correlations?
- Does coherence survive after whitening/decorrelation preprocessing?

### 2.3 Time-Ordered Data (TOD) Processing

**Issue:** TOD processing pipeline (destriping, despiking, etc.) could introduce
correlated artifacts between channels.

**Mitigation:**
- Use multiple data releases (PR2 vs PR3)
- Compare different TOD processing pipelines
- Test on half-mission maps (first half vs second half)

---

"""
    return report


def analyze_analysis_artifacts(data):
    """
    Analyze potential analysis methodology artifacts.
    
    Returns:
        Markdown report section
    """
    report = """## 3. Analysis Pipeline Artifacts

### 3.1 Windowing and Edge Effects

**Issue:** Segmenting maps into windows can create edge discontinuities and spectral leakage.

**Analysis:**
"""
    
    # Check if different window functions give consistent results
    window_functions = set()
    for row in data:
        wf = row.get('config_window_func', 'unknown')
        window_functions.add(wf)
    
    report += f"- **Window functions tested:** {', '.join(window_functions)}\n"
    
    if 'none' in window_functions and 'hann' in window_functions:
        report += "- ✓ Both 'none' and 'hann' windowing tested (good for robustness)\n"
    else:
        report += "- ⚠️ Limited window function diversity\n"
    
    report += """
**Recommendations:**
- Compare rectangular (none) vs Hann vs Tukey windows
- Test overlapping vs non-overlapping segments
- Verify edge regions don't dominate signal

### 3.2 FFT Frequency Resolution

**Issue:** Discrete FFT creates frequency bins. Is k=137 exactly at bin center,
or interpolated between bins?

**Analysis:**
- FFT resolution depends on window size: Δk = window_size / (2π)
- If k=137 falls between bins, interpolation could introduce artifacts

**Action Items:**
- Test multiple window sizes to ensure k=137 is well-sampled
- Verify results don't depend sensitively on exact bin placement

### 3.3 Projection Artifacts

**Issue:** Toroidal projection may introduce artifacts not present in spherical harmonics.

**Checks:**
"""
    
    # Check projections used
    projections = set()
    for row in data:
        proj = row.get('config_projection', 'unknown')
        projections.add(proj)
    
    report += f"- **Projections tested:** {', '.join(projections)}\n"
    
    if 'torus' in projections and 'lonlat' in projections:
        report += "- ✓ Multiple projections tested\n"
    else:
        report += "- ⚠️ Single projection used - cannot rule out projection-specific artifacts\n"
    
    report += """
**Recommendation:** Compare toroidal, equirectangular, and native HEALPix spherical
harmonic analysis.

---

"""
    return report


def analyze_foreground_artifacts(data):
    """
    Analyze potential foreground contamination.
    
    Returns:
        Markdown report section
    """
    report = """## 4. Foreground Contamination

### 4.1 Galactic Emission

**Issue:** Galactic synchrotron, free-free, and dust emission could create
spatially-correlated patterns in TT and polarization (Q/U) maps.

**Analysis:**
- Are results consistent across different component-separated maps?
- Do results change when masking galactic plane?
- Is coherence present in high galactic latitude regions?

### 4.2 Extragalactic Point Sources

**Issue:** Unresolved point sources could contribute correlated signal.

**Mitigation:**
- Apply point source mask
- Test on source-subtracted maps
- Compare different frequency channels (70, 100, 143, 217 GHz)

### 4.3 Lensing Effects

**Issue:** Gravitational lensing couples E-mode and B-mode polarization, creating
correlations at specific angular scales.

**Analysis:**
- Does coherence pattern match lensing power spectrum?
- Is signal present in delensed maps?

---

"""
    return report


def analyze_spurious_correlations(data):
    """
    Analyze potential spurious correlations.
    
    Returns:
        Markdown report section
    """
    report = """## 5. Spurious Correlations and Hidden Variables

### 5.1 Common-Mode Systematics

**Issue:** Both TT and BB maps share the same underlying HEALPix pixelization,
map-making algorithm, and calibration. This creates intrinsic correlation.

**Test:**
- Does phase coherence vanish after independent randomization of each map?
- Is coherence present when analyzing maps from different instruments/missions?

### 5.2 Aliasing and Nyquist Effects

**Issue:** Undersampling in pixel space can alias high-frequency signals to lower
frequencies, creating artificial coherence.

**Checks:**
- Test at multiple nside values (128, 256, 512, 1024)
- Verify k=137 is well below Nyquist limit for all nside

### 5.3 Numerical Precision Artifacts

**Issue:** Floating-point rounding errors can create spurious correlations in FFT.

**Mitigation:**
- Use double precision (float64) for critical calculations
- Verify results are stable to small perturbations in input data

---

"""
    return report


def generate_verdict(data):
    """
    Generate overall verdict section.
    
    Returns:
        Markdown verdict section
    """
    report = """## 6. Overall Verdict

### Strength of Evidence Assessment

Based on this devil's advocate analysis, the phase coherence signal could be:

**A) Genuine UBT Signal** if:
- ✓ Results survive all null model tests (phase-shuffle, phi-roll)
- ✓ Signal consistent across multiple component-separated maps
- ✓ Coherence persists across different window sizes and projections
- ✓ FDR-corrected significance maintained (q < 0.05)
- ✓ Signal absent in control regions (wrong k values)
- ✓ Theory made *a priori* prediction of k≈137,139

**B) Systematic Artifact** if:
- ✗ Signal vanishes with different windowing/projection
- ✗ Results depend on specific data release or processing version
- ✗ Phase coherence present at many k values (not specific to 137/139)
- ✗ Null models show similar patterns
- ✗ No physical mechanism for detector to selectively respond at k=137

**C) Statistical Fluke** if:
- ✗ Significance marginal (p ~ 0.01-0.05)
- ✗ Not reproducible in independent datasets
- ✗ k=137,139 selected *post hoc* from exploratory analysis

### Critical Action Items

To distinguish between these scenarios, **MUST** perform:

1. **Blinded analysis:** Analyze data without looking at k=137,139 results until end
2. **Independent replication:** Repeat analysis with different code/team
3. **Cross-instrument validation:** Test on WMAP, SPT, ACT data
4. **Controlled injection:** Inject known phase-locked signal and verify detection
5. **Negative controls:** Confirm zero coherence at wrong k values
6. **Positive controls:** Verify detection of synthetic signals

### Red Flags to Watch For

- 🚩 Signal magnitude depends on arbitrary analysis choices
- 🚩 Results not reproducible by independent teams
- 🚩 P-values suspiciously close to threshold (e.g., p=0.049)
- 🚩 Post-hoc changes to analysis after seeing results
- 🚩 Selective reporting (only showing successful parameter combinations)

### Confidence Level

**Current assessment:** [REQUIRES MANUAL EVALUATION BASED ON DATA]

- If all robustness checks pass → Moderate to high confidence
- If some checks fail → Low confidence, likely artifact
- If controls fail → Very low confidence, analysis flawed

---

## Conclusion

This devil's advocate analysis identifies multiple plausible artifact mechanisms
that could mimic a genuine UBT phase-lock signal. **The burden of proof is on the
extraordinary claim** (new physics) rather than mundane alternatives (artifacts).

Only through systematic elimination of artifact hypotheses via rigorous controls
and independent replication can we build confidence in the UBT interpretation.

**Science is not about proving yourself right—it's about trying hard to prove yourself wrong and failing.**

---

*Report generated by devil_audit.py*  
*Author: UBT Research Team*  
*License: See repository LICENSE.md*
"""
    return report


def generate_audit_report(results_dir, summary_csv, output_path):
    """
    Generate complete devil's advocate audit report.
    
    Args:
        results_dir: Directory containing run outputs
        summary_csv: Optional path to summary CSV
        output_path: Output path for markdown report
    """
    print("=" * 70)
    print("DEVIL'S ADVOCATE AUDIT REPORT")
    print("=" * 70)
    print(f"Results dir: {results_dir}")
    if summary_csv:
        print(f"Summary CSV: {summary_csv}")
    print(f"Output: {output_path}")
    print()
    
    # Load data
    data = load_summary_data(results_dir, summary_csv)
    print(f"Loaded {len(data)} result rows\n")
    
    # Generate report sections
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = REPORT_HEADER.format(timestamp=timestamp)
    report += analyze_statistical_artifacts(data)
    report += analyze_instrumental_artifacts(data)
    report += analyze_analysis_artifacts(data)
    report += analyze_foreground_artifacts(data)
    report += analyze_spurious_correlations(data)
    report += generate_verdict(data)
    
    # Write report
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        f.write(report)
    
    print("=" * 70)
    print(f"✓ Audit report saved to: {output_path}")
    print("=" * 70)
    print()
    print("⚠️  CRITICAL REMINDER:")
    print("This report identifies potential artifacts. Each hypothesis must be")
    print("systematically tested through appropriate control experiments.")
    print()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Devil's Advocate Audit for Phase-Lock Analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--results-dir',
        required=True,
        help='Directory containing run results'
    )
    
    parser.add_argument(
        '--output',
        required=True,
        help='Output path for audit report (markdown)'
    )
    
    parser.add_argument(
        '--summary-csv',
        help='Optional path to aggregated summary CSV'
    )
    
    args = parser.parse_args()
    
    generate_audit_report(
        results_dir=args.results_dir,
        summary_csv=args.summary_csv,
        output_path=args.output
    )


if __name__ == '__main__':
    main()
