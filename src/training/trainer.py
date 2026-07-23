import torch
from torch.utils.data import DataLoader

from src.training.metrics import calculate_correct_predictions


class Trainer:
    def __init__(
        self,
        model,
        train_loader: DataLoader,
        val_loader: DataLoader,
        criterion,
        optimizer,
        device,
    ):
        self.model = model
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.criterion = criterion
        self.optimizer = optimizer
        self.device = device

        self.model.to(self.device)

    def train_one_epoch(self):
        return self._run_epoch(
            dataloader=self.train_loader,
            training=True,
        )

    def validate_one_epoch(self):
        return self._run_epoch(
            dataloader=self.val_loader,
            training=False,
        )

    def _run_epoch(
        self,
        dataloader: DataLoader,
        training: bool,
    ):
        if training:
            self.model.train()
        else:
            self.model.eval()

        running_loss = 0.0
        correct_predictions = 0
        total_samples = 0

        if training:

            for images, labels in dataloader:

                images = images.to(self.device)
                labels = labels.to(self.device)

                self.optimizer.zero_grad()

                outputs = self.model(images)

                loss = self.criterion(outputs, labels)

                loss.backward()

                self.optimizer.step()

                running_loss += loss.item()

                correct, total = calculate_correct_predictions(
                    outputs,
                    labels,
                )

                correct_predictions += correct
                total_samples += total

        else:

            with torch.no_grad():

                for images, labels in dataloader:

                    images = images.to(self.device)
                    labels = labels.to(self.device)

                    outputs = self.model(images)

                    loss = self.criterion(outputs, labels)

                    running_loss += loss.item()

                    correct, total = calculate_correct_predictions(
                        outputs,
                        labels,
                    )

                    correct_predictions += correct
                    total_samples += total

        average_loss = running_loss / len(dataloader)
        accuracy = correct_predictions / total_samples

        return average_loss, accuracy