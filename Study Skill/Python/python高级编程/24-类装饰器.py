# 无参数实现方法
class Test(object):
    def __init__(self, func):
        # 原函数引用
        self.__func = func

    def __call__(self):  # __call__函数在直接执行对象时会自动调用
        print("testtesttesttesttest")
        self.__func()  # 再次解包


@Test
def test1():
    print('test1')


test1()


print("*" * 30)


# 有参数实现方法
class Test2(object):
    def __init__(self, a):
        # 传入的参数由a接收
        self.a = a

    def __call__(self, func):  # __call__函数在直接执行对象时会自动调用
        print("call方法执行")
        # 接受函数引用
        self.__func = func
        # 调用装饰器
        return self.b()

    def b(self):
        print("装饰器执行")
        return self.__func  # 返回数据给原调用位置


@Test2(100)  # 参数传给a,返回的是一个对象，然后自动执行__call__方法，此时执行此行是将test2的引用传给__call__方法
def test2():
    print('test2')
    return 1


print(test2())
