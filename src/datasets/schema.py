from dataclasses import dataclass
from typing import List, Optional


@dataclass
class BoundingBox:
    x1: float
    y1: float
    x2: float
    y2: float


@dataclass
class GarmentItem:

    image_path: str

    dataset_source: str

    bbox: Optional[BoundingBox]

    category: Optional[str]

    subcategory: Optional[str]

    primary_color: Optional[str]

    secondary_colors: List[str]

    pattern: Optional[str]

    material: Optional[str]

    sleeve_length: Optional[str]

    neckline: Optional[str]

    fit: Optional[str]

    season: List[str]

    occasion: List[str]

    style: List[str]