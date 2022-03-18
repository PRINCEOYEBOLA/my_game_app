#importing  a function for events created as game_functions module to manage the game events and other settings
#Importing the code from the game_function module (events, screen, ship, settings) 

import pygame

from pygame.sprite import Group

from settings import Settings

from ship import Ship

import game_functions as gf

def run_game():
	# Initializing pygame, settings and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Aliens Invasion")
	#Making a ship
	ship = Ship(ai_settings, screen)
	#Create a group to store the bullets
	bullets = Group()
	#Set the background color.
	bg_color = (0, 0, 0)
	# Start the main loop for the game.
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		# Get rid of bullets that have disappeared.
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		#print(len(bullets))
		# redraw the screen to reflect the background color
		gf.update_screen(ai_settings, screen, ship, bullets)
		bullets.update()
		
run_game()
