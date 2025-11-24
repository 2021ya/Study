"""
需求：
士兵拿枪开火，枪发射子弹

"""


class Gun:
    """枪类"""

    def __init__(self, name, count_bullet):
        self.name = name  # 枪支名称
        self.count_bullet = count_bullet  # 子弹容量
        self.free_count_bullet = 0  # 剩余子弹容量
        print("枪支初始化中...")

    def __str__(self):
        return "当前枪支【%s】\n弹夹容量<%d>" % (self.name, self.count_bullet)

    def __del__(self):
        print("枪支【%s】销毁" % self.name)

    def fire(self):
        """开火"""
        if self.free_count_bullet > 0:
            self.free_count_bullet -= 1  # 开火发射一颗子弹
            print("   -------\n"
                  "   |     | \n"
                  "   |-----|\n"
                  "     ||                                                  **        \n"
                  " |------------------=========  -*                      **   **        \n"
                  " |         |                                              **         \n"
                  "|   --------|      \n"
                  "|  |\n"
                  "|  |\n"
                  "|  |     \n")
            print(self.examine())
        else:
            print("bullet:%d/%d" % (self.free_count_bullet, self.count_bullet))  # 无子弹提示

    def replace(self):
        """换弹夹"""
        self.free_count_bullet = self.count_bullet
        return "咔嚓"

    def examine(self):
        """检查子弹"""
        return "bullet:%d/%d" % (self.free_count_bullet, self.count_bullet)


class Soldier:
    """士兵类"""

    def __init__(self, name):
        self.name = name  # 士兵姓名
        self.gun = None  # 新兵无持有枪支
        print("初始化士兵中...")

    def __str__(self):
        return "士兵【%s】\n持有枪支:\n%s" % (self.name, self.gun)

    def __del__(self):
        print("士兵【%s】删除" % self.name)

    def trigger(self):
        print("瞄准...")
        self.gun.fire()  # 调用枪支类中的射击函数


ak47 = Gun("ak47", 40)  # 造枪
human = Soldier("2021")  # 造人。。？

human.gun = ak47  # 给他一把ak47
# print(human)  # 打印士兵信息
# print(ak47)  # 打印枪支信息
# print(human.gun.examine())  # 检查子弹情况
print(human.gun.replace())  # 换弹夹
print(human.gun.examine())  # 检查子弹情况
while True:
    human_choose = input("开火(enter)/退出(0)")
    if human_choose == "0":
        break
    elif human_choose == "":
        human.trigger()
    else:
        print("操作错误")

"""
拓展：
is 与 == 的区别
is判断内存地址是否相等
==只是判断值是否相等
"""