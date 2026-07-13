from .convnext import ConvNeXtClassifier


def build_model(
    backbone: str,
    num_classes: int
):

    backbone = backbone.lower()

    if backbone == "convnext":

        return ConvNeXtClassifier(num_classes)

    raise ValueError(
        f"Unknown backbone: {backbone}"
    )