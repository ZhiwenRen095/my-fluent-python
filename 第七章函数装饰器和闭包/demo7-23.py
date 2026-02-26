"""
普通的装饰器不带括号（如 @decorate），

而带参数的装饰器（如 @register(active=False)）实际上经历了两个阶段的调用：

工厂调用： 执行 register(active=False)，返回 decorate 函数。

装饰执行： 返回的 decorate 函数随后作用于被装饰的函数（如 f1）。

装饰器不是什么魔法，@ 只是语法糖：

@decorator
def func():
    pass

# 完全等价于：
func = decorator(func)


def retry(times=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == times - 1:
                        raise
                    print(f"Retry {i+1}/{times}...")
        return wrapper
    return decorator

@retry(times=5)
def unstable_api():
    pass
完全等价于
unstable_api =  retry(times=5)(unstable_api) # wrapper


--------------------------------------------------------------------------
@retry(times=5)           分两步执行：

第一步：retry(times=5)    ← 先调用 retry，传入参数
        返回 decorator     ← 得到一个"不带参数的装饰器"

第二步：@decorator         ← 再用返回值装饰函数
        unstable_api = decorator(unstable_api)
                       = wrapper
--------------------------------------------------------------------------
"""
registry = set()


def register(active=True):
    """
    这里的关键是，register() 要返回 decorate，
    然后把它应用到被装饰的函数上。
    """

    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func

    return decorate


@register(active=False)
def f1(a, b):
    return a + b

if __name__ == '__main__':
    print(f1(1, 2))
    print(f1.__name__)
