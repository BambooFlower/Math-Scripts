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
