"""
    Abstract class

    * javaなどで実装されていたので、後々ついた。
      実装不要なら使わなくても良い
"""
import abc


class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractclassmethod
    def drive(self):
        pass


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No drive')


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    # def drive(self):
    #    print("OK")
    # 実装忘れると TypeError: Can't instantiate abstract class Adult with abstract methods drive

    def drive(self):
        print("ok")


baby = Baby()
adult = Adult()
