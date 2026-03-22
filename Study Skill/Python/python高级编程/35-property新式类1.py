class Test(object):

    def __init__(self):
        self.a = 1

    @property
    def a1(self):  # 如果只写入来方法，那么就是获取值，执行下方函数
        return self.a

    @a1.setter  # 设置新值时会自动调用下方函数
    def a1(self, value):
        self.a = value
        print('test_:{}'.format(value))

    @a1.deleter  # 删除属性时，会自动调用下方函数
    def a1(self):
        print("delete")


a = Test()
print("获取值：", a.a1)

a.a = 10086
print("修改之后的值：", a.a1)

del a.a1


"""
property使用方法：
    装饰器来装饰一个函数，如果外部需要取属性，那么会自动执行@property所装饰的函数，如果要修改那么会自动执行@xxx.setter所装饰的函数，同理删除属性也是如此
    但是，例如@property所装饰的函数名称为abc，那么剩下的装饰器前缀也都是abc，外部取值也是abc
注意：
    可以只有@property而没有剩下的
    在python2中只有第一个，没有剩下的两个
"""

