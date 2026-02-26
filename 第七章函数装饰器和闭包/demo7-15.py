import time


def clock(func):
    """实现一个简单的装饰器, 输出函数的运行时间"""

    def clocked(*args):
        start = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - start
        func_name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
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
    snooze(3)
    ans = factorial(8)

    # 遮盖了被装饰函数的 __name__ 和 __doc__ 属性。
    print(factorial.__name__)
    print(factorial.__doc__)