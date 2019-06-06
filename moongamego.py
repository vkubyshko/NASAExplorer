from pykinect2 import PyKinectV2, PyKinectRuntime
from pykinect2.PyKinectV2 import *

import time
import ctypes
import _ctypes
import pygame
import sys
import math
from random import randint
import moonpage


def drawMoonGame(self):
    for block in Blocks.listofBlocks:
        block.draw(self)
    moonpage.player(self)
    self.player.draw(self)
    pass

class Blocks(object):
    listofBlocks = []
    def __init__(self,length,color='silver'):
        x = randint(0,1000)
        #-2100,400
        y = randint(-2100,400)
        #length = randint(25,40)
        self.x = x
        self.y = y
        self.length = length
        self.height = 10
        self.color = color
        self.gif1 = pygame.image.load('lava1.gif')
        self.gif2 = pygame.image.load('lava2.gif')
        self.gif3 = pygame.image.load('lava3.gif')
    def draw(self,other):
        other.screen.blit(self.gif1, (self.x,self.y))
    def __repr__(self):
        return str(self.x)+'by'+str(self.y)
    def hash(self):
        return hash(self.x,self.y)

class Player(object):
    def __init__(self,other):
        self.x = other.screen_width//5
        self.y = other.screen_height//3
        self.gif1 = pygame.image.load('player.gif')
    def draw(self,other):
        other.screen.blit(self.gif1, (self.x,self.y))
    def jump(self):
        self.y-=20

class Meteorite(object):
    listofMeteorites=[]
    def __init__(self,x):
        self.x=x
        self.r=10
        self.y=-200
        self.color='brown'
    def draw(self):
        pygame.draw.rect(self.screen,(0,0,200),
                        (self.x,self.y,self.x+self.r,self.y+self.r),
                        fill=self.color)
    def __repr__(self):
        return 'Meteorite at: ' + str(self.x) + str(self.y)
    def hash(self):
        return hash(self.x,self.y)

def collision(self):
    if self.goingdown:
        for block in Blocks.listofBlocks:
            if (block.x<=self.player.x<block.x+200) and \
            100<=(block.y-self.player.y)<=200:
                print('on block!!!')
                self.player.y = block.y-120
                self.onblock = True
                self.jump = False
                #if block == data.endblock:
                #    print('game over')
            else: self.onblock = False

def moveMeteorites(data):
    for meteorite in Meteorite.listofMeteorites:
        meteorite.y +=5

def collidemet(data):
    for meteorite in Meteorite.listofMeteorites:
        if abs(meteorite.x-data.player.x)<=10 and \
        abs(meteorite.y-data.player.y)<=10:
            print('crash')
