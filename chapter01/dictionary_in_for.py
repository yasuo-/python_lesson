"""
    dictionary in for
    辞書をforで処理する

    よく使われる
"""

d = {'x': 100, 'y': 200}

for v in d:
    print(v)    # keyのみ表示される

print(d.items())

for k, v in d.items():  # itemsを使う
    print(k, ':', v)


