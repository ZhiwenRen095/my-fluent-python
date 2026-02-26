"""
性能对比测试

对比使用 collections.deque 和 list 实现的性能差异。
"""

import time
from collections import deque as std_deque
from src.queue import Queue
from src.stack import Stack
from src.deque import Deque


def benchmark_queue_operations(n: int = 100000):
    """对比队列操作的性能"""
    print(f"\n队列操作性能测试 (n={n})")
    print("=" * 50)
    
    # 使用我们的 Queue（基于 deque）
    q = Queue[int]()
    start = time.perf_counter()
    for i in range(n):
        q.enqueue(i)
    for i in range(n):
        q.dequeue()
    elapsed_queue = time.perf_counter() - start
    print(f"Queue (基于 deque): {elapsed_queue:.4f} 秒")
    
    # 使用 list 实现队列（低效）
    q_list = []
    start = time.perf_counter()
    for i in range(n):
        q_list.append(i)  # O(1)
    for i in range(n):
        q_list.pop(0)  # O(n) - 低效！
    elapsed_list = time.perf_counter() - start
    print(f"List 实现: {elapsed_list:.4f} 秒")
    print(f"性能提升: {elapsed_list / elapsed_queue:.2f}x")


def benchmark_stack_operations(n: int = 100000):
    """对比栈操作的性能"""
    print(f"\n栈操作性能测试 (n={n})")
    print("=" * 50)
    
    # 使用我们的 Stack（基于 deque）
    s = Stack[int]()
    start = time.perf_counter()
    for i in range(n):
        s.push(i)
    for i in range(n):
        s.pop()
    elapsed_stack = time.perf_counter() - start
    print(f"Stack (基于 deque): {elapsed_stack:.4f} 秒")
    
    # 使用 list 实现栈（同样高效，因为都在尾部操作）
    s_list = []
    start = time.perf_counter()
    for i in range(n):
        s_list.append(i)  # O(1)
    for i in range(n):
        s_list.pop()  # O(1)
    elapsed_list = time.perf_counter() - start
    print(f"List 实现: {elapsed_list:.4f} 秒")
    print(f"性能差异: {elapsed_list / elapsed_stack:.2f}x")


def benchmark_deque_operations(n: int = 100000):
    """对比双端队列操作的性能"""
    print(f"\n双端队列操作性能测试 (n={n})")
    print("=" * 50)
    
    # 使用我们的 Deque
    dq = Deque[int]()
    start = time.perf_counter()
    for i in range(n):
        dq.append(i)
    for i in range(n):
        dq.append_left(i)
    for i in range(n):
        dq.pop()
    for i in range(n):
        dq.pop_left()
    elapsed_deque = time.perf_counter() - start
    print(f"Deque (基于 collections.deque): {elapsed_deque:.4f} 秒")
    
    # 使用标准库的 deque
    std_dq = std_deque()
    start = time.perf_counter()
    for i in range(n):
        std_dq.append(i)
    for i in range(n):
        std_dq.appendleft(i)
    for i in range(n):
        std_dq.pop()
    for i in range(n):
        std_dq.popleft()
    elapsed_std = time.perf_counter() - start
    print(f"标准库 deque: {elapsed_std:.4f} 秒")
    print(f"性能差异: {elapsed_deque / elapsed_std:.2f}x")


def benchmark_priority_queue_operations(n: int = 10000):
    """测试优先级队列的性能"""
    print(f"\n优先级队列操作性能测试 (n={n})")
    print("=" * 50)
    
    from src.priority_queue import PriorityQueue
    import random
    
    pq = PriorityQueue[int]()
    items = [random.randint(1, 1000) for _ in range(n)]
    
    start = time.perf_counter()
    for item in items:
        pq.push(item)
    elapsed_push = time.perf_counter() - start
    print(f"插入 {n} 个元素: {elapsed_push:.4f} 秒")
    
    start = time.perf_counter()
    while not pq.is_empty():
        pq.pop()
    elapsed_pop = time.perf_counter() - start
    print(f"删除 {n} 个元素: {elapsed_pop:.4f} 秒")
    print(f"总时间: {elapsed_push + elapsed_pop:.4f} 秒")


def run_all_benchmarks():
    """运行所有性能测试"""
    print("=" * 50)
    print("高性能数据结构性能测试")
    print("=" * 50)
    
    benchmark_queue_operations(100000)
    benchmark_stack_operations(100000)
    benchmark_deque_operations(50000)
    benchmark_priority_queue_operations(10000)
    
    print("\n" + "=" * 50)
    print("测试完成！")
    print("=" * 50)


if __name__ == '__main__':
    run_all_benchmarks()

