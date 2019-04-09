import pygame
from pygame.locals import *
from player import *
from box import *
from startscreen import *
import random

flag = 0
screen = pygame.display.set_mode((1200,800))
start = pygame.image.load('welcome.jpg')
start = pygame.transform.scale(start, (1200, 800))
startrect = start.get_rect()
screen.blit(start,startrect)
pygame.display.update()

Startscreen(flag)
running=True
pygame.init()
screen = pygame.display.set_mode((1200,800))
player1 = Player(550,550,(255,0,0))
backmove=-6100

clock=pygame.time.Clock()

P11 = pygame.image.load('pig1.png')
P11 = pygame.transform.scale(P11, (80, 80))
P12 = pygame.image.load('pig2.png')
P12 = pygame.transform.scale(P12, (80, 80))

background = pygame.image.load('realbackground1.jpg')
backgroundrect = background.get_rect()

while running:
	clock.tick(60)
	ticks = pygame.time.get_ticks()
	if(backmove >= 0):
		screen.blit(background,(0,0))
		if(player1.x >= 1080 and player1.x <= 1200 and player1.y <= 226 and player1.y >= -65):
			screen = pygame.display.set_mode((1200,800))
			start = pygame.image.load('welcome.jpg')
			start = pygame.transform.scale(start, (1200, 800))
			startrect = start.get_rect()
			screen.blit(start,startrect)
			pygame.display.update()
			player1 = Player(550,550,(255,0,0))
			backmove=-6100
			Startscreen(0)

	else:
		backmove+=1
		screen.blit(background,(0,backmove))
		#print(player1.y)
		if(player1.y >= 720):
			screen = pygame.display.set_mode((1200,800))
			start = pygame.image.load('welcome.jpg')
			start = pygame.transform.scale(start, (1200, 800))
			startrect = start.get_rect()
			screen.blit(start,startrect)
			pygame.display.update()
			player1 = Player(550,550,(255,0,0))
			backmove=-6100
			Startscreen(0)

	boxes=[]
	boxes.append(Box(933,306+backmove,267,30))
	boxes.append(Box(856,366+backmove,74,30))
	boxes.append(Box(748,417+backmove,81,28))
	boxes.append(Box(653,477+backmove,65,30))
	boxes.append(Box(551,533+backmove,60,27))
	boxes.append(Box(444,590+backmove,61,27))
	boxes.append(Box(366,641+backmove,32,31))
	boxes.append(Box(260,700+backmove,28,30))
	boxes.append(Box(317,754+backmove,68,31))
	boxes.append(Box(417,829+backmove,100,30))
	boxes.append(Box(550,908+backmove,150,30))
	boxes.append(Box(745,983+backmove,175,32))
	boxes.append(Box(932,1066+backmove,267,28))
	boxes.append(Box(602,1155+backmove,307,25))
	boxes.append(Box(950,1267+backmove,248,21))
	boxes.append(Box(462,1299+backmove,35,35))
	boxes.append(Box(319,1351+backmove,36,35))
	boxes.append(Box(752,1370+backmove,286,35))
	boxes.append(Box(547,1371+backmove,36,31))
	boxes.append(Box(90,1405+backmove,277,27))
	boxes.append(Box(446,1483+backmove,283,31))
	boxes.append(Box(128,1619+backmove,285,29))
	boxes.append(Box(459,1737+backmove,283,36))
	boxes.append(Box(854,1851+backmove,311,36))
	boxes.append(Box(503,1978+backmove,312,33))
	boxes.append(Box(258,2035+backmove,38,35))
	boxes.append(Box(346,2107+backmove,41,39))
	boxes.append(Box(0,2147+backmove,190,30))
	boxes.append(Box(421,2199+backmove,52,42))
	boxes.append(Box(344,2286+backmove,46,44))
	boxes.append(Box(566,2309+backmove,336,30))
	boxes.append(Box(278,2371+backmove,36,41))
	boxes.append(Box(958,2417+backmove,239,29))
	boxes.append(Box(617,2498+backmove,241,32))
	boxes.append(Box(0,2490+backmove,216,25))
	boxes.append(Box(926,2615+backmove,243, 26))
	boxes.append(Box(335,2610+backmove,235,23))
	boxes.append(Box(727,2726+backmove,238, 26))
	boxes.append(Box(95,2723+backmove,239,34))
	boxes.append(Box(429,2827+backmove,259,34))
	boxes.append(Box(0,2845+backmove,70,37))
	boxes.append(Box(159,2930+backmove,187,38))
	boxes.append(Box(402,3008+backmove,182,35))
	boxes.append(Box(631,3092+backmove,182,37))
	boxes.append(Box(830,3185+backmove,66,650))
	boxes.append(Box(1046,3224+backmove,154,57))
	boxes.append(Box(1047,3383+backmove,153,52))
	boxes.append(Box(1046,3547+backmove,154,54))
	boxes.append(Box(1050,3721+backmove,150,55))
	boxes.append(Box(1053,3904+backmove,147,53))
	boxes.append(Box(547,4035+backmove,367,54))
	boxes.append(Box(134,4205+backmove,303,56))
	boxes.append(Box(512,4367+backmove,304,55))
	boxes.append(Box(964,4500+backmove,236,43))
	boxes.append(Box(587,4701+backmove,386,53))
	boxes.append(Box(93,4643+backmove,79,69))
	boxes.append(Box(313,4754+backmove,76,69))
	boxes.append(Box(94,4892+backmove,75,64))
	boxes.append(Box(306,5000+backmove,78,69))
	boxes.append(Box(98,5114+backmove,77,70))
	boxes.append(Box(267,5231+backmove,66,59))
	boxes.append(Box(562,5409+backmove,28,52))
	boxes.append(Box(158,5610+backmove,260,42))
	boxes.append(Box(530,5783+backmove,301,47))
	boxes.append(Box(997,5929+backmove,97,54))
	boxes.append(Box(696,6091+backmove,129,54))
	boxes.append(Box(227,6157+backmove,60,56))
	boxes.append(Box(949,6262+backmove,251,54))
	boxes.append(Box(0,6369+backmove,139,55))
	boxes.append(Box(431,6453+backmove,330,55))
	boxes.append(Box(869,6667+backmove,331,68))
	boxes.append(Box(324,6781+backmove,437,58))

	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				screen = pygame.display.set_mode((1200,800))
				start = pygame.image.load('welcome.jpg')
				start = pygame.transform.scale(start, (1200, 800))
				startrect = start.get_rect()
				screen.blit(start,startrect)
				pygame.display.update()
				player1 = Player(550,550,(255,0,0))
				backmove=-6100
				Startscreen(0)
			player1.startmove(key=event.key,p=1)
		elif event.type==pygame.KEYUP:
			player1.stopmove(key=event.key,p=1)
		elif event.type==QUIT:
			running=False
	
	for b in boxes:
		player1.boxcheck(b)

	player1.downcheck(boxes)
	player1.run()

	if ticks%120>60:
		screen.blit(P11,(player1.x,player1.y))
	else:
		screen.blit(P12,(player1.x,player1.y))

	pygame.display.update()

screen.fill((0,0,0))
pygame.display.update()