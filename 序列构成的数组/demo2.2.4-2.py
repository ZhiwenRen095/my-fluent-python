import psutil
import os
from tqdm import tqdm


def get_process_memory() -> float:
    """获取当前进程占用的物理内存 (MB)"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024


def my_test(colors: list[str], sizes: list[str]) -> float:
    prev: float = get_process_memory()

    for _ in ((c, s) for c in colors for s in sizes):
        pass

    return get_process_memory() - prev

def my_test2(colors: list[str], sizes: list[str]) -> float:
    prev: float = get_process_memory()

    for _ in  [(color, size) for color in colors for size in sizes]:
        pass

    return get_process_memory() - prev


if __name__ == '__main__':
    epoch = 100
    colors = ['black', 'white'] * 500
    sizes = ['S', 'M', 'L'] * 500

    # 列表推导式测试
    total_memory_list = []
    for _ in tqdm(range(epoch), desc="列表推导式"):
        total_memory_list.append(my_test2(colors, sizes))

    print(f"列表推导式平均内存增量: {sum(total_memory_list)/epoch:.6f} MB")

    # 生成器表达式测试
    total_memory_gen = []
    for _ in tqdm(range(epoch), desc="生成器表达式"):
        total_memory_gen.append(my_test(colors, sizes))

    print(f"生成器表达式平均内存增量: {sum(total_memory_gen)/epoch:.6f} MB")

