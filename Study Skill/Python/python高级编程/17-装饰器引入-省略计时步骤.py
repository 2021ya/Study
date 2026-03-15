import time


def calculate(num):
    result = 0
    for i in range(1, num+1):
        result += i ** 3  # 两个星号是立方运算
    return result


start_time = time.time()
print(calculate(100000))
print(time.time() - start_time)
