from pykinect2 import PyKinectV2, PyKinectRuntime
from pykinect2.PyKinectV2 import *

import time
import ctypes
import _ctypes
import pygame
import sys
import extras
import math
from random import randint
import random
import moonpage1
import saturn


def drawMoonGame(self):
    moonpage1.redrawMoon(self)
    moonpage1.player(self)
    if self.player.y>500:
        self.state+=1
        print('you fell off')
    if self.restarts<1:
        self.state +=1
    if self.player.y<200:
        change = 200 - self.player.y
        self.player.y += change
        for block in Blocks.listofBlocks:
            block.y += change
            if block.y>540:
                Blocks.listofBlocks.remove(block)
        self.rocket_y += change
        for portal in Portal.listofPortals:
            portal.y1 += change
            portal.y2 += change
        for monster in extras.Monster.listofMonsters:
            monster.y += change
            if monster.y>540:
                extras.Monster.listofMonsters.remove(monster)
        for monster in extras.Monster2.listofMonster2:
            monster.y += change
            if monster.y>540:
                extras.Monster2.listofMonster2.remove(monster)
        self.blackhole.y1 += change
    self.onBlock = False
    
    for block in Blocks.listofBlocks:
        if block.y>0:
            block.collision(self)
            block.draw(self)
    for portal in Portal.listofPortals:
        portal.draw(self)
    makemeteor(self) #makes and draws
    
    if self.invisible:
        if time.time()-self.time_invisible>1.5:
            self.invisible = False
    else:
        for meteor in Meteorite.listofMeteorites:
            meteor.collide(self)
        for portal in Portal.listofPortals:
            if portal.deactivate == False:
                portal.collide(self)
            elif time.time()-portal.time>2:
                Portal.listofPortals.remove(portal)
        extras.collideMonsters(self)
    extras.drawMonsters(self)
    saturn.draw_score(self)
    if self.invisible:
        if (time.time()-self.time_flash)>0.2:
            self.flashplayer = not self.flashplayer
            self.time_flash = time.time()
    else: self.flashplayer = False
    
    if not self.flashplayer:
        self.player.draw(self)
    
    self.blackhole.collide(self)
    self.blackhole.draw(self)
    pass

def makemeteor(self):
    if time.time()-self.meteortime>randint(2,3)+random.random():
        new = Meteorite()
        self.meteortime = time.time()
        Meteorite.listofMeteorites.append(new)
    for meteor in Meteorite.listofMeteorites:
        meteor.draw(self)
        meteor.y +=3
        if meteor.y>540:
            Meteorite.listofMeteorites.remove(meteor)

class Blocks(object):
    listofBlocks = []
    def __init__(self,x,y, number):
        
        self.x = x
        self.y = y
        if number==0:
            self.gif1 = pygame.image.load('moonground.gif')
            self.length = 960
        elif number==1:
            self.gif1 = pygame.image.load('lava2.gif')
            self.length = 251
        elif number==2:
            self.gif1 = pygame.image.load('lava2.gif')
            #147
            self.length=251
        else:
            self.gif1 = pygame.image.load('lava3.gif')
            self.length=106
    def draw(self,other):
        other.screen.blit(self.gif1, (self.x,self.y))
    def __repr__(self):
        return str(self.x)+' by '+str(self.y)
    def hash(self):
        return hash(self.x,self.y)
    def collision(self,other):
        #100,120
        if other.jump<=0:
            if self.x-50<=other.player.x<=self.x+self.length-50 and 100<=self.y-other.player.y<=120:
            
                other.onBlock = True

class Player(object):
    def __init__(self,other):
        self.x = other.playerxstart
        self.y = other.playerystart
        self.center = self.x+55
        self.gif1 = pygame.image.load('player1.gif')
        
        self.length = 110
    def draw(self,other):
        
        other.screen.blit(self.gif1, (self.x,self.y))

