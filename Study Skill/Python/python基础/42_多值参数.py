# 一个参数可以接收多数据
def dome(num, *args, **kwargs):  # 通常的时候元组用*args，字典用**kwargs
    print(num, "一个*是元组 ", args, "两个*是字典", kwargs)


dome(1)
dome(1, 2, 3, 4, 5)  # 如果没有指定参数，那么第一个值会被第一个参数接收，剩下的都会放到第二个参数接收
dome(1, 2, 3, 4, 5, key="value", age=18)  # 调用参数的时候记得不要加*，不然报错




