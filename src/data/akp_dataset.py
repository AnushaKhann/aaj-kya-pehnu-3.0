from pathlib import Path
import json

import pandas as pd
from PIL import Image

from torch.utils.data import Dataset
from src.data.label_encoder import LabelEncoder

class AKPDataset(Dataset):
    def __init__(
        self,
        dataset_dir,
        csv_file,
        transform=None
    ):

        self.dataset_dir = Path(dataset_dir)

        self.images_dir = self.dataset_dir / "images"

        self.data = pd.read_csv(
            self.dataset_dir / csv_file
        )

        self.transform = transform

        with open(
            self.dataset_dir / "classes.json",
            "r"
        ) as f:
            class_mapping = json.load(f)

        self.label_encoder = LabelEncoder(
            class_mapping=class_mapping
        )
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):

        row = self.data.iloc[index]

        image_path = self.images_dir / row["filename"]

        image = Image.open(image_path).convert("RGB")

        label = self.label_encoder.encode(
            row["category"]
        )

        if self.transform is not None:
            image = self.transform(image)

        return image, label