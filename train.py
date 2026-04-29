import torch
import torch.nn as nn
import torch.optim as optim

from models.cnn_model import SimpleCNN
from utils.dataset import get_dataloader
from utils.train_utils import train_one_epoch, evaluate
from utils.visualize import plot_curves

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

train_loader, val_loader, classes = get_dataloader("data")

model = SimpleCNN(num_classes=len(classes)).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

losses = []
accuracies = []

for epoch in range(10):
    loss, train_acc = train_one_epoch(model, train_loader, criterion, optimizer, device)
    val_acc = evaluate(model, val_loader, device)

    losses.append(loss)
    accuracies.append(val_acc)

    print(f"Epoch {epoch+1} | Loss: {loss:.4f} | Train Acc: {train_acc:.4f} | Val Acc: {val_acc:.4f}")

torch.save(model.state_dict(), "checkpoints/model.pth")

plot_curves(losses, accuracies)
