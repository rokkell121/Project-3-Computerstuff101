
#importing the pygame package

import pygame
import sys
import time
import random
from pygame.locals import *
import pygame.mixer

#Initializing it
pygame.init()

#bliting the colours  
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
green = (  0, 255,   0)

#Size of the screen, title, importing sound and loading images 
setDisplay = pygame.display.set_mode((1181,981))
title = pygame.display.set_caption("Treasure Hunt")
sound = pygame.mixer.Sound('song.wav') 
bg = pygame.image.load("map.gif")
img = pygame.image.load('pirate.gif')
img1 = pygame.image.load('pirate1.gif')
treasure = pygame.image.load('treasure.gif')

#Movement and Position of the robot 
FPS = 30
imgx = 7
imgy = 519
img1x=1160
img1y=160
pixMove = 5
offset = 30  
movement = 'right'
movement1 = 'left'

#Traffic Light
light = 'red'
light = 'green'
light1 = 'red'
light1 = 'green'
 
fpsTime = pygame.time.Clock()

#Defining score and loading the font on the screen
def texts(score):
   font=pygame.font.SysFont(None,30)
   scoretext=font.render("Score:"+str(score), 1,(255,255,255))
   screen.blit(scoretext, (900, 500))
   
#Treasure class which loads the image and sets the position
class Treasure:

    def __init__(self,x,y):
        self.x=900
        self.y=500
        self.treasure=pygame.image.load('treasure.gif')

    def rendertreasure(self):
        window.blit(self.treasure, (self.x,self.y))
    
 
#Class of TwoRobots and defining the image and movement for the robot
class TwoRobots:
 
     def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pirate.gif')
        self.image = pygame.image.load('pirate1.gif')
        self.rect = self.image.get_rect()
 

    def checking_right(imgx,imgy,movement):
        if bg.get_at((imgx + offset,imgy)).g is not  0:
            if bg.get_at((imgx,imgy - offset)).g is  0:
                movement = 'up'
            elif bg.get_at((imgx,imgy + offset)).g is  0:
                movement = 'down'
        return movement 

    def checking_left(imgx,imgy,movement):
        if bg.get_at((imgx - offset,imgy)).g is not  0:
                if bg.get_at((imgx ,imgy + 10)).g is  0:
                    movement = 'down'
                elif bg.get_at((imgx,imgy - offset )).g is  0:
                    movement = 'up'
        return movement 

    def checking_down(imgx,imgy,movement):
        if bg.get_at((imgx,imgy + offset)).g is not  0:
                if bg.get_at((imgx + offset,imgy)).g is  0:
                    movement = 'right'
                elif bg.get_at((imgx - offset,imgy )).g is  0:
                    movement = 'left'
        if imgx > 500 and imgy > 770:
            time.sleep(10)
        return movement

    def checking_up(imgx,imgy,movement):
        if bg.get_at((imgx,imgy - offset)).g is not  0:
                if bg.get_at((imgx - offset,imgy )).g is  0:
                    movement = 'left'
                elif bg.get_at((imgx + offset,imgy )).g is  0:
                    movement = 'right'
        return movement



    def checking_right1(img1x,img1y,movement1):
        if bg.get_at((img1x + offset,img1y)).g is not  0:
            if bg.get_at((img1x,img1y + offset)).g is  0:
                movement1 = 'down'
            elif bg.get_at((img1x,img1y - offset)).g is  0:
                movement1 = 'up'
        return movement1 

    def checking_left1(img1x,img1y,movement1):
        if bg.get_at((img1x - offset,img1y)).g is not  0:
                if bg.get_at((img1x ,img1y + 100)).g is  0:
                    movement1 = 'down'
                elif bg.get_at((img1x,img1y - offset )).g is  0:
                    movement1 = 'up'
        return movement1

    def checking_down1(img1x,img1y,movement1):
        if bg.get_at((img1x,img1y + offset)).g is not  0:
                if bg.get_at((img1x + offset,img1y)).g is  0:
                    movement1 = 'right'
                elif bg.get_at((img1x - offset,img1y )).g is  0:
                    movement1 = 'left'
        return movement1

    def checking_up1(img1x,img1y,movement1):
        if bg.get_at((img1x,img1y - offset)).g is not  0:
                if bg.get_at((img1x - offset,img1y )).g is  0:
                    movement1 = 'left'
                elif bg.get_at((img1x + offset,img1y )).g is  0:
                    movement1 = 'right'
        return movement1
    def checking_treasure(imgx,imgy):
        if imgx>975 and imgy==519:
            setDisplay.blit(treasure, (0,0))
            
     def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pirate.gif')
        self.image = pygame.image.load('pirate1.gif')
        self.rect = self.image.get_rect()
 

    def checking_right(imgx,imgy,movement):
        if bg.get_at((imgx + offset,imgy)).g is not  0:
            if bg.get_at((imgx,imgy - offset)).g is  0:
                movement = 'up'
            elif bg.get_at((imgx,imgy + offset)).g is  0:
                movement = 'down'
        return movement 

    def checking_left(imgx,imgy,movement):
        if bg.get_at((imgx - offset,imgy)).g is not  0:
                if bg.get_at((imgx ,imgy + 10)).g is  0:
                    movement = 'down'
                elif bg.get_at((imgx,imgy - offset )).g is  0:
                    movement = 'up'
        return movement 

    def checking_down(imgx,imgy,movement):
        if bg.get_at((imgx,imgy + offset)).g is not  0:
                if bg.get_at((imgx + offset,imgy)).g is  0:
                    movement = 'right'
                elif bg.get_at((imgx - offset,imgy )).g is  0:
                    movement = 'left'
        if imgx > 500 and imgy > 770:
            time.sleep(10)
        return movement

    def checking_up(imgx,imgy,movement):
        if bg.get_at((imgx,imgy - offset)).g is not  0:
                if bg.get_at((imgx - offset,imgy )).g is  0:
                    movement = 'left'
                elif bg.get_at((imgx + offset,imgy )).g is  0:
                    movement = 'right'
        return movement

    while True:
            sound.play()
            

            if movement1 == 'left':
                img1x -= pixMove
                checking_treasure(img1x,img1y)
                movement1 = checking_left1(img1x,img1y,movement1)

                
            elif movement1 == 'down':
                img1y += pixMove
                checking_treasure(img1x,img1y)
                movement1 = checking_down1(img1x,img1y,movement1)

            elif movement1 == 'right':
                img1x += pixMove
                checking_treasure(img1x,img1y)
                movement1 = checking_right1(img1x,img1y,movement1)
                


            elif movement1 == 'up':
                img1y -= pixMove
                checking_treasure(img1x,img1y)
                movement1 = checking_up1(img1x,img1y,movement1)  
            
       

           
            
                
            setDisplay.fill(black)


