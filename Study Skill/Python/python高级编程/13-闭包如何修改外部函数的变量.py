def counter(start=0):
    def add_one():
        nonlocal start  # 修改全局变量是用global,在闭包中，修改外部函数变量需要使用nonlocal
        start += 1
        return start
    return add_one


"""
闭包中还可以有多个函数，但一般不这样做
"""


# 创建一个闭包
c1 = counter(5)
print(c1())
# 创建另一个闭包
c2 = counter(50)
print(c2())
# 不需要时释放
del c1, c2
