from collections import deque
from typing import Generic, TypeVar, Iterator, Optional

T = TypeVar('T')


class MyStack(Generic[T]):
    """高性能栈实现"""

    def __init__(self, iterable: Optional[Iterator[T]] = None) -> None:
        """
        初始化栈
        :param iterable: 可选的迭代器，用于初始化栈
        """
        self._items: deque[T] = deque(iterable) if iterable else deque()

    def push(self, item: T) -> None:
        """
        入栈
        :param item: 要入栈的元素
        :return:
        """
        self._items.append(item)

    def pop(self) -> T:
        """
        出栈
        :return: 弹出栈顶元素
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        """
        查看栈顶元素
        :return: 不出栈
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """
        判断栈是否为空
        :return:
        """
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return not self.is_empty()

    def __repr__(self) -> str:
        """返回栈的字符串表示"""
        return f"MyStack({list(self._items)})"

    def __iter__(self) -> Iterator[T]:
        """支持迭代，从栈底到栈顶"""
        return iter(self._items)

    def __contains__(self, item: T) -> bool:
        """支持 in 操作符检查元素是否存在"""
        return item in self._items
