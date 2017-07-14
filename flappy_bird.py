import pygame
import random
import time



pygame.init() 
display_width = 600
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Fleppy")
clock = pygame.time.Clock()
sky = pygame.image.load("sky.jpg")
ground = pygame.image.load("ground.jpg")
bird = pygame.image.load("bird.png").convert_alpha()
pipe = pygame.image.load("pipe.png").convert_alpha()
pipe2 = pygame.image.load("pipe2.png").convert_alpha()
bird = pygame.transform.scale(bird,(20,20))
svs = pygame.image.load("svs.png")
music = pygame.mixer.music.load("music.mp3")
life = 3		
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (135,206,250)
def draw_pipes(pipe_posx,pipe_1_posy,pipe_2_posy):
	#pygame.draw.rect(gameDisplay,green,(pipe_posx,pipe_1_posy,pipe_width,pipe_1_height))
	gameDisplay.blit(pipe,(pipe_posx,pipe_1_posy))
	gameDisplay.blit(pipe2,(pipe_posx,pipe_2_posy))
	
def draw_player(x,y):
	gameDisplay.blit(bird,(x,y))
		
def highscore(count):
	font = pygame.font.SysFont(None,40)
	text = font.render("Score : "+str(count),True,black)
	gameDisplay.blit(text,(0,0))	
	
def message_display(text,size,x,y,color):
	font = pygame.font.Font("freesansbold.ttf",size)
	text = font.render(text,True,color)
	text_rect = text.get_rect()
	text_rect.center =(x,y)
	gameDisplay.blit(text,text_rect)

def takra_gya(count):
	pygame.mixer.music.stop()
	time.sleep(1)
	crash(count)
	
def crash(count):
	pygame.draw.rect(gameDisplay,white,(0,400,600,200))
	message_display("Try Again",80,display_width/2,450,blue)
	message_display("Score : "+str(count),40,display_width/2,550,blue)
	message_display("Game Starts in 3 sec",20,100,525,red)
	pygame.display.update()
	time.sleep(2)

def intro():
	#pygame.mixr.Sound.play(start_music)
	intro = True
	menu1_x = 100
	menu1_y = 400
	menu2_x = 400
	menu2_y = 400
	menu_width = 100
	menu_height = 50
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		#pygame.display.set_icon(bird)
		
		pygame.draw.rect(gameDisplay,black,(200,400,100,50))
		pygame.draw.rect(gameDisplay,black,(500,400,100,50))
			
		gameDisplay.fill(white)
		message_display("Flappy Bird",100,display_width/2,display_height/2,blue)
		gameDisplay.blit(svs,((display_width/2)-100,10))	
		pygame.draw.rect(gameDisplay,green,(menu1_x,menu1_y,menu_width,menu_height))
		pygame.draw.rect(gameDisplay,red,(menu2_x,menu1_y,menu_width,menu_height))
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
		
		if menu1_x < mouse[0] < menu1_x+menu_width and menu1_y < mouse[1] < menu1_y+menu_height:
			pygame.draw.rect(gameDisplay,blue,(menu1_x,menu1_y,menu_width,menu_height))
			if click[0] == 1:
				intro = False
		if menu2_x < mouse[0] < menu2_x+menu_width and menu2_y < mouse[1] < menu2_y+menu_height:
			pygame.draw.rect(gameDisplay,blue,(menu2_x,menu1_y,menu_width,menu_height))
			if click[0] == 1:
				pygame.quit()
				quit()
	
		message_display("Go",40,menu1_x+menu_width/2,menu1_y+menu_height/2,black)
		message_display("Exit",40,menu2_x+menu_width/2,menu2_y+menu_height/2,black)
		
		pygame.display.update()
		clock.tick(50)
	
def gameloop():
	
	gameover = False
	pipe_width = 100
	pipe_height = 500
	pipe_posx = 600
	pipe_1_posy = random.randrange(-500,-100)
	pipe_2_posy = pipe_1_posy+500+100
	speed = 10
	player_width = 20
	player_height = 20
	player_posx = 100
	player_posy = 100
	player_pos_change = 50
	count = 0
	ground_x = 0
	ground_y = 500
	pygame.mixer.music.play(-1)
	
	while not gameover:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					player_posy -= player_pos_change
					
				if event.key == pygame.K_DOWN:
					player_posy += player_pos_change
					
			#if event.type == pygame.KEYUP:
			#	if event.key == pygame.K_UP:
			#		print()
			#	if event.key == pygame.K_UP:
			#		print()
			
		if(pipe_posx+pipe_width <= 0):
			
			pipe_posx = 600
			pipe_1_posy = random.randrange(-500,-100)
			pipe_2_posy = pipe_1_posy+500+100
			count+=1
			ground_x = 0
			
			
		gameDisplay.fill(black)
		gameDisplay.blit(sky,(0,0))
		draw_player(player_posx,player_posy)
		
		draw_pipes(pipe_posx,pipe_1_posy,pipe_2_posy)
		gameDisplay.blit(ground,(ground_x,ground_y))
		highscore(count)
		
		pygame.display.update()
		clock.tick(30)
		if(player_posx+player_width >= pipe_posx and player_posx <= pipe_posx+pipe_width and player_posy <= pipe_1_posy+pipe_height ):
			takra_gya(count)
			gameover = True
		if(player_posx+player_width >= pipe_posx and player_posx <= pipe_posx+pipe_width and player_posy+player_height >= pipe_2_posy):
			takra_gya(count)
			gameover = True
		if(player_posy+player_height >= 500):
			takra_gya(count)
			gameover = True
			
		ground_x -= speed
		pipe_posx -= speed 
		player_posy += 5

		
		
intro()
life = 1
while life <= 3:
	gameloop()
	life += 1
#this is not yet completed there are many changes required to improve this game
#By_Sumit_Patidar
