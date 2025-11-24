class Game(object):

    history = ()  # 类属性

    def __init__(self, name):
        """当前玩家姓名"""
        print("loading...")
        self.name = name

    @classmethod  # 类方法
    def top_score(cls):
        """历史最高成绩"""
        for i in Game.history:
            if Game.history is None:
                return None
            else:
                return max(Game.history)

    @staticmethod  # 类静态属性
    def help():
        return "帮助信息"

    def start(self):
        print("User[%s]Start..." % self.name)


# 主程序
while True:
    print("0)退出\n1)查看帮助信息\n2)查看历史最高分\n3)创建游戏对象，开始游戏")
    user_choose = int(input("please input your choice(1/2/3): "))
    if user_choose == 1:
        game_help = Game.help()
        print(game_help)
    elif user_choose == 2:
        game_history = Game.top_score()
        print(game_history)
    elif user_choose == 3:
        user_name = input("please input your name: ")
        game = Game(user_name)
        print("Add success!")
    elif user_choose == 0:
        break
    else:
        print("input error")










