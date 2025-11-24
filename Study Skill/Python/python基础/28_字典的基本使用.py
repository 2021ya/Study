i2021 = {"name": "2021",
         "age": 19}


# 字典的取值(使用中括号然后用key来查询）(可以理解为中括号中一直是key）
print(i2021["name"])

# 字典的添加中括号里放key，然后用等号来定义新的value（如果key不存在会新建key: value,如果key存在会修改key: value)
i2021["id"] = "1*************"
print(i2021)

# 字典的修改
i2021["id"] = "1####我是修改之后的##"
print(i2021)

# 字典的删除
i2021.pop("name")  # 使用.pop来删除，指定key来删除
print(i2021)

# 字典的统计
print(len(i2021))  # 同样使用len()函数

# 字典的合并
temp1 = {"temp1": 1,
         "temp2": 2}
i2021.update(temp1)  # 使用.update（更新）函数来合并，若有已存在的key，会覆盖
print(i2021)

# 清空字典
i2021.clear()  # 同样使用.clear来清空字典
print(i2021)










