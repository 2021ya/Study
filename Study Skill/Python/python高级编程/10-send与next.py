def test():
    while True:
        num = yield 100  # 此处num并不会被赋值，而是外部如果使用了send()函数的话，会传入一个值，而num变量就是用来接收这个值的
        print(num)


if __name__ == '__main__':
    gen = test()  # 创建生成器
    print(next(gen))  # 正常调用，num会返回None
    print("---")
    print(gen.send(10))
    # 如果要调用send，那么需要用生成器里面的函数,例如gen.send()  注意：如果是第一次执行生成器，那么不可以使用.send()函数
    # 需要先调用一次next(),如果非要使用，那么调用.send()函数时传入None
    """     --代码分析
    100  # 生成器挂起时返回的是yield的值，num的打印并没有执行
    ---
    10  # 使用.send()函数传入10，执行了打印代码，然后开启第二次循环
    100  # 返回yield的值
    """
