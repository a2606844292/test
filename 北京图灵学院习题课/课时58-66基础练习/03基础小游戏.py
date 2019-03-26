# 判断年份是否为闰年
# year = input('请输入年份:')
# # 判断用户输入是否数字
# if year.isdigit():
#     year = int(year)
#     if year % 4 == 0:
#         print(str(year) + '是闰年')
#     else:
#         print(str(year) + '不是闰年')

# 给用户三次机会，猜想我们的程序生成的一个数字A，每次用户猜想过后会提示
# 数字是否正确以及用户数字是大于还是小于A，当机会用完提示输掉游戏

import random
secert =random.randint(1,100)
time = 3
while time:
    num=input('请输入数字')
    if num.isdigit():
        num=int(num)
        if num == secert:
            print('恭喜你猜对了')
            break
        elif num <secert:
            print('数字太小了')
        else:
            print('数字太大了')
    else:
        print('请输入数字')
