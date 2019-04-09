import pygame
from pygame.locals import *

class Startscreen(pygame.sprite.Sprite):
	def __init__(self, flag):
		while(flag == 0):
			for event in pygame.event.get():
				if event.type==MOUSEBUTTONDOWN and event.button == 1:
					self.x, self.y = pygame.mouse.get_pos()
					if(self.x >= 472 and self.x <= 673 and self.y >=519 and self.y<= 660):
						flag=1
					elif(self.x >= 723 and self.x <= 919 and self.y >= 525 and self.y<= 661):
						exit()
				elif event.type==QUIT:
					exit()