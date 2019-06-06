from pykinect2 import PyKinectV2, PyKinectRuntime
from pykinect2.PyKinectV2 import *

#from Vika import GameRuntime.draw_hand
import time
import ctypes
import _ctypes
import pygame
import sys
import extras
import math
import moongamego1
import jump
from random import randint
import solarsysteminit
import moonpage1
import extras

def draw_hand(self):
        x = self.screen_width//2 +int((self.righttip_x)*900)
        y = self.screen_height//2 -int((self.righttip_y)*900)
        gif4 = pygame.image.load('hand.gif')
        self.screen.blit(gif4,(self.hand_x,self.hand_y))
        

def start(self):
    if self.state ==0:
        self.screen.blit(self.pg1, (0,0))
        check(self,8)
        moonpage1.draw_hand(self)
        extras.skipforward(self,5,865)
    elif self.state==1:
        self.screen.blit(self.pg2,(0,0))
        check(self,8)
        moonpage1.draw_hand(self)
        extras.skipforward(self,5,865)
    elif self.state==2:
        self.screen.blit(self.pg3,(0,0))
        check(self,8)
        moonpage1.draw_hand(self)
        extras.skipforward(self,5,865)
        if self.state==3:
            self.time = time.time()
    elif self.state==3:
        self.screen.blit(self.pg4,(0,-12))
        draw_hand(self)
        #cont(self)
        extras.drawContButtonMoon(self,y=450)
        
    elif self.state==4:
        print('state 4')
        pass
    elif self.state == 5:
        redrawMoon(self)
        moongamego1.drawMoonGame(self)
        if self.restarts <1:
            self.state +=1
    #restart page
    elif self.state ==6:
        drawstate6(self)
        moongamego1.restartgame(self)
        extras.drawBackButton(self)
        extras.drawContButton(self)
        
        moonpage1.draw_hand(self)
    #congrats you won
    elif self.state ==7:
        self.wonEarth = True
        drawstate7(self)
        moongamego1.restartgame(self)
        extras.drawBackButton(self)
        extras.drawContButton(self)
        moonpage1.draw_hand(self)
    elif self.state==8:
        moongamego1.restartgame(self)
        self.solarsystem=True
        self.gotoearth = False
        solarsysteminit.init(self)
    

def check(self,wait):
    if time.time()-self.time>=wait:
            self.time = time.time()
            self.state +=1
            
def cont(self):
    b1x1=190
    b1x2=430
    by1=400
    by2=500
    b2x1=580
    b2x2=770
    if b1x1<=self.hand_x<=b1x2 and by1<=self.hand_y<=by2:
        if self.continu:
            if time.time()-self.time>=2:
                self.state=0
        self.continu = True
        self.back = False
    elif b2x1<=self.hand_x<=b2x2 and by1<=self.hand_y<=by2:
        if self.back:
            if time.time()-self.time>=2:
                self.state += 1
        self.continu = False
        self.back = True


