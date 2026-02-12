# Copyright (c) 2026 David Jaroš (UBT Framework)
# SPDX-License-Identifier: MIT

"""
Tests for Alpha Stability Scan

These tests are NON-CIRCULAR: they do not hardcode "137 must win"
but instead test:
- Determinism (same seed → same results)
- Schema compliance (correct output format)
- Invariants (ranking is consistent, metrics are positive, etc.)
"""

import pytest
import json
import csv
from pathlib import Path
import tempfile
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from analysis.stability_metrics import (
    spectral_gap_metric,
    robustness_metric,
    combined_stability,
    is_prime,
    is_twin_prime,
    compute_all_metrics
)

from analysis.alpha_stability_scan import (
    scan_range,
    rank_candidates,
    find_local_maximum,
    save_results
)


class TestStabilityMetrics:
    """Test individual stability metric functions."""
    
    def test_is_prime(self):
        """Test prime detection."""
        assert is_prime(2)
        assert is_prime(3)
        assert is_prime(137)
        assert not is_prime(1)
        assert not is_prime(4)
        assert not is_prime(136)
        assert not is_prime(138)
    
    def test_is_twin_prime(self):
        """Test twin prime detection."""
        assert is_twin_prime(3)  # (3, 5)
        assert is_twin_prime(5)  # (3, 5) or (5, 7)
        assert is_twin_prime(137)  # (137, 139)
        assert is_twin_prime(139)  # (137, 139)
        assert not is_twin_prime(2)
        assert not is_prime(4)
    
    def test_spectral_gap_positive(self):
        """Spectral gap metric must be positive."""
        for n in [101, 137, 150, 199]:
            gap = spectral_gap_metric(n)
            assert gap > 0, f"Spectral gap for n={n} must be positive"
    
    def test_robustness_positive(self):
        """Robustness metric must be positive."""
        for n in [101, 137, 150, 199]:
            rob = robustness_metric(n, seed=42)
            assert rob > 0, f"Robustness for n={n} must be positive"
    
    def test_determinism(self):
        """Same seed should give same results."""
        n = 137
        
        # Run twice with same seed
        rob1 = robustness_metric(n, seed=42)
        rob2 = robustness_metric(n, seed=42)
        
        assert rob1 == rob2, "Robustness metric must be deterministic with fixed seed"
        
        comb1 = combined_stability(n, seed=42)
        comb2 = combined_stability(n, seed=42)
        
        assert comb1 == comb2, "Combined metric must be deterministic with fixed seed"
    
    def test_compute_all_metrics_schema(self):
        """Test that compute_all_metrics returns correct schema."""
        metrics = compute_all_metrics(137, seed=0)
        
        required_keys = ['n', 'is_prime', 'is_twin_prime', 
                         'spectral_gap', 'robustness', 'combined']
        
        for key in required_keys:
            assert key in metrics, f"Missing key: {key}"
        
        assert metrics['n'] == 137
        assert metrics['is_prime'] == 1
        assert metrics['is_twin_prime'] == 1
        assert metrics['spectral_gap'] > 0
        assert metrics['robustness'] > 0
        assert metrics['combined'] > 0


