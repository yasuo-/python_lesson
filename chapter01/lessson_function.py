print('##############')


def say_something():
    # print('hi')
    s = 'hi'
    return s


print(type(say_something()))

result = say_something()
print(result)


def what_is_this(color):
    # print(color)
    if color == 'red':
        return print('tomato')
    elif color == 'green':
        return print('suica')
    else:
        return print('I don`t know')


print(what_is_this('red'))

print('############## 引数')


def menu(entree, drink, dessert):
    print('entree: ', entree)
    print('drink:', drink)
    print('dessert:', dessert)


menu('beef', 'beer', 'ice')  # 位置引数
menu('beef', 'ice', 'beer')  # パラメーター次第で間違える
menu(entree='beef', drink='beer', dessert='ice')  # キーワード引数
menu('beef', drink='beer', dessert='ice')
menu('beef', dessert='ice', drink='beer')
print('##############')
# menu(drink='beer', 'beef', dessert='ice')  # パラメーターの順番とキーワード引数がかぶっているものは判断できない


print('############## default 引数')


def menu2(entree='beef', drink='beer', dessert='ice'):
    print('entree: ', entree)
    print('drink:', drink)
    print('dessert:', dessert)


menu2()
menu2('chicken', drink='tomato')  # entreeとdrinkが上書きされる


print('############## 引数  array')


def test_func(x, len=[]):
    len.append(x)
    return len


r = test_func(100)
print(r)  # [100]
r = test_func(100)
print(r)  # [100, 100]  前の100が残ってしまうため、引数のデフォルト値に[]の指定は良くない


def test_func2(x, len=None):
    if len is None:
        len = []  # lenがNoneならセットする
    len.append(x)
    return len


r = test_func2(100)
print(r)  # [100]
r = test_func2(100)
print(r)  # [100]


print('############## 位置引数  タプル化')


def say_something(word1, word2, word3):
    print(word1)
    print(word2)
    print(word3)
#  実行できるが面倒


say_something('Hello', 'Mike', 'keito')


# pythonなら引数の変数前に*を入れることでまとめてくれる
def say_something2(*args):
    for arg in args:
        print(arg)


say_something2('Hello', 'Mike', 'keito')


# 位置引数と一緒に使える
def say_something3(w, *args):
    print(w)
    for arg in args:
        print(arg)


say_something3('Hello', 'Mike', 'keito')
# Helloは wに入る
# 残りは*argに入る

# 下記のような使い方もできる
t = ('Mike', 'Taro', 'jiro')
say_something3('Hi', *t)


print('############## キーワード引数  辞書化')


def menu(entree='beef', drink='wine'):
    print(entree, drink)


menu(entree='beef', drink='coffee')


# 引数増やしたくなった場合 **をつける
def menu2(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


menu2(entree='beef', drink='coffee')
#  辞書化する {'entree': 'beef', 'drink': 'coffee'}

d = {
    'entree': 'beef',
    'drink': 'coffee',
    'dessert': 'ice'
}

menu2(**d)


# 位置引数, タプル化, 辞書化全て使える
def menu3(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


menu3('apple', 'banana', 'orange', entree='beef', drink='coffee')
# 引数の順番には注意
# def menu3(food, **kwargs, *args):  エラーになる


