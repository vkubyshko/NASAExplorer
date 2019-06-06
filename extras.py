##extras
from pykinect2 import PyKinectV2, PyKinectRuntime
from pykinect2.PyKinectV2 import *

import time
import ctypes
import _ctypes
import pygame
import sys
import math
import moonpage
import moonpage1
import extras
import saturn
import jupiter
import jupiterclasses
from random import randint
import random
import moongamego1
import solarsysteminit
import saturnstart

#calc flap
#calculate flap
def flap(self):
    self.flap = (self.prev_lefthand_y -
                    self.cur_lefthand_y)+ \
                (self.prev_righthand_y -
                    self.cur_righthand_y)
    if math.isnan(self.flap) or self.flap<0:
        self.flap = 0

    #cycle out prev w curr
    self.prev_lefthand_y=self.cur_lefthand_y
    self.prev_righthand_y=self.cur_righthand_y

def bird(self):
    #gravity
    self.bird_height -= 3
    #self.bird_height += self.jump * 250
    if self.bird_height <= 0:
        # Don't let the bird fall off the bottom of the screen
        self.bird_height = 0
    if self.bird_height >= self.screen_height:
        # Don't let the bird fly off the top of the screen
        self.bird_height = self.screen_height
def movehand(self):
    self.hand_x=self.screen_width//4 +int((self.righttip_x)*600)
    self.hand_y=self.screen_height//4 -int((self.righttip_y)*600)
    if self.hand_x<0: 
        self.hand_x=0
    if self.hand_x>self.screen_width: 
        self.hand_x=self.screen_width
    if self.hand_y<0: 
        self.hand_y=0
    if self.hand_y>self.screen_height: 
        self.hand_y=self.screen_height

def moving(self):
    
    if self.righttip_x-self.currighthip_x>0.2:
        self.righttilt=True
        self.raft_y = 400
    elif self.lefttip_x-self.curlefthip_x<-0.2:
        self.lefttilt=True
        self.raft_y =330
    else: 
        self.notilt=True
        self.raft_y=400


def squat(self):
    dif1=self.prevleftknee_y-self.prevlefthip_y
    dif2=self.prevrightknee_y-self.prevrighthip_y
    dif3=self.curleftknee_y-self.curlefthip_y
    dif4=self.currightknee_y-self.currighthip_y
    self.squat = (dif1+dif2)-(dif3+dif4)
    
    self.squat = False
    if (dif3)>-0.15 and dif4>-0.15:
        self.squat = True

    self.prevleftknee_y=self.curleftknee_y
    self.prevrightknee_y=self.currightknee_y
    self.prevlefthip_y=self.curlefthip_y
    self.prevrighthip_y=self.currighthip_y 

def raisehand(self):
    if self.raft_y==440:
        if (self.cur_righthand_y-self.head_y)>=0.1:
            return True


def shoot(self):
    if self.shooting==False and raisehand(self)==True:
        self.shooting=True
        if self.numberofBullets>0:
            new = jupiterclasses.Bullet(self.raft_x+self.player_offset)
            jupiterclasses.Bullet.listofBullets.append(new)
    elif raisehand(self)==None:
        self.shooting=False
    if self.shooting:
        if (time.time()-self.shoottime)>0.5:
            if self.numberofBullets>0:
                new = jupiterclasses.Bullet(self.raft_x+self.player_offset)
                jupiterclasses.Bullet.listofBullets.append(new)
                self.numberofBullets -=1
                self.shoottime = time.time()
    for bullet in jupiterclasses.Bullet.listofBullets:
        bullet.draw(self)
        bullet.move()

def shoottokill(self):
    
    for bullet in jupiterclasses.Bullet.listofBullets:
        bullet.collide(self)

