from collections.abc import Iterable  # 判断是否为可迭代对象
from collections.abc import Iterator  # 判断是否为迭代器


class MyClass(object):
    """可迭代对象"""
    def __init__(self):
        pass

    def __iter__(self):  # 如果只拥有__iter__，那么这个实例为可迭代对象
        return MyIterClass()
    """
       作用：
           1，标记此实例为可迭代对象
           2，因为iter()函数是取出迭代器，所以这里返回对应的迭代器
    """


class MyIterClass(object):
    """迭代器(迭代器一定是可迭代对象，但可迭代对象不一定是迭代器)"""
    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):  # 如果同时拥有__iter__和__next__，那么这个实例为迭代器
        return "迭代器被调用"
    """
    作用：
        1，标记此实例为迭代器（必须同时拥有__iter__）
        2，当next()函数调用迭代器时，会执行__next__中代码
    """


"""
流程：
    创建一个可迭代对象，那么就是MyClass实例，这个实例可以被迭代，如果要取出此可迭代对象的迭代器，那么自动会调用可迭代对象中的__iter__函数来返回迭代器
    
"""

iterable = MyClass()  # 生成可迭代对象实例
print("{}是否为可迭代对象：".format("iterable"), isinstance(iterable, Iterable))
iterable_iter = iter(iterable)  # 取出迭代器
print("{}是否为迭代器：".format("iterable_iter"), isinstance(iterable_iter, Iterator))
print("通过next()来调用迭代器执行代码：", next(iterable_iter))
