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
                self.log.write_log("The directory is initialized successfully！")
            except Exception as e:
                self.log = Log()
                self.log.write_log("If initialization fails, check the read permissions of the file...")
                self.log.write_log("Directory init error:{}".format(e))


class Version(object):
    """版本控制"""
    def __init__(self):
        if os.path.exists("./data/version.txt"):  # 判断路径是否存在
            pass
        else:
            with open("./data/version.txt", "a") as f:
                f.write("V1.0.0.0")  # 当前版本
                f.close()
        self.init_version = "V1.0.0.0"

    def read_version(self):
        with open("./data/version.txt", "r") as f:
            version = f.readline()
            if version == self.init_version:
                return version
            else:
                return "Version Error！"


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
    def time_localtime(choose_time):
        """返回指定时间，数字从1开始到6结束"""
        tuple_time = time.localtime()
        if choose_time is None:
            return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        elif choose_time == 1:
            return tuple_time[0]
        elif choose_time == 2:
            return tuple_time[1]
        elif choose_time == 3:
            return tuple_time[2]
        elif choose_time == 4:
            return tuple_time[3]
        elif choose_time == 5:
            return tuple_time[4]
        elif choose_time == 6:
            return tuple_time[5]

    @staticmethod
    def now_timestamp():
        """返回当前时间戳"""
        return int(time.time())

    @staticmethod
    def conversion(c_time, type_str=True):
        """格式化时间转为时间戳"""
        if type_str:
            timestamp = time.mktime(time.strptime(c_time, "%Y-%m-%d %H:%M:%S"))
            return timestamp
        else:
            str_time = time.localtime(c_time)
            return time.strftime("%Y-%m-%d %H:%M:%S", str_time)


