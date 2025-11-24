class Animal:  # -----当前为父类

    def __init__(self):
        self.__name = 'Animal'  # 私有属性
        pass

    def __test(self):  # 私有方法
        print("aaa我是私有方法")

    def test2(self):
        self.__test()  # 父类中的公有方法可以调用父类中的私有方法的，这样就可以从子类访问父类的私有方法了

    def eat(self):
        return "eat"

    def drink(self):
        print("drink..")

    def run(self):
        print('run')

    def sleep(self):
        print('sleep')


class Dog(Animal):  # 在括号中写上父类，可以继承父类的属性----当前为子类

    def __init__(self):
        self.drink()  # 子类可以访问父类公有方法
        pass

    def bark(self):
        print('bark。。。')


class XiaoTianQuan(Dog):  # 父类 -->  子类  -->  子类  --> ...可以一直传递(类名每个单词首字母字母大写)

    def __init__(self):
        pass

    def fly(self):
        print('fly')

    def bark(self):  # 如果父类满足不了子类的需求，可在子类重重新编写
        print("ao wu...")  # 重新编写的代码
        # 调用父类两种方法
        super().bark()  # 使用super().函数可以在需要时调用父类方法
        Dog.bark(self)  # 旧版本中想要调用父类只能用"父类.方法(self)来写",必须写self

        print("!@#$#%^&*(*&^%$#@")  # 其他代码


class Cat:

    def __init__(self):
        pass

    def catch(self):
        print('catch')


xiaohei = Dog()
xiaohei.eat()
xiaohei.drink()
xiaohei.sleep()
xiaohei.run()
xiaohei.bark()

xiaotianquan = XiaoTianQuan()
xiaotianquan.fly()
xiaotianquan.sleep()
xiaotianquan.run()
xiaotianquan.bark()
xiaotianquan.sleep()

# xiaotianquan.catch()  # 显然不能调用猫类函数，只能单继承

# 子类无法访问父类的私有属性与方法,反之，父类不可访问子类私有属性或方法
# xiaohei.__test()
xiaohei.__name()

print(xiaohei._Animal__test())  # 可以强制访问私有方法
print(dir(xiaohei))








