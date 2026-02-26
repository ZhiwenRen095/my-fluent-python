"""
双端队列的单元测试

使用 unittest 框架测试 Deque 类的所有功能。
"""

import unittest
from src.deque import Deque


class TestDeque(unittest.TestCase):
    """双端队列类的测试用例"""
    
    def test_empty_deque(self):
        """测试空双端队列"""
        dq = Deque[int]()
        self.assertTrue(dq.is_empty())
        self.assertEqual(len(dq), 0)
        self.assertFalse(bool(dq))
        self.assertEqual(dq.size(), 0)
    
    def test_append_pop(self):
        """测试右端操作"""
        dq = Deque[int]()
        dq.append(1)
        dq.append(2)
        dq.append(3)
        
        self.assertEqual(len(dq), 3)
        self.assertEqual(dq.pop(), 3)
        self.assertEqual(dq.pop(), 2)
        self.assertEqual(dq.pop(), 1)
        self.assertTrue(dq.is_empty())
    
    def test_append_left_pop_left(self):
        """测试左端操作"""
        dq = Deque[int]()
        dq.append_left(1)
        dq.append_left(2)
        dq.append_left(3)
        
        self.assertEqual(len(dq), 3)
        self.assertEqual(dq.pop_left(), 3)
        self.assertEqual(dq.pop_left(), 2)
        self.assertEqual(dq.pop_left(), 1)
        self.assertTrue(dq.is_empty())
    
    def test_mixed_operations(self):
        """测试混合操作"""
        dq = Deque[int]()
        dq.append_left(1)  # [1]
        dq.append(2)       # [1, 2]
        dq.append_left(3) # [3, 1, 2]
        dq.append(4)       # [3, 1, 2, 4]
        
        self.assertEqual(dq.pop_left(), 3)
        self.assertEqual(dq.pop(), 4)
        self.assertEqual(dq.pop_left(), 1)
        self.assertEqual(dq.pop(), 2)
    
    def test_peek(self):
        """测试查看右端元素"""
        dq = Deque[int]()
        dq.append(10)
        dq.append(20)
        
        self.assertEqual(dq.peek(), 20)
        self.assertEqual(len(dq), 2)
        self.assertEqual(dq.pop(), 20)
        self.assertEqual(dq.peek(), 10)
    
    def test_peek_left(self):
        """测试查看左端元素"""
        dq = Deque[int]()
        dq.append_left(10)
        dq.append_left(20)
        
        self.assertEqual(dq.peek_left(), 20)
        self.assertEqual(len(dq), 2)
        self.assertEqual(dq.pop_left(), 20)
        self.assertEqual(dq.peek_left(), 10)
    
    def test_pop_empty(self):
        """测试从空双端队列出队"""
        dq = Deque[int]()
        with self.assertRaises(IndexError):
            dq.pop()
        with self.assertRaises(IndexError):
            dq.pop_left()
    
    def test_peek_empty(self):
        """测试查看空双端队列"""
        dq = Deque[int]()
        with self.assertRaises(IndexError):
            dq.peek()
        with self.assertRaises(IndexError):
            dq.peek_left()
    
    def test_len_special_method(self):
        """测试 __len__ 特殊方法"""
        dq = Deque[int]()
        self.assertEqual(len(dq), 0)
        dq.append(1)
        self.assertEqual(len(dq), 1)
        dq.append_left(2)
        self.assertEqual(len(dq), 2)
    
    def test_bool_special_method(self):
        """测试 __bool__ 特殊方法"""
        dq = Deque[int]()
        self.assertFalse(bool(dq))
        dq.append(1)
        self.assertTrue(bool(dq))
    
    def test_repr_special_method(self):
        """测试 __repr__ 特殊方法"""
        dq = Deque[int]()
        self.assertEqual(repr(dq), "Deque([])")
        dq.append(1)
        dq.append(2)
        self.assertEqual(repr(dq), "Deque([1, 2])")
    
    def test_iter_special_method(self):
        """测试 __iter__ 特殊方法"""
        dq = Deque[int]()
        dq.append(1)
        dq.append(2)
        dq.append(3)
        
        items = list(dq)
        self.assertEqual(items, [1, 2, 3])
        self.assertEqual(len(dq), 3)
    
    def test_contains_special_method(self):
        """测试 __contains__ 特殊方法"""
        dq = Deque[int]()
        dq.append(1)
        dq.append(2)
        dq.append(3)
        
        self.assertIn(2, dq)
        self.assertNotIn(4, dq)
    
    def test_initialization_with_iterable(self):
        """测试使用可迭代对象初始化双端队列"""
        dq = Deque[int]([1, 2, 3])
        self.assertEqual(len(dq), 3)
        self.assertEqual(dq.pop(), 3)
        self.assertEqual(dq.pop_left(), 1)
        self.assertEqual(dq.pop(), 2)


if __name__ == '__main__':
    unittest.main()

