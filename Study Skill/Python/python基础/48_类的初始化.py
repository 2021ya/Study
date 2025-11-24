class Cat:

    def __init__(self, name):  # 初始化固定用__init__，这个函数在创建对象的时候会自动执行，使用类来创建对象的时候python会自动执行以下操作1、为对象分配内存空间2、初始化
        print("初始化中。。。")
        # self.name = "Tom"  # -----自动执行，创建对象的时候，每个对象都会有这个属性
        self.name = name  # 创建属性，不希望写死代码，那么就写入形参

    def __del__(self):  # 销毁这个对象之前需要做的事情，同样是自动执行，但这个函数是销毁之前自动执行，执行完毕销毁
        print("%s 销毁中。。。" % self.name)

    def __str__(self):  # 正常情况下，打印一个对象的时候会输出由哪一个类创造的对象和内存地址，但是__str__函数可以自定义输出信息
        return "我是%s的自定义信息" % self.name


# Tom = Cat()  # -----创建对象，并没有执行函数__init__方法，但python自动执行了
"""
run:
初始化。。。
"""

Tom = Cat("Tom")  # 传入一个name，那么这个猫的名字就是这个name了
print(Tom.name)

Lazy_Cat = Cat("Big lazy cat")
print(Lazy_Cat.name)

del Lazy_Cat  # 删除Lazy_Cat这个对象，但删除之前会自动执行类中的del函数，然后才是删除
print("-" * 50)

print(Tom)
















