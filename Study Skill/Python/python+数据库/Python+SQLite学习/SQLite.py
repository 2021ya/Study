"""
SQLite与MySQL语法区别(相差不大)

-占位符-
    MySQL:"%s"
    SQLite:"?"

-数字自增-
    MySQL:AUTO_INCREMENT
    SQLite:AUTOINCREMENT-----哎？我写的时候这个是错的，可能更新了，用auto_increment正常

-数据类型-
    MySQL:VARCHAR(), INT
    SQLite:TEXT, INTEGER

-日期存储-
    MySQL:DATATIME
    SQLite:TEXT

-获取当前时间-
    MySQL:now()
    SQLite:datatime("now")

----其他的差不多

"""


# 导入sqlite包（python内置，不需要额外安装）
import time
import sqlite3


db = sqlite3.connect(r"./test.db")  # 连接数据库，若没有数据库就创建
cursor = db.cursor()  # 创建游标对象

# 若表格不存在，创建表格-----注意，只有integer类型才能自增id
sql_new = "create table if not exists test(id integer auto_increment primary key unique, name text(7) not null , age tinyint, time text)"  # sqlite必须每个字段指定数据类型

try:
    cursor.execute(sql_new)
    db.commit()
    print("new ok")
except Exception as e:
    db.rollback()
    print("new_error:", e)

# 插入数据
sql_insert = "insert into test(id, name, age, time) values(?, ?, ?, ?)"

try:
    with db:  # 使用with可以实现自动提交数据
        time = time.localtime()
        cursor.execute(sql_insert, (4, "2024", 20, str(time)))  # time.localtime获取日期和时间,返回的是元组
        print("insert ok")
except Exception as e:
    db.rollback()
    print("insert_error:", e)

# 查询数据
sql_select = "select * from test"

try:
    with db:  # 使用with可以实现自动提交数据
        cursor.execute(sql_select)
        rows = cursor.fetchall()
        i = 1
        for row in rows:
            i += 1
            print("data{}:".format(i), row)
        print("select ok")
except Exception as e:
    db.rollback()
    print("select_error:", e)


# 删除数据
sql_delete = "delete from test where name = '2022'"

try:
    with db:  # 使用with可以实现自动提交数据
        cursor.execute(sql_delete)
        rows = cursor.fetchall()
        print(sql_delete)
        print("delete ok")
except Exception as e:
    db.rollback()
    print("delete error:", e)


# 修改数据
sql_update = "update test set age = 99 where name = '2021'"

try:
    with db:  # 使用with可以实现自动提交数据
        cursor.execute(sql_update)
        rows = cursor.fetchall()
        print(sql_update)
        print("update ok")
except Exception as e:
    db.rollback()
    print("update error:", e)

cursor.close()  # 关闭数据库
