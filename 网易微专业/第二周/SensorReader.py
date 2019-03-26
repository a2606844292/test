try:
    f = open('E:\sensor.txt', 'r')      #数据源没有只能随便放了
    avg, cnt = 0, 0
    for line in f:
        ls = line.strip()
        cnt += 1
        avg += eval(ls[2])
    print('平均的温度值是:{:.2f}'.format(avg / cnt))
    f.close()
except:
    print('文件打开错误')

