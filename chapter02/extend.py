"""
    classの継承
"""


class Car(object):
    # pass                # 何もしない
    def self_run(self):
        print('self_run')


class ToyotaCar(Car):   # Car classを引き継ぐ
    pass                # 何もしない


class TeslaCar(Car):
    def auto_run(self):
        print("auto_run")


car = Car()
car.self_run()

print("########################")
toyota_car = ToyotaCar()
# toyota_carでもauto_runを使える
toyota_car.self_run()

print("########################")
tesla_car = TeslaCar()
tesla_car.auto_run()
# Carクラスのメソッドも使える
tesla_car.self_run()


"""
    メソッドのオーバーライドとsuperによる親の呼び出し
"""


class Car2(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print("run")

    def self_run(self):
        print('self_run')


class ToyotaCar2(Car2):     # Car2 classを引き継ぐ
    # pass                  # 何もしない
    def run(self):          # Carクラスのrun  メソッドを上書き
        print("fast")


class TeslaCar2(Car2):
    def __init__(self, model='Model S', enable_auto_run=False):
        # self.model = model
        super().__init__(model)                # Car2クラスのmodel呼び出し
        self.enable_auto_run = enable_auto_run

    def run(self):
        print("super fast")

    def auto_run(self):
        print("auto_run")


car2 = Car2()
car2.run()

print("########################")
toyota_car2 = ToyotaCar2('Lexus')
# toyota_carでもauto_runを使える
toyota_car2.run()

print("########################")
tesla_car2 = TeslaCar2('Model S')
print(tesla_car2.model)
tesla_car2.auto_run()
# Carクラスのメソッドも使える
tesla_car2.run()


"""
    プロパティを使った属性の設定
"""


class Car3(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print("run")

    def self_run(self):
        print('self_run')


class TeslaCar3(Car3):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 password='123'):
        super().__init__(model)
        # self.enable_auto_run = enable_auto_run    # 自由に書き換え化
        self._enable_auto_run = enable_auto_run     # Falseを変更できないようにする(property使い、書き換える)
        # self.__enable_auto_run = enable_auto_run  # Classの外から読めないようにする(書き換え不可)
        self.password = password

    @property
    def enable_auto_run(self):                      # propertyでgetterにする
        return self._enable_auto_run

    @enable_auto_run.setter                         # 書き換え可能なsetter
    def enable_auto_run(self, is_enable):
        if self.password == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        # print(self.__enable_auto_run)               # __でもClass内メソッドからなら呼べる
        print("super fast")

    def auto_run(self):
        print("auto_run")


print("########################")
tesla_car3 = TeslaCar3('Model S', password='456')       # passwordが456以外ならerrorになる
print(tesla_car3.enable_auto_run)
tesla_car3.enable_auto_run = True
print(tesla_car3.enable_auto_run)
# propertyの関数が呼ばれるがtesla_car3.enable_auto_run()でなくて良い

print(tesla_car3._enable_auto_run)
# __init__の_enable_auto_run)を知って入ればアクセスはできる
# _enable_auto_runを隠したい場合, __enable_auto_runをにする

"""
    Classの構造で気をつけること
    
    tesla_car3.__enable_auto_run = '@@@@@@@@@@@@'
#   print(tesla_car3.__enable_auto_run)
#   __enable_auto_run は自分で新しくObjectを生成している状態
#   バグになったりするので注意
"""


class T(object):
    pass


t = T()
t.name = 'mike'
t.age = 20
print(t.name, t.age)

# tesla_car3.__enable_auto_run = '@@@@@@@@@@@@'
# print(tesla_car3.__enable_auto_run)
# __enable_auto_run は自分で新しくObjectを生成している状態
# バグになったりするので注意


"""
    ダックタイピング
"""


class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('OK')
        else:
            raise Exception('No Drive')


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError


class Car4(object):
    def __init__(self, model=None):
        self.model = model

    def raide(self, person):
        person.drive()


print("######### ダックタイピング ###############")
baby = Baby()
adult = Adult()
car_drive = Car4()
# car_drive.raide(baby)
car_drive.raide(adult)


