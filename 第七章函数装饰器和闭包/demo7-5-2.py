"""
变量作用域规则
b 是局部变量，因为在函数的定义体中给它赋值了
"""
from dis import dis

b = 6


def f2(a):
    """
    Python 编译函数的定义体时，它判断 b 是局部变量，
    因为在函数中给它赋值了
    Python 不要求声明变量，
    但是假定在函数定义体中赋值的变量是局部变量
    """
    global b
    print(a)
    print(b)
    b = 9


f2(3)
print(b)
print(dis(f2))
