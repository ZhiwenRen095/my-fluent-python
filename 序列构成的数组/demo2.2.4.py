"""" 列表推导listcomps 和  生成式表达器genexps """
import psutil
import os
from tqdm import tqdm


def get_process_memory() -> float:
    """获取当前进程占用的物理内存 (MB)"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024


def my_test(symbols: str, is_listcomps: bool) -> float:
    mem_before = get_process_memory()

    a = [ord(s) for s in symbols] if is_listcomps else (ord(s) for s in symbols)

    mem_after = get_process_memory()
    return mem_after - mem_before


if __name__ == '__main__':
    # 设置测试参数
    epoch = 50
    is_listcomps = True
    symbols = '$¢£¥€¤' * 884800

    print(f"--- 测试模式: {'列表推导式' if is_listcomps else '生成器表达式'} ---")
    total_memory = []
    for _ in tqdm(range(epoch), desc="内存测试进度"):
        total_memory.append(my_test(symbols, is_listcomps))

    print(f"进程内存增量: {sum(total_memory) / epoch} MB")
