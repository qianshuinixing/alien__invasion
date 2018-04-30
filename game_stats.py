class GameStats():
	def __init__(self , setting):
		self.setting = setting
		self.reset_stats()
		self.game_active = False
		
	def reset_stats(self):
		self.ships_left = self.setting.ship_limit
		self.score = 0