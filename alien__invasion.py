import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

from game_stats import GameStats
from button import Button


def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	setting = Settings()
	
	screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
	pygame.display.set_caption("外星入侵")
	

	stats = GameStats(setting)
	#设置背景色
	bg_color = setting.bg_color
	
	#创建一艘飞船
	ship = Ship(screen)
	
	#建立一个管理子弹的编组
	bullets = Group()
	
	aliens = Group()
	
	gf.create_fleet(setting , screen , ship , aliens)
	
	# 创建Play按钮
	play_button = Button(setting , screen , "play")
	
	#开始游戏主循环
	while True:
		#监听鼠标和键盘事件
		gf.check_events(ship, bullets, screen, setting ,stats , play_button , aliens )
		
		if stats.game_active:
			#更新飞船的位置
			ship.update(setting)
			#更新子弹的位置
			bullets.update()
			#检查子弹是否与外星人有碰撞， 如果有碰撞，两者都消失
			gf.delet_alien(aliens, bullets , setting , screen , ship )
			#更新外星人的位置
			gf.update_aliens(setting, aliens)
			gf.check_game_over(stats , setting, aliens , ship ,screen , bullets)
			#删除溢出屏幕的子弹
			gf.del_bullet(bullets)
		#更新屏幕
		gf.update_screen(screen , ship , setting , bullets , aliens  , play_button ,stats)

run_game()