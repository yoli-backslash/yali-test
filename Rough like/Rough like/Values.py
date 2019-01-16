#must have---------------------------------------
import pygame #import
import time
import random
import math
import sys
from png import *
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
img=idle1
#idle=pygame.image.load('idle.gif') #image, has to be in the same file as the game
arrows=[]
proj=[]
char=[]

#Functions-------------------------------------------------------------------------------------------------------------
def text_objects(text, font):
    textSurface = font.render(text, True, black) #rendering the text (the text it self,is it rendered?,color)
    return textSurface, textSurface.get_rect() #gives the value of the text surface and location
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115) #font and size
    TextSurf, TextRect = text_objects(text, largeText) #text surfce and location idk
    TextRect.center = ((w/2),(w/2)) #center of text location
    wn.blit(TextSurf, TextRect) #display the text in the location in the font

    pygame.display.update()

    time.sleep(2)
def dist(lol,self):
        self.dis=math.hypot(lol.x-self.x, lol.y-self.y)
        
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
        if self.y>230 and self.y<240 and man.x>140 and man.x<740:
            self.y=231
            self.dy=0
        if self.y>480:
            self.dy=0
            self.y=480
            








#Lists=--------------------------------------------
char2=[]

boi=ent((600,480) , 8)
boi.dx=0
boi.dy=0
boi.q=0
boi.hp=40
boi.img=Reb0
boi.a=-1
boi.right=1
boi.left=0
char2.append(boi)

size = 8
man = ent((100, 480), size)
man.q=0
man.i=0
man.a=0
man.r=5
man.j=0
man.w=1
man.hp=80
man.hit=False
man.h=0


man.quick=0
man.arrow=0
man.ar=0

man.rr=0
man.ll=0
man.fx=0
man.fy=0

man.jump=0
man.aa=0
man.roll=0
man.left=0
man.right=1
man.colour=(purple)
man.speed=0
man.angle=0
man.dy=0
man.dx=0
char.append(man)
'''
fire=ent((9,9),size)
fire.dx=0
fire.dy=0
fire.right=1
fire.left=0
def Cball(x,y,dr):
    size = 8
    fire = ent((200, 480), size)
    fire.q=0
    if dr==1:
        fire.left=0
        fire.right=1
    elif dr==2:
        fire.right=0
        fire.left=1
    fire.dy=0
    fire.dx=0'''
