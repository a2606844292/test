for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n)
            break
    else:
        # 循环中没有找到元素
        print(n,'是质数')