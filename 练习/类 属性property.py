class A():
    def __init__(self):
        self.name = 'xiaobai'
        self.age = 18

    def fget(self):
        print('正在使用读取功能')
        return self.name

    def fser(self):
        print('我被写入了，但是还可以做好多事情')
        self.name = 'wudi' + name

    def fdel(self):
        pass

    name2 = property(fget, fser, fdel, '这是一个property的例子')  # 顺序有问题的话会报错


a = A()
print(a.name)
print(a.name2)