def mooninit(self):
    self.gametime = 0
    self.gametimeover = 0
    self.gamewon = False
    self.myfont = pygame.font.SysFont("monospace", 35)
    self.meteortime = time.time()
    self.flashplayer = False
    self.invisible = False
    self.newjump = True
    self.moonstartpage = False
    self.instructionpage = False
    self.moongamepage = False
    self.moongameover = False
    self.playerxstart = 430
    self.playerystart = 240
    self.state = 0
    self.rocket_y=-1800
    self.rocket_x=-200
    self.restarts = 5
    self.score = 0
    block = moongamego1.Blocks(0,400,0)
    moongamego1.Blocks.listofBlocks.append(block)
    block = moongamego1.FinalBlock(randint(400,460),-1870,2)
    moongamego1.Blocks.listofBlocks.append(block)
    self.player = moongamego1.Player(self)
    self.onBlock = False
    self.pg1 = pygame.image.load('pg1.gif')
    self.pg2 = pygame.image.load('pg2.gif')
    self.pg3 = pygame.image.load('pg3.gif')
    self.pg4 = pygame.image.load('moonin.gif')
    #self.button = pygame.image.load('button.gif')
    #self.button1 = pygame.image.load('playagainbutton.gif')
    self.time = time.time()
    self.direction = 0
    self.jump = 0
    self.gravity = 0
    self.xmovement = 0
    self.gif1 = pygame.image.load('rocket.gif')
    self.gif2 = pygame.image.load('moonsky.gif')
    self.giflost = pygame.image.load('youlost.gif')
    self.gifblank = pygame.image.load('blankspace.gif')
    self.ydist = 200
    num = int((200+2100)/self.ydist)
    for i in range(15):
        a = randint(1,3)
        y = 256 - 144*i
        if a==1:
            x = randint(150,550)
            block = moongamego1.Blocks(x,y,1)
            moongamego1.Blocks.listofBlocks.insert(0,block)
        elif a==2:
            x1 = randint(10,430)
            x2 = randint(430,840)
            while (x2-x1)<=100:
                x1 = randint(10,430)
                x2 = randint(430,840)
            block = moongamego1.Blocks(x1,y,2)
            moongamego1.Blocks.listofBlocks.insert(0,block)
            block = moongamego1.Blocks(x2,y,2)
            moongamego1.Blocks.listofBlocks.insert(0,block)
        else:
            x1 = randint(0,286)
            x2 = randint(286,572)
            x3 = randint(572,860)
            while (x2-x1)<=50 or (x3-x2)<=50:
                x1 = randint(0,286)
                x2 = randint(286,572)
                x3 = randint(572,860)
            block = moongamego1.Blocks(x1,y,3)
            moongamego1.Blocks.listofBlocks.insert(0,block)
            block = moongamego1.Blocks(x2,y,3)
            moongamego1.Blocks.listofBlocks.insert(0,block)
            block = moongamego1.Blocks(x3,y,3)
            moongamego1.Blocks.listofBlocks.insert(0,block)
    self.portal = moongamego1.Portal()
    moongamego1.Portal.listofPortals.append(self.portal)
    extras.initMonsters(self)
    self.blackhole = moongamego1.BlackHole(self)
    pass

def redrawMoon(self):
    
    self.screen.blit(self.gif2,(self.rocket_x,self.rocket_y+600))
    self.screen.blit(self.gif2,(self.rocket_x,self.rocket_y-600))
    self.screen.blit(self.gif1, (self.rocket_x,self.rocket_y))
    


def side(self):
    self.dx = self.currighthip_x - self.prevrighthip_x

    #cycle out
    self.prevlefthip_x = self.curlefthip_x
    self.prevrighthip_x= self.currighthip_x

def player(self):
    
    if self.jump<=0:
        side(self)
    if self.onBlock:
        jump.jump(self)
    if self.jump>0:
        self.player.y -= self.jump 
       
        self.jump -=4
        if self.jump ==0:
            self.gravity = 0
        self.player.x += self.dx * 350
    else:
        if self.jump<=0 and not self.onBlock:
            self.player.y += self.gravity
            self.gravity +=1
        self.player.x += self.dx * 250
    if self.player.x<20:
        self.player.x=20
    if self.player.x>840:
        self.player.x = 840



def drawstate6(self):
    redrawMoon(self)
    for block in moongamego1.Blocks.listofBlocks:
        block.draw(self)
    self.player.draw(self)
    self.screen.blit(self.giflost,(300,100))
    self.screen.blit(self.gifblank,(320,250))
    
    label = self.myfont.render('Kill count: ' + str(self.score), 1, (102,0,102))
    self.screen.blit(label,(330,270))
    

    draw_hand(self)
    


def drawstate7(self):
    redrawMoon(self)
    for block in moongamego1.Blocks.listofBlocks:
        block.draw(self)
    self.player.draw(self)
    
    ###YOU WON

    #self.screen.blit(self.giflost,(300,100))
    self.screen.blit(self.gifblank,(320,250))
    label = self.myfont.render('Kill count: ' + str(self.score), 1, (102,0,102))
    self.screen.blit(label,(330,270))
    #min = (self.gametime - self.gametimeover)//60
    #secds = (self.gametime - self.gametimeover)%60
    #label = self.myfont.render('Time: ' + str(min) + 'minutes and '+str(secds)+'seconds', 1, (102,0,102))
    #self.screen.blit(label,(330,310))
    #self.screen.blit(self.button,(350,400))
    draw_hand(self)
    