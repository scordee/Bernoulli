import pygame
from pygame.sprite import Sprite

class Missile(Sprite):
	"""A simple representation of the missile class."""
	
	def __init__(self, screen, game_settings, starship):
		"""Initialise all the attributes of the bullet class."""
		super().__init__()
		self.rect = pygame.Rect(0, 0, game_settings.missile_width, 
			2*game_settings.missile_radius)
		self.screen = screen	

		# Positioning of the missile
		self.rect.centerx = starship.rect.centerx
		self.rect.bottom = starship.rect.top

		# Float value of the missile
		self.y = float(self.rect.y)

		# Other properties
		self.colour = game_settings.missile_colour
		self.speed = game_settings.missile_speed_factor		
		self.radius = game_settings.missile_radius
 
	def update_position(self):
		"""Updates the y-coordinate of the missile."""
		self.y -= self.speed
		self.rect.y = self.y

	def draw_missile(self):	
		"""Draws the missile to the screen."""
		pygame.draw.circle(self.screen, self.colour, self.rect.center, self.radius)
