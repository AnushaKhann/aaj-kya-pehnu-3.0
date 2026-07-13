import torch.nn as nn
from torchvision.models import (
    convnext_tiny,
    ConvNeXt_Tiny_Weights
)

from .base_model import BaseFashionModel


class ConvNeXtClassifier(BaseFashionModel):

    def __init__(self, num_classes):

        super().__init__()

        self.model = convnext_tiny(
            weights=ConvNeXt_Tiny_Weights.DEFAULT
        )

        in_features = self.model.classifier[-1].in_features

        self.model.classifier[-1] = nn.Linear(
            in_features,
            num_classes
        )

    def forward(self, x):

        return self.model(x)

    def get_backbone_name(self):

        return "ConvNeXt Tiny"