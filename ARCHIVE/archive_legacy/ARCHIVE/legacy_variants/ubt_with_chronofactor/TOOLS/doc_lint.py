#!/usr/bin/env python3
# Copyright (c) 2026 David Jaroš (UBT Framework)
# SPDX-License-Identifier: MIT

"""
Documentation Linter for UBT

Checks for banned phrases that could lead to overclaiming in scientific documentation.
Designed to prevent accidental exaggeration while allowing historical quotes in archives.
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple, Set

# Banned phrases that suggest absolute claims
BANNED_PHRASES = [
    "only theory",
    "exact achieved",
    "guaranteed",
    "proves that",
    "proven that alpha",  # Specific to avoid "proven in Appendix R" false positives
    "exact prediction achieved",
    "confirmed prediction",  # Too strong without qualification
]

# Exceptions: directories where historical claims are allowed
EXCEPTION_DIRS = {
    "docs/archive",
    "original_release_of_ubt",
    "unified-biquaternion-theory-master",
}

# Exception files (old versions kept for history)
EXCEPTION_FILES = {
    "README_OLD.md",
}


def is_exception_path(file_path: Path) -> bool:
    """Check if file is in an exception directory or is an exception file."""
    # Check directory exceptions
    parts = file_path.parts
    for exc_dir in EXCEPTION_DIRS:
        if exc_dir in parts:
            return True
    
    # Check file name exceptions
    if file_path.name in EXCEPTION_FILES:
        return True
    
    return False


def check_file(file_path: Path, banned: List[str]) -> List[Tuple[int, str, str]]:
    """
    Check a file for banned phrases.
    
    Returns:
        List of (line_number, phrase, line_content) for violations
    """
    violations = []
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                line_lower = line.lower()
                
                for phrase in banned:
                    if phrase in line_lower:
                        violations.append((line_num, phrase, line.strip()))
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)
    
    return violations


def lint_documentation(root_dir: Path, patterns: List[str]) -> Tuple[int, int]:
    """
    Lint documentation files for banned phrases.
    
    Args:
        root_dir: Root directory to search
        patterns: File patterns to check (e.g., ['*.md', 'README*'])
        
    Returns:
        (total_files_checked, total_violations)
    """
    files_checked = 0
    total_violations = 0
    
    print("UBT Documentation Linter")
    print("=" * 80)
    print("Checking for banned phrases...")
    print()
    
    for pattern in patterns:
        for file_path in root_dir.rglob(pattern):
            # Skip if in exception directory
            if is_exception_path(file_path):
                continue
            
            # Skip if hidden or build artifact
            if any(part.startswith('.') for part in file_path.parts):
                continue
            
            violations = check_file(file_path, BANNED_PHRASES)
            
            if violations:
                total_violations += len(violations)
                
                print(f"✗ {file_path}")
                for line_num, phrase, line_content in violations:
                    print(f"  Line {line_num}: Found '{phrase}'")
                    print(f"    > {line_content}")
                print()
            
            files_checked += 1
    
    return files_checked, total_violations


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Lint UBT documentation for banned phrases'
    )
    parser.add_argument('--root', type=Path, default=Path('.'),
                        help='Root directory to search (default: current)')
    parser.add_argument('--patterns', nargs='+', 
                        default=['*.md', 'README*'],
                        help='File patterns to check')
    parser.add_argument('--list-banned', action='store_true',
                        help='List banned phrases and exit')
    
    args = parser.parse_args()
    
    if args.list_banned:
        print("Banned phrases:")
        for phrase in BANNED_PHRASES:
            print(f"  - \"{phrase}\"")
        print()
        print("Exceptions (allowed in these directories):")
        for exc_dir in EXCEPTION_DIRS:
            print(f"  - {exc_dir}/")
        return 0
    
    files_checked, violations = lint_documentation(args.root, args.patterns)
    
    print("=" * 80)
    print(f"Files checked: {files_checked}")
    print(f"Violations found: {violations}")
    
    if violations == 0:
        print("✓ All checks passed")
        return 0
    else:
        print("✗ Violations found - please revise wording")
        print()
        print("Suggestions:")
        print("  - Replace 'only theory' with 'among the few theories' or remove claim")
        print("  - Replace 'exact achieved' with 'matches within X%'")
        print("  - Replace 'guaranteed' with 'expected' or 'predicted'")
        print("  - Replace 'proves' with 'indicates' or 'suggests'")
        return 1


if __name__ == '__main__':
    sys.exit(main())