class Log(object):
    """日志操作类，包括日志中的所有操作"""

    def __init__(self):
        self.log_time = Time()
        try:
            with open(r"./data/log/log.txt", "a") as f:
                f.close()
        except Exception as e:
            print("Log file creation failed:", e)

    def write_log(self, log):
        """写入日志"""
        try:
            with open(r"./data/log/log.txt", "a") as f:
                f.write(self.log_time.time() + "//" + str(log) + "\n")
                f.close()
        except Exception as e:
            print("Log writing failed:{}".format(e))

    def delete_log_data(self):
        """删除日志数据"""
        try:
            with open(r"./data/log/log.txt", "w") as f:
                f.write(self.log_time.time() + "//" + "Try to delete the log data..." + "\n")
                f.close()
            self.write_log("Delete log successfully!")
            return "Delete log successfully!"
        except Exception as e:
            self.write_log("Delete log error:{}".format(e))
            return "Delete log error![Error:{}]".format(e)


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
            print("Database init failed[Error:{}]--SQL:{}".format(e, sql))
            self.log.write_log("Database init failed[Error:{}]--SQL:{}".format(e, sql))
            self.db.rollback()

    def insert_data(self, schedule, start_time):
        """写入数据库数据"""
        sql = "insert into schedule(schedule, add_time, start_time, finish) values(?, ?, ?, ?)"
        # if not type(data) is list:
        #     return "The data is a list type"
        try:
            self.cursor.execute(sql, (schedule, self.time.now_timestamp(), start_time, 0))
            self.db.commit()
            print("Insert data success!--SQL:{}".format(sql))
            self.log.write_log("Insert data success!--SQL:{}".format(sql))
            return "Insert data success!"
        except Exception as e:
            print("Insert data failed,[Error:{}]--SQL:{}".format(e, sql))
            self.log.write_log("Insert data failed,[Error:{}]--SQL:{}".format(e, sql))
            self.db.rollback()
            return "Insert data failed,[Error:{}]--SQL:{}".format(e, sql)

    def select_schedule(self, start_time=None, end_time=None, all_schedule=False):
        """查询日程,默认查询所有未完成的日程，若输入开始时间和结束时间，那么可以查询指定时间的日程"""
        if all_schedule:  # 查询所有日程
            sql = "select id, schedule, finish, start_time from schedule"
            try:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            except Exception as e:
                print("Select schedule failed,[Error:{}]--SQL:{}".format(e, sql))
                self.log.write_log("Select schedule failed,[Error:{}]--SQL:{}".format(e, sql))
                return "Select schedule failed,[Error:{}]--SQL:{}".format(e, sql)
        elif start_time is None and end_time is None:  # 查询所有时间未完成的日程
            sql = "select id, schedule from schedule where finish = 0"
            try:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            except Exception as e:
                print("Select schedule failed,[Error:{}]--SQL:{}".format(e, sql))
                self.log.write_log("Select schedule failed,[Error:{}]--SQL:{}".format(e, sql))
                return "Select schedule failed,[Error:{}]--SQL:{}".format(e, sql)
        elif start_time is not None and end_time is not None:  # 查询指定时间区间的所有日程
            if start_time < end_time:
                sql = "select id, schedule from schedule where start_time between ? and ?"
                try:
                    self.cursor.execute(sql, (start_time, end_time))
                    print("Select schedule:[{}-{}]--SQL:{}".format(start_time, end_time, sql))
                    self.log.write_log("Select schedule:[{}-{}]--SQL:{}".format(start_time, end_time, sql))
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

    def delete_schedule(self, schedule_id):
        """输入日程id，删除日程"""
        sql = "delete from schedule where id = ?"
        try:
            self.cursor.execute(sql, (schedule_id,))
            self.db.commit()
            print("Delete schedule[id={}] success!--SQL:{}".format(schedule_id, sql))
            self.log.write_log("Delete schedule[id={}] success!--SQL:{}".format(schedule_id, sql))
            return "Delete schedule success!"
        except Exception as e:
            self.db.rollback()
            print("Delete schedule [id={}] failed[Error:{}]--SQL:{}".format(schedule_id, e, sql))
            self.log.write_log("Delete schedule [id={}] failed[Error:{}]--SQL:{}".format(schedule_id, e, sql))
            return "删除日程[id={}]失败！[Error:{}]--SQL:{}".format(schedule_id, e, sql)

    def update_schedule(self, schedule, start_time, schedule_id):
        """更新日程"""
        sql = "update schedule set schedule = ? , start_time = ? where id = ?"
        try:
            self.cursor.execute(sql, (schedule, start_time, schedule_id))
            self.db.commit()
            print("Update schedule [id={}] success!--SQL:{}".format(schedule_id, sql))
            self.log.write_log("Update schedule [id={}] success!--SQL:{}".format(schedule_id, sql))
            return "Update schedule success!"
        except Exception as e:
            self.db.rollback()
            print("Update schedule [id={}] failed,[Error:{}]--SQL:{}".format(schedule_id, e, sql))
            self.log.write_log("Update schedule [id={}] failed,[Error:{}]--SQL:{}".format(schedule_id, e, sql))
            return "Update schedule [id={}] failed,[Error:{}]--SQL:{}".format(schedule_id, e, sql)

    def update_schedule_state(self, var, schedule_id):
        """更新日程状态"""
        sql = "update schedule set finish = ? where id = ?"
        try:
            self.cursor.execute(sql, (var, schedule_id))
            self.db.commit()
            print("Update schedule [id={}] success!--SQL:{}".format(schedule_id, sql))
            self.log.write_log("Update schedule [id={}] success!--SQL:{}".format(schedule_id, sql))
            return "Update schedule success!"
        except Exception as e:
            self.db.rollback()
            print("Update schedule [id={}] failed,[Error:{}]--SQL:{}".format(schedule_id, e, sql))
            self.log.write_log("Update schedule [id={}] failed,[Error:{}]--SQL:{}".format(schedule_id, e, sql))
            return "Update schedule [id={}] failed,[Error:{}]--SQL:{}".format(schedule_id, e, sql)

    def count_finish(self):
        """统计日程完成情况"""
        sql = "select count(*) from schedule where finish = 1"  # 完成
        sql2 = "select count(*) from schedule where finish = 0"  # 未完成
        try:
            self.cursor.execute(sql)
            completed = self.cursor.fetchone()
            self.cursor.execute(sql2)
            not_finished = self.cursor.fetchone()
            # print("Count finish success!--SQL:{}".format(sql))
            # self.log.write_log("Count finish success!--SQL:{}".format(sql2))
            return completed, not_finished
        except Exception as e:
            print("count_finish failed,[Error:{}]--SQL:{}".format(e, sql))
            self.log.write_log("count_finish failed,[Error:{}]--SQL:{}".format(e, sql))
            return "count_finish failed,[Error:{}]--SQL:{}".format(e, sql)

    def delete_data(self):
        """删除所有数据"""
        sql = "delete from schedule"
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("Delete all data successfully!--SQL:{}".format(sql))
            self.log.write_log("Delete all data successfully!!--SQL:{}".format(sql))
            return "Delete all data successfully!"
        except Exception as e:
            self.db.rollback()
            print("Delete all data failed,[Error:{}]--SQL:{}".format(e, sql))
            self.log.write_log("Delete all data failed,[Error:{}]--SQL:{}".format(e, sql))
            return "Delete all data failed,[Error:{}]--SQL:{}".format(e, sql)







