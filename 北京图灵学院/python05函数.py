'''
四类参数，普通参数，默认参数，关键字参数，收集参数
关键字参数开始
语法
  def func(p1=v1, p2=v2.....):
      func_body
  调用函数：
  func(p1=value1, p2=value2.......)
比较麻烦，但也有好处：
不容易混淆， 一般实参和形参只是按照位置一一对应即可，容易出错
使用关键字参数，可以不考虑参数位置
'''

# #普通参数
# def stu(name, age, coutry):
#     print('I am a student')
#     print('我叫{0},我今年{1},我来自{2}'.format(name, age, coutry))
#
# n = '小白'
# a = 18
# c = 'chain'
# stu(n, a, c)

# #关键字参数
# def stu(name='no name', age=0, coutry='cn'):
#     print('I am a student')
#     print('我叫{0},我今年{1},我来自{2}'.format(name, age, coutry))
#
# n = '小白'
# a = 18
# c = 'chain'
# stu(name=n, age=a, coutry=c)
# -----------------------------------------------------------
#收集参数
# 把没有位置，不能和定义时的参数位置相对应的参数，放入一个特定的数据结构中
# 语法
#   def func(*args):
#       func_body
#       按照list使用方式访问args得到传入的参数
#   调用：
#   func(p1, p2, p3, .....)
# 参数名args不是必须这么写，但是，我们推荐直接用args，约定俗成
# 参数名args前需要由星号
# 收集参数可以和其他参数共存
# -----------------------------------------------------------
# 收集参数代码
# 函数模拟一个学生进行自我介绍，但具体内容不清楚
# args把他看做一个list
# def stu(*args):
#     print('大家好，这是我的自我介绍')
#     # type函数作用是检测变量的类型
#     for item in args:
#         print(item)
#
# stu('xiaobai', 18, '广东佛山顺德区', 'xiaohei', 'single')
# stu('xiaoming')
# -----------------------------------------------------------
# 收集参数之关键字收集参数
# 把关键字参数按字典格式存入收集参数
# 语法：
#
#   def func( **kwargs):
#       func_body
#
#   # 调用：
#   func(p1=v1, p2=v2, p3=v3........)
# kwargs一般约定俗成
# 调用的时候，把多余的关键字参数放入kwargs
# 访问kwargs需要按字典格式访问

# def stu(**kwargs):
#     print('大家好，这是我的自我介绍')
#     print(type(kwargs))
#     #对于字典的访问，python2和3有区别
#     for k,v in kwargs.items():
#         print(k,'-----',v)
#
# stu(name='xiaobai', age=18, addr='广东佛山顺德区', love='xiaohei', work='student')
# -----------------------------------------------------------

'''
收集参数混合调用的顺序问题
收集参数，关键字参数，普通参数可以混合使用
使用规则就是，普通参数和关键字参数优先
定义的时候一般找普通参数，关键字参数，收集参数tuple，收集参数dict
'''


# 收集参数混合调用案例
# stu模拟一个学生的自我介绍
# def stu(name, age, *args, hobby="没有", **kwargs):
#     print("Hello 大家好")
#     print("我叫 {0}， 我今年{1}大了。".format(name, age))
#     if hobby == "没有":
#         print("我没有爱好， so sorry")
#     else:
#         print("我的爱好是{0}".format(hobby))
#     print("*" * 20)
#     for i in args:
#         print(i)
#     print("#" * 30)
#     for k, v in kwargs.items():
#         print(k, "---", v)
# # 开始调用函数
# name = "liuying"
# age = 19
# # 调用的不同格式
# stu(name, age)
#
# stu(name, age, hobby="游泳")
#
# stu(name, age, "xiaobai", "xiaoming", hobby="游泳", hobby2="烹饪", hobby3="睡觉")

'''收集参数的解包问题
把参数放入list或者字典中，直接把list/dict中的值放入收集参数中
语法：参看案例'''

# def stu(*args):
#     print('....')
#     for i in  args:
#         print(type(i))
#         print(i)
#
# stu('xiaobai',18,200)
#
# l =['xiaobai',23,'xiaoming']
#
# stu(*l)
# #此时，arg的表示形式是字典内的list类型的元素，即arg=['xiaobai',23,'xiaoming']
# #此时的调用，我们需要解包符号，即调用的时候，调用的时候前面加一个星号
# #同理，dict类型收集参数一样可以解包，但是¶
# # 对dict类型进行解包
# # 需要用两个星号进行解包
#-----------------------------------------------------
# 返回值
# 函数和过程的区别
# 有无返回值
# 需要用return显示返回内容，
# 如果没有返回，则默认返回None
# 推荐写法，无论有无返回值，最后都要以return 结束

# def func_1():
#     print('yes')
#     return 1
# def func_2():
#     print('no')
#
# print(func_1())
# print(func_2())
#-------------------------------------------------------
# 函数文档
# 函数的文档的作用是对当前函数提供使用相关的参考信息
# 文档的写法：
# 在函数内部开始的第一行使用三引号字符串定义符
# 一般具有特定格式
# 参看案例
# 文档查看
# 使用help函数，形如 help(func)
# 使用doc, 参看案例

# def stu(name,age,*args):
#     '''
#     这是第一行
#     这是第二行
#     这是第三行
#     '''
#
# help(stu)
# stu.__doc__
