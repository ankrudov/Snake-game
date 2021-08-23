import pygame 
import sys
from pygame.locals import *
import random

pygame.init()

#game window 
screen_width = 600
screen_height = 600

#create game window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Snake')
my_font = pygame.font.SysFont('monospace', 12, bold=False, italic=False)

#gamevariables
#cell size in pixels for snake
cell_size = 10
#directions 1 is up, 2 is right, 3 is down, 4 is left
direction = 1
update_snake = 0
food = [0,0]
new_food = True
new_piece = [0,0]
score = 0


#creating the snake, x and y coordinates
snake_pos = [[int(screen_width/2),int(screen_height/2)]]
#adding segments to the snake
snake_pos.append([300,310])
snake_pos.append([300,320])
snake_pos.append([300,330])

#define a background image, color or text
bg = (46,198,209)
food_color = (252,186,3)
#snake body color
body_inner = (50,175,25)
body_outer = (100,100,100)
head_color = (255,0,0) #red
score_color = (51,153,255)
font = pygame.font.SysFont(None, 40, bold=False, italic=False)


#functions
def draw_screen():
    screen.fill(bg)

def draw_score():
    score_txt = 'Score: ' + str(score)
    score_img = font.render(score_txt,True,score_color)
    screen.blit(score_img,(250,0))
  
def game_over():
    #snake has eaten itself
    snake_head = 0
    for segment in snake_pos and snake_head > 0:
        if snake_pos[0] == segment:
            game_over = True
        snake_head +=1
    #snake has hit sides
    if snake_pos[0][0] <0 or snake_pos[0][0] > screen_width or snake_pos[0][1] < 0 or snake_pos[0][1] > screen_height:
        game_over = True 

#start game loop
run = True
while run:
    #set background color in game
    draw_screen()
    draw_score()
    game_over()
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1 
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            if event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                direction = 4  

    #generate food 
    if new_food == True:
        new_food = False
        food[0] = cell_size * random.randint(0,(screen_width/cell_size) -2)
        food[1] = cell_size * random.randint(0,(screen_height/cell_size) -2)

    #drawfood
    pygame.draw.rect(screen,food_color,(food[0],food[1],cell_size,cell_size))

    #snake head and food collision
    if snake_pos[0] == food:
        new_food = True
        #new snake segment postioned at the end of snake
        new_piece = list(snake_pos[-1])
        if direction == 1:
            new_piece[1] += cell_size
        if direction == 3:
            new_piece[1]  -= cell_size
        if direction == 2:
            new_piece[0] -= cell_size
        if direction == 4:
            new_piece[0]  += cell_size
        snake_pos.append(new_piece)
        score +=1


    #snake movement
    if update_snake > 99:
        update_snake = 0
        snake_pos = snake_pos[-1:] + snake_pos[:-1]
        if direction == 1:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] - cell_size

        if direction == 3:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] + cell_size

        if direction == 2:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] + cell_size

        if direction == 4:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] - cell_size
    
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
    update_snake +=1

#end game 
pygame.quit()