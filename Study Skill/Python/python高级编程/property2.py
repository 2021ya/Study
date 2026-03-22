class Test(object):

    def __init__(self):
        self.a = 1

    def get_value(self):
        return self.a

    def set_value(self, value):
        self.a = value

    def del_value(self):
        del self.a

    VALUE = property(get_value, set_value, del_value, "说明文档")


t = Test()
print(t.VALUE)  # 获取值
t.VALUE = 100  # 修改值
print(t.VALUE)  # 获取值
print(Test.VALUE.__doc__)  # 输出说明文档
del t.VALUE  # 删除属性
