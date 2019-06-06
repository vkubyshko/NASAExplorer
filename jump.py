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


def jump(self):
    change = (self.currighthip_y-self.prevrighthip_y) + (self.curlefthip_y-self.prevlefthip_y)
    if change >=0.1 and self.newjump:
        print('jumped!') 
        self.jump = 32
        self.newjump = False
    if change <0:
        self.newjump=True
    self.prevrighthip_y = self.currighthip_y
    self.prevlefthip_y = self.curlefthip_y
    
def movePlayer(self):
    jump(self)
    self.player.y -= self.jump 
