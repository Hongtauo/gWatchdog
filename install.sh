#!/bin/bash

# GPU Watchdog 安装脚本 (Linux/macOS)

echo "=== GPU Watchdog 安装向导 ==="

# 检查 Python 版本
echo "检查 Python 版本..."
python3 --version
if [ $? -ne 0 ]; then
    echo "错误: Python3 未安装"
    exit 1
fi

# 检查 nvidia-smi
echo "检查 NVIDIA 驱动程序..."
nvidia-smi --version
if [ $? -ne 0 ]; then
    echo "警告: nvidia-smi 未找到。请确保已安装 NVIDIA 驱动程序。"
    echo "Ubuntu/Debian 用户可以运行: sudo apt install nvidia-driver-xxx"
else
    echo "✓ NVIDIA 驱动程序检测成功"
fi

# 创建虚拟环境（可选）
read -p "是否创建虚拟环境? (y/n): " create_venv
if [ "$create_venv" = "y" ]; then
    echo "创建虚拟环境..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✓ 虚拟环境已创建并激活"
fi

# 安装依赖
echo "安装 Python 依赖包..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ 依赖包安装成功"
else
    echo "错误: 依赖包安装失败"
    exit 1
fi

# 验证安装
echo "验证安装..."
python3 -c "import torch; print(f'PyTorch 版本: {torch.__version__}'); print(f'CUDA 可用: {torch.cuda.is_available()}')"

if [ $? -eq 0 ]; then
    echo "✓ 安装验证成功"
    echo ""
    echo "=== 安装完成! ==="
    echo "你可以运行以下命令测试："
    echo "python3 example_usage.py"
else
    echo "错误: 安装验证失败"
    exit 1
fi