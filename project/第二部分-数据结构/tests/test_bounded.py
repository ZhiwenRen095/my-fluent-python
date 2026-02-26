"""
有界队列和栈的单元测试

使用 unittest 框架测试 BoundedQueue 和 BoundedStack 类的所有功能。
"""

import unittest
from src.bounded import BoundedQueue, BoundedStack


class TestBoundedQueue(unittest.TestCase):
    """有界队列类的测试用例"""
    
    def test_basic_operations(self):
        """测试基本操作"""
        bq = BoundedQueue[int](maxsize=3)
        bq.enqueue(1)
        bq.enqueue(2)
        bq.enqueue(3)
        
        self.assertEqual(len(bq), 3)
        self.assertTrue(bq.is_full())
        self.assertEqual(bq.maxsize, 3)
    
    def test_enqueue_when_full(self):
        """测试队列已满时入队"""
        bq = BoundedQueue[int](maxsize=2)
        bq.enqueue(1)
        bq.enqueue(2)
        
        with self.assertRaises(ValueError):
            bq.enqueue(3)
    
    def test_invalid_maxsize(self):
        """测试无效的最大容量"""
        with self.assertRaises(ValueError):
            BoundedQueue[int](maxsize=0)
        
        with self.assertRaises(ValueError):
            BoundedQueue[int](maxsize=-1)
    
    def test_initialization_with_iterable(self):
        """测试使用可迭代对象初始化"""
        bq = BoundedQueue[int](maxsize=3, iterable=[1, 2, 3])
        self.assertEqual(len(bq), 3)
        self.assertTrue(bq.is_full())
    
    def test_initialization_exceeds_maxsize(self):
        """测试初始化时超过最大容量"""
        with self.assertRaises(ValueError):
            BoundedQueue[int](maxsize=2, iterable=[1, 2, 3])
    
    def test_is_full(self):
        """测试 is_full 方法"""
        bq = BoundedQueue[int](maxsize=2)
        self.assertFalse(bq.is_full())
        bq.enqueue(1)
        self.assertFalse(bq.is_full())
        bq.enqueue(2)
        self.assertTrue(bq.is_full())
    
    def test_dequeue_after_full(self):
        """测试队列满后出队再入队"""
        bq = BoundedQueue[int](maxsize=2)
        bq.enqueue(1)
        bq.enqueue(2)
        self.assertTrue(bq.is_full())
        
        bq.dequeue()
        self.assertFalse(bq.is_full())
        bq.enqueue(3)
        self.assertTrue(bq.is_full())


class TestBoundedStack(unittest.TestCase):
    """有界栈类的测试用例"""
    
    def test_basic_operations(self):
        """测试基本操作"""
        bs = BoundedStack[int](maxsize=3)
        bs.push(1)
        bs.push(2)
        bs.push(3)
        
        self.assertEqual(len(bs), 3)
        self.assertTrue(bs.is_full())
        self.assertEqual(bs.maxsize, 3)
    
    def test_push_when_full(self):
        """测试栈已满时入栈"""
        bs = BoundedStack[int](maxsize=2)
        bs.push(1)
        bs.push(2)
        
        with self.assertRaises(ValueError):
            bs.push(3)
    
    def test_invalid_maxsize(self):
        """测试无效的最大容量"""
        with self.assertRaises(ValueError):
            BoundedStack[int](maxsize=0)
        
        with self.assertRaises(ValueError):
            BoundedStack[int](maxsize=-1)
    
    def test_initialization_with_iterable(self):
        """测试使用可迭代对象初始化"""
        bs = BoundedStack[int](maxsize=3, iterable=[1, 2, 3])
        self.assertEqual(len(bs), 3)
        self.assertTrue(bs.is_full())
    
    def test_initialization_exceeds_maxsize(self):
        """测试初始化时超过最大容量"""
        with self.assertRaises(ValueError):
            BoundedStack[int](maxsize=2, iterable=[1, 2, 3])
    
    def test_is_full(self):
        """测试 is_full 方法"""
        bs = BoundedStack[int](maxsize=2)
        self.assertFalse(bs.is_full())
        bs.push(1)
        self.assertFalse(bs.is_full())
        bs.push(2)
        self.assertTrue(bs.is_full())
    
    def test_pop_after_full(self):
        """测试栈满后出栈再入栈"""
        bs = BoundedStack[int](maxsize=2)
        bs.push(1)
        bs.push(2)
        self.assertTrue(bs.is_full())
        
        bs.pop()
        self.assertFalse(bs.is_full())
        bs.push(3)
        self.assertTrue(bs.is_full())


if __name__ == '__main__':
    unittest.main()

