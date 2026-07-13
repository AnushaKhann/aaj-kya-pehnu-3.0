"""
taxonomy_mapper.py

Converts Fashionpedia categories
into AKP wardrobe categories.
"""

from typing import Dict


FASHIONPEDIA_TO_AKP: Dict[str, str | None] = {

    # Tops

    "shirt, blouse": "Shirt",

    "top, t-shirt, sweatshirt": "T-Shirt",

    "sweater": "Sweater",

    "cardigan": "Cardigan",

    "jacket": "Jacket",

    "vest": "Vest",

    # Bottoms

    "pants": "Pants",

    "shorts": "Shorts",

    "skirt": "Skirt",

    # Outerwear

    "coat": "Coat",

    # One-piece

    "dress": "Dress",

    "jumpsuit": "Jumpsuit",

    # Accessories

    "shoe": "Shoes",

    "bag, wallet": "Bag",

    "hat": "Hat",

    "scarf": "Scarf",

    # Ignore

    "cape": None,

    "glasses": None,

    "headband, head covering, hair accessory": None,

    "tie": None,

    "glove": None,

    "watch": None,

    "belt": None,

    "leg warmer": None,

    "tights, stockings": None,

    "sock": None,

    "umbrella": None,

    "hood": None,

    "collar": None,

    "lapel": None,

    "epaulette": None,

    "sleeve": None,

    "pocket": None,

    "neckline": None,

    "buckle": None,

    "zipper": None,

    "applique": None,

    "bead": None,

    "bow": None,

    "flower": None,

    "fringe": None,

    "ribbon": None,

    "rivet": None,

    "ruffle": None,

    "sequin": None,

    "tassel": None,
}

def map_category(category_name: str) -> str | None:
    """
    Convert a Fashionpedia category
    into an AKP category.
    """

    return FASHIONPEDIA_TO_AKP.get(category_name)


def is_supported(category_name: str) -> bool:
    """
    Returns True if the category
    should be kept.
    """

    return map_category(category_name) is not None