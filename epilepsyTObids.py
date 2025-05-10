import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "src"))

from epilepsy2bids.bids.siena.convert2bids import convert

root = Path("./siena-scalp-eeg-database-1.0.0")
outDir = Path("./output/bids_format")

convert(root, outDir)

print("Convert Done!")
