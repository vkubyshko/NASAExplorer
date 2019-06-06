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
import jupiterclasses
from random import randint
import random

def start(self):
    if self.state == 0:
        self.screen.blit(self.pg1,(0,0))
        moonpage1.check(self,8)
        extras.skipforward(self,5,865)
        moonpage1.draw_hand(self)
    if self.state == 1:
        self.screen.blit(self.pg2,(0,0))
        moonpage1.check(self,8)
        extras.skipforward(self,5,865)
        moonpage1.draw_hand(self)
    elif self.state == 2:
        self.screen.blit(self.pg3,(0,0))
        moonpage1.check(self,8)
        extras.skipforward(self,5,865)
        moonpage1.draw_hand(self)
    elif self.state == 3:
        self.screen.blit(self.pg4,(0,-45))
        extras.drawContButtonJup(self)
        moonpage1.draw_hand(self)
    elif self.state == 4:
        startgame(self)
    elif self.state == 5:
        #lose
        drawRiver(self)
        drawmoon(self)
        drawblocks(self)
        drawstate5(self)
        extras.drawBackButtonJup(self)
        extras.drawContButtonJuptoSS(self)
        moonpage1.draw_hand(self)
        pass
    elif self.state == 6:
        #win
        self.wonJupiter = True
        drawRiver(self)
        drawmoon(self)
        drawblocks(self)
        drawstate6(self)
        extras.drawBackButtonJup(self)
        extras.drawContButtonJuptoSS(self)
        moonpage1.draw_hand(self)
        pass



def startgame(self):
    checkgameover(self)
    drawRiver(self)
    drawmoon(self)
    drawblocks(self)
    moonpage.side(self)
    jupiterclasses.player(self)
    self.tilt = 'None'
    self.raft_x += self.dx * 300
    redrawRaft(self)
    for star in jupiterclasses.Star.listofStars:
        star.move()
        star.draw(self)
        if star.y>560:
            jupiterclasses.Star.listofStars.remove(star)
            
        star.collide(self)
    extras.shoot(self)
    for alien in jupiterclasses.Alien.listofAliens:
        alien.move()
        if alien.y>560:
            jupiterclasses.Alien.listofAliens.remove(alien)
            
        if self.raft_y==440:
            alien.collide(self)
        alien.draw(self)
    for flag in jupiterclasses.FinalFlag.listofFlags:
        flag.move()
        flag.draw(self)
        flag.collide(self)
    
    saturn.draw_score(self)
    label = self.myfont2.render('Bullets left:'+str(self.numberofBullets), 1, (255,255,0))
    self.screen.blit(label, (10, 55))

    if time.time()-self.startime>self.startimer:
        new = jupiterclasses.Star()
        jupiterclasses.Star.listofStars.append(new)
        self.startime = time.time()
        self.startimer = randint(2,5)+random.random()
    if time.time()-self.alientime>self.alientimer:
        new = jupiterclasses.Alien()
        jupiterclasses.Alien.listofAliens.append(new)
        self.alientime = time.time()
        self.alientimer = randint(2,5)+random.random()
    if (time.time()-self.UFOtime)>=self.UFOtimer:
        new = jupiterclasses.UFO()
        jupiterclasses.UFO.listofUFOs.insert(0,new)
        self.UFOtime = time.time()
        self.UFOtimer = randint(2,5)+random.random()
    extras.squat(self)
    for ufo in jupiterclasses.UFO.listofUFOs:
        ufo.move()
        if ufo.y>540:
                jupiterclasses.UFO.listofUFOs.remove(ufo)
        ufo.draw(self)
        if not self.squat:
            ufo.collide(self)
    
    if self.raft_y!=440:
        redrawRaft(self)
    drawplayer(self)
    extras.shoottokill(self)
    
def drawplayer(self):
    image = self.gif3
    offset=0
    if self.squat:
        image = self.squatimage
        offset = 50
    self.screen.blit(image,(self.raft_x+self.player_offset,self.raft_y-80+offset))

    

def drawmoon(self):
    if time.time()-self.time>2:
        new = Mountain(0,185)
        Mountain.listofMountains.insert(0,new)
        new = Mountain(480,185)
        Mountain.listofMountains.insert(0,new)
        self.time = time.time()
    for mountain in Mountain.listofMountains:
         if mountain.counter<5:
            mountain.draw(self)
            mountain.counter +=1
            mountain.move(self)
    pygame.draw.polygon(self.screen,(152,152,152),((0,185),(960,185),(960,540),(0,540)),0)
    pygame.draw.polygon(self.screen,(128,128,128),((0,185),(960,185),(960,540),(0,540)),3)
    for mountain in Mountain.listofMountains:
        if mountain.counter>=5:
            mountain.draw(self)
            mountain.counter +=1
            mountain.move(self)
            if mountain.y >540:
                Mountain.listofMountains.remove(mountain)

