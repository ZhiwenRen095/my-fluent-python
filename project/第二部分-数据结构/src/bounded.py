"""
有界队列和栈实现

基于《流畅的Python》的最佳实践，提供固定大小的队列和栈。
当达到容量上限时，会抛出异常或自动移除最旧的元素。
"""

from collections import deque
from typing import Generic, TypeVar, Iterator, Optional

from .queue import Queue
from .stack import Stack

T = TypeVar('T')


class BoundedQueue(Queue[T]):
    """
    有界队列实现
    
    继承自 Queue，但限制最大容量。当队列已满时，入队操作会抛出异常。
    
    Examples:
        >>> bq = BoundedQueue[int](maxsize=3)
        >>> bq.enqueue(1)
        >>> bq.enqueue(2)
        >>> bq.enqueue(3)
        >>> bq.enqueue(4)  # 会抛出 ValueError
    """
    
    def __init__(
        self, 
        maxsize: int,
        iterable: Optional[Iterator[T]] = None
    ) -> None:
        """
        初始化有界队列
        
        Args:
            maxsize: 队列的最大容量
            iterable: 可选的迭代器，用于初始化队列
            
        Raises:
            ValueError: 如果 maxsize <= 0
            ValueError: 如果 iterable 的长度超过 maxsize
        """
        if maxsize <= 0:
            raise ValueError("maxsize must be greater than 0")
        
        super().__init__(iterable)
        
        if len(self._items) > maxsize:
            raise ValueError(f"iterable length ({len(self._items)}) exceeds maxsize ({maxsize})")
        
        self._maxsize = maxsize
    
    def enqueue(self, item: T) -> None:
        """
        将元素添加到队列尾部（入队）
        
        Args:
            item: 要添加的元素
            
        Raises:
            ValueError: 当队列已满时
        """
        if len(self._items) >= self._maxsize:
            raise ValueError(f"queue is full (maxsize={self._maxsize})")
        super().enqueue(item)
    
    def is_full(self) -> bool:
        """
        检查队列是否已满
        
        Returns:
            如果队列已满返回 True，否则返回 False
        """
        return len(self._items) >= self._maxsize
    
    @property
    def maxsize(self) -> int:
        """返回队列的最大容量"""
        return self._maxsize
    
    def __repr__(self) -> str:
        """返回有界队列的字符串表示"""
        return f"BoundedQueue({list(self._items)}, maxsize={self._maxsize})"


class BoundedStack(Stack[T]):
    """
    有界栈实现
    
    继承自 Stack，但限制最大容量。当栈已满时，入栈操作会抛出异常。
    
    Examples:
        >>> bs = BoundedStack[int](maxsize=3)
        >>> bs.push(1)
        >>> bs.push(2)
        >>> bs.push(3)
        >>> bs.push(4)  # 会抛出 ValueError
    """
    
    def __init__(
        self, 
        maxsize: int,
        iterable: Optional[Iterator[T]] = None
    ) -> None:
        """
        初始化有界栈
        
        Args:
            maxsize: 栈的最大容量
            iterable: 可选的迭代器，用于初始化栈
            
        Raises:
            ValueError: 如果 maxsize <= 0
            ValueError: 如果 iterable 的长度超过 maxsize
        """
        if maxsize <= 0:
            raise ValueError("maxsize must be greater than 0")
        
        super().__init__(iterable)
        
        if len(self._items) > maxsize:
            raise ValueError(f"iterable length ({len(self._items)}) exceeds maxsize ({maxsize})")
        
        self._maxsize = maxsize
    
    def push(self, item: T) -> None:
        """
        将元素添加到栈顶（入栈）
        
        Args:
            item: 要添加的元素
            
        Raises:
            ValueError: 当栈已满时
        """
        if len(self._items) >= self._maxsize:
            raise ValueError(f"stack is full (maxsize={self._maxsize})")
        super().push(item)
    
    def is_full(self) -> bool:
        """
        检查栈是否已满
        
        Returns:
            如果栈已满返回 True，否则返回 False
        """
        return len(self._items) >= self._maxsize
    
    @property
    def maxsize(self) -> int:
        """返回栈的最大容量"""
        return self._maxsize
    
    def __repr__(self) -> str:
        """返回有界栈的字符串表示"""
        return f"BoundedStack({list(self._items)}, maxsize={self._maxsize})"

