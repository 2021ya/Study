import pymysql


db = pymysql.connect(host="localhost", user="root", password="", database="test", charset="utf8")
cursor = db.cursor(pymysql.cursors.DictCursor)


username = input("n:")
password = input("p:")


try:
    sql = "select password from sql_test where name = \"{}\"".format(username)
    # 危险注入:select password from sql_test where name = "name" or 1 = 1 -- "
    # 直接执行SQL语句，两个--直接将后面的引号注释了，所以形成了入侵
    cursor.execute(sql)
    print(sql)
    print(cursor.fetchall())

except Exception as e:
    print(e)
