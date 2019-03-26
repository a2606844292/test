def max_min(the_list):
    # for i in the_list:
    #     if the_list.index(i) == 0:  # 如果the_list的索引值i等于0的时候，把i赋值给max和min
    #         max_value = i
    #         min_value = i
    #     the_list.pop(0)
    #
    #     for j in  the_list:
    #         if j >max_value:
    #             max_value=j
    #         if j < min_value:
    #             min_value = j
    # print(max_value, min_value)

    max_value=the_list[0]
    min_value=the_list[0]
    for j in the_list:
        if j > max_value:
            max_value = j
        if j < min_value:
            min_value = j
    print(max_value, min_value)




if __name__ == '__main__':
    num = [1, 0, 4, 2, 3]
    max_min(num)


'''
    1 0 4 2 3
    ---------
    max 1 1 4 4 4 4
    min 1 0 0 0 0 0

    max     min
    1 vs 0
    1 vs 4
    4 vs 2  0 vs 2
    4 vs 3  0 vs 3



'''