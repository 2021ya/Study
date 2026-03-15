

def check_login(func):
    def inner(*args, **kwargs):  # 第一个参数可以接受无命名的多个参数，第二个参数可接受多个有命名的参数
        print("验证1")
        print("验证2")
        print("验证3")
        func(*args, **kwargs)  # 这里会直接拆包然后自动从中取值

    return inner


@check_login
def f1(num1):  # 此时有参数
    print('f1', num1)


@check_login
def f2(num1, num2):
    print('f2', num1, num2)


@check_login
def f3(num1, num2, num3):
    print('f3', num1, num2, num3)


"""
因为f1在装饰器执行的时候，已经指向了inner()函数，所以参数应该在inner()内添加实参
最后又因为会通过func()执行原f1函数，所以func()函数中要把inner()中的实参写上
"""

f1(1)
f2(2, 3)
f3(4, 5, 6)




