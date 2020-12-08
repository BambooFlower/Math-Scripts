# Visualizes the rendered audio using Dynamic FFT 
# We use a 31-band visualizer, though the last two frequency bands are not shown
# The audio file is rendered in AudioRender.py

import pygame
from pygame import mixer
import matplotlib.pyplot as plt
import AudioRender as Audio
import time
import numpy as np
 
class Renderer():
    def __init__(self,resolution=(800,720),fps=60):
        M = 1024  # Slice size

        # Load the song
        songName = "backstage.wav"
        
        # Number of FFT bar groups
        self.num_groups = 31

        song = Audio.Audio_fft(songName, M=M,group_num=self.num_groups)
        
        self.max_amp = song.max_amp
        self.max_amp_raw = song.max_amp_raw

        # Initalise visualiser
        pygame.init()        
        # Initialize mixer
        pygame.mixer.quit()
        pygame.mixer.init(frequency=song.rate)
        pygame.mixer.music.load(songName)
        pygame.mixer.music.play(0)

        clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(resolution)
         
        # Close the program if the user clicks the close button
        done = False
        while not done:
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
                scale = int(np.floor(song.rate/M*seconds))
                slice_num = [M*(scale),M*(scale+1)]
    
                self.draw_fourier(song.get_fft(slice_num,grouped=True,localAvg=False))
                self.draw_raw(song.get_wave(slice_num))

            except ValueError:
                break
                
                
            # Titles on the screen
            FrequencyTitle = pygame.font.Font(None, 30).render("Frequency Spectrum of the Song", True, pygame.Color('black'))
            TimeTitle = pygame.font.Font(None, 30).render("Song Frequency", True, pygame.Color('black'))
            
            self.screen.blit(FrequencyTitle, (260, 320))
            self.screen.blit(TimeTitle, (320, 690))


            # Update the screen 
            pygame.display.flip()
            clock.tick(fps)

        pygame.quit()

    def draw_fourier(self,data):
        # Draw the 29 frequency bands

        left_top = (10,10)
        width_height = (784,300)

        graph_col = (50,50,50)
        
        # Draw the box
        pygame.draw.rect(self.screen,(255,255,255),(left_top,width_height))
        pygame.draw.rect(self.screen,graph_col,(left_top,width_height),2)
        
        for i in range(1,self.num_groups-1):
            if(data[i] >= 0):
                bar_h = data[i]
                bar_w = int((width_height[0])/(self.num_groups-2))
                box_x = int(left_top[0] + bar_w*i - bar_w)
                if bar_h > width_height[1] - left_top[0]//2:
                    bar_h = width_height[1] - left_top[0]//2

                pygame.draw.rect(self.screen,graph_col,(box_x,
                                                      308,   
                                                      bar_w,
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
        

        # Circular Instogram using matplotlib
        # N = 80
        # bottom = 8
        # max_height = 4
        # theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
        # radii = max_height*np.random.rand(N)
        # width = (2*np.pi) / N

        # ax = plt.subplot(111, polar=True)
        # bars = ax.bar(theta, radii, width=width, bottom=bottom)
        # plt.show()






        for i in range(num_els):

            # Failed attemps in pygame 
            # Center of the box is given (405,520)
            # pygame.draw.circle(self.screen, (0,0,255), (400, 520), 15, 1)
            # pygame.draw.arc(self.screen, (0,0,255), (405, 520, 100*rec_w, 100), 0, 6.283, 1)
            # pygame.draw.arc(self.screen, (255,0,0), (int(left_top[0]+i*rec_w),
            #     int(left_top[1]+width_height[1]//2), rec_w, int(-(width_height[1]//2)*avg[i])),
            #         0, 6.283, 1)    # 2pi is 6.283


            pygame.draw.rect(self.screen,(0,0,0),(int(left_top[0]+i*rec_w),
                                                  int(left_top[1]+width_height[1]//2),
                                                  rec_w,
                                    int(-(width_height[1]//2)*avg[i])), 1
                             )


            

app = Renderer(fps=24)
