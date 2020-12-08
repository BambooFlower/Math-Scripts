# Generate a simple harmony wav audio file
# This generated wav file can be used for audio visualization

import numpy as np
from scipy.io.wavfile import write

data = []
rate = 44100
notes = [261.626,293.665,329.628,349.228,391.995,440.000,493.883,523.251]

def add_chord(notes_,dur):
    for i in range(round(rate*dur)):
        tmp = 0
        for note in notes_:
            freq = notes[note]
            tmp += np.math.sin(freq*i/rate*np.math.pi*2)
        data.append(tmp)

add_chord([0],0.2)
add_chord([1],0.2)
add_chord([2],0.2)
add_chord([3],0.2)
add_chord([4],0.2)
add_chord([5],0.2)
add_chord([6],0.2)
add_chord([7,0,2,4],1)


scaled = np.int16(data/np.max(np.abs(data)) * 32767)
write('SimpleScale.wav', 44100, scaled)