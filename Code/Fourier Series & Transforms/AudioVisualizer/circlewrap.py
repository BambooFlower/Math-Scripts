#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from math import cos,sin
import pygame
from Interpolate import Polynomial
import AudioRender as Audio
from pygame import gfxdraw
import random
import numpy as np

class Bar_window():
    def __init__(self,N,size):
        self.size = width,height = size
        self.N = N  # Number of bars
        self.window = pygame.Surface(self.size)
        self.bars =[]
        self.shift_1 = 0
        self.rotation_shift_1 = -1/(2*math.pi*60)
        self.rotation_shift_2 = 1/(2*math.pi*60)*0.25
        self.add_bar()
        self.add_centre()
        self.first_circle_max_height = 80
    
    def make_shift(self):
        self.shift_1 += random.randint(-1, 1)
    
    def add_rotation(self):
        for c,bar in enumerate(self.bars):
            if c < self.N:
                bar.theta += self.rotation_shift_1
            else:
                bar.theta += self.rotation_shift_2
            if bar.theta < 0:
                    bar.theta = math.pi*2
            elif bar.theta > math.pi*2:
                    bar.theta = 0
        
    
    def add_bar(self):
        width = 1
        height = 0
        
        r = 50
                
        x_1 = self.size[0]//2
        y_1 = self.size[1]//2
        
        theta_step = 2*math.pi/(self.N-1)
        
        for i in range(self.N):
            width_height = (width,height)
            
            rad = theta_step*i
            
            centre = (x_1,y_1)
            self.bars.append(Bar(self.window,
                    b_id=i,
                    theta=rad,
                    centre=centre,
                    width_height=width_height,
                    colour=(255,i*10%255,124),
                    r=r)
                    )
            
        width = 3
        height = 0
        
        r = 140
        
        x_1 = self.size[0]//2
        y_1 = self.size[1]//2
        
        theta_step = 2*math.pi/(self.N-1)
        
        for i in range(self.N):
            width_height = (width,height)
            
            rad = theta_step*i
            
            centre = (x_1,y_1)
            self.bars.append(Bar(self.window,
                    b_id=i,
                    theta=rad,
                    centre=centre,
                    width_height=width_height,
                    colour=(255,i*10%255,124),
                    r=r)
                    )
                
    def deg_to_rad(self,deg):
        return 2*math.pi*deg/360
    
    def add_centre(self):
        c_coord = x_c,y_c = (self.size[0]//2,self.size[1]//2)
        self.centre_dot = pygame.Surface((2,2))
        self.centre_dot.fill((255,255,255))
        rect = self.centre_dot.get_rect()
        rect.center = c_coord
        self.window.blit(self.centre_dot,rect)
        
    def update_bars(self,heights,colours):
        self.window.fill((0,0,0))  # Draw background
        # Update first circle
        for c,b in enumerate(self.bars):         
            if c < self.N:
                tmp_height = 0.5*heights[c-1]
                if tmp_height > self.first_circle_max_height:
                    tmp_height = self.first_circle_max_height
                b.update_bar(tmp_height,colours[c-1])
            elif c > self.N:
                tmp_pos = c-self.N-1
                b.update_bar(2*heights[tmp_pos-1],colours[tmp_pos-1])
    
class Bar():
    def __init__(self,surface,centre,b_id,width_height,r,colour,theta=0,plot_type='circle'):
        BLACK = (0,0,0)
        # GREEN = (0,255,0)
        self.b_id = b_id
        self.surface = surface
        self.colour = colour
        self.bg_col = BLACK
        self.width,self.height = width_height
        self.center = centre
        self.theta = theta
        self.r = r
        self.plot_type = plot_type
        
        self.rect = self.surface.get_rect()
                
        self.calc_aa_rect()
    
    def update_bar(self,height,colour):
        self.height = height
        self.colour = colour
        if self.plot_type == 'circle':
            self.calc_aa_rect()
    
    def calc_aa_rect(self):
        # https://stackoverflow.com/questions/30578068/pygame-draw-anti-aliased-thick-line
        # P2----P3
        # |     |
        # P1----P4
        # https://en.wikipedia.org/wiki/Rotation_matrix
        
        # Might be possible to make this faster 
        
        # Precompute things                
        ct = cos(self.theta)
        st = sin(self.theta)
        
        pre1 = self.height+self.r
        pre2 = self.width-self.width
        
        pre3 = self.center[0]+ct*self.width
        pre4 = self.center[1]+st*self.width
        
        pre5 = self.center[0]+ct*pre2
        pre6 = self.center[1]+st*pre2
        
        pre7 = st*self.r
        pre8 = ct*self.r
        
        pre9 = st*pre1
        pre10 = ct*pre1
        
        P1 = (pre3-pre7,
              pre4+pre8)
        
        P2 = (pre3-pre9,
              pre4+pre10)
        
        P3 = (pre5-pre9,
              pre6+pre10)
        
        P4 = (pre5-pre7,
              pre6+pre8)
        
        gfxdraw.aapolygon(self.surface, (P1, P2, P3, P4), self.colour)
        gfxdraw.filled_polygon(self.surface, (P1, P2, P3, P4), self.colour)
        
class JukeBox():
    def __init__(self,fps=60,jump_fps=15,n_groups=10):
        self.interpolate = Polynomial(steps=jump_fps,n=1)
        self.fps = fps
        self.jump_fps = jump_fps
        self.M = 1024  # Slice size
        
        self.prev_seconds = 0

        # Load the song
        songName = "backstage.mp3"
        
        # Number of FFT bar groups
        self.num_groups = n_groups
        self.N = self.num_groups 
        self.song = Audio.Audio_fft(songName, M=self.M,group_num=self.num_groups)
        
        self.max_amp = self.song.max_amp
        self.max_amp_raw = self.song.max_amp_raw

        # Initialize mixer
        pygame.mixer.quit()
        pygame.mixer.init(frequency=self.song.rate)
        pygame.mixer.music.load(songName)
    
    def start(self):
        pygame.mixer.music.play(0)
    
class Renderer():
    def __init__(self,screen_size,n_bars,fps,jump_fps,degree=1):
        self.J = JukeBox(fps,jump_fps,n_bars)
        self.interpolate = Polynomial(steps=jump_fps,n=degree)
        self.screen_size = screen_size
        self.n_bars = n_bars
        self.fps = fps
        self.jump_fps = jump_fps
                
        self.inner_vals = []
        self.ccc = []
        self.prev_ccc = np.array([[[0,0,0] for j in range(self.jump_fps-1)] for i in range(1,self.n_bars)])
        
        self.first_circle_max_height = 80
        
        
        # Initalise visualiser
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.visual = Bar_window(self.n_bars,self.screen_size)
        self.blit_list = []
        self.bg_exists = False
        self.main_loop()
        
    def draw_bar_window(self):
        tmp = self.screen.blit(self.visual.window,(0,0))
        self.blit_list.append(tmp)
    
    def draw_background(self):
        if not self.bg_exists:
            self.blit_list.append(self.screen.fill(pygame.Color('white')))
            self.bg_exists = False
    
    def update_all(self):
        for el in self.blit_list:
            pygame.display.update(el)
        self.blit_list = []
        
    def render_box_frame(self,frame):
        if frame > 0:
            # print(frame,self.prev_ccc,self.inner_vals)
            colours = []
            heights = []

            for i in range(1,self.n_bars):
                # self.bars[i-1].colour = prev_ccc[i-1][frame_count-1]
                colours.append(self.prev_ccc[i-1][frame])
                tmp_h_curr = self.inner_vals[frame][i]
                # if tmp_h_curr > self.first_circle_max_height:
                #     tmp_h_curr = self.first_circle_max_height                
                heights.append(tmp_h_curr)
                pass
            self.visual.update_bars(
                                    # [random.randint(1,50) for i in range(self.n_bars*2)],
                                    heights,
                                    colours
                                    # [
                                    #     [random.randint(0, 255),
                                    #      random.randint(0, 255),
                                    #      random.randint(0, 255)] for i in range(self.n_bars*2)
                                    # ]
                                    )
            self.blit_list.append(self.visual.window.get_rect())
        else:
            pass
    
    def calc_fft(self):
        song_time = pygame.mixer.music.get_pos()
        seconds = song_time/1000
        
        try:        
            scale = int(np.floor(self.J.song.rate/self.J.M*seconds))
            # #print(prev_seconds,seconds)
            prev_scale = int(np.floor(self.J.song.rate/self.J.M*(self.J.prev_seconds)))
            slice_num = [self.J.M*(scale),self.J.M*(scale+1)]
            # #next_slice = [M*(next_scale),M*(next_scale+1)]
            prev_slice = [self.J.M*(prev_scale),self.J.M*(prev_scale+1)]
    
            # shift += random.randint(-1,1) ## Move it elsewhere
            curr_fft = self.J.song.get_fft(slice_num,grouped=True,localAvg=False)
            prev_fft = self.J.song.get_fft(prev_slice,grouped=True,localAvg=False)
            # #print(curr_fft[-1],next_fft[-1])
            self.inner_vals = self.interpolate.calc(prev_fft,curr_fft)
            self.J.prev_seconds = seconds
            self.ccc=[]
            for i in range(1,self.n_bars):
                tmp_h_curr = curr_fft[i]
                if tmp_h_curr > self.first_circle_max_height:
                    tmp_h_curr = self.first_circle_max_height
            #     # print(tmp_h_curr,tmp_h_prev)
                if tmp_h_curr > 0:
                    v = (tmp_h_curr/(self.first_circle_max_height))*15
                else:
                    v = 0
                if v > 1:
                    v = 1
                tmp_rgb = self.hsv_to_rgb((self.visual.shift_1 + i)%self.n_bars/(self.n_bars),0.5,v)
                tmp_vals = self.interpolate.calc(self.prev_ccc[i-1][-1],
                                                  tmp_rgb)
                self.ccc.append(tmp_vals)
            self.prev_ccc = self.ccc
        except ValueError:
            return False

        return True
    
    def hsv_to_rgb(self,h, s, v):
        if s == 0.0: v*=255; return (v, v, v)
        i = int(h*6.) # XXX assume int() truncates!
        f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
        if i == 0: return (v, t, p)
        if i == 1: return (q, v, p)
        if i == 2: return (p, v, t)
        if i == 3: return (p, q, v)
        if i == 4: return (t, p, v)
        if i == 5: return (v, p, q)
    
    def render_all(self,frame):
        self.draw_background()
        self.draw_bar_window()
        self.render_box_frame(frame)
        self.update_all()

    def main_loop(self):
        # Close the program if the user clicks the close button
        done = False
        frame = 0
        self.J.start()
        while not done:
            frame += 1
            
            for event in pygame.event.get():   
                if event.type == pygame.QUIT:  
                    done = True
                
            if frame == self.jump_fps:
                frame = 0
            self.visual.add_rotation()
            if frame == 1:
                self.visual.make_shift()
                if not self.calc_fft():
                    break
                
            self.render_all(frame)
            self.clock.tick(self.fps)
        pygame.quit()

class Visualiser():
    def __init__(self):
        self.fps = 60
        self.jump_fps = 5
        self.resolution = (800,700)
        self.n_bars = 100
        self.interpolation_degree = 1
        
        R = Renderer(self.resolution,self.n_bars,self.fps,self.jump_fps,degree=self.interpolation_degree)
        
v = Visualiser()
