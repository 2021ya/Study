class Cat:  # 用class来定义一个类，后面不需要括号，然后类的命名规则是大驼峰命名法（每个单词的首字母大写且不用下划线隔开）
    """这是一个猫类"""

    def eat(self):  # 这个就是类里面的方法,self的用法是哪一个对象调用，这个self就是哪一个对象的引用（内存地址）（大白话：谁用写谁名，这个self就是谁）
        """方法1：吃"""
        print("%s Eat..." % self.name)  # 哪一个对象调用，这个self就是哪一个对象，点后面是那个对象的方法/属性，用self.来调用这个对象的其他方法和属性

    def drink(self):
        """方法2：喝"""
        print("Drink...")


Tom = Cat()  # 这个就是创建对象，这个类可以创建多个对象，而Tom就是一个对象。通过类来创建对象，这个对象的所有属性、方法都是一样的

# 如果想要在类的外部来给对象增加属性，那么需要用到赋值语句，但这种方法并不推荐使用（要添加属性的对象.需要添加的属性名 = ""）
Tom.name = "Tom"  # 这种方法只适合临时添加属性，不建议使用
print(Tom.name)

Tom.eat()
Tom.drink()
print(Tom)  # 输出Tom的信息

"""
<__main__.Cat object at 0x0000020523A282C0>
后面那串是一个16进制的数字----引用（内存地址）

##拓展
%d-----输出的是整数类型的10进制数
%x-----输出的是16进制的数
"""

lazy_cat = Cat()

# 如果想要在类的外部来给对象增加属性，那么需要用到赋值语句，但这种方法并不推荐使用（要添加属性的对象.需要添加的属性名 = ""）
lazy_cat.name = "LazyCat"
print(lazy_cat.name)

lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)


print(id(Tom))
print(id(lazy_cat))
print("引用（内存地址）不同，证明两只猫不是同一个")


lazy_cat2 = lazy_cat  # 这时，两只猫就一样了
print(lazy_cat2)
print(id(lazy_cat2))
















"""
面向对象的编程，我的理解是定义了一个大的某个东西，比如说人，定义了一个人，然后这个人会干什么这就是这个人的方法，这个人是什么样子的，这个叫属性
"""
