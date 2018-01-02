"""
    classの定義
"""

# s = 'ogjopahjbps'
# print(s.capitalize())


class Person(object):       # objectはなくて良いがpython2の名残から書いておいてもOK
    def say_something(self):
        print('helo')


person = Person()
person.say_something()

# 関数でもできるが、人間がわかりやすいような形


"""
    クラスの初期化
"""


class Person2(object):
    def __init__(self, name='rei'):
        """
        初期
        :param name:
        """
        self.name = name
        print('First')
        print(self.name)

    def say_something(self):
        print('hello2')

    def run(self, num):
        print('run' * num)

    def say_hello(self):
        """
         __init__で指定したnameを呼び出す
         say_somethingを呼び出す
         runメソッドをnum回分呼ぶ
        :return:
        """
        print('I am {}. hello'.format(self.name))
        self.say_something()        # 自分自身のメソッド呼びだし
        self.run(5)                 # 5回呼び出し


person2 = Person2('Mike')
# __init__(self)メソッドが呼ばれ Firstが表示される
# この中で初期設定など行えば良い
# 値を保持させたい時にselfを使う
# selfは自分自身.... self.nameは自分自身の名前
# ここでは、引数のnameを入れている(nameの引数にデフォルトを入れれる)

# classでは、selfがないと自分自身に値を保持させられない

person2.say_hello()
# selfを使って呼び出している


"""
    コンストラクタとデストラクタ
"""


class Person3(object):
    def __init__(self, name):   # コンストラクタ
        print("init")
        self.name = name

    def say_something(self):
        print("say")

    def run(self, num):
        print("run" * num)

    def __del__(self):          # デストラクタ
        print("bye")


person3 = Person3('taro')
person3.run(20)

print('###############')
# この後に__del__メソッドが呼ばれる
# __del__ メソッドを自分で呼ぶ場合

del person3

print('---------------')
