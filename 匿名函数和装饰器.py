'''
匿名函数：没有名字的函数
'''

nums = [12, 4, 32, 5, 23, 7]


# def fn(x):
#     return x * 2 + 1


nums_new = list(map(lambda  x: x * 2 + 1,nums)) #x是参数，：后面的是返回值
print(nums_new)

#将匿名函数赋给变量(不建议)
a = lambda x : x+1
print(a(2))

'''
装饰器：在代码运行期间动态增加啊功能的方式，称为装饰器Decoration，类似于AOP

'''
#定义一个装饰器，为函数添加打印日志的功能
def log(func):
    def wrapper(*args, **kw):
        print('开始执行 %s():' % func.__name__)
        return func(*args, **kw)
        print('函数结束 %s():' % func.__name__)
    return wrapper  #返回装饰函数

@log
def even(lst):
    for i in lst:
        if i % 2 == 0:
            print(i)
@log
def calc(num1,num2):
    res = num1 + num2
    return res
even([12,32,2,23,23,23,23,23])