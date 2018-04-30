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
		
	def prep_score(self):
		"""将得分转换为一幅渲染的图像"""
		score_str = str(self.stats.score)
		#将font 渲染成一个图像 你是谁啊 我真的不认识你啊 你个大撒比 哈哈哈哈哈
		self.score_image = self.font.reder(score_str , True , self.text_color , self.setting.bg_color)
		
		#将得分放在屏幕右上角
		seslf.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20