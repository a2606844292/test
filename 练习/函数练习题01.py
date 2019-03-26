'''
1.设计一个重量转换器，输入以g为单位得数字后返回值为kg得结果
2.设计一个求直角三角形斜边长得函数(两条直角边为参数，求最长边)

'''

# def fun(g):
#     kg = str(g / 1000) + 'kg'
#     return kg
# print(fun(2000))


def theorem(a,b):
    c=(a**2 * b**2)**(1/2)
    return c
print(theorem(3,4))