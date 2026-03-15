

def check_login(func):
    def inner(*args, **kwargs):  # 第一个参数可以接受无命名的多个参数，第二个参数可接受多个有命名的参数
        return "<b>{}<b>".format(func(*args, **kwargs))  # 将调用func()的函数结果返回给实际调用的函数
    return inner


def check_login2(func):
    def inner2(*args, **kwargs):  # 第一个参数可以接受无命名的多个参数，第二个参数可接受多个有命名的参数
        return "<i>{}<i>".format(func(*args, **kwargs))  # 将调用func()的函数结果返回给实际调用的函数
    return inner2


@check_login
@check_login2
def f1(input_):  # 此时有参数
    return input_


"""
逻辑说明：
    在执行到@check_login时，本来它会装饰下方的函数，但是下方也是装饰器，所以它将下方装饰器所装饰完毕的函数给一下装饰了
表面执行：
    先执行最靠近函数的装饰器，依次往上
"""


a = f1("这是测试文字")
print(a)
