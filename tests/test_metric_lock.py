#!/usr/bin/env python3
"""
Metric Lock Test - Enforce UBT Canonical Axioms

This test ensures that the canonical axioms defined in core/AXIOMS.md are not
violated by accidental redefinition of the emergent metric or fundamental fields.

Author: UBT Team
Date: February 2026
License: MIT
"""

import os
import re
from pathlib import Path
from typing import List, Tuple, Set

try:
    import pytest
    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False
    # Mock pytest for standalone mode
    class pytest:
        @staticmethod
        def skip(msg):
            pass


class MetricLockViolation(Exception):
    """Raised when a metric lock violation is detected"""
    pass


class AxiomEnforcer:
    """Enforces UBT canonical axioms"""
    
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.axioms_file = repo_root / "core" / "AXIOMS.md"
        
    def test_axioms_file_exists(self):
        """Verify core/AXIOMS.md exists"""
        assert self.axioms_file.exists(), (
            f"AXIOMS file not found: {self.axioms_file}\n"
            "The canonical axioms must be documented in core/AXIOMS.md"
        )
    
    def test_axioms_content_complete(self):
        """Verify AXIOMS.md contains required canonical statements"""
        assert self.axioms_file.exists(), "AXIOMS.md must exist"
        
        with open(self.axioms_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for required canonical elements
        required_elements = [
            # Complex time definition
            (r"tau\s*=\s*t\s*\+\s*i.*psi", "Complex time definition τ = t + iψ"),
            
            # Metric definition with key components
            (r"g_\{.*mu.*nu", "Metric tensor g_μν"),
            (r"\\text\{Re\}|Re\\\[|Re\[", "Real part Re[·] in metric"),
            (r"D_.*mu.*Theta", "Covariant derivative D_μΘ in metric"),
            (r"dagger", "Adjoint operation † in metric"),
            
            # Fundamental field
            (r"Theta.*fundamental", "Θ as fundamental field"),
            
            # Lock statements
            (r"LOCK|Lock.*Rule", "Lock rules present"),
            (r"NO.*alternative.*metric|unique.*metric", "No alternative metric rule"),
        ]
        
        missing = []
        for pattern, description in required_elements:
            if not re.search(pattern, content, re.IGNORECASE | re.MULTILINE):
                missing.append(description)
        
        if missing:
            raise AssertionError(
                f"AXIOMS.md is incomplete. Missing required elements:\n" +
                "\n".join(f"  - {item}" for item in missing)
            )
    
    def test_no_forbidden_metric_patterns(self):
        """Scan repository for forbidden metric redefinition patterns"""
        
        # Forbidden patterns that indicate metric lock violations
        forbidden_patterns = [
            (r'\beffective_metric\b', "effective_metric variable"),
            (r'\bbackground_metric\b', "background_metric variable"),
            (r'\bmetric_v2\b', "metric_v2 variable"),
            (r'\bg0_mu_nu\b', "g0_mu_nu (background metric)"),
            (r'\bmetric_hat\b', "metric_hat variable"),
            (r'\bmetric_version_2\b', "metric_version_2"),
            
            # LaTeX patterns (more lenient - might appear in comparisons)
            # Only flag if they appear to be NEW definitions
            (r'\\newcommand.*\\geffective', r"\geffective command definition"),
            (r'\\newcommand.*\\gbackground', r"\gbackground command definition"),
            (r'\\def.*g0.*mu', r"\def for g0 metric"),
        ]
        
        # File patterns to scan
        scan_extensions = {'.py', '.md', '.tex'}
        
        # Directories to exclude
        exclude_dirs = {
            '.git', '__pycache__', 'node_modules', 'build', 'dist', 
            '.pytest_cache', 'vendor', 'venv', '.venv', 'docs/archive'
        }
        
        violations = []
        
        for file_path in self._iter_scannable_files(scan_extensions, exclude_dirs):
            file_violations = self._scan_file(file_path, forbidden_patterns)
            violations.extend(file_violations)
        
        if violations:
            violation_msg = "\n\n" + "="*70 + "\n"
            violation_msg += "METRIC LOCK VIOLATION DETECTED\n"
            violation_msg += "="*70 + "\n\n"
            violation_msg += "The following forbidden patterns were found:\n\n"
            
            for filepath, line_num, pattern_desc, line_content in violations:
                rel_path = filepath.relative_to(self.repo_root)
                violation_msg += f"  {rel_path}:{line_num}\n"
                violation_msg += f"    Pattern: {pattern_desc}\n"
                violation_msg += f"    Line: {line_content.strip()}\n\n"
            
            violation_msg += "These patterns violate UBT Canonical Axiom C (Unique Emergent Metric).\n"
            violation_msg += "See core/AXIOMS.md for details.\n"
            violation_msg += "\n" + "="*70 + "\n"
            
            raise MetricLockViolation(violation_msg)
    
    def _iter_scannable_files(self, extensions: Set[str], exclude_dirs: Set[str]):
        """Iterate over files to scan, excluding certain directories"""
        for root, dirs, files in os.walk(self.repo_root):
            # Modify dirs in-place to skip excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            root_path = Path(root)
            for filename in files:
                file_path = root_path / filename
                
                # Skip the AXIOMS.md file itself (it documents forbidden patterns)
                if file_path == self.axioms_file:
                    continue
                
                # Skip this test file itself (it defines patterns to search for)
                if file_path.name == "test_metric_lock.py":
                    continue
                
                # Skip AXIOMS_METRIC_LOCK_SUMMARY.md (documents forbidden patterns as examples)
                if file_path.name == "AXIOMS_METRIC_LOCK_SUMMARY.md":
                    continue
                
                if file_path.suffix in extensions:
                    yield file_path
    
    def _scan_file(self, filepath: Path, patterns: List[Tuple[str, str]]) -> List[Tuple[Path, int, str, str]]:
        """Scan a single file for forbidden patterns"""
        violations = []
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            for line_num, line in enumerate(lines, start=1):
                # Skip comment-only lines in code files
                line_stripped = line.strip()
                if filepath.suffix == '.py' and line_stripped.startswith('#'):
                    continue
                if filepath.suffix == '.tex':
                    if line_stripped.startswith('%'):
                        # Allow in comments unless it's a definition
                        if not re.search(r'\\newcommand|\\def|\\gdef', line):
                            continue
                    # Allow \label{...effective_metric...} - these are just equation labels
                    if r'\label{' in line and 'effective_metric' in line:
                        continue
                
                # Check each forbidden pattern
                for pattern, description in patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        violations.append((filepath, line_num, description, line))
        
        except (UnicodeDecodeError, PermissionError):
            # Skip files that can't be read
            pass
        
        return violations


# Test functions for pytest
def test_axioms_file_exists():
    """Test that core/AXIOMS.md exists"""
    repo_root = Path(__file__).parent.parent
    enforcer = AxiomEnforcer(repo_root)
    enforcer.test_axioms_file_exists()


def test_axioms_content_complete():
    """Test that AXIOMS.md contains required canonical statements"""
    repo_root = Path(__file__).parent.parent
    enforcer = AxiomEnforcer(repo_root)
    enforcer.test_axioms_content_complete()


def test_no_forbidden_metric_patterns():
    """Test that no forbidden metric redefinition patterns exist"""
    repo_root = Path(__file__).parent.parent
    enforcer = AxiomEnforcer(repo_root)
    enforcer.test_no_forbidden_metric_patterns()


# Standalone execution mode
if __name__ == "__main__":
    """Run as standalone script for manual verification"""
    import sys
    
    repo_root = Path(__file__).parent.parent
    enforcer = AxiomEnforcer(repo_root)
    
    print("="*70)
    print("UBT Metric Lock Test - Standalone Mode")
    print("="*70)
    print()
    
    all_passed = True
    
    # Test 1: Axioms file exists
    print("Test 1: Checking core/AXIOMS.md exists...")
    try:
        enforcer.test_axioms_file_exists()
        print("  ✓ PASS: AXIOMS.md found")
    except AssertionError as e:
        print(f"  ✗ FAIL: {e}")
        all_passed = False
    print()
    
    # Test 2: Axioms content complete
    print("Test 2: Checking AXIOMS.md content...")
    try:
        enforcer.test_axioms_content_complete()
        print("  ✓ PASS: All required canonical elements present")
    except AssertionError as e:
        print(f"  ✗ FAIL: {e}")
        all_passed = False
    print()
    
    # Test 3: No forbidden patterns
    print("Test 3: Scanning repository for forbidden metric patterns...")
    try:
        enforcer.test_no_forbidden_metric_patterns()
        print("  ✓ PASS: No forbidden patterns detected")
    except MetricLockViolation as e:
        print(f"  ✗ FAIL:\n{e}")
        all_passed = False
    print()
    
    print("="*70)
    if all_passed:
        print("✓ ALL TESTS PASSED - Metric lock is secure")
        print("="*70)
        sys.exit(0)
    else:
        print("✗ SOME TESTS FAILED - Metric lock violations detected")
        print("="*70)
        sys.exit(1)
