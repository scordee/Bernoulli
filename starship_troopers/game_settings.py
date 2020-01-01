# Settings class
class Settings():
	"""Attribtutes with all the settings of the game."""
	def __init__(self):
		"""Initialise all the attributes of the settings class."""

		# Game screen attributes
		self.screen_width = 600
		self.screen_height = 600
		self.screen_bg_colour = (225, 176, 110)
		
		# Starship attributes
		self.ship_height = 40
		self.ship_width = 60
		self.ship_colour = (0, 0, 0)
		self.ship_speed_factor = 2
		
		# Missile properties
		self.missile_radius = 2
		self.missile_width = 0
		self.missile_colour = (0, 0, 0)
