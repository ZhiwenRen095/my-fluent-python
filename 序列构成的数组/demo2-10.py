"""具名元组的属性和方法"""
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

LatLong = namedtuple('LatLong', 'lat long')

if __name__ == '__main__':
    print(City._fields)  # 具名元组的类属性, 返回包含这个类所有字段名称的元组

    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

    # 具名元组的类方法,接受一个可迭代对象来生成这个类的一个实例,它的作用跟 City(*delhi_data) 是一样的
    delhi = City._make(delhi_data)

    print(delhi._asdict())

    print(City(*delhi_data))
