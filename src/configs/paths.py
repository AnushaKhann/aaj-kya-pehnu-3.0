from pathlib import Path

# Root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data directories
DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

EXTERNAL_DATA_DIR = DATA_DIR / "external"

# Dataset paths
DEEPFASHION2_DIR = RAW_DATA_DIR / "deepfashion2"

FASHIONPEDIA_DIR = RAW_DATA_DIR / "fashionpedia"

MODANET_DIR = RAW_DATA_DIR / "modanet"