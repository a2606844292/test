#1.定义函数使用def
#def calc(a,b):
#    res = a + b
#    return res
#print(calc(1,4))

#2.参数类型检查,求绝对值
#def my_abs(x):
#    if not isinstance(x,(int,float)):
#       raise TypeError("参数类型不正确，只能为数值类型")#抛出异常
#    if x>=0:
#        return x
#    if x<0:
#        return -x
#print(my_abs(1))
# 默认参数，即有默认值的参数案例
#def my_pow(x,y=2):
#    if y==0:
#       return 1
#    res = x
#   for i in range(y-1):
#        res *= x
#    return res
#print(my_pow(5,3))

#可变参数，使用*号，表示个数是可变的
#def my_sum(x,*y):
#    print(x)
#    print(y) #接收的实际是一个tuple
#my_sum(3,5,8,6,5,4)

#对于可变参数，可以直接传入list或tuple，只需在参数添加*号
#nums =[12,4,6,1,2,3,4]
#my_sum(12,*nums)

#关键词参数，使用**，也表示参数个数是可变的，但传递的是带名称的参数
#def f1(x,**y):
#    print(x)
#    print(y)    #接收到的实际是上一个的dict
#f1(3,a=5,b=9)

#user ={"id":1001,"name":"xiaobai","age":18}
#f1(4,**user)

#命名关键字参数，限制关键字参数的名字，使用*分隔，*号后面的参数表示命名的关键词参数
#def f2(x,*,name,age):
#    print(x)
#    print(name)
#    print(age)
#f2(4,name="xiaobai",age=20)

#接收任意参数
#def f3(*args,**kwargs):
#    print(args)
#    print(kwargs)
#f3(1,43,"aaa",name="xiaobai",age=20)
