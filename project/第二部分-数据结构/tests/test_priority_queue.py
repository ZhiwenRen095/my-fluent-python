"""
优先级队列的单元测试

使用 unittest 框架测试 PriorityQueue 类的所有功能。
"""

import unittest
from src import MyPriorityQueue as PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    """优先级队列类的测试用例"""

    def test_empty_priority_queue(self):
        """测试空优先级队列"""
        pq = PriorityQueue[int]()
        self.assertTrue(pq.is_empty())
        self.assertEqual(len(pq), 0)
        self.assertFalse(bool(pq))
        self.assertEqual(pq.size(), 0)

    def test_push_pop(self):
        """测试插入和删除操作"""
        pq = PriorityQueue[int]()
        pq.push(3)
        pq.push(1)
        pq.push(2)

        self.assertEqual(pq.pop(), 1)  # 最小元素
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 3)
        self.assertTrue(pq.is_empty())

    def test_peek(self):
        """测试查看最小元素"""
        pq = PriorityQueue[int]()
        pq.push(3)
        pq.push(1)
        pq.push(2)

        self.assertEqual(pq.peek(), 1)
        self.assertEqual(len(pq), 3)  # peek 不应该移除元素
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.peek(), 2)

    def test_pop_empty(self):
        """测试从空优先级队列删除"""
        pq = PriorityQueue[int]()
        with self.assertRaises(IndexError):
            pq.pop()

    def test_peek_empty(self):
        """测试查看空优先级队列"""
        pq = PriorityQueue[int]()
        with self.assertRaises(IndexError):
            pq.peek()

    def test_custom_key(self):
        """测试自定义优先级函数"""
        pq = PriorityQueue[str](key=lambda x: len(x))
        pq.push("aaa")  # 优先级 3
        pq.push("b")  # 优先级 1
        pq.push("cc")  # 优先级 2

        self.assertEqual(pq.pop(), "b")  # 最短的
        self.assertEqual(pq.pop(), "cc")
        self.assertEqual(pq.pop(), "aaa")

    def test_same_priority(self):
        """测试相同优先级的元素"""
        pq = PriorityQueue[int]()
        pq.push(1)
        pq.push(1)
        pq.push(1)

        # 应该按照插入顺序返回（FIFO）
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 1)

    def test_len_special_method(self):
        """测试 __len__ 特殊方法"""
        pq = PriorityQueue[int]()
        self.assertEqual(len(pq), 0)
        pq.push(1)
        self.assertEqual(len(pq), 1)
        pq.push(2)
        self.assertEqual(len(pq), 2)

    def test_bool_special_method(self):
        """测试 __bool__ 特殊方法"""
        pq = PriorityQueue[int]()
        self.assertFalse(bool(pq))
        pq.push(1)
        self.assertTrue(bool(pq))

    def test_iter_special_method(self):
        """测试 __iter__ 特殊方法"""
        pq = PriorityQueue[int]()
        pq.push(3)
        pq.push(1)
        pq.push(2)

        items = list(pq)
        self.assertEqual(sorted(items), [1, 2, 3])
        # 迭代后优先级队列应该不变
        self.assertEqual(len(pq), 3)

    def test_contains_special_method(self):
        """测试 __contains__ 特殊方法"""
        pq = PriorityQueue[int]()
        pq.push(1)
        pq.push(2)
        pq.push(3)

        self.assertIn(2, pq)
        self.assertNotIn(4, pq)

    def test_initialization_with_iterable(self):
        """测试使用可迭代对象初始化优先级队列"""
        pq = PriorityQueue[int]([3, 1, 2])
        self.assertEqual(len(pq), 3)
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 3)


if __name__ == '__main__':
    unittest.main()
