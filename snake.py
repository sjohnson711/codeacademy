import pygame, sys, time, random

speed = 15

#windows sizes

frame_size_x = 720
frame_size_y = 480



check_errors = pygame.init()

if(check_errors[1] > 0):
    print("Error "+ check_errors[1])
else:
    print("Game Successfully initialized")


#intialise game windows


pygame.display.set_caption("Snake Game")
game_window = pygmae.display.set_mode(frame_size_x, frame_size_y)

# colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)


fps_controller = pygame.time.Clock()
# one snake square size
square_size = 20 

def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, direction
    direction = "RIGHT"
    head_pos = [120,60]
    snake_body = [[120,60]]
    food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size, 
                random.randrange(1, (frame_size_y // square_size)) * square_size]

    food_spawn = True
    score = 0

init_vars()
# pause at 5:29 ASMR Programming - Coding a Snake Game - No talking
def show_score():







