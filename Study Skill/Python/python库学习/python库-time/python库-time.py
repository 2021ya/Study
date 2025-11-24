# python标准库-处理时间相关的
import time


"""
时间类型
1、时间戳（从1970-1-1-00:00到指定时间或现在，单位为s）
2、结构化时间对象
3、格式化时间字符串
"""

# 时间戳
print("程序运行时时间戳：", time.time())
print("程序运行时一个小时之前的时间戳：", time.time() - 3600)  # 单位为s


# 结构化时间对象
tuple_time = time.localtime()
print("当前时间的结构化时间对象", time.localtime())  # 返回一个tuple（元组）
"""
tm_year=2025-----年
tm_mon=11-----月
tm_mday=15-----日
tm_hour=21-----时
tm_min=17-----分
tm_sec=21-----秒
tm_wday=5-----周(从0开始为周一)
tm_yday=319-----一年的第几天
tm_isdst=0-----夏令时
"""
print("Now time：{}-{:02d}-{:02d}|{:02d}:{:02d}:{:02d}".format(tuple_time[0], tuple_time[1], tuple_time[2], tuple_time[3], tuple_time[4], tuple_time[5]))


# 格式化字符串
print("格式化字符串时间：", time.ctime())  # 直接返回美国地区的日期格式
print("格式时间：", time.strftime("%Y年%m月%d日 %H时%M分%S秒 %A %B 一周的第%w天 本周是一年的第%W周"))  # 可以自己设置格式A、a为星期，B、b为月份


# 等待
print("本程序刚睡了2.5秒", time.sleep(2.5))  # 让你的程序睡几秒


# 计算程序执行的时间
s1 = time.time()
time.sleep(2)
s2 = time.time()
print("程序运行了{:.02f}s".format(s2-s1))


# 时间转换
print("时间戳转为格式化时间", time.localtime(time.time()))
print("格式化时间转为时间戳", time.mktime(time.localtime()))
print("固定时间转格式化字符串", time.strptime("2025-11-15 22:06:00", "%Y-%m-%d %H:%M:%S"))