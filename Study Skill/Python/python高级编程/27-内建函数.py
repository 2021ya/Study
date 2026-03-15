# 查看所有内建函数
print(dir(__builtins__))

# map函数
a = map(lambda x: x * x, [1, 2, 3])  # 逗号后面的参数是给x传的
print(a)
for i in a:
    print(i)
"""
map()函数第一个必须是函数，必须有返回值，后面是参数，依次传给第一个函数，然后返回函数结果
"""


def f1(x, y):
    return x, y


l1 = [0, 1, 2, 3, 4, 5, 6]
l2 = ['Sun', 'M', 'T', 'W', 'T', 'F', 'S']
l3 = map(f1, l1, l2)  # f1为函数，返回一个元组（x，y),l1与l2是对应x与y的参数
"""
map()函数第一个必须是函数，必须有返回值，后面是参数，依次传给第一个函数，然后返回函数结果
"""
print(list(l3))  # 最后将l3的映射转换为列表

# 过滤器
b = filter(lambda x: x >= 5, [1, 2, 3, 4, 5, 6])  # 第一个同样为函数，逗号之后为参数，符合条件Ture的留下，否则其余不留
print(list(b))


# reduce
from functools import reduce

c = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6])
print(c)
# 一次性从列表中取出两个值给x和y，将1和2相加为3，然后把3给x，继续取出3相加。。。
d = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6], 10)  # 如果后面有单独的数字，那么这个数字为x的初始值
print(d)


