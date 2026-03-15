"""
UBT TeX Invariant Tests
=======================

These tests enforce theory-level invariants to ensure UBT never silently
reverts to classical General Relativity as the fundamental theory.

CRITICAL: These are NOT documentation checks - they are theory constraints
that protect the integrity of the biquaternionic formalism.

The tests ensure:
1. g_{μν} is never treated as fundamental (must be projection of 𝓖_{μν})
2. Biquaternionic objects (𝓖, Ω, 𝓡, 𝓣) remain primary
3. GR appears only as Re(...) / Hermitian projection
4. Required lock-in files exist and contain proper definitions
"""

import os
import re
from pathlib import Path
from typing import List, Tuple, Dict

import pytest

from rules import (
    FORBIDDEN_GR_PHRASES,
    REQUIRED_METRIC_PROJECTIONS,
    REQUIRED_LOCK_IN_FILES,
    check_allowed_context,
    get_line_info,
)


# Repository root
REPO_ROOT = Path(__file__).parent.parent


def find_all_tex_files() -> List[Path]:
    """
    Recursively find all .tex files in the repository.
    
    Returns:
        List of Path objects for .tex files
    """
    # Directory segments to exclude from scan (historical/archived material)
    EXCLUDE_DIRS = {"ARCHIVE", "archive", ".git"}
    tex_files = []
    for tex_file in REPO_ROOT.rglob("*.tex"):
        # Skip hidden directories and common build artifacts
        if any(part.startswith('.') for part in tex_file.parts):
            continue
        # Skip archived material — ARCHIVE/ is historical and excluded from canonical checks
        if any(part in EXCLUDE_DIRS for part in tex_file.parts):
            continue
        tex_files.append(tex_file)
    return tex_files


def read_file_safe(filepath: Path) -> str:
    """
    Safely read a file with UTF-8 encoding, handling errors.
    
    Args:
        filepath: Path to file
        
    Returns:
        File contents as string
    """
    try:
        return filepath.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        # Try with latin-1 as fallback
        return filepath.read_text(encoding='latin-1')


