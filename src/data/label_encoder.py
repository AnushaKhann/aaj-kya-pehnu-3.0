from typing import List


class LabelEncoder:
    """
    Converts category names into numerical labels and back.
    """

from typing import Dict, List, Optional


class LabelEncoder:
    """
    Converts category names into numerical labels and back.
    """

    def __init__(
        self,
        class_names: Optional[List[str]] = None,
        class_mapping: Optional[Dict[str, int]] = None
    ):

        if class_mapping is not None:
            self.class_to_index = class_mapping

            self.index_to_class = {
                idx: name
                for name, idx in class_mapping.items()
            }

            self.class_names = [
                self.index_to_class[i]
                for i in range(len(self.index_to_class))
            ]

        elif class_names is not None:
            self.class_names = sorted(class_names)

            self.class_to_index = {
                name: idx
                for idx, name in enumerate(self.class_names)
            }

            self.index_to_class = {
                idx: name
                for idx, name in enumerate(self.class_names)
            }

        else:
            raise ValueError(
                "Provide either class_names or class_mapping."
            )

    def encode(self, class_name):

        return self.class_to_index[class_name]

    def decode(self, index):

        return self.index_to_class[index]

    def num_classes(self):

        return len(self.class_names)