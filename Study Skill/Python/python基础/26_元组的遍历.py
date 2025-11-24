info_tuple = ("2021", 18, 1.80)

for my_tuple in info_tuple:
    print(my_tuple)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(num_list))
num_tuple = tuple(num_list)  # 可以将列表转换为元组,但是前面需要定义一个变量（相当于你把文件复制到本地一份才能修改）
print(type(num_tuple))


list_info = list(info_tuple)  # 同理
print(type(list_info))















