"""
    リスト内包表記
"""
t = (1, 2, 3, 4, 5)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

# 1行で書ける
# 短いロープなら、リスト内包表記
# メモリ使用量少なくできる
r = [i for i in t if i % 2 == 0]
print(r)

# あえて使いすぎない

"""
    辞書包括表記
"""
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

# 通常
d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

# 包括表記
d = {x: y for x, y in zip(w, f)}
print(d)

"""
    集合内表記
"""

s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}

print(s)


"""
    ジェネレーター内包表記
"""


def g():
    for i in range(10):
        yield i


g = g()
# ジェネレーター内包
g = (i for i in range(10))
print(type(g))
print(g)

# tupleにする場合
g2 = tuple(i for i in range(10))
print(type(g2))
print(g)

for x in g2:
    print(x)
