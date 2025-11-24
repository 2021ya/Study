# t010203 = True  # 显得多余了哈哈哈

check_tick = input("您是否有车票(yes/no):")

if check_tick == "yes":
    tick = input("请输入您的车票编号：")
    if tick == "t010203":
        # 布尔类型可以直接用，例如："if t010203:" 可以直接运行下方代码块
        print("Enter")
        capacity = int(input("检测到有充电宝，告知充电宝容量："))  # 如果输入的不是数字直接报错，em目前我无法解决
        if capacity > 20000:
            print("您的充电宝容量为%d" % capacity)
            print("容量过大，请自行处理，禁止进入！")
        elif 0 < capacity < 20000:
            print("您的充电宝容量为%d,处于安全范围" % capacity)
            print("Enter")
        else:
            print("Unknown Error!")
    else:
        print("Error!")
elif check_tick == "no":
    print("请先购买车票...")
else:
    print("Unknown Error!")





















