import pygame 
from pygame.locals import *

pygame.init()

#game window 
screen_width = 600
screen_height = 600

#create game window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Snake')

#cell size in pixels for snake
cell_size = 10

#creating the snake, x and y coordinates
snake_pos = [[int(screen_width/2),int(screen_height/2)]]
#adding segments to the snake
snake_pos.append([300,310])
snake_pos.append([300,320])
snake_pos.append([300,330])

#define a background image or color
bg = (46,198,209)

#snake body color
body_inner = (50,175,25)
body_outer = (100,100,100)
head_color = (255,0,0) #red

def draw_screen():
    screen.fill(bg)

#start game loop
run = True
while run:
    #set background color in game
    draw_screen()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #drawing snake
    head=1
    for x in snake_pos: 
        if head == 0:
            pygame.draw.rect(screen,body_outer,(x[0],x[1],cell_size,cell_size))
            pygame.draw.rect(screen,body_inner,(x[0]+1,x[1]+1,cell_size -2,cell_size -2))  
        if head == 1:
            pygame.draw.rect(screen,body_outer,(x[0],x[1],cell_size,cell_size))
            pygame.draw.rect(screen,head_color,(x[0]+1,x[1]+1,cell_size -2,cell_size -2))  
            head = 0

    pygame.display.update()

#end game 
pygame.quit()