# Lunar Orbit

import math
import numpy
import matplotlib.pyplot

moon_distance = 384e6 # in meters

def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])
    
    for i in range(num_steps +1):
        # Convert the angle in radians and then comput the orbit 
        angle = 2. * math.pi * i/num_steps
        x[i, 0] = moon_distance * math.cos(angle)
        x[i, 1] = moon_distance * math.sin(angle)

    return x

x = orbit()

matplotlib.pyplot.axis('equal')
matplotlib.pyplot.title('Circular Orbit')
matplotlib.pyplot.plot(x[:, 0], x[:, 1])
axes = matplotlib.pyplot.gca()
axes.set_xlabel('Longitudinal position in meters')
axes.set_ylabel('Lateral position in meters')
matplotlib.pyplot.show()
    