def drawblocks(self):
    L = [185+i*4 for i in range(100)]
    for i in range(len(L)):
        y = L[i]
        r = self.r[(self.first+i)%64]
        g = self.g[(self.first+i)%64]
        b = self.b[(self.first+i)%64]
        x1 = line1(self,y)
        x2 = line1(self,y+2)
        x3 = line2(self,y+2)
        x4 = line2(self,y)
        
        pygame.draw.polygon(self.screen,(r,g,b),((x1,y),(x2,y+4),(x3,y+4),(x4,y)),0)
       # print(r)
    self.first = (self.first + 1)%64
    
def drawRiver(self):
    self.screen.blit(self.gif1, (0,0))

def redrawRaft(self):
    #print(self.notilt,self.righttilt,self.lefttilt)

    if self.tilt=='None':
        raft = self.gif2
    elif self.tilt=='Left':
        raft = self.gif4
    elif self.tilt=='Right':
        raft = self.gif5
    self.screen.blit(raft,(self.raft_x,self.raft_y))
    
    pass



def redrawRiver(self):
    self.screen.blit(self.gif1, (-50,0))

class Mountain(object):
    listofMountains=[]
    def __init__(self,x,y):
        self.r = 152
        self.g = 152
        self.b = 152
        self.x1 = x
        self.x2 = x+480
        self.xoffset = 0
        self.y = y
        self.Pointx = []
        self.multiplier = 0.2
        self.grow = 1
        if x ==0:
            self.point = (0,540)
            self.dx = 1
        else: 
            self.point = (960,540)
            self.dx =-1
        for i in range(15):
            x = randint(10,460)
            self.Pointx.append(x)
        self.Pointx.sort()
        self.Pointy = []
        for i in range(15):
            y1 = randint(10,30)
            self.Pointy.append(y1)
        self.Points = [(self.x1-self.xoffset,self.y)] + \
        [(self.Pointx[i]-self.xoffset+self.x1,self.y-int(self.Pointy[i]*self.multiplier)) for i in range(15)] + \
        [(self.x2-self.xoffset,self.y)] + [self.point]
        
        self.counter = 0
        
    def draw(self,other):
        
        pygame.draw.polygon(other.screen,(int(self.r),int(self.g),int(self.b)),self.Points,0)
        pygame.draw.polygon(other.screen,(128,128,128),self.Points,3)
    def move(self,other):
        
        if self.counter<20:
            self.multiplier += 0.02
            self.Points = [(self.x1,self.y)] + [(self.Pointx[i]+self.x1,self.y-int(self.Pointy[i]*self.multiplier)) for i in range(15)] + [(self.x2,self.y)] + [self.point]
        else:
            self.r +=0.2
            self.g +=0.2
            self.b +=0.2
            change = int((self.y-184)/40)
            if change==0: change=1
            if self.x1==0:
                oldx = line1(self,self.y)
                newx = line1(self,self.y+change)
                dx = (newx-oldx)
            else:
                oldx = line2(self,self.y)
                newx = line2(self,self.y+change)
                dx = (newx-oldx)
            self.y += change
            self.multiplier += 0.03
            self.xoffset -= dx
            self.grow *= 1.005
            if self.multiplier>10:
                self.multiplier = 1
            #for y in range(len(self.Pointy)):
                #self.Pointy[y] = self.Pointy[y]+ self.y
            self.Points = [self.point] + [(self.x1-self.xoffset,self.y)] + \
            [(int(self.Pointx[i]-self.xoffset*self.grow+self.x1),self.y-int(self.Pointy[i]*self.multiplier)) for i in range(15)] + \
            [(self.x2-self.xoffset,self.y)] + [self.point]
          

        pass

    def __repr__(self):
        return hash(self.x)

def draw(self,other,Points):
    pygame.draw.polygon(self.screen,(255,255,255),Points,0)

def changescore(self):
    if time.time()-self.score_time>=0.5:
        
        self.score_time=time.time()
        self.score -= 1

