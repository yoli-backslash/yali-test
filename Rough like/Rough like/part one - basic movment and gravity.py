#must have---------------------------------------
import pygame #import
import time
import random
import math
import sys
pygame.init() #starts pygame

green=(0,255,0)
white = (255,255,255)
purple=(100,20,200)
brown=(200,100,0)
black = (0,0,0)
blue=(0,0,255)
red=(255,0,0)
(width, height) = (1000, 600)
wn = pygame.display.set_mode((width, height))
pygame.display.set_caption('testing')
wn.fill(white)
clock = pygame.time.Clock()
#idle=pygame.image.load('idle.gif') #image, has to be in the same file as the game

walking0=pygame.image.load('walking0.png')
walking1=pygame.image.load('walking1.png')
walking2=pygame.image.load('walking2.png')
walking3=pygame.image.load('walking3.png')
walking4=pygame.image.load('walking4.png')
walking5=pygame.image.load('walking5.png')
walking6=pygame.image.load('walking6.png')

idle0=pygame.image.load('idle0.png')
idle1=pygame.image.load('idle1.png')
idle2=pygame.image.load('idle2.png')

R2=pygame.image.load('R2.png')
jump=pygame.image.load('jump.png')
idle=pygame.image.load('idle.png')
R1=pygame.image.load('R1.png')

attack0=pygame.image.load('attack0.png')
attack1=pygame.image.load('attack1.png')
attack2=pygame.image.load('attack2.png')

roll0=pygame.image.load('roll0.png')
roll1=pygame.image.load('roll1.png')
roll2=pygame.image.load('roll2.png')
roll3=pygame.image.load('roll3.png')


idle = pygame.transform.scale(idle, (100, 100))
idle = pygame.transform.scale(idle, (100, 100))
R1 = pygame.transform.scale(R1, (100, 100))

Rattack0 = pygame.transform.scale(attack0, (180, 130))
Rattack1 = pygame.transform.scale(attack1, (180, 130))
Rattack2 = pygame.transform.scale(attack2, (180, 130))

Lattack0 = pygame.transform.flip(Rattack0, True,False)
Lattack1 = pygame.transform.flip(Rattack1, True,False)
Lattack2 = pygame.transform.flip(Rattack2, True,False)

Rroll0 = pygame.transform.scale(roll0, (180, 130))
Rroll1 = pygame.transform.scale(roll1, (180, 130))
Rroll2 = pygame.transform.scale(roll2, (180, 130))
Rroll3 = pygame.transform.scale(roll3, (180, 130))

Lroll0 = pygame.transform.flip(Rroll0,True,False)
Lroll1 = pygame.transform.flip(Rroll1,True,False)
Lroll2 = pygame.transform.flip(Rroll2,True,False)
Lroll3 = pygame.transform.flip(Rroll3,True,False)




walking0 = pygame.transform.scale(walking0, (180, 150))
walking1 = pygame.transform.scale(walking1, (180, 150))
walking2 = pygame.transform.scale(walking2, (180, 150))
walking3 = pygame.transform.scale(walking3, (180, 150))
walking4 = pygame.transform.scale(walking4, (180, 150))
walking5 = pygame.transform.scale(walking5, (180, 150))
walking6 = pygame.transform.scale(walking6, (180, 150))
idle0 = pygame.transform.scale(idle0, (180, 150))
idle1 = pygame.transform.scale(idle1, (180, 150))
idle2 = pygame.transform.scale(idle2, (180, 150))
img=idle1
R2 = pygame.transform.scale(R2, (100, 100))
jump = pygame.transform.scale(jump, (100, 100))
char=[]

#Functions-------------------------------------------------------------------------------------------------------------
def text_objects(text, font):
    textSurface = font.render(text, True, black) #rendering the text (the text it self,is it rendered?,color)
    return textSurface, textSurface.get_rect() #gives the value of the text surface and location

def crash():
    message_display('You Crashed')
    x=(w*0.5)
class ent:
    def __init__(self, position, size):
        self.x, self.y = position
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.speed=0.01
        self.angle=8
        self.gravity=1
        self.q=1
        self.dy=math.cos(self.angle) * self.speed
        self.dx=math.sin(self.angle) * self.speed
        
    def display(self):
        wn.blit(img,(self.x,self.y)) #displays

    def move(self):
        self.x+=self.dx
        self.y-=self.dy
        self.dy-=0.08
       
        
    def floor(self):
        if self.y>480:
            self.dy=0
            self.y=480
            








