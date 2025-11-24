import pymysql


# 获取连接
db = pymysql.connect(host="localhost", user="root", password="", database="mydome", charset="utf8")

# 创建游标对象
cursor = db.cursor(pymysql.cursors.DictCursor)  # 默认查询是元组，可以修改为字典

# 数据读取
try:  # 为避免错误，通常是尝试执行
    # 执行SQL语句
    sql = "select * from stu limit 50"  # limit控制读取数据的多少
    cursor.execute(sql)  # 查看服务版本

    # 解析数据写法1-单行解析
    # while True:
    #     row = cursor.fetchone()  # 每次读取一行fetchone
    #     if row is None:  # 如果拿不出数据，那么返回的是空
    #         break
    #     print(row)

    # 解析数据写法1-一次性解析完毕
    data = cursor.fetchall()  # fetchall读取全部
    for row in data:  # 单行输出
        print(row)

except Exception as error:
    print("Error:", error)


# 数据写入
try:
    # 写入数据写法1-----注意注意！！！：这种方法直接将一个SQL语句写出来，会有被入侵的风险，例如加注释之类的
    # data2 = ("2024", 21, "w", "python04")
    # sql2 = "insert into stu(name, age, sex, classid) value('%s', '%s', '%s', '%s')" % (data2[0], data2[1], data2[2], data2[3])  # 可用变量接收;%s站位，数据从data2中取
    # return_i = cursor.execute(sql2)  # 每次执行SQL语句都会返回影响数据数
    # db.commit()  # 事务提交-----执行SQL语句只是在内存操作，用commit()函数可以保存操作
    # print("影响数据数：", return_i)

    # 写入数据写法2-----防SQL注入写法，SQL语句与数据分离,这样，即使用户输入了恶意的字符串，数据库也会将其视为参数值，而不会作为SQL代码执行。
    data2 = ("2024", 21, "w", "python04")
    sql2 = "insert into stu(name, age, sex, classid) value(%s, %s, %s, %s)"   # 只写4个占位符
    cursor.execute(sql2, data2)  # 执行SQL语句,然后从data2里面取4个数据
    db.commit()  # 事务提交
    print("影响数据数：", cursor.rowcount)  # 使用cursor.rowcount可以打印影响行数

except Exception as error:
    db.rollback()  # 事务回滚-----用于报错之后撤回操作，使用rollback()函数
    print("Error:", error)


# 数据修改
try:
    # 修改数据写法-----防SQL注入写法，SQL语句与数据分离
    data2 = ("2025", 22, "m", "python01", 11)
    sql2 = "update stu set name = %s, age = %s, sex = %s, classid = %s where id = %s"   # 4个占位符
    cursor.execute(sql2, data2)  # 执行SQL语句,然后从data2里面取4个数据
    db.commit()  # 事务提交
    print("影响数据数：", cursor.rowcount)  # 使用cursor.rowcount可以打印影响行数

except Exception as error:
    db.rollback()  # 事务回滚-----用于报错之后撤回操作，使用rollback()函数
    print("Error:", error)


# 数据删除
try:
    # 修改数据写法-----防SQL注入写法，SQL语句与数据分离
    data2 = 13
    sql2 = "delete from stu where id = %s"   # 4个占位符
    cursor.execute(sql2, data2)  # 执行SQL语句,然后从data2里面取1个数据
    db.commit()  # 事务提交
    print("影响数据数：", cursor.rowcount)  # 使用cursor.rowcount可以打印影响行数

except Exception as error:
    db.rollback()  # 事务回滚-----用于报错之后撤回操作，使用rollback()函数
    print("Error:", error)

# 关闭数据库
db.close()
