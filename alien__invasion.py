import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	setting = Settings()
	
	screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
	pygame.display.set_caption("外星入侵")
	
	#设置背景色
	bg_color = setting.bg_color
	
	#创建一艘飞船
	ship = Ship(screen)
	
	#建立一个管理子弹的编组
	bullets = Group()
	
	aliens = Group()
	
	gf.create_fleet(setting , screen , ship , aliens)
	
	#开始游戏主循环
	while True:
		#监听鼠标和键盘事件
		gf.check_events(ship , bullets , screen , setting)
		#更新飞船的位置
		ship.update(setting)
		#更新子弹的位置
		bullets.update()
		#删除溢出屏幕的子弹
		gf.del_bullet(bullets)
		#更新屏幕
		gf.update_screen(screen , ship , setting , bullets , aliens)

run_game()