#Lists=--------------------------------------------

size = 8
main = ent((100, 480), size)
main.q=0
main.i=0
main.a=0
main.aa=0
main.left=0
main.right=1
main.colour=(purple)
main.speed=0
main.angle=0
main.dy=0
main.dx=0
char.append(main)






    
#Main game-----------------------------------------------
def game():
    
    global img
    attack=False
    crashed=False
    while not crashed:
        for event in pygame.event.get(): #get keypress
            if event.type == pygame.quit:
                crashed = True #breakes the loop
            for man in char:
                if event.type==pygame.KEYDOWN:#if key is pressed
                    if event.key ==pygame.K_a:#left arrow
                        man.dx=-5
                        man.left=1
                        man.right=0
                        img = pygame.transform.flip(img, True,False)
                    elif event.key==pygame.K_d:
                        man.dx=5
                        man.left=0
                        man.right=1
                    if event.key==pygame.K_w and man.y>460:
                        man.dy=5
                        img=jump
                    if event.key==pygame.K_k:
                        man.aa=1
                if event.type==pygame.KEYUP:#if key is unpressed
                    if event.key == pygame.K_d or event.key == pygame.K_a:
                        man.dx=0
                    if event.key==pygame.K_k:
                        man.aa=0
                    #if event.key == pygame.K_UP:
                
                        
                







        wn.fill(white)#fills screen with color

        for man in char:                
            man.move()
            man.floor()
            if man.aa==0:
                if man.dx==0:
                    man.i+=1
                    if man.i==10:
                        img=idle1
                    if man.i==20:
                        img=idle0
                    if man.i==30:
                        img=idle1
                    if man.i==40:
                        img=idle2
                        man.i=0

                if man.q > 42:
                    man.q=1
                if man.dx == -5 and man.y>460:
                    man.q+=1
                    if man.q==6:
                        img=walking0
                        img = pygame.transform.flip(img, True,False)
                    if man.q==12:
                        img=walking1
                        img = pygame.transform.flip(img, True,False)
                    if man.q==18:
                        img=walking2
                        img = pygame.transform.flip(img, True,False)
                    if man.q==24:
                        img=walking3
                        img = pygame.transform.flip(img, True,False)
                    if man.q==30:
                        img=walking4
                        img = pygame.transform.flip(img, True,False)
                    if man.q==36:
                        img=walking5
                        img = pygame.transform.flip(img, True,False)
                    if man.q==42:
                        img=walking6
                        img = pygame.transform.flip(img, True,False)
                        man.q = 0
                    

                if man.dx == 5 and man.y>460:
                    man.q+=1
                    if man.q==6:
                        img=walking0
                    if man.q==12:
                        img=walking1
                    if man.q==18:
                        img=walking2
                    if man.q==24:
                        img=walking3
                    if man.q==30:
                        img=walking4
                    if man.q==36:
                        img=walking5
                    if man.q==42:
                        img=walking6
                        man.q = 0

            if man.aa==1:
                man.a+=1
                if man.a==0:
                    if man.right==1:
                        img=Rattack0
                    elif man.left==1:
                        img=Lattack0
                if man.a==7:
                    if man.right==1:
                        img=Rattack1
                    elif man.left==1:
                        img=Lattack1
                if man.a==14:
                    if man.right==1:
                        img=Rattack2
                    elif man.left==1:
                        img=Lattack2
                    man.a=-7
                    
            pygame.draw.line(wn,green,(0,600),(1000,600),20)
            wn.blit(img,(man.x,man.y)) #displays



        pygame.display.update() #update something
        clock.tick(60) #fps
      


#End-----------------------------------------------------------------------------------
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115) #font and size
    TextSurf, TextRect = text_objects(text, largeText) #text surfce and location idk
    TextRect.center = ((w/2),(w/2)) #center of text location
    wn.blit(TextSurf, TextRect) #display the text in the location in the font

    pygame.display.update()

    time.sleep(2)


game()
pygame.quit()
quit()
