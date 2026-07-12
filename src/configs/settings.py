"""
Global configuration for the Fashion Vision Engine.

Every module in the project imports settings from here.
Never hardcode paths or magic values anywhere else.
"""

from pathlib import Path

# Project Root

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data Directories

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

EXTERNAL_DATA_DIR = DATA_DIR / "external"

# Dataset Paths

DEEPFASHION2_DIR = RAW_DATA_DIR / "deepfashion2"

FASHIONPEDIA_DIR = RAW_DATA_DIR / "fashionpedia"

MODANET_DIR = RAW_DATA_DIR / "modanet"

IMATERIALIST_DIR = RAW_DATA_DIR / "imaterialist"

# Models

MODEL_DIR = PROJECT_ROOT / "models"

CHECKPOINT_DIR = MODEL_DIR / "checkpoints"

PRETRAINED_DIR = MODEL_DIR / "pretrained"

# Experiments

EXPERIMENT_DIR = PROJECT_ROOT / "experiments"

# Random Seed

SEED = 42

# Image

IMAGE_SIZE = 224

# Training

BATCH_SIZE = 32

NUM_WORKERS = 4

DEVICE = "mps"