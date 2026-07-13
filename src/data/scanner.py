from pathlib import Path


class DatasetScanner:
    """
    Scans a dataset organized as:

    dataset/
        class1/
            image1.jpg
            image2.jpg
        class2/
            image3.jpg
    """

    IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

    def __init__(self, dataset_root):

        self.dataset_root = Path(dataset_root)

    def scan(self):

        image_paths = []
        labels = []
        class_names = []

        class_dirs = sorted(
            [d for d in self.dataset_root.iterdir() if d.is_dir()]
        )

        for class_dir in class_dirs:

            class_name = class_dir.name
            class_names.append(class_name)

            for image_path in class_dir.iterdir():

                if image_path.suffix.lower() in self.IMAGE_EXTENSIONS:

                    image_paths.append(image_path)
                    labels.append(class_name)

        return image_paths, labels, class_names