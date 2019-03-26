'''
#### 定义一个集合的操作类
包括的方法
1. 集合元素添加: add_setinfo()
2. 集合的交集: get_intersection()
3. 集合的并集: get_union()
4. 集合的差集: del_difference()

'''


class SecInfo():
    def __init__(self,sett):
        self.sett=sett
    def add(self,keyname):
        self.sett.add(keyname)
        return self.sett

    def get(self,union):
        return self.sett & union




A=set([1,2,3,4,5])
B=set([5,6,3])
my_set=SecInfo(A)
# print(my_set.add(6))
print(my_set.get(B))