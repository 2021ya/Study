class Woman:

    def __init__(self, name):
        self.name = name
        self.__age = 18  # 属性前面加上两个下换线，外部就访问不了这个属性了，这个叫私有属性（原理是对名称做了处理，改为了"_类名__私有属性"）

    def str(self):
        return "%s 的年龄是%s" % (self.name, self.__age)  # 对象内部使用，外部访问不到


xiaofang = Woman("芳龄")
print(xiaofang)
print(xiaofang.str())  # 调用内部函数，用内部函数来访问
# print(xiaofang.__age)
# xiaofang.__age  方法也同理
print(xiaofang._Woman__age)  # 强制访问私有属性用"_类名__私有属性"来访问，不推荐使用,私有方法同理
print(id(Woman))
