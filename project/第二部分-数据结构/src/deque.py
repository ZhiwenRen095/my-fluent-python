"""
高性能双端队列实现

基于《流畅的Python》的最佳实践，使用 collections.deque 作为底层实现，
提供 O(1) 时间复杂度的两端操作。
"""

from collections import deque as _deque
from typing import Generic, TypeVar, Iterator, Optional

T = TypeVar('T')


class Deque(Generic[T]):
    """
    高性能双端队列实现
    
    使用 collections.deque 作为底层数据结构，提供 O(1) 的两端操作。
    支持类型提示、迭代、以及多种特殊方法。
    
    Examples:
        >>> dq = Deque[int]()
        >>> dq.append_left(1)
        >>> dq.append(2)
        >>> dq.append(3)
        >>> len(dq)
        3
        >>> dq.pop_left()
        1
        >>> dq.pop()
        3
    """
    
    def __init__(self, iterable: Optional[Iterator[T]] = None) -> None:
        """
        初始化双端队列
        
        Args:
            iterable: 可选的迭代器，用于初始化双端队列
        """
        self._items: _deque[T] = _deque(iterable) if iterable else _deque()
    
    def append(self, item: T) -> None:
        """
        将元素添加到右端（尾部）
        
        Args:
            item: 要添加的元素
        """
        self._items.append(item)
    
    def append_left(self, item: T) -> None:
        """
        将元素添加到左端（头部）
        
        Args:
            item: 要添加的元素
        """
        self._items.appendleft(item)
    
    def pop(self) -> T:
        """
        从右端（尾部）移除并返回元素
        
        Returns:
            右端的元素
            
        Raises:
            IndexError: 当双端队列为空时
        """
        if self.is_empty():
            raise IndexError("pop from empty deque")
        return self._items.pop()
    
    def pop_left(self) -> T:
        """
        从左端（头部）移除并返回元素
        
        Returns:
            左端的元素
            
        Raises:
            IndexError: 当双端队列为空时
        """
        if self.is_empty():
            raise IndexError("pop_left from empty deque")
        return self._items.popleft()
    
    def peek(self) -> T:
        """
        查看右端（尾部）元素，但不移除
        
        Returns:
            右端的元素
            
        Raises:
            IndexError: 当双端队列为空时
        """
        if self.is_empty():
            raise IndexError("peek from empty deque")
        return self._items[-1]
    
    def peek_left(self) -> T:
        """
        查看左端（头部）元素，但不移除
        
        Returns:
            左端的元素
            
        Raises:
            IndexError: 当双端队列为空时
        """
        if self.is_empty():
            raise IndexError("peek_left from empty deque")
        return self._items[0]
    
    def is_empty(self) -> bool:
        """
        检查双端队列是否为空
        
        Returns:
            如果双端队列为空返回 True，否则返回 False
        """
        return len(self._items) == 0
    
    def size(self) -> int:
        """
        返回双端队列中元素的数量
        
        Returns:
            双端队列中元素的数量
        """
        return len(self._items)
    
    def __len__(self) -> int:
        """返回双端队列长度，支持 len() 函数"""
        return len(self._items)
    
    def __bool__(self) -> bool:
        """判断双端队列是否非空，支持布尔上下文"""
        return len(self._items) > 0
    
    def __repr__(self) -> str:
        """返回双端队列的字符串表示"""
        return f"Deque({list(self._items)})"
    
    def __iter__(self) -> Iterator[T]:
        """支持迭代，从左端到右端"""
        return iter(self._items)
    
    def __contains__(self, item: T) -> bool:
        """支持 in 操作符检查元素是否存在"""
        return item in self._items

