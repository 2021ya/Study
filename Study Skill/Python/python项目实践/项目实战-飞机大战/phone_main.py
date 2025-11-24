# 主程序文件
import pygame
import plane_sprites


# 主游戏类-----用于启动游戏的时候创建一个游戏
class GameStart(object):

    def __init__(self):
        """初始化"""
        pygame.init()  # 模块初始化
        pygame.mixer.init()  # 混音器初始化
        pygame.mixer.music.load(r".\sound\game_music.ogg")  # 加载背景音乐
        pygame.mixer.music.set_volume(0.5)  # 设置音量
        pygame.mixer.music.play(loops=-1)  # -1为循环播放，0为只播放一次，其他正整数为播放次数
        self.log = plane_sprites.Log()
        self.log.write_log("Game Init...")
        print("Game Init...")
        self.screen = pygame.display.set_mode(plane_sprites.SCREEN_RECT)  # 创建屏幕,数字尽量不要写死，不然更改需求的时候很麻烦，要定义常量（所有字母全部大写，连接用下划线）
        self.clock = pygame.time.Clock()  # 创建游戏时钟
        self.__create_sprites()  # 调用私有方法来创建精灵
        pygame.time.set_timer(plane_sprites.CREATE_ENEMY_EVENT, 700)  # 调用精灵模块中的事件常量来设置多久执行一次这个事件，第一个为事件，第二个为时间（毫秒）
        pygame.time.set_timer(plane_sprites.FIRE_BUTTON_EVENT, 250)  # 调用精灵模块中的事件常量来设置多久执行一次这个事件，第一个为事件，第二个为时间（毫秒）
        # 分数读取
        self.num = plane_sprites.kill_enemy
        # 游戏进程检测
        self.i = 1  # 首页，0为开始， 1为等待用户选择
        # 逃脱数图片加载
        self.enemy_successfully_num_0 = pygame.image.load(r"images\enemy_successfully_num_0.png")
        self.enemy_successfully_num_1 = pygame.image.load(r"images\enemy_successfully_num_1.png")
        self.enemy_successfully_num_2 = pygame.image.load(r"images\enemy_successfully_num_2.png")
        self.enemy_successfully_num_3 = pygame.image.load(r"images\enemy_successfully_num_3.png")
        self.enemy_successfully_num_x = pygame.image.load(r"images\enemy_successfully_num_X.png")

    def __create_sprites(self):
        """创建精灵"""
        background1 = plane_sprites.Background(is_alt=False)  # 调用精灵文件中背景类创建一个背景精灵1
        background2 = plane_sprites.Background(is_alt=True)  # 调用精灵文件中背景类创建一个背景精灵2
        self.back_group = pygame.sprite.Group(background1, background2)  # 创建一个精灵组，内含背景精灵
        self.enemy_group = pygame.sprite.Group()  # 创建敌机空精灵组
        self.hero = plane_sprites.Hero()  # 创建角色-----定义为属性，方便后续碰撞检测与操控
        self.hero_group = pygame.sprite.Group(self.hero)  # 创建角色精灵组

    def __event_handler(self):
        """事件处理"""
        # 事件监听
        for event in pygame.event.get():  # 遍历事件列表，寻找是否有以下情况
            # 三种情况同时判断
            if event.type == pygame.QUIT:  # 右上角X-----退出事件
                self.log.write_log("(状态:游戏进行中时)触发事件：<<<右上角关闭事件(X)>>>")
                print("(状态：游戏进行中时)触发事件：<<<右上角关闭事件(X)>>>")
                self.__game_over()
            if event.type == plane_sprites.CREATE_ENEMY_EVENT:  # 检测敌机出现事件
                enemy = plane_sprites.Enemy(r".\images\enemy1.png")
                self.enemy_group.add(enemy)  # 将敌机精灵添加到敌机精灵组中
                self.log.write_log("敌机出现...")  # 写入日志
                print("敌机出现...")
            if event.type == plane_sprites.FIRE_BUTTON_EVENT:  # 发射子弹事件
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:  # 向右移动-----第一个是按键按下的事件，第二个是检测按键是否为—>（方向键常量K_开头）
            #     print("向右移动...")  # 此种方法只能按下按键做一个动作，无法连续
        # 键盘模块
        # 要写在for循环外边，不然等循环完毕才会执行下方代码，太慢！下方按键方向检测与上方代码无关，所以不需要写在里面
        keys_pressed = pygame.key.get_pressed()  # 返回一个按键元组，如果对应按键按下，那么它的值会变为1，否则为0
        if keys_pressed[pygame.K_RIGHT]:  # 如果—>按下，那么它会持续变为1，直至松开-----用中括号捕捉按键
            self.hero.speed_x = 3  # 英雄速度为2
            self.log.write_log("向右移动...")
            print("向右移动...")
        elif keys_pressed[pygame.K_LEFT]:  # <—
            self.hero.speed_x = -3  # 英雄速度为2
            self.log.write_log("向左移动...")
            print("向左移动...")
        elif keys_pressed[pygame.K_UP]:  # up
            self.hero.speed_y = -3  # 英雄速度为2
            self.log.write_log("向上移动...")
            print("向上移动...")
        elif keys_pressed[pygame.K_DOWN]:  # down
            self.hero.speed_y = 3  # 英雄速度为2
            self.log.write_log("向下移动...")
            print("向下移动...")
        else:
            # 若无按键为1，英雄速度为0-----一定要设置，不然你这按一下飞机自己探索去了。。。
            self.hero.speed_x = 0
            self.hero.speed_y = 0

    def __check_collide(self):
        """碰撞检测"""
        # 子弹摧毁敌机
        if pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True):  # 前两个参数时精灵组，后两个是碰撞之后谁会自动销毁，1-3对应，2-4对应
            plane_sprites.kill_enemy += 1  # 如果摧毁敌机，击杀数+1
        # 方法一
        # if pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True, True):  # 前两个参数时精灵组，后两个是碰撞之后谁会自动销毁，1-3对应，2-4对应
        #     self.__game_over()  # 角色碰撞，游戏结束
        # 方法二
        enemy_s = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)  # 第一个是角色，第二个是敌机精灵组，若发生碰撞，敌机是否销毁，此函数返回与角色相撞的列表
        if len(enemy_s) > 0:
            self.log.write_log("(状态:游戏进行中时)<<<角色死亡原因：敌机碰撞死亡>>>")
            print("(状态:游戏进行中时)<<<角色死亡原因：敌机碰撞死亡>>>")
            self.hero.kill()  # 销毁飞机
            self.__game_over()  # 结束游戏

    def __update_sprites(self):
        self.back_group.draw(self.screen)  # 将精灵组中的精灵绘画到屏幕上
        self.enemy_group.draw(self.screen)  # 将精灵组中的精灵绘画到屏幕上
        self.hero_group.draw(self.screen)
        self.hero.bullet_group.draw(self.screen)
        """
        draw() 方法：负责将精灵的 image 绘制到屏幕的 rect 位置
        """
        self.back_group.update()  # 调用精灵组中每个精灵各自的update方法
        self.enemy_group.update()  # 调用精灵组中每个精灵各自的update方法
        self.hero_group.update()
        self.hero.bullet_group.update()

    # @staticmethod
    def __game_over(self):
        """游戏结束"""

        self.log.write_log("(状态:游戏清屏中时)角色阵亡，死亡坐标：{}".format(self.hero.rect))
        print("(状态:游戏清屏中时)角色阵亡，死亡坐标：{}".format(self.hero.rect))
        self.log.write_log("Game Over...")
        print("Game Over...")
        clear = "游戏清屏"
        clear2 = "-"
        self.log.write_log((clear2 * 50) + clear + (clear2 * 50))
        print((clear2 * 50) + clear + (clear2 * 50))
        self.log.write_log("由于游戏库卸载，部分清屏数据无法录入日志！\n")
        plane_sprites.enemy_successfully = 0
        pygame.quit()  # 卸载库pygame，这里卸载一下是为了清除数据
        # exit()  # 中止程序
        self.__init__()  # 之前卸载之后，这里需要重新初始化
        self.i = 1  # 回到主页

    def fraction_show(self):
        """分数展示"""
        # 分数数字加载
        num0 = pygame.image.load(r".\images\0.png")
        num1 = pygame.image.load(r".\images\1.png")
        num2 = pygame.image.load(r".\images\2.png")
        num3 = pygame.image.load(r".\images\3.png")
        num4 = pygame.image.load(r".\images\4.png")
        num5 = pygame.image.load(r".\images\5.png")
        num6 = pygame.image.load(r".\images\6.png")
        num7 = pygame.image.load(r".\images\7.png")
        num8 = pygame.image.load(r".\images\8.png")
        num9 = pygame.image.load(r".\images\9.png")
        numx = pygame.image.load(r".\images\X.png")
        str_num = str(self.num)  # 将数字转为字符串
        # 首位判断
        if str_num[0: 1: 1] == "0":
            game.screen.blit(num0, (140, 173))
        elif str_num[0: 1: 1] == "1":
            game.screen.blit(num1, (140, 173))
        elif str_num[0: 1: 1] == "2":
            game.screen.blit(num2, (140, 173))
        elif str_num[0: 1: 1] == "3":
            game.screen.blit(num3, (140, 173))
        elif str_num[0: 1: 1] == "4":
            game.screen.blit(num4, (140, 173))
        elif str_num[0: 1: 1] == "5":
            game.screen.blit(num5, (140, 173))
        elif str_num[0: 1: 1] == "6":
            game.screen.blit(num6, (140, 173))
        elif str_num[0: 1: 1] == "7":
            game.screen.blit(num7, (140, 173))
        elif str_num[0: 1: 1] == "8":
            game.screen.blit(num8, (140, 173))
        elif str_num[0: 1: 1] == "9":
            game.screen.blit(num9, (140, 173))
        else:
            game.screen.blit(numx, (140, 173))
        # 末尾判断
        if str_num[1: 2: 1] == "0":
            game.screen.blit(num0, (238, 173))
        elif str_num[1: 2: 1] == "1":
            game.screen.blit(num1, (238, 173))
        elif str_num[1: 2: 1] == "2":
            game.screen.blit(num2, (238, 173))
        elif str_num[1: 2: 1] == "3":
            game.screen.blit(num3, (238, 173))
        elif str_num[1: 2: 1] == "4":
            game.screen.blit(num4, (238, 173))
        elif str_num[1: 2: 1] == "5":
            game.screen.blit(num5, (238, 173))
        elif str_num[1: 2: 1] == "6":
            game.screen.blit(num6, (238, 173))
        elif str_num[1: 2: 1] == "7":
            game.screen.blit(num7, (238, 173))
        elif str_num[1: 2: 1] == "8":
            game.screen.blit(num8, (238, 173))
        elif str_num[1: 2: 1] == "9":
            game.screen.blit(num9, (238, 173))
        else:
            game.screen.blit(numx, (238, 173))

    def start(self):
        """开始游戏"""

        while True:  # 主程序
            # self.__init__()  # 初始化程序
            start_background = pygame.image.load(r".\images\background.png")  # 首页背景加载
            start_image = pygame.image.load(r".\images\start.png")  # 首页开始图片加载
            exit_image = pygame.image.load(r".\images\exit.png")  # 首页退出图片加载
            fraction_background = pygame.image.load(r".\images\fraction_background.png")  # 分数背景板加载
            game.screen.blit(start_background, (0, 0))  # 首页背景显示
            game.screen.blit(start_image, (90, 470))  # 首页“开始游戏”显示
            game.screen.blit(exit_image, (90, 525))  # 首页“退出游戏”显示
            game.screen.blit(fraction_background, (130, 110))  # 分数背景板展示
            game.fraction_show()  # 展示分数
            self.log.write_log("(状态:游戏主页面时)上局分数：{}".format(self.num))  # 记录日志分数
            pygame.display.update()  # 更新屏幕

            # 首页
            while self.i:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:  # 按s开始
                        self.log.write_log("<<<##########开始游戏事件(s)##########>>>")
                        plane_sprites.kill_enemy = 0  # 开始游戏时重置分数
                        self.i = 0  # 0开始游戏
                        break
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_t:  # 按t退出
                        self.log.write_log("(状态:游戏主页面时)<<<退出游戏事件(t)>>>")
                        print("(状态:游戏主页面时)<<<退出游戏事件>>>（t）")
                        pygame.quit()  # 卸载库pygame
                        exit()  # 中止程序
                    if event.type == pygame.QUIT:  # 右上角X-----退出事件
                        self.log.write_log("(状态:游戏主页面时)<<<右上角关闭事件(X)>>>")
                        print("(状态:游戏主页面时)<<<右上角关闭事件(X)>>>")
                        self.log.write_log("<<<==========(状态:游戏退出时)游戏清屏==========>>>")
                        pygame.quit()  # 卸载库pygame
                        exit()  # 中止程序

            self.log.write_log("Game Start...")  # 写入日志
            print("Game Start...")

            # 游戏开始
            while True:
                # 设置刷新帧率
                self.clock.tick(plane_sprites.SCREEN_TICK)
                # 事件监听
                self.__event_handler()
                # 碰撞检测
                self.__check_collide()
                # 敌方成功次数检测
                if plane_sprites.enemy_successfully == 3:  # 控制敌机成功次数
                    self.log.write_log("(状态:游戏进行中时)<<<敌机成功逃脱3次，角色失败>>>")  # 写入日志
                    print("(状态:游戏进行中时)<<<敌机成功逃脱3次，角色失败>>>")
                    self.__game_over()
                # 更新/绘制精灵组
                self.__update_sprites()
                # 逃脱显示
                if plane_sprites.enemy_successfully == 0:
                    self.screen.blit(self.enemy_successfully_num_0, (0, 659))
                elif plane_sprites.enemy_successfully == 1:
                    self.screen.blit(self.enemy_successfully_num_1, (0, 659))
                elif plane_sprites.enemy_successfully == 2:
                    self.screen.blit(self.enemy_successfully_num_2, (0, 659))
                elif plane_sprites.enemy_successfully == 3:
                    self.screen.blit(self.enemy_successfully_num_3, (0, 659))
                else:
                    self.screen.blit(self.enemy_successfully_num_x, (0, 659))
                    self.log.write_log("当前敌机逃脱数：{}".format(plane_sprites.enemy_successfully))

                # 更新显示
                pygame.display.update()
                # 游戏进程结束检测
                if self.i == 1:
                    break


# 只有在当前文件运行才会开始，被导入其他文件时，无法运行
if __name__ == '__main__':
        game = GameStart()  # 创建游戏
        game.start()  # 启动游戏

