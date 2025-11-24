def demo(num, num_list_):
    print("传入数字为", num)
    num = 100
    # num_list_ = [1, 2, 3, 4, 5]
    print(num_list_)
    print("函数内部参数为", num)
    num_list_.append(699)
    num_list_ += num_list  # +=这个字符也能修改外部数据的原因是+=这个字符是调用了.extend方法
    print(num_list_)


qj_1 = 99
num_list = [4, 5, 6, 7, 8, 9]
demo(qj_1, num_list)  # 传入全局变量不可变类型99，输出内部变量100
print(qj_1)
print(num_list)  # 传入全局可变类型变量，输出内部变量，外部变量不受影响

# 从上方代码可以看出，局部变量优先级高于全局变量，而在内部使用赋值语句对变量进行修改，不会影响外部的变量，在函数体内部使用的赋值语句，只会在函数体内部生效
# 而在函数内部调用方法之后才会修改值
