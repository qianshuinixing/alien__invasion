class Settings():
	"""存储《外星人入侵》的所有设置的类"""
	def __init__(self):
		"""初始化游戏的设置"""
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		self.ship_speed_factor = 1
		#子弹参数设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullet_allowed = 3
		
		# 外星人参数设置
		self.alien_speed_factor = 1