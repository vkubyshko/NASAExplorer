from pykinect2 import PyKinectV2, PyKinectRuntime
from pykinect2.PyKinectV2 import *

import time
import ctypes
import _ctypes
import pygame
import sys
import math
import jump
import moonpage
import extras
from random import randint

class Star(object):
    listofStars = []
    def __init__(self):
        self.x = 480
        self.y = 187
        self.xend = randint(40,920)
        if self.xend==480:
            self.xend = 478
        self.d = 5
    def move(self):
        change = int((self.y-184)/35)
        if change==0: change=1
        self.y += change
        self.x = line(self.xend,self.y)
        self.d += 0.4
    def draw(self,other):
        drawStar(other,self.x,self.y,int(self.d),5)
        pass
    def collide(self,other):
        if abs(other.raft_x+120-self.x)<=120 and -30<=(440-self.y)<=-10:
            print('get a star!')
            other.score += 1
            other.numberofBullets += 5
            Star.listofStars.remove(self)

class FinalFlag(Star):
    listofFlags = []
    def __init__(self,x):
        super().__init__()
        self.xend = x
        if x==0:
            self.gif = pygame.image.load('flag_back.gif')
        else:
            self.gif = pygame.image.load('flag.gif')
    def move(self):
        super().move()
        self.d+=0.4
    def draw(self,other):
        d = int(self.d)
        pygame.draw.line(other.screen,(0,0,0),(self.x,self.y),(self.x,self.y-d),2)
        if self.xend==0:
            pygame.draw.polygon(other.screen,(255,0,0),((self.x,self.y-d),(self.x,self.y-int(1.5*d)),(self.x-2*d,self.y-int(1.25*d))),0)
        else:
            pygame.draw.polygon(other.screen,(255,0,0),((self.x,self.y-d),(self.x,self.y-int(1.5*d)),(self.x+2*d,self.y-int(1.25*d))),0)
    def collide(self,other):
        if other.raft_y<=self.y:
            other.state += 1

def line(x,y):
    x1 = 480
    y1 = 187
    y2 = 540
    if x==480: x=479
    slope = (y2-y1)/(x-x1)
    x = (y-y1)/slope + x1
    return int(x)

def drawStar(other, centerX, centerY, diameter, numPoints):
    #make lots of variables to hold diameter, radius, big and small
    dSmall=diameter*3/8
    #middle circle
    #canvas.create_oval(centerX-dSmall/2,centerY-dSmall/2,centerX+dSmall/2,
    #centerY+dSmall/2,fill=color,width=0)
    pygame.draw.circle(other.screen,(255,255,204),(centerX,centerY),int((dSmall+1)/2),0)
    #change between angles based on number of points
    dAngle=(2*math.pi)/numPoints
    # just starting upsidedown instead of subtracting sin changes
    angleStart=(math.pi)*3/2
    ptAngle=dAngle*2
    radius=diameter/2
    dRadius=radius*3/8
    #create triangle for each point which has to meet the circle halway between
    #consecutive points
    for i in range(numPoints):
        pointX=centerX + radius*math.cos(angleStart)
        pointY = centerY + radius*math.sin(angleStart)
        #angle between point and point before/after
        angleAfter=angleStart+dAngle/2
        angleBefore=angleStart-dAngle/2
        #make triangle meet circle
        pxLeft=centerX + dRadius*math.cos(angleBefore)
        pxRight=centerX + dRadius*math.cos(angleAfter)
        pyLeft=centerY + dRadius*math.sin(angleBefore)
        pyRight=centerY + dRadius*math.sin(angleAfter)
        #canvas.create_polygon(pointX,pointY,pxLeft,pyLeft,
        #pxRight,pyRight,fill=color)
        #angleStart=angleStart+dAngle
        L = [(pointX,pointY),(pxLeft,pyLeft),(pxRight,pyRight)]
        pygame.draw.polygon(other.screen,(255,255,204),L,0)
        angleStart=angleStart+dAngle


class Alien(Star):
    listofAliens = []
    def __init__(self):
        super().__init__()
    def draw(self,other):
        alien(other,self.x,self.y,self.d)
    def move(self):
        super().move()
        self.d -=0.2
    def collide(self,other):
        if abs(other.raft_x+120-self.x)<=120 and -40<=(434-self.y)<=0:
            print('got hit by an alien')
            other.restarts -= 1
            Alien.listofAliens.remove(self)
            #new = Alien()
            #Alien.listofAliens.append(new)

class UFO(Star):
    listofUFOs= []
    def __init__(self):
        super().__init__()
        if 475<=self.xend<=480:
            self.xend = 474
        elif 480<self.xend<=485:
            self.xend = 486
        change = self.xend-480
        self.shadowend = 480 + 2*change
        self.shadowy = 185
        self.shadowr = 5
    def draw(self,other):
        pygame.draw.ellipse(other.screen,(111,104,104),(self.x-int(self.d/2),self.y-int(self.d/4),int(self.d),int(self.d/2)),0)
        ufo(other,self.x,self.shadowy,self.shadowr)
    def move(self):
        super().move()
        self.d = self.shadowr
        change = ((self.shadowy-184)/80)
        if change==0: change=0.05
        self.shadowr += change
        self.shadowy = line2(self.shadowend,self.x)
    def moveshadow(self):
        #self.shadowy = line(self.shadowend,self.x)
        pass
    def collide(self,other):
        if abs(other.raft_x+120-self.x)<=120 and -40<=(434-self.y)<=0:
            print('got hit by a UFO')
            other.restarts -= 1
            UFO.listofUFOs.remove(self)
            