class TestUBTTheoryInvariants:
    """
    Test suite for UBT theory invariants.
    
    These tests enforce that the biquaternionic formalism is maintained
    and GR is always properly contextualized as a projection.
    """
    
    def test_required_lock_in_files_exist(self):
        """
        CRITICAL: Verify that required lock-in files exist.
        
        These files define the fundamental theory and must not be removed.
        """
        missing_files = []
        
        for required_file in REQUIRED_LOCK_IN_FILES:
            file_path = REPO_ROOT / required_file
            if not file_path.exists():
                missing_files.append(required_file)
        
        assert not missing_files, (
            f"CRITICAL: Required lock-in files are missing!\n"
            f"Missing files: {missing_files}\n\n"
            f"These files are MANDATORY for maintaining UBT theory integrity:\n"
            f"  - UBT_Main.tex: Core theory definition\n"
            f"  - THEORY_STATUS_DISCLAIMER.tex: Biquaternionic geometry lock-in\n\n"
            f"Removing these files breaks the fundamental theory structure."
        )
    
    def test_metric_projection_defined(self):
        """
        CRITICAL: Verify that g_{μν} := Re(𝓖_{μν}) is defined somewhere.
        
        The classical metric MUST be explicitly defined as a projection of
        the biquaternionic metric. This is non-negotiable.
        """
        tex_files = find_all_tex_files()
        
        # Search for the required projection definition
        found_definitions = []
        
        for tex_file in tex_files:
            content = read_file_safe(tex_file)
            
            for pattern in REQUIRED_METRIC_PROJECTIONS:
                matches = list(re.finditer(pattern, content, re.IGNORECASE))
                if matches:
                    for match in matches:
                        line_num, line_content = get_line_info(content, match.start())
                        found_definitions.append({
                            'file': tex_file.relative_to(REPO_ROOT),
                            'line': line_num,
                            'content': line_content.strip()
                        })
        
        assert found_definitions, (
            f"CRITICAL: No definition of g_{{μν}} := Re(𝓖_{{μν}}) found!\n\n"
            f"The classical metric g_{{μν}} MUST be explicitly defined as the\n"
            f"real projection of the biquaternionic metric 𝓖_{{μν}}.\n\n"
            f"Expected patterns (at least one must appear):\n"
            + "\n".join(f"  - {p}" for p in REQUIRED_METRIC_PROJECTIONS[:3]) +
            f"\n\nThis definition is MANDATORY to maintain UBT theory integrity."
        )
        
        # Success - log where definitions were found
        print(f"\n✓ Found {len(found_definitions)} metric projection definition(s):")
        for defn in found_definitions[:5]:  # Show first 5
            print(f"  {defn['file']}:{defn['line']}")
    
    def test_no_forbidden_gr_language(self):
        """
        CRITICAL: Verify no forbidden GR language appears without proper context.
        
        Forbidden patterns indicate treating classical GR as fundamental
        instead of as a projection of the biquaternionic theory.
        """
        tex_files = find_all_tex_files()
        violations = []
        
        for tex_file in tex_files:
            content = read_file_safe(tex_file)
            relative_path = tex_file.relative_to(REPO_ROOT)
            
            for pattern, description in FORBIDDEN_GR_PHRASES:
                matches = re.finditer(pattern, content, re.IGNORECASE)
                
                for match in matches:
                    # Check if this match appears in an allowed context
                    if check_allowed_context(content, (match.start(), match.end())):
                        continue  # Allowed - skip
                    
                    line_num, line_content = get_line_info(content, match.start())
                    violations.append({
                        'file': str(relative_path),
                        'line': line_num,
                        'rule': description,
                        'pattern': pattern,
                        'matched_text': match.group(0),
                        'line_content': line_content.strip()
                    })
        
        if violations:
            error_msg = [
                "CRITICAL: Forbidden GR language detected!",
                "",
                "The following violations treat classical GR as fundamental",
                "instead of as a projection of biquaternionic geometry:",
                ""
            ]
            
            for v in violations:
                error_msg.extend([
                    f"File: {v['file']}:{v['line']}",
                    f"Rule: {v['rule']}",
                    f"Matched: {v['matched_text']}",
                    f"Line: {v['line_content']}",
                    ""
                ])
            
            error_msg.extend([
                "FIX: Add proper context showing GR is a projection:",
                "  - Use: 'in the real limit' or 'after projection'",
                "  - Use: 'Re(𝓖_{μν})' when referring to g_{μν}",
                "  - Use: 'recovers Einstein equations' not 'standard Einstein equations'",
                "",
                "Remember: 𝓖_{μν} is fundamental, g_{μν} is derived!"
            ])
            
            pytest.fail("\n".join(error_msg))
    
    def test_lock_in_files_contain_projections(self):
        """
        Verify that lock-in files explicitly define the projection rule.
        
        UBT_Main.tex and THEORY_STATUS_DISCLAIMER.tex must contain
        explicit statements about metric projection.
        """
        for lock_in_file in REQUIRED_LOCK_IN_FILES:
            file_path = REPO_ROOT / lock_in_file
            
            if not file_path.exists():
                continue  # Handled by test_required_lock_in_files_exist
            
            content = read_file_safe(file_path)
            
            # Check for biquaternionic metric mention
            has_biq_metric = bool(re.search(
                r"\\mathcal\{G\}_\{\\mu\\nu\}|biquaternionic\s+metric",
                content,
                re.IGNORECASE
            ))
            
            # Check for projection definition
            has_projection = any(
                re.search(pattern, content, re.IGNORECASE)
                for pattern in REQUIRED_METRIC_PROJECTIONS
            )
            
            assert has_biq_metric or has_projection, (
                f"Lock-in file {lock_in_file} must contain:\n"
                f"  - Reference to biquaternionic metric 𝓖_{{μν}}\n"
                f"  - Projection rule g_{{μν}} := Re(𝓖_{{μν}})\n\n"
                f"This ensures the fundamental theory structure is documented."
            )
    
    def test_no_silent_metric_assumptions(self):
        """
        Detect potential silent assumptions about g_{μν} being fundamental.
        
        This test looks for patterns that might indicate treating the
        classical metric as given without proper biquaternionic foundation.
        """
        tex_files = find_all_tex_files()
        suspicious_patterns = []
        
        # Patterns that might indicate silent assumptions
        warning_patterns = [
            (r"(?<!Re\()(?<!\\text\{Re\}\()g_\{\\mu\\nu\}\s+satisfies", "g_{μν} used without projection context"),
            (r"given\s+(?:the\s+)?metric\s+g_\{\\mu\\nu\}", "Metric g_{μν} treated as 'given'"),
        ]
        
        for tex_file in tex_files:
            content = read_file_safe(tex_file)
            relative_path = tex_file.relative_to(REPO_ROOT)
            
            for pattern, description in warning_patterns:
                matches = re.finditer(pattern, content, re.IGNORECASE)
                
                for match in matches:
                    if check_allowed_context(content, (match.start(), match.end())):
                        continue
                    
                    line_num, line_content = get_line_info(content, match.start())
                    suspicious_patterns.append({
                        'file': str(relative_path),
                        'line': line_num,
                        'warning': description,
                        'matched': match.group(0)
                    })
        
        # This is a warning, not a failure - log suspicious patterns
        if suspicious_patterns:
            print(f"\n⚠ Found {len(suspicious_patterns)} potentially suspicious pattern(s):")
            for sp in suspicious_patterns[:10]:  # Show first 10
                print(f"  {sp['file']}:{sp['line']} - {sp['warning']}")
            print("\nReview these to ensure proper biquaternionic context.")


