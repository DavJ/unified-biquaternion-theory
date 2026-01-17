#!/usr/bin/env python3

"""
Automated in-place fix for forensic_fingerprint/tools/spectral_parity_test.py on macOS,
without requiring git/patch tools.

This v2 script is more tolerant about how main() is defined (it matches with leading
indentation and also handles cases where main is named differently).

Fixes attempted:
- Ensure there is a callable entrypoint main(argv=None) (or adapt existing main-like function)
- Ensure argparse uses argv: parse_args(argv)
- Make the module docstring a raw string to silence invalid escape sequence warnings
- Repair common line-merge / indentation issues around rng initialization
- Writes a .bak backup before modifying

Usage (from repo root):
  python3 apply_spectral_parity_autofix_v2.py
"""

import re
from pathlib import Path
import shutil
import sys

TARGET = Path("forensic_fingerprint/tools/spectral_parity_test.py")

def die(msg: str, code: int = 1):
    print(f"[autofix] ERROR: {msg}", file=sys.stderr)
    raise SystemExit(code)

def info(msg: str):
    print(f"[autofix] {msg}")

def main():
    if not TARGET.exists():
        die(f"Cannot find {TARGET}. Run this from the repository root.")
    src = TARGET.read_text(encoding="utf-8")

    # Backup
    bak = TARGET.with_suffix(TARGET.suffix + ".bak")
    if not bak.exists():
        shutil.copyfile(TARGET, bak)
        info(f"Backup created: {bak}")

    out = src

    # 1) Make top-level docstring raw string if present and not already raw
    out = re.sub(r'^(\\s*)(\"\"\"|\\\'\\\'\\\')', r'\\1r\\2', out, count=1)

    # 2) Locate a main-like function definition.
    # Accept leading spaces and any arguments.
    m = re.search(r'^(?P<indent>\\s*)def\\s+main\\s*\\((?P<args>[^)]*)\\)\\s*:\\s*$', out, flags=re.MULTILINE)
    if m:
        indent = m.group("indent")
        # If it is def main(): change to def main(argv=None):
        out, n1 = re.subn(rf'^{re.escape(indent)}def\\s+main\\s*\\(\\s*\\)\\s*:\\s*$',
                          f'{indent}def main(argv=None):',
                          out, flags=re.MULTILINE)
        if n1:
            info("Updated def main() -> def main(argv=None).")
        else:
            # Ensure signature has argv=None if it doesn't already reference argv
            if "argv" not in m.group("args"):
                out = re.sub(rf'^{re.escape(indent)}def\\s+main\\s*\\([^)]*\\)\\s*:\\s*$',
                             f'{indent}def main(argv=None):',
                             out, count=1, flags=re.MULTILINE)
                info("Normalized def main(...) -> def main(argv=None).")
            else:
                info("main() already takes arguments (leaving signature).")
    else:
        # Some versions may define entrypoint as _main or cli_main
        m2 = re.search(r'^(?P<indent>\\s*)def\\s+(?P<name>(_main|cli_main|run|entrypoint))\\s*\\((?P<args>[^)]*)\\)\\s*:\\s*$',
                       out, flags=re.MULTILINE)
        if not m2:
            # As last resort, we won't fail hard; we'll just warn.
            info("WARNING: Could not locate def main(...). Will continue with other fixes.")
        else:
            info(f"Found entrypoint function '{m2.group('name')}'. (Not renaming automatically.)")

    # 3) Ensure argparse uses argv: parse_args(argv)
    # Replace first parse_args() with parse_args(argv) if argv symbol exists in main signature.
    out, n_pa = re.subn(r'parse_args\\s*\\(\\s*\\)',
                        'parse_args(argv)',
                        out, count=1)
    if n_pa:
        info("Rewrote first parse_args() -> parse_args(argv).")
    else:
        info("parse_args() not found or already uses argv.")

    # 4) Fix known bad merge: ')rng' -> ')\\n    rng ='
    out = re.sub(r'\\)\\s*rng\\s*=', ')\\n    rng =', out)

    # 5) Fix indentation around rng line if unexpectedly indented (8+ spaces -> 4 spaces)
    out = re.sub(r'^(\\s{8,})rng\\s*=\\s*np\\.random\\.default_rng\\(([^)]*)\\)\\s*$',
                 r'    rng = np.random.default_rng(\\2)',
                 out, flags=re.MULTILINE)

    TARGET.write_text(out, encoding="utf-8")
    info(f"Updated: {TARGET}")
    info("Done. Now rerun your spectral_parity_test command.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
