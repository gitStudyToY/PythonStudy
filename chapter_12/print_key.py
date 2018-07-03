import sys
import pygame

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((500,500))
	pygame.display.set_caption("Print Key")
	
	while True:
		screen.fill((250,250,250))
		
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				print(event.key)
			
		
		pygame.display.flip()
		
run_game()
