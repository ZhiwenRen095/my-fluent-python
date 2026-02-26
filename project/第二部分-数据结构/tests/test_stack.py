"""
栈的单元测试

使用 unittest 框架测试 Stack 类的所有功能。
"""

import unittest
from src import MyStack as Stack


class TestStack(unittest.TestCase):
    """栈类的测试用例"""

    def test_empty_stack(self):
        """测试空栈"""
        s = Stack[int]()
        self.assertTrue(s.is_empty())
        self.assertEqual(len(s), 0)
        self.assertFalse(bool(s))
        self.assertEqual(s.size(), 0)

    def test_push_pop(self):
        """测试入栈和出栈操作"""
        s = Stack[int]()
        s.push(1)
        s.push(2)
        s.push(3)

        self.assertEqual(len(s), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.is_empty())

    def test_peek(self):
        """测试查看栈顶元素"""
        s = Stack[int]()
        s.push(10)
        s.push(20)

        self.assertEqual(s.peek(), 20)
        self.assertEqual(len(s), 2)  # peek 不应该移除元素
        self.assertEqual(s.pop(), 20)
        self.assertEqual(s.peek(), 10)

    def test_pop_empty(self):
        """测试从空栈出栈"""
        s = Stack[int]()
        with self.assertRaises(IndexError):
            s.pop()

    def test_peek_empty(self):
        """测试查看空栈"""
        s = Stack[int]()
        with self.assertRaises(IndexError):
            s.peek()

    def test_len_special_method(self):
        """测试 __len__ 特殊方法"""
        s = Stack[int]()
        self.assertEqual(len(s), 0)
        s.push(1)
        self.assertEqual(len(s), 1)
        s.push(2)
        self.assertEqual(len(s), 2)

    def test_bool_special_method(self):
        """测试 __bool__ 特殊方法"""
        s = Stack[int]()
        self.assertFalse(bool(s))
        s.push(1)
        self.assertTrue(bool(s))

    def test_repr_special_method(self):
        """测试 __repr__ 特殊方法"""
        s = Stack[int]()
        self.assertEqual(repr(s), "Stack([])")
        s.push(1)
        s.push(2)
        self.assertEqual(repr(s), "Stack([1, 2])")

    def test_iter_special_method(self):
        """测试 __iter__ 特殊方法"""
        s = Stack[int]()
        s.push(1)
        s.push(2)
        s.push(3)

        items = list(s)
        self.assertEqual(items, [1, 2, 3])

        # 测试迭代后栈不变
        self.assertEqual(len(s), 3)

    def test_contains_special_method(self):
        """测试 __contains__ 特殊方法"""
        s = Stack[int]()
        s.push(1)
        s.push(2)
        s.push(3)

        self.assertIn(2, s)
        self.assertNotIn(4, s)

    def test_initialization_with_iterable(self):
        """测试使用可迭代对象初始化栈"""
        s = Stack[int]([1, 2, 3])
        self.assertEqual(len(s), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_lifo_order(self):
        """测试栈的 LIFO（后进先出）特性"""
        s = Stack[str]()
        s.push("first")
        s.push("second")
        s.push("third")

        self.assertEqual(s.pop(), "third")
        self.assertEqual(s.pop(), "second")
        self.assertEqual(s.pop(), "first")


if __name__ == '__main__':
    unittest.main()
