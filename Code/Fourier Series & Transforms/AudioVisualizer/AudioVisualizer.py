# Visualizes the rendered audio using Dynamic FFT 
# We use a 31-band visualizer, though the last two frequency bands are not shown
# The audio file is rendered in AudioRender.py

import pygame
from pygame import mixer

import AudioRender as Audio
import time
import numpy as np
import math
import random
from Interpolate import Polynomial

class Bar():
    def __init__(self,num):
        self.num = None
        self.x = None
        self.y = None
        self.theta = None
        
        # Centered coordinate
        self.c_x = None
        self.c_y = None
        
        self.height = None
        self.width = None
        self.colour = None
        
class Bars_window():
    # This class holds the main surface of the 
    def __init__(self):
        pass
 
class Renderer():
    def __init__(self,resolution=(900,720),fps=60,jump_fps=15):
        self.screen_size = resolution
        self.interpolate = Polynomial(steps=jump_fps,n=1)
        self.fps = fps
        self.jump_fps = jump_fps
        self.M = 1024  # Slice size

        # Load the song
        songName = "backstage.mp3"
        
        # Number of FFT bar groups
        self.num_groups = 100
        self.N = self.num_groups 
        self.bars = self.gen_bars()
        self.calc_screen()
        self.song = Audio.Audio_fft(songName, M=self.M,group_num=self.num_groups)
        
        self.max_amp = self.song.max_amp
        self.max_amp_raw = self.song.max_amp_raw

        # Initalise visualiser
        pygame.init()        
        # Initialize mixer
        pygame.mixer.quit()
        pygame.mixer.init(frequency=self.song.rate)
        pygame.mixer.music.load(songName)
        pygame.mixer.music.play(0)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.main_loop()

    def gen_bars(self):
        # Calculate positions of each bar
        # So that I only need to calculate the colour in the main loop
        # and the height
        s_width,s_height = self.screen_size
        
        left_top = (10,10)

        box_width = 2
        fourier_height = 300
        fourier_width = s_width - 2*left_top[0] - box_width//2
        
        width_height = (fourier_width,fourier_height)
        bar_spacing = 1                
    
        bar_w = (fourier_width-(self.N+2)*bar_spacing)/(self.N-1)
        bars = []
        floor_x = left_top[1]+width_height[1]-box_width//2
        for i in range(1,self.N):
            b = Bar(i)
            b.x = math.floor(left_top[0]+box_width+i*bar_spacing+(i-1)*(bar_w))
            b.y = floor_x
            b.width = math.floor(bar_w)
            bars.append(b)
        return bars
    
    def main_loop(self):
        # Close the program if the user clicks the close button
        done = False
        frame_count = 0
        
        prev_seconds = 0
        prev_ccc = np.array([[[0,0,0] for j in range(self.jump_fps-1)] for i in range(1,self.N)])
        shift = 0

        while not done:
            frame_count += 1
            self.screen.fill(pygame.Color('white'))
            
            song_time = pygame.mixer.music.get_pos()

            for event in pygame.event.get():   
                if(event.type == 2):
                    mixer.pause()
                    time.sleep(2)
                    mixer.unpause()
                if event.type == pygame.QUIT:  
                    done = True   
              
            seconds = song_time/1000
            
            try:                    
                if frame_count == 1:
                    scale = int(np.floor(self.song.rate/self.M*seconds))
                    #print(prev_seconds,seconds)
                    prev_scale = int(np.floor(self.song.rate/self.M*(prev_seconds)))
                    slice_num = [self.M*(scale),self.M*(scale+1)]
                    prev_slice = [self.M*(prev_scale),self.M*(prev_scale+1)]

                    shift += random.randint(-1,1)
                    curr_fft = self.song.get_fft(slice_num,grouped=True,localAvg=False)
                    prev_fft = self.song.get_fft(prev_slice,grouped=True,localAvg=False)
                    inner_vals = self.interpolate.calc(prev_fft,curr_fft)
                    prev_seconds = seconds
                    ccc=[]
                    for i in range(1,self.N):
                        tmp_h_curr = curr_fft[i]
                        if tmp_h_curr > self.width_height[1] - self.left_top[0]//2:
                            tmp_h_curr = self.width_height[1] - self.left_top[0]//2

                        # print(tmp_h_curr,tmp_h_prev)
                        if tmp_h_curr > 0:
                            v = (tmp_h_curr/(self.width_height[1]-self.left_top[0]//2))*15
                        else:
                            v = 0
                        if v > 1:
                            v = 1
                        tmp_rgb = self.hsv_to_rgb((shift + i)%self.N/(self.N),0.5,v)
                        tmp_vals = self.interpolate.calc(prev_ccc[i-1][-1],
                                                         tmp_rgb)
                        ccc.append(tmp_vals)
                    prev_ccc = ccc
            except ValueError:
                break
            
            # Set colour for each bar
            for i in range(1,self.N):
                self.bars[i-1].colour = prev_ccc[i-1][frame_count-1]
            
                
            self.draw_fourier(inner_vals[frame_count-1])
            self.draw_raw(self.song.get_wave(slice_num))
            # Titles on the screen
            FrequencyTitle = pygame.font.Font(None, 30).render("Frequency Spectrum of the Song", True, pygame.Color('black'))
            TimeTitle = pygame.font.Font(None, 30).render("Song Frequency", True, pygame.Color('black'))
            
            self.screen.blit(FrequencyTitle, (260, 320))
            self.screen.blit(TimeTitle, (320, 690))

            # Update the screen 
            pygame.display.flip()
            self.clock.tick(self.fps)
            if frame_count == self.jump_fps:
                frame_count = 0
        pygame.quit()
        
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
        
    def calc_screen(self):
        s_width,s_height = self.screen_size
        
        self.left_top = (10,10)

        box_width = 2
        fourier_height = 300
        fourier_width = s_width - 2*self.left_top[0] - box_width//2
        
        self.width_height = (fourier_width,fourier_height)

    def draw_fourier(self,data,cols=None,c_colour=(20,20,20)):
        # Draw the (however many) frequency bands
        
        box_width = 2

        graph_col = (50,50,50)
                
        # Draw the box
        pygame.draw.rect(self.screen,(0,0,0),(self.left_top,self.width_height))
        pygame.draw.rect(self.screen,graph_col,(self.left_top,self.width_height),box_width)

        
        for i in range(1,self.N):
            if(data[i] >= 0):
                bar = self.bars[i-1]
                bar_h = data[i]
                bar.height = bar_h  # Update bar height

                if bar_h > self.width_height[1] - self.left_top[0]//2:
                    bar_h = self.width_height[1] - self.left_top[0]//2

                pygame.draw.rect(self.screen,bar.colour,(bar.x,
                                                      bar.y,
                                                      bar.width,
                                                      int(-bar_h))
                                 )
    
    def draw_raw(self, data):
        # Draw the raw music frequency

        left_top = (144,370)
        width_height = (512,300)

        pygame.draw.rect(self.screen,(255,255,255),(left_top,width_height))
        pygame.draw.rect(self.screen,(0,0,0),(left_top,width_height),2)
        
        dat = np.array(data)
        
        avg = np.mean(dat.reshape(-1, 4), axis=1)
        avg /= (self.max_amp_raw)
        
        num_els = len(avg)
        rec_w = int(width_height[0]/num_els)
        
        for i in range(num_els):
            pygame.draw.rect(self.screen,(0,0,0),(int(left_top[0]+i*rec_w),
                                                  int(left_top[1]+width_height[1]//2),
                                                  rec_w,
                                    int(-(width_height[1]//2)*avg[i]))
                             )

app = Renderer(fps=60,jump_fps=5)
