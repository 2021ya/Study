import threading


# 定义全局变量
NUMBER = 0


def task1():

    for i in range(0, 10000000):
        global NUMBER
        NUMBER += 1
    print(NUMBER)


def task2():
    for i in range(0, 10000000):
        global NUMBER
        NUMBER += 1
    print(NUMBER)


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start()
t2.start()
"""
得出的值可能并不完整，因为两个线程相互竞争，同时进行加一，数据不确定
"""