# 写一个程序来管理用于登陆系统的用户信息：登陆名字和密码。
# 登陆用户账号建立后，已存在用户可以用登陆名字和密码重返系统，
# 新用户不能用别人的用户名建立用户账号

# 模拟从数据库里取出来的用户名和密码
user_pass={'xiaobai':'123456','xiaoming':'654321'}

def create_user(username,password):
    """
    username:用户建立账号的用户名
    password：用户建立账号的密码
    """
    # 判断 用户输入的账号是不是已经存在
    usernames = user_pass.keys()
    if username in usernames:
        print('登陆成功')
    else:
        # 没有被注册，那么就更新我们的user_pass
        # 实际情况是会做持久化存储到数据库中
        user_pass[username] = password
        print("恭喜你，你已经很荣幸的成为了我们的会员")
# create_user("goudan","123")
#
# print(user_pass)


def login_user(username,password):
    # 首先要判断登陆的用户名是否存在
    usernames=user_pass.keys()
    if username not in usernames:
        print('用户不存在')
    elif password != user_pass[username]:
        print('密码不正确')
    else:
        print('登陆成功')
login_user('xiaobai','123456')


