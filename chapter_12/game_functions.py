import pygame
import sys
from bullet import Bullet

def check_events_keydown(event,screen,ship,bullets):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			ship.moving_right = True
		if event.key == pygame.K_LEFT:
			ship.moving_left = True
		if event.key == pygame.K_UP:
			ship.moving_top = True
		if event.key == pygame.K_DOWN:
			ship.moving_down = True
		if event.key == pygame.K_SPACE :
			if len(bullets) < 3:
				bullet = Bullet(screen,ship)
				bullets.add(bullet)
		
			
def check_events_keyup(event,ship):
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT:
			ship.moving_right = False
		if event.key == pygame.K_LEFT:
			ship.moving_left = False
		if event.key == pygame.K_UP:
			ship.moving_top = False
		if event.key == pygame.K_DOWN:
			ship.moving_down = False	
				

def check_events(screen,ship,bullets):
	#  监视键盘和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		check_events_keydown(event,screen,ship,bullets)
		check_events_keyup(event,ship)

def update_bullets(bullets,screen):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.right > 1500:
			bullets.remove(bullet)
			print(len(bullets))		

def update_screen(bullets):
	for bullet in bullets.sprites():
		bullet.draw_bullet()
