"""
Callable 是 typing 模块提供的类型提示工具，用于表示可调用对象（函数、方法、lambda 等）。
Callable[[参数类型列表], 返回类型]
Callable[[T], float]
#        ^   ^
#        |   |
#        |   └─ 返回类型：float
#        └───── 参数类型列表：[T]
"""
import heapq
from typing import Generic, TypeVar, Iterator, Optional, Tuple, Callable

T = TypeVar('T')


class MyPriorityQueue(Generic[T]):
    def __init__(
            self,
            iterable: Optional[Iterator[T]] = None,
            key: Optional[Callable[[T], float]] = None
    ) -> None:
        self._items: list[Tuple[float, int, T]] = []  # [(priority, _counter, item)]
        self._counter: int = 0
        self._key: Callable[[T], float] = key if key else lambda x: x

        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, item: T) -> None:
        """
        将元素添加到优先级队列

        Args:
            item: 要添加的元素
        """
        priority = self._key(item)  # 计算优先级
        heapq.heappush(self._items, (priority, self._counter, item))  # heap底层根据元组比较大小
        self._counter += 1

    def pop(self) -> T:
        """
        返回堆顶元素并对剩余元素进行堆化heapify
        :return:
        """
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        _, _, item = heapq.heappop(self._items)
        return item

    def is_empty(self) -> bool:
        return len(self._items) == 0

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

    def size(self) -> int:
        return len(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"MyPriorityQueue({[item for _, _, item in self._items]})"

    def __bool__(self) -> bool:
        return self.size() > 0

    def __iter__(self) -> Iterator[T]:
        temp_items = self._items.copy()
        while temp_items:
            _, _, item = heapq.heappop(temp_items)
            yield item

    def __contains__(self, item: T) -> bool:
        return any(item == stored_item for _, _, stored_item in self._items)
