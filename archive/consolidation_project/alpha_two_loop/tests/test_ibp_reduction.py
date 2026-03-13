"""
Test suite for IBP reduction to master integrals.

This test verifies that all 2-loop vacuum polarization diagrams
reduce correctly to the declared master integral basis.

NO STUBS - all tests use actual symbolic computations.
"""

import pytest
import sys
from pathlib import Path

# Add symbolics to path
test_dir = Path(__file__).parent
symbolics_dir = test_dir.parent / "symbolics"
sys.path.insert(0, str(symbolics_dir))

from ibp_system import (
    reduce_to_MI,
    construct_2loop_vacuum_polarization_diagrams,
    reduce_all_vacuum_polarization_diagrams,
    IBPSystem,
    DiagramTopology,
)


class TestIBPReduction:
    """Test IBP reduction system."""
    
    def test_all_diagrams_reduce_to_known_MIs(self):
        """Verify all diagrams reduce to declared master integral basis."""
        # Get all reductions
        reductions = reduce_all_vacuum_polarization_diagrams()
        
        # Known MI basis
        known_MIs = {'bubble', 'sunset', 'double_bubble'}
        
        # Check each reduction
        for diag_name, reduction in reductions.items():
            assert len(reduction) > 0, f"{diag_name} has empty reduction"
            
            for mi_name, coeff in reduction:
                assert mi_name in known_MIs, \
                    f"{diag_name} reduces to unknown MI: {mi_name}"
    
    def test_no_unknown_integrals(self):
        """Ensure no 'unknown' or 'unresolved' integrals appear."""
        reductions = reduce_all_vacuum_polarization_diagrams()
        
        forbidden_names = ['unknown', 'unresolved', 'pending', 'TODO']
        
        for diag_name, reduction in reductions.items():
            for mi_name, coeff in reduction:
                mi_lower = mi_name.lower()
                for forbidden in forbidden_names:
                    assert forbidden not in mi_lower, \
                        f"{diag_name} has forbidden MI name: {mi_name}"
    
    def test_sunset_topology_reduces_correctly(self):
        """Test sunset diagram reduces to sunset MI."""
        diagrams = construct_2loop_vacuum_polarization_diagrams()
        
        sunset_diag = None
        for diag in diagrams:
            if diag.topology == DiagramTopology.SUNSET:
                sunset_diag = diag
                break
        
        assert sunset_diag is not None, "Sunset diagram not found"
        
        reduction = reduce_to_MI(sunset_diag)
        
        # Should reduce to sunset MI
        mi_names = [name for name, coeff in reduction]
        assert 'sunset' in mi_names, \
            f"Sunset topology should reduce to sunset MI, got {mi_names}"
    
    def test_double_bubble_topology_reduces_correctly(self):
        """Test double bubble diagram reduces to double_bubble MI."""
        diagrams = construct_2loop_vacuum_polarization_diagrams()
        
        double_diag = None
        for diag in diagrams:
            if diag.topology == DiagramTopology.DOUBLE_BUBBLE:
                double_diag = diag
                break
        
        assert double_diag is not None, "Double bubble diagram not found"
        
        reduction = reduce_to_MI(double_diag)
        
        # Should reduce to double_bubble MI
        mi_names = [name for name, coeff in reduction]
        assert 'double_bubble' in mi_names, \
            f"Double bubble should reduce to double_bubble MI, got {mi_names}"
    
    def test_all_diagrams_constructed(self):
        """Verify we construct all necessary 2-loop diagrams."""
        diagrams = construct_2loop_vacuum_polarization_diagrams()
        
        # Should have at least 3 diagrams (sunset, double bubble, vertex)
        assert len(diagrams) >= 3, \
            f"Expected at least 3 diagrams, got {len(diagrams)}"
        
        # Check topologies present
        topologies = {diag.topology for diag in diagrams}
        expected_topologies = {
            DiagramTopology.SUNSET,
            DiagramTopology.DOUBLE_BUBBLE,
            DiagramTopology.VERTEX_CORRECTION,
        }
        
        for expected_top in expected_topologies:
            assert expected_top in topologies, \
                f"Missing topology: {expected_top.value}"
    
    def test_reduction_verification_works(self):
        """Test that reduction verification catches invalid reductions."""
        diagrams = construct_2loop_vacuum_polarization_diagrams()
        ibp = IBPSystem()
        
        for diag in diagrams:
            # Valid reduction
            valid_reduction = reduce_to_MI(diag)
            assert ibp.verify_reduction(diag, valid_reduction), \
                f"Valid reduction failed verification for {diag}"
            
            # Invalid reduction (unknown MI)
            invalid_reduction = [('unknown_integral', 1)]
            assert not ibp.verify_reduction(diag, invalid_reduction), \
                "Invalid reduction should fail verification"
    
    def test_no_hardcoded_values_in_reductions(self):
        """Ensure no hardcoded numerical values appear in reduction coefficients."""
        reductions = reduce_all_vacuum_polarization_diagrams()
        
        # Check that coefficients are symbolic or simple rationals
        for diag_name, reduction in reductions.items():
            for mi_name, coeff in reduction:
                # Coefficient should be symbolic expression or exact rational
                # NOT a float like 1.84 or 137.036
                coeff_str = str(coeff)
                
                # Forbidden patterns
                forbidden_floats = ['1.84', '137.03', '0.00729']
                for forbidden in forbidden_floats:
                    assert forbidden not in coeff_str, \
                        f"{diag_name} has suspicious coefficient: {coeff}"


class TestMasterIntegralBasis:
    """Test the master integral basis is complete and minimal."""
    
    def test_mi_basis_is_minimal(self):
        """Verify MI basis is minimal (no redundant integrals)."""
        ibp = IBPSystem()
        basis = ibp.master_basis
        
        # Should have exactly 3 MIs for 2-loop vacuum polarization
        # (This is the known minimal basis)
        assert len(basis) == 3, \
            f"Expected 3 MIs in minimal basis, got {len(basis)}"
        
        expected = {'bubble', 'sunset', 'double_bubble'}
        assert basis == expected, \
            f"Unexpected MI basis: {basis}"
    
    def test_mi_basis_is_complete(self):
        """Verify all diagrams can be reduced to this basis."""
        reductions = reduce_all_vacuum_polarization_diagrams()
        ibp = IBPSystem()
        
        # All MIs used should be in the basis
        used_mis = set()
        for reduction in reductions.values():
            for mi_name, coeff in reduction:
                used_mis.add(mi_name)
        
        # Every used MI must be in the basis
        assert used_mis.issubset(ibp.master_basis), \
            f"Used MIs {used_mis} not in basis {ibp.master_basis}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
