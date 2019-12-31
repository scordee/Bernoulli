import sys

import pygame

from game_settings import Settings
from starship import Starship

def start_game():
	pygame.init()
	game_settings = Settings()
	
	screen = pygame.display.set_mode(
		(game_settings.screen_width, game_settings.screen_height))

	pygame.display.set_caption("Starship Troopers")

	# Create the starship
	starship = Starship(game_settings, screen)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# Redraw the screen at every pass through the loop 
		screen.fill(game_settings.screen_bg_colour)
		starship.draw_starship()
		
		# 
		pygame.display.flip()

start_game()
