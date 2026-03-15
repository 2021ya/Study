def check_login(func):
    def inner(a, b):
        print("验证1")
        print("验证2")
        print("验证3")
        func(a, b)
    return inner


@check_login
def f1(num1, num2):  # 此时有参数
    print('f1', num1, num2)


"""
因为f1在装饰器执行的时候，已经指向了inner()函数，所以参数应该在inner()内添加实参
最后又因为会通过func()执行原f1函数，所以func()函数中要把inner()中的实参写上
"""

f1(1, 2)
