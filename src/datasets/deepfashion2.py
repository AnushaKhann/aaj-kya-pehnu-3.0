"""
DeepFashion2 Dataset

Implementation will be added after we receive
the dataset password and extract the files.
"""

from pathlib import Path

from .base_dataset import BaseFashionDataset


class DeepFashion2Dataset(BaseFashionDataset):

    def __init__(self, dataset_path: Path):

        super().__init__(dataset_path)

    def load_images(self):
        raise NotImplementedError

    def load_annotations(self):
        raise NotImplementedError

    def get_categories(self):
        raise NotImplementedError

    def visualize_sample(self, index):
        raise NotImplementedError

    def statistics(self):
        raise NotImplementedError