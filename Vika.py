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
import mars
import saturnstart
import jupiter
import jupiter1
import jump
from startscreen import *
import solarsysteminit
class GameRuntime(object):
    def __init__(self):
        pygame.init()
        self.screen_width = 1920
        self.screen_height = 1080
        self.continu = False
        self.back = False
        self.mainpage = pygame.image.load('mainpageimage.gif')
        self.startscreen = True
        self.timemainpage = time.time()
        self.solarsystem=False
        self.gotoearth=False
        self.gotomars=False
        self.gotojup=False
        self.gotosat=False
        self.bird_height = self.screen_height/2
        self.bird_width = self.screen_width/2
        GameRuntime.initjoints(self)
        self.mars_x=0
        self.mars_y=0
        self.mars=False
        self.earth=False
        self.jupiter=False
        self.saturn=False
        self.sky = pygame.image.load('sky (2).gif')
        GameRuntime.initplanetlocation(self)
        self.arrow = pygame.image.load('arrow.gif')
        self.button = pygame.image.load('button.gif')
        self.button1 = pygame.image.load('playagainbutton.gif')
        #saturnstart.init(self)
        #solarsysteminit.init(self)

    def initjoints(self):
        self.wonEarth = False
        self.wonJupiter = False
        self.wonSaturn = False
        self.head_y = 0
        self.prev_righthand_y = 0
        self.prev_lefthand_y = 0
        self.cur_righthand_x = 0
        self.cur_righthand_y = 0
        self.cur_lefthand_x = 0
        self.cur_lefthand_y = 0
        self.righttip_x=0
        self.righttip_y=0
        self.lefttip_x = 0
        self.lefttip_y = 0
        self.hand_x=0
        self.hand_y=0
        self.righthip_x=0
        self.righthip_y=0
        self.curlefthip_x=0
        self.currighthip_x=0
        self.prevlefthip_x = 0
        self.prevrighthip_x = 0
        self.rightfist = False
        self.leftfist = False
        self.rightshoulder_y = 0
        self.leftshoulder_y = 0
        self.currighthip_y = 0
        self.curlefthip_y = 0
        self.currightknee_y = 0
        self.curleftknee_y = 0
        self.prevrighthip_y = 0
        self.prevlefthip_y = 0
        self.prevrightknee_y = 0
        self.prevleftknee_y = 0
        self.spineshoulder_x = 0
        self.spinebase_x = 0
        self.curfootright_y = 0
        self.curfootleft_y = 0
        self.prevfootright_y = 0
        self.prevfootleft_y = 0
        self.flap = 0
        self.squat = 0
        self.jump = 0

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
    
    # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        # Set the width and height of the window [width/2, height/2]
        self.screen = pygame.display.set_mode((960,540), pygame.HWSURFACE|pygame.DOUBLEBUF, 32)

        # Loop until the user clicks the close button.
        self.done = False

        # Kinect runtime object, we want color and body frames
        self.kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)

        # back buffer surface for Kinect color frames, 32bit color, width and height equal to the
        # Kinect color frame size

        self.frame_surface = pygame.Surface((self.kinect.color_frame_desc.Width, self.kinect.color_frame_desc.Height), 0, 32)

        # here we will store skeleton data

        self.bodies = None


    def draw_bird(self):
        #pygame.draw.circle(self.frame_surface, (200,200,0), (int(self.screen_width/2), \
            #int(self.screen_height - self.bird_height)), 40)
        pygame.draw.circle(self.frame_surface, (200,200,0), (int(self.screen_width - self.bird_width), int(self.screen_height - self.bird_height)), 40)
        pygame.draw.circle(self.frame_surface, (200,200,0), (200,20), 40)
        pygame.draw.circle(self.frame_surface, (200,200,0), (400,20), 40)
        pygame.draw.circle(self.frame_surface, (200,200,0), (600,20), 40)
        pygame.draw.circle(self.frame_surface, (200,200,0), (800,20), 40)
        pygame.draw.circle(self.frame_surface, (200,200,0), (1000,20), 40)
        pygame.draw.circle(self.frame_surface, (200,200,0), (1200,20), 40)
        pygame.draw.circle(self.frame_surface, (200,200,0), (1400,20), 40)
        pygame.draw.circle(self.frame_surface, (200,200,0), (1600,20), 40)


    def draw_rings(self):
        pygame.draw.arc(self.screen,(200,0,0),(-200,460,400,160),0,math.pi,5)
        pygame.draw.arc(self.screen,(200,0,0),(-250,380,500,320),0,math.pi,5)
        pygame.draw.arc(self.screen,(200,0,0),(-440,260,880,560),0,math.pi,5)
        pygame.draw.arc(self.screen,(200,0,0),(-560,120,1120,840),0,math.pi,5)
        pygame.draw.arc(self.screen,(200,0,0),(-600,90,1200,900),0,math.pi,5)
        pygame.draw.arc(self.screen,(200,0,0),(-920,-85,1840,1220),0,math.pi,5)
        pygame.draw.arc(self.screen,(200,0,0),(-950,-100,1900,1280),0,math.pi,5)
        pygame.draw.arc(self.screen,(200,0,0),(-1080,-190,2160,1460),0,math.pi,5)


    def startpagesurfaceDraw(self):
        #gif1 = pygame.image.load("moon.gif")
        #gif2 = pygame.image.load('solarsystem2.gif')
        gif1 = pygame.image.load('merc.gif')
        gif2 = pygame.image.load('ven.gif')
        gif7 = pygame.image.load('nept.gif')
        gif8 = pygame.image.load('uran.gif')
        if not self.mars:
            gif4 = pygame.image.load('mars.gif')
        else:
            gif4 = pygame.image.load('marsbig.gif')
        if not self.earth:
            gif3 = pygame.image.load('earth.gif')
        else:
            gif3 = pygame.image.load('bigearth.gif')
        if not self.jupiter:
            gif6 = pygame.image.load('jup.gif')
        else: gif6 = pygame.image.load('bigjup.gif')
        if not self.saturn:
            gif5 = pygame.image.load('sat.gif')
        else: gif5 = pygame.image.load('bigsat.gif')
        self.screen.blit(gif1, (self.merc_x,self.merc_y))
        self.screen.blit(gif2, (self.venus_x,self.venus_y))
        self.screen.blit(gif7, (self.nept_x,self.nept_y))
        self.screen.blit(gif8, (self.uran_x,self.uran_y))
        self.screen.blit(gif3, (self.earth_x-self.earth_r,
                                self.earth_y-self.earth_r))
        self.screen.blit(gif4, (self.mars_x-self.mars_r,
                                self.mars_y-self.mars_r))
        self.screen.blit(gif5, (self.saturn_x-self.saturn_r,
                                self.saturn_y-self.saturn_r))
        self.screen.blit(gif6, (self.jupiter_x-self.jupiter_r,
                                self.jupiter_y-self.jupiter_r))
        self.checkcollision()
        GameRuntime.draw_hand(self)

        pass


    def draw_hand(self):
        x = self.screen_width//2 +int((self.righttip_x)*900)
        y = self.screen_height//2 -int((self.righttip_y)*900)
        gif4 = pygame.image.load('hand.gif')
        self.screen.blit(gif4,(self.hand_x,self.hand_y))
        

    def draw_color_frame(self, frame, target_surface):
        target_surface.lock()
        address = self.kinect.surface_as_array(target_surface.get_buffer())
        ctypes.memmove(address, frame.ctypes.data, frame.size)
        del address
        target_surface.unlock()

    def checkcollision(self):
        dist = ((self.hand_x-self.mars_x)**2+
                 (self.hand_y-self.mars_y)**2)**0.5
        if dist<=self.mars_r and self.wonJupiter and self.wonSaturn and self.wonEarth: 
            if self.mars==False:
                self.time_start=time.time()
            time_now = time.time()
            if time_now-self.time_start>=3:
                self.solarsystem=False
                self.gotomars=True
                mars.init(self)
            self.mars=True
            self.mars_r=90
            
        else: 
            self.mars=False
            self.mars_r=70
        dist = ((self.hand_x-self.jupiter_x)**2+(self.hand_y-self.jupiter_y)**2)**0.5
        if dist<=self.jupiter_r: 
            if self.jupiter==False:
                self.time_start=time.time()
            time_now = time.time()
            if time_now-self.time_start>=3:
                self.solarsystem=False
                self.gotojup=True
                jupiter.init(self)
            self.jupiter=True
            self.jupiter_r=100
        else: 
            self.jupiter=False
            self.jupiter_r=80
        dist = ((self.hand_x-self.saturn_x)**2+
                (self.hand_y-self.saturn_y)**2)**0.5
        if dist<=self.saturn_r: 
            if self.saturn==False:
                self.time_start=time.time()
            time_now = time.time()
            if time_now-self.time_start>=3:
                self.solarsystem=False
                self.gotosat=True
                saturnstart.init(self)
            self.saturn_r=100
            self.saturn=True

        else: 
            self.saturn=False
            self.saturn_r=80
        dist = ((self.hand_x-self.earth_x)**2+
                (self.hand_y-self.earth_y)**2)**0.5
        if dist<=self.earth_r:  
            if self.earth==False:
                self.time_start=time.time()
            time_now = time.time()
            if time_now-self.time_start>=3:
                self.solarsystem=False
                moonpage1.mooninit(self)
                self.gotoearth=True
            self.earth=True
            self.earth_r=90
        else: 
            self.earth=False
            self.earth_r=70


    def run(self):
        # -------- Main Program Loop -----------
        while not self.done:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self.done = True # Flag that we are done so we exit this loop
            # We have a color frame. Fill out back buffer surface with frame's data
            if self.kinect.has_new_color_frame():
                frame = self.kinect.get_last_color_frame()
                self.draw_color_frame(frame, self.frame_surface)
                frame = None
            # We have a body frame, so can get skeletons
            if self.kinect.has_new_body_frame():
                self.bodies = self.kinect.get_last_body_frame()
                if self.bodies is not None:
                    for i in range(0, self.kinect.max_body_count):
                        body = self.bodies.bodies[i]
                        if not body.is_tracked:
                            continue

                        joints = body.joints
                        # save the hand positions
                        if joints[PyKinectV2.JointType_HandRight].TrackingState != PyKinectV2.TrackingState_NotTracked:
                            self.cur_righthand_y = joints[PyKinectV2.JointType_HandRight].Position.y
                            self.cur_righthand_x = joints[PyKinectV2.JointType_HandRight].Position.x
                        if joints[PyKinectV2.JointType_HandLeft].TrackingState != PyKinectV2.TrackingState_NotTracked:
                            self.cur_lefthand_y = joints[PyKinectV2.JointType_HandLeft].Position.y
                            self.cur_lefthand_x = joints[PyKinectV2.JointType_HandLeft].Position.x
                        if joints[PyKinectV2.JointType_HandTipRight].TrackingState!=PyKinectV2.TrackingState_NotTracked:
                            self.righttip_x = joints[PyKinectV2.JointType_HandTipRight].Position.x
                            self.righttip_y = joints[PyKinectV2.JointType_HandTipRight].Position.y
                        if joints[PyKinectV2.JointType_HandTipLeft].TrackingState!=PyKinectV2.TrackingState_NotTracked:
                            self.lefttip_x = joints[PyKinectV2.JointType_HandTipLeft].Position.x
                            self.lefttip_y = joints[PyKinectV2.JointType_HandTipLeft].Position.y
                        if joints[PyKinectV2.JointType_ShoulderLeft].TrackingState!=PyKinectV2.TrackingState_NotTracked:
                            self.leftshoulder_y = joints[PyKinectV2.JointType_ShoulderLeft].Position.y
                        if joints[PyKinectV2.JointType_ShoulderRight].TrackingState!=PyKinectV2.TrackingState_NotTracked:
                            self.rightshoulder_y = joints[PyKinectV2.JointType_ShoulderRight].Position.y
                        if joints[PyKinectV2.JointType_HipLeft].TrackingState!=PyKinectV2.TrackingState_NotTracked:
                            self.curlefthip_y = joints[PyKinectV2.JointType_HipLeft].Position.y
                            self.curlefthip_x = joints[PyKinectV2.JointType_HipLeft].Position.x
                        if joints[PyKinectV2.JointType_HipRight].TrackingState!=PyKinectV2.TrackingState_NotTracked:
                            self.currighthip_y = joints[PyKinectV2.JointType_HipRight].Position.y
                            self.currighthip_x = joints[PyKinectV2.JointType_HipRight].Position.x
                        if joints[PyKinectV2.JointType_KneeRight].TrackingState!=PyKinectV2.TrackingState_NotTracked:
                            self.currightknee_y = joints[PyKinectV2.JointType_KneeRight].Position.y
                        if joints[PyKinectV2.JointType_KneeLeft].TrackingState!=PyKinectV2.TrackingState_NotTracked:
                            self.curleftknee_y = joints[PyKinectV2.JointType_KneeLeft].Position.y

                        if joints[PyKinectV2.JointType_SpineBase].TrackingState!=PyKinectV2.TrackingState_NotTracked:
                            self.spinebase_x = joints[PyKinectV2.JointType_SpineBase].Position.x
                        if joints[PyKinectV2.JointType_SpineShoulder].TrackingState!=PyKinectV2.TrackingState_NotTracked:
                            self.spineshoulder_x = joints[PyKinectV2.JointType_SpineShoulder].Position.x
                        if joints[PyKinectV2.JointType_FootLeft].TrackingState!=PyKinectV2.TrackingState_NotTracked:
                            self.curfootleft_y = joints[PyKinectV2.JointType_FootLeft].Position.y
                        if joints[PyKinectV2.JointType_FootRight].TrackingState!=PyKinectV2.TrackingState_NotTracked:
                            self.curfootright_y = joints[PyKinectV2.JointType_FootRight].Position.y

                        if joints[PyKinectV2.JointType_Head].TrackingState!=PyKinectV2.TrackingState_NotTracked:
                            self.head_y = joints[PyKinectV2.JointType_Head].Position.y
                       
            
            #if want to calc flap
            #extras.flap(self)
                                  

            # --- Game logic
            #if want a bird
            #extras.bird(self)
            #create bounds for width
            extras.movehand(self)
            # Draw graphics
            
            #self.draw_bird()
            #self.draw_hand()
            self.draw_rings()
            #jump.movePlayer(self)

            # Optional debugging text
            #font = pygame.font.Font(None, 36)
            #text = font.render(str(self.flap), 1, (0, 0, 0))
            #self.frame_surface.blit(text, (100,100))
            # --- copy back buffer surface pixels to the screen, resize it if needed and keep aspect ratio
            # --- (screen size may be different from Kine ct's color frame size)
            h_to_w = float(self.frame_surface.get_height()) / self.frame_surface.get_width()
            target_height = int(h_to_w * self.screen.get_width())
            surface_to_draw = pygame.transform.scale(self.frame_surface, (self.screen.get_width(), target_height));
            self.screen.blit(surface_to_draw, (0,0))
            if self.startscreen:
                self.screen.blit(self.mainpage,(0,-80))
                if (time.time()-self.timemainpage)>=5:
                    self.startscreen = False
                    self.solarsystem = True
            
            if self.solarsystem:
                self.screen.blit(self.sky,(0,0))
                self.draw_rings() 
                self.startpagesurfaceDraw()
                self.draw_hand()
            
            if self.gotoearth:
                moonpage1.start(self)
            if self.gotojup:
                jupiter.start(self)
            if self.gotosat:
                saturnstart.start(self)
            if self.gotomars:
                mars.mars(self)

            surface_to_draw = None
            pygame.display.update()

            # --- Limit to 60 frames per second
            self.clock.tick(60)

        # Close our Kinect sensor, close the window and quit.
        self.kinect.close()
        pygame.quit()

game = GameRuntime();
game.run();

#def runFile(self):
#   __main__ = "Kinect Screen"
#game = GameRuntime()
#game.run()
