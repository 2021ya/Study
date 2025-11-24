class Test(object):  # object是基类，正常情况下python3中如果这个类没有父类的话默认自动指定基类为object，但是python2中如果这个类没有父类的话，它不会指定基类，所以为了兼容，尽量自己写上吧

    def test1(self):
        print("A --- test1")

    def test2(self):
        print("A --- test2")


class Test2:

    def test2(self):
        print("B --- test2")

    def test1(self):
        print("B --- test1")


class Test3(Test2, Test):  # 子类继承两个父类，如果两个父类有两个相同的函数，优先执行先继承的那个父类函数（尽量不要有同名的函数，不然可能难阅读）

    pass


c = Test3()  # 创建对象的时候记得加括号

print(c.test1())
print(c.test2())

# 类的搜索顺序
# print(c.__mro__)  这个方法原本可以输出搜索顺序，但是mro函数输出错误了，可能已经删掉了



























