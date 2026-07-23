import torch
from pathlib import Path

CHECKPOINT_DIR = Path("models/checkpoints")
CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)


def save_checkpoint(
    model,
    optimizer,
    epoch,
    train_loss,
    val_loss,
    val_accuracy,
    filename,
):
    checkpoint = {
        "epoch": epoch,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
        "train_loss": train_loss,
        "val_loss": val_loss,
        "val_accuracy": val_accuracy,
    }

    torch.save(
        checkpoint,
        CHECKPOINT_DIR / filename,
    )
    
def load_checkpoint(
    model,
    optimizer,
    filename,
):
    checkpoint_path = CHECKPOINT_DIR / filename

    if not checkpoint_path.exists():
        return None

    checkpoint = torch.load(
        checkpoint_path,
        map_location="cpu",
    )

    try:
        model.load_state_dict(
            checkpoint["model_state_dict"]
        )

        optimizer.load_state_dict(
            checkpoint["optimizer_state_dict"]
        )

    except RuntimeError as e:
        print(f"Incompatible checkpoint: {e}")
        print("Starting fresh training...")
        return None

    return checkpoint