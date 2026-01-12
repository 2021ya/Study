import multiprocessing
import os
import time
import random


# 进程类
class Copy(object):
    """通过重写进程类来实现自定义子进程"""
    def __init__(self):
        pass

    @staticmethod  # 进程使用的函数建议使用静态类
    def cv(queue, file_name, copy_dir_pash, paste_dir_pash):
        """复制文件"""
        # time.sleep(random.randint(1, 3))
        data = None
        # 复制文件
        try:
            # print("进程PID:{}|复制文件:\"{}\"".format(os.getpid(), file_name))
            file = open(r"{}/{}".format(copy_dir_pash, file_name), 'rb')
            data = file.read()
            file.close()
        except Exception as e:
            print(e)
        # 粘贴文件
        try:
            file = open(r"{}/{}".format(paste_dir_pash, file_name), 'wb')
            file.write(data)
            file.close()
            # print("进程PID:{}|粘贴文件\"{}\"完成".format(os.getpid(), file_name))
        except Exception as e:
            print(e)
        # 执行完毕将完成文件的名称放入队列记录
        queue.put(file_name)


# 主函数
def main():
    copy_dir = input("Copy Dir Pash:")
    paste_dir = input("Dest Dir Pash:")
    start = time.time()
    # 创建进程池
    pool = multiprocessing.Pool(3)
    # # 创建进程池队列
    pool_queue = multiprocessing.Manager().Queue()
    # 遍历当前目录的所有文件
    all_file = os.listdir(copy_dir)
    # 使用进程池来执行
    for file_name in all_file:
        pool.apply_async(Copy.cv, (pool_queue, file_name, copy_dir, paste_dir))
    # 进度条
    for i in range(len(all_file)):  # 记住，这里range是从0开始
        complete = pool_queue.get()  # 每完成一个得到一个，如果没有完成会阻塞
        print("\r\033[0m操作进度：\033[0m[\033[32m%-{}s\033[0m]【\033[32m%.2f%%\033[0m】".format(len(all_file)) % ("#" * (i+1), ((i+1)/len(all_file))*100), end="")
        r"""
        替换参数：\r是将光标回到开头，实现替换字符
        颜色参数：\033[1;32;47
        """
    print()  # 使进度条单独一行
    # 关闭进程池-如果没有任务了自动关闭
    pool.close()
    # 等待子进程结束并回收
    pool.join()
    end = time.time()
    input("程序运行了:{}s".format(end - start))


# 判断主文件运行
if __name__ == "__main__":
    main()
