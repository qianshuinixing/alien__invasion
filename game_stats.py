class GameStats():
	def __init__(self , setting):
		self.setting = setting
		self.reset_stats()
		self.game_active = False
		self.score_base = 10
		
	def reset_stats(self):
		self.ships_left = self.setting.ship_limit
		self.score = 0
		self.level = 1
	
	def update_score(self , nums):
		self.score += nums * self.score_base
	
	def add_level(self):
		self.level += 1
		
	def sub_life():
		self.ships_left -= 1