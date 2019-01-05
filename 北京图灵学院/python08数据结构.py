#汉诺塔问题
'''
规则：
    1.每次移动一个盘子
    2.任何时候大盘子在下面，小盘子在上面
方法：
1.n=1： 直接把A上的一个盘子移动到C上， A->C
2.n=2:
    把小盘子从A放到B上， A->B
    把大盘子从A放到C上， A->C
    把小盘子从B放到C上， B->C
3.n=3:
    把A上的两个盘子，通过C移动到B上去， 调用递归实现
    把A上剩下的一个最大盘子移动到C上， A->C
    把B上两个盘子，借助于A，挪到C上去， 调用递归
4.n = n：
    把A上的n-1个盘子，借助于C，移动到B上去，调用递归
    把A上的最大盘子，也是唯一一个，移动到C上，A->C
    把B上n-1个盘子，借助于A，移动到C上， 调用递归

'''


def hano(n, a, b, c):
    '''
    汉诺塔的递归实现
    n：代表几个盘子
    a：代表第一个塔，开始的塔
    b：代表第二个塔，中间过渡的塔
    c：代表第三个塔, 目标塔
    '''
    if n == 1:
        print(a, "-->", c)
        return None
    '''

    if n == 2:
        print(a, "-->", b)
        print(a, "-->", c)
        print(b, "-->", c)
        return None
    '''
    # 把n-1个盘子，从a塔借助于c塔，挪到b塔上去
    hano(n - 1, a, c, b)
    print(a, "-->", c)
    # 把n-1个盘子，从b塔，借助于a塔，挪到c塔上去
    hano(n - 1, b, a, c)

a = "A"
b = "B"
c = "C"

n = 2
hano(n, a, b, c)








#-----------------------------------------------------
#List(列表)
# del 删除
# a = [1, 2, 3, 4, 5, 6]
# del a[2]
# print(a)

#-----------------------------------------------------
# del 删除
# 如果使用del之后，id的值和删除前不一样，则说明删除生成了一个新的list
a = [1,2,3,4,5,6]
print(id(a))
del a[2]
print(id(a))
print(a)
#-----------------------------------------------------
# 使用加号链接两个列表
a = [1,2,3,4,5]
b = [5,6,7,8,9]
d = ['a', 'b', 'c']
c = a + b + d
print(c)
#-----------------------------------------------------
# 使用乘号操作列表
# 列表直接跟一个整数相乘
# 相当于把n个列表接在一起
a = [1,2,3,4,5]
b = a *3
print(b)

# 成员资格运算
# 就是判断一个元素是否在爱list里边
a = [1,2,3,4,5,6]
b = 8
#-----------------------------------------------------
#c 的值是一个布尔值
c = b in a
print(c)

b = 4
print(b in a)
#-----------------------------------------------------
# not in
a = [1,2,3,4,5]
b = 9

print(b not in a)
#-----------------------------------------------------
#链表的遍历
    # for
    # while
# for in list
#-----------------------------------------------------
a = [1, 2, 3, 4, 5]
# 挨个打印a里边的元素
for i in a:
    print(i)

b = ["I love xiaobai"]

for i in b:
    print(i)
#-----------------------------------------------------

# range
# in 后面的变量要求是可以可迭代的内容
for i in range(1,10):
    print(i)

print(type(range(1,10)))
#-----------------------------------------------------

# while循环访问list
# 一般不用while遍历list

a = [1,2,3,4,5,6]
length = len(a)

# indx表示的是list的下标
indx = 0
while indx < length:
    print(a[indx])
    indx += 1
#-----------------------------------------------------

# 双层列表循环
#a 为嵌套列表，或者叫双层列表
a = [["one", 1], ["two", 2], ["three", 3]]
for k, v in a:
    print(k, "--", v)
# -----------------------------------------------------

# 双层列表循环变异

#a 为嵌套列表，或者叫双层列表
a = [["one", 1, "eins"], ["two", 2,"zwei"], ["three", 3,"drei"] ]
#这个例子说明，k，v,w的个数应该跟解包出来的变量个数一致
for k,v,w in a:
    print(k, "--", v, "--",w)
 # -----------------------------------------------------

'''列表内涵: list content
    通过简单方法创作列表
'''
# for 创建
a = ['a', 'b', 'c']
    # 用list a创建一个list b
    # 下面代码的含义是，对于所有a中的元素，逐个放入新列表b中
b = [i for i in a]
print(b)
#-----------------------------------------------------
# 对a中所有元素乘以10，生成一个新list
a = [1,2,3,4,5]
# 用list a创建一个list b
# 下面代码的含义是，对于所有a中的元素，逐个放入新列表b中
b = [i*10 for i in a]
print(b)
#-----------------------------------------------------
# 列表生成式可以嵌套
# 由两个列表a，b
a = [i for i in range(1,4)] # 生成list a
print(a)

b = [i for i in range(100,400) if i % 100 == 0]
print(b)

# 列表生成是可以嵌套,此时等于两个for循环嵌套
c = [  m+n for m in a for n in b]
print(c)

# 上面代码跟下面代码等价
for m in a:
    for n in b:
        print(m+n, end="  ")
print()

# 嵌套的列表生城市也可以用条件表达式
c = [  m+n for m in a for n in b if m+n < 250]
print(c)
#-----------------------------------------------------
#关于列表的常用函数
# len:求列表长度

a = [x for x in range(1,100)]
print(len(a))

# max:求列表中的最大值
# min： 同理
print(max(a))

b = ['man', 'film', 'python']
print(max(b))

# list：将其他格式的数据转换成list
a = [1,2,3]
print(list(a))

s = "I love xiaobaic"
print(list(s))

# 把range产生的内容转换成list
print(list(range(12, 19)))