class Monster(object):
    listofMonsters=[]
    def __init__(self,x):
        
        self.ind = x
        self.x = moongamego1.Blocks.listofBlocks[x].x
        self.beg = self.x
        self.end = self.x+251
        rand = randint(0,150)
        
        self.x += rand
        self.y = moongamego1.Blocks.listofBlocks[x].y
        self.dx = 1
        self.gif1 = pygame.image.load('monster1.gif')
        self.gif2 = pygame.image.load('monster1a.gif')
        self.length=100
        self.height=100
    def move(self):
        self.x += self.dx
        if self.x>self.end-self.length or self.x<self.beg:
            self.x-=self.dx
            self.dx*=-1
    def __repr__(self):
        return (self.x,self.y)
    def draw(self,other):
        if self.dx ==1:
            image=self.gif2
        else:
            image=self.gif1
        other.screen.blit(image,(self.x,self.y-self.height))

    def collide(self,other):
        #if get hurt
        xcol = xcollide(self.x,self.length,other.player.x,other.player.length)
        if xcol and (-self.height<=(self.y-self.height-other.player.y)<=60):
            other.restarts -= 1
            other.invisible = True
            other.time_invisible = time.time()
            other.time_flash = time.time()
        #if kill
        if xcol and 60<=(self.y-self.height-other.player.y)<=100:
            moonpage1.side(other)
            other.jump = 30
            self.newjump = False
            Monster.listofMonsters.remove(self)
            other.score +=1


def drawMonsters(self):
    for monster in Monster.listofMonsters:
        monster.draw(self)
        monster.move()
        
    for monster in Monster2.listofMonster2:
        monster.draw(self)
        monster.move()



def collideMonsters(self):
    for monster in Monster.listofMonsters:
        if -100<=monster.y<=540:
            monster.collide(self)
    for monster in Monster2.listofMonster2:
        if -100<=monster.y<=540:
            monster.collide(self)

class Monster2(Monster):
    listofMonster2=[]
    def __init__(self,x):
        super().__init__(x)
        self.gif1 = pygame.image.load('monster2.2.gif')
        self.gif2 = pygame.image.load('monster2.1 (2).gif')
        self.gif3 = pygame.image.load('monster2.4.gif')
        self.gif4 = pygame.image.load('monster2.3.gif')
        self.R = [self.gif1,self.gif2,self.gif1,self.gif3,self.gif4,self.gif3]
        self.gif5 = pygame.image.load('monster2.2a.gif')
        self.gif6 =pygame.image.load('monster2.1a.gif')
        self.gif7 =pygame.image.load('monster2.4a.gif')
        self.gif8 =pygame.image.load('monster2.3a.gif')
        self.L = [self.gif5,self.gif6,self.gif5,self.gif7,self.gif8,self.gif7]
        self.counter = 0
        self.length=86
        self.height = 69
       
    def move(self):
        super().move()
    def draw(self,other):
        if self.dx ==1:
            image = self.R[self.counter]
        else:
            image = self.L[self.counter]
        other.screen.blit(image,(self.x,self.y-self.height))
        self.counter = (self.counter+1)%6
    def collide(self,other):
        #if get hurt
        xcol = xcollide(self.x,self.length,other.player.x,other.player.length)
        if xcol and (-self.height<=(self.y-self.height-other.player.y)<=60):
            other.restarts -= 1
            other.invisible = True
            other.time_invisible = time.time()
            other.time_flash = time.time()
        #if kill
        if xcol and 60<=(self.y-self.height-other.player.y)<=80:
            moonpage1.side(other)
            other.jump = 30
            self.newjump = False
            other.score += 1
            Monster2.listofMonster2.remove(self)
   
def xcollide(x1,length1,x2,length2):
    if x1>=x2:
        if x2+length2>=x1:
            return True
    else:
        if x1+length1>=x2:
            return True

def initMonsters(self):
    list = []
    for i in range(len(moongamego1.Blocks.listofBlocks)):
        if moongamego1.Blocks.listofBlocks[i].length==251:
            list.append(i)
    random.shuffle(list)
    leng = len(list)
    for i in range(int(leng/6)):
        ind = list.pop()
        new=extras.Monster(ind)
        extras.Monster.listofMonsters.append(new)
    for i in range(int(leng/5)):
        ind = list.pop()
        new=extras.Monster2(ind)
        extras.Monster2.listofMonster2.append(new)
    