class TestStabilityScan:
    """Test the full stability scan pipeline."""
    
    def test_scan_range_returns_list(self):
        """Scan should return a list of candidates."""
        candidates = scan_range(130, 140, seed=0)
        assert isinstance(candidates, list)
        assert len(candidates) == 11  # 130 to 140 inclusive
    
    def test_scan_range_prime_filter(self):
        """Prime filter should only return primes."""
        candidates = scan_range(130, 140, filter_primes=True, seed=0)
        
        for c in candidates:
            assert is_prime(c['n']), f"n={c['n']} is not prime but was included"
    
    def test_scan_range_twin_prime_filter(self):
        """Twin prime filter should only return twin primes."""
        candidates = scan_range(130, 145, filter_twin_primes=True, seed=0)
        
        for c in candidates:
            assert is_twin_prime(c['n']), f"n={c['n']} is not twin prime but was included"
    
    def test_rank_candidates_ordering(self):
        """Ranking should be in descending order."""
        candidates = scan_range(130, 140, seed=0)
        ranked = rank_candidates(candidates, metric_key='combined')
        
        # Check descending order
        for i in range(len(ranked) - 1):
            assert ranked[i]['combined'] >= ranked[i+1]['combined'], \
                "Candidates should be in descending order"
        
        # Check ranks are sequential
        for i, c in enumerate(ranked, start=1):
            assert c['rank'] == i, f"Rank should be {i} but got {c['rank']}"
    
    def test_find_local_maximum_found(self):
        """Test finding a candidate that exists."""
        candidates = scan_range(130, 145, seed=0)
        ranked = rank_candidates(candidates)
        
        analysis = find_local_maximum(ranked, target_n=137, window=3)
        
        assert analysis['found'] == True
        assert analysis['target_n'] == 137
        assert 'target_value' in analysis
        assert 'is_local_max' in analysis
        assert 'rank' in analysis
    
    def test_find_local_maximum_not_found(self):
        """Test handling when target not in range."""
        candidates = scan_range(100, 120, seed=0)
        ranked = rank_candidates(candidates)
        
        analysis = find_local_maximum(ranked, target_n=137, window=3)
        
        assert analysis['found'] == False
        assert analysis['target_n'] == 137
        assert 'message' in analysis
    
    def test_save_and_load_csv(self):
        """Test CSV save and load roundtrip."""
        candidates = scan_range(135, 140, seed=0)
        ranked = rank_candidates(candidates)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = Path(tmpdir) / 'test.csv'
            save_results(ranked, csv_path, format='csv')
            
            assert csv_path.exists()
            
            # Read back and check
            with open(csv_path, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            
            assert len(rows) == len(ranked)
            
            # Check first row
            assert rows[0]['n'] == str(ranked[0]['n'])
    
    def test_save_and_load_json(self):
        """Test JSON save and load roundtrip."""
        candidates = scan_range(135, 140, seed=0)
        ranked = rank_candidates(candidates)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            json_path = Path(tmpdir) / 'test.json'
            save_results(ranked, json_path, format='json')
            
            assert json_path.exists()
            
            # Read back and check
            with open(json_path, 'r') as f:
                loaded = json.load(f)
            
            assert len(loaded) == len(ranked)
            assert loaded[0]['n'] == ranked[0]['n']
    
    def test_determinism_full_scan(self):
        """Full scan should be deterministic with fixed seed."""
        candidates1 = scan_range(130, 140, seed=42)
        candidates2 = scan_range(130, 140, seed=42)
        
        assert len(candidates1) == len(candidates2)
        
        for c1, c2 in zip(candidates1, candidates2):
            assert c1['n'] == c2['n']
            assert c1['spectral_gap'] == c2['spectral_gap']
            assert c1['robustness'] == c2['robustness']
            assert c1['combined'] == c2['combined']


class TestNonCircularity:
    """Test that tests are non-circular (don't hardcode that 137 must win)."""
    
    def test_no_hardcoded_137_wins(self):
        """
        This test verifies that our test suite doesn't assume 137 wins.
        
        We run a scan and check that:
        1. The scan completes successfully
        2. We get rankings
        3. We can identify the top candidate
        4. But we DON'T assert that top candidate must be 137
        
        This is the correct non-circular approach.
        """
        candidates = scan_range(130, 145, seed=0)
        ranked = rank_candidates(candidates)
        
        # These assertions are fine (test mechanics)
        assert len(ranked) > 0
        assert ranked[0]['rank'] == 1
        assert 'n' in ranked[0]
        
        # This would be CIRCULAR (wrong):
        # assert ranked[0]['n'] == 137  # DON'T DO THIS
        
        # Instead, we just verify the structure:
        top_n = ranked[0]['n']
        assert isinstance(top_n, (int, np.int64))
        assert 130 <= top_n <= 145
        
        # And we can report what we found (for documentation)
        # but not enforce it in the test
        print(f"Top candidate in range [130, 145]: n={top_n}")


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
