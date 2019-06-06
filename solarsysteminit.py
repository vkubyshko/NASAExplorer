from pykinect2 import PyKinectV2, PyKinectRuntime
from pykinect2.PyKinectV2 import *

import time
import ctypes
import _ctypes
import pygame
import sys
import math
import moonpage1
import extras
import saturn
import saturnstart
import jupiter
import jupiter1
import jump
from startscreen import *

#return to solarsystem
def init(self):
    self.screen_width = 1920
    self.screen_height = 1080
    self.continu = False
    self.back = False
    self.solarsystem=True
    self.gotoearth=False
    self.gotomars=False
    self.gotojup=False
    self.gotosat=False
    self.bird_height = self.screen_height/2
    self.bird_width = self.screen_width/2
    self.mars_x=0
    self.mars_y=0
    self.mars=False
    self.earth=False
    self.jupiter=False
    self.saturn=False
    self.sky = pygame.image.load('sky (2).gif')
    initplanetlocation(self)
    

def initplanetlocation(self):
    self.mars_x=170
    self.mars_y=160
    self.mars_r=70
    self.earth_x=320
    self.earth_y=340
    self.earth_r=70
    self.jupiter_x=550
    self.jupiter_y=340
    self.jupiter_r=80
    self.saturn_x=640
    self.saturn_y=80
    self.saturn_r=80
    self.merc_x=100
    self.merc_y=470
    self.venus_x=60
    self.venus_y=350
    self.nept_x=770
    self.nept_y=40
    self.uran_x=780
    self.uran_y=200
    self.player_y = 540
    self.player_x=480
