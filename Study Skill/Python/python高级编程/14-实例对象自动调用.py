class Test(object):

    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __call__(self, x):
        print((x, self.k * self.b))


if __name__ == '__main__':
    test = Test(5, 5)  # 实例化对象
    test(1)  # 如果直接通过对象来调用，且没有用类中函数，那么会自动调用__call__方法
