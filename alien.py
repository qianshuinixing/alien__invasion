import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self , setting , screen):
		super().__init__()
		self.screen = screen
		self.setting = setting
		# 加载外星人图像，并设置其rect属性
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		# 每个外星人最初的位置
		self.rect.x = self.rect.width
		self.rect.x = self.rect.height
		
		# 存储外星人的准确位置
		self.x = float(self.rect.x)
		#外星人的飞行方向，向左或者向右
		#self.fleet_direction = 1 #1表示右移 -1表示左移
		self.y = float(self.rect.y)
	
	def update(self):
		self.x += self.setting.fleet_direction * self.setting.alien_speed_factor_x
		self.rect.x = self.x
	
	def check_edges(self):
		"如果外星人位于屏幕边缘， 就返回True"
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		