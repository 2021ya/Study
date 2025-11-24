class Tool(object):

    class_count = 0  # 记录有多少对象调用了这个类----利用赋值语句来设置类属性

    @staticmethod  # 定义类的静态方法，上方写“@staticmethod”---------不需要访问实例方法和属性，也不需要方法类方法与属性的时候定义类静态方法
    def test():
        print("我是静态方法。。。")

    @classmethod  # 定义类方法，上面需要写@classmethod-------只需要访问类属性的时候定义类方法
    def print_class_count(cls):  # 里面写cls，和self的效果雷同，self是函数，cls是类，这个cls可以换成其他的，但是不建议换
        print(cls.class_count)

    def __init__(self, name):
        self.name = name  # 每个工具自己的名字
        print(self.name)
        Tool.class_count += 1  # 调用一次（或者创建一次对象）自动执行初始化，自动加1-----"类名.类属性方法"来访问类属性
    # 既要方法类属性，也要访问实例属性，应该定义实例方法


tool1 = Tool("斧头")
tool2 = Tool("菜刀")

print(tool1, tool2)
print(Tool.class_count)

# 通过对象来查找对象所处类的属性-----为什么要这么做？哈哈哈
# python在查找的时候，先查找对象所处函数体内部是否有，否的话，去类属性里面找
print("tool count:%d" % tool1.class_count)
# 如果使用赋值语句，那么它会在对象自己内部函数中查找，如果没有查到，会创建，而不是继续查找
tool1.class_count = 99
print(tool1.class_count)

Tool.test()  # 访问静态方法














