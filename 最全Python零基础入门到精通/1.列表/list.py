movies=['肖申克的救赎','1994','佛兰克.德拉邦特',['蒂姆.佛里曼','鲍勃','威廉姆','克兰西']]

# for each_item in movies:
#     if isinstance(each_item,list):    #判断循环内是否列表
#         for item in each_item:
#             print(item)
#     else:
#         print(each_item)

def prints(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print(each_item)
        else:
            print(each_item)

prints(movies)