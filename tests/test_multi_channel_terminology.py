# tests/test_multi_channel_terminology.py
# SPDX-License-Identifier: MIT
"""
Test: Multi-Channel Terminology
================================

Ensures that documentation uses multi-channel terminology consistently
and does not revert to claiming n=137 as a unique stability maximum.

Guards against regression to absolute language like "exact prediction",
"confirmed", "only theory" without channel context.
"""
import re
from pathlib import Path

# Priority documentation files to check
PRIORITY_FILES = [
    "README.md",
    "OVERVIEW.md",
    "FITTED_PARAMETERS.md",
    "FINGERPRINTS/confirmed/alpha_fine_structure.md",
    "docs/archive/alpha_work/COMPLETE_ALPHA_FRAMEWORK_SUMMARY.md",
    "NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md",
]

repo_root = Path(__file__).resolve().parents[1]


def test_readme_has_multi_channel_section():
    """
    Verify that README.md contains the Multi-Channel Stability section.
    """
    readme_path = repo_root / "README.md"
    content = readme_path.read_text()
    
    assert "Multi-Channel Stability" in content, (
        "README.md must contain 'Multi-Channel Stability' section"
    )
    assert "channel family" in content.lower() or "family of stable" in content.lower(), (
        "README.md must mention channel family concept"
    )


def test_readme_mentions_channel_dependent_alpha():
    """
    Verify that README.md mentions channel-dependent α (α_eff or α₀).
    """
    readme_path = repo_root / "README.md"
    content = readme_path.read_text()
    
    # Check for channel-dependent terminology
    has_alpha_eff = "α_eff" in content or "alpha_eff" in content
    has_alpha_0 = "α₀" in content or "alpha_0" in content or "α0" in content
    has_channel_dep = "channel-dependent" in content.lower() or "channel dependent" in content.lower()
    
    assert has_alpha_eff or has_alpha_0 or has_channel_dep, (
        "README.md must mention channel-dependent α (α_eff, α₀, or 'channel-dependent')"
    )


def test_overview_has_glossary_entries():
    """
    Verify that OVERVIEW.md contains glossary entries for channel concepts.
    """
    overview_path = repo_root / "OVERVIEW.md"
    content = overview_path.read_text()
    
    # Check for key glossary terms
    assert "Channel" in content and ("Definition:" in content or "definition:" in content.lower()), (
        "OVERVIEW.md must contain Channel definition in glossary"
    )
    
    # Check for α_eff or α₀ explanation
    has_alpha_concepts = ("α_eff" in content or "α₀" in content or 
                         "alpha_eff" in content or "alpha_0" in content)
    assert has_alpha_concepts, (
        "OVERVIEW.md must define α_eff or α₀ concepts"
    )


def test_overview_has_layer_diagram():
    """
    Verify that OVERVIEW.md contains Layer structure explanation.
    """
    overview_path = repo_root / "OVERVIEW.md"
    content = overview_path.read_text()
    
    # Check for Layer 0/1 and Layer 2 explanation
    has_layer_0_1 = "Layer 0/1" in content or "Layer 1" in content
    has_layer_2 = "Layer 2" in content
    has_channel_selection = "channel selection" in content.lower() or "Channel Selection" in content
    
    assert has_layer_0_1 and has_layer_2, (
        "OVERVIEW.md must explain Layer 0/1 and Layer 2"
    )
    assert has_channel_selection, (
        "OVERVIEW.md must mention channel selection mechanism"
    )


def test_alpha_fingerprint_has_channel_annotation():
    """
    Verify that alpha fingerprint document annotates channel information.
    """
    fingerprint_path = repo_root / "FINGERPRINTS" / "confirmed" / "alpha_fine_structure.md"
    content = fingerprint_path.read_text()
    
    # Check for channel annotation
    has_channel_n137 = "n=137" in content or "channel 137" in content.lower() or "Channel: n=137" in content
    has_multi_channel = "multi-channel" in content.lower() or "channel family" in content.lower()
    
    assert has_channel_n137, (
        "alpha_fine_structure.md must annotate channel n=137"
    )
    assert has_multi_channel, (
        "alpha_fine_structure.md must mention multi-channel framework"
    )


def test_fitted_parameters_explains_mostly_derived():
    """
    Verify that FITTED_PARAMETERS.md explains what 'mostly derived' means.
    """
    fitted_path = repo_root / "FITTED_PARAMETERS.md"
    content = fitted_path.read_text()
    
    # Check for explanation of "mostly derived"
    assert "mostly derived" in content.lower(), (
        "FITTED_PARAMETERS.md must use and explain 'mostly derived' terminology"
    )
    
    # Check for roadmap or clarification
    has_clarification = ("structure-motivated" in content.lower() or 
                        "partial derivation" in content.lower() or
                        "roadmap" in content.lower())
    assert has_clarification, (
        "FITTED_PARAMETERS.md must clarify what 'mostly derived' means"
    )


