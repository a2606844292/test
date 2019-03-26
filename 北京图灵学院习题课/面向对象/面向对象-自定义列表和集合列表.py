'''
定义一个列表的操作类listlnfo
包含方法
1.列表元素添加:add_key()，添加的是数字或者字母
2.列表元素取值:get_key
3.列表合并:update_list(list)
4.删除并且返回最后一个元素:del_key()

'''


class Listlnfo():
    def __init__(self, list):
        self.list = list

    def add_key(self, key_name):
        # 添加的key必须是字符串或者数字
        if isinstance(key_name, (str, int)):
            self.list.append(key_name)
            print(self.list)
            return 'ok'
        else:
            return '输入数字或者字符串'

    def get_key(self, index):
        # 判断传入的索引是否超出列表
        if index >= 0 and index < len(self.list):  # 索引值大于等于0并且小于列表索引数
            return self.list[index]
        return '你输入的太多了。。。。。'

    def update_list(self, new_list):
        self.list.extend(new_list)  # 将旧列表和新的列表进行合并
        return self.list

    def del_key(self):
        # 首先判断我们的列表是否还有元素
        if len(self.list) >= 0:
            return self.list.pop(-1)
        else:
            return '列表是空的'


list = Listlnfo([1, 2, 3, 4, 5])
# print(list.add_key(6))
# print(list.get_key(3))
# print(list.update_list([8,9,10]))
# print(list.del_key())

#### 定义一个集合的操作类
# 包括的方法
# 1. 集合元素添加: add_setinfo()
# 2. 集合的交集: get_intersection()
# 3. 集合的并集: get_union()
# 4. 集合的差集: del_difference()


class SecInfo():
    def __init__(self, my_set):
        self.sett = my_set

    def add(self,keyname):
        self.sett.add(keyname)
        return self.sett

    def get(self,unioninfo):
        if isinstance(unioninfo, set):
            return self.sett & unioninfo
        else:
            return "你传入的不是set"
    def get2(self,unioninfo):
        if isinstance(unioninfo, set):
            return self.sett | unioninfo
        return "你传入的不是set"
    def deling(self,unioninfo):
        if isinstance(unioninfo, set):
            return self.sett - unioninfo
        return "你传入的不是set"


A=set([1,2,3,4,5])
B=set([5,6,3])
my_set= SecInfo(A)
# print(my_set.add(6))
# print(my_set.get(B))
# print(my_set.get2(B))
# print(my_set.deling(B))
print(my_set.deling("123"))













