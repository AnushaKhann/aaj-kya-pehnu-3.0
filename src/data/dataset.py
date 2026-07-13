from PIL import Image

from torch.utils.data import Dataset


class ClothingDataset(Dataset):
    """
    Generic clothing dataset.

    Parameters
    ----------
    image_paths : list
        List of image file paths.

    labels : list
        List of integer labels.

    transform : torchvision transform
        Image transformations.
    """

    def __init__(self, image_paths, labels, transform=None):

        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform

    def __len__(self):

        return len(self.image_paths)

    def __getitem__(self, index):

        image = Image.open(self.image_paths[index]).convert("RGB")

        label = self.labels[index]

        if self.transform:

            image = self.transform(image)

        return image, label