import sys

import pygame
import plane_sprites


# 初始化
screen = pygame.display.set_mode((400, 700))  # 绘制屏幕，设置屏幕（元组）
background = pygame.image.load(r".\images\background.png")  # 加载背景
screen.blit(background, (0, 0))  # 绘制图片到屏幕

# 英雄
hero = plane_sprites.GameSprites(r".\images\me1.png", speed=-1)  # 创建英雄，默认速度为1,这里改为-1
enemy1 = plane_sprites.GameSprites(r".\images\enemy1.png", speed=2)
enemy2 = plane_sprites.GameSprites(r".\images\enemy2.png", speed=1)

# 精灵组
enemy_group = pygame.sprite.Group(enemy1, enemy2)

# 游戏循环
while True:

    # 捕捉按键模块
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # -----QUIT
            pygame.quit()
            exit()

    # 帧率tick设置-----控制当前每秒循环执行次数
    pygame.time.Clock().tick(60)

    # 绘制背景
    screen.blit(background, (0, 0))

    # 绘制角色
    screen.blit(hero.image, hero.rect)
    # screen.blit(enemy1.image, enemy1.rect)
    enemy_group.draw(screen)

    # 更新屏幕
    pygame.display.update()

    # 更新绘画移动
    # enemy_group.draw(screen)  # 精灵组内部重新绘画一遍
    enemy_group.update()  # 精灵组内部全部调用自己的update方法
    hero.update()  # 更新角色移动，调用自己的update方法
    # enemy1.update()  # 更新角色移动






















