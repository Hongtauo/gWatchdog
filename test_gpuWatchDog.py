# GPU Watchdog 测试脚本

from gpuWatchDog import select_best_gpu
import torch
import sys

def test_gpu_selection():
    """测试 GPU 选择功能"""
    print("=== GPU 选择测试 ===")
    try:
        device = select_best_gpu()
        print(f"✓ 成功选择设备: {device}")
        return True
    except Exception as e:
        print(f"✗ GPU 选择失败: {e}")
        return False

def test_torch_cuda():
    """测试 PyTorch CUDA 支持"""
    print("\n=== PyTorch CUDA 测试 ===")
    print(f"PyTorch 版本: {torch.__version__}")
    print(f"CUDA 可用: {torch.cuda.is_available()}")
    
    if torch.cuda.is_available():
        print(f"CUDA 版本: {torch.version.cuda}")
        print(f"可用 GPU 数量: {torch.cuda.device_count()}")
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
        return True
    else:
        print("警告: CUDA 不可用，将使用 CPU")
        return False

def test_memory_operations():
    """测试内存操作"""
    print("\n=== 内存操作测试 ===")
    try:
        device = select_best_gpu()
        
        # 创建测试张量
        test_tensor = torch.randn(1000, 1000)
        test_tensor = test_tensor.to(device)
        
        print(f"✓ 张量成功移动到: {test_tensor.device}")
        print(f"张量形状: {test_tensor.shape}")
        
        # 简单计算测试
        result = torch.mm(test_tensor, test_tensor.T)
        print(f"✓ 矩阵乘法计算成功，结果设备: {result.device}")
        
        return True
    except Exception as e:
        print(f"✗ 内存操作测试失败: {e}")
        return False

def run_all_tests():
    """运行所有测试"""
    print("开始运行 GPU Watchdog 测试套件...\n")
    
    tests = [
        ("GPU 选择", test_gpu_selection),
        ("PyTorch CUDA", test_torch_cuda),
        ("内存操作", test_memory_operations)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
                print(f"✓ {test_name} 测试通过")
            else:
                print(f"✗ {test_name} 测试失败")
        except Exception as e:
            print(f"✗ {test_name} 测试异常: {e}")
        
        print("-" * 50)
    
    print(f"\n=== 测试结果 ===")
    print(f"通过: {passed}/{total}")
    print(f"成功率: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("🎉 所有测试通过！GPU Watchdog 工作正常。")
        return 0
    else:
        print("⚠️  部分测试失败，请检查配置。")
        return 1

if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)