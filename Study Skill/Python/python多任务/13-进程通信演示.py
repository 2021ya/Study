import time
import multiprocessing


def task1(queue):
    # 放数据
    for i in ["a", "b", "c"]:
        queue.put(i)
        time.sleep(0.5)


def task2(queue):
    # 取数据
    while True:
        time.sleep(0.5)  # 不确定哪个进程先执行，先等待0.5s
        if not queue.empty():  # 如果不为空
            print(queue.get())
        else:  # 数据空了就退出循环
            break


if __name__ == '__main__':
    # 创建队列
    q = multiprocessing.Queue()
    # 创建进程
    p = multiprocessing.Process(target=task1, args=(q, ))
    p2 = multiprocessing.Process(target=task2, args=(q, ))
    # 启动进程
    p.start()
    p2.start()

