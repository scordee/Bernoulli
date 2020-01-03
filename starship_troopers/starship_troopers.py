import sys

import pygame
from pygame.sprite import Group

import game_functions as gf
from game_settings import Settings
from starship import Starship
from missile import Missile

def start_game():
	pygame.init()
	game_settings = Settings()
	
	screen = pygame.display.set_mode(
		(game_settings.screen_width, game_settings.screen_height))

	pygame.display.set_caption("Starship Troopers")

	# Create the starship
	starship = Starship(game_settings, screen)

	# Create a group of missiles
	missiles = Group()

	while True:
		gf.check_for_events(game_settings, screen, starship, missiles)
		starship.update_position(game_settings)
		gf.update_missiles_position_and_count(missiles)
		gf.update_screen(game_settings, screen, starship, missiles)
	
start_game()
