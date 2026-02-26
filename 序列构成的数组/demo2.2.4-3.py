colors = ['black', 'white']
sizes = ['S', 'M', 'L']

gen = ('%s %s' % (c, s) for c in colors for s in sizes)

gen2 = ((c, s) for c in colors for s in sizes)

gen3 = (x for x in range(10))

print(next(gen))  # 'black S'
print(type(next(gen)))  # <class 'str'>
print(next(gen2))  # ('black', 'S')
print(type(next(gen2)))  # <class 'tuple'>
print(next(gen3))  # ('black', 'S')
print(type(next(gen3)))  # <class 'int'>

print("*" * 88)

for x in gen2:
    print(x)