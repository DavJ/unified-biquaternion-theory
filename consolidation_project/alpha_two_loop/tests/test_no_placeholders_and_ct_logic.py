"""
Test suite to ensure no placeholder/pending/1.84 references remain near R_UBT
and to verify clean CT baseline logic is enforced.

This test scans all text files in the repository (excluding speculative extensions)
to ensure that references to R_UBT are consistent with the CT baseline theorem
(R_UBT = 1 under assumptions A1-A3).
"""
import os
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
TEXT_EXT = (".md", ".tex")
# Look for explicit problematic patterns  
# We exclude quotes/escaped uses since those might be disclaimers saying NOT to use 1.84
BAD_PATTERNS = [
    (r"(?<!\\approx\s)(?<!≈\s)(?<![=\"\'])1\.84", "numeric value 1.84 used directly"),
    (r"\bplaceholder\b.*\bR_UBT\b", "placeholder near R_UBT"),
    (r"\bR_UBT\b.*\bplaceholder\b", "R_UBT near placeholder"),
    (r"\bpending\b.*\bR_UBT\b", "pending near R_UBT"),
    (r"\bR_UBT\b.*\bpending\b", "R_UBT near pending"),
]

def scan_text():
    """
    Scan repository for problematic patterns near R_UBT references.
    
    Returns:
        List of tuples (filepath, pattern, description) for violations found
    """
    hits = []
    for p in ROOT.rglob("*"):
        # Skip speculative extensions and non-text files
        if "speculative" in str(p):
            continue
        if p.suffix not in TEXT_EXT:
            continue
        if not p.is_file():
            continue
            
        try:
            txt = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
            
        # Only check files that mention R_UBT or related terms
        if not ("R_UBT" in txt or "R\\_UBT" in txt or "mathcal R" in txt or "mathcal{R}" in txt):
            continue
            
        # Check for problematic patterns
        for pattern, description in BAD_PATTERNS:
            if re.search(pattern, txt, flags=re.IGNORECASE | re.DOTALL):
                hits.append((str(p.relative_to(ROOT)), pattern, description))
    return hits

def test_no_placeholders_for_R_UBT():
    """
    Ensure no placeholder/pending/1.84 references remain in files discussing R_UBT.
    
    This test enforces the fit-free baseline: all references to R_UBT should point
    to the CT baseline theorem (R_UBT = 1 under A1-A3) rather than using placeholder
    values or stating that calculation is pending.
    """
    hits = scan_text()
    
    # Format error message if violations found
    if hits:
        msg_lines = ["Found placeholder/pending/1.84 references near R_UBT:"]
        for filepath, pattern, description in hits:
            msg_lines.append(f"  - {filepath}: {description}")
        msg_lines.append("\nAll references should use CT baseline theorem (Appendix CT):")
        msg_lines.append("  R_UBT = 1 under assumptions A1-A3")
        msg = "\n".join(msg_lines)
        assert False, msg

def test_ct_baseline_value():
    """
    Verify that the CT baseline value is correctly set to 1.
    
    This is a sanity check that the baseline theorem is correctly implemented
    in the codebase.
    """
    # Import the stub function from the ward tests
    import sys
    test_dir = pathlib.Path(__file__).parent
    sys.path.insert(0, str(test_dir))
    
    try:
        from test_ct_ward_and_limits import compute_R_UBT_stub
        
        # Check that baseline equals 1 for various psi values
        for psi in [0.0, 0.1, 0.5, 1.0]:
            R_UBT = compute_R_UBT_stub(psi, mu=1.0)
            assert abs(R_UBT - 1.0) < 1e-12, \
                f"CT baseline should give R_UBT=1, got {R_UBT} for psi={psi}"
    finally:
        sys.path.pop(0)

if __name__ == "__main__":
    # Allow running standalone for debugging
    import pytest
    pytest.main([__file__, "-v"])
