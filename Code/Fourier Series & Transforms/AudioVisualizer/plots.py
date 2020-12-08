#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import matplotlib.pyplot as plt
# import numpy as np


# def plot_sine():
#     # x = np.linspace(-3*np.pi,3*np.pi,100)
#     x = np.linspace(0,10,100)
#     A = 2
#     L = 2*np.pi
#     F = 3
#     R = 10
#     y = A*np.sin(x*L*F/R)
#     plt.plot(x,y)
#     plt.ylabel('sin(x)')
#     plt.xlabel('x')
#     plt.title('Sine wave')
#     plt.show()

# def d(x,a=0.005):
#     return 1/(np.abs(a)*np.sqrt(np.pi))*np.exp(-(x/a)**2)
# def f(t):
#     #return np.cos(2*np.pi*3*t)*np.exp(-np.pi*t**2)#np.cos(2*np.pi*2*t)+np.cos(2*np.pi*3*t)
#     return np.cos(2*np.pi*2*t)+np.cos(2*np.pi*3*t)
    
# x = np.linspace(-2,2,10000)
# y = f(x)
# plt.plot(x,y)
# plt.xlabel('t')
# plt.ylabel('f(t)')
# plt.title('Sound Wave')

# x = np.linspace(-5,5,10000)
# #y = 0.5*(np.exp(-np.pi*(x-3)**2)+np.exp(-np.pi*(x+3)**2))
# y = d(x-2)+d(x+3)+d(x+2)+d(x-3)
# plt.plot(x,y)
# plt.ylabel('Magnitude of the Fourier Transform')
# plt.xlabel('x')
# plt.yticks([])
# plt.title('Fourier Transform')

import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from pydub import AudioSegment

# List of group frequencies
def gen_groups(num_groups):
    step_size = 1/num_groups
    out = []
    for i in range(num_groups):
        out.append(15*np.exp(i*step_size*7))
    return out

def group_data(data,num_groups):
    freq_space = (rate / M)
        
    # Split array
    pos = 0
    separated_arrs = [0]*num_groups
    
    for i in range(M//2):
        if(groups[pos] <= (i+1)*freq_space):
            pos += 1
        if pos >= len(separated_arrs):
            pos = len(separated_arrs)-1
        separated_arrs[pos] += spectrum[i]
    
    return separated_arrs

num_groups = 20
groups = gen_groups(num_groups)

song = AudioSegment.from_file('SimpleScale.wav')
song = song.set_channels(1)
rate = song.frame_rate
M = 4196
seconds = 0.3
T = 1/rate

scale = int(np.floor(rate/M*seconds))
slice_num = [M*(scale),M*(scale+1)]

song_slice = song.get_sample_slice(slice_num[0],slice_num[1]).get_array_of_samples()
spectrum = fft(song_slice)
# Remove the second half, since the FFT of real frequencies is symmetric
spectrum = 2.0/M*np.abs(spectrum)[:M//2] 

separated_arrs = group_data(spectrum,num_groups)
plt.bar(range(len(separated_arrs)),separated_arrs)
plt.title('Grouped FFT SimpleScale.wav')

# xf = np.linspace(0, 1.0/(2.0*T), M//2)
# plt.bar(xf,spectrum)
# # plt.xlim(0,2000)
# plt.xlabel('Frequency')
# plt.ylabel('Fourier Transform Magnitude')
# plt.title('FFT of Backstage.mp3 at t=0.3s')

# plt.plot(np.linspace(seconds,seconds+M*T,len(song_slice)),song_slice)
# plt.xlabel('t')
# plt.ylabel('Pressure')
# plt.title('Raw sound file values')