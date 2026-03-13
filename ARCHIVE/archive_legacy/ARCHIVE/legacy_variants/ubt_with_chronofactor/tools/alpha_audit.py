#!/usr/bin/env python3
"""
Alpha Audit Tool - Repository Scanner
======================================

Scans the UBT repository for occurrences of alpha-related terms and concepts.
This tool helps verify whether UBT rigorously and unambiguously predicts
the fine-structure constant α without fitted parameters.

Author: UBT Team
Version: 1.0
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any


# Key terms to detect (case-insensitive)
DEFAULT_TERMS = [
    r'\balpha\b',
    r'\\alpha\b',
    r'fine-structure',
    r'\b137\b',
    r'1/137',
    r'\bB\s*=',
    r'\bB\s*\(',
    r'R_psi',
    r'Rψ',
    r'R_\\psi',
    r'N_eff',
    r'N_\{\\mathrm\{eff\}\}',
    r'mode\s+count',
    r'\\mathcal\{R\}_\{UBT\}',
    r'two-loop',
    r'\bWard\b',
    r'Thomson\s+limit',
    r'renormalization',
    r'\bfit\b',
    r'assumption',
    r'\bA1\b',
    r'\bA2\b',
    r'\bA3\b',
]


def scan_file(filepath: Path, terms: List[str], context_lines: int = 6) -> List[Dict[str, Any]]:
    """
    Scan a single file for term occurrences.
    
    Args:
        filepath: Path to file to scan
        terms: List of regex patterns to search for
        context_lines: Number of context lines before/after hit
        
    Returns:
        List of hit dictionaries with context
    """
    hits = []
    
    try:
        # Handle different file types
        if filepath.suffix == '.ipynb':
            # Parse Jupyter notebook
            with open(filepath, 'r', encoding='utf-8') as f:
                nb_data = json.load(f)
                
            # Extract source from cells
            lines = []
            for cell in nb_data.get('cells', []):
                source = cell.get('source', [])
                if isinstance(source, list):
                    lines.extend(source)
                else:
                    lines.append(source)
            
            # Add newlines
            content = ''.join(lines)
            lines = content.split('\n')
            
        else:
            # Regular text file
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
        
        # Search for terms
        for lineno, line in enumerate(lines, 1):
            for term in terms:
                if re.search(term, line, re.IGNORECASE):
                    # Extract context
                    start = max(0, lineno - 1 - context_lines)
                    end = min(len(lines), lineno + context_lines)
                    
                    context_before = [lines[i].rstrip('\n') for i in range(start, lineno - 1)]
                    hit_line = line.rstrip('\n')
                    context_after = [lines[i].rstrip('\n') for i in range(lineno, end)]
                    
                    hits.append({
                        'path': str(filepath),
                        'lineno': lineno,
                        'term': term,
                        'context_before': context_before,
                        'hit': hit_line,
                        'context_after': context_after,
                    })
                    break  # Only record one hit per line
    
    except Exception as e:
        print(f"Warning: Could not process {filepath}: {e}")
    
    return hits


def scan_repository(root: Path, terms: List[str], context_lines: int = 6) -> List[Dict[str, Any]]:
    """
    Recursively scan repository for term occurrences.
    
    Args:
        root: Root directory to scan
        terms: List of regex patterns to search for
        context_lines: Number of context lines before/after hit
        
    Returns:
        List of all hits across all files
    """
    all_hits = []
    
    # File extensions to scan
    extensions = {'.tex', '.md', '.ipynb', '.py'}
    
    # Directories to skip
    skip_dirs = {'.git', '__pycache__', 'node_modules', '.pytest_cache', 'venv', 'env'}
    
    for item in root.rglob('*'):
        # Skip directories
        if item.is_dir():
            continue
        
        # Skip files in excluded directories
        if any(skip_dir in item.parts for skip_dir in skip_dirs):
            continue
        
        # Only scan relevant file types
        if item.suffix not in extensions:
            continue
        
        # Scan file
        hits = scan_file(item, terms, context_lines)
        all_hits.extend(hits)
    
    return all_hits


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Scan UBT repository for alpha-related terms',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scan entire repository
  python tools/alpha_audit.py --root . --out reports/alpha_hits.json
  
  # Custom terms
  python tools/alpha_audit.py --terms "alpha" "fine-structure" --context 3
  
  # Scan specific directory
  python tools/alpha_audit.py --root consolidation_project
        """
    )
    
    parser.add_argument('--root', type=str, default='.',
                       help='Root directory to scan (default: .)')
    parser.add_argument('--out', type=str, default='reports/alpha_hits.json',
                       help='Output JSON file (default: reports/alpha_hits.json)')
    parser.add_argument('--context', type=int, default=6,
                       help='Number of context lines (default: 6)')
    parser.add_argument('--terms', nargs='+', type=str, default=None,
                       help='Custom terms to search for (default: predefined list)')
    
    args = parser.parse_args()
    
    # Parse arguments
    root = Path(args.root).resolve()
    out_file = Path(args.out)
    context_lines = args.context
    terms = args.terms if args.terms else DEFAULT_TERMS
    
    print("=" * 70)
    print("UBT Alpha Audit - Repository Scanner")
    print("=" * 70)
    print()
    print(f"Root directory: {root}")
    print(f"Output file: {out_file}")
    print(f"Context lines: {context_lines}")
    print(f"Number of search terms: {len(terms)}")
    print()
    
    # Scan repository
    print("Scanning repository...")
    hits = scan_repository(root, terms, context_lines)
    
    print(f"Found {len(hits)} occurrences across repository")
    print()
    
    # Create output directory if needed
    out_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Write results
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(hits, f, indent=2, ensure_ascii=False)
    
    print(f"Results written to: {out_file}")
    print()
    
    # Summary statistics
    files_with_hits = set(hit['path'] for hit in hits)
    print("Summary:")
    print(f"  Total hits: {len(hits)}")
    print(f"  Files with hits: {len(files_with_hits)}")
    print()
    
    # Top files by hit count
    file_counts = {}
    for hit in hits:
        path = hit['path']
        file_counts[path] = file_counts.get(path, 0) + 1
    
    top_files = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    
    print("Top 10 files by hit count:")
    for path, count in top_files:
        rel_path = Path(path).relative_to(root) if Path(path).is_relative_to(root) else Path(path)
        print(f"  {count:4d}  {rel_path}")
    print()
    
    print("=" * 70)
    print("Scan complete")
    print("=" * 70)


if __name__ == '__main__':
    main()
