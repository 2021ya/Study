"""
生成器是一种特殊的迭代器
生成器是记录算法，需要时推导
"""

# 列表推导式
num_list = [x for x in range(10000000000000000000000000)]
# 说明：用一个变量来接收列表，for x in range(10)是正常的for循环，但是前面的x是后面for循环取出的每个元素都是最初列表的一个元素
print(num_list)

for num in num_list:
    print(num)

# 生成器创建方法一:如果将[]换为()那么，这个生成出来的是个生成器，没有数据，只有算法
num_tuple = (x for x in range(100000000000000000000000))
print(num_tuple)

for num in num_tuple:
    print(num_tuple)

"""
上方代码与下方代码理论上来说结果一样，区别就是，上方代码需要预先生成大量数据，下方代码需要时生成，那么就会出现上方代码会等很久很久，下方代码直接输出了

生成器本质也是迭代器，也可以用next()函数取数据
"""







