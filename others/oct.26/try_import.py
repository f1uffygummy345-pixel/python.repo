import sys
from pathlib import Path

# Add the containing directory so this script can import its sibling module.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import app

print("The import is finished")
print(app.calculate_total(3))