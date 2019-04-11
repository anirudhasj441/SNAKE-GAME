import random , os
import pygame


pygame.init()

x=540
y=960


DISPLAYSURF=pygame.display.set_mode((x,y))
pygame.display.set_caption('snake game')


bg=(0,0,0)
BLUE=(0,0,255)
white=(255,255,255)
red=(255,0,0)


font=pygame.font.SysFont( None ,30)
font1=pygame.font.SysFont( None ,39)
font3=pygame.font.SysFont( None ,10)


def text_screen(text,colour,x1,y1):
		screen_text=font.render(text, True ,colour)
		DISPLAYSURF.blit(screen_text,(x1,y1))


def txt(text,colour,x1,y1):
		screen_text=font1.render(text, True ,colour)
		DISPLAYSURF.blit(screen_text,(x1,y1))
		

def text_objects(text, font):
    textSurface = font.render(text, True, bg)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
      #  pygame.draw.rect(DISPLAYSURF, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(DISPLAYSURF, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    DISPLAYSURF.blit(textSurf, textRect)


gs=False


while not gs:
			DISPLAYSURF.fill(white)
			txt('WELCOME TO SNAKE GAME',bg,0,100)
			text_screen('PRESS ENTER TO PLAY',red,100,150)
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RETURN:
						gs=True
			pygame.display.update()


def gameloop():

	
	rex=100
	rey=270
	size=20
	fps=20
	clock=pygame.time.Clock()
	velx=0
	vely=0
	score=0
	vel=3
	ge=False
	go=False
	
	
	while True:
		fx=random.randint(10,x//2)
		fy=random.randint(10,550)
		if fx>(100-60) and fx<(100+60) and fy>=100 and fy<=200:
			continue
		elif fx>(400-60) and fx<(400+60) and fy>=200 and fy<=300:
			continue
		elif fy>(100-60) and fy<(100+60) and fx>=100 and fy<=400:
			continue
		elif fy>(200-60) and fy<(200+60) and fx>=100 and fy<=400:
			continue
		elif fy>(300-60) and fy<(300+60) and fx>=100 and fy<=400:
			continue
		else: 
			break
	
	
	if os.path.exists('highscore.txt'):
		with open('highscore.txt','r') as f1:
			highscore=f1.read()
	else:
		with open('highscore.txt','w') as f1:
			f1.write(0)
	
	
	snk_list=[]
	snk_length=1
	def plot_snk(DISPLAYSURF,colour,snk_list,sizex,sizey):
		for x,y in snk_list:
			pygame.draw.rect(DISPLAYSURF,colour,(x,y,sizex,sizey))
	
	
	while not ge:	
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RIGHT or event.key==pygame.K_6:
							velx=vel
							vely=0
					if event.key==pygame.K_LEFT or event.key==pygame.K_4:
							velx=-vel
							vely=0
					if event.key==pygame.K_UP or event.key==pygame.K_8:
							vely=-vel
							velx=0
					if event.key==pygame.K_DOWN or event.key==pygame.K_2:
							vely=vel
							velx=0
					if event.key==pygame.K_SPACE:
							velx=0  
							vely=0	
			
			
			def right():
				velx=vel
				vely=0
			def left():
				velx=-vel
				vely=0
			def up():
				vely=-vel
				velx=0
			def down():
				vely=vel
				velx=0
				
			
			if abs(rex-fx)<=6 and abs(rey-fy)<=6:
				score+=10
				fx=random.randint(10,x/2)
				fy=random.randint(10,550)
				snk_length+=3
				vel+=1
			
			
			if rey>600:
				rey=0
			if rey<0:
				rey=600
			if rex>x:
				rex=0
			if rex<0:
				rex=x
			
			
			if rey>(300-30) and rey<(300+10) and rex>=100 and rex<=400:
				go=True
			if rey>(100-30) and rey<(100+10) and rex>=100 and rex<=400:
				go=True
			if rey>(200-30) and rey<(200+10) and rex>=100 and rex<=400:
				go=True
			if rex>(100-30) and rex<(100+10) and rey>=100 and rey<=200:
				go=True
			if rex>(400-30) and rex<(400+10) and rey>=200 and rey<=300:
				go=True
			
			
			rex=rex+velx
			rey=rey+vely
			
			
			DISPLAYSURF.fill(bg)
			
			
			pygame.draw.rect(DISPLAYSURF,red,(fx,fy,size,size))
			
			
			plot_snk(DISPLAYSURF,white,snk_list,size,size)
			
			
			pygame.draw.line(DISPLAYSURF,white,(0,600),(540,600),20)	
			pygame.draw.line(DISPLAYSURF,white,(0,0),(0,600),20)
			pygame.draw.line(DISPLAYSURF,white,(0,0),(540,0),20)
			pygame.draw.line(DISPLAYSURF,white,(540,0),(540,600),20)	
			pygame.draw.line(DISPLAYSURF,BLUE,(100,100),(400,100),20)		
			pygame.draw.line(DISPLAYSURF,BLUE,(100,200),(400,200),20)
			pygame.draw.line(DISPLAYSURF,BLUE,(100,300),(400,300),20)		
			pygame.draw.line(DISPLAYSURF,BLUE,(100,100),(100,200),20)
			pygame.draw.line(DISPLAYSURF,BLUE,(400,200),(400,300),20)
			
			
			text_screen("SCORE:"+str(score),red,50,50)
			text_screen("HIGH SCORE:"+str(highscore),red,50,25)
			
			
			if go==True:
				if score> int(highscore):
						highscore=score		
				with open('highscore.txt','w') as f2:
					f2.write(str(highscore))
				DISPLAYSURF.fill(white)
				txt("game over",red,120,350)
				text_screen("SCORE:"+str(score)+'   HIGH SCORE:'+str(highscore),red,80,400)
				text_screen('PRESS ENTER TO QUIT',red,145,450)
				for event in pygame.event.get():
					if event.type==pygame.KEYDOWN:
						if event.key==pygame.K_RETURN:
							ge=True
						if event.key==pygame.K_SPACE:
							gameloop()
			
			
			head=[]
			head.append(rex)
			head.append(rey)
			snk_list.append(head)
			
			
			if len(snk_list)>snk_length:
				del snk_list[0]
			if head in snk_list[:-1]:
				go=True
						
			pygame.display.update()	
			clock.tick(fps)


gameloop()

		
			