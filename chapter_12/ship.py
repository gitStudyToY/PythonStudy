import pygame

class Ship():
	def __init__(self,screen):
		#设置图像元素
		self.screen = screen
		self.image = pygame.image.load("images\ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.moving_right = False
		self.moving_left = False
		self.moving_top = False
		self.moving_down = False
		self.speed_factor = 1
		

		#将图像放置在屏幕中央
		self.rect.left = self.screen_rect.left
		self.rect.centery = self.screen_rect.centery
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		self.update()
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.speed_factor
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= self.speed_factor
		if self.moving_top and self.rect.top > self.screen_rect.top:
			self.rect.centery -= self.speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += self.speed_factor
