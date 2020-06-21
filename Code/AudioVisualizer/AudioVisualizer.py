# Visualizes the rendered audio using Dynamic FFT 
# We use a 31-band visualizer, though the last two frequency bands are not shown
# The audio file is rendered in AudioRender.py

import pygame
from pygame import mixer
import AudioRender as Audio
import time
import numpy as np
import sys
 
class Renderer():
    def __init__(self,resolution=(800,720),fps=60):
        M = 2048 # Slice size

        # Load the song
        songName = "backstage.wav"
        song = Audio.Audio_fft(songName,True, M=M)
        
        # Initialize the visualizer
        pygame.init()
        pygame.mixer.music.load(songName)
        pygame.mixer.music.play(0)

        clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(resolution)
        self.screen.fill(pygame.Color('white'))
         
        # Close the program if the user clicks the close button
        done = False
        while not done:
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
            except:
                break
                
                
            # Titles on the screen
            FrequencyTitle = pygame.font.Font(None, 30).render("Frequency Spectrum of the Song", True, pygame.Color('black'))
            TimeTitle = pygame.font.Font(None, 30).render("Song Frequency", True, pygame.Color('black'))
            
            self.screen.blit(FrequencyTitle, (260, 320))
            self.screen.blit(TimeTitle, (320, 690))


            # Update the screen 
            pygame.display.flip()
            clock.tick(60)

    def draw_fourier(self,data):
        # Draw the 29 frequency bands

        
        # Draw the box
        pygame.draw.rect(self.screen,(255,255,255),(10,10,780,300))
        pygame.draw.rect(self.screen,(0,0,0),(10,10,780,300),2)
        
        for i in range(0,29):
            if(data[i] >= 0):
                pygame.draw.rect(self.screen,(0,0,0),(9+10+26.5*i,310-2,20,-0.6*295*data[i]))
    
    def draw_raw(self, data):
        # Draw the raw music frequency

        pygame.draw.rect(self.screen,(255,255,255),(144,370,512,300))
        pygame.draw.rect(self.screen,(0,0,0),(144,370,512,300),2)
        
        dat = np.array(data)
        
        avg = np.mean(dat.reshape(-1, 4), axis=1)
        avg /= 2**15
        
        for i in range(len(avg)):
            pygame.draw.rect(self.screen,(0,0,0),(144+i,525,2.75,-0.8*150*avg[i]))

app = Renderer(fps=30)