def skipforward(self,y,x,state=3):
    
    self.screen.blit(self.arrow,(x,y))
    
    print(self.hand_x-x)
    if abs(self.hand_x-x)<=50 and -30<=(self.hand_y-y)<=20:
        self.state = state
    pass




###EARTH
def drawContButton(self,x=520,y=400,state=5):
    length=260
    height=75
    self.screen.blit(self.button,(x,y))
    if -10<=(self.hand_x-x)<=250 and -10<=(self.hand_y-y)<=40:
        moongamego1.restartgame(self)
        self.gotoearth = False
        self.solarsystem = True
        solarsysteminit.init(self)

def drawBackButton(self,x=180,y=400,state=5):
    length=287
    height=75
    self.screen.blit(self.button1,(x,y))
    if -10<=(self.hand_x-x)<=250 and -10<=(self.hand_y-y)<=40:
        
        moongamego1.restartgame(self)
        moonpage1.mooninit(self)
        self.state = state
        self.gametime = time.time()
        #saturn.start(self)

def drawContButtonMoon(self,x=520,y=400,state=5):
    length=260
    height=75
    self.screen.blit(self.button,(x,y))
    if -10<=(self.hand_x-x)<=250 and -10<=(self.hand_y-y)<=40:
        self.state = state

###SATURN
def drawContButtonSattoSS(self,x=520,y=400):
    length=260
    height=75
    self.screen.blit(self.button,(x,y))
    if -10<=(self.hand_x-x)<=250 and -10<=(self.hand_y-y)<=40:
        saturnstart.restartgame(self)
        saturnstart.init(self)
        self.gotosat = False
        self.solarsystem = True
        solarsysteminit.init(self)

def drawBackButtonSat(self,x=180,y=400,state=3):
    length=287
    height=75
    self.screen.blit(self.button1,(x,y))
    if -10<=(self.hand_x-x)<=250 and -10<=(self.hand_y-y)<=40:
        
        saturnstart.restartgame(self)
        saturnstart.init(self)
        self.state = state
        #self.gametime = time.time()
        #saturn.start(self)

def drawContButtonSat(self,x=520,y=400,state=2):
    length=260
    height=75
    self.screen.blit(self.button,(x,y))
    if -10<=(self.hand_x-x)<=250 and -10<=(self.hand_y-y)<=40:
        self.state = state



###JUPITER
def drawContButtonJuptoSS(self,x=520,y=400,state=5):
    length=260
    height=75
    self.screen.blit(self.button,(x,y))
    if -10<=(self.hand_x-x)<=250 and -10<=(self.hand_y-y)<=40:
        jupiterclasses.restartgame(self)
        self.gotojup = False
        self.solarsystem = True
        solarsysteminit.init(self)

def drawBackButtonJup(self,x=180,y=400,state=3):
    length=287
    height=75
    self.screen.blit(self.button1,(x,y))
    if -10<=(self.hand_x-x)<=250 and -10<=(self.hand_y-y)<=40:
        
        jupiterclasses.restartgame(self)
        jupiter.init(self)
        self.state = state
        self.gametime = time.time()
        #saturn.start(self)

def drawContButtonJup(self,x=520,y=400,state=4):
    length=260
    height=75
    self.screen.blit(self.button,(x,y))
    if -10<=(self.hand_x-x)<=250 and -10<=(self.hand_y-y)<=40:
        self.state = state


##main page
def drawButton(self,x=350,y=420):
    length=260
    height=75
    self.screen.blit(self.button,(x,y))
    if -10<=(self.hand_x-x)<=250 and -10<=(self.hand_y-y)<=40:
        self.gotomars = False
        self.solarsystem = True