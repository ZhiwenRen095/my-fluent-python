"""
队列的单元测试

使用 unittest 框架测试 Queue 类的所有功能。
"""

import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    """队列类的测试用例"""
    
    def test_empty_queue(self):
        """测试空队列"""
        q = Queue[int]()
        self.assertTrue(q.is_empty())
        self.assertEqual(len(q), 0)
        self.assertFalse(bool(q))
        self.assertEqual(q.size(), 0)
    
    def test_enqueue_dequeue(self):
        """测试入队和出队操作"""
        q = Queue[int]()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        
        self.assertEqual(len(q), 3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertTrue(q.is_empty())
    
    def test_peek(self):
        """测试查看队首元素"""
        q = Queue[int]()
        q.enqueue(10)
        q.enqueue(20)
        
        self.assertEqual(q.peek(), 10)
        self.assertEqual(len(q), 2)  # peek 不应该移除元素
        self.assertEqual(q.dequeue(), 10)
        self.assertEqual(q.peek(), 20)
    
    def test_dequeue_empty(self):
        """测试从空队列出队"""
        q = Queue[int]()
        with self.assertRaises(IndexError):
            q.dequeue()
    
    def test_peek_empty(self):
        """测试查看空队列"""
        q = Queue[int]()
        with self.assertRaises(IndexError):
            q.peek()
    
    def test_len_special_method(self):
        """测试 __len__ 特殊方法"""
        q = Queue[int]()
        self.assertEqual(len(q), 0)
        q.enqueue(1)
        self.assertEqual(len(q), 1)
        q.enqueue(2)
        self.assertEqual(len(q), 2)
    
    def test_bool_special_method(self):
        """测试 __bool__ 特殊方法"""
        q = Queue[int]()
        self.assertFalse(bool(q))
        q.enqueue(1)
        self.assertTrue(bool(q))
    
    def test_repr_special_method(self):
        """测试 __repr__ 特殊方法"""
        q = Queue[int]()
        self.assertEqual(repr(q), "Queue([])")
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(repr(q), "Queue([1, 2])")
    
    def test_iter_special_method(self):
        """测试 __iter__ 特殊方法"""
        q = Queue[int]()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        
        items = list(q)
        self.assertEqual(items, [1, 2, 3])
        
        # 测试迭代后队列不变
        self.assertEqual(len(q), 3)
    
    def test_contains_special_method(self):
        """测试 __contains__ 特殊方法"""
        q = Queue[int]()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        
        self.assertIn(2, q)
        self.assertNotIn(4, q)
    
    def test_initialization_with_iterable(self):
        """测试使用可迭代对象初始化队列"""
        q = Queue[int]([1, 2, 3])
        self.assertEqual(len(q), 3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
    
    def test_fifo_order(self):
        """测试队列的 FIFO（先进先出）特性"""
        q = Queue[str]()
        q.enqueue("first")
        q.enqueue("second")
        q.enqueue("third")
        
        self.assertEqual(q.dequeue(), "first")
        self.assertEqual(q.dequeue(), "second")
        self.assertEqual(q.dequeue(), "third")


if __name__ == '__main__':
    unittest.main()

