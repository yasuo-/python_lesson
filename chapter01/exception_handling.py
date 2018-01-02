"""
    例外処理
"""

l = [1, 2, 3]
i = 5

try:
    l[i]
except IndexError as exc:   # IndexErrorの時のみ
    print("Don't worry Index Error: {}".format(exc))
except NameError as ex:
    print("Name Error: {}".format(ex))
except Exception as ex:
    print("Other Error: {}".format(ex))
else:                       # tryの成功時のみ実行される
    print('done')
finally:                    # 最後に実行される
    print('final')

print("last")


"""
    独自例外
"""

raise IndexError('test error')


class UppercaseError(Exception):
    pass


def check():
    words = ['apple', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)      # 自分で作ったエラー


try:
    check()
except UppercaseError as exc:               # 独自のエラー
    print('This is my fault. {} Go next'.format(exc))
