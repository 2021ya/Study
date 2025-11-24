def sum_number(num1, num2):  # 定义两个参数
    """两数求和"""
    sum_of_numbers = num1 + num2
    print("The sum of numbers is", sum_of_numbers)


num_1 = int(input("num_1:"))
num_2 = int(input("num2_:"))
sum_number(num_1, num_2)  # 传入两个参数，然后函数内部计算（定义几个参数就需要传入几个参数）


def sum_of_free():
    """实现自由定义数求和"""
    user_frequency = int(input("请输入你所求和的个数："))

    function_frequency = 1  # 函数循环次数,初始值为1，第一次循环就是1，而不是0
    number_sum = 0

    while function_frequency <= user_frequency:

        number = int(input("Enter %d number: " % function_frequency))
        number_sum += number  # 循环一次加用户输入的数一次
        function_frequency += 1  # 每次循环，循环次数加一，直至等于用户所输入的数
    # print("number_sum:%d" % number_sum)  # 这个只是打印了结果但是函数外部不知道结果
    return number_sum  # 用return来 返回结果，使得外部可以接受结果,return后续代码不会执行！


result = sum_of_free()  # 调用函数
print("number_sum:", result)


