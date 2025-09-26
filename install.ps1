# GPU Watchdog 安装脚本

# 检查 Python 版本
python --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "错误: Python 未安装或未添加到 PATH" -ForegroundColor Red
    exit 1
}

Write-Host "=== GPU Watchdog 安装向导 ===" -ForegroundColor Green

# 检查 nvidia-smi
Write-Host "检查 NVIDIA 驱动程序..." -ForegroundColor Yellow
nvidia-smi --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "警告: nvidia-smi 未找到。请确保已安装 NVIDIA 驱动程序。" -ForegroundColor Red
    Write-Host "你可以从以下地址下载: https://www.nvidia.com/drivers" -ForegroundColor Yellow
} else {
    Write-Host "✓ NVIDIA 驱动程序检测成功" -ForegroundColor Green
}

# 安装依赖
Write-Host "安装 Python 依赖包..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ 依赖包安装成功" -ForegroundColor Green
} else {
    Write-Host "错误: 依赖包安装失败" -ForegroundColor Red
    exit 1
}

# 验证安装
Write-Host "验证安装..." -ForegroundColor Yellow
python -c "import torch; print(f'PyTorch 版本: {torch.__version__}'); print(f'CUDA 可用: {torch.cuda.is_available()}')"

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ 安装验证成功" -ForegroundColor Green
    Write-Host ""
    Write-Host "=== 安装完成! ===" -ForegroundColor Green
    Write-Host "你可以运行以下命令测试："
    Write-Host "python example_usage.py" -ForegroundColor Cyan
} else {
    Write-Host "错误: 安装验证失败" -ForegroundColor Red
    exit 1
}