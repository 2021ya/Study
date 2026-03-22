class Test(object):

    def __init__(self):
        self.a = 1
        self.b = 2


# 可以动态修改属性
p = Test()
p.a = 5
print("{}".format(p.a))

# 还能添加属性
p.c = 99
print("{}".format(p.c))

# 还能给整个类添加属性,让类初始的时候就有这个属性
Test.d = 666
print("{}".format(p.d))

# 还能添加函数？？？em，有点多余了吧？？
def test(self):
    print("test")

p.e = test
p.e(p)  # 这个p是将自身的引用传入

# 添加函数的第二种方法？？？不是这都有人用？
import types


p.f = types.MethodType(test, p)  # 这个p是将自身的引用传入，第一个为函数
p.f()  # 是在下无语了...

# 随意改也太随意了，那么可以这样限制一下
class A(object):

    __slots__ = 'x'  # 可以声明，只有哪些属性，然后就只有这些属性，注意：这个只在当前类中生效，如何其他类继承，那么其他类还是可以随意添加，只是限制了这个类而已

    def __init__(self):
        pass

