"""
装饰器的一大特性是，能把被装饰的函数替换成其他函数。
第二个特性是，装饰器在加载模块时立即执行。
"""

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    pass
