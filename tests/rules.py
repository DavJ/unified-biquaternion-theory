"""
UBT Theory Invariant Rules
===========================

This module defines theory-level invariants that MUST be enforced across
the repository to ensure UBT never silently reverts to classical General
Relativity as the fundamental theory.

These rules are NOT optional documentation checks - they are core theory
constraints that protect the biquaternionic formalism.
"""

import re
from typing import List, Tuple

# =============================================================================
# FORBIDDEN PATTERNS - GR language without proper projection/limit context
# =============================================================================

FORBIDDEN_GR_PHRASES = [
    # Forbidden: Treating classical metric as fundamental
    (
        r"Let\s+g_\{\\mu\\nu\}\s+be\s+the\s+spacetime\s+metric",
        "Classical metric g_{μν} treated as fundamental instead of projection"
    ),
    (
        r"(?<!Re\()(?<!projection\s)g_\{\\mu\\nu\}\s+is\s+the\s+(?:fundamental|primary|basic)\s+metric",
        "Classical metric g_{μν} described as fundamental"
    ),
    (
        r"standard\s+Einstein\s+equations(?!\s+(?:arise|emerge|result|follow|are\s+recovered))",
        "Einstein equations referenced without projection/emergence context"
    ),
    (
        r"Christoffel\s+symbols?\s+\\Gamma",
        "Christoffel symbols referenced without clarifying they are projections"
    ),
    (
        r"Levi-Civita\s+connection",
        "Levi-Civita connection referenced without projection context"
    ),
    (
        r"assume\s+g_\{\\mu\\nu\}\s+is\s+the\s+metric",
        "Assuming classical metric without biquaternionic foundation"
    ),
    (
        r"start\s+with\s+(?:the\s+)?metric\s+g_\{\\mu\\nu\}",
        "Starting with classical metric instead of biquaternionic metric"
    ),
]

# =============================================================================
# REQUIRED METRIC PROJECTION PATTERNS
# =============================================================================

REQUIRED_METRIC_PROJECTIONS = [
    # At least one of these patterns must appear in the codebase
    r"g_\{\\mu\\nu\}\s*:?=\s*(?:\\text\{)?Re(?:\\})?\(?\s*\\mathcal\{G\}_\{\\mu\\nu\}",
    r"g_\{\\mu\\nu\}\s*:?=\s*(?:\\text\{)?Re(?:\\})?\(?\s*\$?\\mathcal\{G\}_\{\\mu\\nu\}",
    r"g_\{\\mu\\nu\}\s+:=\s+\\text\{Re\}\(\\mathcal\{G\}_\{\\mu\\nu\}\)",
]

# Alternative notations
REQUIRED_METRIC_PROJECTIONS.extend([
    r"g_\{\\mu\\nu\}\s*=\s*\\mathrm\{Re\}\(\\mathcal\{G\}_\{\\mu\\nu\}\)",
    r"real\s+projection.*g_\{\\mu\\nu\}.*\\mathcal\{G\}_\{\\mu\\nu\}",
])

# =============================================================================
# REQUIRED LOCK-IN FILES
# =============================================================================

REQUIRED_LOCK_IN_FILES = [
    "UBT_Main.tex",
    "THEORY_STATUS_DISCLAIMER.tex",
]

# =============================================================================
# ALLOWED CONTEXTS - When classical GR language is acceptable
# =============================================================================

ALLOWED_CONTEXTS = [
    # These patterns indicate proper contextualization
    r"in\s+the\s+(?:real|Hermitian|classical)\s+(?:limit|sector|projection)",
    r"taking\s+(?:the\s+)?(?:real\s+part|Re|Hermitian\s+projection)",
    r"after\s+projection",
    r"(?:recovers?|reproduces?)\s+(?:Einstein|GR|General\s+Relativity|the\s+standard)",
    r"compatibility\s+with\s+(?:Einstein|GR|General\s+Relativity)",
    r"reduces?\s+to\s+(?:Einstein|GR|General\s+Relativity|the\s+classical)",
    r"real-valued\s+limit",
    r"observer-restricted\s+sector",
    r"Hermitian\s+reduction",
    r"are\s+derived",
    r"is\s+derived",
    r"derived\s+(?:projection|from)",
    r"not\s+fundamental",
    r"arise\s+(?:as|from|only\s+after)",
    r"obtained\s+(?:as|from|via)",
    r"defined\s+as.*Re\(",
    r"=.*Re\(",
    r":=.*Re\(",
    r"resulting",
    r"when\s+restricted\s+to",
    r"real\s+projection",
    r"GR\s+limit",
    r"classical\s+(?:limit|sector)",
]

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def check_allowed_context(text: str, match_pos: Tuple[int, int], window: int = 200) -> bool:
    """
    Check if a forbidden pattern appears in an allowed context.
    
    Args:
        text: Full text content
        match_pos: (start, end) position of the match
        window: Number of characters to check before and after match
        
    Returns:
        True if the match appears in an allowed context, False otherwise
    """
    start = max(0, match_pos[0] - window)
    end = min(len(text), match_pos[1] + window)
    context = text[start:end]
    
    for allowed_pattern in ALLOWED_CONTEXTS:
        if re.search(allowed_pattern, context, re.IGNORECASE):
            return True
    
    return False


def get_line_info(text: str, pos: int) -> Tuple[int, str]:
    """
    Get line number and line content for a position in text.
    
    Args:
        text: Full text content
        pos: Character position
        
    Returns:
        (line_number, line_content)
    """
    lines = text[:pos].split('\n')
    line_num = len(lines)
    line_content = text.split('\n')[line_num - 1] if line_num <= len(text.split('\n')) else ""
    return line_num, line_content
