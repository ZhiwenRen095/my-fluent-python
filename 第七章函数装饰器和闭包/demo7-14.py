"""
对数字、字符串、元组等不可变类型来说，只能读取，不能更新。
如果尝试重新绑定，例如 count = count + 1，其实会隐式创建局部
变量 count。
这样，count 就不是自由变量了，因此不会保存在闭包中。
"""


def make_averager():
    """
    Python 3 引入了 nonlocal 声明。
    它的作用是把变量标记为自由变量，即使在函数中为变量赋予新值了，
    也会变成自由变量。
    如果为 nonlocal 声明的变量赋予新值，闭包中保存的绑定会更新。
    """
    count = 0
    total = 0

    def averager(value):
        nonlocal count, total
        count += 1
        total += value
        return total / count

    return averager


if __name__ == '__main__':
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(type(avg.__closure__))
    print(avg.__closure__)
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
