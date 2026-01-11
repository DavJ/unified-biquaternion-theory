#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - Run Summary Tool
============================================

Generates a summary table of CMB comb test runs for quick inspection and comparison.

This tool reads run directories (containing JSON results files) and generates a
formatted table showing:
- Timestamp
- Dataset (Planck/WMAP)
- P-value
- Best period
- Phases
- Whitening mode
- ℓ-ranges
- Verdict (PASS/FAIL/CANDIDATE)
- Completion status

Usage Examples
--------------

# Summarize all runs in default output directory:
python tools/forensic/print_run_summary.py

# Summarize specific directory:
python tools/forensic/print_run_summary.py forensic_fingerprint/out/real_runs

# Summarize with glob pattern:
python tools/forensic/print_run_summary.py "forensic_fingerprint/out/real_runs/cmb_comb_2026*"

# Show last N runs only:
python tools/forensic/print_run_summary.py --last 10

# Output as CSV:
python tools/forensic/print_run_summary.py --format csv --output runs_summary.csv

# Output as JSON:
python tools/forensic/print_run_summary.py --format json --output runs_summary.json

License: MIT
Author: UBT Research Team
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
import glob as glob_module

def find_repo_root(start_path=None):
    """
    Find repository root by walking upward.
    
    Parameters
    ----------
    start_path : Path or None
        Starting directory (default: script location)
    
    Returns
    -------
    Path
        Repository root directory
    """
    if start_path is None:
        start_path = Path(__file__).resolve().parent
    else:
        start_path = Path(start_path).resolve()
    
    current = start_path
    markers = ['.git', 'pyproject.toml', 'pytest.ini']
    
    while current != current.parent:
        for marker in markers:
            if (current / marker).exists():
                return current
        current = current.parent
    
    for marker in markers:
        if (current / marker).exists():
            return current
    
    raise FileNotFoundError(
        f"Could not find repository root from {start_path}"
    )


def parse_run_directory(run_dir):
    """
    Parse a single run directory and extract summary information.
    
    Parameters
    ----------
    run_dir : Path
        Path to run directory
    
    Returns
    -------
    dict or None
        Run summary dict, or None if parsing failed
    """
    run_dir = Path(run_dir)
    
    if not run_dir.is_dir():
        return None
    
    summary = {
        'path': str(run_dir),
        'name': run_dir.name,
        'timestamp': None,
        'planck_p': None,
        'planck_period': None,
        'planck_phase': None,
        'planck_ell_range': None,
        'planck_whitening': None,
        'wmap_p': None,
        'wmap_period': None,
        'wmap_phase': None,
        'wmap_ell_range': None,
        'wmap_whitening': None,
        'verdict': None,
        'complete': False,
        'incomplete_reason': []
    }
    
    # Extract timestamp from directory name if possible
    # Expected format: cmb_comb_YYYYMMDD_HHMMSS
    try:
        parts = run_dir.name.split('_')
        if len(parts) >= 4:
            date_str = parts[-2]  # YYYYMMDD
            time_str = parts[-1]  # HHMMSS
            timestamp_str = f"{date_str}_{time_str}"
            summary['timestamp'] = datetime.strptime(timestamp_str, '%Y%m%d_%H%M%S')
    except (ValueError, IndexError):
        # If timestamp extraction fails, use directory modification time
        summary['timestamp'] = datetime.fromtimestamp(run_dir.stat().st_mtime)
    
    # Check for Planck results
    planck_json = run_dir / 'planck_results.json'
    if planck_json.exists():
        try:
            with open(planck_json, 'r') as f:
                planck_data = json.load(f)
            
            summary['planck_p'] = planck_data.get('p_value')
            summary['planck_period'] = planck_data.get('best_period')
            summary['planck_phase'] = planck_data.get('phase')
            
            ell = planck_data.get('ell', [])
            if ell:
                summary['planck_ell_range'] = (min(ell), max(ell))
            
            summary['planck_whitening'] = planck_data.get('whiten_mode', 'unknown')
        except (json.JSONDecodeError, KeyError) as e:
            summary['incomplete_reason'].append(f"Planck JSON error: {e}")
    else:
        summary['incomplete_reason'].append("Missing planck_results.json")
    
    # Check for WMAP results
    wmap_json = run_dir / 'wmap_results.json'
    if wmap_json.exists():
        try:
            with open(wmap_json, 'r') as f:
                wmap_data = json.load(f)
            
            summary['wmap_p'] = wmap_data.get('p_value')
            summary['wmap_period'] = wmap_data.get('best_period')
            summary['wmap_phase'] = wmap_data.get('phase')
            
            ell = wmap_data.get('ell', [])
            if ell:
                summary['wmap_ell_range'] = (min(ell), max(ell))
            
            summary['wmap_whitening'] = wmap_data.get('whiten_mode', 'unknown')
        except (json.JSONDecodeError, KeyError) as e:
            summary['incomplete_reason'].append(f"WMAP JSON error: {e}")
    # WMAP is optional, so don't mark as incomplete if missing
    
    # Check for combined verdict
    verdict_md = run_dir / 'combined_verdict.md'
    if verdict_md.exists():
        try:
            with open(verdict_md, 'r') as f:
                content = f.read()
            
            # Extract verdict from markdown
            if '✓ **PASS**' in content:
                summary['verdict'] = 'PASS'
            elif '✗ **FAIL**' in content:
                summary['verdict'] = 'FAIL'
            elif 'INCOMPLETE' in content:
                summary['verdict'] = 'INCOMPLETE'
            elif 'CANDIDATE' in content:
                summary['verdict'] = 'CANDIDATE'
            else:
                summary['verdict'] = 'UNKNOWN'
        except Exception as e:
            summary['incomplete_reason'].append(f"Verdict MD error: {e}")
    else:
        summary['incomplete_reason'].append("Missing combined_verdict.md")
    
    # Mark as complete if no critical issues
    summary['complete'] = len(summary['incomplete_reason']) == 0 or \
                         all('WMAP' in reason for reason in summary['incomplete_reason'])
    
    return summary


