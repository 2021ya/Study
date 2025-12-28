import os
import time
import multiprocessing


def task(num):
    time.sleep(0.5)
    print("进程pid:{}".format(os.getpid()), "打印数值：", num)


if __name__ == '__main__':

    # 创建进程池
    pool = multiprocessing.Pool(3)  # 创建进程池，最多三个进程

    for i in range(10):  # 创建多个任务=10
        # 向进程池添加任务
        pool.apply_async(task, args=(i,))

    # 关闭空闲进程
    pool.close()  # 结束线程池-----此处必须手动结束

    # 等待子进程全部结束后再继续执行
    pool.join()  # 清理资源，等待调用者结束，如果用作线程，那么会等待线程结束才会继续运行，但是一旦运行了此行代码，那么资源就会被清理，就不可再进行启动线程了

