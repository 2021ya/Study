"""
需求：
公式：y = 2x + 1
初始值x为0，下次y的结果作为x的值
坐标自定义生成个数
"""


# 尝试一：自我思考
def test(b, c):
    """计算一元一次方程"""
    count = 0  # 循环次数控制
    x = 0  # 初始值
    while True:
        if count == 3:  # 退出循环
            break
        y = b * x + c  # 运算
        print("输出坐标:({},{})".format(x, y))
        x = y  # 结果当做下一次x的值
        count += 1


# 尝试二：迭代器实现
class Test1(object):
    """可迭代对象和生成器可以合成一个，那么就是定制迭代器，但多任务的时候可能会出问题，具体情况具体使用"""

    def __init__(self, b, c):
        self.x = 0  # x初始数据
        self.b = b
        self.c = c
        self.data = []  # 存储数据,被遍历时，返回值
        self.current = 0  # 记录当前访问位置

    def __iter__(self):
        return self  # 使自己为可迭代对象，提取迭代器时返回自身

    def __next__(self):
        """迭代器运算"""
        # if 0 < self.current < len(self.data):
        y = self.b * self.x + self.c  # 运算
        self.data.append((self.x, y))
        self.x = y  # 结果当做下一次x的值
        data = self.data[self.current]
        self.current += 1  # 位置加一
        return data  # 若被迭代，返回数据
        # else:
        #     self.current = 0  # 重置
        #     self.x = 0
        #     raise StopIteration


if __name__ == '__main__':
    print("*" * 30)
    test(2, 1)
    print("*" * 30)
    test1 = Test1(2, 1)  # 实例化对象
    test1_iter = iter(test1)  # 提取迭代器
    print(next(test1_iter))
    print(next(test1_iter))
    print(next(test1_iter))
    # 自己选择调用次数
    count = 0
    while True:
        if count == 5:
            break
        count += 1
        print(next(test1_iter))
        print(type(next(test1_iter)))




