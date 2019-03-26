class Sum:
    def __init__(self, name):
        self.name = name

    def cry(self):
        print('输出数字123456')


class a(Sum):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def cry(self):
        print('输出数字11111111')


class b(Sum):
    def __init__(self, name,sex,age):
        super().__init__(name)
        self.age = age
        self.sex = sex

    def cry(self):
        print('输出数字2222222222')

def play(Student):
    print(Student.name)
    Student.cry()




a = a('旺财', 18)
b = b('大白', '公',18)
play(a)
play(b)
