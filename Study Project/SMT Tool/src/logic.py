import os
import time
import sqlite3


class File(object):
    """文件操作类，包括关于文件操作的所有功能"""

    def __init__(self):

        # 判断程序目录是否存在
        if not os.path.exists(r"./data"):
            try:
                os.makedirs(r"./data")  # 存放程序数据
                os.makedirs(r"./data/databases")  # 存放数据库
                os.makedirs(r"./data/log")  # 存放日志
                self.log = Log()
                self.log.write_log("目录初始化成功...")
            except Exception as e:
                self.log = Log()
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

    @staticmethod
    def conversion(str_time):
        """格式化时间转为字符串"""
        timestamp = time.mktime(time.strptime(str_time, "%Y-%m-%d %H:%M:%S"))
        return timestamp


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
        sql = "create table if not exists schedule(id INTEGER PRIMARY KEY AUTOINCREMENT, schedule text(150), add_time integer, start_time integer, finish integer default 0)"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("Database init failed[Error:{}]--run_sql:{}".format(e, sql))
            self.log.write_log("Database init failed[Error:{}]--run_sql:{}".format(e, sql))
            self.db.rollback()

    def insert_data(self, data, start_time):
        """写入数据库数据"""
        sql = "insert into schedule(schedule, add_time, start_time, finish) values(?, ?, ?, ?)"
        # if not type(data) is list:
        #     return "The data is a list type"
        try:
            self.cursor.execute(sql, (data, self.time.now_timestamp(), start_time, 0))
            self.db.commit()
            print("Insert data success!--run_sql:{}".format(sql))
            self.log.write_log("Insert data success!--run_sql:{}".format(sql))
            return "Insert data success!"
        except Exception as e:
            print("Insert data failed,[Error:{}]--run_sql:{}".format(e, sql))
            self.log.write_log("Insert data failed,[Error:{}]--run_sql:{}".format(e, sql))
            self.db.rollback()
            return "Insert data failed,[Error:{}]--run_sql:{}".format(e, sql)

    def select_data(self, data):
        pass

    def select_schedule(self, start_time=None, end_time=None):
        """查询日程,默认查询所有日程，若输入开始时间和结束时间，那么可以查询指定时间的日程"""
        if start_time is None and end_time is None:  # 查询所有时间
            sql = "select schedule from schedule"
            try:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            except Exception as e:
                print("Select schedule failed,[Error:{}]--run_sql:{}".format(e, sql))
                self.log.write_log("Select schedule failed,[Error:{}]--run_sql:{}".format(e, sql))
                return "Select schedule failed,[Error:{}]--run_sql:{}".format(e, sql)
        elif start_time is not None and end_time is not None:  # 查询指定时间区间的日程
            if start_time < end_time:
                sql = "select schedule from schedule where start_time between ? and ?"
                try:
                    self.cursor.execute(sql, (start_time, end_time))
                    print("Select schedule:[{}-{}]--run_sql:{}".format(start_time, end_time, sql))
                    self.log.write_log("Select schedule:[{}-{}]--run_sql:{}".format(start_time, end_time, sql))
                    rows = self.cursor.fetchall()
                    return rows
                except Exception as e:
                    print("Select schedule [{}-{}] failed![Error:{}]".format(start_time, end_time, e))
                    self.log.write_log("Select schedule [{}-{}] failed![Error:{}]".format(start_time, end_time, e))
                    return "Select schedule [{}-{}] failed![Error:{}]".format(start_time, end_time, e)
            elif start_time > end_time:  # 开始时间大于结束时间检查
                print("[Error:{} > {}]".format(start_time, end_time))
                self.log.write_log("[Error:{} > {}]".format(start_time, end_time))
                return "[Error:{} > {}]".format(start_time, end_time)










