"""
cropper.py

Utility for cropping garments
from Fashionpedia images.
"""

from pathlib import Path

from PIL import Image

class GarmentCropper:

    def __init__(self, output_size=(224, 224)):
        self.output_size = output_size
        
    def crop(
        self,
        image,
        bbox,
        padding=0.15
    ):

        x, y, w, h = bbox

        pad_x = w * padding
        pad_y = h * padding

        left = max(0, x - pad_x)
        top = max(0, y - pad_y)

        right = min(image.width, x + w + pad_x)
        bottom = min(image.height, y + h + pad_y)

        cropped = image.crop(
            (
                int(left),
                int(top),
                int(right),
                int(bottom)
            )
        )

        return cropped.resize(self.output_size)
    
    def save(
        self,
        image: Image.Image,
        save_path: Path
    ):

        save_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        image.save(save_path)