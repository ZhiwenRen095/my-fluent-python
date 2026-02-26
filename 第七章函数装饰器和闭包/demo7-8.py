"""
在 Python 中，__call__ 是一个非常特殊的魔法方法（Magic Method）。
它的核心作用是：让一个类的实例可以像函数一样被调用。
"""


class Average:
    def __init__(self):
        self.series = []

    def __call__(self, value):
        self.series.append(value)
        total = sum(self.series)
        return total / len(self.series)

if __name__ == '__main__':
    avg = Average()
    print(avg(10))
    print(avg(11))
    print(avg(12))
