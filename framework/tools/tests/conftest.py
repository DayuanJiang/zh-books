import sys
from pathlib import Path

# The framework tools are plain scripts in the parent folder; make them importable from the tests.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
