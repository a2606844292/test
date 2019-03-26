# # 假设x=1，y=2，z=3，如何快速将三个变量的值相互交换
#
# x = 1
# y = 2
# z = 3
#
# print(x, y, z)
#
# x, y, z = z, x, y
# print(x, z, y)
#
# # 成员运算符in的用法
#
# ls = range(101)
# if 100 in ls:
#     print(True)
# else:
#     print(False)
#
# # range函数,输出0-10的数字，2是步长，输出结果是0，2，4.。。。。。
# ls = range(0, 10, 2)
# for i in ls:
#     print(i)
#
# while True:
#     while True:
#         break
#         print(1)
#     print(2)
#     break
# print(3

i = 0
string = ('i am xiaobai')
while i < len(string):
    print(i)
    i += 1

# 设计一个验证用户密码的程序，用户只有三次机会，不过用户输入的内容包含"*"则不计算在内

password = '123456'

time = 3
while time:
    _password = input('请输入密码')
    if '*' in password:
        print('密码中不能包含*')
    else:
        if _password == password:
            print('登陆成功')
        time -= 1       #每循环一次就减去1
        exit()
else:
    print('密码错误，登陆失败')
