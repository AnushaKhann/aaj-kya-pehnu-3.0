"""
Base Dataset Interface

Every fashion dataset (DeepFashion2, Fashionpedia, ModaNet, etc.)
must inherit from this class.

This guarantees a common interface across datasets.
"""

from abc import ABC, abstractmethod
from pathlib import Path


class BaseFashionDataset(ABC):

    def __init__(self, dataset_path: Path):

        self.dataset_path = dataset_path

    @abstractmethod
    def load_images(self):
        """Load image paths"""
        pass

    @abstractmethod
    def load_annotations(self):
        """Load annotations"""
        pass

    @abstractmethod
    def get_categories(self):
        """Return dataset categories"""
        pass

    @abstractmethod
    def visualize_sample(self, index: int):
        """Visualize one sample"""
        pass

    @abstractmethod
    def statistics(self):
        """Return dataset statistics"""
        pass