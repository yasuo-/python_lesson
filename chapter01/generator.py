"""
    generator
"""
l = ['morning', 'afternoon', 'night']

for i in l:
    print(i)

print("###########################")


def greeting():
    yield 'morning'
    yield 'afternoon'
    yield 'night'


def counter(num=10):
    for _ in range(num):
        yield 'run'

"""
    pythonではyieldを見るとgenerator
"""

# for g in greeting():
#    print(g)

g = greeting()  # generator生成
c = counter()
print(next(g))
print("##################")
print(next(g))
print(next(c))
print("@@@@@@@@@@@@@@@@@@")
print(next(g))
print(next(c))

"""
    重たい処理を小分けに行える
"""

"""
    forだとただ繰り返す
    yieldだとnext()で呼び出せて覚えている
"""


