name_list = ["2021", "2022", "2023"]  # 列表的定义，用中括号来定义


# 列表的取值和取索引
print(name_list[1])  # 取值用中括号，起始索引为0，索引不能超出范围

# 若知道数据，但不知道索引
print(name_list.index("2023"))  # .index为索引，若要查询的值不在列表中会报错！

# 修改列表中的数据
name_list[1] = "二零二二"  # 修改列表中的数据需要指定索引位置，然后再进行修改，同样索引需要在范围内

# 追加数据
name_list.append("我是追加的数据")  # .append可以再列表后面追加数据
name_list.insert(0, "我是插入的数据")  # .insert是插入数据，第一个是索引，第二个是插入的数据
temporary_list = ["aaa", "bbb", "ccc"]
name_list.extend(temporary_list)  # .extend可以在当前列表的末尾加入另一个列表，合并？应该是的

# 删除数据
name_list.remove("bbb")  # .remove删除指定数据，若有重复数据，会删除第一个出现的数据
name_list.pop()  # 默认弹出最后一个数据
name_list.pop(5)  # .pop可以删除指定索引的值
name_list.clear()  # 清空列表
temp_list = ["aaa", "bbb", "ccc"]
del temp_list[1]  # 删除内存中的数据
name = "2021"
del name  # 还能删除变量

# 列表统计
print("数据有：", len(temp_list))
print("共出现：", temp_list.count("aaa"))  # 统计列表中某个值出现的次数

# 列表的排序
temp_name_list = ["bbb", "aaa", "ccc"]
temp_number_list = [2, 1, 3]
temp_name_list.sort()  # .sort可以使列表排序，默认空值为升序
temp_number_list.sort()
temp_name_list.sort(reverse=True)  # reverse(反转）默认等于False,等于Ture时，降序排列
temp_number_list.sort(reverse=True)
temp_name_list.reverse()  # .reverse直接将列表反转
temp_number_list.reverse()


print(temp_list)
print(name_list)
print(temp_name_list)
print(temp_number_list)
