import pygame.font

class Scoreboard():
	"""显示得分信息的类"""
	
	def __init__(self , setting , screen , stats):
		"""初始化显示得分涉及的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.setting = setting
		self.stats = stats
		
		# 显示得分信息时使用的字体设置
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None , 48)
		
		# 准备初始得分图像
		self.prep_score()
	
	def draw_ships_left(self):
		ships_left = self.stats.ships_left
		
		for count in range(ships_left):
			#加载飞船图像并获取其外接矩形
			image = pygame.image.load('images\ship.bmp')
			rect = image.get_rect()
			rect.top = 20
			rect.centerx = 20 + count*(rect.width+20)
			self.screen.blit(image , rect)
	
	def prep_level(self):
		"""将等级转换为一副渲染的图像"""
		level_str = str(self.stats.level)
		self.level_image = self.font.render(level_str , True , self.text_color , self.setting.bg_color)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.centerx = self.screen_rect.centerx
		self.level_rect.top = 20
	
	def draw_level_board(self):
		self.prep_level()
		self.screen.blit(self.level_image , self.level_rect)
	
	def prep_score(self):
		"""将得分转换为一幅渲染的图像"""
		score_str = str(self.stats.score)
		#将font 渲染成一个图像 你是谁啊 我真的不认识你啊 你个大撒比 哈哈哈哈哈
		self.score_image = self.font.render(score_str , True , self.text_color , self.setting.bg_color)
		
		#将得分放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
	
	def draw_score_board(self):
		self.prep_score()
		self.screen.blit(self.score_image , self.score_rect)