class TestBiquaternionicPrimacy:
    """
    Tests ensuring biquaternionic objects remain primary.
    
    Verifies that 𝓖, Ω, 𝓡, 𝓣 are treated as fundamental while
    g, Γ, R, T are properly contextualized as projections.
    """
    
    def test_biquaternionic_stress_energy_defined(self):
        """
        Verify that biquaternionic stress-energy 𝓣_{μν} is defined.
        
        The fundamental stress-energy must be biquaternionic, with
        classical T_{μν} as a projection.
        """
        tex_files = find_all_tex_files()
        
        biq_stress_energy_patterns = [
            r"\\mathcal\{T\}_\{\\mu\\nu\}",
            r"biquaternionic\s+stress-energy",
            r"stress.energy.*biquaternion",
        ]
        
        found = False
        for tex_file in tex_files:
            content = read_file_safe(tex_file)
            for pattern in biq_stress_energy_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    found = True
                    break
            if found:
                break
        
        assert found, (
            "Biquaternionic stress-energy 𝓣_{μν} must be defined.\n"
            "Classical T_{μν} should be projection: T_{μν} := Re(𝓣_{μν})"
        )
    
    def test_biquaternionic_curvature_defined(self):
        """
        Verify that biquaternionic curvature 𝓡_{μν} is defined.
        
        Fundamental curvature must be biquaternionic, with
        classical R_{μν} as a projection.
        """
        tex_files = find_all_tex_files()
        
        biq_curvature_patterns = [
            r"\\mathcal\{R\}_\{\\mu\\nu\}",
            r"biquaternionic\s+(?:curvature|Ricci)",
        ]
        
        found = False
        for tex_file in tex_files:
            content = read_file_safe(tex_file)
            for pattern in biq_curvature_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    found = True
                    break
            if found:
                break
        
        assert found, (
            "Biquaternionic curvature 𝓡_{μν} must be defined.\n"
            "Classical R_{μν} should be projection: R_{μν} := Re(𝓡_{μν})"
        )


def test_repository_structure_intact():
    """
    Verify the repository structure supports theory invariants.
    
    This test ensures the basic infrastructure for maintaining
    UBT theory integrity is in place.
    """
    # Check that tests directory exists
    assert (REPO_ROOT / "tests").exists(), "tests/ directory must exist"
    
    # Check that rules.py exists
    assert (REPO_ROOT / "tests" / "rules.py").exists(), "tests/rules.py must exist"
    
    # Check that we can find .tex files
    tex_files = find_all_tex_files()
    assert len(tex_files) > 0, "Repository must contain .tex files"
    
    print(f"\n✓ Repository structure intact: {len(tex_files)} .tex files found")


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v"])
