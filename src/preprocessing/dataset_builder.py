"""
dataset_builder.py

Builds AKP dataset from Fashionpedia.
"""

from sklearn.model_selection import train_test_split
from collections import Counter
import pandas as pd
from tqdm import tqdm
from pathlib import Path
from typing import Dict

from datasets import Dataset

from .taxonomy_mapper import map_category, is_supported
from .cropper import GarmentCropper
import json

class AKPDatasetBuilder:

    def __init__(
        self,
        output_dir,
        category_names,
        image_size=(224, 224)
    ):
        self.output_dir = Path(output_dir)

        # Store Fashionpedia category names
        self.category_names = category_names

        self.cropper = GarmentCropper(
            output_size=image_size
        )
        self.metadata_rows = []
        self.class_counter = Counter()
        
    def create_directories(self):

        (self.output_dir / "images").mkdir(
            parents=True,
            exist_ok=True
        )

        (self.output_dir / "metadata").mkdir(
            parents=True,
            exist_ok=True
        )
        
    def process_sample(
        self,
        sample: Dict,
        sample_index: int
    ):

        image = sample["image"]

        objects = sample["objects"]

        for object_index in range(len(objects["category"])):

            category_id = objects["category"][object_index]

            category = self.category_names[category_id]

            if not is_supported(category):
                continue

            akp_category = map_category(category)
            self.class_counter[akp_category] += 1

            bbox = objects["bbox"][object_index]

            cropped = self.cropper.crop(
                image,
                bbox
            )

            filename = f"{sample_index:06}_{object_index}.jpg"

            image_path = (
                self.output_dir
                / "images"
                / filename
            )

            cropped.save(image_path)

            metadata = {
                "image_id": sample["image_id"],
                "akp_category": akp_category,
                "original_category": category,
                "bbox": bbox,
                "width": sample["width"],
                "height": sample["height"]
            }

            metadata_path = (
                self.output_dir
                / "metadata"
                / filename.replace(".jpg", ".json")
            )

            with open(metadata_path, "w") as f:
                json.dump(metadata, f, indent=4)

            self.metadata_rows.append(
                {
                    "filename": filename,
                    "category": akp_category,
                    "image_id": sample["image_id"]
                }
            )
                
    def build(
        self,
        dataset,
        limit=None
    ):
        """
        Build AKP dataset from a Hugging Face dataset.

        Args:
            dataset: Dataset split (train/val)
            limit: Number of samples to process
        """

        self.create_directories()

        if limit is None:
            limit = len(dataset)
        else:
            limit = min(limit, len(dataset))

        for index in tqdm(
            range(limit),
            desc="Building AKP Dataset"
        ):

            sample = dataset[index]

            self.process_sample(
                sample,
                index
            )
        metadata_df = pd.DataFrame(self.metadata_rows)
        # Build a consistent label mapping
        class_names = sorted(metadata_df["category"].unique())

        class_mapping = {
            class_name: idx
            for idx, class_name in enumerate(class_names)
        }
        
        with open(
            self.output_dir / "classes.json",
            "w"
        ) as f:
            json.dump(
                class_mapping,
                f,
                indent=4
            )

        metadata_df.to_csv(
            self.output_dir / "metadata.csv",
            index=False
        )
        
        category_counts = metadata_df["category"].value_counts()

        if (category_counts >= 2).all():

            print("Using stratified train/validation split.")

            train_df, val_df = train_test_split(
                metadata_df,
                test_size=0.2,
                random_state=42,
                stratify=metadata_df["category"]
            )

        else:

            print(
                "Some categories have fewer than 2 samples. "
                "Falling back to random split."
            )

            train_df, val_df = train_test_split(
                metadata_df,
                test_size=0.2,
                random_state=42,
                shuffle=True
            )
        train_df.to_csv(
            self.output_dir / "train.csv",
            index=False
        )

        val_df.to_csv(
            self.output_dir / "val.csv",
            index=False
        )
        
        stats_path = self.output_dir / "dataset_stats.json"

        with open(stats_path, "w") as f:
            json.dump(
                dict(self.class_counter),
                f,
                indent=4
            )
        print(f"\nProcessed {limit} samples.")
        print(f"Training samples: {len(train_df)}")
        print(f"Validation samples: {len(val_df)}")