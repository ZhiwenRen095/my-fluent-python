"""
在 Python 的世界里，“一切皆对象”这句话的完整表达应该是：“一切皆一等对象”。
使用高阶函数 make_averager
接受函数为参数，或者把函数作为结果返回的函数是高阶函数
"""


def make_averager():
    """
    简单来说，闭包（Closure） 是一种函数，
    它保留了在定义它时存在的“自由变量”的绑定。
    即便定义这些变量的作用域已经失效（函数已执行完毕），
    闭包依然可以访问这些变量。
    """
    series = []

    def averager(value):
        series.append(value)
        total = sum(series)
        return total / len(series)

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
