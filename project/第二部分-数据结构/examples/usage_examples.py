"""
使用示例

展示各种数据结构的使用方法和实际应用场景。
"""

from src.queue import Queue
from src.stack import Stack
from src.deque import Deque
from src.priority_queue import PriorityQueue
from src.bounded import BoundedQueue, BoundedStack


def example_queue():
    """队列使用示例"""
    print("=" * 50)
    print("队列 (Queue) 使用示例")
    print("=" * 50)
    
    # 创建队列
    q = Queue[int]()
    
    # 入队
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(f"队列内容: {q}")
    print(f"队列长度: {len(q)}")
    
    # 查看队首
    print(f"队首元素: {q.peek()}")
    
    # 出队
    print(f"出队: {q.dequeue()}")
    print(f"出队: {q.dequeue()}")
    print(f"队列内容: {q}")
    
    # 使用特殊方法
    print(f"队列是否为空: {not bool(q)}")
    print(f"元素 3 是否在队列中: {3 in q}")


def example_stack():
    """栈使用示例"""
    print("\n" + "=" * 50)
    print("栈 (Stack) 使用示例")
    print("=" * 50)
    
    # 创建栈
    s = Stack[int]()
    
    # 入栈
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"栈内容: {s}")
    print(f"栈长度: {len(s)}")
    
    # 查看栈顶
    print(f"栈顶元素: {s.peek()}")
    
    # 出栈
    print(f"出栈: {s.pop()}")
    print(f"出栈: {s.pop()}")
    print(f"栈内容: {s}")


def example_deque():
    """双端队列使用示例"""
    print("\n" + "=" * 50)
    print("双端队列 (Deque) 使用示例")
    print("=" * 50)
    
    # 创建双端队列
    dq = Deque[int]()
    
    # 从两端添加元素
    dq.append_left(1)  # 左端
    dq.append(2)       # 右端
    dq.append_left(3)  # 左端
    dq.append(4)       # 右端
    print(f"双端队列内容: {dq}")
    
    # 从两端移除元素
    print(f"从左端移除: {dq.pop_left()}")
    print(f"从右端移除: {dq.pop()}")
    print(f"双端队列内容: {dq}")


def example_priority_queue():
    """优先级队列使用示例"""
    print("\n" + "=" * 50)
    print("优先级队列 (PriorityQueue) 使用示例")
    print("=" * 50)
    
    # 创建优先级队列
    pq = PriorityQueue[int]()
    
    # 插入元素（不按顺序）
    pq.push(5)
    pq.push(1)
    pq.push(3)
    pq.push(2)
    pq.push(4)
    print(f"优先级队列内容: {pq}")
    
    # 按优先级顺序取出
    print("按优先级顺序取出:")
    while not pq.is_empty():
        print(f"  {pq.pop()}")
    
    # 使用自定义优先级函数
    print("\n使用自定义优先级（按字符串长度）:")
    pq_str = PriorityQueue[str](key=lambda x: len(x))
    pq_str.push("apple")
    pq_str.push("pi")
    pq_str.push("banana")
    
    while not pq_str.is_empty():
        print(f"  {pq_str.pop()}")


def example_bounded():
    """有界队列和栈使用示例"""
    print("\n" + "=" * 50)
    print("有界队列和栈 (Bounded) 使用示例")
    print("=" * 50)
    
    # 创建有界队列
    bq = BoundedQueue[int](maxsize=3)
    bq.enqueue(1)
    bq.enqueue(2)
    bq.enqueue(3)
    print(f"有界队列: {bq}")
    print(f"是否已满: {bq.is_full()}")
    
    # 尝试添加更多元素会抛出异常
    try:
        bq.enqueue(4)
    except ValueError as e:
        print(f"错误: {e}")
    
    # 创建有界栈
    bs = BoundedStack[int](maxsize=2)
    bs.push(1)
    bs.push(2)
    print(f"有界栈: {bs}")
    print(f"是否已满: {bs.is_full()}")


def example_bfs():
    """使用队列实现广度优先搜索"""
    print("\n" + "=" * 50)
    print("应用示例: 广度优先搜索 (BFS)")
    print("=" * 50)
    
    # 简单的图结构
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [],
        6: []
    }
    
    def bfs(start):
        """广度优先搜索"""
        visited = set()
        q = Queue[int]()
        q.enqueue(start)
        visited.add(start)
        result = []
        
        while q:
            node = q.dequeue()
            result.append(node)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.enqueue(neighbor)
        
        return result
    
    print("从节点 1 开始的 BFS:")
    print(f"  遍历顺序: {bfs(1)}")


def example_balanced_parentheses():
    """使用栈检查括号匹配"""
    print("\n" + "=" * 50)
    print("应用示例: 括号匹配检查")
    print("=" * 50)
    
    def is_balanced(expression: str) -> bool:
        """检查括号是否匹配"""
        s = Stack[str]()
        pairs = {'(': ')', '[': ']', '{': '}'}
        
        for char in expression:
            if char in pairs:
                s.push(char)
            elif char in pairs.values():
                if s.is_empty():
                    return False
                opening = s.pop()
                if pairs[opening] != char:
                    return False
        
        return s.is_empty()
    
    test_cases = [
        "()",
        "()[]{}",
        "([{}])",
        "([)]",
        "(((",
        ""
    ]
    
    for expr in test_cases:
        result = is_balanced(expr)
        print(f"  '{expr}': {'匹配' if result else '不匹配'}")


def example_reverse_polish_notation():
    """使用栈计算逆波兰表达式"""
    print("\n" + "=" * 50)
    print("应用示例: 逆波兰表达式计算")
    print("=" * 50)
    
    def evaluate_rpn(tokens: list[str]) -> int:
        """计算逆波兰表达式"""
        s = Stack[int]()
        
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = s.pop()
                a = s.pop()
                if token == '+':
                    s.push(a + b)
                elif token == '-':
                    s.push(a - b)
                elif token == '*':
                    s.push(a * b)
                elif token == '/':
                    s.push(a // b)
            else:
                s.push(int(token))
        
        return s.pop()
    
    # 计算: (3 + 4) * 2 = 14
    # 逆波兰表达式: 3 4 + 2 *
    tokens = ["3", "4", "+", "2", "*"]
    result = evaluate_rpn(tokens)
    print(f"  表达式: {' '.join(tokens)}")
    print(f"  结果: {result}")


def run_all_examples():
    """运行所有示例"""
    example_queue()
    example_stack()
    example_deque()
    example_priority_queue()
    example_bounded()
    example_bfs()
    example_balanced_parentheses()
    example_reverse_polish_notation()
    
    print("\n" + "=" * 50)
    print("所有示例运行完成！")
    print("=" * 50)


if __name__ == '__main__':
    run_all_examples()

