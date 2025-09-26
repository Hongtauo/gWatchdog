import subprocess
import torch

def select_best_gpu():
    """
    获取 GPU 信息，并选择具有最多空闲显存的 GPU。
    如果未找到 GPU，则返回 CPU 设备。

    Returns:
        torch.device: 最优 GPU 的设备对象或 CPU 设备对象。
    """
    def get_gpu_memory_info():
        """获取每块 GPU 的显存信息"""
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=index,memory.free,memory.total', '--format=csv,noheader,nounits'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if result.returncode != 0:
                print(f"Error executing nvidia-smi: {result.stderr}")
                return []

            # 解析输出
            gpu_info = []
            output_lines = result.stdout.strip().split('\n')
            
            # 检查是否有有效输出
            if not output_lines or output_lines == ['']:
                return []
            
            for line in output_lines:
                if line.strip():  # 跳过空行
                    try:
                        index, free, total = map(int, line.split(', '))
                        gpu_info.append((index, free, total))
                    except ValueError:
                        print(f"Warning: Could not parse GPU info line: {line}")
                        continue
            return gpu_info
        except FileNotFoundError:
            print("nvidia-smi not found. Are you sure NVIDIA drivers are installed and accessible?")
            return []

    # 获取 GPU 信息
    gpu_info = get_gpu_memory_info()
    if gpu_info:
        print("GPU Memory Information (ID, Free Memory [MB], Total Memory [MB]):")
        for index, free, total in gpu_info:
            print(f"GPU {index}: {free} MB free / {total} MB total")

        # 按空闲内存排序
        gpu_info.sort(key=lambda x: x[1], reverse=True)

        # 选择空闲最多的 GPU
        selected_gpu = gpu_info[0][0]
        print(f"Selecting GPU {selected_gpu} with the most free memory.")

        # 返回设备
        return torch.device(f"cuda:{selected_gpu}")
    else:
        print("No GPU information available.")
        return torch.device("cpu")
