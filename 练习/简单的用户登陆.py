username=['xiaoming','xiaobai','xiaohao']
password='123456'


for i in range(3):
    Username = input('please input your username:')
    Password = input('please input your password:')
    if Username in username and Password == password:
        print('登陆成功')
        break
    else:
        print('登陆失败')
        if i>=3:
            exit()