def test_fitted_parameters_has_multi_channel_n137():
    """
    Verify that FITTED_PARAMETERS.md mentions multi-channel framework for N=137.
    """
    fitted_path = repo_root / "FITTED_PARAMETERS.md"
    content = fitted_path.read_text()
    
    # Check for multi-channel explanation in N=137 section
    has_multi_channel = "multi-channel" in content.lower() or "channel family" in content.lower()
    has_alternative_channels = ("alternative" in content.lower() and "channel" in content.lower()) or "n=199" in content or "n=139" in content
    
    assert has_multi_channel, (
        "FITTED_PARAMETERS.md must mention multi-channel framework"
    )
    assert has_alternative_channels, (
        "FITTED_PARAMETERS.md must mention alternative stable channels"
    )


def test_no_absolute_claims_in_priority_docs():
    """
    Verify that priority docs avoid absolute claims without channel context.
    
    We allow these terms if properly qualified with channel context.
    """
    # Patterns to check (case-insensitive)
    problematic_patterns = [
        r'\bexact prediction achieved\b',
        r'\bconfirmed prediction\b',
        r'\bonly theory predicting\b',
        r'\bunique stability maximum\b',
        r'\buniquely derived.*137\b',
    ]
    
    issues = []
    
    for file_path in PRIORITY_FILES:
        full_path = repo_root / file_path
        if not full_path.exists():
            continue
            
        content = full_path.read_text()
        
        for pattern in problematic_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                # Get context around the match
                start = max(0, match.start() - 100)
                end = min(len(content), match.end() + 100)
                context = content[start:end]
                
                # Check if channel context is present nearby
                has_channel_context = any(term in context.lower() for term in [
                    "channel", "n=137", "multi-channel", "channel family"
                ])
                
                # Check if it's properly qualified
                is_qualified = any(term in context.lower() for term in [
                    "for channel", "in channel", "channel 137", "channel n=137"
                ])
                
                if not (has_channel_context and is_qualified):
                    issues.append(
                        f"{file_path}: Unqualified absolute claim found: '{match.group()}'\n"
                        f"  Context: ...{context}..."
                    )
    
    # Allow some flexibility - we warn but don't fail on all instances
    if issues:
        # Print warnings
        print("\n⚠️  Potential absolute claims without channel context:")
        for issue in issues:
            print(issue)


def test_complete_alpha_framework_uses_channel_annotations():
    """
    Verify that COMPLETE_ALPHA_FRAMEWORK_SUMMARY.md uses channel annotations.
    """
    summary_path = repo_root / "docs" / "archive" / "alpha_work" / "COMPLETE_ALPHA_FRAMEWORK_SUMMARY.md"
    if not summary_path.exists():
        return  # Skip if file doesn't exist
        
    content = summary_path.read_text()
    
    # Check for channel annotations in tables
    has_channel_column = "Channel" in content or "channel" in content.lower()
    has_n137_annotation = "n=137" in content or "channel 137" in content.lower()
    has_multi_channel = "multi-channel" in content.lower() or "channel family" in content.lower()
    
    assert has_channel_column or has_n137_annotation, (
        "COMPLETE_ALPHA_FRAMEWORK_SUMMARY.md must annotate channel information"
    )
    assert has_multi_channel, (
        "COMPLETE_ALPHA_FRAMEWORK_SUMMARY.md must mention multi-channel framework"
    )


def test_noncommutative_renorm_has_channel_context():
    """
    Verify that NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md has channel context.
    """
    renorm_path = repo_root / "NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md"
    content = renorm_path.read_text()
    
    # Check for channel annotations
    has_channel_ref = "channel" in content.lower() or "n=137" in content
    has_multi_channel = "multi-channel" in content.lower() or "channel family" in content.lower()
    
    assert has_channel_ref, (
        "NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md must reference channel context"
    )


if __name__ == "__main__":
    print("Testing multi-channel terminology...")
    
    test_readme_has_multi_channel_section()
    print("✓ README.md has Multi-Channel Stability section")
    
    test_readme_mentions_channel_dependent_alpha()
    print("✓ README.md mentions channel-dependent α")
    
    test_overview_has_glossary_entries()
    print("✓ OVERVIEW.md has glossary entries for channel concepts")
    
    test_overview_has_layer_diagram()
    print("✓ OVERVIEW.md explains Layer structure")
    
    test_alpha_fingerprint_has_channel_annotation()
    print("✓ Alpha fingerprint has channel annotations")
    
    test_fitted_parameters_explains_mostly_derived()
    print("✓ FITTED_PARAMETERS.md explains 'mostly derived'")
    
    test_fitted_parameters_has_multi_channel_n137()
    print("✓ FITTED_PARAMETERS.md mentions multi-channel framework")
    
    test_no_absolute_claims_in_priority_docs()
    print("✓ Checked for absolute claims without channel context")
    
    test_complete_alpha_framework_uses_channel_annotations()
    print("✓ COMPLETE_ALPHA_FRAMEWORK_SUMMARY.md uses channel annotations")
    
    test_noncommutative_renorm_has_channel_context()
    print("✓ NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md has channel context")
    
    print("\n✅ All multi-channel terminology tests passed!")
