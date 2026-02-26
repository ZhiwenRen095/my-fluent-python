from array import array
from datetime import datetime
from typing import Callable


def my_wrapper(func: Callable):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        end = datetime.now()
        print(f"{func.__name__}函数耗时：{end - start}s")

    return wrapper


@my_wrapper
def example():
    total: int = 10 ** 7
    gen = (i for i in range(total))
    floats = array('d', gen)
    print(floats[0])


if __name__ == '__main__':
    example()
