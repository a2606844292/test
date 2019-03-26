#调用方法1
# import py_模块.mode
# print(py_模块.mode.a)
# print(py_模块.mode.plus(3,5))

'''
2. 使用模块
    导入模块的两种方式：
    方式1：import 包名.模块名 [ as 别名]
    方式2：from 包名 import 模块名
    from 包名.模块名 import 变量|函数|类
导入模块的代码可以放在任意位置，但一般都放在程序的开头

'''
# import py_模块.mode as m
# print(m.plus(3,5))

#方法二
# from py_模块 import mode
# print(mode.b)
# print(mode.plus2(8,2))

from py_模块.mode import b,plus,Calculator
from py_模块.mode import * #不建议

print(b)
print(plus(3,5))
print(Calculator.sum(3,12,5))


