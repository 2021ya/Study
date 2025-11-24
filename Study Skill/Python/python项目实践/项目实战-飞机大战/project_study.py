import pygame  # 导入库

# 游戏初始化
pygame.init()  # 初始化，加载库中函数到内存

# 创建英雄碰撞箱
hero_rect = pygame.Rect(195, 520, 90, 90)  # 对应分别是：x,y,weight,height
# print(f"对象坐标原点({hero_rect.x},{hero_rect.y})")
# print(f"对象大小{hero_rect.size}")

# 绘制原始屏幕
screen = pygame.display.set_mode((480, 700))  # 默认有三个参数，当前传入一个参数，默认都为0,此函数返回的是游戏主窗口

"""
size 指定屏幕的 宽和 高，默认创建的窗口大小和屏幕大小一致
flags 参数指定屏幕的附加选项，例如是否全屏等等，默认不需要传递
depth 参数表示颜色的位数，默认自动匹配
"""

# 加载背景-----绘制图像到屏幕步骤>>1.加载图像2.绘制图像3.刷新屏幕
background = pygame.image.load(r".\images.\background.png")  # 加载图像到内存
screen.blit(background, (0, 0))  # 绘制背景到（0，0）
# pygame.display.update()  # 刷新屏幕,可在绘制完同事出现的图像时，再刷新

# 绘制英雄
hero = pygame.image.load(r".\images.\me1.png")
screen.blit(hero, (hero_rect.x, hero_rect.y))  # 绘制图像到碰撞箱里面
# pygame.display.update()

# 时钟
clock = pygame.time.Clock()

# 游戏循环----进入循环之后，应该记录的是用户的操作
while True:
    clock.tick(60)  # 设定循环每秒执行次数----用于屏幕刷新次数
    for event in pygame.event.get():  # 获取当前执行到此处代码的时候用户的操作
        if event.type == pygame.QUIT:  # 若检测到按右上角×，就退出
            pygame.quit()  # 卸载内存，避免占用
            exit()  # 直接终止当前程序
    screen.blit(background, (0, 0))  # 重新绘制背景到（0，0）
    screen.blit(hero, (hero_rect.x, hero_rect.y))  # 重新绘制英雄
    hero_rect.y -= 1  # 英雄自动向前移动
    if hero_rect.y <= -126:  # 判断英雄是否触顶
        hero_rect.y = 700  # 触顶之后将英雄碰撞箱（因为英雄一直在碰撞箱中）设置为700（底部）---传送到底部
    pygame.display.update()
    pass

#
# pygame.quit()  # 卸载内存，避免占用






































