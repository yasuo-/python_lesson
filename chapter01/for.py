"""
    for
"""

# whileだと

some_list = [1, 2, 3, 4]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1


# forだと
j = 0
for j in some_list:
    print(j)

# 反復処理 => イテレーター


for k in 'abcdefg':
    print(k)    # 1文字ずつ表示される


for word in ['My', 'name', 'is', 'cat']:
    if word == 'cat':
        break       # breakでforが抜けれる
    if word == 'name':
        continue    # skipする
    print(word)


for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break           # for から抜ける
    print(fruit)
else:
    print('I ate all')  # loopが全て終わったら表示される
