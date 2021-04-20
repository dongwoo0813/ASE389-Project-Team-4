# -*- coding: utf-8 -*-
"""
Author: Edward Jung, Heeyong Huh, Jaehyun Park, Andrew Repetski

Our Original Work
"""
# import pygame module in this program
import pygame
import numpy as np
import time
import sys
import random
from database import database_selector

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
  
# define the RGB value
# for white colour
white = (255, 255, 255)
  
# assigning values to X and Y variable
X = 1300
Y = 750
  
# create the display surface object
# of specific dimension..e(X, Y).
display = pygame.display.set_mode((X, Y ))
  
# set the pygame window name
pygame.display.set_caption('Image')
rect = pygame.Rect((0, 0), (X, Y))

background_color = (192, 192, 192)
display.fill(background_color, rect)  # Clear the screen.

res = (720,720)

color_dark = (100,100,100)

height = display.get_height()
width = display.get_width()

Population = 0;
Accuracy = 0;
Sensitivity = 0;    
Specificity = 0;
Correct = 0;

TP = 0;
TN = 0;     
FP = 0;
FN = 0;

## USE THIS LINE WHEN RUNNING TEST

rand_db, DB = database_selector()
print("Number of database used = ", rand_db)

## USE THIS LINE WHEN RUNNING TEST

## COMMENT THE LINE BELOW WHEN RUNNING TEST
## ONLY FOR DEBUGGING
# DB = np.zeros(8)
# DB[0:4:1] = 1
# DB[4:8:1] = 0
## COMMENT THE LINE ABOVE WHEN RUNNING TEST

# print("DB: ", DB)
(row, ) = DB.shape
print("row = ", row)

num = 0
Key = 2
# running = True

Response_Duration = 4 #Duration

while num < row:
    image3 = pygame.image.load(r'Blank-Page.JPG')
    display = pygame.display.set_mode((X,Y))
    display.blit(image3, [0, 0])
    pygame.display.update()
    pygame.time.delay(500)

    Loop_begin = pygame.time.get_ticks()
    # create a surface object, image is drawn on it.
    
    random_number = random.randint(0,1)
    # print("random number = ", random_number)
    if random_number == 0:
        image1 = pygame.image.load(r'Sensed-Obstacle.JPG')
        display = pygame.display.set_mode((X, Y ))
        display.blit(image1, [0, 0])
        pygame.display.update() 

    else:    
        image2 = pygame.image.load(r'Sensed-No-Obstacle.JPG')
        display = pygame.display.set_mode((X, Y ))
        display.blit(image2, [0, 0])
        pygame.display.update() 

    pygame.time.delay(1500)

    image3 = pygame.image.load(r'Blank-Page.JPG')
    display = pygame.display.set_mode((X,Y))
    display.blit(image3, [0, 0])
    pygame.display.update()
    pygame.time.delay(500)

    start_time = pygame.time.get_ticks()

    image = pygame.image.load(r'Trust-Buttons.JPG')
    display = pygame.display.set_mode((X,Y))
    display.blit(image, [0, 0])
    pygame.display.update()

    pygame.time.delay(2000)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("GAME ABORTED. EXITING.")
            pygame.quit()
            sys.exit()

        input_time = pygame.time.get_ticks()- start_time


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Key = 1
                remain_time = (Response_Duration*1000 - input_time)
                pygame.time.delay(remain_time)
                time1 = pygame.time.get_ticks()


            elif event.key == pygame.K_RIGHT:
                Key = 0
                remain_time = (Response_Duration*1000 - input_time)
                pygame.time.delay(remain_time)
                time1 = pygame.time.get_ticks()


    pygame.event.clear()

    image3 = pygame.image.load(r'Blank-Page.JPG')
    display = pygame.display.set_mode((X,Y))
    display.blit(image3, [0, 0])
    pygame.display.update()
    pygame.time.delay(500)


    if DB[num] == 1 and Key == 1:
        # create a surface object, image is drawn on it.
        image1 = pygame.image.load(r'Correct-No-Obstacle.JPG')
        display = pygame.display.set_mode((X, Y ))
        display.blit(image1, [0, 0])
        pygame.display.update()
        # print("TP = ", TP)
        if (num > 39):
            print("")
            TP += 1
            # print("Number when calculating = ", num)
            # print("TP = ", TP)
        print("Number = ", num)
        num += 1

        pygame.time.delay(1000)
        continue
    
    elif DB[num] == 0 and Key == 1:
        image1 = pygame.image.load(r'Incorrect-No-Obstacle.JPG')
        display = pygame.display.set_mode((X, Y ))
        display.blit(image1, [0, 0])
        pygame.display.update()
        if (num > 39):
            FP += 1
            # print("Number when calculating = ", num)
            # print("FP = ", FP)
        print("Number = ", num)
        num += 1
        
        pygame.time.delay(1000)
        continue


    if DB[num] == 1 and Key == 0:
        # create a surface object, image is drawn on it.
        image1 = pygame.image.load(r'Incorrect-Obstacle.JPG')
        display = pygame.display.set_mode((X, Y ))
        display.blit(image1, [0, 0])
        pygame.display.update()
        if (num > 39):
            FN += 1
            # print("Number when calculating = ", num)
            # print("FN = ", FN)
        print("Number = ", num)
        num += 1
        pygame.time.delay(1000)
        continue

    elif DB[num] == 0 and Key == 0:
        image1 = pygame.image.load(r'Correct-Obstacle.JPG')
        display = pygame.display.set_mode((X, Y ))
        display.blit(image1, [0, 0])
        pygame.display.update()
        if (num > 39):
            TN += 1
            # print("Number when calculating = ", num)
            # print("TN = ", TN)
        print("Number = ", num)
        num += 1
        pygame.time.delay(1000)
        continue
    Key = 2


    Loop_end = pygame.time.get_ticks()
    print("Duration per loop = ", Loop_end - Loop_begin)

Population = num
Correct = TP + TN
Accuracy = Correct/Population;
Sensitivity = TP/(TP + FN);
Specificity = TN/(TN + FP);
print("The game is over")
print("TP = ", TP)
print("FP = ", FP)
print("FN = ", FN)
print("TN = ", TN)
print("Accuracy = ", Accuracy)
print("Sensitivity = ", Sensitivity)
print("Specificity = ", Specificity)

pygame.quit()
sys.exit()

