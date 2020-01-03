import pygame

# Starship class
class Starship():
	"""A class representing the starship."""
	def __init__(self, game_settings, screen):
		"""Initialise all the attributes of the starship class."""

		self.screen = screen
		self.screen_rect = screen.get_rect()		

		# Create the ship 
		self.rect = pygame.Rect(0, 0, 
			game_settings.starship_width, game_settings.starship_height)
		self.colour = game_settings.starship_colour
		
		# Positioning
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Float positions
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Move flags
		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False

	def update_position(self, game_settings):
		"""Updates the float positions depending on the move flags."""
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.x += game_settings.starship_speed_factor
		elif self.move_left and self.x > 0:
			self.x -= game_settings.starship_speed_factor				
	
		self.rect.x = self.x

		if self.move_up and self.y > 0:
			self.y -= game_settings.starship_speed_factor
		elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += game_settings.starship_speed_factor 

		self.rect.y = self.y

	def draw_starship(self):
		"""Draws the starship to the screen."""
		pygame.draw.rect(self.screen, self.colour, self.rect) 
