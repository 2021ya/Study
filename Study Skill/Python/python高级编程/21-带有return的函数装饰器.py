

def check_login(func):
    def inner(*args, **kwargs):  # 第一个参数可以接受无命名的多个参数，第二个参数可接受多个有命名的参数
        print("验证1")
        print("验证2")
        print("验证3")
        return func(*args, **kwargs)  # 将调用func()的函数结果返回给实际调用的函数

    return inner


@check_login
def f1(num1):  # 此时有参数
    print('f1', num1)
    return 100
    # 此时的num1是返回到了inner()函数中，但是打印a时执行的inner()函数，没有返回值
    # 所以解决办法就是在inner()函数中加上return，将func()的返回值给返回实际调用的那个地方去


@check_login
def f2():
    print('f2')
    # 没有返回值时，会返回None


a = f1(1)
print(a)
f2()
