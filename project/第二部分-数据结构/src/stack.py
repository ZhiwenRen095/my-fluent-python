"""
高性能栈实现

基于《流畅的Python》的最佳实践，使用 collections.deque 作为底层实现，
提供 O(1) 时间复杂度的入栈/出栈操作。
"""

from collections import deque
from typing import Generic, TypeVar, Iterator, Optional

T = TypeVar('T')


class Stack(Generic[T]):
    """
    高性能栈实现
    
    使用 collections.deque 作为底层数据结构，提供 O(1) 的入栈和出栈操作。
    支持类型提示、迭代、以及多种特殊方法。
    
    Examples:
        >>> s = Stack[int]()
        >>> s.push(1)
        >>> s.push(2)
        >>> s.push(3)
        >>> len(s)
        3
        >>> s.pop()
        3
        >>> s.peek()
        2
    """
    
    def __init__(self, iterable: Optional[Iterator[T]] = None) -> None:
        """
        初始化栈
        
        Args:
            iterable: 可选的迭代器，用于初始化栈
        """
        self._items: deque[T] = deque(iterable) if iterable else deque()
    
    def push(self, item: T) -> None:
        """
        将元素添加到栈顶（入栈）
        
        Args:
            item: 要添加的元素
        """
        self._items.append(item)
    
    def pop(self) -> T:
        """
        从栈顶移除并返回元素（出栈）
        
        Returns:
            栈顶的元素
            
        Raises:
            IndexError: 当栈为空时
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> T:
        """
        查看栈顶元素，但不移除
        
        Returns:
            栈顶的元素
            
        Raises:
            IndexError: 当栈为空时
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """
        检查栈是否为空
        
        Returns:
            如果栈为空返回 True，否则返回 False
        """
        return len(self._items) == 0
    
    def size(self) -> int:
        """
        返回栈中元素的数量
        
        Returns:
            栈中元素的数量
        """
        return len(self._items)
    
    def __len__(self) -> int:
        """返回栈长度，支持 len() 函数"""
        return len(self._items)
    
    def __bool__(self) -> bool:
        """判断栈是否非空，支持布尔上下文"""
        return len(self._items) > 0
    
    def __repr__(self) -> str:
        """返回栈的字符串表示"""
        return f"Stack({list(self._items)})"
    
    def __iter__(self) -> Iterator[T]:
        """支持迭代，从栈底到栈顶"""
        return iter(self._items)
    
    def __contains__(self, item: T) -> bool:
        """支持 in 操作符检查元素是否存在"""
        return item in self._items

