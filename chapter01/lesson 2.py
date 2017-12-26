# 1. import lesson_package.utils
# 2. from lesson_package import utils
# 3. from lesson_package.utils import say_twice

# 下記もできるがおすすめできない
# from lesson_package import utils as u

# 2を使う
from lesson_package import utils
# from lesson_package.talk import human

# 下記アスタリスクもある（__init__.pyに記載必要)あまり使わないように
from lesson_package.talk import *


# 1. r = lesson_package.utils.say_twice('hello')
# 2. r = utils.say_twice('hello')
# 3. r = say_twice('hello')  # この書き方はどこで使っているのかわからなくなるからあまり使わない

r = utils.say_twice('hello')

print(r)
print(human.sing())
print(animal.sing())


# 会社によって異なる
# 必ずフルパスで書くとこもあり
