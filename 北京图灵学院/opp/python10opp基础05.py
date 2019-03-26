# 属性案例
# 创建Student类，描述学生类
# 学生具有Student.name属性
# 但name格式并不统一
# 可以用增加一个函数，然后自动调用的方式，但很蠢

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # 如果不想修改代码
        self.setName(name)

    def intro(self):
        print('Hi my name is {}'.format(self.name))

    def setName(self, name):
        self.name = name.upper()


s1 = Student('XIAOBAI', 18)
s2 = Student('xiaoming', 19)

s1.intro()
s2.intro()


# ------------------------------------------------------
# peroperty案例
# 定义一个Person类，具有name，age属性
# 对于任意输入的姓名，我们希望都用大写方式保存
# 年龄，我们希望内部统一用整数保存
# x = property(fget, fset, fdel, doc)

class Person():
    '''
    茕茕孑立 沆瀣一气
    踽踽独行 醍醐灌顶
    绵绵瓜瓞 奉为圭臬
    龙行龘龘 犄角旮旯

    '''

    # 函数的名称可以任意
    def fget(self):
        return self._name * 2  # name是私有变量

    def fset(self, name):
        self._name = name.upper()

    def fdel(self):
        self._name = 'Noname'

    name = property(fget, fset, fdel, '对name进行操作')


p1 = Person()
p1.name = 'xiaobai'
print(p1.name)

# 类的内置属性举例
print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__bases__)


# init举例
class A():
    def __init__(self, name=0):
        print('我被调用了')


a = A()


# __call__举例
# 对象当函数调用时触发
class A():
    def __init__(self, name=0):
        print('我被调用了')

    def __call__(self):
        print('我又被调用了')


a = A()
a()


# __str__举例
# 当对象被当做字符串使用的时候调用
class A():
    def __init__(self, name=0):
        print('我被调用了')

    def __call__(self):
        print('我又被调用了')

    def __str__(self):
        return 'xiaobai'


a = A()
print(a)


# __repr__:返回字符串，跟__str__具体区别_
# repr__和__str__这两个方法都是用于显示的，
# __str__是面向用户的，而__repr__面向程序员。

# 描述符相关
# __set__
# __get__
# __delete__

# 属性操作相关
# __getatt__:访问一个不存在的属性时触发
class A():
    name = 'NoName'
    age = 18

    def __getattr__(self, name):
        print('没有找到')


a = A()
print(a.name)
print(a.addr)


# __setattr__:对成员属性进行设置的时候触发
# 参数：
# -self用来获取当前对象
# -对设置的属性名称，以字符串形式出现
# 需要对属性名称设置的值
# 作用:对进行属性设置的时候进行验证或者修改
# 注意：在该方法中不能对属性中直接进行赋值操作，否则进入死循环

# __setattr__案例
class Person():
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        print('设置属性:{0}'.format(name))
        # 下面语句会导致问题，死循环
        # self.name = value
        # 此情况，为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(name, value)


p = Person()
print(p.__dict__)
p.age = 18


# __gt__

class Student():
    def __init__(self, name):
        self._name = name

    def __gt__(self, obj):
        print('{0}比{1}大吗?'.format(self, obj))
        return self._name > obj._name


stu1 = Student('one')
stu2 = Student('two')
print(stu1 > stu2)


# 三种方法的案例
class Person():
    # 实例方法
    def eat(self):
        print('Eating...')

    # 类方法的第一个参数，一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)
        print('Playing...')

    # 静态方法,不需要用第一个参数表示
    @staticmethod
    def say():
        print('Saying...')


xiaobai = Person()

# 实例方法
xiaobai.eat()
#类方法
Person.play()
xiaobai.play()
#静态方法
Person.say()
xiaobai.say()
