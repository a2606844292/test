#空函数
#def empty():
#    pass    #s使用pass表示函数暂时不写


#函数返回值
#def f1():
#    name = "xiaobai"
#    age = 20
#    sex ="male"
#    return name,age,sex

#print(f1()) #返回值实际上是一个元组
#a,b,c=f1()
#print(a,b,c)

#def f2(x):  #定义参数为f2,形参为x
#   z = 6   #定义一个变量z = 6
#    def f3(y):  #定义参数为f3,形参为y
#        print( x * y + z)   #输出x*y+z,内部函数使用外部函数的参数或局部变量，称为闭包
#    return f3   #返回f3

#fn=f2(2)    #将f2赋值给fn
#fn(5)       #调用

#递归函数:一个函数在内部调用自身，这个函数就是递归函数
#计算x的y次方
#常规方法
#def calc(x,y):
#if y == 0:
#    return 1
#    i = 1
#    res = x
#    while i<y:
#        res*=x
#        i+=1
#    return  res
#print(calc(2,3))
#递归方式
#2*2*2*2*2=2*(2*2*2*2)=2*(2*2*2)=
# def calc(x,y):
#     if y ==0:
#         return 1
#     else:
# return x * calc(x, y - 1)  #2x(2,2)不停的调用自己，调用一次减去一个1，太大会导致溢出
# print(calc(2,3))





