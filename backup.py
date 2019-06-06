from pykinect2 import PyKinectV2, PyKinectRuntime
from pykinect2.PyKinectV2 import *

#from moonpage import *
import ctypes
import _ctypes
import pygame
import sys
import math

#from startscreen import *

class GameRuntime(object):
    def __init__(self):
        pygame.init()
        self.screen_width = 1920
        self.screen_height = 1080
        self.bird_height = self.screen_height/2
        self.bird_width = self.screen_width/2
        GameRuntime.initjoints(self)
        self.mars_x=0
        self.mars_y=0
        self.mars=False
        self.earth=False
        self.jupiter=False
        self.saturn=False
        GameRuntime.initplanetlocation(self)

    def initjoints(self):
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
        self.rightfist = False
        self.leftfist = False
        self.rightshoulder_y = 0
        self.leftshoulder_y = 0
        self.flap = 0

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
        #arc(Surface, color, Rect, start_angle, stop_angle, width=1)
        radius=200
        rect = (-r,self.screen_height-r,radius*2,radius*4)
        pygame.draw.arc(self.frame_surface,(200,0,0),rect,0,math.pi/2)
        pass

    def surfaceDraw(self):
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
        
        gif4 = pygame.image.load('hand.gif')
        print(self.hand_x,self.hand_y)
        self.screen.blit(gif4,(self.hand_x,self.hand_y))
        pass

    def draw():
        pass


    def draw_hand(self):
        self.checkcollision()
        x = self.screen_width//2 +int((self.righttip_x)*900)
        y = self.screen_height//2 -int((self.righttip_y)*900)
        #print(x,y)
        pygame.draw.circle(self.frame_surface,(200,0,0), (x,y),40)
        #asurf = pygame.image.load(os.path.join('data', 'bla.png'))
        #gif1 = pygame.image.load("moon.gif")
        #pygame.draw

    def draw_color_frame(self, frame, target_surface):
        target_surface.lock()
        address = self.kinect.surface_as_array(target_surface.get_buffer())
        ctypes.memmove(address, frame.ctypes.data, frame.size)
        del address
        target_surface.unlock()

    def checkcollision(self):
        dist = ((self.hand_x-self.mars_x)**2+
                 (self.hand_y-self.mars_y)**2)**0.5
        if dist<=self.mars_r: 
            self.mars=True
            self.mars_r=90
        else: 
            self.mars=False
            self.mars_r=70
        dist = ((self.hand_x-self.jupiter_x)**2+(self.hand_y-self.jupiter_y)**2)**0.5
        if dist<=self.jupiter_r: 
            self.jupiter=True
            self.jupiter_r=100
        else: 
            self.jupiter=False
            self.jupiter_r=80
        dist = ((self.hand_x-self.saturn_x)**2+
                (self.hand_y-self.saturn_y)**2)**0.5
        if dist<=self.saturn_r: 
            self.saturn_r=100
            self.saturn=True
        else: 
            self.saturn=False
            self.saturn_r=80
        dist = ((self.hand_x-self.earth_x)**2+
                (self.hand_y-self.earth_y)**2)**0.5
        if dist<=self.earth_r: 
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
            
            #calculate flap
            self.flap = (self.prev_lefthand_y -
                         self.cur_lefthand_y)+ \
                        (self.prev_righthand_y -
                         self.cur_righthand_y)
            if math.isnan(self.flap) or self.flap<0:
                self.flap = 0

            #cycle out prev w curr
            self.prev_lefthand_y=self.cur_lefthand_y
            self.prev_righthand_y=self.cur_righthand_y
                                  

            # --- Game logic
            #gravity
            self.bird_height -= 3
            #self.bird_height += self.jump * 250
            if self.bird_height <= 0:
                # Don't let the bird fall off the bottom of the screen
                self.bird_height = 0
            if self.bird_height >= self.screen_height:
                # Don't let the bird fly off the top of the screen
                self.bird_height = self.screen_height
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
            #create bounds for width
                
            # Draw graphics
            
            #self.draw_bird()
            #self.draw_hand()

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
            self.surfaceDraw()
            self.draw_hand()

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