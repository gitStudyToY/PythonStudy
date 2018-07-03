import sys
import pygame
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullet import Bullet

def see_blue_sky():
	pygame.init()
	screen = pygame.display.set_mode((1200,500))
	pygame.display.set_caption("Sky")
	
	ship = Ship(screen)
	
	bullets = Group()
	while True:
		screen.fill((230,230,230))
		gf.check_events(screen,ship,bullets)
		gf.update_bullets(bullets,screen)
		gf.update_screen(bullets)
		ship.blitme()
		pygame.display.flip()


see_blue_sky()
