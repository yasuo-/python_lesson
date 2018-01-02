"""
    多重継承

    できるだけない方が良い
"""


class Person(object):
    def talk(self):
        print('talk')

    def name(self):
        print('person name')


class Car(object):
    def run(self):
        print('run')

    def name(self):
        print('car name')


class PersonCarRobot(Person, Car):
    def fly(self):
        print("fly")


person_car_robot = PersonCarRobot()
person_car_robot.talk()             # Personクラスのメソッドが使える
person_car_robot.run()              # Carクラスのメソッドが使える
person_car_robot.fly()

person_car_robot.name()             # "person name"
# 同じメソッド...Personクラスのメソッドが呼ばれる
# 多重継承の左側のプロパティが優先