#Random Traffic light stopping
            if random.randint(0,2000) < 30:
                #draws the red circle 
                pygame.draw.circle(setDisplay, red, [589, 878], 50)
                light1 = 'red'
                #if the light is red then movement of the robot is 0
                pixMove = 0
            if random.randint(0,2000) < 30:
                pygame.draw.circle(setDisplay, yellow, [589, 878], 50)
                light1 = 'yellow'
                #if the light is yellow it moves by 1
                pixMove = 1
            if random.randint(0,2000) < 60:
                pygame.draw.circle(setDisplay, green, [589, 878], 50)
                light1 = 'green'
                #if the light is green and it moves by 5 which is the normal speed set
                pixMove = 5

            if light1 != "red": 


                if movement == 'right':
                    imgx += pixMove
                    checking_treasure(imgx,imgy)
                    movement = checking_right(imgx,imgy,movement)
                
                elif movement == 'left':
                    imgx -= pixMove
                    checking_treasure(imgx,imgy)
                    movement = checking_left(imgx,imgy,movement)

                
                elif movement == 'down':
                    imgy += pixMove
                    checking_treasure(imgx,imgy)
                    movement = checking_down(imgx,imgy,movement)
           


                elif movement == 'up':
                    imgy -= pixMove
                    checking_treasure(imgx,imgy)
                    movement = checking_up(imgx,imgy,movement) 
      


                if random.randint(0,2000) < 30: 
                    pygame.draw.circle(setDisplay, red, [300, 878], 50) 
                    light = 'red' 
                    pixMove = 0 
                if random.randint(0,2000) < 30: 
                    pygame.draw.circle(setDisplay, yellow, [300, 878], 50) 
                    light1 = 'yellow' 
                    pixMove = 1 
                if random.randint(0,2000) < 60: 
                    pygame.draw.circle(setDisplay, green, [300, 878], 50) 
                    light = 'green' 
                    pixMove = 5 

                if light != "red": 


                  
#This blits the Pirate image on the screen. 

                    setDisplay.blit(img, (imgx,imgy))
                    for event in pygame.event.get():
                        print event
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit() 
        

#Set of images bliting on the screen     
            setDisplay.blit(bg, (0,0))
            setDisplay.blit(img, (imgx,imgy))
            setDisplay.blit(treasure, (982,518))
            setDisplay.blit(treasure, (258,178))
            setDisplay.blit(treasure, (728,483))
            setDisplay.blit(treasure, (692,220))
            setDisplay.blit(img1, (img1x,img1y))
            pygame.display.flip()
     
     
         
            pygame.display.update()
            fpsTime.tick(FPS)
     
 
pygame.display.update()
