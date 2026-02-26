# 高性能数据结构实现

基于《流畅的Python》的最佳实践，实现的高性能数据结构集合，包括队列、栈、双端队列、优先级队列等。

## 特性

- **高性能**: 使用 `collections.deque` 和 `heapq` 作为底层实现，所有操作的时间复杂度为 O(1) 或 O(log n)
- **类型安全**: 支持类型提示（Type Hints）和泛型，提供更好的代码可读性和IDE支持
- **Pythonic**: 实现了多种特殊方法，支持 `len()`, `bool()`, `in`, `iter()` 等Python内置操作
- **完整测试**: 包含全面的单元测试，覆盖所有功能和边界情况
- **性能测试**: 提供性能对比测试，展示与标准实现的性能差异
- **实用示例**: 包含多个实际应用场景的使用示例

## 项目结构

```
python-data-structures/
├── src/
│   ├── __init__.py
│   ├── stack.py              # 栈实现
│   ├── queue.py              # 队列实现
│   ├── deque.py              # 双端队列实现
│   ├── priority_queue.py     # 优先级队列实现
│   └── bounded.py            # 有界版本实现
├── tests/
│   ├── __init__.py
│   ├── test_stack.py
│   ├── test_queue.py
│   ├── test_deque.py
│   ├── test_priority_queue.py
│   └── test_bounded.py
├── benchmarks/
│   └── performance_test.py   # 性能对比测试
├── examples/
│   └── usage_examples.py     # 使用示例
├── requirements.txt
└── README.md
```

## 安装和使用

### 基本使用

#### 队列（Queue）

队列遵循 FIFO（先进先出）原则。

```python
from src.queue import Queue

# 创建队列
q = Queue[int]()

# 入队
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# 查看队列
print(q)  # Queue([1, 2, 3])
print(len(q))  # 3

# 出队
print(q.dequeue())  # 1
print(q.dequeue())  # 2

# 查看队首元素（不移除）
print(q.peek())  # 3

# 检查是否为空
print(q.is_empty())  # False
print(q.size())  # 1
```

#### 栈（Stack）

栈遵循 LIFO（后进先出）原则。

```python
from src.stack import Stack

# 创建栈
s = Stack[int]()

# 入栈
s.push(1)
s.push(2)
s.push(3)

# 查看栈
print(s)  # Stack([1, 2, 3])
print(len(s))  # 3

# 出栈
print(s.pop())  # 3
print(s.pop())  # 2

# 查看栈顶元素（不移除）
print(s.peek())  # 1

# 检查是否为空
print(s.is_empty())  # False
print(s.size())  # 1
```

#### 双端队列（Deque）

双端队列支持在两端进行高效操作。

```python
from src.deque import Deque

# 创建双端队列
dq = Deque[int]()

# 从两端添加元素
dq.append_left(1)  # 左端
dq.append(2)       # 右端
dq.append_left(3)  # 左端

# 从两端移除元素
print(dq.pop_left())  # 3
print(dq.pop())       # 2
print(dq.peek_left()) # 1
```

#### 优先级队列（PriorityQueue）

优先级队列使用最小堆实现，支持自定义优先级函数。

```python
from src.priority_queue import PriorityQueue

# 创建优先级队列
pq = PriorityQueue[int]()

# 插入元素（不按顺序）
pq.push(5)
pq.push(1)
pq.push(3)

# 按优先级顺序取出（最小元素优先）
print(pq.pop())  # 1
print(pq.pop())  # 3
print(pq.pop())  # 5

# 使用自定义优先级函数
pq_str = PriorityQueue[str](key=lambda x: len(x))
pq_str.push("apple")
pq_str.push("pi")
pq_str.push("banana")

print(pq_str.pop())  # "pi" (最短)
print(pq_str.pop())  # "apple"
print(pq_str.pop())  # "banana"
```

#### 有界队列和栈（Bounded）

有界版本限制最大容量，防止无限增长。

```python
from src.bounded import BoundedQueue, BoundedStack

# 创建有界队列（最大容量为3）
bq = BoundedQueue[int](maxsize=3)
bq.enqueue(1)
bq.enqueue(2)
bq.enqueue(3)
print(bq.is_full())  # True

# 尝试添加更多元素会抛出异常
try:
    bq.enqueue(4)
except ValueError as e:
    print(f"错误: {e}")  # 错误: queue is full (maxsize=3)

# 有界栈类似
bs = BoundedStack[int](maxsize=2)
bs.push(1)
bs.push(2)
print(bs.is_full())  # True
```

### 特殊方法支持

所有数据结构都实现了多种特殊方法，支持Python的内置操作：

```python
# 使用 len() 获取长度
q = Queue[int]()
q.enqueue(1)
q.enqueue(2)
print(len(q))  # 2

# 使用 bool() 判断是否非空
if q:
    print("队列不为空")

# 使用 in 操作符检查元素
q.enqueue(3)
print(2 in q)  # True
print(4 in q)  # False

# 支持迭代
for item in q:
    print(item)  # 1, 2, 3

# 使用可迭代对象初始化
q2 = Queue[int]([1, 2, 3, 4])
print(list(q2))  # [1, 2, 3, 4]
```

