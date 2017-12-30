"""
    lambda
"""

l = ['Mon', 'tue', 'Wed', 'Thu', 'fir', 'sat', 'Sun']


def change_words(words, func):
    for word in words:
        print(func(word))


def capitalize_func(word):
    return word.capitalize()


def lower_func(word):
    return word.lower()


change_words(l, capitalize_func)

# lambdaなら
capitalize_func = lambda word: word.capitalize()

# また...
change_words(l, lambda word: word.capitalize())

change_words(l, lambda word: word.lower())


# lambdaを使わなければ、関数が増えてくる。
# capitalize_func や lower_funcなど

# functionを引数にするものは、lambdaを使ってしまえばコード量の削減になる

# lambda -> 関数を式として扱い変数に代入できるようにする手法であり、プログラムのコードを簡潔にする

# ex2
# 通常
def func(price, tax):
    return price + (price * tax)


payment = func(100, 0.08)
print(payment)

# lambda
payment2 = (lambda price, tax: price + (price * tax))(100, 0.08)
print(payment2)

# defによる関数定義は登場せず、代わりにlambdaと書いて、その横に引数そして、セミコロン(:)の後に引数を使用した処理内容という形式にて書く

"""
    lambda 引数: 処理内容
"""