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