def alien(self,cx,cy,r):
    r = int(r)
    pygame.draw.line(self.screen,(108,196,23),(cx,cy),(cx+r,int(cy-r*1.5)),int(r/2))
    pygame.draw.line(self.screen,(108,196,23),(cx,cy),(cx-r,int(cy-r*1.5)),int(r/2))
    pygame.draw.circle(self.screen,(108,196,23),(cx+r,int(cy-r*1.5)),int(r*0.35),0)
    pygame.draw.circle(self.screen,(108,196,23),(cx-r,int(cy-r*1.5)),int(r*0.35),0)
    pygame.draw.circle(self.screen,(255,255,255),(cx+r,int(cy-r*1.5)),int(r*0.20),0)
    pygame.draw.circle(self.screen,(255,255,255),(cx-r,int(cy-r*1.5)),int(r*0.20),0)
    pygame.draw.circle(self.screen,(0,0,0),(cx+r,int(cy-r*1.5)),int(r*0.15),0)
    pygame.draw.circle(self.screen,(0,0,0),(cx-r,int(cy-r*1.5)),int(r*0.15),0)
    pygame.draw.arc(self.screen,(108,196,23),(cx-r,cy-r,2*r,2*r),0,math.pi,r)
    colorpurp = (113,24,196)
    pygame.draw.circle(self.screen,colorpurp,(cx-int(r*0.6),cy-int(r*0.2)),int(r*.2),0)
    pygame.draw.circle(self.screen,colorpurp,(cx+int(r*0.6),cy-int(r*0.2)),int(r*.2),0)
    pygame.draw.circle(self.screen,colorpurp,(cx,cy-int(r*0.6)),int(r*.25),0)
    
    #water waves
    pygame.draw.arc(self.screen,(255,255,255),(cx-int(1.5*r),cy-int(r*.8),r,2*int(r*.4)),math.pi,2*math.pi,int(r*0.1))
    pygame.draw.arc(self.screen,(255,255,255),(cx-int(.5*r),cy-int(r*.8),r,2*int(r*.4)),math.pi,2*math.pi,int(r*0.1))
    pygame.draw.arc(self.screen,(255,255,255),(cx+int(.5*r),cy-int(r*.6),r,2*int(r*.3)),math.pi,2*math.pi,int(r*0.1))



def player(self):
    if self.raft_y==440:
        jump.jump(self)
    if self.jump>0:
        self.raft_y -= self.jump 
        self.jump -=4
        if self.jump ==0:
            self.gravity = 0
    else:
        if self.raft_y<440:
            self.raft_y -= self.gravity
            self.gravity -= 1
        elif self.raft_y>440:
            self.raft_y=440
        
def ufo(self,cx,cy,r):
    #circle
    pygame.draw.circle(self.screen,(229,209,197),(cx,cy-int(r*.5)),int(r*.2),0)
    #pygame.draw.circle(self.screen,(0,0,0),(cx,cy-int(r*.5)),int(r*.2),1)
    L = [(cx-int(r*.3),cy-int(r*.5)),(cx+int(r*.3),cy-int(r*.5)),
         (cx+int(r*.9),cy),(cx-int(r*.9),cy)]
    #middle block
    pygame.draw.polygon(self.screen,(228,86,60),L,0)
    L = [((cx-r),cy),(cx+r,cy),(cx+int(r*.7),cy-int(r*0.35)),(cx-int(r*.7),cy-int(r*0.35))]
    #top
    pygame.draw.polygon(self.screen,(196,0,0),L,0)
    L = [(cx-r,cy),(cx+r,cy),(int(cx+r/2),cy+int(r/4)),(int(cx-r/2),cy+int(r/4))]
    #legs
    pygame.draw.rect(self.screen,(213,196,161),(int(cx-r/3),cy+int(r/4),int(r/1.5),int(r/8)),0)
    pygame.draw.line(self.screen,(213,196,161),(cx,cy),(cx+int(r/3),cy+int(r/2)),3)
    pygame.draw.line(self.screen,(213,196,161),(cx,cy),(cx-int(r/3),cy+int(r/2)),3)
    #bottom half
    pygame.draw.polygon(self.screen,(161,0,0),L,0)
    
def line2(xend,x):
    x1=480
    x2=xend
    y1=185
    y2=540
    slope = (y2-y1)/(x2-x1)
    y = y1+slope*(x-x1)
    return int(y)

def line3(xend,y):
    x1=480
    x2=xend
    y1=185
    y2=540
    if x2==x1:
        x2-=1
    slope = (y2-y1)/(x2-x1)
    x = (y-y1)/slope + x1
    return int(x)

def line4(x,y):
    x1 =480
    y1 =185
    x2 = x
    y2 = y
    if x2==x1:
        x2-=1
    slope = (y2-y1)/(x2-x1)
    x = (540-y1)/slope + x1
    return int(x)

class Bullet(object):
    listofBullets=[]
    def __init__(self,x):
        self.y = 440+20
        self.x = x
        self.xend = line4(self.x,self.y)
    def move(self):
        self.y -= 6
        self.x = line3(self.xend,self.y)
        if self.y<188:
            Bullet.listofBullets.remove(self)
    def draw(self,other):
        pygame.draw.circle(other.screen,(0,0,0),(int(self.x),int(self.y)),5,0)
    def collide(self,other):
        for alien in Alien.listofAliens:
            if abs(alien.x-self.x)<=alien.d and abs(alien.y-self.y)<=6:
                Alien.listofAliens.remove(alien)
                Bullet.listofBullets.remove(self)
                other.killCount += 1




def restartgame(self):
    UFO.listofUFOs = []
    Star.listofStars = []
    Alien.listofAliens = []
    FinalFlag.listofFlags = []
    Bullet.listofBullets = []