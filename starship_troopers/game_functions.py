import sys

import pygame

from missile import Missile


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
	'''
	When an update is called on the group, it calls the update
	each element of the group. In this case, bullet.update()
	'''
	missiles.update_position()

	# Get rid of missiles that have disappeared.
	for missile in missiles.copy():
		if missile.rect.bottom <= 0:	
			missiles.remove(missile)

def update_screen(game_settings, screen, starship, missiles):
	"""Update the rect surfaces  on the screen and flip to the new screen."""
	
	# Update the screen
	screen.fill(game_settings.screen_bg_colour)

	# Redraw all missiles.
	for missile in missiles.sprites():
		missile.draw_missile()

	# Redraw the starship
	starship.draw_starship()

	# Make the most recently drawn screen visible.
	pygame.display.flip()
