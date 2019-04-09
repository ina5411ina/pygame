import pygame
from pygame.locals import *

class Box(pygame.sprite.Sprite):
	def __init__(self,x,y,width,height):
		super(Box,self).__init__()
		self.surf=pygame.Surface((width,height))
		self.surf.fill((255, 255, 0))
		self.rect = self.surf.get_rect()
		self.x=x
		self.y=y
		self.width=width
		self.height=height
