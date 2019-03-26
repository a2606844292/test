class a():
    def __init__(self,name):
        self.name=name

    def people_run(self):
        print(self.name+'在跑步ing')
class b(a):
    def __init__(self,name,email):# 继承Person
        print('调用父类元素')
        self.email=email
        super().__init__(name)


stu = a('xiaobai')
stu.people_run()