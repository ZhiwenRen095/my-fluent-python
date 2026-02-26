"""
生成第 n 个斐波纳契数，递归方式非常耗时
"""
import functools
from clockdemo import clock


# 使用缓存实现，速度更快
@functools.lru_cache(maxsize=8, typed=False)
@clock
def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(30))