def collect_runs(search_path=None, pattern=None):
    """
    Collect all run directories from search path.
    
    Parameters
    ----------
    search_path : str or Path or None
        Base path to search (default: forensic_fingerprint/out/real_runs)
    pattern : str or None
        Glob pattern for run directories (default: all subdirectories)
    
    Returns
    -------
    list of dict
        List of run summaries, sorted by timestamp (newest first)
    """
    repo_root = find_repo_root()
    
    if search_path is None:
        search_path = repo_root / 'forensic_fingerprint' / 'out' / 'real_runs'
    else:
        search_path = Path(search_path)
        if not search_path.is_absolute():
            search_path = repo_root / search_path
    
    # Handle glob patterns
    if pattern:
        # Pattern provided: use glob
        if not Path(pattern).is_absolute():
            pattern_path = repo_root / pattern
        else:
            pattern_path = Path(pattern)
        
        run_dirs = sorted(glob_module.glob(str(pattern_path)), reverse=True)
        run_dirs = [Path(d) for d in run_dirs if Path(d).is_dir()]
    else:
        # No pattern: collect all subdirectories
        if not search_path.exists():
            print(f"WARNING: Search path does not exist: {search_path}")
            return []
        
        run_dirs = [d for d in search_path.iterdir() if d.is_dir()]
    
    # Parse each run directory
    summaries = []
    for run_dir in run_dirs:
        summary = parse_run_directory(run_dir)
        if summary:
            summaries.append(summary)
    
    # Sort by timestamp (newest first)
    summaries.sort(key=lambda x: x['timestamp'] if x['timestamp'] else datetime.min, reverse=True)
    
    return summaries