### 类型提示

所有类都支持泛型，可以指定元素类型：

```python
# 整数队列
q_int = Queue[int]()

# 字符串队列
q_str = Queue[str]()

# 列表栈
s_list = Stack[list]()

# 自定义类型
from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

q_point = Queue[Point]()
q_point.enqueue(Point(1, 2))
```

## 性能特性

### 时间复杂度

- **队列 (Queue)**:
  - `enqueue()`: O(1)
  - `dequeue()`: O(1)
  - `peek()`: O(1)
  - `is_empty()`: O(1)
  - `size()`: O(1)

- **栈 (Stack)**:
  - `push()`: O(1)
  - `pop()`: O(1)
  - `peek()`: O(1)
  - `is_empty()`: O(1)
  - `size()`: O(1)

- **双端队列 (Deque)**:
  - `append()` / `append_left()`: O(1)
  - `pop()` / `pop_left()`: O(1)
  - `peek()` / `peek_left()`: O(1)

- **优先级队列 (PriorityQueue)**:
  - `push()`: O(log n)
  - `pop()`: O(log n)
  - `peek()`: O(1)

### 为什么使用 deque 而不是 list？

- `collections.deque` 在两端（头部和尾部）的插入和删除操作都是 O(1)
- Python 的 `list` 在头部插入/删除是 O(n)，因为需要移动所有元素
- 对于队列和栈这种主要在一端操作的数据结构，`deque` 提供了最佳性能

## 运行测试

### 运行所有测试

使用 Python 的 `unittest` 模块运行测试：

```bash
# 运行单个测试文件
python -m unittest tests.test_queue
python -m unittest tests.test_stack

# 运行所有测试
python -m unittest discover tests
```

或者使用 `pytest`（如果已安装）：

```bash
pytest tests/ -v
```

### 运行性能测试

```bash
python benchmarks/performance_test.py
```

### 运行使用示例

```bash
python examples/usage_examples.py
```

## 异常处理

当对空数据结构执行操作时，会抛出 `IndexError`：

```python
q = Queue[int]()
try:
    q.dequeue()
except IndexError as e:
    print(f"错误: {e}")  # 错误: dequeue from empty queue

s = Stack[int]()
try:
    s.peek()
except IndexError as e:
    print(f"错误: {e}")  # 错误: peek from empty stack
```

对于有界版本，当达到容量上限时会抛出 `ValueError`：

```python
bq = BoundedQueue[int](maxsize=2)
bq.enqueue(1)
bq.enqueue(2)
try:
    bq.enqueue(3)
except ValueError as e:
    print(f"错误: {e}")  # 错误: queue is full (maxsize=2)
```

## 设计理念

本实现遵循《流畅的Python》中的以下最佳实践：

1. **充分利用特殊方法**: 实现了 `__len__`, `__bool__`, `__repr__`, `__iter__`, `__contains__` 等特殊方法，使类更加Pythonic
2. **类型提示**: 使用 `typing.Generic` 和 `TypeVar` 实现泛型支持，提高代码可读性和类型安全性
3. **性能优先**: 选择 `collections.deque` 和 `heapq` 作为底层实现，确保所有操作的高性能
4. **清晰的API**: 方法命名清晰，文档字符串完整，易于理解和使用
5. **模块化设计**: 每个数据结构独立实现，便于维护和扩展

## 实际应用示例

### 使用队列实现广度优先搜索（BFS）

```python
from src.queue import Queue

def bfs(graph, start):
    """广度优先搜索"""
    visited = set()
    q = Queue[int]()
    q.enqueue(start)
    visited.add(start)
    
    while q:
        node = q.dequeue()
        print(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                q.enqueue(neighbor)
```

### 使用栈实现括号匹配

```python
from src.stack import Stack

def is_balanced(expression):
    """检查括号是否匹配"""
    s = Stack[str]()
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in pairs:
            s.push(char)
        elif char in pairs.values():
            if s.is_empty() or pairs[s.pop()] != char:
                return False
    
    return s.is_empty()
```

### 使用优先级队列实现 Dijkstra 算法

```python
from src.priority_queue import PriorityQueue

def dijkstra(graph, start):
    """Dijkstra 最短路径算法"""
    distances = {start: 0}
    pq = PriorityQueue[tuple[int, int]](key=lambda x: x[1])
    pq.push((start, 0))
    
    while not pq.is_empty():
        node, dist = pq.pop()
        for neighbor, weight in graph.get(node, []):
            new_dist = dist + weight
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                pq.push((neighbor, new_dist))
    
    return distances
```

更多示例请查看 `examples/usage_examples.py` 文件。

## 依赖

本项目主要使用 Python 标准库，无需额外安装依赖即可运行：

- `collections.deque` - 用于队列、栈、双端队列的底层实现
- `heapq` - 用于优先级队列的底层实现
- `typing` - 用于类型提示

可选依赖（用于测试和开发）：

- `pytest` - 测试框架
- `mypy` - 类型检查
- `black` - 代码格式化

## 许可证

本项目为学习练习项目，基于《流畅的Python》的实践。
