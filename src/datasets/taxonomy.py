"""
Universal Fashion Taxonomy

This is the master taxonomy used throughout the project.
Every external dataset is mapped into this taxonomy.
"""

from enum import Enum


class GarmentCategory(str, Enum):

    TOP = "Top"

    BOTTOM = "Bottom"

    DRESS = "Dress"

    OUTERWEAR = "Outerwear"

    FOOTWEAR = "Footwear"

    BAG = "Bag"

    ACCESSORY = "Accessory"
    
class TopType(str, Enum):

    TSHIRT = "T-Shirt"

    SHIRT = "Shirt"

    POLO = "Polo"

    HOODIE = "Hoodie"

    SWEATSHIRT = "Sweatshirt"

    SWEATER = "Sweater"

    BLOUSE = "Blouse"

    TANK_TOP = "Tank Top"

    CAMI = "Camisole"

    CROP_TOP = "Crop Top"

    KURTI = "Kurti"

class BottomType(str, Enum):

    JEANS = "Jeans"

    TROUSERS = "Trousers"

    SHORTS = "Shorts"

    SKIRT = "Skirt"

    LEGGINGS = "Leggings"

    JOGGERS = "Joggers"

    PALAZZO = "Palazzo"
    
class Color(str, Enum):

    BLACK = "Black"

    WHITE = "White"

    BLUE = "Blue"

    RED = "Red"

    GREEN = "Green"

    YELLOW = "Yellow"

    PINK = "Pink"

    PURPLE = "Purple"

    ORANGE = "Orange"

    BROWN = "Brown"

    GREY = "Grey"

    BEIGE = "Beige"

    NAVY = "Navy"

    OLIVE = "Olive"

    MAROON = "Maroon"

    CREAM = "Cream"
    
