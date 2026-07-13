from pathlib import Path
import json


class FashionpediaAdapter:

    def __init__(self, annotation_file):

        self.annotation_file = Path(annotation_file)

        with open(self.annotation_file, "r") as f:
            self.data = json.load(f)
            
    def build_lookup_tables(self):

        self.category_lookup = {
            c["id"]: c["name"]
            for c in self.data["categories"]
        }

        self.attribute_lookup = {
            a["id"]: a["name"]
            for a in self.data["attributes"]
        }
        
    def get_annotation(self, index):

        ann = self.data["annotations"][index]

        category = self.category_lookup[
            ann["category_id"]
        ]

        attributes = [
            self.attribute_lookup[a]
            for a in ann["attribute_ids"]
        ]

        return {

            "image_id": ann["image_id"],

            "category": category,

            "attributes": attributes,

            "bbox": ann["bbox"],

            "segmentation": ann["segmentation"]

        }