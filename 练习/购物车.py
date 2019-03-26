goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]

shopping_menu = []
username = 'xiaobai'
password = '123456'

usernames = input("username:")
passwords = input("password:")

if usernames == username and passwords == password:
    print("----Welcome", username, "----")
    pay = int(input("你的工资是：")
else:
    print('您输入的账号或密码有误，请重新输入')



