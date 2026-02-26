"""
示例 7-15 中实现的 clock 装饰器有几个缺点：
1.不支持关键字参数，
2.而且遮盖了被装饰函数的 __name__ 和 __doc__ 属性。
"""
import functools
import time


def clock(func):
    """使用functools.wraps 装饰器把相关的属性从 func 复制到 clocked 中"""

    @functools.wraps(func)
    def clocked(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start

        func_name = func.__name__

        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)

        print(f"[{elapsed:0.8f}s] {func_name}({arg_str}) -> {result!r}")

        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    """计算阶乘"""
    return 1 if n < 1 else n * factorial(n - 1)


if __name__ == '__main__':
    pass
    # snooze(3)
    # ans = factorial(8)
    #
    # print(factorial.__name__)
    # print(factorial.__doc__)
