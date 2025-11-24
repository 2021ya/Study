class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        return "普通狗"


class ShenQuan(Dog):

    def game(self):
        return "神犬"


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):

        print("%s在和%s玩" % (self.name, dog.game()))  # 这步中，只是让狗对象调用的game函数，而不关心是什么狗，让它们各自访问自己中的game函数

        # 调用狗玩耍的函数
        print(dog.game())  # 多态：让不同的子类调用相同的方法产生不同的结果


xiaoming = Person("xiaoming")
wang_cai = Dog("wang cai")
shen_quan = ShenQuan("shen quan")

# 只需要传入狗就可，其中的狗会自己调用自己内部的函数
xiaoming.game_with_dog(wang_cai)
# wang cai 调用了自己的game函数

xiaoming.game_with_dog(shen_quan)
# shen quan调用了自己的game函数

















