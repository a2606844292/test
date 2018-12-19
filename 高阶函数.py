'''
高阶函数：一个函数接收另一个函数作为参数，这种函数称为高阶函数
'''

nums = [12, -4, 2, -1, 12, 35, 213, 142, 14414]


# 定义一个函数，用来检查数字是否大于5
# 自定义高阶函数，用来过滤列表中的元素

def f1(x):
    if x > 5:
        return True
    return False


def fn(fun, lst):
    '''

    将列表中所有符合条件的元素筛选出来，返回一个新的列表
    :param fun:
    :param lst:
    :return:
    '''
    new_list = []
    for i in lst:
        if fun(i):
            new_list.append(i)
        return new_list


nums1 = fn(f1, nums)
print(nums1)

#

def f2(x):
    return x % 2 == 0
print(fn(f1, nums))

#内置高阶函数filter()，用于序列
num2 = filter(f1,nums)
print(list(num2))

#内置高阶函数map(),用于处理序列
def f3(x):
    return x * x


num3 = map(f3, nums)
print(list(num3))

#内置高阶函数，sort(),用于排序
print(sorted(nums))
print(sorted(nums,key=abs))