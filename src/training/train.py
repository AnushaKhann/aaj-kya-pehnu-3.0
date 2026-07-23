import torch
import torch.nn as nn
import torch.optim as optim

from pathlib import Path

from src.data.akp_dataset import AKPDataset
from src.data.transforms import get_train_transforms
from src.data.transforms import get_validation_transforms
from src.data.dataloader import create_dataloader
from src.training.checkpoint import (
    save_checkpoint,
    load_checkpoint,
)
from src.models.factory import build_model
from src.training.trainer import Trainer

def main():
    if torch.backends.mps.is_available():
        device = torch.device("mps")

    elif torch.cuda.is_available():
        device = torch.device("cuda")

    else:
        device = torch.device("cpu")

    print(f"Using device: {device}")
    dataset_dir = Path("data/processed/akp_v2")

    train_dataset = AKPDataset(
        dataset_dir=dataset_dir,
        csv_file="train.csv",
        transform=get_train_transforms(),
    )
    
    val_dataset = AKPDataset(
        dataset_dir=dataset_dir,
        csv_file="val.csv",
        transform=get_validation_transforms(),
    )
    
    train_loader = create_dataloader(
        train_dataset,
        batch_size=32,
        shuffle=True,
        num_workers=0,
    )
    
    val_loader = create_dataloader(
        val_dataset,
        batch_size=32,
        shuffle=False,
        num_workers=0,
    )
    print(f"Training samples: {len(train_dataset)}")
    print(f"Validation samples: {len(val_dataset)}")
    
    model = build_model(
        backbone="convnext",
        num_classes=train_dataset.label_encoder.num_classes(),
        )
    
    criterion = nn.CrossEntropyLoss()
    
    optimizer = optim.AdamW(
        model.parameters(),
        lr=1e-4,
        weight_decay=1e-4,
    )
    
    trainer = Trainer(
        model=model,
        train_loader=train_loader,
        val_loader=val_loader,
        criterion=criterion,
        optimizer=optimizer,
        device=device,
    )
    
    num_epochs = 10
    best_val_accuracy = 0.0
    
    checkpoint = load_checkpoint(
        model=model,
        optimizer=optimizer,
        filename="last_model.pth",
    )

    if checkpoint is not None:

        start_epoch = checkpoint["epoch"]

        best_val_accuracy = checkpoint["val_accuracy"]

        print(
            f"Resuming training from epoch {start_epoch + 1}"
        )
    

    else:

        start_epoch = 0

        best_val_accuracy = 0.0

        print("No checkpoint found. Starting fresh training.")
        
    if start_epoch >= num_epochs:
        print(
            f"Training already completed "
            f"({start_epoch}/{num_epochs} epochs)."
        )
        return
    
    
    
    for epoch in range(start_epoch, num_epochs):

        train_loss, train_accuracy = trainer.train_one_epoch()

        val_loss, val_accuracy = trainer.validate_one_epoch()

        print(
            f"Epoch [{epoch + 1}/{num_epochs}] "
            f"| Train Loss: {train_loss:.4f} "
            f"| Train Acc: {train_accuracy:.4f} "
            f"| Val Loss: {val_loss:.4f} "
            f"| Val Acc: {val_accuracy:.4f}"
        )

        save_checkpoint(
            model=model,
            optimizer=optimizer,
            epoch=epoch + 1,
            train_loss=train_loss,
            val_loss=val_loss,
            val_accuracy=val_accuracy,
            filename="last_model.pth",
        )

        if val_accuracy > best_val_accuracy:

            best_val_accuracy = val_accuracy

            save_checkpoint(
                model=model,
                optimizer=optimizer,
                epoch=epoch + 1,
                train_loss=train_loss,
                val_loss=val_loss,
                val_accuracy=val_accuracy,
                filename="best_model.pth",
            )

            print("Best model updated!")


if __name__ == "__main__":
    main()