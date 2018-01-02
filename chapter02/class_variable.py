"""
    クラス変数

    インスタンス変数に注意
"""


class Person(object):

    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person('A')
a.who_are_you()

b = Person('B')
b.who_are_you()


class Words(object):

    words = []                  # 初期化しなくて良いものをは、インスタンス変数へ

    def __init__(self):
        self.words_init = []

    def add_word(self, word):
        self.words.append(word)

    def add_word_init(self, word):
        self.words_init.append(word)


c = Words()
c.add_word('add 1')
c.add_word('add 2')


d = Words()
d.add_word('add 3')
d.add_word('add 4')

print(c.words)              # ['add 1', 'add 2', 'add 3', 'add 4']
# d変数も含まれてしまう
# 注意

c.add_word_init('add 1')
c.add_word_init('add 2')
print(c.words_init)         # ['add 1', 'add 2']

d.add_word_init('add 3')
d.add_word_init('add 4')
print(d.words_init)         # ['add 3', 'add 4']
# __init__で初期化しているため 別れる
