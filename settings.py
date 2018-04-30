class Settings():
	"""存储《外星人入侵》的所有设置的类"""
	def __init__(self):
		"""初始化游戏的设置"""
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		#子弹参数设置
		self.bullet_speed_factor = 1
		self.bullet_width = 1000
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullet_allowed = 10
		
		# 外星人参数设置
		
		self.alien_speed_factor_y = 20
		
		
		# 飞船设置
		self.ship_limit = 3
		
		
		# 游戏加速因子
		self.speedup_scale = 1.1
		
		self.initialize_dynamic_setting()
		
	def initialize_dynamic_setting(self):
		"""初始化随游戏进行而变化的设置"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor_x = 1
		#飞船飞行的方向
		self.fleet_direction = 1
		
	def increase_speed(self):
		"""提高游戏速度"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor_x *= self.speedup_scale