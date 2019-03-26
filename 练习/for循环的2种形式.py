#方法1：range()+len()
lst=[1,2,3,4,5]
for i in range(len(lst)):
    print(i,lst[i])




#方法2：enumerate()
for index,value in enumerate(lst):
    print(index,value)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])
