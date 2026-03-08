from collections.abc import Iterable


class MyClass(object):

    def __init__(self):
        self.list = []

    def __iter__(self):
        """只要类中有此函数，不需要写任何代码，就认为，此类可迭代，类似于名片"""
        """如果一个类中同时拥有了__iter__和__next__那么创建出来的方法一定是迭代器，那么就可以遍历了"""
        """
        作用：
            1，标记此实例为可迭代对象
            2，返回对应的迭代器
        """
        pass

    def add(self, data):
        self.list.append(data)


if __name__ == '__main__':
    test = MyClass()
    test.add(1)
    test.add(2)
    test.add(3)
    # 判断是否为iterable
    print(isinstance(test, Iterable))
    for i in test:
        print(i)
