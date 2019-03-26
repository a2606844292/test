menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

menul = []
while True:
    for key in menu:
        print(key)
    print('退出请输入s')
    write = input('选择查询的城市:').strip()
    if write == 's':
        break
    if write in menu:
        menul.append(menu)  # 添加到menu1这个列表中
        menu = menu[write]  # 在menu中取得对应的value值
    else:
        continue
