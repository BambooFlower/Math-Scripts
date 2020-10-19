# Generate a simple harmony wav audio file
# This generated wav file can be used for audio visualization

import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

data = []
rate = 44100
notes = [261.626,293.665,329.628,349.228,391.995,440.000,493.883,523.251]

def add_note(note,dur):
# Note maker
    freq = notes[note]
    for i in range(0,round(rate*dur)):
        data.append(np.math.sin(freq*i/rate*np.math.pi*2))
    
add_note(0,1)
add_note(1,1)
add_note(2,1)
add_note(3,1)
add_note(4,1)
add_note(5,1)
add_note(6,1)
add_note(7,1)


scaled = np.int16(data/np.max(np.abs(data)) * 32767)
write('SimpleHarmony.wav', 44100, scaled)