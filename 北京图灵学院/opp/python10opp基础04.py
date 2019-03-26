# 继承的语法
# 在python中，任何类都有一个共同的父类叫object

class Person():
    name = 'xiaobai'
    age = 18
    _sore = 0  # 考试成绩是秘密，只要自己知道
    _petname = 'baibai'  # 小名，是保护的，子类可以用，但不能公用

    def sleep(self):
        print('i like sleep')


class Teacher(Person):
    teacher_id = '007'

    def make_test(self):
        print('make some money')


t = Teacher()
print(t.name)
print(t._petname)  # 受保护不能外部访问，不知道为什么直接可以调用
t.sleep()
print(t.teacher_id)
t.make_test()
t.make_test()

# 私有访问问题
# 公开访问私有变量，报错
# print(t.__score)

print('*' * 20)


# 子类扩充父类功能的案例
# 人由工作的函数， 老师也由工作的函数，但老师的工作需要讲课

class Person():
    name = 'NoName'
    age = 18
    _sore = 0  # 考试成绩是秘密，只要自己知道
    _petname = 'baibai'  # 小名，是保护的，子类可以用，但不能公用

    def sleep(self):
        print('i like sleep')

    def work(self):
        print('working........')


class Teacher(Person):
    teacher_id = '007'
    name = 'xiaobai'

    def make_test(self):
        print('make some money')

    def work(self):
        super().work()
        self.make_test()
        # 扩充父类的功能只需要调用父类相应的函数
        # Person.work(self)
        # 扩充父类的另一种方法
        # super代表得到父类


t = Teacher()
t.work()

print('*' * 20)


# 构造函数的概念

class xiaobai():
    def __init__(self):
        print('i am big xiaobai')
        # __init__就是构造函数
        # 每次实例化的时候，第一个被自动的调用
        # 因为主要工作是进行初始化，所以得名


# 实例话的时候，括号内的参数需要跟构造函数参数匹配
x = xiaobai()
lufei = xiaobai()

print('*' * 20)


# 继承中的构造函数 - 1
class Animel():
    pass


class PaxingAni(Animel):
    pass


class Xiaobai(PaxingAni):
    # __init__就是构造函数
    # 每次实例化的时候，第一个被自动的调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('i am big xiaobai')


# 实例话的时候，自动调用了Xiaobai的构造函数
kaka = Xiaobai()

print('*' * 20)


# 继承中的构造函数 - 2

class Animel():
    def __init__(self):
        print("Animel")


class PaxingAni(Animel):
    def __init__(self):
        print(" Paxing Dongwu")


class Dog(PaxingAni):
    # __init__就是构造函数
    # 每次实例化的时候，第一个被自动的调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print("I am init in dog")


# 实例话的时候，自动调用了Dog的构造函数
# 因为找到了构造函数，则不在查找父类的构造函数
kakas = Dog()

# 猫没有写构造函数
class Cat(PaxingAni):
    pass

# 此时应该自动调用构造函数，因为Cat没有构造函数，所以查找父类构造函数
# 在PaxingAni中查找到了构造函数，则停止向上查找
c = Cat()
