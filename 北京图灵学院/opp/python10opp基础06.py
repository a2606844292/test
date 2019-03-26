# 变量的三种方法

class A():
    def __init__(self):
        self.name = 'xiaobai'
        self.age = 18


a = A()
# 属性的三种用法
# 1.赋值
# 2.读取
# 3.删除
a.name = 'xiaohei'  # 赋值
print(a.name)
del a.name


# print(a.name)

# 类属性 property
# 应用场景：
# 对变量除了普通的三种操作，还想增加一些附加的操作，那么可以通过property完成
class A():
    def __init__(self):
        self.name = 'xiaobai'
        self.age = 18

    # 此功能，是对类变量进行读取操作的时候应该执行的函数功能
    def fget(self):
        print('正在使用读取功能')
        return self.name

    # 模拟的是对变量进行写操作的时候执行的功能
    def fser(self):
        print('我被写入了，但是还可以做好多事情')
        self.name = 'wudi' + name

    # fdel模拟的是删除变量的时候进行的操作
    def fdel(self):
        pass

    name2 = property(fget, fser, fdel, '这是一个property的例子')  # 顺序有问题的话会报错
    # property的四个参数顺序是固定的
    # 第一个参数代表读取的时候需要调用的函数
    # 第二个参数代表写入的时候需要调用的函数
    # 第三个是删除


a = A()
print(a.name)
print(a.name2)


