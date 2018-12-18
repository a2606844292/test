'''
变量作用域scope:值得是变量生效的区域

两种作用域
1.全局作用域
    函数以外的区域都是全局作用域
    在全局作用域定义的变量，都是全局变量
2.函数作用域，也称为局部作用域
    函数内的区域，每调用一次函数就会创建一个新的函数作用域
    在函数作用域定义的变量，都是局部变量
'''

# a = 5 #全局变量
#
# def fn():
#     b=8
#     print("函数内部:a=",a)
#     print("函数内部:b=", b)
# fn()

# global关键字
# def fn2():
#     global a
#     a = 10
#     print("函数内部:a=", a)
# fn2()
#
# print("函数外部a=",a)

'''
命名空间namespace:指的是存储的位置，每个变量都存储在指定的命名空间

每个作用域都有一个对应的命名空间
全局命名空间，用来存储全局变量：函数命名空间，用来存储函数中的变量
命名空间实际上就是一个字典dict
'''


# locals()获取当前作用域的命名空间
# scope = locals()#在全局作用域中调用locals(),获取就是全局命名空间
# print(scope)
# print(type(scope))

# 通过scope操作命名空间的变量
# print(scope["a"])
# scope["c"]=666
# scope['z']="tom"
# print(scope['c'])
# print(scope['z'])
# print(z)


# def fn3():
#     a = 888
#     scope = locals()    #获取到的函数命名空间
#     print(scope)
# fn3()

#globals() 可以在任意位置获取全局命名空间
# globals_scope = globals()
# print(globals_scope)
# print(globals_scope["a"])