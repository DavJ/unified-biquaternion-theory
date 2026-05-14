#!/usr/bin/env python3
"""
Lint Complex Time Usage in UBT LaTeX Files
===========================================

This script checks that "complex time" usage in LaTeX files either:
1. References the [TRANSITION_CRITERION] tag, OR
2. Appears in explicitly allowed files/sections

Exit code 0 if all checks pass, 1 if violations found.
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple, Set

# Files where complex time is allowed without justification (legacy/intro)
ALLOWED_FILES = {
    "README.md",
    "UBT_READING_GUIDE.md",
    "appendix_B_scalar_imaginary_fields_consolidated.tex",  # Defines the criterion
    "appendix_ALPHA_one_loop_biquat.tex",  # Primary alpha derivation
}

# Patterns that indicate complex time usage
COMPLEX_TIME_PATTERNS = [
    re.compile(r'complex\s+time', re.IGNORECASE),
    re.compile(r'T\s*=\s*t\s*\+\s*i\s*\\?psi', re.IGNORECASE),
    re.compile(r'\\tau\s*=\s*t\s*\+\s*i\s*\\?psi(?!\s*\+)', re.IGNORECASE),  # Not followed by + (biquat)
]

# Pattern for transition criterion reference
CRITERION_REFERENCE_PATTERN = re.compile(
    r'(TRANSITION[_\s]*CRITERION|transition\s+criterion|eq:transition-criterion)',
    re.IGNORECASE
)


def find_tex_and_md_files(root_dir: Path) -> List[Path]:
    """Find all .tex and .md files in the repository, excluding certain directories."""
    excluded_dirs = {'.git', 'build', 'vendor', 'node_modules', '__pycache__', 'old'}
    
    files = []
    for ext in ['*.tex', '*.md']:
        for filepath in root_dir.rglob(ext):
            # Skip if in excluded directory
            if any(excl in filepath.parts for excl in excluded_dirs):
                continue
            files.append(filepath)
    
    return files


def check_file_for_violations(filepath: Path, root_dir: Path) -> List[Tuple[int, str]]:
    """
    Check a single file for complex time usage without proper justification.
    
    Returns:
        List of (line_number, context) tuples for violations
    """
    relative_path = filepath.relative_to(root_dir)
    
    # Check if file is in allowed list
    if relative_path.name in ALLOWED_FILES or str(relative_path) in ALLOWED_FILES:
        return []
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')
    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)
        return []
    
    # Check if file has transition criterion reference
    has_criterion_reference = bool(CRITERION_REFERENCE_PATTERN.search(content))
    
    # If file references the criterion, it's OK
    if has_criterion_reference:
        return []
    
    # Check for complex time mentions
    violations = []
    for line_num, line in enumerate(lines, start=1):
        # Skip comments in LaTeX files
        if filepath.suffix == '.tex':
            stripped = line.strip()
            if stripped.startswith('%'):
                continue
        
        # Check if line contains complex time pattern
        for pattern in COMPLEX_TIME_PATTERNS:
            if pattern.search(line):
                # Found complex time usage without criterion reference
                violations.append((line_num, line.strip()))
                break  # One violation per line is enough
    
    return violations


def main():
    """Main linting function."""
    repo_root = Path(__file__).parent.parent
    
    print("=" * 70)
    print("LINTING COMPLEX TIME USAGE IN UBT REPOSITORY")
    print("=" * 70)
    print()
    print("Checking that 'complex time' usage includes [TRANSITION_CRITERION]")
    print("reference or appears in allowed files...")
    print()
    
    files_to_check = find_tex_and_md_files(repo_root)
    print(f"Scanning {len(files_to_check)} files...")
    print()
    
    total_violations = 0
    files_with_violations = []
    
    for filepath in files_to_check:
        violations = check_file_for_violations(filepath, repo_root)
        
        if violations:
            relative_path = filepath.relative_to(repo_root)
            files_with_violations.append(relative_path)
            total_violations += len(violations)
            
            print(f"❌ {relative_path}")
            for line_num, context in violations:
                # Truncate long lines
                if len(context) > 80:
                    context = context[:77] + "..."
                print(f"   Line {line_num}: {context}")
            print()
    
    # Summary
    print("=" * 70)
    if total_violations == 0:
        print("✅ NO VIOLATIONS FOUND")
        print("=" * 70)
        print()
        print("All uses of 'complex time' either:")
        print("  1. Reference the [TRANSITION_CRITERION], OR")
        print("  2. Appear in allowed files (legacy/definitions)")
        print()
        return 0
    else:
        print(f"❌ FOUND {total_violations} VIOLATIONS IN {len(files_with_violations)} FILES")
        print("=" * 70)
        print()
        print("Files with violations:")
        for filepath in files_with_violations:
            print(f"  - {filepath}")
        print()
        print("To fix: Add reference to [TRANSITION_CRITERION] or")
        print("        add file to ALLOWED_FILES list if justified.")
        print()
        return 1


if __name__ == "__main__":
    sys.exit(main())
