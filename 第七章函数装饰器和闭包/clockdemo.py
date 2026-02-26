"""
clock装饰器
"""
import functools
import time


def clock(func):
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
