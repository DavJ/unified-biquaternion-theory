import sys
from pathlib import Path

# Ensure repo root is on sys.path so `import THEORY_COMPARISONS...` works reliably
REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
