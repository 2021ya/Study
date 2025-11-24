def sum_number(num):
    print(num)
    if num == 0:  # 同样函数需要出口，像循环一样，否则会死循环
        return  # 条件成立，下方代码不执行，返回调用函数的地方（逐层返回）
    sum_number(num - 1)  # 递归的意思就是自己调用自己


sum_number(9)







