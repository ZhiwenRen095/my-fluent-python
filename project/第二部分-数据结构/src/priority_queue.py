"""
高性能优先级队列实现

基于《流畅的Python》的最佳实践，使用 heapq 模块作为底层实现，
提供 O(log n) 时间复杂度的插入和删除最小元素操作。
"""

import heapq
from typing import Generic, TypeVar, Iterator, Optional, Tuple, Callable

T = TypeVar('T')


class PriorityQueue(Generic[T]):
    """
    高性能优先级队列实现（最小堆）
    
    使用 heapq 模块作为底层数据结构，提供 O(log n) 的插入和删除操作。
    支持类型提示、迭代、以及多种特殊方法。
    
    Examples:
        >>> pq = PriorityQueue[int]()
        >>> pq.push(3)
        >>> pq.push(1)
        >>> pq.push(2)
        >>> pq.pop()
        1
        >>> pq.peek()
        2
    """

    def __init__(
            self,
            iterable: Optional[Iterator[T]] = None,
            key: Optional[Callable[[T], float]] = None
    ) -> None:
        """
        初始化优先级队列
        
        Args:
            iterable: 可选的迭代器，用于初始化优先级队列
            key: 可选的函数，用于提取元素的优先级（默认为元素本身）
        """
        self._items: list[Tuple[float, int, T]] = []
        self._counter = 0  # 用于处理相同优先级的元素
        self._key = key if key else lambda x: x

        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, item: T) -> None:
        """
        将元素添加到优先级队列
        
        Args:
            item: 要添加的元素
        """
        priority = self._key(item)
        heapq.heappush(self._items, (priority, self._counter, item))
        self._counter += 1

    def pop(self) -> T:
        """
        移除并返回优先级最高的元素（最小元素）
        
        Returns:
            优先级最高的元素
            
        Raises:
            IndexError: 当优先级队列为空时
        """
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        _, _, item = heapq.heappop(self._items)
        return item

    def peek(self) -> T:
        """
        查看优先级最高的元素，但不移除
        
        Returns:
            优先级最高的元素
            
        Raises:
            IndexError: 当优先级队列为空时
        """
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        _, _, item = self._items[0]
        return item

    def is_empty(self) -> bool:
        """
        检查优先级队列是否为空
        
        Returns:
            如果优先级队列为空返回 True，否则返回 False
        """
        return len(self._items) == 0

    def size(self) -> int:
        """
        返回优先级队列中元素的数量
        
        Returns:
            优先级队列中元素的数量
        """
        return len(self._items)

    def __len__(self) -> int:
        """返回优先级队列长度，支持 len() 函数"""
        return len(self._items)

    def __bool__(self) -> bool:
        """判断优先级队列是否非空，支持布尔上下文"""
        return len(self._items) > 0

    def __repr__(self) -> str:
        """返回优先级队列的字符串表示"""
        items = [item for _, _, item in self._items]
        return f"PriorityQueue({items})"

    def __iter__(self) -> Iterator[T]:
        """支持迭代（按优先级顺序）"""
        # 创建一个副本以避免修改原始堆
        temp_items = self._items.copy()
        while temp_items:
            _, _, item = heapq.heappop(temp_items)
            yield item

    def __contains__(self, item: T) -> bool:
        """支持 in 操作符检查元素是否存在"""
        return any(stored_item == item for _, _, stored_item in self._items)
