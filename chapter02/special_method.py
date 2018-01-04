"""
    特殊メソッド
"""


class Word(object):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):     # イコール
        return self.text.lower() == word.text.lower()


w = Word('test')
# __len__
print(len(w))       # 4
w2 = Word('#############')
# __add__
print(w + w2)       # test#############
# __eq__
print(w == w2)      # false 同じなら true

# 他にも特殊文字たくさんある
# 一番使うのは __str__