def format_table(summaries, max_rows=None):
    """
    Format summaries as a text table.
    
    Parameters
    ----------
    summaries : list of dict
        Run summaries
    max_rows : int or None
        Maximum number of rows to display (None = all)
    
    Returns
    -------
    str
        Formatted table
    """
    if max_rows:
        summaries = summaries[:max_rows]
    
    if not summaries:
        return "No runs found.\n"
    
    lines = []
    lines.append("="*160)
    lines.append("CMB COMB TEST RUN SUMMARY")
    lines.append("="*160)
    lines.append("")
    
    # Header
    header = (
        f"{'Timestamp':<20} "
        f"{'Run Name':<30} "
        f"{'Planck p':<12} "
        f"{'Period':<8} "
        f"{'Phase(°)':<9} "
        f"{'ℓ-range':<15} "
        f"{'Whiten':<10} "
        f"{'WMAP p':<12} "
        f"{'Period':<8} "
        f"{'Verdict':<12} "
        f"{'Status':<10}"
    )
    lines.append(header)
    lines.append("-"*160)
    
    # Rows
    for s in summaries:
        timestamp_str = s['timestamp'].strftime('%Y-%m-%d %H:%M:%S') if s['timestamp'] else 'N/A'
        run_name = s['name'][:28] + '..' if len(s['name']) > 30 else s['name']
        
        # Planck columns
        planck_p_str = f"{s['planck_p']:.2e}" if s['planck_p'] is not None else 'N/A'
        planck_period_str = str(s['planck_period']) if s['planck_period'] is not None else 'N/A'
        planck_phase_deg = (s['planck_phase'] * 180 / 3.14159) if s['planck_phase'] is not None else None
        planck_phase_str = f"{planck_phase_deg:.1f}" if planck_phase_deg is not None else 'N/A'
        planck_ell_str = f"{s['planck_ell_range'][0]}-{s['planck_ell_range'][1]}" if s['planck_ell_range'] else 'N/A'
        planck_whiten_str = (s['planck_whitening'] or 'N/A')[:8]
        
        # WMAP columns
        wmap_p_str = f"{s['wmap_p']:.2e}" if s['wmap_p'] is not None else 'N/A'
        wmap_period_str = str(s['wmap_period']) if s['wmap_period'] is not None else 'N/A'
        
        # Verdict
        verdict_str = s['verdict'] or 'N/A'
        
        # Status
        if s['complete']:
            status_str = '✓ Complete'
        else:
            status_str = '⚠ Incomplete'
        
        row = (
            f"{timestamp_str:<20} "
            f"{run_name:<30} "
            f"{planck_p_str:<12} "
            f"{planck_period_str:<8} "
            f"{planck_phase_str:<9} "
            f"{planck_ell_str:<15} "
            f"{planck_whiten_str:<10} "
            f"{wmap_p_str:<12} "
            f"{wmap_period_str:<8} "
            f"{verdict_str:<12} "
            f"{status_str:<10}"
        )
        lines.append(row)
        
        # Show incomplete reasons if any
        if not s['complete'] and s['incomplete_reason']:
            for reason in s['incomplete_reason']:
                if 'WMAP' not in reason:  # Only show non-WMAP issues
                    lines.append(f"    └─ {reason}")
    
    lines.append("="*160)
    lines.append(f"\nTotal runs: {len(summaries)}")
    
    # Legend
    lines.append("\nLegend:")
    lines.append("  Period: Best-fit Δℓ from candidate set [8, 16, 32, 64, 128, 255]")
    lines.append("  Phase: Best-fit φ in degrees [0°-360°]")
    lines.append("  Whiten: Whitening mode (none/diagonal/cov_diag/covariance/diag/full)")
    lines.append("  Verdict: PASS/FAIL/CANDIDATE/INCOMPLETE/UNKNOWN")
    lines.append("  Status: ✓ Complete (all required files present) / ⚠ Incomplete (missing files)")
    
    return '\n'.join(lines)


