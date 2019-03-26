# 4.类和对象的成员分析
#     -类和对象都可以存储成员，成员可以归类所有，野可以归对象所有
#     -类存储成员时使用与类关联的一个对象
#     -独享存储成员是是存储在当前对象中
# 对象访问一个成员时，如果对象没有成员，尝试访问类中的同名成员
# -如果对象中有此成员，一定使用对象的成员


# 1.........................
class Student():
    name = 'xiaobai'
    age = 18


print(Student.__dict__)

# 实例化
xiaobai = Student()
print(xiaobai.name)


# 2.........................
class A():
    name = 'xiaobai'
    age = 18

    # 注意say的写法，参数由一个self
    def say(self):
        self.name = 'dabai'
        self.age = 200


# 此案例说明
# 类实例的属性和其对象的实例的属性不对对象的实例属性赋值的前提下
# 指向同一个变量

# 此时，A称为类实例
print(A.name)
print(A.age)
print('*' * 20)
print(id(A.name))
print(id(A.age))
print('*' * 20)

a = A()
# 查看A内所有的属性
print(A.__dict__)
print(a.__dict__)

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

# 对name和age赋值
a.name = 'xiaoming'
a.age = 16
print(id(a.name))
print(id(a.age))


# 5.关于self
# -self在对象的方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象自动传入当前的第一参数中
# -self并不是关键字，只是一个用于接受对象的普通参数，理论上可以用任何一个普通的变量
# -方法中有self形参的方法成为非绑定类的方法，可以通过对象访问，没用self的是绑定的方法只能通过类访问
# -使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员可以通过__class__成员名访问
class Student():
    name = 'xiaobai'
    age = 18

    # 注意say的写法，参数由一个self
    def say(self):
        self.name = 'dabai'
        self.age = 200
        print('My name is {0}'.format(self.name))
        print('My age is {0}'.format((self.age)))

    def sayAgain(s):
        print('My name is {0}'.format(s.name))
        print('My age is {0}'.format((s.age)))


xiaoming = Student()
xiaoming.say()
# 2个方法都可以实现
xiaoming.sayAgain()


# 4.--------------------------------------------------
class Teacher():
    name = 'xiaobai'
    age = 18

    # 注意say的写法，参数由一个self
    def say(self):
        self.name = 'dabai'
        self.age = 200
        # 调用类的成员变量需要用 __class__
        print('My name is {0}'.format(__class__.name))
        print('My age is {0}'.format((self.age)))

    def sayAgain():
        print('Hello nice to me you')


t = Teacher()
t.say()
# 调用绑定类函数使用类名
Teacher.sayAgain()


# 5.--------------------------------------------------
# 关于self的案例

class A():
    name = 'xiaobai'
    age = 18

    def __init__(self):
        self.name = 'xiaobai'
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)


class B():
    name = 'xiaobai'
    age = 90


a = A()
# 此时，系统会默认把a作为第一个参数传入参数
a.say()
# 此时，self被a替换
A.say(a)
# 同样可以把A作为参数传入
A.say(A)
# 此时，传入的时类实例B，因为B具有name和age的属性，所以不会报错
A.say(B)


# 以上代码，利用了鸭子模型,类型相同就能传入


# 6.面向对象的三大特性
# -封装
# -继承
# -多态

# 6.1封装
# -封装就是对对象的成员进行访问限制
# -封装的三个级别
#     -公开：public
#     -受保护的：protected
#     - 私有的：private
# public,protected,private不是关键字
# -判别对象的位置
#   -对象内部
#   -对象外部
#   -子类中
# 私有
#   -私有成员时最高级别的封装，只能在当前类或对象访问
#   -在成员前面添加两个下划线即可

#   class Person():
# name时共有的成员
# name ='xiaobai'
# __age就是私有成员
# __age=18
# python的私有不是真的私有，时一种成为name mangling的改名策略
# 私有变量案例


class Person():
    # name是共有的成员
    name = "liuying"
    # __age就是私有成员
    __age = 18


p = Person()
# name是公有变量
print(p.name)
# __age是私有变量
# 注意报错信息，无法访问私有变量
# print(p.__age)

# name mangling技术
print(Person.__dict__)

p._Person__age = 19
print(p._Person__age)
