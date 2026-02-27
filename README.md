# Fluent Python 学习笔记

本书《流畅的Python (Fluent Python)》的学习代码仓库，包含各章节示例代码和实践项目。

## 项目结构

```
fluent-python/
├── 第一章python数据模型/      # Python数据模型相关示例
├── 第二章数据结构/            # 数据结构相关示例
├── 第三章字典和集合/          # 字典和集合的使用
├── 第五章一等函数/            # 函数作为一等对象
├── 第六章使用一等函数实现设计模式/  # 函数式设计模式
├── 第七章函数装饰器和闭包/    # 装饰器与闭包
├── 第八章对象引用/            # 对象引用与垃圾回收
├── 第九章符合Python风格的对象/ # Pythonic类设计
├── 第14章可迭代的对象、迭代器和生成器/  # 迭代器与生成器
├── 序列构成的数组/            # 序列类型深入
├── sketch/                   # 代码草稿和练习
└── project/                  # 实践项目
    └── 第二部分-数据结构/    # 高性能数据结构实现
```

## 实践项目：数据结构

`project/第二部分-数据结构/` 包含基于《流畅的Python》最佳实践实现的高性能数据结构：

- **Queue** - 先进先出队列 (FIFO)
- **Stack** - 后进先出栈 (LIFO)
- **Deque** - 双端队列
- **PriorityQueue** - 优先级队列
- **BoundedQueue/Stack** - 有界版本

特性：
- 使用 `collections.deque` 实现 O(1) 操作
- 完整的类型提示支持
- 实现 Python 特殊方法 (`__len__`, `__iter__`, `__contains__` 等)
- 完整的单元测试

## 环境要求

- Python 3.8+

## 快速开始

```bash
# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# 运行数据结构测试
cd project/第二部分-数据结构
python -m pytest tests/ -v
```

## 学习进度

- [x] 第一章 - Python数据模型
- [x] 第二章 - 数据结构
- [x] 第三章 - 字典和集合
- [x] 第五章 - 一等函数
- [x] 第六章 - 函数式设计模式
- [x] 第七章 - 装饰器与闭包
- [x] 第八章 - 对象引用
- [x] 第九章 - Python风格的对象
- [x] 第14章 - 迭代器与生成器
