import multiprocessing
import time


# 创建一个进程执行的函数
def process():
    while True:
        print("我是子进程")
        time.sleep(1)


if __name__ == '__main__':
    """
    注意：创建进程原理是操作系统重新实例化了一个python解释器来执行指定函数，在这个过程中会重新导出此脚本文件，那么就会执行一遍此
        脚本文件,如果此时不将创建进程的代码用if __name__这个代码保护起来，那么就会无限创建进程，会导致报错
    """
    # 实例化进程对象
    process1 = multiprocessing.Process(target=process, args=(args, xxx), kwargs={"name": "aaa", "age": 23})  # 传参同理
    # 创建进程
    process1.start()
    # 主进程继续执行
    while True:
        print("我是主进程")
        time.sleep(1)
