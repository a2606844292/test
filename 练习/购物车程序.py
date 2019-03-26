goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
shopping = []
username = ['xiaobai']
password = ['123456']

_username = input("用户名：")
_password = input("密码：")

if username[0] == _username and password[0] == _password:
    print("登录成功！")
    salary = input("输入工资：")
    if salary.isdigit():
        salary = int(salary)
        while True:
            for k, v in enumerate(goods):
                print(k, v)                 #打印商品列表

            user_choice = input("选择要购买商品，输入该商品编号>>>:")

            if user_choice.isdigit():                   #检测字符串是否只由数字组成
                user_choice = int(user_choice)          #转换成int类型

                print('请输入商品编号。。。。。。')
                if user_choice < len(goods) and user_choice >= 0:
                    item = goods[user_choice]

                    if item["price"] <= salary:
                        shopping.append(item)
                        salary = salary - item["price"]
                        print("还剩\033[31;1m%s\033[0m" % (salary))
                    else:
                        print("余额不足")
                else:
                    print("商品不存在")
            elif user_choice == 'q'or user_choice=='n':
                print("----------shopping list----------")
                print('输入q查询余额，输入n退出程序')

                for p in shopping:
                    print(p)

                print("余额还剩\033[31;1m%s\033[0m" % (salary))
                exit()
            else:
                print("无效选项")

else:
    print("登录失败！")



