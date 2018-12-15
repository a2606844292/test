#try：
#   year=int(input("input year:"))
#except ValueError:
#    print("年份需要输入数字")



#try:
#    print(1/"a")
#except Exception as e:#将错误信息赋值e输出
 #   print("%s" %e)

#try:$把错误全部输出
#    raise  NameError("HELLOeRROR")
#except NameError:
#    print("my custom error")

try:
    a = open("name.txt")
except Exception as e:
    print(e)
finally:
    a.close()