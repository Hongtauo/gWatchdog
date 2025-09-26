# GPU Watchdog 🐕‍🦺

GPU Watchdog 是一个智能的 GPU 选择工具，可以自动检测系统中的 NVIDIA GPU，并选择具有最多空闲显存的 GPU 进行深度学习任务（适合有GPU集群但是不能多卡并行的高校深度学习服务器集群）

## 功能特点 ✨

- 🔍 **自动检测** - 自动扫描系统中所有可用的 NVIDIA GPU
- 📊 **显存分析** - 实时获取每块 GPU 的空闲显存和总显存信息
- 🎯 **智能选择** - 自动选择空闲显存最多的 GPU
- 🛡️ **容错处理** - 如果没有可用 GPU，自动回退到 CPU
- 💬 **详细日志** - 提供详细的 GPU 信息和选择过程日志

## 系统要求 📋

### 硬件要求

- NVIDIA GPU（支持 CUDA）
- 足够的系统内存

### 软件要求

- Python 3.7+
- NVIDIA 显卡驱动程序
- CUDA 工具包（可选，但推荐）

## 安装方法 🚀

### 1. 克隆仓库

```bash
git clone https://github.com/your-username/gWatchdog.git
cd gWatchdog
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 验证 NVIDIA 驱动

确保系统已正确安装 NVIDIA 驱动程序：

```bash
nvidia-smi
```

## 快速开始 🏃‍♂️

### 基本使用

```python
from gpuWatchDog import select_best_gpu

# 选择最优 GPU
device = select_best_gpu()
print(f"选择的设备: {device}")

# 在 PyTorch 中使用
import torch
tensor = torch.randn(3, 3).to(device)
```

### 深度学习模型中使用

```python
import torch
import torch.nn as nn
from gpuWatchDog import select_best_gpu

# 选择最优设备
device = select_best_gpu()

# 创建模型并移动到最优设备
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
).to(device)

# 训练数据也移动到相同设备
inputs = torch.randn(64, 784).to(device)
outputs = model(inputs)
```

## API 文档 📖

### `select_best_gpu()`

选择具有最多空闲显存的 GPU 设备。

**返回值:**

- `torch.device`: 最优 GPU 设备对象，如果没有可用 GPU 则返回 CPU 设备

**示例输出:**

```
GPU Memory Information (ID, Free Memory [MB], Total Memory [MB]):
GPU 0: 7823 MB free / 8192 MB total
GPU 1: 6144 MB free / 8192 MB total
Selecting GPU 0 with the most free memory.
```

## 使用示例 💡

运行完整的示例代码：

```bash
python example_usage.py
```

该示例包含以下场景：

1. **基本使用** - 简单的设备选择
2. **张量操作** - 将张量移动到最优设备
3. **神经网络** - 在深度学习模型中使用
4. **训练循环** - 完整的训练示例

## 故障排除 🔧

### 常见问题

**Q: 提示 "nvidia-smi not found"**
A: 请确保已正确安装 NVIDIA 显卡驱动程序，并且 `nvidia-smi` 命令在系统 PATH 中。

**Q: 函数返回 CPU 设备而不是 GPU**
A: 可能的原因：

- 系统没有 NVIDIA GPU
- NVIDIA 驱动程序未正确安装
- PyTorch 没有 CUDA 支持

**Q: 如何检查 PyTorch CUDA 支持？**
A: 运行以下代码：

```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
```

### 调试模式

如果遇到问题，可以手动运行 nvidia-smi 命令检查输出：

```bash
nvidia-smi --query-gpu=index,memory.free,memory.total --format=csv,noheader,nounits
```

## 贡献指南 🤝

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 许可证 📄

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 更新日志 📝

### v1.0.0

- 初始版本发布
- 支持自动 GPU 选择
- 支持显存信息显示
- 支持 CPU 回退机制

---

**⭐ 如果这个项目对你有帮助，请给它一个 Star！**
