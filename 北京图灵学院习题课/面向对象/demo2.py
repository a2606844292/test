import random



#定义一个变量用于存取初始分数
while 1:
    num = input('输入1,2,3三个数字:')
    if num =='-1':
        break
    rand_num = random.randrange(1, 4)
    num = int(num)
    rand_num = int(rand_num)
    source = 0
    if num > rand_num:
        print('输入的数比随机数大')
    elif num == rand_num:
        source += 100
        print('分数为', source)
    elif num < rand_num:
        print('输入的数比随机数小')
