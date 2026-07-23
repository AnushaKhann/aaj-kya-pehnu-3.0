import torch


def calculate_correct_predictions(
    outputs: torch.Tensor,
    labels: torch.Tensor,
) -> tuple[int, int]:
    """
    Calculate the number of correct predictions in a batch.

    Args:
        outputs: Model logits of shape (batch_size, num_classes)
        labels: Ground truth labels of shape (batch_size,)

    Returns:
        Tuple containing:
            - correct_predictions
            - total_samples
    """

    predictions = outputs.argmax(dim=1)

    correct = (predictions == labels).sum().item()

    total = labels.size(0)

    return correct, total