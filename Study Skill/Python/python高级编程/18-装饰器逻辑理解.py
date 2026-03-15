def check_login(func):
    def inner():
        print("验证1")
        print("验证2")
        print("验证3")
        func()
    return inner


@check_login
def f1():
    print('f1')


# 不使用@符号时，实现方法
# f1 = check_login(f1)


f1()

"""
逻辑理解：
    定义f1函数时执行check_login(f1)  # 注意此时是传递的f1的引用
    f1原函数引用被func参数接收
    然后跳过执行inner()函数，执行"return inner"代码，此时将inner()函数引用返回给f1
    然后用户调用f1，此时是执行的inner()函数
    再之后执行inner()中的代码
    然后再次执行func()函数  # 此时执行的是原先f1函数的源代码
总结：
    这个装饰器的作用就是在不改变源函数代码的前提下新增其他功能
"""
