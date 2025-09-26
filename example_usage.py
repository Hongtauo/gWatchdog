import torch
from gpuWatchDog import select_best_gpu

# 示例 1: 基本使用
print("=== 示例 1: 基本使用 ===")
device = select_best_gpu()
print(f"选择的设备: {device}")

# 示例 2: 在模型中使用
print("\n=== 示例 2: 在模型中使用 ===")
device = select_best_gpu()

# 创建一个简单的张量
tensor = torch.randn(3, 3)
tensor = tensor.to(device)
print(f"张量被移动到设备: {tensor.device}")

# 示例 3: 在深度学习模型中使用
print("\n=== 示例 3: 在深度学习模型中使用 ===")
import torch.nn as nn

device = select_best_gpu()

# 创建一个简单的神经网络
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.linear = nn.Linear(10, 5)
    
    def forward(self, x):
        return self.linear(x)

model = SimpleNet()
model = model.to(device)
print(f"模型被移动到设备: {next(model.parameters()).device}")

# 创建输入数据
input_data = torch.randn(32, 10).to(device)
output = model(input_data)
print(f"输入数据形状: {input_data.shape}, 设备: {input_data.device}")
print(f"输出数据形状: {output.shape}, 设备: {output.device}")

# 示例 4: 在训练循环中使用
print("\n=== 示例 4: 在训练循环中使用 ===")
device = select_best_gpu()

# 模拟训练数据
batch_size = 64
input_size = 784
num_classes = 10

model = nn.Sequential(
    nn.Linear(input_size, 128),
    nn.ReLU(),
    nn.Linear(128, num_classes)
).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 模拟训练步骤
for epoch in range(3):
    # 模拟批次数据
    inputs = torch.randn(batch_size, input_size).to(device)
    targets = torch.randint(0, num_classes, (batch_size,)).to(device)
    
    # 前向传播
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    
    # 反向传播
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}, Device: {inputs.device}")

print("\n=== 示例完成 ===")