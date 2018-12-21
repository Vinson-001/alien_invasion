

#import sys

import pygame
from pygame.sprite import Group  #pygame.sprite.Group

#导入Settings 类
from settings import Settings
from ship import Ship
import game_functions as gf


# 初始化游戏
# 创建屏幕
# 刷新最新显示
'''
def run_game():
   
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    
    # 设置背景颜色
    bg_color = (230,230,230)
    
    # 开始游戏的主循环
    while True:
        # 监控鼠标和键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # 每次循环都重绘屏幕
        screen.fill(bg_color)
                
        # 让最近绘制的屏幕可见
        pygame.display.flip()
    
'''
'''
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_with,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 创建一艘飞船
    ship = Ship(screen)
    
    # 设置背景颜色
    bg_color = (230,230,230)
    
    # 开始游戏的主循环
    while True:
        # 监控鼠标和键盘事件
        #for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        sys.exit()
        gf.check_events()
                
        # 每次循环都重绘屏幕
        #screen.fill(ai_settings.bg_color)
        #ship.blitme()
                
        # 让最近绘制的屏幕可见
        #pygame.display.flip() 
        gf.update_screen(ai_settings,screen,ship)   
''' 
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_with,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组 类似列表
    bullets = Group()
    # 设置背景颜色
    bg_color = (230,230,230)
    
    # 开始游戏的主循环
    while True:
        # 监控鼠标和键盘事件
        gf.check_events(ai_settings,screen,ship,bullets)
        # 更新位置
        ship.update() 
        gf.update_buttles(bullets)   
                
        print(len(bullets))
        # 每次循环都重绘屏幕
        gf.update_screen(ai_settings,screen,ship,bullets)
run_game()
