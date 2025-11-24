try:  # 尝试执行下方代码，如果有错误，执行except语句
    user_input = int(input("Please input a number: "))
    new_num = 8 / user_input
    print(new_num)
except ValueError:  # 针对不同错误，对应不同处理办法
    print("value error")
except ZeroDivisionError:
    print("ZeroDivisionError")
except (TypeError, object):  # 也可同时处理多个错误
    print("TypeError")
except Exception as result:  # 第一个是未知错误的报错，第二个是接收未知错误,第二个是变量，可以自己写
    print("Unknown Error: %s" % result)
else:  # 没有异常才会执行的代码
    print("尝试执行成功")
finally:  # 无论是否有异常，都会执行
    print("无论是否执行成功都会执行")

print("程序外部代码")
