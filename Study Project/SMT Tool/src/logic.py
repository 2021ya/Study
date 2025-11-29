import os
import time


class File(object):
    """文件操作类，包括关于文件操作的所有功能"""
    def __init__(self):

        # 判断程序目录是否存在
        if not os.path.exists(r"./data"):
            try:
                os.makedirs(r"./data")  # 存放程序数据
                os.makedirs(r"./data/databases")  # 存放数据库
                os.makedirs(r"./data/log")  # 存放日志
                print("目录初始化成功...")
            except Exception as e:
                print("初始化失败,请检查文件的读取权限..." + "\n"
                      "error:", e)

    def new_file(self):
        """新建文件与目录"""
        pass


class Time(object):
    """时间操作类，包括所有时间的操作"""
    def __init__(self):
        self.now_time = None

    def time(self):
        tuple_time = time.localtime()  # 不放在初始化中，这样每次调用这个函数都是最新时间
        self.now_time = "%04d-%02d-%02d %02d:%02d:%02d" % (tuple_time[0], tuple_time[1], tuple_time[2], tuple_time[3], tuple_time[4], tuple_time[5])
        return self.now_time  # 返回当前日期(精度为秒)

    def update_time(self):
        pass


class Log(object):
    """日志操作类，包括日志中的所有操作"""
    def __init__(self):
        try:
            with open(r"./data/log/log.txt", "a") as f:
                f.close()
        except Exception as e:
            print("Log file creation failed:", e)

    @staticmethod
    def write_log(log):
        """写入日志"""
        log_time = Time()
        try:
            with open(r"./data/log/log.txt", "a") as f:
                f.write(log_time.time() + " ===> " + str(log) + "\n")
                f.close()
        except Exception as e:
            print("Log writing failed:", e)













