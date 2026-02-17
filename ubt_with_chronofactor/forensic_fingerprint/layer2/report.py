"""
Layer 2 Fingerprint - Report Generation

This module generates outputs from Layer 2 fingerprint sweeps.

Output formats:
---------------
- CSV: All sampled configurations with scores
- JSON: Machine-readable summary statistics
- Markdown: Human-readable report with interpretation

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

from .config_space import Layer2Config
from .metrics import compute_rarity_bits


def write_csv(results: List[Dict[str, Any]], path: Path):
    """
    Write configurations and scores to CSV.
    
    Parameters
    ----------
    results : List[Dict[str, Any]]
        List of result dictionaries
    path : Path
        Output CSV file path
    """
    if not results:
        return
    
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        for result in results:
            writer.writerow(result)


def write_summary_json(summary: Dict[str, Any], path: Path):
    """
    Write summary statistics to JSON.
    
    Parameters
    ----------
    summary : Dict[str, Any]
        Summary statistics dictionary
    path : Path
        Output JSON file path
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Convert numpy types to native Python types
    def convert_types(obj):
        """Recursively convert numpy types."""
        if isinstance(obj, dict):
            return {k: convert_types(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [convert_types(item) for item in obj]
        elif hasattr(obj, 'item'):  # numpy scalar
            return obj.item()
        elif isinstance(obj, (int, float, str, bool, type(None))):
            return obj
        else:
            return str(obj)
    
    summary_native = convert_types(summary)
    
    with open(path, 'w') as f:
        json.dump(summary_native, f, indent=2)


def write_report_md(summary: Dict[str, Any], path: Path, mapping_mode: str):
    """
    Write human-readable Markdown report.
    
    Parameters
    ----------
    summary : Dict[str, Any]
        Summary statistics dictionary
    path : Path
        Output Markdown file path
    mapping_mode : str
        Mapping mode used ('placeholder' or 'ubt')
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w') as f:
        # Header
        f.write("# Layer 2 Fingerprint Sweep Results\n")
        f.write("=" * 80 + "\n\n")
        
        # Warning if placeholder
        if mapping_mode == 'placeholder':
            f.write("⚠️ **WARNING: PLACEHOLDER PHYSICS MAPPING**\n")
            f.write("=" * 80 + "\n")
            f.write("This sweep uses PLACEHOLDER toy model formulas.\n")
            f.write("Results are NOT physically interpretable.\n")
            f.write("Framework demonstration only.\n")
            f.write("=" * 80 + "\n\n")
        
        # Metadata
        f.write(f"**Configuration Space**: {summary['space_type']}\n")
        f.write(f"**Number of Samples**: {summary['n_samples']}\n")
        f.write(f"**Random Seed**: {summary['seed']}\n")
        f.write(f"**Mapping Mode**: {mapping_mode}\n")
        f.write(f"**Timestamp**: {datetime.now().isoformat()}\n\n")
        
        # Best configuration
        f.write("## Best Configuration Found\n")
        f.write("-" * 80 + "\n")
        best = summary.get('best_config', {})
        f.write(f"  **Combined Score**: {summary.get('best_score', 'N/A'):.6f}\n")
        if 'best_predictions' in summary:
            for obs, val in summary['best_predictions'].items():
                f.write(f"  **{obs}**: {val:.6f}\n")
        f.write(f"  **RS(n,k)**: ({best.get('rs_n', 'N/A')}, {best.get('rs_k', 'N/A')})\n")
        f.write(f"  **OFDM Channels**: {best.get('ofdm_channels', 'N/A')}\n")
        f.write(f"  **Winding Number**: {best.get('winding_number', 'N/A')}\n")
        f.write(f"  **Quantization Grid**: {best.get('quantization_grid', 'N/A')}\n\n")
        
        # Statistical summary
        f.write("## Statistical Summary\n")
        f.write("-" * 80 + "\n")
        stats = summary.get('score_statistics', {})
        f.write(f"  **Mean Score**: {stats.get('mean', 0):.6f}\n")
        f.write(f"  **Median Score**: {stats.get('median', 0):.6f}\n")
        f.write(f"  **Std Dev Score**: {stats.get('std', 0):.6f}\n\n")
        
        # Hit statistics
        f.write("## Match Statistics (Hit-Rate Analysis)\n")
        f.write("-" * 80 + "\n")
        n_hits = summary.get('n_hits', 0)
        n_total = summary.get('n_samples', 1)
        hit_rate = summary.get('hit_rate', 0.0)
        rarity_bits = summary.get('rarity_bits', float('inf'))
        
        f.write(f"  **Configurations matching all observables**: {n_hits} out of {n_total}\n")
        f.write(f"  **Hit-rate**: {hit_rate:.4f} ({hit_rate*100:.2f}%)\n")
        
        if rarity_bits != float('inf'):
            f.write(f"  **Rarity**: {rarity_bits:.2f} bits\n")
        else:
            f.write(f"  **Rarity**: infinite (no hits)\n")
        
        f.write("\n")
        
        # Interpretation
        f.write("## Rigidity Assessment\n")
        f.write("-" * 80 + "\n")
        
        if mapping_mode == 'placeholder':
            f.write("⚠️ **PLACEHOLDER MODE**: Rigidity assessment not valid.\n")
            f.write("Framework demonstration only - no physical interpretation.\n\n")
        else:
            if hit_rate < 0.01:
                f.write("**High rigidity** - Matching configurations are rare (<1%)\n")
                f.write("Layer 2 appears highly constrained.\n\n")
            elif hit_rate < 0.05:
                f.write("**Moderate rigidity** - Matching configurations uncommon (1-5%)\n")
                f.write("Some freedom in Layer 2 choices.\n\n")
            else:
                f.write("**Low rigidity** - Matching configurations common (≥5%)\n")
                f.write("Layer 2 has significant freedom.\n\n")
        
        # Current configuration analysis
        if 'current_config_rank' in summary:
            f.write("## Current UBT Configuration Analysis\n")
            f.write("-" * 80 + "\n")
            f.write(f"  **Score**: {summary.get('current_config_score', 'N/A'):.6f}\n")
            f.write(f"  **Rank**: {summary.get('current_config_rank', 'N/A')}/{n_total}\n")
            f.write(f"  **Percentile**: {summary.get('current_config_percentile', 0):.2f}%\n\n")
            
            percentile = summary.get('current_config_percentile', 50)
            if percentile < 1.0:
                f.write("**Top 1%** - Current config is exceptional.\n")
            elif percentile < 10.0:
                f.write("**Top 10%** - Current config is good.\n")
            elif percentile < 50.0:
                f.write("**Above median** - Current config is moderate.\n")
            else:
                f.write("**Below median** - Current config may need review.\n")


def write_verdict_md(
    summary: Dict[str, Any], 
    path: Path, 
    mapping_mode: str,
    robustness_results: Dict[float, Dict] = None
):
    """
    Write VERDICT.md with hit-rate analysis and robustness assessment.
    
    Parameters
    ----------
    summary : Dict[str, Any]
        Summary statistics dictionary (for baseline run if robustness enabled)
    path : Path
        Output VERDICT.md file path
    mapping_mode : str
        Mapping mode used ('placeholder' or 'ubt')
    robustness_results : Dict[float, Dict], optional
        Results from robustness runs: {range_scale: summary_dict}
        If None, only baseline analysis is included
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w') as f:
        # Header
        f.write("# Layer2 Fingerprint Rigidity Verdict\n\n")
        
        # Metadata
        f.write(f"**Protocol Version**: 1.0\n")
        f.write(f"**Mapping Mode**: {mapping_mode}\n")
        f.write(f"**Space Type**: {summary['space_type']}\n")
        f.write(f"**Sample Size**: {summary['n_samples']}\n")
        f.write(f"**Random Seed**: {summary['seed']}\n")
        f.write(f"**Timestamp**: {datetime.now().isoformat()}\n\n")
        
        f.write("---\n\n")
        
        # Warning if placeholder
        if mapping_mode == 'placeholder':
            f.write("⚠️ **WARNING: PLACEHOLDER PHYSICS MAPPING**\n")
            f.write("=" * 70 + "\n")
            f.write("This analysis uses PLACEHOLDER toy model formulas.\n")
            f.write("Results have NO scientific interpretation.\n")
            f.write("Framework demonstration only.\n")
            f.write("=" * 70 + "\n\n")
        
        # Hit-Rate Analysis
        f.write("## Hit-Rate Analysis\n\n")
        n_hits = summary['n_hits']
        n_total = summary['n_samples']
        hit_rate = summary['hit_rate']
        rarity_bits = summary['rarity_bits']
        
        f.write(f"- **Hits**: {n_hits} / {n_total}\n")
        f.write(f"- **Hit-Rate**: {hit_rate:.6f} ({hit_rate*100:.4f}%)\n")
        
        if rarity_bits != float('inf'):
            f.write(f"- **Rarity**: {rarity_bits:.2f} bits\n")
        else:
            f.write(f"- **Rarity**: ∞ (infinite - no hits found)\n")
        
        f.write("\n")
        
        # Robustness Analysis (if available)
        if robustness_results is not None and len(robustness_results) > 1:
            f.write("## Robustness Analysis\n\n")
            f.write("| Range Scale | Hit-Rate | Rarity (bits) | Ratio to Baseline |\n")
            f.write("|-------------|----------|---------------|-------------------|\n")
            
            # Ensure we have baseline (scale=1.0)
            baseline_hit_rate = robustness_results.get(1.0, summary)['hit_rate']
            
            for scale in sorted(robustness_results.keys()):
                res = robustness_results[scale]
                scale_hit_rate = res['hit_rate']
                scale_rarity = res['rarity_bits']
                
                if baseline_hit_rate > 0:
                    ratio = scale_hit_rate / baseline_hit_rate
                else:
                    ratio = float('nan')
                
                if scale_rarity != float('inf'):
                    rarity_str = f"{scale_rarity:.2f}"
                else:
                    rarity_str = "∞"
                
                f.write(f"| {scale:.1f} | {scale_hit_rate:.6f} | {rarity_str} | {ratio:.2f} |\n")
            
            f.write("\n")
            
            # Assess robustness
            f.write("### Robustness Assessment\n\n")
            
            # Check if hit-rates stay within [1/3, 3] of baseline
            if baseline_hit_rate > 0:
                ratios = []
                for scale in robustness_results.keys():
                    if scale != 1.0:
                        scale_rate = robustness_results[scale]['hit_rate']
                        if baseline_hit_rate > 0:
                            ratios.append(scale_rate / baseline_hit_rate)
                
                if ratios:
                    min_ratio = min(ratios)
                    max_ratio = max(ratios)
                    
                    is_robust = (min_ratio >= 1/3) and (max_ratio <= 3)
                    
                    f.write(f"**Ratio Range**: [{min_ratio:.2f}, {max_ratio:.2f}]\n")
                    f.write(f"**Criterion**: Ratios should stay in [0.33, 3.00] for robustness\n\n")
                    
                    if is_robust:
                        f.write("**Result**: ✓ ROBUST\n\n")
                        f.write("Hit-rate is stable across range perturbations.\n")
                        f.write("This supports genuine rigidity rather than boundary artifacts.\n\n")
                    else:
                        f.write("**Result**: ✗ NOT ROBUST\n\n")
                        f.write("Hit-rate varies significantly with range perturbations.\n")
                        f.write("May indicate sensitivity to range boundaries.\n")
                        f.write("Consider refining parameter ranges or investigating edge effects.\n\n")
                else:
                    f.write("**Result**: Insufficient data for robustness assessment\n\n")
            else:
                f.write("**Result**: Cannot assess (baseline hit-rate is zero)\n\n")
        
        # Conclusion
        f.write("## Conclusion\n\n")
        
        if mapping_mode == 'ubt':
            # Rigidity assessment
            f.write("### Rigidity Assessment\n\n")
            
            if hit_rate < 0.01:
                f.write("**High rigidity** - Matching configurations are rare (<1%)\n\n")
                f.write("Layer 2 parameter space appears highly constrained.\n")
                f.write("Only a small fraction of configurations reproduce observed constants.\n")
            elif hit_rate < 0.05:
                f.write("**Moderate rigidity** - Matching configurations uncommon (1-5%)\n\n")
                f.write("Layer 2 parameter space shows some constraints.\n")
                f.write("Some freedom remains in parameter choices.\n")
            else:
                f.write("**Low rigidity** - Matching configurations common (≥5%)\n\n")
                f.write("Layer 2 parameter space appears weakly constrained.\n")
                f.write("Many configurations can reproduce observed constants.\n")
            
            f.write("\n")
            
            # Current configuration ranking
            if 'current_config_rank' in summary:
                f.write("### Current Configuration Ranking\n\n")
                percentile = summary.get('current_config_percentile', 50)
                rank = summary.get('current_config_rank', 0)
                
                f.write(f"**Rank**: {rank} / {n_total}\n")
                f.write(f"**Percentile**: {percentile:.2f}%\n\n")
                
                if percentile < 1.0:
                    f.write("Current UBT configuration is in the **top 1%**.\n")
                    f.write("This is an exceptional configuration.\n")
                elif percentile < 10.0:
                    f.write("Current UBT configuration is in the **top 10%**.\n")
                    f.write("This is a good configuration.\n")
                elif percentile < 50.0:
                    f.write("Current UBT configuration is **above median**.\n")
                    f.write("This is a moderate configuration.\n")
                else:
                    f.write("Current UBT configuration is **below median**.\n")
                    f.write("Configuration may need review.\n")
                
                f.write("\n")
            
            # Overall verdict
            f.write("### Overall Verdict\n\n")
            
            if hit_rate < 0.01 and summary.get('current_config_percentile', 100) < 10:
                f.write("**Strong evidence for Layer 2 constraints**:\n")
                f.write("- High rigidity (rare matches)\n")
                f.write("- Current configuration is exceptional\n")
                f.write("- Suggests Layer 2 choices may be physically constrained\n")
            elif hit_rate < 0.05:
                f.write("**Moderate evidence for Layer 2 constraints**:\n")
                f.write("- Some rigidity observed\n")
                f.write("- Further investigation recommended\n")
            else:
                f.write("**Weak evidence for Layer 2 constraints**:\n")
                f.write("- Low rigidity (many matching configurations)\n")
                f.write("- Layer 2 choices may be arbitrary\n")
            
        else:
            # Placeholder mode
            f.write("⚠️ **WARNING**: This analysis uses PLACEHOLDER physics mapping.\n\n")
            f.write("Results have NO scientific interpretation.\n")
            f.write("This is a framework demonstration only.\n\n")
            f.write("**No rigidity assessment is valid in placeholder mode.**\n")
            f.write("**No configuration ranking is meaningful in placeholder mode.**\n\n")
            f.write("For scientifically interpretable results, use `--mapping ubt`.\n")


def save_figures(results: List[Dict[str, Any]], outdir: Path):
    """
    Save diagnostic figures.
    
    Parameters
    ----------
    results : List[Dict[str, Any]]
        List of result dictionaries
    outdir : Path
        Output directory for figures
    """
    try:
        import matplotlib
        matplotlib.use('Agg')  # Non-interactive backend
        import matplotlib.pyplot as plt
    except ImportError:
        print("Warning: matplotlib not available, skipping figure generation")
        return
    
    if not results:
        return
    
    # Create figures directory
    fig_dir = outdir / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    
    # Extract data
    scores = [r['combined_score'] for r in results]
    
    # Figure 1: Score histogram
    plt.figure(figsize=(8, 6))
    plt.hist(scores, bins=50, edgecolor='black')
    plt.xlabel('Combined Score')
    plt.ylabel('Count')
    plt.title('Distribution of Combined Scores')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(fig_dir / 'score_hist.png', dpi=150)
    plt.close()
    
    # Figure 2: Alpha error histogram (if available)
    if 'alpha_inv_error' in results[0]:
        alpha_errors = [r['alpha_inv_error'] for r in results]
        plt.figure(figsize=(8, 6))
        plt.hist(alpha_errors, bins=50, edgecolor='black')
        plt.xlabel('Alpha Inverse Normalized Error')
        plt.ylabel('Count')
        plt.title('Distribution of Alpha Inverse Errors')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(fig_dir / 'alpha_error_hist.png', dpi=150)
        plt.close()
    
    # Figure 3: Scatter plot (winding number vs alpha error)
    if 'winding_number' in results[0] and 'alpha_inv_error' in results[0]:
        winding = [r['winding_number'] for r in results]
        alpha_errors = [r['alpha_inv_error'] for r in results]
        
        plt.figure(figsize=(8, 6))
        plt.scatter(winding, alpha_errors, alpha=0.5)
        plt.xlabel('Winding Number')
        plt.ylabel('Alpha Inverse Normalized Error')
        plt.title('Winding Number vs Alpha Error')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(fig_dir / 'scatter_winding_vs_alpha_error.png', dpi=150)
        plt.close()
