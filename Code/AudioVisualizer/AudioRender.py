# Render the audio of the wav file
# The rendered audio is then visualized in AudioVisualizer.py

import numpy as np
from scipy.fftpack import fft
from pydub import AudioSegment

class Audio_fft():
    def __init__(self, filename,M=2048,group_num=16):
        self.song = AudioSegment.from_file(filename)
        
        self.rate = self.song.frame_rate
        
        self.M = M
        self.max_amp_raw = self.song.max_possible_amplitude
        self.max_amp = 2**(np.log2(self.max_amp_raw)*1.10)
        
        self.num_groups = group_num
        self.groups = self.gen_groups(group_num)        
        
    def gen_groups(self,num_groups):
        step_size = 1/num_groups
        out = []
        for i in range(num_groups):
            out.append(15.877*np.exp(i*step_size*7.1274))
        return out
                
    def get_fft(self,slice_num, group_num=16, get_freq_space=False,
                grouped=True,localAvg=False):
        
        song_slice = self.song.get_sample_slice(slice_num[0],slice_num[1]).get_array_of_samples()
        spectrum = fft(song_slice)

        # Remove the second half, since the FFT of real frequencies is symmetric
        spectrum = np.abs(spectrum)[:self.M//2]  

        self.freq_space = (self.rate / self.M/2)
        
        # Return not grouped fft
        if not grouped:
            return spectrum

        # Split array
        pos = 0
        separated_arrs = [0]*self.num_groups
        
        for i in range(self.M//2):
            if(self.groups[pos] <= (i+1)*self.freq_space):
                pos += 1
            separated_arrs[pos] += spectrum[i]

           
        if not localAvg:
            separated_arrs = np.nan_to_num(np.array(separated_arrs))
            return separated_arrs / (self.max_amp)
             
        
        # Workout averages
        means = []
        for i in separated_arrs:
            means.append(np.mean(i))  
            
        # Scale means
        means = np.nan_to_num(np.array(means))
        means /= (means).max()
        return means
    

    def get_freq_array(self):
        freq_space = (self.rate / self.M/2)
        return np.linspace(0,self.M*(freq_space+0.1),self.M/2)
    
    
    def get_wave(self,slice_num):
        return self.song.get_sample_slice(slice_num[0],slice_num[1]).get_array_of_samples()
    
