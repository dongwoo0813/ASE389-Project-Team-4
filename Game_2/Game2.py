
import pygame
import sys

import numpy as np
import random

SCREEN_WIDTH = 500*2
SCREEN_HEIGHT = 800


# COLORS
white = (255, 255, 255)
black = (0, 0, 0)
lightblue = (0, 0, 255)
red = (200, 0, 0 )
shadow = (192, 192, 192)
lightred= (255, 100, 100)
purple = (102, 0, 102)
lightpurple= (153, 0, 153)
lightgreen = (0, 255, 0 )
green = (0, 200, 0 )
blue = (0, 0, 128)


num_box = 6

# DIMENSION OF ROBOT
robot_width = 70
robot_height = 70

# DIMENSION OF BOX
box_width = 80
box_height = 80

# Location of Boxes
box_x = (160,280,100,260,100,250)
box_y = (60,160,300,400,520,600)

# WIDTH AND HEIGHT OF WALL
wall_width = 50
wall_height = SCREEN_HEIGHT

# SIZE OF FONT
font_size = 80

pygame.init()
pygame.display.set_caption("Game 2")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pos_x = (SCREEN_WIDTH-robot_width)/2;
pos_y = SCREEN_HEIGHT - robot_height;

clock = pygame.time.Clock()
while True:


    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pos_x -= 1*1

    if key_event[pygame.K_RIGHT]:
        pos_x += 1*1

    if key_event[pygame.K_UP]:
        pos_y -= 1*1

    if key_event[pygame.K_DOWN]:
        pos_y += 1*1


    if (pos_x < wall_width or pos_x > SCREEN_WIDTH - wall_width - robot_width):
        sys.exit()
    elif (pos_y < 0):
        sys.exit()

    screen.fill(white)
    # background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))



    BOX1 = (box_x[0], box_y[0], box_width, box_height)
    pygame.draw.rect(screen, lightblue, BOX1)   

    BOX2 = (box_x[1], box_y[1], box_width, box_height)
    pygame.draw.rect(screen, lightred, BOX2)

    BOX3 = (box_x[2], box_y[2], box_width, box_height)
    pygame.draw.rect(screen, lightblue, BOX3)

    BOX4 = (box_x[3], box_y[3], box_width, box_height)
    pygame.draw.rect(screen, lightred, BOX4)

    BOX5 = (box_x[4], box_y[4], box_width, box_height)
    pygame.draw.rect(screen, lightred, BOX5)

    BOX6 = (box_x[5], box_y[5], box_width, box_height)
    pygame.draw.rect(screen, lightblue, BOX6)


    font1 = pygame.font.SysFont('+5', font_size)
    img1 = font1.render('+5', True, black)
    screen.blit(img1,((box_x[0]+(box_width-font_size+10)),(box_y[0]+box_height/4)))

    font2 = pygame.font.SysFont('-5', font_size)
    img2 = font2.render('-5', True, black)
    screen.blit(img2,((box_x[1]+(box_width-font_size+10)),(box_y[1]+box_height/4)))

    font3 = pygame.font.SysFont('+5', font_size)
    img3 = font3.render('+5', True, black)
    screen.blit(img3,((box_x[2]+(box_width-font_size+10)),(box_y[2]+box_height/4)))

    font4 = pygame.font.SysFont('-5', font_size)
    img4 = font4.render('-5', True, black)
    screen.blit(img4,((box_x[3]+(box_width-font_size+10)),(box_y[3]+box_height/4)))

    font5 = pygame.font.SysFont('-5', font_size)
    img5 = font5.render('-5', True, black)
    screen.blit(img5,((box_x[4]+(box_width-font_size+10)),(box_y[4]+box_height/4)))

    font6 = pygame.font.SysFont('+5', font_size)
    img6 = font6.render('+5', True, black)
    screen.blit(img6,((box_x[5]+(box_width-font_size+10)),(box_y[5]+box_height/4)))

    WALL1 = (0, 0, wall_width, wall_height)
    pygame.draw.rect(screen, shadow, WALL1)

    WALL2 = (SCREEN_WIDTH-wall_width, 0, wall_width, wall_height)
    pygame.draw.rect(screen, shadow, WALL2)

    # image3 = pygame.image.load('-5.png')
    # display = pygame.display.set_mode((20,20))
    # pygame.Surface.blit(screen,image3, (20, 20))


    ## Robot
    robot = (pos_x, pos_y, robot_width, robot_height)
    pygame.draw.rect(screen, black, robot)

    robot_body = (pos_x+ robot_width/5,pos_y +robot_height/8, robot_width*0.6, robot_height*0.6)
    pygame.draw.rect(screen, shadow, robot_body)
    pygame.display.update()

# def trustworthy():
#     # 0 = Trustworthy
#     # 1 = Untrustworthy
#     # 2 = Half-Half Trustworthy
#     trustworthiness = random.randint(0,2)
#     return trustworthiness


def assign(num_box):
    # Assigns -5 and 5 to the obstacle
    # -5 for obstacle
    # 5 for clear way

    num = 0
    Box = np.zeros(num_box)
    while (num < 5):
        Box[num] = random.randint(0,1)
        if Box[num] == 0:
            Box[num] = -1
        num += num
    Box = Box*5
    return Box


def pos_box(self):

    return 0


