"""
函数装饰器用于在源码中“标记”函数，以某种方式增强函数的行为。
这是一项强大的功能，但是若想掌握，必须理解闭包。
"""


def deco(func):
    def inner():
        print('second, running inner()')
    func()
    return inner

@deco
def target():
    print('first, running target()')

if __name__ == '__main__':
    target()