def init(self):
    self.state = 0
    self.starttime = time.time()
    self.endtime = 60
    self.player_offset = 80
    self.shoottime = 0
    self.shooting = False
    self.time = time.time()
    self.startime = time.time()
    self.startimer = randint(1,4)
    self.alientime = time.time()
    self.alientimer = randint(1,4)
    self.UFOtime = time.time()
    self.UFOtimer = randint(1,4)
    self.UFOredraw = time.time()
    self.score_time = time.time()
    self.squatting = False
    self.squat = False
    self.killCount = 0
    self.pg1 = pygame.image.load('juppg4.gif')
    self.pg2 = pygame.image.load('juppg2.gif')
    self.pg3 = pygame.image.load('juppg3.gif')
    self.pg4 = pygame.image.load('jupin.gif')
    self.gif1 = pygame.image.load('jupgame.gif')
    self.gif2 = pygame.image.load('raftt.gif')
    self.gif3 = pygame.image.load('player1.gif')
    #self.gif4 = pygame.image.load('tilttleft.gif')
    #self.gif5 = pygame.image.load('tilttright.gif')
    self.heart = pygame.image.load('heart.gif')
    self.squatimage = pygame.image.load('squatplayer.gif')
    self.win = pygame.image.load('win.gif')
    self.giflost = pygame.image.load('youlost.gif')
    self.gifblank = pygame.image.load('blankspace.gif')
    self.myfont = pygame.font.SysFont("monospace", 30)
    self.myfont2 = pygame.font.SysFont("monospace", 20)
    self.restarts = 5
    self.raft_x = 360
    self.raft_y = 440
    self.tilt = 'None'
    self.jump = 0
    self.gravity = 0
    self.numberofBullets = 10
    self.score = 0
    self.first = 0
    self.r = [47+4*i for i in range(32)] + [47+i*4 for i in range(31,-1,-1)]
    self.g = [86+i*4 for i in range(32)] + [86+i*4 for i in range(31,-1,-1)]
    self.b = [233+int(i**0.75) for i in range(32)] + [233+int(i**0.75) for i in range(31,-1,-1)]
    mount = Mountain(0,185)
    Mountain.listofMountains.append(mount)
    mount = Mountain(480,185)
    Mountain.listofMountains.append(mount)
    
    
def line1(self,y):
    x1 = 480
    y1 = 185
    x2 = 0
    y2 = 540
    slope = (y2-y1)/(x2-x1)
    x = (y-y1)/slope + x1
    return int(x)

def line2(self,y):
    x1 = 480
    y1 = 185
    x2 = 960
    y2 = 540
    slope = (y2-y1)/(x2-x1)
    x = (y-y1)/slope + x1
    return int(x)


def redrawRaft(self):
    #circles
    #(224,215,208),(194,175,161),(145,131,120),(99,70,49),(66,47,33),(49,35,24)
    length = 240
    r = 20
    for i in range(6):
        leftx = jupiterclasses.line(self.raft_x+(2*r*i),self.raft_y)
        rightx = jupiterclasses.line(self.raft_x+2*r+(2*r*i),self.raft_y)
        L = [(self.raft_x+(2*r*i),self.raft_y+70),(self.raft_x+(2*r*(i+1)),self.raft_y+70),
             (rightx,self.raft_y),(leftx,self.raft_y)]
        pygame.draw.polygon(self.screen,(99,70,49),L,0)
        pygame.draw.polygon(self.screen,(66,47,33),L,3)
        pygame.draw.arc(self.screen,(66,47,33),(leftx,int(self.raft_y-3),rightx-leftx,10),0,math.pi,3)
        pygame.draw.circle(self.screen,(66,47,33),(int(self.raft_x+r+(2*r*i)),int(self.raft_y+70)),r+1,0)
        pygame.draw.circle(self.screen,(102,51,0),(int(self.raft_x+r+(2*r*i)),int(self.raft_y+70)),r-1,0)
        


def checkgameover(self):
    if self.restarts<1:
        self.state+=1
    elif (time.time()-self.starttime)>=self.endtime:
        flag1 = jupiterclasses.FinalFlag(0)
        flag2 = jupiterclasses.FinalFlag(960)
        jupiterclasses.FinalFlag.listofFlags.append(flag1)
        jupiterclasses.FinalFlag.listofFlags.append(flag2)
        self.starttime=time.time()
        


def drawstate5(self):
    
    self.screen.blit(self.giflost,(300,100))
    self.screen.blit(self.gifblank,(315,250))
    
    score = self.score
    label = self.myfont.render('Stars: ' + str(self.score), 1, (102,0,102))
    self.screen.blit(label,(390,270))
    label = self.myfont.render('Kill Count: ' + str(self.killCount), 1, (102,0,102))
    self.screen.blit(label,(370,320))
    
def drawstate6(self):
    
    self.screen.blit(self.win,(285,50))
    self.screen.blit(self.gifblank,(315,250))
    
    score = self.score
    label = self.myfont.render('Stars: ' + str(self.score), 1, (102,0,102))
    self.screen.blit(label,(390,270))
    label = self.myfont.render('Kill Count: ' + str(self.killCount), 1, (102,0,102))
    self.screen.blit(label,(370,320))
    
