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
		self.game_settings = game_settings

		# Create the alien
		self.rect = pygame.Rect(0,0,
			self.game_settings.alien_width, self.game_settings.alien_height)
		self.colour = self.game_settings.alien_colour

		# Positioning the alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Cast alien positions from int to float
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def check_edges(self):
		"""Return True if alien is at edge of screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.x >= screen_rect.right:
			return True
		elif self.rect.x <= 0:
			return True

	def update(self):
		"""Move the alien right."""		
		self.x += (self.game_settings.alien_horizontal_speed_factor *
					self.game_settings.alien_fleet_direction) 
		self.rect.x = self.x		

	def draw_alien(self):
		"""Draw the alien at its current location."""
		pygame.draw.ellipse(self.screen, self.colour, self.rect)
