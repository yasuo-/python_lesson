"""
    range関数
"""

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for なら
for i in num_list:
    print(i)


# めんどくさい...

for j in range(10):     # 0から9まで表示される
    print(j)

for k in range(2, 10):  # 2からスタート
    print(k)

for l in range(2, 10, 3):   # 3飛ばし
    print(l)

# 10回処理する

for h in range(10):
    print('hello')


for _ in range(10):
    print('Hello')

# indexに _ で書くと、rangeから入ってくるindexはループでは使われないと理解できる

