def sum_number_end(num):
    if num == 1:  # 函数出口
        return 1  # 逐层返回
    # temp = sum_number_end(num - 1)
    """
    整体：传入3执行函数体，传入2，执行函数体 | 传入1成立，返回上一步，执行1+2返回3，返回上上步，3+3=6
    """
    # return num + temp
    return num + sum_number_end(num - 1)
    # 在我突然灵机一动，发现这好像是sum_number_end = aₙ + (for循环遍历的)aₙ₋₁ （这个for循环终止就是上方的if语句）


print(sum_number_end(3))


"""
代码执行流程思考图

----递归0层

def sum_number_end(num):                                -----传入3
    if num == 1:                                        -----不成立跳过
        return 1  # 逐层返回                              -----不执行
    temp = sum_number_end(num - 1)                      -----temp = sum_number_end(3 - 1)  也就是：temp = sum_number_end(2)
    return temp + num                                   -----进入temp = sum_number_end(2)内部，还未执行
    


----递归1层，进入temp = sum_number_end(2)
    
    def sum_number_end(num):                                -----传入2
        if num == 1:                                        -----不成立跳过
            return 1  # 逐层返回                              -----不执行
        temp = sum_number_end(num - 1)                      -----temp = sum_number_end(2 - 1)  也就是：temp = sum_number_end(1)
        return temp + num                                   -----进入temp = sum_number_end(1)内部，还未执行
        
        
        
--------递归2层，进入temp = sum_number_end(1)
        
        def sum_number_end(num):                                -----传入1
            if num == 1:                                        -----成立
                return 1  # 逐层返回                              -----执行，返回1，并返回上一次调用函数的代码（返回到递归1层）
            temp = sum_number_end(num - 1)                      -----因为return返回，所以代码不执行了
            return temp + num                                   -----因为return返回，所以代码不执行了



----返回上一次调用函数的代码（返回到递归1层），temp = sum_number_end(2)
    
    def sum_number_end(num):                                -----已执行（当前递归num = 2）
        if num == 1:                                        -----已执行
            return 1  # 逐层返回                              -----已执行
        temp = sum_number_end(num - 1)                      -----已返回到temp = sum_number_end(2 - 1)  也就是：temp = sum_number_end(1)返回的是1，所以temp = 1，当前num = 2
        return temp + num                                   -----返回temp + num 即 1 + 2 = 3，并返回上一次调用函数的代码（返回到递归0层）
        
        
        
---递归0层

def sum_number_end(num):                                -----已执行（当前递归num = 3）
    if num == 1:                                        -----已执行
        return 1  # 逐层返回                              -----已执行
    temp = sum_number_end(num - 1)                      -----temp = sum_number_end(3 - 1)  也就是：temp = sum_number_end(2)返回的是3，所以temp = 3，当前num = 3
    return temp + num                                   -----返回temp + num 即 3 + 3 = 6，函数体执行完毕
        
        
"""
