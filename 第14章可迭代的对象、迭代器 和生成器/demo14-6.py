

def gen_AB():
    print('start')
    yield 'A'

    print('continue')
    yield 'B'

    print('end')
    yield 'C'

for word in gen_AB():
    print('--->' + word)
