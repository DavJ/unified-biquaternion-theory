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


def save_figures(results: List[Dict[str, Any]], outdir: Path):
    """
    Save diagnostic figures (placeholder for future implementation).
    
    Parameters
    ----------
    results : List[Dict[str, Any]]
        List of result dictionaries
    outdir : Path
        Output directory for figures
    """
    # TODO: Implement visualization
    # - Parameter distribution histograms
    # - Score vs parameter scatter plots
    # - 2D correlation heatmaps
    # - Best configurations visualization
    pass
