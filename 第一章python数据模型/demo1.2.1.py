""" 自定义魔术方法 """
from __future__ import annotations
from math import hypot


class Vector:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x!r},{self.y!r})"

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> Vector:
        return Vector(self.x * scalar, self.y * scalar)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __abs__(self) -> float:
        return hypot(self.x, self.y)


if __name__ == '__main__':
    v1 = Vector(3, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)
    print(abs(v1))
    if v1:
        pass
