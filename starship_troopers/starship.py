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
			game_settings.ship_width, game_settings.ship_height)
		self.colour = game_settings.ship_colour
		
		# Positioning
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def draw_starship(self):
		"""Draws the starship to the screen."""
		pygame.draw.rect(self.screen, self.colour, self.rect) 
