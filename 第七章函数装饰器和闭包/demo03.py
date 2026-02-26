"""
导入demo02,装饰器演示第二个特性
第二个特性是，装饰器在加载模块时立即执行。

函数装饰器在导入模块时立即执行，
而被装饰的函数只在明确调用时运行。
这突出了 Python 程序员所说的导入时和运行时之间的区别。
"""

import demo02

if __name__ == '__main__':
    """
    首先输出
    running register(<function f1 at 0x0000023FECEC6A20>)
    running register(<function f2 at 0x0000023FECEC6AC0>)
    """
    print(demo02.registry)

    demo02.registry[0]()

