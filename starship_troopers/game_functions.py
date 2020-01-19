import sys

import pygame
from pygame.sprite import Sprite

from missile import Missile
from alien import Alien

def check_for_events(game_settings, screen, starship, missiles):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_for_keydown_events(event, game_settings, screen, starship, missiles)
		elif event.type == pygame.KEYUP:
			check_for_keyup_events(event, starship)

def check_for_keydown_events(event, game_settings, screen, starship, missiles):
	"""Respond to key presses."""
	if event.key == pygame.K_RIGHT:
		starship.move_right = True
	elif event.key == pygame.K_LEFT:
		starship.move_left = True
	elif event.key == pygame.K_UP:
		starship.move_up = True
	elif event.key == pygame.K_DOWN:
		starship.move_down = True
	elif event.key == pygame.K_SPACE:
		launch_missile(game_settings, screen, starship, missiles)	
	elif event.key == pygame.K_q:
		sys.exit()

def launch_missile(game_settings, screen, starship, missiles):
	"""Launch a  missile and add it to the missiles group."""
	new_missile = Missile(screen, game_settings, starship)
	missiles.add(new_missile)

def check_for_keyup_events(event, starship):
	"""Respond to key releases."""
	if event.key == pygame.K_RIGHT:
		starship.move_right = False
	elif event.key == pygame.K_LEFT:
		starship.move_left = False
	elif event.key == pygame.K_UP:
		starship.move_up = False
	elif event.key == pygame.K_DOWN:
		starship.move_down = False

def update_missiles_position_and_count(missiles):
	"""Update the position of missiles and get rid of old missiles."""
	# Update missiles positions.
	for missile in missiles.sprites():
		missile.update_position()

	# Get rid of missiles that have disappeared.
	for missile in missiles.copy():
		if missile.rect.bottom <= 0:	
			missiles.remove(missile)

def get_number_aliens_x(game_settings, alien_width):
	"""Returns the number of aliens per row."""
	available_space_x = game_settings.screen_width - (2 * alien_width)	
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x 

def get_number_alien_rows(game_settings, starship_height, alien_height):
	"""Returns the number of alien rows."""
	available_space_y = game_settings.screen_height - (3 * alien_height) - 3 * starship_height
	number_alien_rows = int(available_space_y / (2 * alien_height))
	return number_alien_rows

def create_alien(game_settings, screen, column_number, row_number, aliens):
	"""Creates an alien"""
	alien = Alien(game_settings, screen)
	alien_width = alien.rect.width
	alien_height = alien.rect.height
	alien.x = alien_width + 2 * alien_width * column_number
	alien.y = alien_height + 2 * alien_height * row_number
	alien.rect.x = alien.x
	alien.rect.y = alien.y
	aliens.add(alien)

def create_alien_fleet(game_settings, screen, starship, aliens):
	"""Creates the alien fleet."""
	alien = Alien(game_settings, screen)
	number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
	number_alien_rows = get_number_alien_rows(game_settings, starship.rect.height, alien.rect.height)

	# Create rows of aliens
	for row_number in range(number_alien_rows):
		for column_number in range(number_aliens_x):
			create_alien(game_settings, screen, column_number, row_number, aliens)

def check_fleet_edges(game_settings, aliens):
	"""Check if any of the fleet's aliens have reach the edge and then act accordingly."""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(game_settings, aliens)
			break

def change_fleet_direction(game_settings, aliens):
	"""Move the entire fleet down and then change the fleet direction."""
	for alien in aliens.sprites():
		alien.y += game_settings.alien_fleet_drop_speed
		alien.rect.y = alien.y
	game_settings.alien_fleet_direction *= -1 

def update_aliens(game_settings, aliens):
	"""
	Check if the fleet is at the edge. The check moves the fleet downwards, which is then followed by updating the state of all the aliens.
	"""
	check_fleet_edges(game_settings, aliens)
	aliens.update()

def update_screen(game_settings, screen, starship, missiles, aliens):
	"""Update the rect surfaces on the screen and flip to the new screen."""
	# Update the screen
	screen.fill(game_settings.screen_bg_colour)

	# Redraw all missiles.
	for missile in missiles.sprites():
		missile.draw_missile()

	# Redraw the starship
	starship.draw_starship()

	# Redraw all the aliens
	for alien in aliens.sprites():
		alien.draw_alien()

	# Make the most recently drawn screen visible.
	pygame.display.flip()
