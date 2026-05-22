#!/usr/bin/env python3
"""
Audit claim-status consistency for UBT repository.
Fails if forbidden claim phrases appear outside allowed historical/archive files.
Checks:
- No 'alpha derived' claim outside superseded/historical sections
- No consciousness/afterlife/psychon claims in canonical/
- No Zerilli status contradiction across active status files
- No forbidden speculative claims in canonical/, papers/ abstract/introduction/conclusion, or README.md
- All status files (STATUS_OF_UBT.md, CLAIMS_MATRIX.md, WHAT_IS_PROVED.md, ROADMAP.md, DERIVATION_STATUS_STANDARD.md) agree on Zerilli status
"""
import sys
import os
import re

# Forbidden phrases and allowed exceptions
FORBIDDEN = [
    r'alpha (is|was|has been)? ?derived',
    r'α (is|was|has been)? ?derived',
    r'psychon',
    r'afterlife',
    r'consciousness field',
    r'ThetaComm',
    r'soul',
    r'immortality',
    r'simulation ontology',
    r'Zerilli.*OPEN',
    r'GAP-Z.*OPEN',
    r'candidate route.*Zerilli',
    r'not counted as \[L1\] closure',
]

ALLOWED_PATHS = [
    'speculative_extensions/',
    'docs/historical/',
    'docs/archive/',
    'reports/contradictions_resolved.md',
]

STATUS_FILES = [
    'STATUS_OF_UBT.md',
    'CLAIMS_MATRIX.md',
    'WHAT_IS_PROVED.md',
    'ROADMAP.md',
    'DERIVATION_STATUS_STANDARD.md',
]

ZERILLI_PROOF_PATTERN = re.compile(r'Zerilli.*PROVED|GAP-Z.*PROVED|Zerilli equation.*PROVED', re.IGNORECASE)


def is_allowed(path):
    return any(p in path for p in ALLOWED_PATHS)

def grep_forbidden(root):
    errors = []
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith(('.pyc', '.o', '.so', '.png', '.jpg', '.jpeg', '.gif', '.pdf')):
                continue
            fpath = os.path.join(dirpath, fname)
            relpath = os.path.relpath(fpath, root)
            if is_allowed(relpath):
                continue
            try:
                with open(fpath, encoding='utf-8', errors='ignore') as f:
                    for i, line in enumerate(f, 1):
                        for pat in FORBIDDEN:
                            if re.search(pat, line, re.IGNORECASE):
                                errors.append(f"Forbidden phrase '{pat}' in {relpath}:{i}: {line.strip()}")
            except Exception as e:
                continue
    return errors

def check_zerilli_status(root):
    status = []
    for fname in STATUS_FILES:
        fpath = os.path.join(root, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, encoding='utf-8', errors='ignore') as f:
            text = f.read()
            if ZERILLI_PROOF_PATTERN.search(text):
                status.append((fname, 'PROVED'))
            elif re.search(r'Zerilli.*OPEN|GAP-Z.*OPEN', text, re.IGNORECASE):
                status.append((fname, 'OPEN'))
            else:
                status.append((fname, 'UNKNOWN'))
    if len(set(s for _, s in status if s != 'UNKNOWN')) > 1:
        return [f"Zerilli status mismatch: {status}"]
    return []

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    errors = grep_forbidden(root)
    errors += check_zerilli_status(root)
    if errors:
        print("CLAIM STATUS AUDIT FAILED:")
        for err in errors:
            print("  ", err)
        sys.exit(1)
    print("CLAIM STATUS AUDIT PASSED.")

if __name__ == '__main__':
    main()
