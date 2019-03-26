# 导入urllib中的request模块，用来发送http/https

from urllib import request


# 获取数据
def get_data():
    url = 'https://search.51job.com/list/030600,000000,0000,00,9,99,web%E5%89%8D%E7%AB%AF,2,3.html'
    # 创建request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    # print(type(response))
    print(response.getcode())   #响应状态码
    # print(response.info())

    if response.getcode() == 200:
        data = response.read()  # 读取响应结果
        # print(type(data)) # bytes类型
        data = str(data, encoding='gbk')  # 转换为str
        # print(data)

        # 将数据写入文件中
        with open('index.html', mode='w', encoding='gbk') as f:
            f.write(data)


if __name__ == '_main_':
    get_data()

get_data()
