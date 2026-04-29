import torch
from PIL import Image
from torchvision import transforms
from models.cnn_model import SimpleCNN

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

classes = ["class0", "class1", "class2"]  # 改成你的类别

model = SimpleCNN(num_classes=len(classes))
model.load_state_dict(torch.load("checkpoints/model.pth"))
model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

img = Image.open("test.jpg").convert("RGB")
img = transform(img).unsqueeze(0).to(device)

output = model(img)
_, predicted = torch.max(output, 1)

print("Prediction:", classes[predicted.item()])
