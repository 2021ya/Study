from time import time


class Test(object):
    pass


def test():
    """这是文档说明"""
    pass


# 输出文档说明
print("打印文档说明：", test.__doc__)

# 输出模块位置
print("输出属性模块位置：", test.__module__)
print("输出属性模块位置：", time.__module__)

# 字典查询__dict__

print(Test.__dict__)
"""
这个方法可以将类名、方法名作为字典中的key值存储，将对应的数值来作为value，返回一个字典
"""
