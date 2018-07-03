import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	
	def __init__(self,screen,ship):
		super().__init__()
		self.rect = pygame.Rect(0,0,15,3)
		self.color = (60,60,60)
		
		self.screen = screen 
		self.rect.centery = ship.rect.centery
		self.rect.left = ship.rect.right
		self.x = float(self.rect.x)
		self.speed_factor = 1
		
		
	def update(self):
		self.x += self.speed_factor
		self.rect.x = self.x
		
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
		
		
		
