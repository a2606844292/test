# 编写程序，要求用户输入1-100之间的整数并且判断，输入符合要求的打印小白真帅
name = input('请输入1-100之间的整数')
print(type(name))
if name.isdigit():  # 判断是否整数
    name = int(name)
    if 1<=name<= 100 :
        print('小白真帅')
    else:
        print('输入有误，请重新输入')
