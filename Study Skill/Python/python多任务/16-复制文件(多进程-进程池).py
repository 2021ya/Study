import multiprocessing
import os
import time


# 进程类
class Copy(object):
    """通过重写进程类来实现自定义子进程"""
    def __init__(self):
        pass

    @staticmethod  # 进程使用的函数建议使用静态类
    def cv(file_name, copy_dir_pash, paste_dir_pash):
        """复制文件"""
        data = None
        # 复制文件
        try:
            print("进程PID:{}|复制文件:\"{}\"".format(os.getpid(), file_name))
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
            print("进程PID:{}|粘贴文件\"{}\"完成".format(os.getpid(), file_name))
        except Exception as e:
            print(e)


# 主函数
def main():
    copy_dir = input("Copy Dir Pash:")
    paste_dir = input("Dest Dir Pash:")
    start = time.time()
    # 创建进程池
    pool = multiprocessing.Pool(3)
    # # 创建进程池队列
    # pool_queue = multiprocessing.Manager().Queue()
    # 遍历当前目录的所有文件
    all_file = os.listdir(copy_dir)
    # 使用进程池来执行
    for file_name in all_file:
        pool.apply_async(Copy.cv, (file_name, copy_dir, paste_dir))
    # 关闭进程池
    pool.close()
    # 等待子进程结束并回收
    pool.join()
    end = time.time()
    print("程序运行了:{}s".format(end - start))


# 判断主文件运行
if __name__ == "__main__":
    main()
