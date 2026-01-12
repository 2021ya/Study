import time



def task1():
    while True:
        print("task1")
        yield  # 执行此函数时不会完全执行完毕，而是会停到这一行，并且保存当前状态，直到下一次调用(next())，才会恢复状态，继续执行
        time.sleep(0.1)


def task2():
    while True:
        print("task2")
        yield
        time.sleep(0.1)


def main():
    t1 = task1()  # 这两行需要放到循环外部，否则会重置yield
    t2 = task2()
    while True:
        next(t1)  # 每次调用都会消耗一次yield，主要要在函数中加循环
        next(t2)


if __name__ == '__main__':
    main()

"""
此方法实现的多任务实际上运行速度快看不出来而已
"""
