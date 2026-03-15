import time


def a(time_out=0):
    def check_login(func):
        def inner(*args, **kwargs):  # 第一个参数可以接受无命名的多个参数，第二个参数可接受多个有命名的参数
            time.sleep(time_out)
            return "<b>{}<b>".format(func(*args, **kwargs))  # 将调用func()的函数结果返回给实际调用的函数
        return inner
    return check_login


@a(3)  # 带参数只需要多套一层即可，但最终执行都是最内层执行
def f1(input_):  # 此时有参数
    return input_


a = f1("这是测试文字")
print(a)
