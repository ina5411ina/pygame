import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	def __init__(self,x,y,color):
		super(Player,self).__init__()
		self.surf=pygame.Surface((50,50))
		self.surf.fill(color)
		self.rect = self.surf.get_rect()
		self.x=x
		self.y=y
		self.lm=False #left move
		self.rm=False
		self.canjump=True
		self.xspd=10
		self.yspd=0
		self.keepjmp=True
		self.jmptop=True
		self.lastx=0
		self.hp=300
		self.pigsize=80

	def startmove(self,key,p):
		if key==pygame.K_LEFT:
			self.lm=True
		if key==pygame.K_RIGHT:
			self.rm=True

	def stopmove(self,key,p):
		if key==pygame.K_LEFT:
			self.lm=False
		if key==pygame.K_RIGHT:
			self.rm=False

	def jumpspd(self):
		if self.yspd>-20 and self.jmptop==False:
			self.yspd-=2
			if self.yspd==-20:
				self.jmptop=True
		elif self.yspd<20:
			self.yspd+=2

	def run(self):
		if abs(self.x-self.lastx)<5:
			if self.hp>-10:
				self.hp-=2
			self.lastx=self.x
		else:
			if self.hp<300 :
				self.hp+=5
			self.lastx=self.x
		if self.lm==True and self.x>0:
			self.x-=self.xspd
		if self.rm==True and self.x<1150:
			self.x+=self.xspd
		if self.keepjmp==True and self.canjump==True:
			self.canjump=False
			if self.jmptop==True:
				self.jmptop=False
		if self.canjump==False:
			self.y+=self.yspd
			self.jumpspd()

	def boxcheck(self,box):
		if box.x<(self.x+self.pigsize) and box.x+box.width>self.x:
			if self.y<box.y+box.height and self.y>box.y:
				self.jmptop=True
				self.yspd=0
				self.y=box.y+box.height+1
			if (self.y+self.pigsize)>box.y and self.y<box.y:
				#print((self.y+self.pigsize),box.y+box.height)
				self.yspd=0
				self.y=box.y-self.pigsize
				self.canjump=True
				self.jmptop=True
		if self.y > (800-self.pigsize):
				self.yspd=0
				self.y=(800-self.pigsize)
				self.canjump=True
				self.jmptop=True

	def downcheck(self,box):
		ch=False
		for b in box:
			if b.x<(self.x+self.pigsize) and b.x+b.width>self.x:
				ch=True
		if self.y==(800-self.pigsize) :
			ch=True
		if ch==False and self.canjump==True:
			self.jmptop=True
			self.canjump=False
