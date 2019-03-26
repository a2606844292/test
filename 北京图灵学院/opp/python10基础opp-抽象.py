# 抽象
class Animel():
    def sayhello(self):
        pass


class dog(Animel):
    print('闻一哈')


class Person(Animel):
    def sayhello(self):
        print('telling....')


d = dog()
d.sayhello()

xiaobai = Person()
xiaobai.sayhello()

# 抽象类的实现

import abc


# 声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):

    # 定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink():
        pass

    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

    def sleep(self):
        print("Sleeping.......")


# 函数名可以当变量使用
def sayHello(name):
    print('{}你好'.format(name))


sayHello('xiaobai')

person = sayHello
person('xiaohei')


# 自己组装一个类
class A():
    pass


def say(self):
    print("Saying... ...")


class B():
    def say(self):
        print('Saying......')


A.say = say

a = A()
a.say()

b = B()
b.say()

# 组装类例子 2
# 自己组装一个类

from types import MethodType


class A():
    pass


def say(self):
    print('sleeping.....')


a = A()
a.say = MethodType(say, A)
a.say()


# 利用type造一个类

# 先定义类应该具有的成员函数
def say(self):
    print("Saying.....")


def talk(self):
    print("Talking .....")


# 用type来创建一个类
A = type("AName", (object,), {"class_say":say, "class_talk":talk})

# 然后可以像正常访问一样使用类
a = A()

a.class_say()
a.class_talk()

