# append()和extend()和insert()
# a = [1,2,3,4,5]
# a.append([6,7,8])       #添加到数组末尾
# print(a)
#
# b = [1,2,3,4,5]
# b.extend([6,7,8])       #添加到数组末尾不带[]
# print(b)
#
# c = [1,2,3,4,5]
# c.insert(3,10)          #在第三的位置添加一个10
# print(c)
#
# member = ["无敌","的","小白","是最帅的"]
# member.insert(1,99)
# member.insert(3,88)
# member.insert(5,77)
# member.append(666)
# print(member)
#
# # 请问如何将下边这个列表的'图灵学院'修改为'小白'？
# ls = [1, [1, 2, ['图灵学院']], 3, 5, 8, 13, 18]
#
# ls[1][2][0]='小白'
# print(ls)

# 将列表推导式还原出来
# ls=[(x,y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
# print(ls)

ls=[]
for x in range(10):
    for y in range(10):
        if x%2==0 and y%2!=0:
            ls.append((x,y))
print(ls)