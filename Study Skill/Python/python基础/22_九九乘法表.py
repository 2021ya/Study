line = 1  # 循环次数,也是行数判断，循环9次，也就是9行


while line <= 9:  # 控制行数为9行
    number1 = 1  # 数字二初始值为1，然后依次相加
    number2 = line  # 每个式子的第二个数和行数相等
    while number1 <= line:  # 每行的公式和行数相等，当此循环等于行数时跳出循环，相当于这个循环是生成每行的式子
        number = number1 * number2  # 运算两两相乘的数
        """
        print("%s * %s =" % (number1, number2), end="")  # 打印两两相乘的数
        print("%2d" % number, end="")  # 设置结果字符长度默认为2个字符
        print("   ", end="")  # 每个式子空开两个空格
        """
        print("%d * %d = %2d" % (number1, number2, number), end="    ")  # 优化，整合上方三行代码
        number1 += 1  # 每行第一个式子生成完毕之后，第一个数字加一，第二个数字还是和行数相等
    line += 1  # 当前行打印完成行数+1
    print("")  # 之后继续下一行






















