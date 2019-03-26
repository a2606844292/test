# 多继承的例子
# 字类可以直接拥有父类的属性方法，私有属性的方法除外
class Fish():
    def __init__(self, name):
        self.name = name

    def swim(self):
        print('I am swimimg')


class Bird():
    def __init__(self, name):
        self.name = name

    def fly(self):
        print('I am flying')


############################################

class Person():
    def __init__(self, name):
        self.name = name

    def work(self):
        print('working')


# 单继承的例子
class Student(Person):
    def __init__(self, name):
        self.name = name


class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name


class SwimMan(Person, Fish):
    def __init__(self):
        self.name = name


stu = Student("yueyue")
stu.work()

s = SuperMan('xiaobai')
s.fly()
s.swim()


# --------------------------
# 菱形继承问题
class A():
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


# 构造函数例子
class Person():
    # 对Person类进行实例化的时候
    # 姓名要确定
    # 年龄得确定
    # 地址肯定有
    def __init__(self):
        self.name = 'Noname'
        self.age = 18
        self.address = "Studentwhonheim"
        print("In init func")


p = Person()


# -------------------------------------
# 构造函数的调用顺序 - 1
# 如果子类没有写构造函数，则自动向上查找，知道找到位置
class A():
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")


class C(B):
    pass


# 此时，首先查找C的构造函数
# 如果没有，则向上按照MRO顺序查找父类的构造函数，知道找到为止
c = C()


# ---------------------------------------
# # 构造函数的调用顺序 - 2
# class A():
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self, name):
#         print("B")
#         print(name)
#
#
# class C(B):
#     pass


# 此时，首先查找C的构造函数
# 如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到为止
# 此时，会出现参数结构不对应错误
# c = C()           #这只调用了一个参数，而父类调用了两个函数，所以会产生报错

# ---------------------------------------
# # 构造函数的调用顺序 - 3
class A():
    def __init__(self):
        print("A")


class B(A):
    def __init__(self, name):
        print("B")
        print(name)


class C(B):
    # c中想扩展B的构造函数，
    # 即调用B的构造函数后在添加一些功能
    # 由两种方法实现

    '''
    # 第一种是通过父类名调用
    def __init__(self, name):
        # 首先调用父类构造函数
        B.__init__(self, name)
        # 其次，再增加自己的功能
        print("这是C中附加的功能")
    '''

    # 第二种，使用super调用
    def __init__(self, name):
        # 首先调用父类构造函数
        super().__init__(name)
        # 其次，再增加自己的功能
        print("这是C中附加的功能")


# 此时，首先查找C的构造函数
# 如果没有，则向上按照MRO顺序查找父类的构造函数，知道找到为止
# 此时，会出现参数结构不对应错误
c = C("我是C")


# ------------------------------------------


# Mixin案例
class Person():
    name = "liuying"
    age = 18

    def eat(self):
        print("EAT.......")

    def drink(self):
        print("DRINK......")

    def sleep(self):
        print("SLEEP.....")


class Teacher(Person):
    def work(self):
        print("Work")


class Student(Person):
    def study(self):
        print("Study")


class Tutor(Teacher, Student):
    pass


t = Tutor()

print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

print("*" * 20)


# ------------------------------------------

class TeacherMixin():
    def work(self):
        print("Work")


class StudentMixin():
    def study(self):
        print("Study")


class TutorM(Person, TeacherMixin, StudentMixin):
    pass


tt = TutorM()
print(TutorM.__mro__)
print(tt.__dict__)
print(TutorM.__dict__)


# ------------------------------------------
# issubclass
# 判断子类是否在父类
class A():
    pass


class B(A):
    pass


class C():
    pass


print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(B, object))


# ------------------------------------------
# isinstance
# 检测一个对象是否是一个类的实例
class A():
    pass


a = A()

print(isinstance(a, A))
print(isinstance(A, A))


# ------------------------------------------
# hasattr
# 检测一个对象是否有成员xxx
class A():
    name = 'Noname'


a = A()
print(hasattr(a, 'name'))
'''
- getattr: get attribute
- setattr: set attribute
- delattr: delete attribute
- dir: 获取对象的成员列表
'''

#help案例
#查看setattr的具体用法
help(setattr)