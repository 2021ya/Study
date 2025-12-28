import multiprocessing
import os
import time


# 定义读函数
def read(queue):
    while True:
        if not queue.empty():
            print("获取读进程PID:{}, 父进程PID:{}, 读取数据：{}".format(os.getpid(), os.getppid(), queue.get()))
        else:
            time.sleep(60)
            break


# 定义写函数
def writ(queue):
    for i in "abcdefg":
        print("获取写进程PID:{}, 父进程PID:{},放入数据：{}".format(os.getpid(), os.getppid(), i))
        queue.put(i)
    time.sleep(60)


# 定义主函数
def main():
    # 创建进程池
    pool = multiprocessing.Pool(5)
    # 创建进程池中的通信队列
    pool_queue = multiprocessing.Manager().Queue()
    """
    注意：进程池之间的通信不可直接使用multiprocessing.Queue()来创建队列，这个队列只适用于手动创建进程的通信，如果进程池直接的进程通信
        必须使用multiprocessing.Manager().Queue()
    """
    # 使用多进程执行函数
    pool.apply_async(writ, (pool_queue,))
    # 等待写入完成
    time.sleep(1)
    # 读
    pool.apply_async(read, (pool_queue, ))  # 将队列传入进程池
    # 关闭进程池
    pool.close()
    # 主进程等待子进程关闭
    pool.join()


# 判断是否主文件运行
if __name__ == '__main__':
    main()

