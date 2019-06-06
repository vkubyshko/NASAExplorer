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
import solarsysteminit

def mars(self):
    self.screen.blit(self.gif,(0,0))
    extras.drawButton(self)

def init(self):
    self.gif = pygame.image.load('welcome to mars.gif')