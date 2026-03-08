# y = 2x + 1
"""
需求：
    通过生成器来实现坐标运算，并且将每次的y值当做下一个x的新值，初始x为0，并且可以自由控制需要的坐标数以及在运行数次之后还可以修改公式中2和1的值
"""


""" 第一次尝试
def deal_with():
    k = 2
    b = 1
    x = 0  # 设置x初始值
    while True:
        y = k * x + b
        new_k = yield  # 询问是否修改k值
        if new_k != k and new_k is not None:
            k = new_k
        new_b = yield  # 询问是否修改b值
        if new_b != b and new_b is not None:
            b = new_b
        yield x, y  # 返回当前坐标
        x = y  # 将y的值作为x的新值
"""


def deal_with():
    k = 2
    b = 1
    x = 0
    while True:
        y = k * x + b
        received = yield x, y  # 通过received来接受外部值
        if isinstance(received, tuple) and len(received) == 2:  # isinstance判断是否为已知类型
            k, b = received  # 如果外部调用.send来修改值，那么这里会进行修改
        x = y  # 将y值作为下一次x的新值


if __name__ == '__main__':
    test = deal_with()
    count = 0
    print(next(test))  # 启动生成器使用
    while True:
        if count == 5:
            break
        count += 1
        # print(next(test))
        print(test.send((3, 2)))  # 初始启动的生成器不可直接发送数据


"""
# count = 0
# run = 9  # 所得坐标数量
# run_num = run * 3
# while True:
#     if count == run_num:
#         break
#     count += 1
#     value = next(test)
#     if value is not None:
#         print(value)
"""
