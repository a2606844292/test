'''
六、模块1. 简介模块化是指将一个程序分解为一个个的模块module，
通过组合模块来搭建出一个完整的程序
    优点：便于团队开发、方便维护、代码复用在Python中一个.py文件就是一个模块，
    创建模块实际上就是创建一个.py文件，可以被其他模块导入并使用注意：
    自定义模块时要注意命名规范，使用小写，不要使用中文、特殊字符等不要与内置模块

'''

# 在模块中定义变量

a = 10
b = 20


# 在模块中定义函数
def plus(x, y):
    '''
    加法
    :param x:
    :param y:
    :return:
    '''
    return x + y


# 在模块中定义函数
def plus2(x, y):
    '''
    减法
    :param x:
    :param y:
    :return:
    '''
    return x - y

#在模块中定义类
class Calculator:
    @classmethod
    def sum(cls,*nums):
        res =0
        for n in nums:
            res += n
        return res
print(Calculator.sum(2,3,4))

'''
__name__属性是模块的内置属性
当该.py文件是主执行文件，直接被执行时，其值为__main__
当该.py文件被调用，导入执行时，其值为模块名

'''
#程序入门，类似于java的main()方法，只在当直接调用文件时才会执行
# print(__name__)

if __name__ == '__main__':
    print(Calculator.sum(2,3,5))
