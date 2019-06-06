from pykinect2 import PyKinectV2, PyKinectRuntime
from pykinect2.PyKinectV2 import *

import time
import ctypes
import _ctypes
import pygame
import sys
import math
from random import randint
import random
import copy

##960,540
##height of player 115
#astronaut sprite
#https://pjcr16.wordpress.com/category/sprites/ 

def start(self):
    redrawAll(self)
    print(len(Road.rows),len(Meteor.listofMeteors),len(Coin.listofCoins),len(Octo.rings))
    gameplay(self)
    #else: pass

def gameplay(self):
    print(len(Road.rows),len(Meteor.listofMeteors),len(Coin.listofCoins),len(Octo.rings))
    if time.time()-self.timeplayer>=0.15:
        tilt(self)
        movee(self)
        if self.octo == True:
            new = Octo()
            Octo.rings.insert(0,new)
        for ring in Octo.rings:
            ring.r += int(ring.r**0.65)
            if ring.r > 500:
                Octo.rings.remove(ring)
        if self.spriteplay == self.gif2:
            self.spriteplay = self.gif1
        else:
            self.spriteplay = self.gif2
        
        #self.timeplayer = time.time()

        
        self.octo = not self.octo 

        self.timeplayer=time.time()
    print(time.time())
    for meteor in Meteor.listofMeteors:
        if meteor.y>540:
            Meteor.listofMeteors.remove(meteor)
        meteor.move()
    for coin in Coin.listofCoins:
        coin.move()
        if coin.y>540:
            Coin.listofCoins.remove(coin)
        

    if (time.time()-self.timemeteor)>=randint(1,3)+random.random():
        if self.counter< self.counterstop:
            new = Meteor(randint(0,6))
            Meteor.listofMeteors.append(new)
            self.timemeteor = time.time()
    if (time.time()-self.timecoin)>=randint(1,3)+random.random():
        if self.counter<self.counterstop:
            new = Coin()
            Coin.listofCoins.append(new)
            self.timecoin = time.time()


    
    if time.time()-self.timeee>=0.5:
        self.counter += 1
        timerFired(self)
        self.timeee=time.time()
        self.score -= 1
    
    pass

def draw_score(self):
    # render text
    #label = self.myfont.render('Score: ' + str(self.score), 1, (255,255,0))
    score = self.score
    self.heart = pygame.image.load('heart.gif')
    if score<0:
        score = 0
    elif score>100:
        score=100
    textt = 'Coins:'
    if self.gotojup:
        textt = 'Stars:'
    elif self.gotoearth:
        textt = 'Kills:'
    label = self.myfont.render(textt + str(score), 1, (255,255,0))
    self.screen.blit(label, (10, 5))
    if self.restarts>=1:
        self.screen.blit(self.heart,(210,5))
    if self.restarts>=2:
        self.screen.blit(self.heart,(265,5))
    if self.restarts>=3:
        self.screen.blit(self.heart,(320,5))
    if self.restarts>=4:
        self.screen.blit(self.heart,(375,5))
    if self.restarts>=5:
        self.screen.blit(self.heart,(430,5))

def turncoin(self):
    self.turn += self.dturn
    if self.turn<.1 or self.turn>1:
        self.turn -= self.dturn
        self.dturn *= -1

def draw_background(self):
    positions = [int(i**0.6) for i in range(100)]
    for ring in Octo.rings:
        octo = octogon(ring.r)
        pygame.draw.polygon(self.screen, (255,105,180), octo,2)

class Octo(object):
    rings = []
    def __init__(self):
        self.r = 30


def init(self,board=None):
    self.counteratend=0
    self.timemeteor = time.time()
    self.timeee = time.time()
    self.time_flash = 0
    self.timecoin = time.time()
    self.time = time.time()
    self.time1 = time.time()
    self.timeplayer = time.time()
    self.timemeteor = time.time()
    self.flashplayer = False
    self.invisible = False
    self.octo = False
    self.gif1 = pygame.image.load('player1.gif')
    self.gif2 = pygame.image.load('player2.gif')
    self.heart = pygame.image.load('heart.gif')
    self.myfont = pygame.font.SysFont("monospace", 26)
    initialize()
    self.draw = self.gif1
    self.spriteplay = self.gif1
    self.time_invisible = 0 
    self.player_x = 430
    self.player_y = 390
    self.turn = 1
    self.dturn = .05
    ring = Octo()
    self.foreverring = Octo()
    Octo.rings.append(ring)
    self.play = False
    self.score = 100
    self.restarts = 5
    
    pass

