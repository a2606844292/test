# 传值和传地址的区别
# 对于简单的数值，采用传值操作，即在函数内对参数的操作不影响外面的变量
# 对于复杂变量，采用传地址操作，此时函数内的参数和外部变量是同一份内容，
# 任何地方对此内容的更改都影响另外的变量或参数的使用
def a(n):
    n[2] = 300
    print(n)
    return None


def b(n):
    n += 100
    print(n)
    return None


an = [1, 2, 3, 4, 5, 6]
bn = 9

print(an)
a(an)
print(an)

print(bn)
b(bn)
print(bn)

# 关于列表的函数
l = ['a', "i love xiaobai", 45, 766, 5 + 4j]
print(l)

# append 插入一个内容, 在末尾追加
a = [i for i in range(1, 5)]
print(a)
a.append(100)
print(a)

# insert: 指定位置插入
# insert(index, data), 插入位置是index前面 index索引，数据
print(a)
a.insert(3, 666)
print(a)

# 删除
# del 删除
# pop，从对位拿出一个元素，即把最后一个元素取出来
print(a)
last_ele = a.pop()  # 要对a.pop赋值
print(last_ele)
print(a)

# remove:在列表中删除指定的值的元素
# 如果被删除的值没在list中，则报错
# 即，删除list指定值的操作应该使用try。。。excepty语句，或者先行进行判断
# if x in list:
#    list.remove(x)
a.insert(4, 666)
print(a)
print(id(a))
a.remove(666)
print(a)
print(id(a))
# 输出两个id值一样，说明，remove操作是在原list直接操作

# clear:清空
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))

# 如果不需要列表地址保持不变，则清空列表可以使用以下方式
# a = list()
# a = []

# reverse:翻转列表内容，原地翻转
a = [1, 2, 3, 4, 5]
print(a)
print(id(a))
a.reverse()
print(a)
print(id(a))

# extend:扩展列表，两个列表，把一个直接拼接到后一个上
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(a)
print(id(a))
a.extend(b)
print(a)
print(id(a))

# count:查找列表中指定值或元素的个数
print(a)
a.append(8)
a.insert(4, 8)
print(a)
a_len = a.count(8)
print(a_len)

# -----------------------------
# copy: 拷贝，此函数是浅拷贝，
# 列表类型变量赋值示例
a = [1, 2, 3, 4, 5, 666]
print(a)
# list类型，简单赋值操作，是传地址
b = a
b[3] = 777
print(a)
print(id(a))
print(b)
print(id(b))
print("*" * 20)
# 为了解决以上问题，list赋值需要采用copy函数
b = a.copy()
print(a)
print(id(a))
print(b)
print(id(b))
print("*" * 30)

b[3] = 888
print(a)
print(b)

# 深拷贝跟浅拷贝的区别
# 出现下列问题的原因是，copy‘函数是个浅拷贝函数，即只拷贝一层内容
# 深拷贝需要使用特定工具
a = [1, 2, 3, [10, 20, 30]]
b = a.copy()
print(id(a))
print(id(b))
print(id(a[3]))
print(id(b[3]))
a[3][2] = 666
print(a)
print(b)

# #元组-tuple
# 元组可以看成是一个不可更改的list
# 元组创建
# 创建空元组
t = ()
print(type(t))

# 创建一个只有一个值的元组
t = (1,)
print(type(t))
print(t)

t = 1,
print(type(t))
print(t)

# 创建多个值的元组
t = (1, 2, 3, 4, 5)
print(type(t))
print(t)

t = 1, 2, 3, 4, 5
print(type(t))
print(t)

# 使用其他结构创建
l = [1, 2, 3, 4, 5]
t = tuple(l)
print(type(t))
print(t)

'''
元组的特性
是序列表，有序
元组数据值可以访问，不能修改，不能修改，不能修改
元组数据可以是任意类型
总之，list所有特性，除了可修改外，元组都具有
也就意味着，list具有的一些操作，比如索引，分片，序列相加，相乘，成员资格操作等，一模一样

'''
# 索引操作
t = (1, 2, 3, 4, 5)
print(t[4])

t = (1, 2, 3, 4, 5, 6)
t1 = t[1::2]  # 每2个留一个数
print(id(t))
print(id(t1))
print(t1)

# 切片可以超标
t2 = t[2:100]
print(t2)

# 序列相加
t1 = (1, 2, 3)
t2 = (5, 6, 7)

# 传址操作
print(t1)
print(id(t1))
t1 = t1 + t2
print(t1)
print(id(t1))

# 以上操作，类似于
t1 = (1, 2, 3)
t1 = (2, 3, 4)

# tuple 的不可修改，指的是内容的不可修改
# 修改tuple内容会导致报错
# t1[1] = 100

# 元组相乘
t = (1, 2, 3)
t = t * 3
print(t)

# 成员检测
t = (1, 2, 3)
if 2 in t:
    print("YES")
else:
    print("NO")

# 元组遍历，一般采用for
# 1. 单层元组遍历
t = (1, 2, 3, "wangxiaojing", "i", "love")
for i in t:
    print(i, end=" ")

# 2. 双层元组的遍历
t = ((1, 2, 3), (2, 3, 4), ("i", "love", "wangxiaojing"))

# 对以上元组的遍历，可以如下
# 1.

for i in t:
    print(i)

for k, m, n in t:
    print(k, '--', m, '--', n)
