import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A simple class representation of an alien."""
	def __init__(self, game_settings, screen):
		"""
		Initialises the attributes of the super class Sprite.
		Initialises all the attributes of the alien class.
		"""
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()

		# Create the alien
		self.rect = pygame.Rect(0,0
			game_settings.alien_height, game_settings.alien_width)
		self.colour = game_settings.alien_colour

		# Positioning the alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Cast alien positions from int to float
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
	
		# Other properties
		self.colour = game_settings.alien_colour

	def draw_alien(self):
		"""Draw the alien at its current location."""
		pygame.draw.eclipse(self.screen, self.colour, self.rect)
