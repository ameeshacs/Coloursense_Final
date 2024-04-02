import torchvision.models as models
import torchvision.transforms as transforms
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
import preprocess as p
import os
from efficientnet_pytorch import EfficientNet
import torch
from torch.utils.data import random_split
import torch.nn as nn



# Check if CUDA (GPU support) is available
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

# Data loading
transform_train = transforms.Compose([
    transforms.RandomResizedCrop(size=(256, 256), scale=(0.5, 1.0), ratio=(3 / 4, 4 / 3)),
    transforms.Resize((256, 256)),  # Resize images to match model input size
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Normalize images
])

koln50_preprocessed = 'C:\Users\ASUS\OneDrive\Desktop\FinalYear\FYP\FYP_Impl\ColourSense\koln50_preprocessed'   # Replace "/path/to/koln50_preprocessed" with the actual path

transform_test = transforms.Compose([ 
    transforms.Resize((256, 256)), 
    transforms.ToTensor(), 
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]) 
])

train_dataset = ImageFolder(root=os.path.join(koln50_preprocessed, 'train'), transform=transform_train)
# dataset_size = len(train_dataset)
# train_size = int(dataset_size * 0.9)
# val_size = dataset_size - train_size
# train_dataset_jin, val_dataset_jin = random_split(train_dataset, [train_size, val_size])
train_loader = DataLoader(train_dataset, batch_size=10, shuffle=True, num_workers=4)

test_dataset = ImageFolder(root=os.path.join(koln50_preprocessed, 'test'), transform=transform_test)
test_loader = DataLoader(test_dataset, batch_size=10, shuffle=False, num_workers=4)

# Model Initialization
mobilenet = models.mobilenet_v2(pretrained=True)
efficientnet = EfficientNet.from_pretrained('efficientnet-b0')  # Initialize EfficientNet-B0
resnet = models.resnet18(pretrained=True)

# Move models to device
mobilenet.to(device)
efficientnet.to(device)
resnet.to(device)

# Model Training
optimizer_mobilenet = optim.Adam(mobilenet.parameters(), lr=0.001)
optimizer_efficientnet = optim.Adam(efficientnet.parameters(), lr=0.001)
optimizer_resnet = optim.Adam(resnet.parameters(), lr=0.001)

num_epochs = 25
# Define the loss function
criterion = nn.CrossEntropyLoss()

for epoch in range(num_epochs):
    # Training loop for MobileNet
    mobilenet.train()
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer_mobilenet.zero_grad()
        outputs = mobilenet(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer_mobilenet.step()

    # Training loop for EfficientNet
    efficientnet.train()
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer_efficientnet.zero_grad()
        outputs = efficientnet(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer_efficientnet.step()

# Model Evaluation
mobilenet.eval()
efficientnet.eval()
resnet.eval()

correct_mobilenet = 0
correct_efficientnet = 0
correct_resnet = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        
        # Evaluation for MobileNet
        outputs_mobilenet = mobilenet(images)
        _, predicted_mobilenet = torch.max(outputs_mobilenet.data, 1)
        correct_mobilenet += (predicted_mobilenet == labels).sum().item()

        # Evaluation for EfficientNet
        outputs_efficientnet = efficientnet(images)
        _, predicted_efficientnet = torch.max(outputs_efficientnet.data, 1)
        correct_efficientnet += (predicted_efficientnet == labels).sum().item()

        # Evaluation for ResNet
        outputs_resnet = resnet(images)
        _, predicted_resnet = torch.max(outputs_resnet.data, 1)
        correct_resnet += (predicted_resnet == labels).sum().item()

        total += labels.size(0)

accuracy_mobilenet = correct_mobilenet / total
accuracy_efficientnet = correct_efficientnet / total
accuracy_resnet = correct_resnet / total

print('Accuracy of MobileNet on the test images: {:.2f}%'.format(100 * accuracy_mobilenet))
print('Accuracy of EfficientNet on the test images: {:.2f}%'.format(100 * accuracy_efficientnet))
print('Accuracy of ResNet on the test images: {:.2f}%'.format(100 * accuracy_resnet))
