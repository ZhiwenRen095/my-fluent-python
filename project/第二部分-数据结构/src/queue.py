"""
高性能队列实现

基于《流畅的Python》的最佳实践，使用 collections.deque 作为底层实现，
提供 O(1) 时间复杂度的入队/出队操作。
"""

from collections import deque
from typing import Generic, TypeVar, Iterator, Optional

T = TypeVar('T')


class Queue(Generic[T]):
    """
    高性能队列实现
    
    使用 collections.deque 作为底层数据结构，提供 O(1) 的入队和出队操作。
    支持类型提示、迭代、以及多种特殊方法。
    
    Examples:
        >>> q = Queue[int]()
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q.enqueue(3)
        >>> len(q)
        3
        >>> q.dequeue()
        1
        >>> q.peek()
        2
    """
    
    def __init__(self, iterable: Optional[Iterator[T]] = None) -> None:
        """
        初始化队列
        
        Args:
            iterable: 可选的迭代器，用于初始化队列
        """
        self._items: deque[T] = deque(iterable) if iterable else deque()
    
    def enqueue(self, item: T) -> None:
        """
        将元素添加到队列尾部（入队）
        
        Args:
            item: 要添加的元素
        """
        self._items.append(item)
    
    def dequeue(self) -> T:
        """
        从队列头部移除并返回元素（出队）
        
        Returns:
            队列头部的元素
            
        Raises:
            IndexError: 当队列为空时
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()
    
    def peek(self) -> T:
        """
        查看队列头部元素，但不移除
        
        Returns:
            队列头部的元素
            
        Raises:
            IndexError: 当队列为空时
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]
    
    def is_empty(self) -> bool:
        """
        检查队列是否为空
        
        Returns:
            如果队列为空返回 True，否则返回 False
        """
        return len(self._items) == 0
    
    def size(self) -> int:
        """
        返回队列中元素的数量
        
        Returns:
            队列中元素的数量
        """
        return len(self._items)
    
    def __len__(self) -> int:
        """返回队列长度，支持 len() 函数"""
        return len(self._items)
    
    def __bool__(self) -> bool:
        """判断队列是否非空，支持布尔上下文"""
        return len(self._items) > 0
    
    def __repr__(self) -> str:
        """返回队列的字符串表示"""
        return f"Queue({list(self._items)})"
    
    def __iter__(self) -> Iterator[T]:
        """支持迭代，从队列头部到尾部"""
        return iter(self._items)
    
    def __contains__(self, item: T) -> bool:
        """支持 in 操作符检查元素是否存在"""
        return item in self._items

