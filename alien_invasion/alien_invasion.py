# coding=utf-8
import sys

import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

from alien import Alien

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard
 
def run_game():
	#  初始化 pygame 、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	
	#  创建一个用于存储子弹的编组
	bullets = Group()
	#  创建一个外星人编组
	aliens = Group()
	
	#创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	stats = GameStats(ai_settings)
	
	#  创建 Play 按钮
	play_button = Button(ai_settings, screen, "Play")
	sb = Scoreboard(ai_settings, screen, stats)
	
	#开始游戏的主循环
	while True:
		 
		 #监视键盘和鼠标事件
		 gf.check_events(ai_settings, screen, ship, bullets,stats,play_button,aliens,sb)
		 
		 if stats.game_active:
			 #更新飞船位置
			 ship.update()
			 #更新子弹
			 gf.update_bullets(bullets,aliens,ai_settings, screen, ship,sb,stats)
			 #更新外星人
			 gf.update_aliens(ai_settings,aliens,ship,stats,screen,bullets,sb)
		 #让颜色填充整个屏幕, 每次循环时都重绘屏幕
		 gf.update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,sb)
				 
		 
run_game()
			 
	
