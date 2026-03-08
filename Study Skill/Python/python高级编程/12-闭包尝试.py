# 闭包：一个函数中嵌套另一个函数，并且另一个函数用到了外部函数的参数或局部变量，那么这就是闭包


def person(user_name):
    def say(massage):
        print(user_name + ": " + massage)
    return say  # 注意：带括号是先调用再返回，不带括号是返回函数的引用并不会调用


if __name__ == '__main__':
    # 调用函数
    xx = person('xx')
    xx("Hello World!")
    # 闭包并不会释放空间，你调用一百次person函数，那么就会有100个这样的内存空间，需要手动释放
    # 在python中，引用为0时，系统会自己释放空间
    del xx  # 所以用到了del函数
