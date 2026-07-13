"""
category_filter.py

Filters Fashionpedia annotations and keeps
only wardrobe-relevant categories.
"""

from typing import List, Dict

from .taxonomy_mapper import (
    map_category,
    is_supported,
)

class CategoryFilter:

    def __init__(self):
        pass

    def filter_annotations(
        self,
        annotations: List[Dict]
    ) -> List[Dict]:

        filtered = []

        for ann in annotations:

            category = ann["category"]

            if not is_supported(category):
                continue

            ann["akp_category"] = map_category(category)

            filtered.append(ann)

        return filtered