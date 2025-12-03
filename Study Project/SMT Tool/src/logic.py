import os
import time
import sqlite3


class File(object):
    """文件操作类，包括关于文件操作的所有功能"""

    def __init__(self):

        self.log = Log()
        # 判断程序目录是否存在
        if not os.path.exists(r"./data"):
            try:
                os.makedirs(r"./data")  # 存放程序数据
                os.makedirs(r"./data/databases")  # 存放数据库
                os.makedirs(r"./data/log")  # 存放日志
                self.log.write_log("目录初始化成功...")
            except Exception as e:
                self.log.write_log("初始化失败,请检查文件的读取权限...")
                self.log.write_log("Directory init error:{}".format(e))

    def new_file(self):
        """新建文件与目录"""
        pass


class Time(object):
    """时间操作类，包括所有时间的操作"""

    def __init__(self):
        self.now_time = None

    def time(self):
        tuple_time = time.localtime()  # 不放在初始化中，这样每次调用这个函数都是最新时间
        self.now_time = "%04d-%02d-%02d %02d:%02d:%02d" % (
            tuple_time[0], tuple_time[1], tuple_time[2], tuple_time[3], tuple_time[4], tuple_time[5])
        return self.now_time  # 返回当前日期(精度为秒)

    @staticmethod
    def now_timestamp():
        """返回当前时间戳"""
        return int(time.time())


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
                f.write(log_time.time() + "//" + str(log) + "\n")
                f.close()
        except Exception as e:
            print("Log writing failed:{}".format(e))


class Database(object):

    def __init__(self):
        # 类初始化
        self.log = Log()
        self.time = Time()
        # 数据库初始化
        self.db = sqlite3.connect(r"./data/databases/data.db")  # 连接数据库，若不存在创建数据库
        self.cursor = self.db.cursor()  # 创建数据库游标
        # 如果不存在数据表，就创建，其中包括id(整数类型，自增，主键，唯一)、schedule(文本类型150字符)、time(文本类型)、finish(整数类型,默认值0-未完成)
        sql = "create table if not exists schedule(id integer auto_increment primary key unique not null, schedule text(150), time text(20), timestamp integer, finish integer default 0)"
        try:
            self.cursor.execute(sql)
            print("Database create success")
            self.db.commit()
        except Exception as e:
            print("Database init failed:{}".format(e))
            self.log.write_log("<system>:Database init failed:{}".format(e))
            self.db.rollback()

    def insert_data(self, data):
        sql = "insert into schedule(schedule, time, timestamp, finish) values(?, ?, ?, ?)"
        if not type(data) is list:
            return "The data is a list type"
        try:
            self.cursor.execute(sql, (data, self.time.time(), self.time.now_timestamp(), 0))
            self.db.commit()
            print("Insert data success")
            self.log.write_log("{}:Insert data success".format("<system>"))
            return "Insert data success"
        except Exception as e:
            self.log.write_log("{}:Insert data failed,[{}]".format(self.time.time(), e))
            print("{}:Insert data failed,[{}]".format("<system>", e))
            self.db.rollback()
            return "{}:Insert data failed,[{}]".format("<system>", e)

    def select_data(self, data):
        pass

    def select_recent_12h(self):
        """查询离当前距离12小时的日程"""
        sql = "select schedule from schedule where ? < timestamp < ?"
        try:
            self.cursor.execute(sql, (self.time.now_timestamp()-43200, self.time.now_timestamp()+43200))
            print("{}:Select recent 12h".format(self.time.now_time))
            self.log.write_log("{}:Select recent 12h".format(self.time.now_time))
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print("{}:Select recent 12h failed![{}]".format(self.time.now_time, e))
            self.log.write_log("{}:Select recent 12h failed![{}]".format(self.time.now_time, e))
            return "{}:Select recent 12h failed![{}]".format(self.time.now_time, e)










