"""
    zip関数
"""

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

# 読みづらい

for day, fruit, drink in zip(days, fruits, drinks):
    print(days, fruit, drink)

# zip関数を使う
