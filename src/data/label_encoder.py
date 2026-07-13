from typing import List


class LabelEncoder:
    """
    Converts category names into numerical labels and back.
    """

    def __init__(self, class_names: List[str]):

        self.class_names = sorted(class_names)

        self.class_to_index = {
            name: idx
            for idx, name in enumerate(self.class_names)
        }

        self.index_to_class = {
            idx: name
            for idx, name in enumerate(self.class_names)
        }

    def encode(self, class_name):

        return self.class_to_index[class_name]

    def decode(self, index):

        return self.index_to_class[index]

    def num_classes(self):

        return len(self.class_names)