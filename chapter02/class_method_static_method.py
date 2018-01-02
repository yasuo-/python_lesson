"""
    クラスメソッドとスタティックメソッド

    @classmethod
        インスタンス生成しなくても呼び出せる
    @staticmethod
        classの外にメソッド書くものとあまり違いなし
"""


class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        """
        クラスメソッド
        Objectのクラスをインスタンスとして生成しなくても
        呼び出せる
        :return:
        """
        return cls.kind

    @staticmethod
    def about():
        """
        static method
        パラメーターはなくても良い
        :return:
        """
        print('about human static method')

    @staticmethod
    def about2(year):
        """
        static method
        パラメーターあり
        :param year:
        :return:
        """
        print('about2 human age: {} static method in params'.format(year))


a = Person()
print(a.x)

b = Person
# print(b.x)          # オブジェクトではないため呼び出せない
print(b.kind)         # インスタンス変数は呼び出せる

print(Person.kind)
print(a.what_is_your_kind())
print(b.what_is_your_kind())

Person.about()
Person.about2(20)