def format_csv(summaries, max_rows=None):
    """
    Format summaries as CSV.
    
    Parameters
    ----------
    summaries : list of dict
        Run summaries
    max_rows : int or None
        Maximum number of rows
    
    Returns
    -------
    str
        CSV formatted string
    """
    if max_rows:
        summaries = summaries[:max_rows]
    
    if not summaries:
        return "timestamp,run_name,planck_p,planck_period,planck_phase_deg,planck_ell_min,planck_ell_max,planck_whitening,wmap_p,wmap_period,wmap_phase_deg,wmap_ell_min,wmap_ell_max,wmap_whitening,verdict,complete,incomplete_reason\n"
    
    lines = []
    
    # Header
    lines.append(
        "timestamp,run_name,planck_p,planck_period,planck_phase_deg,planck_ell_min,planck_ell_max,planck_whitening,"
        "wmap_p,wmap_period,wmap_phase_deg,wmap_ell_min,wmap_ell_max,wmap_whitening,verdict,complete,incomplete_reason"
    )
    
    # Rows
    for s in summaries:
        timestamp_str = s['timestamp'].isoformat() if s['timestamp'] else ''
        
        planck_phase_deg = (s['planck_phase'] * 180 / 3.14159) if s['planck_phase'] is not None else ''
        wmap_phase_deg = (s['wmap_phase'] * 180 / 3.14159) if s['wmap_phase'] is not None else ''
        
        planck_ell_min = s['planck_ell_range'][0] if s['planck_ell_range'] else ''
        planck_ell_max = s['planck_ell_range'][1] if s['planck_ell_range'] else ''
        wmap_ell_min = s['wmap_ell_range'][0] if s['wmap_ell_range'] else ''
        wmap_ell_max = s['wmap_ell_range'][1] if s['wmap_ell_range'] else ''
        
        incomplete_reason = '; '.join(s['incomplete_reason'])
        
        row = (
            f"{timestamp_str},"
            f"{s['name']},"
            f"{s['planck_p'] if s['planck_p'] is not None else ''},"
            f"{s['planck_period'] if s['planck_period'] is not None else ''},"
            f"{planck_phase_deg},"
            f"{planck_ell_min},{planck_ell_max},"
            f"{s['planck_whitening'] or ''},"
            f"{s['wmap_p'] if s['wmap_p'] is not None else ''},"
            f"{s['wmap_period'] if s['wmap_period'] is not None else ''},"
            f"{wmap_phase_deg},"
            f"{wmap_ell_min},{wmap_ell_max},"
            f"{s['wmap_whitening'] or ''},"
            f"{s['verdict'] or ''},"
            f"{s['complete']},"
            f"\"{incomplete_reason}\""
        )
        lines.append(row)
    
    return '\n'.join(lines)


def format_json(summaries, max_rows=None):
    """
    Format summaries as JSON.
    
    Parameters
    ----------
    summaries : list of dict
        Run summaries
    max_rows : int or None
        Maximum number of rows
    
    Returns
    -------
    str
        JSON formatted string
    """
    if max_rows:
        summaries = summaries[:max_rows]
    
    # Convert datetime objects to ISO format for JSON serialization
    summaries_json = []
    for s in summaries:
        s_copy = s.copy()
        if s_copy['timestamp']:
            s_copy['timestamp'] = s_copy['timestamp'].isoformat()
        summaries_json.append(s_copy)
    
    return json.dumps(summaries_json, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description="Generate summary table of CMB comb test runs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Summarize all runs in default directory:
  python print_run_summary.py

  # Summarize specific directory:
  python print_run_summary.py forensic_fingerprint/out/real_runs

  # With glob pattern:
  python print_run_summary.py "forensic_fingerprint/out/real_runs/cmb_comb_2026*"

  # Last 10 runs only:
  python print_run_summary.py --last 10

  # Output as CSV:
  python print_run_summary.py --format csv --output runs.csv
        """
    )
    
    parser.add_argument(
        'path',
        nargs='?',
        default=None,
        help='Path to run directory or glob pattern (default: forensic_fingerprint/out/real_runs)'
    )
    
    parser.add_argument(
        '--last',
        type=int,
        default=None,
        help='Show only the last N runs (default: all)'
    )
    
    parser.add_argument(
        '--format',
        choices=['table', 'csv', 'json'],
        default='table',
        help='Output format (default: table)'
    )
    
    parser.add_argument(
        '--output',
        '-o',
        type=str,
        default=None,
        help='Output file (default: stdout)'
    )
    
    args = parser.parse_args()
    
    # Collect runs
    if args.path and ('*' in args.path or '?' in args.path):
        # Glob pattern provided
        summaries = collect_runs(pattern=args.path)
    else:
        # Directory path provided (or default)
        summaries = collect_runs(search_path=args.path)
    
    # Format output
    if args.format == 'table':
        output = format_table(summaries, max_rows=args.last)
    elif args.format == 'csv':
        output = format_csv(summaries, max_rows=args.last)
    elif args.format == 'json':
        output = format_json(summaries, max_rows=args.last)
    else:
        output = format_table(summaries, max_rows=args.last)
    
    # Write output
    if args.output:
        output_path = Path(args.output)
        with open(output_path, 'w') as f:
            f.write(output)
        print(f"Summary written to: {output_path}")
    else:
        print(output)


if __name__ == '__main__':
    main()
