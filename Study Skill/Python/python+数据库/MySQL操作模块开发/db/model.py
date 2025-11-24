import pymysql
from MySQL操作模块开发 import config


class Model(object):
    """单表查询类"""

    def __init__(self, table, config_=config):
        """构造方法，连接数据库，初始化"""
        try:  # 防止连接失败
            self.table_name = table
            self.link = pymysql.connect(host=config_.HOST, user=config_.USER, password=config_.PASSWORD, database=config_.DATABASE, charset=config_.CHARSET, port=config_.PORT)
            self.cursor = self.link.cursor(pymysql.cursors.DictCursor)
            self.pk = "id"  # 主键，默认id
            self.fields = []  # 字段名称
            self.__loading_fields()  # 加载字段
            print("数据库【{}】登录成功".format(self.table_name))
        except Exception as error:
            print("数据库【{}】连接失败:".format(self.table_name), error)

    def __loading_fields(self):
        """内部加载字段信息，不可外部调用"""
        # 执行SQL语句，列出字段
        sql = "show columns from %s" % self.table_name
        self.cursor.execute(sql)
        # 读取所有返回记录到data中
        data = self.cursor.fetchall()
        # 遍历data
        for i in data:
            # 取出每个字段的名称，并写入到字段名称列表中
            self.fields.append(i["Field"])
            # 判断主键，并记录到主键信息
            if i["Key"] == "PRI":
                self.pk = i["Field"]

    def add(self, data={}):
        """传入字典写入数据"""
        try:
            keys = []  # 存储字典的key-----字段
            values = []  # 存储字典的value-----数据
            for k, v in data.items():  # 遍历字典，将字典的key和value全部一次取出（使用.items()函数）
                if k not in self.fields:  # 若字段名不在数据库字段名称，那么就会直接返回-----非法判断
                    return "字段非法！"
                keys.append(k)
                values.append(v)
            sql = "insert into %s(%s) value(%s)" % (self.table_name, ",".join(keys), ",".join(["%s"] * len(values)))  # 拼装字符串，自动遍历列表中的每个数据，然后拼接到逗号后面;有几个数据，转换为几个百分号
            self.cursor.execute(sql, tuple(values))  # 这个代码是将SQL语句中的%s用后面的tuple(values)绑定参数了(转义，直接将%s转为值，而不是代码)，并且一一对应
            self.link.commit()
            return "数据添加成功,数据id【{}】".format(self.cursor.lastrowid)  # 返回影响的数据id(只适用于insert)
        except Exception as error:
            self.link.rollback()
            return "数据添加失败:{}".format(error)

    def update(self, field, new_data, pri_key):
        """传入字典更改数据"""
        try:
            if field not in self.fields:
                return "字段非法！"
            sql = "update %s set %s = %s where %s = %s" % (self.table_name, field, "%s", self.pk, pri_key)
            print(sql)
            self.cursor.execute(sql, new_data)
            self.link.commit()
            return "数据修改成功,数据影响数【{}】".format(self.cursor.rowcount)
        except Exception as error:
            self.link.rollback()
            return "数据修改失败:{}".format(error)

    def find(self, data_id):
        """获取指定id号数据"""
        try:
            sql = "select * from %s where %s = '%s'" % (self.table_name, self.pk, data_id)
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except Exception as error:
            print("查询单条数据错误:", error)

    def delete(self, data_id):
        """删除指定id号数据"""
        try:
            sql = "delete from %s where %s = '%s'" % (self.table_name, self.pk, data_id)
            self.cursor.execute(sql)
            self.link.commit()  # 事务提交
            effected = self.cursor.rowcount
            return "删除成功, 影响行数:%s" % effected
        except Exception as error:
            self.link.rollback()  # 事务回滚
            print("删除单条数据错误:", error)

    def findall(self):
        """获取所有数据"""
        try:
            sql = "select * from %s" % self.table_name
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as error:
            print("查询所有错误:", error)

    def __del__(self):
        """构析方法"""
        if self.link is not None:  # 程序结束时，数据库没有关闭就关闭数据库
            self.link.close()

    def select(self, where=None, order=None, limit=None):  # order分页， limit限制行数,desc为order的参数，为降序，默认升序
        """查询，需要输入条件"""
        try:
            sql = "select * from %s" % self.table_name
            # 条件判断部分有SQL注入风险-----警告
            if isinstance(where, list) and len(where) > 0:  # isinstance(表，列表),判断where是否为列表
                sql += " where " + " and ".join(where)  # .join函数只有在两个及以上时才会插入拼接
            if order is not None:
                sql += " order by %s"
            if limit is not None:
                sql += " limit %s"
                print(sql)
            self.cursor.execute(sql, (order, limit))
            return self.cursor.fetchall()
        except Exception as error:
            return "查询错误:{}".format(error)

