class Meteorite(object):
    listofMeteorites=[]
    def __init__(self):
        self.x=randint(0,810)
        self.y=-50
        self.center = 75 + self.x
        self.gif = pygame.image.load('meteor.gif')
    def draw(self,other):
        
         other.screen.blit(self.gif,(self.x,self.y))
    def __repr__(self):
        return 'Meteorite at: ' + str(self.x) + str(self.y)
    def hash(self):
        return hash(self.x,self.y)
    def collide(self,other):
        center = int(other.player.x+155/2)
        if abs(self.center-center)<=25 and 0<=(other.player.y-self.y)<=80:
            print("YOU GOT HIT BITCH")
            other.restarts -= 1
            other.invisible = True
            other.time_invisible = time.time()
            other.time_flash = time.time()
            Meteorite.listofMeteorites.remove(self)

class FinalBlock(Blocks):
    def __init__(self,x,y, number):
        super().__init__(x,y, number)
        self.gifflag = pygame.image.load('flag.gif')
    def draw(self,other):
        super().draw(other)
        other.screen.blit(self.gifflag, (self.x+40,self.y-140))
    def collision(self,other):
        super().collision(other)
        if self.x-10<=other.player.x<=self.x+40+50 and 90<=self.y-other.player.y<=125:
            other.gamewon = True
            other.gametimeover = time.time()
            other.state = 7

class Portal(object):
    listofPortals = []
    def __init__(self):
        self.side = 75
        length = len(Blocks.listofBlocks)
        options = [i for i in range(5,length-5)]
        random.shuffle(options)
        self.firstindex = options.pop()
        
        self.secondindex = options.pop()
        
        block1 = Blocks.listofBlocks[self.firstindex]
        block2 = Blocks.listofBlocks[self.secondindex]
        self.x1 = block1.x + int(block1.length/3)
        self.y1 = block1.y - self.side
        self.center1 = self.x1 + 37
        self.x2 = block2.x + int(block2.length/3)
        self.y2 = block2.y - self.side
        self.center2 = self.x2 + 37
        self.gif = pygame.image.load('portal.gif')
        self.deactivate = False
    def draw(self,other):
        other.screen.blit(self.gif,(self.x1,self.y1))
        other.screen.blit(self.gif,(self.x2,self.y2))

    def collide(self,other):
        
        if abs(other.player.x-self.x1)<=50 and 30<=(self.y1-other.player.y)<=50:
            
            distx = self.x2-self.x1
            disty = self.y2-self.y1
            
            other.player.y += disty
            other.player.x += distx
            self.deactivate = True
            self.time = time.time()
            other.invisible = True
            other.time_invisible = time.time()
            other.time_flash = time.time()
                
        elif abs(other.player.x-self.x2)<=50 and 30<=(self.y2-other.player.y)<=50:
            
            distx = self.x2-self.x1
            disty = self.y2-self.y1
            other.player.y -= disty
            other.player.x -= distx
            self.deactivate = True
            self.time=time.time()
            other.invisible = True
            other.time_invisible = time.time()
            other.time_flash = time.time()

class BlackHole(Portal):
    def __init__(self,other):
        super().__init__()
        self.gif = pygame.image.load('blackhole.gif')
        self.side = 75
        length = len(Blocks.listofBlocks)
        options = [i for i in range(1,length-2)]
        options.remove(other.portal.firstindex)
        options.remove(other.portal.secondindex)
        random.shuffle(options)
        firstindex = options.pop()
        block1 = Blocks.listofBlocks[firstindex]
        self.x1 = block1.x + int(block1.length/3)
        self.y1 = block1.y - self.side
        self.center1 = self.x1 + 37
    def draw(self,other):
        other.screen.blit(self.gif,(self.x1,self.y1))

    def collide(self,other):
        
        if abs(other.player.x-self.x1)<=50 and 30<=(self.y1-other.player.y)<=50:
            
            distx = self.x2-self.x1
            disty = self.y2-self.y1
            other.player.y += disty
            other.player.x += distx
            other.state +=1



def restartgame(self):
    Blocks.listofBlocks = []
    Portal.listofPortals = []
    extras.Monster.listofMonsters = []
    extras.Monster2.listofMonster2 = []
    Meteorite.listofMeteorites = []

        