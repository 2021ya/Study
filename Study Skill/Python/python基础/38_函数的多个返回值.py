def eg():
    print("start...")
    temp = 39
    temp2 = 99
    print("end...")
    print(temp)
    # return (temp, temp2)  # 返回一个元组，可包含多个数据
    return temp, temp2  # 若返回的是元组数据，括号可以省略不写


result = eg()  # 一次接受一个元组数据
print(result)

# 单独处理数据时，需要将两个数据拿出来，清晰可见-----不够好吗？？
qj_temp = result[0]
qj_temp2 = result[1]

print(qj_temp)
print(qj_temp2)

# 可以直接接受两个数据并分给两个变量。。。-----好，还能这样写，长知识了
qj_temp_1, qj_temp_2 = eg()
"""
上方代码的意思是
qj_temp_1 = 返回值的第一个数据
qj_temp_2 = 返回值的第二个数据
"""
print(qj_temp)
