info_tuple = (1, 2, "aa", 1)  # 元组由括号定义，不能修改其内的数据
info2_tuple = (1,)  # 若只定义一个值，必须后面加一个逗号


print(info_tuple[2])  # 取值
print(info_tuple.count(1))  # .count统计出现的次数
print(info_tuple.index("aa"))  # 查询索引
print(len(info_tuple))  # len()可以统计列表和元组中数据的个数
