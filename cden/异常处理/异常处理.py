'''

try:
    可能出现异常的代码
except:
    出现异常后要执行的操作
else:
    不出现异常时执行的操作finally:无论是否出现异常都必须要执行的
'''

try:
    print('try....')
    a=5/int('abc')
# except:
# 捕获所有异常
# except ZeroDivisionError as e:
# 捕获ZeroDivisionError异常，获取到异常
except (ZeroDivisionError,ValueError,Exception) as e: # 捕获多个异常
    print('出现异常',e)
else:
    print('没有异常时执行')
finally:
    print('finally。。。')

# 自定义异常，继承自Exception(Exception类是所有异常类的
class UsernameExistsException(Exception):
    pass

def fn(username):
    if username == 'admin' or username == 'tom':
        raise UsernameExistsException('用户名已存在')
    else:
        print('ok')# 使用raise抛出异常



fn(input('请输入用户名:'))