class Meteor(object):
    listofMeteors = []
    def __init__(self,i):
        self.color = (153,78,0)
        self.y = 155
        self.left = Road.rows[-i].left1
        self.right = Road.rows[-i].right1
        self.x = int((self.right+self.left)//2)
        self.c = int((self.right-self.left)//2)
        self.r = 5
        self.i = i
    def draw(self,other):
        rr = int(self.r)
        pygame.draw.circle(other.screen, (105,55,0), (self.x,self.y), self.r)
        r = int(rr*0.9)
        pygame.draw.circle(other.screen, (111,58,0), (self.x,self.y+r-rr), r)
        r = int(r*0.9)
        pygame.draw.circle(other.screen, (117,61,0), (self.x,self.y+r-rr), r)
        r = int(r*0.9)
        pygame.draw.circle(other.screen, (123,64,0), (self.x,self.y+r-rr), r)
        r = int(r*0.9)
        pygame.draw.circle(other.screen, (129,67,0), (self.x,self.y+r-rr), r)
        r = int(r*0.9)
        pygame.draw.circle(other.screen, (135,70,0), (self.x,self.y+r-rr), r)
        r = int(r*0.9)
        pygame.draw.circle(other.screen, (141,73,0), (self.x,self.y+r-rr), r)
        r = int(r*0.9)
        pygame.draw.circle(other.screen, (147,76,0), (self.x,self.y+r-rr), r)
        r = int(r*0.9)
        pygame.draw.circle(other.screen, self.color, (self.x,self.y+r-rr), r)
    def move(self):
        self.y += int((self.y-100)/40)
        xleft = line1(self.y,Road.change)
        xright = line2(self.y,Road.change)
        size = int((xright-xleft)//7)
        #print(size)
        self.x = int(xleft + size*self.i + size//2)
        size = int((-319+(self.y)*(45/19))//15)
        self.r = size
    def collide(self,other,center):
        if self.i==int(center//(960/7)) and self.y>=450:
            
            other.invisible = True
            other.time_invisible = time.time()
            other.restarts -= 1
            if other.restarts==0:
                other.play = False
            else:
                
                other.invisible = True
                other.time_invisible = time.time()
                other.time_flash = time.time()
                Meteor.listofMeteors.remove(self)
                
def wait(w):
    tim = time.time()
    while time.time()-tim<w:
        pass
    return

class Coin(Meteor):
    listofCoins=[]
    def __init__(self):
        self.i = randint(0,6)
        super().__init__(self.i)
        self.color = (255,223,0)
    def draw(self,other):
        turncoin(other)
        c = other.turn*self.r
        pygame.draw.ellipse(other.screen, (220,181,24), (self.x-c,self.y-self.r,2*c,2*self.r), 0)
        r = int(c*0.9)
        pygame.draw.ellipse(other.screen, (self.color), (self.x-r,self.y-self.r*.9,2*r,2*self.r*.9), 0)
        r = int(r*0.9)
        pygame.draw.ellipse(other.screen, (220,181,24), (self.x-r,self.y-self.r*.81,2*r,2*self.r*.81), 0)
        r = int(r*0.9)
        pygame.draw.ellipse(other.screen, (self.color), (self.x-r,self.y-self.r*.9*.81,2*r,2*self.r*.9*.81), 0)
    def move(self):
        self.y += int((self.y-80)/60)
        xleft = line1(self.y,Road.change)
        xright = line2(self.y,Road.change)
        size = int((xright-xleft)//7)
        #print(size)
        self.x = int(xleft + size*self.i + size//2)
        size = int((-319+(self.y)*(45/19))//20)
        self.r = size
    def collide(self,other,center):
        
        if self.i==int(center//(960/7)) and self.y>=450:
            
            Coin.listofCoins.remove(self)
            #new = Coin()
            #Coin.listofCoins.append(new)
            other.score += 20
            



class Road(object):
    
    positions = [i*10 for i in range(7)]
    rows = []
    colors = [(148,0,211),(75,0,130),(0,0,255),
            (0,255,128),(0,255,0),(255,255,0),
            (255,127,0),(255,0,0)]
    change = 0
    dchange = 1
    
    def __init__(self,y,h,index,pattern):
        #on horizon
        #print(index,self.y)
        self.y = y
        self.x=0
        self.index = index
        self.rgb = Road.colors[self.index]
        #what we can see
        self.height = h
        self.width = 10
        self.m=2
        self.pattern = pattern
        self.left = line1(self.y)
        self.right = line2(self.y)
        self.left1 = line1(self.y+self.height)
        self.right1 = line2(self.y+self.height)
        dist1 = self.right1-self.left1
        size1 = dist1/7
        self.size = size1
        
        
    def draw(self,other):
        left = line1(self.y,self.change)
        right = line2(self.y,self.change)
        left1 = line1(self.y+self.height,self.change)
        right1 = line2(self.y+self.height,self.change)
        dist = right-left
        dist1 = right1-left1
        size = dist/7
        size1 = dist1/7
        drawGrid(self,other,size,size1,left,right,
        left1,right1)
    def __repr__(self):
        return str(self.pattern)
    def collide(self,other,player):
        block = int(player//self.size)
        old = self.pattern[block]
        
        if old=='x':
            self.pattern[block]='xn'
        elif old=='':
            self.pattern[block]='n'

    
def drawGrid(self,other,size,size1,left,right,left1,right1):
    for i in range(7):
        if self.pattern[i]=='x':
            col=(0,0,0)
        elif self.pattern[i]=='':
            col=self.rgb
        elif self.pattern[i]=='r':
            col=(240,51,51)
        elif self.pattern[i]=='w':
            col=(255,255,255)
        elif self.pattern[i]=='c':
            col=(240,51,51)
        else: col=(200,200,200)
        
        lpt=left+size*i+2
        lpt1=left1+size1*i+2
        rpt=lpt+size-2
        rpt1=lpt1+size1-2
        pygame.draw.polygon(other.screen,col,
                            ((lpt,self.y),(rpt,self.y),
                            (rpt1,self.y+self.height),
                            (lpt1,self.y+self.height)))

def drawplayer(self,gif):
    self.screen.blit(self.spriteplay,(self.player_x,self.player_y))

##960,540
##height of player 115, 10 margin on bottom


####################################

def initialize(first=None):
    # load data.xyz as appropriate
    y=160
    h=2
    r=200
    g=100
    b=20
    mult=2
    prev=None
    for i in range(15):
        if i==0:
            board=intBoard()
        else:
            board=blankBoard()
        row=Road(y,h,i%8,board)
        Road.rows.insert(0,row)
        y += h+1
        h += int(mult)
        mult *= 1.2
        prev=board
    for i in range(len(Road.rows)):
        row = Road.rows[i]
    pass


def timerFired(self):
    lastrow = Road.rows[-1]
    if self.counter>=self.counterstop:
        prevpat = ['w','c','w','c','w','c','w']
    else:
        prevpat = initBoard(lastrow.pattern)
    for i in range(len(Road.rows)):
        row=Road.rows[-i-1]
        row.index = (row.index-1)%8
        row.rgb = Road.colors[row.index]
        curpat=row.pattern
        row.pattern=prevpat
        prevpat=curpat
        ####
        Road.change += Road.dchange
        if Road.change<=-50 or Road.change >=50:
            Road.change -= Road.dchange
            Road.dchange *=-1

def redrawAll(other):
    pygame.draw.rect(other.screen,(0,0,0),(0,0,980,550),0)
    draw_background(other)
    octo = octogon(other.foreverring.r)
    pygame.draw.polygon(other.screen, (255,105,180), octo,2)
    center = other.player_x+40
    if other.invisible:
            if (time.time()-other.time_invisible)>=3:
                other.invisible = False
    for i in range(len(Road.rows)):
        row = Road.rows[i]
        
        if i==2 and not other.invisible:
            row.collide(other,center)
            pass
        
        if i==1:
            if 'xn' in row.pattern:
                ix = row.pattern.index('xn')
                row.pattern[ix]='x'
                if not other.invisible:
                    other.restarts -= 1
                    if other.restarts==0:
                        other.play = False
                    else:
                        other.restarts -= 1
                        other.invisible = True
                        other.time_invisible = time.time()
                        other.time_flash = time.time()
                
            elif 'n' in row.pattern:
                ix = row.pattern.index('n')
                row.pattern[ix]=''
        
        row.draw(other)
    for meteor in Meteor.listofMeteors:
        if not other.invisible:
            meteor.collide(other,center)
        meteor.draw(other)
        
    for coin in Coin.listofCoins:
        if not other.invisible:
            coin.collide(other,center)
        coin.draw(other)
    
    if other.invisible:
        if (time.time()-other.time_flash)>0.2:
            other.flashplayer = not other.flashplayer
            other.time_flash = time.time()
    else: other.flashplayer = False
    
    if not other.flashplayer:
        drawplayer(other,other.spriteplay)

    draw_score(other)

        
    # draw in canvas
    pass

def movee(self):
    mov = int(960/8)
    if self.tiltright and self.player_x<960-2*mov:
        self.player_x += mov
    elif self.tiltleft and self.player_x>mov:
        self.player_x -= mov

def tilt(self):
    self.tiltright = False
    self.tiltleft = False
    dif = self.spineshoulder_x - self.spinebase_x
    if dif>=0.1:
        self.tiltright = True
    elif dif <=-0.1:
        self.tiltleft = True

def intBoard():
    board = ['' for i in range(7)]
    for i in range(1):
        ind = randint(0,6)
        board[ind] = 'x'
    return board

def blankBoard():
    board = ['' for i in range(8)]
    return board

def initBoard(prev):
    board = copy.copy(prev)
    on=0
    off=0
    while off<=1:
        ind = randint(0,6)
        if board[ind]=='':
            board[ind]='x'
            off+=1
    while on<=1:
        ind = randint(0,6)
        if board[ind]=='x':
            board[ind]=''
            on+=1
    return board

#http://www.webmath.com/_answer.php

    
def linemeteor(x,y,i):
    y2=155
    x2=int(450+(60/14)+i*(60/7))
    y1=535
    x1=int((960/14)+i*(960/7))
    slope=(y2-y1)/(x2-x1)
    x = int((y-y1)/slope+x1)
    return int(x)

def function(x1,y1,x2,y2,x3,y3,point):
    a1=x1**2
    a2=x2**2
    a3=x3**2
    b1=x1
    b2=x2
    b3=x3
    
    top = (b2-b3)*(y1-y2)-(b1-b2)*(y2-y3)
    bottom = (b2-b3)*(a1-a2)-(b1-b2)*(a2-a3)
    a = top/bottom
    
    top = (y1-y2)-(a1-a2)*a
    b = top/(b1-b2)
    
    c = y1-a1*a-b1*b
    
    return a*point**2+b*point+c

def line1(y,change=0):
    x1=470
    y1=160
    x2=0
    y2=540
    slope=(y2-y1)/(x2-x1)
    x = (y-y1)/slope + x1
    start = 450 -(450/2)
    answer=function(y2,x2,y1,x1,350,start+change,y)
    return int(answer)

def line2(y,change=0):
    x1=490
    y1=160
    x2=960
    y2=540
    slope=(y2-y1)/(x2-x1)
    x = (y-y1)/slope +x1
    start = 510 +(450/2)
    answer=function(y2,x2,y1,x1,350,start+change,y)
    return int(answer)

def line(x1,y1,boxnum,height):
    y2=160
    x2=270+boxnum*1
    slope=(y2-y1)/(x2-x1)
    x = ((height/slope)+x1)
    return int(x)

def octogon(r):
    cx = 480
    cy=151.9
    x8 = 480 - r
    x7 = x8
    x3 = 480 + r
    x4 = x3
    x1 = 480 - int(r*0.6)
    x6 = x1
    x2 = 480 + int(r*0.6)
    x5 = x2

    y8 = int((1/12)*x8 + 120)
    y7 = int((-1/12)*x7 + 200)
    y3 = int((-1/12)*x3 + 200)
    y4 = int((1/12)*x4 + 120)
    y1 = int((25/24)*x1 - 340)
    y2 = int((-25/24)*x2 + 660)
    y6 = int((-25/24)*x6 + 660)
    y5 = int((25/24)*x5 - 340)


    return ((x1,y1),(x2,y2),(x3,y3),
            (x4,y4),(x5,y5),(x6,y6),
            (x7,y7),(x8,y8))