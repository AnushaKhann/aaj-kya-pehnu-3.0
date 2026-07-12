"""
Maps labels from different datasets into our universal taxonomy.
"""

class LabelMapper:

    def __init__(self):
        self.mapping = {}

    def map_category(self, dataset_name, category):
        return self.mapping.get(dataset_name, {}).get(category, category)