class Person:

    def __init__(self, new_name, new_weight):
        print("初始化中。。。")
        self.name = new_name
        self.weight = new_weight

    def __del__(self):
        print("%s被删除了。。。" % self.name)

    def __str__(self):
        return "my name is %s, my weight is %.2f" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5  # 对象自身的体重减少
        print("%s has finished running." % self.name)

    def eat(self):
        self.weight += 1  # 对象自身的体重增加
        print("%s has finished eating food." % self.name)


new_name = input("Please input your name:")
new_weight = int(input("Please input your weight:"))

new_name1 = Person(new_name, new_weight)  # 创建一个对象
print(new_name1)

user_choose = input("Please enter choose(eat or run):")

if user_choose == "eat":
    new_name1.eat()
    print(new_name1)
elif user_choose == "run":
    new_name1.run()
    print(new_name1)
else:
    print("Please choose eat or run")


new_name2 = input("Please input your name:")
new_weight2 = int(input("Please input your weight:"))

new_name2 = Person(new_name2, new_weight2)

user_choose2 = input("Please enter choose(eat or run):")

if user_choose2 == "eat":
    new_name2.eat()
    print(new_name2)
elif user_choose2 == "run":
    new_name2.run()
    print(new_name2)
else:
    print("Please choose eat or run")


print(new_name1)
print(new_name2)





