class Parent(object):

    def __init__(self, name, age, height, *args, **kwargs):
        print("parent init ...")
        print("name : ", name)
        print("age : ", age)
        print("height : ", height)


class Child(Parent):

    def __init__(self, name, age, height, *args, **kwargs):
        print("Child init ...")  # 虽然这里不需要参数，但还是要接受全部参数传给父类
        super().__init__(name, age, height, *args, **kwargs)  # 初始化父类方法


class Child2(Parent):

    def __init__(self, name, age, height, *args, **kwargs):
        print("Child2 init ...")
        super().__init__(name, age, height, *args, **kwargs)


class Child3(Child, Child2):

    def __init__(self, name, age, height, *args, **kwargs):
        print("Child3 init ...")
        super().__init__(name, age, height, *args, **kwargs)


print(Child3.__mro__)
"""
.__mro__是一个算法
    因为在多继承中，容易多次初始化最终的父类方法，而.__mro__方法可以解决这个问题
    它会输出一个元组，获取当前类的名称，然后如果当前类中调用了super方法来初始化它的父类方法
    那么super它会输出一个元组,其中获取所有的父类方法，然后按照特定的顺序来执行
    
    执行逻辑：
        获取当前类，然后在元组中找到当前类，执行当前类的下一个类的初始化方法
        
    注意：
        因为多继承中，需要兼顾各个类需要的参数，为避免报错，所以需要使用*args和**kwargs(不定长参数)来全部接受参数, 多考虑各个类的配合
"""

test = Child3("2021", 20, 181)


























