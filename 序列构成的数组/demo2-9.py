"""定义和使用具名元组"""
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

Card = namedtuple('Card', ['rand', 'suit'])

"""
下面4中写法等价：

# 写法1：空格分隔的字符串（最常见、最简洁）
City = namedtuple('City', 'name country population coordinates')

# 写法2：逗号分隔也行（但不推荐，因为容易和参数混淆）
City = namedtuple('City', 'name, country, population, coordinates')

# 写法3：显式列表
City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])

# 写法4：元组也行
City = namedtuple('City', ('name', 'country', 'population', 'coordinates'))
"""
if __name__ == '__main__':
    tokyo: City = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print(tokyo)
    card: Card = Card(3, 'K')
    print(card)

    # 使用具名元组
    for field in tokyo:
        print(field)