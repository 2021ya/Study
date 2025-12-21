# 游戏精灵类
import os
import random
import pygame


# 敌机成功数量
enemy_successfully = 0
# 击杀数数量
kill_enemy = 0
# 屏幕大小常量
SCREEN_RECT = (480, 700)
# 刷新帧率常量
SCREEN_TICK = 60
# 创建敌人事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建子弹自动发射事件
FIRE_BUTTON_EVENT = pygame.USEREVENT + 1  # 这个事件本身是个整数，之前的事件占用了，这次就加上1


class Log(object):
    """日志记录"""
    def __init__(self):
        dir_exists = os.path.exists(r".\log")  # 判断路径是否存在
        if not dir_exists:  # 如果不存在，新建目录
            os.mkdir(r".\log")

    @staticmethod
    def write_log(text):  # 传入需要写入的文件
        """保存日志"""
        try:
            with open(r".\log\log.txt", "a", encoding="GBK") as f:  # 以GBK编码格式追加文本
                f.write(text + "\n")
                f.close()  # 关闭文件
        except IOError:
            print("写入异常：", IOError)
        except Exception as e:
            print("未知异常：", e)
        else:
            print("写入成功")
        finally:
            # print("退出写入函数")
            pass


log = Log()  # 创建日志精灵


def enemy_successfully_count():
    global enemy_successfully  # 之前的知识，global函数，首先声明我要修改全局变量了
    enemy_successfully += 1  # 然后直接修改
    print("敌机逃脱数+1")
    log.write_log("敌机逃脱数+1")


class GameSprites(pygame.sprite.Sprite):  # 继承一下父类游戏精灵的方法，以免重复代码（开发子类的时候，不主动调用父类的话，不能使用父类的方法）-----游戏精灵类
    """游戏精灵基类,负责加载图像，加载碰撞箱，设置初始速度"""
    def __init__(self, image_path, speed=1):
        super().__init__()  # 继承父类的初始化方法
        self.image = pygame.image.load(image_path)  # 加载图像为"自己.image"
        self.rect = self.image.get_rect()  # 使用.get_rect()可直接返回碰撞箱，默认坐标为(0.0)，大小为图片大小
        self.speed = speed

    def update(self):
        self.rect.y += self.speed  # 当刷新时，碰撞箱y值加速度


class Background(GameSprites):
    """背景精灵类"""
    def __init__(self, is_alt=False):
        super().__init__(r".\images\background.png", speed=1)
        if is_alt:  # 判断是否为交替图像
            self.rect.y = -self.rect.height  # 如果是Ture,就将图像放到屏幕外部的上方

    def update(self):
        """一张背景超出屏幕之外时，重新给它弄到屏幕上方"""
        super().update()
        if self.rect.y >= self.rect.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprites):
    """敌机精灵类"""

    def __init__(self, enemy_path):  # 初始化创建敌机
        super().__init__(enemy_path, speed=random.randint(2, 7))  # 调用精灵基类创建敌机并指定敌机初始随机速度
        # self.rect.y = -self.rect.height  # 敌机在屏幕上方外部生成
        self.rect.bottom = 0  # bottom（低部）可将碰撞箱底部设置为0，这样和上句代码完全相同
        self.rect.x = random.randint(0, 480 - self.rect.width)  # 指定飞机初始随机位置

    def __del__(self):
        log.write_log("敌机死亡坐标：{}".format(self.rect))
        print("敌机死亡坐标：{}".format(self.rect))

    def update(self):
        super().update()  # 敌机从上方往下方飞行
        if self.rect.y >= 700:  # 判断敌机是否飞出屏幕
            enemy_successfully_count()  # 敌机成功数加一
            log.write_log("敌机超出三界之外，不在我的掌控之中，所以即将销毁！！！")
            print("敌机超出三界之外，不在我的掌控之中，所以即将销毁！！！")
            log.write_log("当前敌机逃脱数：{}".format(enemy_successfully))
            self.kill()  # 如果飞出删除此敌机


class Hero(GameSprites):

    def __init__(self):
        super().__init__(r".\images\me1.png", speed=0)
        self.speed_x = 0
        self.speed_y = 0
        self.rect.x = 189  # 角色初始处于屏幕中间位置
        self.rect.bottom = 580  # 角色初始处于屏幕距离底部60像素位置
        self.bullet_group = pygame.sprite.Group()  # 创建子弹精灵组

    def fire(self):
        """子弹方法"""
        bullet = Bullet(self)  # 创建角色左方子弹
        bullet2 = Bullet(self, left=False)  # 创建角色右方子弹
        self.bullet_group.add(bullet, bullet2)  # 将子弹添加到子弹精灵组
        log.write_log("Fire bullet...")
        print("Fire bullet...")

    def update(self):
        """移动控制"""
        # 左右上下移动
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # 屏幕边界控制-----这里不要用elif，不然有bug，可以飞出屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 480 - self.rect.width:
            self.rect.x = 480 - self.rect.width
        if self.rect.y < 10:
            self .rect.y = 10
        if self.rect.y > 700 - 140:
            self.rect.y = 700 - 140

    def __del__(self):
        log.write_log("角色阵亡，死亡坐标：{}".format(self.rect))
        print("角色阵亡，死亡坐标：{}".format(self.rect))


class Bullet(GameSprites):

    def __init__(self, hero, left=True):
        super().__init__(r".\images\bullet1.png", speed=-5)  # 使用父类方法创建子弹精灵
        self.rect.x = hero.rect.x + 15  # 飞机左侧子弹初始位置
        self.rect.y = hero.rect.y + 16  # 飞机子弹初始高度
        if not left:
            self.rect.x = hero.rect.x + 83  # 飞机右侧子弹初始位置

    def update(self):
        super().update()
        if self.rect.bottom <= 0:  # 子弹底部飞出屏幕，销毁
            self.kill()

    def __del__(self):
        log.write_log("子弹销毁--坐标为{}".format(self.rect))
        print("子弹销毁--坐标为{}".format(self.rect))
