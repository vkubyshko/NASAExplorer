from pykinect2 import PyKinectV2, PyKinectRuntime
from pykinect2.PyKinectV2 import *

import time
import ctypes
import _ctypes
import pygame
import sys
import math
from random import randint
import copy
import saturn 
import moonpage
import moonpage1
import extras
import saturntemp

def start(self):
    if self.state == 0:
        self.screen.blit(self.pg1,(0,0))
        moonpage1.check(self,8)
        moonpage1.draw_hand(self)
        extras.skipforward(self,5,865,2)
    if self.state == 1:
        self.screen.blit(self.pg2,(0,0))
        moonpage1.check(self,8)
        moonpage1.draw_hand(self)
        extras.skipforward(self,5,865,2)
    elif self.state == 2:
        self.screen.blit(self.pg3,(0,0))
        moonpage1.check(self,8)
        moonpage1.draw_hand(self)
        extras.drawContButtonSat(self,state=3)
        if self.state ==3:
            self.play=True
    elif self.state == 3:
        saturn.redrawAll(self)
        if self.score<=0 or self.restarts<1:
            self.state = 5
        if self.counter>=self.counterstop+13:
            if self.blink:
                self.screen.blit(self.win,(300,150))
                #self.time = time.time()
            if time.time() - self.time>0.5:
                self.blink = not self.blink
                self.time = time.time()
                self.counteratend +=1
            if self.counteratend>=10:
                self.state += 1
        elif self.play==True and self.score>0:
            saturn.gameplay(self)
            
    elif self.state == 4:
        self.wonSaturn = True
        saturn.redrawAll(self)
        drawstate4(self)
        extras.drawBackButtonSat(self,state=2)
        extras.drawContButtonSattoSS(self)
    elif self.state == 5: ##YOU LOST
        saturn.redrawAll(self)
        drawstate5(self)
        extras.drawBackButtonSat(self,state=2)
        extras.drawContButtonSattoSS(self)
        moonpage1.draw_hand(self)

def init(self):
    self.state=0
    self.pg1 = pygame.image.load('satp1.gif')
    self.pg2 = pygame.image.load('satp2.gif')
    self.pg3 = pygame.image.load('satinst.gif')
    self.gifready = pygame.image.load('ready.gif')
    self.gifset = pygame.image.load('set.gif')
    self.gifgo = pygame.image.load('go.gif')
    self.win = pygame.image.load('win.gif')
    self.giflost = pygame.image.load('youlost.gif')
    self.gifblank = pygame.image.load('blankspace.gif')
    saturn.init(self)
    self.invisible = False
    self.counter = 0
    self.counterstop = 100
    self.blink = True
    self.invisible_time = 0



def restartgame(self):
    saturn.Coin.listofCoins=[]
    saturn.Meteor.listofMeteors=[]
    saturn.Octo.rings = []
    saturn.Road.rows = []



def drawstate4(self):
    ###YOU WON

    #self.screen.blit(self.giflost,(300,100))
    self.screen.blit(self.gifblank,(320,250))
    label = self.myfont.render('Final lives: ' + str(self.restarts), 1, (102,0,102))
    self.screen.blit(label,(330,270))
    label = self.myfont.render('Final energy: ' + str(self.score) + '%', 1, (102,0,102))
    self.screen.blit(label,(330,310))





def drawstate5(self):
    
    self.screen.blit(self.giflost,(300,100))
    self.screen.blit(self.gifblank,(320,250))
    label = self.myfont.render('Final lives: ' + str(self.restarts), 1, (102,0,102))
    self.screen.blit(label,(330,270))
    score = self.score
    if score>100:
        score=100
    elif score<0:
        score=0
    label = self.myfont.render('Final energy: ' + str(self.score) + '%', 1, (102,0,102))
    self.screen.blit(label,(330,310))
    