'''
迭代:也称为遍历，循环获取每一个元素
'''

import collections  # 导入模块

# for i in ['tom', 'xiaobai', 'xxxx']:
#     print(i, end=' ')
#
# for i in ("xiaobai", "xiaoming"):
#     print(i, end=' ')
#
# for k, v in {"name": "tom", 'age': 18, 'sex': 'male'}.items():
#     print(k, v)
#
# for i in 'hello':
#     print(i)

# 判断对象是否是可迭代的
# print(isinstance('hello', collections.Iterable))

# 获取索引值
# name = ['tom', 'xiaobai', 'alice']
# for i in range(len(name)):
#     print(i, name[i])
#
# # 方式二：使用enumeract()函数，转换为索引-元素对
# print(enumerate(name))
# print(isinstance(enumerate(name), collections.Iterable))
# for k, v in enumerate(name):
#     print(k, v)

'''
列表生成表式，用来创建list的生成式
'''
#生成[0,99]的list
# num = list(range(0, 100))  # 转换成list
# print(num, type(num))
#
# for i in num:
#     print(i)

#生成一个包含(1,100)之间所有3的倍数的list
#方法一
lst=[]
# for i in  range(1,101):
#     if i %3 == 0:
#         lst.append(i)
# print(lst)

#方法二
lst = [i for i in range(1, 101) if i % 3 == 0]
print(lst)
